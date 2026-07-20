---
title: 第 1 章 · 从三行代码开始：最小 Harness
date: 2026-07-20T07:00:00+08:00
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

封装一个自己的 Deep Agent 工具，起点比想象中要小。`deepagents` 的核心入口只有一个函数：

```python
from deepagents import create_deep_agent

agent = create_deep_agent(
    model=your_model,
    tools=your_tools,
)
response = agent.invoke({"messages": [{"role": "user", "content": "帮我查一下……"}]})
```

这就是一个能跑的 Deep Agent。真正要花心思的，是接下来两件事：**你要往这三四个参数里塞什么**，以及**你什么都不塞的时候，库已经悄悄替你装好了什么**。这一章只讲这两件事，先不碰任何自定义中间件。

## 一个真实的"第一版"

理论例子容易失真，我们看一个真实存在过的版本：SourceLens 的 `lensnode` 服务在 2026-06-07 的第一个提交（`6405cd0` "Add SourceLens Lens execution stack"）里，`agent_runtime.py` 只有 246 行，核心装配是这样的（节选自当时的版本）：

```python
model = LensGatewayChatModel(
    model_ref=str(model_ref),
    ai_gateway_url=self.config.ai_gateway_url,
    token=self.config.token,
    request_timeout_s=self.config.request_timeout_s,
)
tools = build_agent_tools(command, emit_event=emit_agent_event)
kwargs = {
    "model": model,
    "tools": tools,
    "system_prompt": _system_prompt(scenario, command, resources.context_skill_contents),
    "backend": FilesystemBackend(root_dir=str(resources.root), virtual_mode=True),
    "name": f"lensnode-{command.get('task') or 'agent'}",
}
if resources.skill_paths:
    kwargs["skills"] = resources.skill_paths

agent = create_deep_agent(**kwargs)
response = agent.invoke(
    {"messages": [{"role": "user", "content": question}]},
    config={"recursion_limit": 30},
)
```

没有子代理配置，没有自定义中间件，没有卸载阈值调优，没有 `save_deliverable`，甚至连 `agent.stream` 都没用（直接 `agent.invoke` 拿一次性结果）。这就是一个真实系统跑在生产上的**第一版** Deep Agent——比很多人以为的"起步门槛"要低得多。后面几章会看到，今天的 `agent_runtime.py`（973 行）几乎全部内容，都是从这个起点上一步步长出来的。

## 你必须提供的，只有这几样

对照上面这段代码，`create_deep_agent` 真正要求你想清楚的参数，其实只有：

1. **`model`** —— 一个 LangChain `BaseChatModel`。如果你用的是库直接支持的官方 provider（Anthropic、OpenAI 等），传对应的 SDK 封装类就行；如果你要接自己的网关/自建路由（就像上面 `LensGatewayChatModel` 这样），需要自己实现一层，下一章会展开讲。
2. **`tools`** —— 你的业务能力，一个函数/工具的列表。这是整个 harness 里**唯一必须由你原创**的部分：框架不知道你的领域数据在哪、你的业务规则是什么，这些只能你自己写。
3. **`system_prompt`**（可选，但强烈建议给）—— 告诉模型它是谁、能干什么、必须遵守什么流程。不给的话模型只能靠工具描述自己摸索。
4. **`backend`**（可选）—— 不给的话，`deepagents` 会用一个默认的内存态文件系统；给一个 `FilesystemBackend(root_dir=..., virtual_mode=True)`，就能把模型的读写限制在你划出来的一块目录里，见第 2 章。

除此之外，`skills`、`subagents`、`middleware`、`memory`、`permissions`、`response_format` 等等，全部是可选的——**不给就是"不要"，库不会因为你没给就少做什么该做的事**。这正是下一节要讲的重点。

## 你什么都不配置时，库已经替你做了什么

即便像上面那样只传最基本的四五个参数，`create_deep_agent` 内部依然会按固定顺序（容器内实际安装的 `deepagents 0.6.8`，`graph.py:750-813`）装好一整套中间件：

- **`TodoListMiddleware`** —— 给模型一个 `write_todos` 工具，可以规划、追踪多步任务。
- **`FilesystemMiddleware`** —— 除了给 `backend` 接文件工具（`ls`/`read_file`/`write_file`/`edit`/`glob`/`grep`），还**默认**会在工具返回结果超过 `20000` token、或者人类消息超过 `50000` token 时，主动把内容卸载成文件（`filesystem.py:698-707`）——这不是你要求它做的，是库的默认行为。
- **内建 `SummarizationMiddleware`** —— 对没有 model profile 信息的模型，默认在上下文摸到约 `170000` token 时触发一次压缩（`compute_summarization_defaults`，`deepagents/middleware/summarization.py:172-209`）。你没配置任何压缩参数，也不代表你的 agent 不会压缩——只是压缩阈值是库替你选的，而不是你自己算过的。
- **`PatchToolCallsMiddleware`** —— 修补一些模型输出的工具调用格式问题。
- **`AnthropicPromptCachingMiddleware`** —— 无条件装配，模型不是 Anthropic 系列时自动忽略（`unsupported_model_behavior="ignore"`）。

这几项都是**开箱即用**、不需要你写一行中间件代码的能力。它们也是这份指南第 4 章要重点拆解的对象——因为"库替你选的默认阈值"和"你的场景真正需要的阈值"往往对不上，这正是后面 SourceLens 真实踩坑的起点。

## 这一章的落点

搭一个自己的 Deep Agent 工具，第一步不是研究一整套中间件体系，而是**先把这三四个参数填对，把它跑起来**。框架已经替你把"一个能长期运行、不会立刻崩掉的循环"这件事解决了大半；你真正要花精力的，是下一章要讲的——怎么把你自己的模型、自己的工具、自己的数据边界，正确地接进这几个参数里。
