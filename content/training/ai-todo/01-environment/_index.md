---
title: 第二部分 · 环境准备
linkTitle: 第二部分 · 环境准备
date: 2026-07-08T00:10:00+08:00
draft: false
author: Ray Sun
tags:
  - AI
  - 零基础
  - WorkBuddy
  - 环境准备
categories:
  - AI应用开发
weight: 2
prev: /training/ai-todo/00-introduction/03-code-as-blackbox
sidebar:
  open: true
---

# 第二部分 · 环境准备

初学者最大的拦路虎，往往不是代码，而是**环境跑不起来**。这一部分我们只有一个目标：让你的电脑能顺利运行 AI 开发工具，并且能创建项目、启动页面、看到结果。

**重要原则**：这一部分不解释太多原理。你只要照着做，每一步做完都有一个「验收命令」告诉你成没成。**做完看到预期结果，就继续下一步；没看到，就把报错原封不动发给 AI。**

<!--more-->

## 工具已经替你选好：WorkBuddy

本课程统一使用 **WorkBuddy**。

选择它不是因为它最强，而是因为它更适合中国市场的零基础用户：下载安装、登录和使用都比较方便；界面也以对话为主，不需要先理解传统 IDE 里的项目目录、代码区和终端。

### 从 AI 编辑器到智能体（Agent）

Cursor 是 AI 编程工具的重要先驱，它把 AI 深度集成到代码编辑器中，推动了通过对话生成和修改代码的开发方式。

后来，AI 开发工具进一步发展成了智能体（Agent）。

普通聊天式 AI 通常是：

> 「输入一句话 → 返回一个答案」

智能体则会围绕一个目标连续工作：

> 「理解需求 → 拆解任务 → 执行操作 → 检查结果 → 发现问题后继续修复」

这也是它能够直接参与应用开发的原因。

目前，Claude Code 和 Codex 更适合复杂项目和专业开发场景。

### 为什么选择 WorkBuddy

我们最早也尝试让非技术人员使用 Cursor，但传统 IDE 会同时展示项目目录、代码编辑区和终端。

这些东西对开发者很自然，对零基础用户却会增加额外的学习成本。

WorkBuddy 的使用体验更接近大家已经熟悉的 ChatGPT：主要入口就是一个对话框。

但它并不是普通聊天工具，而是一个智能体入口。你提出需求后，它可以直接操作本地项目、运行程序，并持续完成后续任务。

简单来说：

> 「看起来是在聊天，实际上是在让智能体替你做事。」

WorkBuddy 不一定是能力最强的工具，但足以完成本课程。

随着项目复杂度提高，可以进一步使用 Cursor、Claude Code 或 Codex。

无论使用哪一种工具，基本流程都不会变化：

> 「提出需求 → 智能体执行 → 检查结果 → 继续修改」

## 关于这一部分怎么用

分成五个小节，一节一节跟着做：

{{< cards >}}
  {{< card link="01-download-workbuddy" title="6 · 下载 WorkBuddy" subtitle="根据系统选对下载入口" icon="cloud-download" >}}
  {{< card link="02-install-workbuddy" title="7 · 安装并登录 WorkBuddy" subtitle="Windows / macOS 安装步骤" icon="desktop-computer" >}}
  {{< card link="03-check-environment" title="8 · 检查 Python 和 Node.js 环境" subtitle="用运行环境检测提前排雷" icon="check-circle" >}}
  {{< card link="04-first-run" title="9 · 第一次运行 WorkBuddy" subtitle="打个招呼，验证环境真的通了" icon="play" >}}
  {{< card link="05-first-project" title="10 · 第一次让 AI 创建项目" subtitle="搭出项目骨架，浏览器里见结果" icon="sparkles" >}}
{{< /cards >}}

> 💡 **一个贯穿全课的判断题从这里就开始了**：每一步做完，你都要问自己「我看到预期的结果了吗？」看到了打勾，没看到就反馈给 AI。这个习惯，请从环境准备就养成。

从 [6 · 下载 WorkBuddy]({{< relref "01-download-workbuddy.md" >}}) 开始。
