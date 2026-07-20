---
title: Deep Agent 研发使用指南
linkTitle: Deep Agent 研发使用指南
weight: 2
prev: /training/ai-todo
next:
sidebar:
  open: true
---

# Deep Agent（LangChain/deepagents）研发使用指南 —— 如何封装你自己的 Deep Agent 工具

这不是一篇 deepagents 的 API 手册翻译，而是一份**面向研发团队**的使用指南，讲的是"如果你也要用 `deepagents` 封装一个自己的工具，这条路该怎么走"——从三行代码能跑起来的最小 harness，一步步长成一个真正顶用的系统。SourceLens 的 `lensnode` 服务贯穿全文做例子（它就是这么长出来的，连真实的提交顺序都原样保留），但它始终是例子，不是主角。

<!--more-->

## 这份指南适合谁

会写 Python、想用 `deepagents`（基于 LangChain / LangGraph）封装自己业务工具的研发，不要求你会用 SourceLens 或对它的代码感兴趣——它只是贯穿全文的一个具体例子，所有结论都标注了具体文件和行号，而不是泛泛的框架介绍。

## 版本说明

正文引用的 API 均基于容器 `sourcelens-lensnode-dev` 内**实际安装**的版本：

- `deepagents 0.6.8`
- `langchain 1.3.7` / `langchain-core 1.4.0` / `langgraph 1.2.4`

这两个库的 API 漂移较快，同一个类的构造参数、默认值可能在几个小版本之间就发生变化。本文所有涉及默认值、方法签名的地方都是对着这个版本的源码核实过的；如果你所在环境的版本不同，请以你自己安装的版本为准重新核实，不要直接照搬这里的数字。

## 内容地图

{{< cards >}}
  {{< card link="00-mental-model" title="第 0 章 · 心智模型" subtitle="Deep Agent 是什么，和单次 LLM 调用/手写 tool 循环有什么区别" icon="light-bulb" >}}
  {{< card link="01-minimal-harness" title="第 1 章 · 从三行代码开始" subtitle="最小 Harness，以及不配置任何东西时库已经替你做了什么" icon="cube" >}}
  {{< card link="02-plug-into-your-system" title="第 2 章 · 接入你自己的系统" subtitle="自定义模型、自定义工具、自定义 Backend 的通用做法" icon="puzzle" >}}
  {{< card link="03-growing-your-harness" title="第 3 章 · 不断丰富你的 Harness" subtitle="照着 SourceLens 真实的提交顺序，看需求怎么一步步逼出委派/场景/交付能力" icon="trending-up" >}}
  {{< card link="04-core-concepts" title="第 4 章 · 核心概念" subtitle="压缩、卸载、上下文编辑别混淆；token 计数与 max_tokens 语义" icon="academic-cap" >}}
  {{< card link="05-advanced-capabilities" title="第 5 章 · 还没用到的高级能力" subtitle="MemoryMiddleware、HITL、RubricMiddleware、异步子代理…" icon="beaker" >}}
  {{< card link="06-case-study" title="第 6 章 · 实战复盘：issue #60" subtitle="一个真实的上下文丢失 bug，从现象到修复的完整过程" icon="shield-exclamation" >}}
  {{< card link="07-best-practices" title="第 7 章 · 最佳实践 / Checklist" subtitle="长文本任务怎么配置，调库行为前先做什么" icon="clipboard-check" >}}
{{< /cards >}}

---

准备好了就从 [第 0 章：心智模型](00-mental-model) 开始。
