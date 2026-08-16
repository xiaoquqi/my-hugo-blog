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

这一部分只做四件事：选工具、装工具、确认工具能正常运行、认识工具的基本界面。做完这四件事，就可以开始真正的开发了。

<!--more-->

## 2.1 选择 AI 开发工具

本课程使用 WorkBuddy。

选它的原因：适合国内的零基础用户。下载、安装、登录都方便；界面是纯对话式的，不需要先搞懂传统 IDE 里的项目目录、代码编辑区、终端这些概念。

AI 编程工具经历了从"代码编辑器 + AI"到"智能体（Agent）"的演变。Cursor 是这条路线的重要先驱，把 AI 深度集成进代码编辑器，让人可以用对话生成和修改代码。后来 AI 工具进一步发展成智能体：普通聊天式 AI 是"输入一句话，返回一个答案"；智能体会围绕一个目标连续工作，流程是"理解需求 → 拆解任务 → 执行操作 → 检查结果 → 发现问题继续修复"。这也是智能体能直接参与应用开发的原因。目前 Claude Code 和 Codex 更适合复杂项目和专业开发场景，但对零基础用户门槛更高。

我们最早尝试过用 Cursor 教非技术人员，但传统 IDE 会同时展示项目目录、代码编辑区和终端，这些对开发者是常识，对零基础用户却是额外的学习成本。

WorkBuddy 的主要入口是一个对话框，体验上接近 ChatGPT，但它不是普通聊天工具，而是一个智能体入口：提出需求后，它可以直接操作本地项目、运行程序、持续完成后续任务。简单说就是看起来在聊天，实际是在让智能体替你做事。

WorkBuddy 不是能力最强的工具，但足以完成本课程。项目复杂度提高后，可以进一步使用 Cursor、Claude Code 或 Codex。不管用哪个工具，基本流程不变：提出需求 → 智能体执行 → 检查结果 → 继续修改。

## 2.2 安装并准备开发环境

三步：下载 WorkBuddy → 完成安装 → 检查运行环境，对应下面第 6~8 节。装完后，第 9 节过一遍界面，还不涉及任何开发内容。

{{< cards >}}
  {{< card link="01-download-workbuddy" title="6 · 下载 WorkBuddy" subtitle="根据系统选对下载入口" icon="cloud-download" >}}
  {{< card link="02-install-workbuddy" title="7 · 安装并登录 WorkBuddy" subtitle="Windows / macOS 安装步骤" icon="desktop-computer" >}}
  {{< card link="03-check-environment" title="8 · 检查 Python 和 Node.js 环境" subtitle="用运行环境检测排查缺失依赖" icon="check-circle" >}}
  {{< card link="04-first-run" title="9 · 认识 WorkBuddy 的界面" subtitle="了解常用菜单的位置和作用" icon="puzzle" >}}
{{< /cards >}}

从 [6 · 下载 WorkBuddy]({{< relref "01-download-workbuddy.md" >}}) 开始。
