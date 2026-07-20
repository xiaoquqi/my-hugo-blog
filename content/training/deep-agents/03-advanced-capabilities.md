---
title: 第 3 章 · 我们还没用到的高级能力
date: 2026-07-20T06:30:00+08:00
author: Ray Sun
tags:
  - Deep Agent
  - LangChain
  - SourceLens
  - AI
categories:
  - AI应用开发
weight: 4
---

`deepagents 0.6.8` 提供的能力比 SourceLens 目前用到的要多。这一章过一遍库里已经有、但 `agent_runtime.py` 从未传入对应参数的几项能力——不是"你应该马上加上"，而是"知道有这个抽屉，需要的时候不用重新发明"。

## MemoryMiddleware —— 跨会话的 AGENTS.md 记忆

`MemoryMiddleware`（容器内 `deepagents/middleware/memory.py:179-242`）可以从 `sources: list[str]` 指定的一批文件（约定俗成是 `AGENTS.md` 风格的说明文档）里加载内容，通过系统提示词里的 `{agent_memory}` 占位符（默认模板 `MEMORY_SYSTEM_PROMPT`，`memory.py:104-169`）注入。它接入 `create_deep_agent` 的方式是传 `memory=[...]` 参数（`graph.py:798-807`，仅当非 `None` 才装配）。

SourceLens 现在每次运行都是"从零开始"的一次性问答/分析，没有跨运行的持久记忆需求，所以这个参数一直是 `None`。如果未来要做"这个助手记得上次聊过的项目背景"之类的能力，这是现成的挂载点——不需要自己另起一套记忆系统。

## ContextHubBackend —— LangSmith Hub 持久文件

`FilesystemBackend(virtual_mode=True)`（第 1 章）是每次运行专属、运行结束即回收的临时区。库里还有一个 `ContextHubBackend`（`deepagents/backends/context_hub.py:45-64`），构造签名 `__init__(self, identifier: str, *, client: Client | None = None)`，通过 `langsmith.Client()` 把文件存到 **LangSmith Hub** 的一个 agent 仓库里——也就是说文件是跨运行、跨会话持久的，不随进程结束而消失。

SourceLens 目前刻意选择临时 scratch 区（每次运行的工作区都是干净的，避免不同用户/不同运行的数据串号），所以没有接这个 backend。它更适合"同一个 agent 反复处理同一批持久资料"的场景。

## HumanInTheLoopMiddleware / permissions —— 工具审批门控

这个能力其实不是 `deepagents` 自己实现的，而是直接复用 LangChain 的 `HumanInTheLoopMiddleware`（`graph.py:13` 从 `langchain.agents.middleware` 导入）。`create_deep_agent` 只有在调用方传了 `interrupt_on=...`，或者某个 `FilesystemPermission` 的 `mode="interrupt"`（`FilesystemPermission.mode` 取值为 `"allow" | "deny" | "interrupt"`，`graph.py:423-433`）时，才会把它自动装进中间件栈（`graph.py:808-813`）。`deepagents/middleware/_fs_interrupt.py` 里的 `_build_interrupt_on_from_permissions` 负责把文件系统权限配置翻译成 LangChain 的中断配置。

SourceLens 现在的工具都是只读检索 + 一个白名单严格的 `save_deliverable`，没有"危险操作需要人工点头"的场景，所以从未传过 `interrupt_on`。如果未来要给模型开放写操作（比如直接改用户仓库里的文件），这是应该优先接入的能力，而不是自己写一套审批逻辑。

## RubricMiddleware —— 结果评分/outcome，beta 能力

`RubricMiddleware`（`deepagents/middleware/rubric.py:296-370`，源码上标了 `@beta` 装饰器）实现的是"跑完一轮，让另一个评分子代理按 rubric 检查结果，不达标就打回重跑"的循环。构造参数包含 `model`、`system_prompt`、`tools`、`max_iterations`（硬上限 20 次，`_MAX_ITERATIONS_HARD_CAP = 20`），内部通过一个独立的 `create_agent(..., response_format=GraderResponse)` 评分子代理实现。

它**不在** `create_deep_agent` 的默认中间件栈里，是从 `deepagents` 顶层单独导出、需要显式 `middleware=[RubricMiddleware(...)]` 传入的可选能力，且只有调用时状态里带了 `rubric` 才会真正激活——不用也不会有额外开销。对"答案质量必须过某个硬性标准，宁可多跑几轮也不能凑合"的任务（比如生成给客户看的最终报告）会有用；SourceLens 目前的问答/分析场景对时延更敏感，暂时没有引入。

## 异步子代理 —— 后台跑在远程 LangGraph Platform

第 1 章讲的 `_fast_subagent()` 是同步子代理：`task` 工具阻塞等待它跑完。`deepagents` 还支持一种完全不同的委派方式——`AsyncSubAgent`（`deepagents/middleware/async_subagents.py`，一个 `TypedDict`，靠是否包含 `graph_id` 字段和同步 `SubAgent` 区分，`graph.py:598-602`）。它通过 `langgraph_sdk` 在 **LangGraph Platform（或自托管的 Agent Protocol 服务）上发起一个后台 run**，立刻返回一个任务 ID 而不是阻塞等待，任务状态存在 `state["async_tasks"]` 里（`async_subagents.py:878`）——因为存在 state 而不是消息历史里，即使主 agent 后续触发了压缩，这个任务状态也不会被摘要掉。

SourceLens 的部署形态里没有独立的 LangGraph Platform 集群，`_fast_subagent()` 走的是进程内同步委派，用不上这套机制。如果未来要支持"提交一个长任务，先返回给用户一个进度页，稍后再来看结果"这种交互，异步子代理是比自己搭一套任务队列更贴合 `deepagents` 生态的方案。

## Context Editing —— 库里有，`deepagents` 默认栈没接

第 2 章提过，`ContextEditingMiddleware`（`langchain/agents/middleware/context_editing.py`）实现的是 Anthropic 的 `clear_tool_uses_20250919` 语义：只清理陈旧的工具调用痕迹，不做摘要式改写，是压缩之外的另一条路径。`deepagents` 的默认中间件栈里没有它，需要用的话手动 `middleware=[ContextEditingMiddleware(...), ...]` 接入。

它跟卸载（offload）解决的是相似的表面问题（上下文里有些内容不再需要了），但机制不同：卸载是"搬到文件里，需要时还能读回来"，上下文编辑是"清掉旧的工具调用记录，不留存根"。如果未来遇到"上下文里堆积了大量已经没有价值、连存根都不想留"的工具调用痕迹，这个中间件是比继续压低卸载阈值更对症的工具。

## 结构化输出 —— `response_format`

`create_deep_agent(..., response_format: ResponseFormat[ResponseT] | type[ResponseT] | dict[str, Any] | None = None)`（`graph.py:247`）直接透传给内部的 `create_agent(..., response_format=response_format)`（`graph.py:845`），也可以单独给某个 `SubAgent` 设置（`SubAgent.response_format`，`subagents.py:115-152`，在 `subagents.py:733` 被消费）。`RubricMiddleware` 的内部评分子代理就是用这个机制强制模型输出结构化的 `GraderResponse`。

SourceLens 现在的最终产出是一段自由文本答案（`_extract_final_message`，`agent_runtime.py:714-726`，直接取最后一条消息的 `content`），没有下游系统需要解析结构化字段，所以没用这个参数。如果未来要让 Deep Agent 的输出直接喂给另一个自动化流程（而不是展示给人看），这是应该优先考虑的机制，而不是让下游自己去正则解析自由文本。

## Skills 的渐进披露 —— 我们只浅用了一半

SourceLens 确实在用 Skills（`agent_runtime.py:363-364`：`resources.skill_paths` 非空且非 General Chat 时传入 `kwargs["skills"]`），但只用到了它"渐进披露（progressive disclosure）"机制的第一层。

`SkillsMiddleware`（`deepagents/middleware/skills.py`，模块 docstring 明确写了"implements Anthropic's agent skills pattern with progressive disclosure"）的做法是：系统提示词里只提前放每个 skill 的 `name`/`description`/文件路径（元数据），完整的 `SKILL.md` 正文**不会**提前塞进上下文——`SKILLS_SYSTEM_PROMPT`（`skills.py:705-745`）明确指示模型：判断任务匹配某个 skill 后，自己用 `read_file` 按需读取，并提醒把 `limit` 调到 `1000`（默认单次读 100 行对大多数 skill 文件不够）。

这意味着"渐进披露"不是一次性把所有内容都算进上下文预算，而是让模型自己决定要不要为某个 skill 付出"读它全文"的上下文代价。SourceLens 目前的用法（通用聊天场景加载已绑定的 skills，第 2 章提过的 `_context_guidance`/`_general_chat_guidance` 把内容整段拼进提示词）某种程度上绕开了这层机制——直接把内容摘要塞进提示词，而不是让模型按需 `read_file`。这不是错误用法，两种方式各有取舍（前者省一次工具调用往返，后者更省上下文），只是值得知道库本身设计的默认路径是后者。

## 小结：抽屉都在，先想清楚要解决什么问题

这一章列的每一项能力都不是"更高级所以更好"，而是"解决某类特定问题时，库里已经有现成的抽屉，不用自己重新发明"。真正决定要不要引入某项能力的，永远是具体的产品/工程需求，而不是"库里有就该用"。

下一章我们回到一个真实发生过的问题——一次上下文丢失的 bug，从现象到修复的完整过程，把前两章讲的概念在真实故障里过一遍。
