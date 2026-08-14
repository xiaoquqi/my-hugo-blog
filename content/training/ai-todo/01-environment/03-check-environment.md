---
title: 8 · 检查 Python 和 Node.js 环境
linkTitle: 8 · 检查 Python 和 Node.js 环境
date: 2026-07-08T00:13:00+08:00
draft: false
author: Ray Sun
tags:
  - AI
  - 零基础
  - WorkBuddy
  - 环境准备
categories:
  - AI应用开发
weight: 3
---

后续课程会使用 Python 和 Node.js，但不必等到运行项目时报错后再处理。

<!--more-->

### 第 1 步：打开运行环境检测

打开 WorkBuddy 设置页，进入「运行环境检测」，检查：

- Python
- Node.js

`[截图：设置 → 运行环境检测]`

### 第 2 步：按需安装

如果提示缺失，直接使用页面提供的安装入口。安装完成后重新检测，确认两项均正常。

### 如果安装失败，怎么反馈给 AI

1. 记录完整错误提示；
2. 关闭并重新打开 WorkBuddy；
3. 再次执行环境检测；
4. 仍然失败时，把错误信息交给 WorkBuddy 分析，可以直接输入：

```text
Python 或 Node.js 环境安装失败。

请根据当前错误信息检查原因，
指导我完成安装，并在最后重新验证环境。
```

### 完成标准

进入下一节前，确认：

- [ ] WorkBuddy 已正常安装并登录；
- [ ] Python 检测正常；
- [ ] Node.js 检测正常。

完成这三项，安装和基础环境准备就结束了。

### 本章小结

Python、Node.js 这两样系统依赖，交给 WorkBuddy 自带的运行环境检测就够了，不用再手动装 Homebrew、WSL 这些东西。三项都绿了，下一节我们正式和 AI 打第一次招呼。
