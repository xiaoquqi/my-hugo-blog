---
title: 7 · 安装并登录 WorkBuddy
linkTitle: 7 · 安装并登录 WorkBuddy
date: 2026-07-08T00:12:00+08:00
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
---

把下载好的安装包，变成一个能正常打开、登录好的 WorkBuddy。Windows 和 macOS 的步骤不太一样，分别说清楚。

<!--more-->

### 第 2 步：完成安装

#### Windows

运行安装程序，按照向导完成安装。

如果 C 盘空间不足，可以在安装时将 WorkBuddy 安装到 D 盘，例如：

```text
D:\Applications\WorkBuddy
```

`[截图：Windows 安装位置选择]`

需要注意：

> ⚠️ **WorkBuddy 安装到 D 盘，不代表后续所有运行环境和缓存都会自动保存到 D 盘。**

因此，开始课程前仍应保证系统盘有一定可用空间。

安装完成后，打开 WorkBuddy 并完成登录。

`[截图：Windows 登录页面]`

#### macOS

先打开「关于本机」，查看芯片类型：

- Apple M 系列芯片：下载 ARM64 版本；
- Intel 处理器：下载 X64 版本。

下载 `.dmg` 文件后，将 WorkBuddy 拖入「应用程序」文件夹并打开。

`[截图：macOS 版本选择]`

`[截图：拖入应用程序文件夹]`

安装完成后，按照提示登录。

### 本章小结

Windows 和 macOS 装法不同，但目标一致：装好、打开、登录成功。下一节我们检查 Python 和 Node.js 环境。
