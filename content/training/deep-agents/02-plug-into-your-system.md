---
title: 第 2 章 · 接入你自己的系统：模型、工具、Backend
date: 2026-07-20T07:05:00+08:00
author: Ray Sun
tags:
  - Deep Agent
  - LangChain
  - SourceLens
  - AI
categories:
  - AI应用开发
weight: 3
---

上一章说过，`create_deep_agent` 真正需要你原创的只有三样：模型、工具、（通常还需要一个）backend。这一章讲清楚这三样东西**通用的做法**是什么——每一节都先说"不管你在封装什么工具，这里该怎么想"，再看 SourceLens 具体是怎么落地的。

## 自定义模型：什么时候需要自己包一层

`create_deep_agent` 的 `model` 参数接受任何 LangChain `BaseChatModel`。如果你直接用 Anthropic、OpenAI 这些库原生支持的 provider，传对应的 SDK 封装类就完事了，这一节可以跳过。

但如果你的调用要经过自己的网关、自己的路由/计费/审计层——这是企业内部封装工具时的常态——你就需要自己实现一个 `BaseChatModel` 子类，核心是覆写 `_generate`（同步）方法，把 LangChain 的消息格式翻译成你后端接受的格式，再把响应翻译回来。SourceLens 的 `LensGatewayChatModel`（`lensnode/lensnode/gateway_model.py:55`）就是这样一层：所有模型调用不直接打到某个厂商 SDK，而是转发给内部 AI 网关。

自己实现这一层时，有几个通用的坑值得提前知道：

**流式和非流式往往要分开处理**。`LensGatewayChatModel._generate`（`gateway_model.py:109`）按有没有传入输出回调，分别走 `_generate_streaming`（SSE 逐 token 转发）或者一次性拿完整响应两条路径——这不是 SourceLens 特有的需求，任何要在前端展示"正在打字"效果的封装都会遇到同样的分支。

**子代理的输出可能需要单独处理**。`deepagents` 跑子代理时会用 LangSmith 的 tracing context 打上 `ls_agent_type="subagent"` 元数据；如果你的模型层要把 token 实时推给用户界面，需要判断当前调用是不是来自子代理（`gateway_model.py:37` 的 `_in_subagent_context()`），不然并行跑的多个子代理会把输出交错打进同一个气泡里。这个坑只有真正用上子代理委派（第 3 章）之后才会暴露，但模型层的判断逻辑现在就可以先写好。

**`_llm_type` 不是随便起的名字**。`BaseChatModel._llm_type` 这个属性除了标识用途，还会被 LangChain 的摘要中间件用来决定 token 计数比例（第 4 章会详细展开）。`LensGatewayChatModel._llm_type` 返回的是 `"lens_gateway_chat_model"`——一个自定义网关模型，天然不会被误判成某个特定厂商的模型，这一点在你自己实现时也值得留意：不要为了"图方便"让 `_llm_type` 冒充成一个官方 provider 的类型字符串，否则会激活一些你没预料到的、针对那个 provider 调优的分支逻辑。

**usage 数据要自己接回来**。模型每次调用完，返回结果里的 token 用量、耗时这些数据默认不会自动出现在你的可观测系统里——需要你自己把它们塞进返回消息的 `response_metadata`（`gateway_model.py:151-154`），后续观测代码才能读到。

## 自定义工具：给模型划一条只读边界

工具是整个 harness 里**唯一没有默认实现、必须你自己写**的部分。设计业务工具时，几条通用原则值得先立住，而不是等出问题了再补：

**先明确工具的读写边界**。如果你的场景是"检索/分析已有资料"，工具应该从设计上就是只读的——不给模型任何写入生产数据的路径。SourceLens 的 `search_workspace`/`read_workspace_file`/`find_files`/`git_log`/`git_diff`（`lensnode/lensnode/agent_tools.py`）全部是只读工具，写操作被严格限制在一个隔离的 scratch 区（下一节讲）。

**大内容要能分页读，不要一次性塞完**。`read_workspace_file`（`agent_tools.py:141`）按 `offset`/`limit` 返回文件的一个窗口而不是整个文件，配合 `search_workspace` 先定位命中行号，再按需分页读——这样模型才能处理任意大小的文件，而不会一读就把上下文打爆。

**给容易失控的工具设一个调用预算**。`git_diff`（`agent_tools.py:310`）设了 `git_diff_max_calls`（默认 8 次），超出后返回一个 `TOOL_BUDGET_EXCEEDED` 状态，明确指示模型"别再调了，用已有证据收尾"。这是一个很小但很有效的护栏模式：与其祈祷模型自己判断"够了"，不如在工具层给它一个硬性的、带说明的止损点。

**参数名要对模型的习惯宽容一些**。`read_workspace_file` 的参数 schema（`_ReadWorkspaceFileArgs`，`agent_tools.py:37`）同时接受 `file_path` 和 `path` 两种字段名——因为不同模型、不同 few-shot 习惯下，模型倾向使用的参数名并不统一，工具层多花一点心思做兼容，比事后调 prompt 让模型"记住用哪个参数名"更可靠。

**想清楚模型生成的东西怎么真正交给用户**。只读检索工具解决的是"进"的问题，工具集里通常还需要一个"出"的通道——模型在 scratch 区里生成的产物（报告、转换后的文件……）默认不会自动到达用户手上。这个通道本身值得单独设计，第 3 章会讲 SourceLens 是什么时候、为什么补上这一环的。

## 自定义 Backend：给模型一个安全的草稿区

`deepagents` 的内建文件工具（`ls`/`read_file`/`write_file`/`edit`/`glob`/`grep`）都是相对某个 **backend** 操作的，不给的话默认是一个内存态、不落盘的实现。多数真实场景需要更明确的隔离：

```python
"backend": FilesystemBackend(
    root_dir=str(resources.root),
    virtual_mode=True,
),
```

`virtual_mode=True` 让这些内建工具的活动范围被限制在 `root_dir` 这一个目录里——模型看到的"文件系统"其实是这次运行专属的一块 scratch 区。SourceLens 给每次运行分配一个私有目录，运行结束即回收。

这里有一个所有类似封装都会踩的坑，值得提前写进你的系统提示词：**内建文件工具和你自己的业务检索工具，作用域是两个完全不同的空间**。内建 `ls`/`read_file` 只能看到 backend 指向的 scratch 区，看不到你在 `tools` 里注入的那些业务数据源（SourceLens 里是用户选中的真实工作区目录）。如果不在提示词里说清楚这一点，模型很容易把"内建 `ls` 看到的空目录"误判成"业务数据不存在"——这不是模型的错，是两套工具语义没有讲清楚导致的。

## 这一章的落点

模型、工具、backend 这三件事做对了，你就有了一个能在自己系统里稳定跑起来的 Deep Agent——但它现在还很朴素：没有委派、没有场景切换、没有真正的交付通道。下一章讲的就是它们是怎么被真实需求一步步逼出来的。
