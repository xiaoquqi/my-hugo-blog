---
title: 面向零基础的 AI 应用开发教程
linkTitle: AI Todo 零基础教程
weight: 1
prev:
next: /training/ai-todo/00-introduction
sidebar:
  open: true
---

# 从 Todo 到 AI Todo：面向零基础用户的 AI 应用开发教程

这是一门**不太一样**的开发课。

它不教你「先背语法、再看懂每一行代码」，而是教你**用 AI 把一个真实应用做出来，并且能判断它做得对不对**。整门课，我们只做一件事：把一个最普通的 Todo（待办清单）应用，一步一步长成一个会帮你拆解任务、总结任务、判断优先级的 **AI Todo 助手**，最后部署到网上让别人也能用。

<!--more-->

## 这门课适合谁

- 完全没有编程经验，但想做出自己的应用。
- 会用电脑、会上网、会打字，仅此而已就够了。
- 有一个「我想做个东西出来」的念头，但一直被「我不会写代码」挡住。
- 想理解 AI 时代普通人到底该怎么做软件。

如果你是有经验的工程师，这门课可能太慢了——但如果你想看看「不写代码怎么带人做产品」，也欢迎旁观。

## 这门课**不是**什么

- ❌ 不是一本 HTML / CSS / JavaScript / Python 语法手册。
- ❌ 不是让你把代码一行行看懂再往下走。
- ❌ 不是工具大比拼，不会让你在十几个 AI 编辑器之间纠结。
- ❌ 不是「先学三个月基础，再谈做项目」。

我们**第一天就开始做产品**，代码细节交给 AI。

## 学完你能做出什么

一个真实、可访问、可迭代的 **AI Todo 助手**：

- 有干净好看的网页界面（Vue + Tailwind CSS）。
- 能添加、删除、完成任务。
- 数据真的保存下来，刷新、关机都不丢（SQLite / PostgreSQL）。
- 有自己的后端服务（Flask，后期升级到 FastAPI）。
- 会调用大模型，**帮你把一句话拆成可执行的小任务、自动总结、自动分类、判断优先级**。
- 用 Docker 一键启动，部署到云服务器，配上域名和 HTTPS。

更重要的是：你会掌握一套**能复用到任何应用**的方法，课程最后我们会用同一套方法，把它扩展成 AI 内容生成器、AI 知识库，甚至小程序。

## 你需要准备什么

- 一台电脑（Mac 或 Windows 都行，课程会分别给出最稳的路径）。
- 网络。
- **Claude Code 或 Codex**（二选一即可，这是我们全程唯一的主力工具）。
- 一点点耐心。真的只要一点点——因为不用你写代码。

## 我们怎么用 Claude Code / Codex 学习

这门课的核心工作方式，就一句话：

> **你负责想清楚要什么、指挥 AI 怎么做、验收结果对不对；代码由 Claude Code / Codex 来写。**

你会反复用到一个「任务提示词模板」，长这样：

```text
任务目标：我要实现什么功能。
当前状态：现在项目已经做到哪一步。
限制条件：这次只做什么，不做什么。
期望结果：运行后我应该看到什么。
验收标准：我怎么判断你做对了。
```

把需求按这个模板讲清楚，AI 就能帮你干活。你要练的，不是打字写代码，而是**把话说清楚 + 把结果看明白**。

## 为什么我们「先看结果，再理解细节」

传统学法是：先理解 → 再动手 → 最后才看到成果，很多人卡在「理解」这一步就放弃了。

AI 时代可以反过来：**先做出结果 → 从结果里建立直觉 → 需要时再理解细节**。

因为有了 AI，软件开发的重心变了。它不再是一道「从零默写答案」的问答题，而更像**选择题 + 判断题**：

- **选择题**：在多个方案、多个功能、多个优先级里，替 AI 做决定。（先做页面还是先做数据库？这个功能现在做不做？）
- **判断题**：判断 AI 交出来的结果对不对。（页面显示了吗？按钮点了有反应吗？数据刷新后还在吗？AI 拆的任务合理吗？）

这两件事，AI 替不了你，也正是这门课要反复训练你的能力。想清楚了这一点，你就已经站在 AI 开发的正确起点上了。

## 课程地图

{{< cards >}}
  {{< card link="00-introduction" title="第一部分 · AI 开发的新方法" subtitle="为什么这不是传统编程课，以及选择题/判断题思维" icon="light-bulb" >}}
  {{< card link="01-environment" title="第二部分 · 环境准备" subtitle="Mac / Windows 最稳路径，跑起来 Claude Code / Codex" icon="desktop-computer" >}}
  {{< card link="02-first-todo-page" title="第三部分 · 先看到结果" subtitle="做出第一个 Todo 页面，学会验收" icon="eye" >}}
  {{< card link="03-vue-todo" title="第四部分 · 变成前端应用" subtitle="Vue + Tailwind，能增删改的 Todo" icon="template" >}}
  {{< card link="04-flask-api" title="第五部分 · 加入后端" subtitle="Flask，第一次前后端联调" icon="server" >}}
  {{< card link="05-database" title="第六部分 · 加入数据库" subtitle="SQLite 让数据真正保存下来" icon="database" >}}
  {{< card link="06-ai-features" title="第七部分 · 加入 AI 能力" subtitle="拆解 / 总结 / 分类 / 判断优先级" icon="sparkles" >}}
  {{< card link="07-ai-development-workflow" title="第八部分 · 学会指挥 AI 开发" subtitle="需求、拆分、下任务、看结果、验收" icon="chat" >}}
  {{< card link="08-engineering-upgrade" title="第九部分 · 工程化升级" subtitle="组件、数据结构、Pydantic、FastAPI" icon="cog" >}}
  {{< card link="09-docker-deployment" title="第十部分 · Docker 与部署" subtitle="一键启动，上云，域名与 HTTPS" icon="cloud" >}}
  {{< card link="10-review-and-extension" title="第十一部分 · 复盘与扩展" subtitle="完整复盘，扩展到内容生成器 / 知识库 / 小程序" icon="academic-cap" >}}
{{< /cards >}}

---

准备好了就从 [第一部分：AI 开发的新方法]({{< relref "00-introduction.md" >}}) 开始。记住：**不用你会写代码，只要你会想、会指挥、会验收。**
