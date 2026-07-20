---
title: 第 3 章 · 不断丰富你的 Harness
date: 2026-07-20T07:10:00+08:00
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

第 1 章那个"第一版"（2026-06-07，`6405cd0`）能跑，但很朴素：没有委派、没有场景切换、没有真正的交付通道。这一章不做假设性的"丰富化教程"，而是照着 SourceLens 之后几周真实发生的提交顺序走一遍——每一步都是被具体需求逼出来的，不是提前设计好的。这条路径本身，就是这一章最重要的内容：**你的 harness 大概率也会按类似的顺序长大，因为逼你加这些能力的需求是通用的，不是 SourceLens 独有的**。

## 第一步逼近：什么时候需要委派子任务

`6405cd0` 之后 4 天，`6dc1cd4`（2026-06-11 "speed up and isolate task subagents"）给主 agent 加上了子代理配置：

```python
"subagents": [_fast_subagent()],
```

（`agent_runtime.py:618-639`，`_fast_subagent()` 复用 `deepagents` 自带的 `GENERAL_PURPOSE_SUBAGENT`，只在它的系统提示词前面拼接了一段"并行优先"的指导语）

驱动这次改动的是一个具体的性能数字：默认的委派子代理跑的是串行 ReAct（一次读一个文件），一个子任务动辄 6 分钟；重写提示词让它像主循环一样批量并行发起工具调用后，同样的子任务掉到约 1 分钟，10 个并行子代理可以在 45 秒内全部跑完。**通用的教训是**：`task` 委派工具是 `deepagents` 免费给你的，但子代理默认的思考方式不一定适合你的场景，往往需要用一段提示词去纠正它，而不是假设"用了子代理就自动变快"。

配套的还有一个判断"值不值得委派"的逻辑（`_subagent_guidance`，`agent_runtime.py:642-667`）：只有在任务本身足够重、足够独立时才建议模型使用 `task` 委派，因为子代理是一次完整的、分钟级的 agent loop——委派本身不是免费的，轻量的多文件读取用批量并行工具调用处理反而更快。子代理拥有和主 agent 完全独立的上下文（包括它自己独立的一份摘要中间件），这一点在第 4 章讲"子代理隔离"时会展开原理；这里先记住结论：**不是所有子任务都值得委派，只有"足够独立、足够重"的才值得**。

## 第二步逼近：任务开始变长

`6dc1cd4` 之后 4 天，`afac535`（2026-06-15 "per-step latency observability + context-compaction safety net"）第一次给 agent 加上了自定义的压缩中间件——这是团队第一次意识到"深度调查类任务会把上下文堆得很大"这件事需要主动管理，而不是放任 `deepagents` 内建的默认阈值（约 17 万 token）去兜底。

这一步的完整原理、以及它当时留下的一个隐患（一个关于"workspace 内容都能重新搜到"的假设，后来在 issue #60 里被证明不完全成立），第 4 章会用整整一章展开——这里只需要知道：**"任务会变长"不是一次性设计出来的洞察，是先跑起来、看见真实场景之后才会意识到的**。三周后（`7854b8d`，2026-06-24），团队又因为一次超时故障把这个压缩触发阈值从 8 万调低到 4.8 万——同一个洞察，随着真实流量的反馈还在持续被修正。

## 第三步逼近：一个 Harness 要服务不同的任务模式

`0807f46`（2026-07-03 "add general chat task support"）给系统引入了第二种任务模式：除了原本"检索工作区证据回答问题"的知识问答场景，新增了一种不做工作区检索、完全靠绑定的 Skill 驱动的通用聊天模式。

对应到代码，这不是重新搭一套 agent，而是让同一个 `create_deep_agent` 装配按场景分叉：

- **不同的工具集**：`build_agent_tools`（知识问答/代码分析场景，只读工作区工具）vs. `build_general_chat_tools`（通用聊天场景，`run_skill_script` 等）——`agent_runtime.py:57` 和 `agent_runtime.py:570` 两个独立的工具构建函数。
- **不同的系统提示词**：`_knowledge_system_prompt` vs. `_general_chat_system_prompt`（`agent_runtime.py:474`、`agent_runtime.py:578`），按 `_is_general_chat(command)` 分派。

**通用的做法是**：与其为每种任务模式各写一个 agent，不如把"工具集"和"系统提示词"做成按场景可替换的两个变量，`model`/`backend`/中间件栈这些骨架保持一致。这样加一种新的任务模式，成本是"写一套新的工具 + 一段新的提示词"，而不是"再搭一遍 harness"。

## 第四步逼近：模型做出来的东西要真的到用户手上

`328aad8`（2026-07-15 "deliver LensNode-generated files to users"）补上了第 2 章末尾留的那个缺口——`save_deliverable` 工具（`agent_tools.py:459`）：模型在 scratch 区里生成的文件，调用这个工具才会被上传给控制面、变成用户可以下载的产物；没调用过的文件，运行结束后随 scratch 区一起被清理掉。

这一步之所以排在这么靠后才补上，是因为它只有在"模型开始被要求产出文件类交付物"（而不仅仅是文本回答）之后才会成为真实需求——**通用的教训是**：不要在一开始就假设你的 harness 需要一整套复杂的交付机制；先让模型能读、能答，交付通道等真实场景逼出这个需求时再补，实现成本并不高。

## 装配顺序：加的东西越多，越要清楚谁在谁前面

随着 harness 长出委派、场景切换、自定义压缩这些能力，一个新问题出现了：这些中间件互相之间的**装配顺序**开始变得重要。`create_deep_agent()`（容器内 `deepagents 0.6.8`，`graph.py:750-813`）内部按固定顺序组装：

```text
TodoListMiddleware              [langchain]
  → (可选) SkillsMiddleware            [deepagents]  仅当传入 skills
  → FilesystemMiddleware              [deepagents]
  → (可选) SubAgentMiddleware          [deepagents]  仅当传入 subagents
  → 内建 SummarizationMiddleware        [deepagents 包装，内部委托 langchain]
  → PatchToolCallsMiddleware           [deepagents]
  → (可选) AsyncSubAgentMiddleware      [deepagents]  仅当传入 async 子代理
  → 调用方传入的 middleware（你自己的中间件插在这里）
  → harness profile 的附加中间件
  → (可选) 工具排除中间件               [deepagents]
  → AnthropicPromptCachingMiddleware   [langchain_anthropic]  无条件添加
  → (可选) MemoryMiddleware             [deepagents]  仅当传入 memory
  → (可选) HumanInTheLoopMiddleware     [langchain]  仅当传入 interrupt_on
```

方括号标的是每个中间件类真正定义在哪个 pip 包里——`create_deep_agent` 只是这条流水线的组装者，`TodoListMiddleware`/`HumanInTheLoopMiddleware` 来自 `langchain`，`AnthropicPromptCachingMiddleware` 来自专门的 `langchain_anthropic`，其余大部分才是 `deepagents` 自己实现的类。这个区分在第 1 章已经强调过一次，这里再列一遍完整顺序时同样标出来，因为**顺序图最容易让人产生"这一整条都是 deepagents 写的"的错觉**——实际上它是三个包的中间件被粘在一起。

这里有个容易踩的坑，SourceLens 自己也是在加了自定义压缩中间件之后才意识到的：**`create_deep_agent` 会无条件给主 agent 装一个它自己的内建 `SummarizationMiddleware`**，出现在调用方传入的 `middleware` 之前。你通过 `kwargs["middleware"] = [...]` 追加的任何自定义压缩逻辑，都不是替换它，而是**叠加在它后面**——一次运行里会同时存在两层摘要中间件。SourceLens 的做法是把自己的触发阈值压得远低于内建阈值（约 17 万 token），保证自己的中间件总是先触发、把上下文压在内建阈值之下，让内建中间件始终保持休眠（`_build_summarization_middleware` 的 docstring，`agent_runtime.py:162-176`，明确写了"不要把触发阈值调到接近 17 万"）。

**通用的道理是**：只要你往 `middleware` 参数里加东西，就必须先搞清楚库自己已经装了什么、顺序是什么——不然很容易出现"我加的这层根本没生效"或者"两层逻辑在打架"这种隐蔽问题。

## 这一章的落点

把这四步逼近串起来看：委派、上下文管理、场景化、交付通道——没有一个是提前设计出来的，全部是"先跑起来，被真实需求逼出来"的结果。这条路径也不是 SourceLens 独有的：如果你也在用 `deepagents` 封装一个自己的工具，大概率会按类似的顺序撞到同样的需求。下一章开始，我们把"任务开始变长"这一步（`afac535` 埋下的那个隐患）彻底讲透——因为它是这几步里唯一一个后来真的引发过生产故障的。
