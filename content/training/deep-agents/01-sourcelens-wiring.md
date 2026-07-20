---
title: 第 1 章 · SourceLens 是怎么用的
date: 2026-07-20T06:10:00+08:00
author: Ray Sun
tags:
  - Deep Agent
  - LangChain
  - SourceLens
  - AI
categories:
  - AI应用开发
weight: 2
---

这一章不讲理论，直接看代码。SourceLens 的 `lensnode` 服务在 `lensnode/lensnode/agent_runtime.py` 里，用 `create_deep_agent(...)` 装配出一个真正跑在生产里的 Deep Agent。我们按"装配顺序"过一遍：模型、backend、工具、middleware，最后看它们怎么被组装成一次调用。

## 自定义模型：LensGatewayChatModel

`deepagents` 的 `model` 参数接受任何 LangChain `BaseChatModel`。SourceLens 没有直接接某个厂商的 SDK，而是自己实现了一个把调用转发到内部 AI 网关的模型类，`lensnode/lensnode/gateway_model.py:55` `LensGatewayChatModel(BaseChatModel)`。

它做了几件值得注意的事：

**流式与非流式两条路径**。`_generate`（`gateway_model.py:109`）根据是否传入 `emit_output` 回调决定走 `_generate_streaming`（`gateway_model.py:160`，SSE 逐 token 转发）还是一次性 `httpx.Client().post(...)` 拿完整响应（`gateway_model.py:141-158`）。

**子代理静默**：deepagents 在跑子代理时会用 LangSmith 的 tracing context 打上 `ls_agent_type="subagent"` 元数据，`gateway_model.py:37` 的 `_in_subagent_context()` 读这个元数据，判断当前这次模型调用是不是来自子代理。如果是，`_generate_streaming` 里的 `silent` 标志（`gateway_model.py:171`）会让这次调用只收集内容，不把 token 推给 `emit_output`——避免并行跑的多个子代理把输出交错打进用户看到的答案气泡里。

**usage/耗时回写**：每次调用完，`response_metadata["usage"]` 和 `["latency_ms"]` 会被塞进返回的 `AIMessage`（例如 `gateway_model.py:151-154`），后面 `agent_runtime.py` 的 `_emit_new_model_calls`（第 899 行）会从这里把 `prompt_tokens`/`completion_tokens`/`cost` 读出来上报到运行轨迹里，每一次 LLM 往返都在追踪面板里可见。

有一个细节会在第 2 章反复用到：`_message_from_gateway`（`gateway_model.py:310`）构造 `AIMessage` 时**只**设置了 `response_metadata["usage"]`，没有设置 LangChain 标准的 `usage_metadata` 字段。这个差异不是笔误，它直接决定了 LangChain 摘要中间件的一个行为分支——具体影响放到第 2 章讲。

## Backend：FilesystemBackend 作为虚拟 scratch 区

```python
"backend": FilesystemBackend(
    root_dir=str(resources.root),
    virtual_mode=True,
),
```

（`agent_runtime.py:356-359`）

`deepagents` 的内建文件工具（`ls`/`read_file`/`write_file`/`edit`/`glob`/`grep`）都是相对某个 backend 操作的。SourceLens 给每次运行分配一个私有的 `resources.root` 目录，`virtual_mode=True` 让这些工具只能在这个根目录下活动——模型看到的"文件系统"其实是这次运行专属的一块 scratch 区，运行结束即回收（`_answer_sync` 的 `finally: cleanup_runtime_resources(resources)`，`agent_runtime.py:426-427`）。

系统提示词里专门强调了这一点（`agent_runtime.py:490-498`）：内建的 `ls`/`read_file` 只能看到这个 scratch 区，**看不到**用户选中的真实工作区目录；工作区必须通过下面讲的自定义工具访问。这是个容易踩的坑——如果模型对着内建 `ls` 返回空就断言"工作区不存在"，那就是把 scratch 区的空当成了工作区的空。

## 工具：业务工具 + 内建工具 + 委派 + 规划

SourceLens 的业务工具在 `lensnode/lensnode/agent_tools.py` 里，`build_agent_tools`（第 57 行）为知识问答/代码分析场景组装出一组**只读**的工作区工具：

- `search_workspace`（`agent_tools.py:74`）—— ripgrep 风格的关键词/正则搜索，返回匹配行 + 上下文，`output_mode` 支持 `content`/`files`/`count`。
- `read_workspace_file`（`agent_tools.py:141`，用 `_ReadWorkspaceFileArgs` 兼容 `file_path`/`path` 两种参数名）—— 按 `offset`/`limit` 分页读文件窗口，文件多大都不是问题。
- `find_files`（`agent_tools.py:207`）—— 按 glob 找文件，还带了一个小体贴：非递归的 `*` 模式在只有子目录、顶层为空时会自动 retry 成 `**/*` 并在返回里注明（`agent_tools.py:232-250`）。
- `git_log` / `git_diff` / `summarize_recent_changes`（第 267、310、362 行）—— 只读 git 证据工具；`git_diff` 有调用次数预算（`git_diff_max_calls`，默认 8 次，`agent_tools.py:64-67, 333-353`），超出后返回 `TOOL_BUDGET_EXCEEDED` 提示模型停止追加调用、直接用已有证据收尾——这是防止模型在漫长 diff 历史里打转的一个简单但有效的护栏。
- `save_deliverable`（`_build_save_deliverable_tool`，`agent_tools.py:459`）—— 把 scratch 区里生成的最终产物上传给控制面，作为可下载文件交付给用户；只有调用过这个工具的文件才会离开 scratch 区。

这些是 SourceLens 自己的工具，之外还有 `deepagents` 自带的文件工具（作用域是上一节的 `FilesystemBackend`）、`task` 工具（委派子代理）、`write_todos`（任务规划，第 2 章的中间件小节会讲它属于哪个中间件）。

## 子代理：只覆写一个 general-purpose 的系统提示词

```python
"subagents": [_fast_subagent()],
```

`_fast_subagent()`（`agent_runtime.py:618-639`）没有定义一个全新的子代理，而是复用 `deepagents` 自带的 `GENERAL_PURPOSE_SUBAGENT`，只是在它的系统提示词前面拼接了一段"并行优先"的指导语。原因写在 docstring 里：默认的委派子代理倾向于串行 ReAct（一次读一个文件），而这往往是子任务慢的主因；工具和模型都继承自父 agent，唯一变的是提示词。

`_subagent_guidance`（`agent_runtime.py:642-667`）按"分析档位"（`agent_rounds`）决定要不要在主提示词里鼓励模型使用 `task` 委派：只有 `deep`/`max` 档位才建议委派，因为子代理是一次完整的 agent loop（多轮、分钟级），委派有真实成本，轻量的多文件读取直接批量并行处理更快——这个判断后面第 2 章讲"子代理隔离"时会再展开为什么委派不是免费的。

## Middleware 栈：装配顺序是确定的

`deepagents` 的 `create_deep_agent()`（容器内 `deepagents/graph.py:750-813`）内部按固定顺序组装中间件：

```text
TodoListMiddleware
  → (可选) SkillsMiddleware            仅当传入 skills
  → FilesystemMiddleware
  → (可选) SubAgentMiddleware          仅当传入 subagents
  → 内建 SummarizationMiddleware        create_summarization_middleware(model, backend)
  → PatchToolCallsMiddleware
  → (可选) AsyncSubAgentMiddleware      仅当传入 async 子代理
  → 调用方传入的 middleware（我们的 LensSummarizationMiddleware 就插在这里）
  → harness profile 的附加中间件
  → (可选) 工具排除中间件
  → AnthropicPromptCachingMiddleware   无条件添加
  → (可选) MemoryMiddleware             仅当传入 memory
  → (可选) HumanInTheLoopMiddleware     仅当传入 interrupt_on
```

这里有个容易被忽略的事实：**`create_deep_agent` 会无条件给主 agent 装一个它自己的内建 `SummarizationMiddleware`**（在调用方传入的 middleware 之前），SourceLens 通过 `kwargs["middleware"] = [summarizer]`（`agent_runtime.py:369-370`）追加的 `LensSummarizationMiddleware` 并不是替换它，而是**叠加在它后面**——一次运行里实际存在两层摘要中间件。这不是疏忽，`_build_summarization_middleware` 的 docstring（`agent_runtime.py:162-176`）写得很清楚：

> `create_deep_agent` 也会装配自己的摘要中间件（对没有 profile 信息的模型，默认触发阈值约 17 万 token）。把我们自己的阈值压得远低于这个上限，就能保证我们的中间件总是先触发、把上下文压在内建阈值之下——内建中间件因此始终保持休眠，全程只有一层摘要真正生效。**不要把 `summary_trigger_tokens` 调到接近 17 万。**

`LensGatewayChatModel` 没有向 `deepagents` 暴露任何 model profile 信息（比如 `max_input_tokens`），所以内建中间件走的正是"无 profile"分支，`170000` 这个数字是 `deepagents` 库自己算出来的默认值（详见第 2 章）。SourceLens 的整个"只让一层摘要生效"的设计，构建在这个默认值之上——这是一个跨版本可能漂移的隐式依赖，升级 `deepagents` 时值得重新核实。

## 组装现场：`_answer_sync`

把上面这些拼起来，`LensDeepAgentRuntime._answer_sync`（`agent_runtime.py:271-427`）的核心调用大致是：

```python
kwargs = {
    "model": model,                       # LensGatewayChatModel
    "tools": tools,                       # build_agent_tools(...) 或 build_general_chat_tools(...)
    "system_prompt": _system_prompt(...), # 按 knowledge_qa / code_analysis / general_chat 场景生成
    "backend": FilesystemBackend(root_dir=str(resources.root), virtual_mode=True),
    "subagents": [_fast_subagent()],
    "name": f"lensnode-{command.get('task') or 'agent'}",
}
if resources.skill_paths and not _is_general_chat(command):
    kwargs["skills"] = resources.skill_paths

summarizer = _build_summarization_middleware(self.config, model_ref, emit_agent_event, cancel_event)
if summarizer is not None:
    kwargs["middleware"] = [summarizer]

agent = create_deep_agent(**kwargs)
```

（`agent_runtime.py:348-387`，节选）

跑起来之后，`_run_agent_with_turn_limit`（`agent_runtime.py:783-858`）用 `agent.stream(..., stream_mode="values")` 消费 LangGraph 的状态流，按"新增 AI 轮次数"设一个硬性上限（`max_turns`，来自 `command.get("max_agent_turns", 26)`）——这是 `deepagents` 本身不提供的一层保护：无论摘要、卸载配得多好，一个跑飞的循环仍然需要一个"最多陪你转多少轮"的兜底。截断发生时不会返回空白，而是在已有答案后面附一句"已达到当前分析深度上限"的提示（`agent_runtime.py:846-857`）。

这就是 SourceLens 装配一个 Deep Agent 的全貌。下一章我们把镜头拉近，讲清楚这套装配里最容易搞混、也是团队真正踩过坑的几个核心概念。
