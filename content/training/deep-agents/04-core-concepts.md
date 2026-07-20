---
title: 第 4 章 · 核心概念（团队最容易搞错的）
date: 2026-07-20T07:15:00+08:00
author: Ray Sun
tags:
  - Deep Agent
  - LangChain
  - SourceLens
  - AI
categories:
  - AI应用开发
weight: 5
---

这一章是全文的重点。第 3 章讲到，SourceLens 在 `afac535`（2026-06-15）第一次给 harness 加上了主动的上下文管理——这是"任务开始变长"这个通用需求逼出来的一步。但"加了压缩中间件"和"真正理解上下文管理"是两回事：一旦对下面这几个概念的理解有偏差，代码照样能跑，却会在某个边界条件下悄悄丢数据、悄悄变慢、或者悄悄超支。这些坑，SourceLens 自己也踩过（第 6 章会讲那次真实的故障）。

这一章不再局限于 SourceLens 的实现——这里讲的是任何用 `deepagents` 封装工具的人，迟早都要搞清楚的几件事。

## 压缩、卸载、上下文编辑：三件不同的事

`deepagents` 生态里有三种听起来都像"减少上下文"的机制，但它们的**有损性**和**触发对象**完全不同，混着用是错误的根源。

### Compaction（压缩）—— 有损

由 `SummarizationMiddleware` 实现（`deepagents` 有自己的一层 `_DeepAgentsSummarizationMiddleware`，容器内 `deepagents/middleware/summarization.py:212-334`，内部委托给 `langchain.agents.middleware.summarization.SummarizationMiddleware`）。触发阈值一到，就把**较旧的一段消息**替换成模型生成的一段摘要文字。摘要是对原文的有损压缩——被摘要掉的原始内容不再存在于上下文里，只剩下模型对它的理解。

SourceLens 用 `LensSummarizationMiddleware`（`agent_runtime.py:95`，继承自 LangChain 的 `SummarizationMiddleware`）来做这件事，`trigger=("tokens", config.summary_trigger_tokens)`（默认 `48000`，来自 `LENSNODE_SUMMARY_TRIGGER_TOKENS`，`config.py:83-85`），`keep=("tokens", config.summary_keep_tokens)`（默认 `16000`）。

### Offload / Eviction（卸载）—— 无损

由 `FilesystemMiddleware` 实现（容器内 `deepagents/middleware/filesystem.py`）。它盯着**单条**过大的工具返回结果（或者过大的人类消息），一旦超过阈值，就把内容整条写成 backend 里的一个文件，上下文里只留一个指向这个文件的存根。模型需要时可以用 `read_file` 把它读回来——内容没有丢，只是换了个地方存放。

`FilesystemMiddleware.__init__` 的默认值（`filesystem.py:698-707`）：`tool_token_limit_before_evict: int | None = 20000`，`human_message_token_limit_before_evict: int | None = 50000`。SourceLens 通过 `_apply_offload_thresholds`（`agent_runtime.py:202-243`）把工具阈值降到 `5000`（`LENSNODE_OFFLOAD_TOOL_TOKENS`，默认 `5000`），人类消息阈值保持库默认不动——第 6 章会讲这个改动解决了什么问题、以及为什么人类消息阈值反而不能降。

### Context Editing（上下文编辑）—— 另一种机制，SourceLens 目前没用

这是 LangChain 自己实现的第三种机制：`langchain.agents.middleware.context_editing.ContextEditingMiddleware`，配合 `ClearToolUsesEdit`，实现的是 Anthropic 的 `clear_tool_uses_20250919` 行为——清理陈旧的工具调用结果，但不做摘要式改写。

**在容器内的 `deepagents` 源码里搜索 `clear_tool_uses`/`context_editing`，零命中**——`create_deep_agent` 的默认中间件栈里没有它，SourceLens 的 `agent_runtime.py` 也没有手动引入它。它是装在这台机器上、随时可以通过 `middleware=[ContextEditingMiddleware(...)]` 手动接入的能力，但目前是"库里有、没人用"的状态，第 5 章会再提一句它适合什么场景。

**记住区分方法**：压缩会**改写**内容（有损），卸载会**搬运**内容（无损，但要主动读回来才能再用），上下文编辑清理的是**陈旧的工具调用痕迹**而不做改写。三者可以同时存在于一次运行里，各自有各自的触发条件，不是三选一。

## 两种上下文丢失模式，解药不同

如果只知道"压缩会丢内容"，还是不够——实践中至少有两种表现完全不同的丢失方式：

**模式①：用户粘贴的主题材料被压缩掉**。用户在聊天框里贴了一大段要核对的原文，这段内容混在 `to_summarize` 的旧消息里，一旦触发压缩，摘要模型把它压成一句"核对这份提案"，原文正文永久消失——而这段内容**不在 workspace 里**，模型没法重新搜索找回来。压缩中间件默认假设"丢了还能再查"，这个假设对工具/workspace 返回的证据成立，对用户手打或粘贴的内容不成立。

**模式②：海量检索的中间累积结果被反复压缩冲掉**。这次问题不是某一条内容特别重要，而是任务本身需要遍历一个大语料库，每一轮工具调用都在往上下文里堆证据，堆得足够快时，压缩会被反复触发——模型还没来得及把已经搜到的证据整理成结论，证据就被摘要打薄了一轮又一轮，整个任务在"搜索 → 压缩 → 遗忘 → 重新搜索"里打转，永远收敛不到答案。

这两种模式的解药不同：模式①需要"**别把用户输入送进压缩**"——也就是给 `HumanMessage` 一个豁免；模式②需要"**别让证据攒到压缩线才处理**"——也就是提前把大块证据卸载成文件，从源头上让上下文增长得慢一点。第 6 章会给出这两个解法在 SourceLens 里的具体实现和真实 A/B 数据。

## Token 计数语义：近似值，不是真实 tokenizer

`SummarizationMiddleware` 判断"是否触发压缩"，用的是 `count_tokens_approximately`（`langchain_core/messages/utils.py:2186`），一个**近似**计数器，不是模型自己的真实 tokenizer。它按字符数除以一个比例估算 token 数，默认 `chars_per_token=4.0`。

这里有一个容易搞混、我们自己也一度记错的细节：`_get_approximate_token_counter`（`langchain/agents/middleware/summarization.py:197-205`）只有当 `model._llm_type` 以 `"anthropic-chat"` 开头时，才会把比例改成 `3.3`（这个数字是 LangChain 团队用 Claude 官方 token 计数 API 做线下实验估出来的）；不满足这个条件的模型，一律用函数自身的默认值 `4.0`。SourceLens 的 `LensGatewayChatModel._llm_type` 返回的是 `"lens_gateway_chat_model"`（`gateway_model.py:70-74`）——**不匹配** `anthropic-chat`，所以我们的摘要中间件用的实际上是 `chars_per_token=4.0`，不是 `3.3`。

这个比例本来就是照英文文本估的（"一个 token 约等于 4 个字符"），中文场景下每个汉字往往接近甚至超过 1 个 token，用"4 字符 = 1 token"的英文比例去估中文，会把中文 token 数**严重低估**——而且比此前团队内部按 `3.3` 估的偏差还要更大一些。

计数器还有一个"自我校准"的兜底：`use_usage_metadata_scaling=True`（`summarization.py:204`），逻辑是拿最近一条 AI 消息的真实 `usage_metadata.total_tokens` 去修正估算值（`langchain_core/messages/utils.py:2328-2338`，修正系数封顶 `1.25`）。但这个校准依赖 `AIMessage.usage_metadata` 这个标准字段被填充——回看第 2 章：`_message_from_gateway`（`gateway_model.py:310-334`）只设置了 `response_metadata["usage"]`，从未设置 `usage_metadata`。也就是说，**这个自我校准分支在 SourceLens 里从未真正生效过**，中文场景下的低估是没有兜底的。

这不是一个抽象的理论问题：`summary_trigger_tokens=48000` 这个数字是"计数器单位"，不是真实 token 数。真实触发时刻，对中文内容而言，实际消耗的 token 可能显著高于表面的 48000——这也是第 6 章里"为什么不能简单调高触发线"这个决策成立的根本原因。

## `max_tokens` 语义：只是输出上限，别当成"总预算"

在 SourceLens 这套栈里，`max_tokens` 有一条清晰的传递路径：`LensGatewayChatModel._generate`（`gateway_model.py:133-134`，仅当调用方显式传了这个 kwarg 才会带上）→ 网关请求体 → `backend/lens/views/gateway.py`（`request.data.get("max_tokens")` 原样转发给 `LLMTracker.call_and_track`）→ `agentcore_metering` 的 `trackers/llm.py`（`max_tokens` 非空则覆盖 `get_litellm_params()` 算出的默认值，写进 `params["max_tokens"]`）→ `litellm.completion(**params)`。全程它就是一个**输出 token 上限**的透传参数，没有任何一层对它做过"输入+输出总量"的解读。

如果调用方没有显式传 `max_tokens`，`agentcore_metering` 的 `litellm_params.py` 会按三层默认链兜底：请求/DB 配置值 → 按 provider 的 YAML 默认值 → 全局兜底常量 `DEFAULT_MAX_TOKENS = 16384`。

**这里要澄清一个容易想当然的误解**：这套代码里**没有**一个叫 `context_window` 的配置项或字段——在 `backend/` 和 `lensnode/` 全代码库里搜索这个词，零命中。真正约束"输入 + 输出加起来不能超过多少"的，是模型/provider 自己在 API 层面强制的上限，这套栈从未对它建模、查询或存储，完全是隐式的、由 litellm 和上游 provider 兜底。

把这三个量分清楚：

1. **`max_tokens`** —— litellm 输出上限，走 DB/YAML 配置，默认 `16384`，与"这次对话已经用了多少 token"无关。
2. **`summary_trigger_tokens`（默认 `48000`）/ `summary_keep_tokens`（默认 `16000`）** —— lensnode 侧摘要中间件的压缩触发线，走环境变量配置，用的是上一节讲的近似计数器，和 `max_tokens` 走的完全是两条独立的配置路径、两种独立的计数方式。
3. **模型/provider 自己的真实上下文窗口上限** —— 这套代码完全没有建模的一个隐式量，出问题时只会在 provider 那一层报错，SourceLens 这边看不到、也管不了。

三者互相独立，任何时候不要假设改一个会影响另一个。

## 子代理隔离：独立的上下文，独立的摘要器

`deepagents` 里每一个声明式 `SubAgent` 会被编译成一个**独立的** `create_agent(...)` 图（容器内 `deepagents/middleware/subagents.py:741`），拥有自己完整的中间件栈——**包括它自己独立的一份 `create_summarization_middleware(subagent_model, backend)`**（`graph.py:625` 显式子代理、`graph.py:701` 自动附加的 general-purpose 子代理都各自持有一份），不是和主 agent 共享同一个摘要器实例。

隔离体现在状态传递上：`_validate_and_prepare_state`（`subagents.py:534-539`）把父 agent 状态里除文件系统等共享字段外的部分过滤掉，**`messages` 直接重置为只包含这次委派的任务描述**——子代理看不到父 agent 到目前为止积累的完整对话历史，它是一次全新的、干净的 agent loop，通过共享的 backend（文件系统）和最终返回值跟父任务发生联系，而不是共享同一份消息列表。

没有 model profile 信息时，子代理和主 agent 用的是同一个"无 profile"默认触发线（`("tokens", 170000)`，见第 1 章），不是单独更小的一个数字。

理解这一点，就理解了为什么第 3 章 `_subagent_guidance`（`agent_runtime.py:642-667`）要按分析档位判断"值不值得委派"：子代理是一次完整的、分钟级的 agent loop，隔离带来的干净上下文是有代价的——启动一次委派本身就是一次不便宜的操作，轻量的多文件读取用批量并行工具调用处理，比走一次完整的子代理委派更快。

到这里，三个核心概念（压缩/卸载/编辑的区别、token 计数与 `max_tokens` 语义、子代理隔离）应该都立住了。下一章我们看库里还有哪些能力，SourceLens 目前完全没碰过。
