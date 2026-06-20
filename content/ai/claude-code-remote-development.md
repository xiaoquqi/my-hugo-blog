---
title: 用 Claude Code Remote Control 实现移动端开发：随时随地，解放双手
date: 2026-06-20T08:00:00+08:00
slug: "claude-code-remote-development"
author: 老孙正经胡说
categories:
  - AI工具实践
tags:
  - Claude Code
  - 远程开发
  - 移动开发
  - tmux
  - AI编程
draft: false
---

2026 年 2 月，Anthropic 正式发布了 Claude Code Remote Control 功能。这不是一个独立的产品，而是 Claude Code CLI 内置的一项能力：让你在任意设备上接管一个正在运行的本地开发会话。拿起手机，就能继续刚才在电脑前做到一半的工作。

<!-- more -->

本文记录我实际使用这套工作流的体验，以及一些让它真正好用起来的实用技巧——包括一个被很多人忽略的语音输入细节。

## 它是怎么工作的

很多人第一反应是"把代码传到云端运行"，但 Remote Control 的设计完全相反。

![Claude Code Remote Control 工作原理](/images/claude-rc-workflow.svg)

**你的代码始终运行在本地机器上**。Remote Control 只是在你的 Claude Code 实例和手机/浏览器之间建立了一条加密的消息通道（经由 Anthropic API 中转，全程 TLS 加密，本机不开放任何入站端口）。你的本地文件系统、MCP 工具、项目配置全部保留，手机端只是一个"窗口"。

![Remote Control 架构对比：本地执行 vs 云端执行](/images/claude-remote-control-terminal-vs-cloud.png)

## 平台支持现状

截至目前：

- **iOS 客户端**：完整支持
- **Android 客户端**：完整支持（2026 年与 iOS 同步开放）
- **Web 浏览器**：支持，访问 [claude.ai/code](https://claude.ai/code) 即可
- **VS Code 扩展**：支持 `/remote-control` 命令

订阅要求：**Claude Pro 及以上**（$20/月起）均可使用，不需要 Max 计划。

> 注意：Team 和 Enterprise 计划默认关闭，需要管理员在后台手动开启。

## 前置准备

开始之前确认两件事：

```bash
# 1. 检查版本（需要 v2.1.51 或更新）
claude --version

# 如版本过低，更新
claude update

# 2. 确认已用 claude.ai 账号登录（不支持纯 API Key 登录）
claude auth login
```

## 核心工作流：三步搭建远程开发环境

### 第一步：用 tmux 创建持久化会话

这一步是整个工作流的基础，也是最容易被跳过却最重要的一步。

**为什么需要 tmux？**

如果直接在普通终端里运行 `claude`，一旦关闭 Terminal 窗口或 SSH 断开，进程就结束了——你在手机上发送的指令没有任何地方可以执行。tmux 让会话在后台持续存活，即使你关掉 Terminal 窗口，Claude Code 仍然在后台运行。

```bash
# 创建一个命名会话（名字自定）
tmux new-session -s dev

# 进入项目目录
cd ~/your-project
```

常用 tmux 快捷键备忘：

| 操作 | 命令 |
|------|------|
| 从会话中"分离"（让它继续在后台跑） | `Ctrl+B` 然后 `D` |
| 重新连回已有会话 | `tmux attach -t dev` |
| 查看所有会话 | `tmux ls` |

### 第二步：启动 Claude Code 并开启 Remote Control

有三种方式，根据你的场景选择：

**方式一：服务器模式**（推荐，支持多设备同时连接）

```bash
claude remote-control --name "我的项目"
```

终端会显示一个会话 URL，按**空格键**切换显示二维码。用手机扫码即可直接在 Claude App 里打开这个会话。

**方式二：交互模式**（本机和手机同时操作）

```bash
# 启动时就开启 Remote Control
claude --remote-control

# 或简写
claude --rc
```

这种模式下，你可以在终端输入指令，同时手机端也可以发消息，两边实时同步。

**方式三：在已有会话中临时开启**

如果你已经在跑一个 Claude Code 会话，不想中断，直接在会话里输入：

```
/rc
```

或者：

```
/remote-control 我的项目名称
```

这会把当前的对话历史也带过去，无缝切换。

### 第三步：手机端连接

打开 iPhone 或 Android 上的 Claude App，点击底部导航栏的 **Code** 标签，会看到所有当前活跃的 Remote Control 会话列表，找到你刚建立的会话点进去就好。

绿色圆点表示会话在线，灰色表示主机已断开。

![Claude Code Remote Control 整体架构](/images/claude-remote-control-how-it-works.png)

## 进阶能力

### 手机推送通知

当 Claude Code 完成一个耗时任务，或者需要你做决策时，可以给手机推送通知。在终端里运行 `/config`，开启 **Push when Claude decides** 选项即可。

这意味着你可以把一个复杂任务扔给 Claude，然后放下手机去干别的事，它做完了会主动通知你。

### 与 CI/CD 系统打通

在 Claude Code 的上下文里可以直接整合 GitHub Actions、云平台日志 API 等，让 Claude 帮你：

- 拉取最近一次 CI 构建的失败日志并分析原因
- 检查生产环境的服务状态
- 对比部署前后的配置差异

整个过程在手机上完成，不需要打开浏览器翻后台。出差途中收到线上报警，能直接用手机排查和处理，不用等回到电脑前。

### VS Code 集成

如果你在 VS Code 里开发，安装 Claude Code 扩展后，在提示框输入 `/rc` 即可开启。VS Code 的 Remote Control 会在顶部显示一个连接状态条，点击可以直接跳转到 Web 端的会话。

## 语音输入：一个让体验大幅提升的细节

Remote Control 配合语音输入，理论上可以实现"不碰键盘开发"。但这里有一个被很多人踩过的坑：

**Claude App 自带的语音识别，中文识别效果远不如微信输入法。**

在实际使用中，Claude 原生的语音识别对中文的准确率相当不稳定，尤其是夹杂技术术语时，误识率很高。相比之下，微信输入法的语音转文字在中文识别上准确度要高得多（背后积累了大量中文训练数据）。

**推荐的使用方式**：

1. 在 Claude App 的输入框里，切换到微信输入法
2. 用微信输入法的语音输入说出你的需求
3. 确认文字内容正确后再发送给 Claude

这多了一步"确认文字"的动作，但比直接用 Claude 原生语音发出去再纠错要省时间得多。

实际体验下来，这套方式可以应对大多数通勤、散步场景下的开发需求：描述需求、查看进度、做出决策，基本上都不需要动手打字。

## 注意事项

| 限制 | 说明 |
|------|------|
| 主机进程必须保持运行 | Claude Code 是本地进程，关机或进程终止会断开会话（tmux 可避免误关闭） |
| 网络断开超 10 分钟 | 会话超时退出，需重新运行 `claude remote-control` |
| 不支持 API Key 登录 | 必须用 claude.ai 账号（OAuth）登录才能使用 Remote Control |
| 每个进程同时只支持一个远程会话 | 需要多会话并发时使用服务器模式 (`--spawn worktree`) |

## 小结

Claude Code Remote Control 解决的核心问题是：**让你在不坐到电脑前的情况下，也能对一个正在进行的开发任务做实质性推进**。

对我而言，最大的改变是出差和通勤时不再是完全断线状态，能够持续推进一些原本只能等回到工位才能处理的问题。

如果你已经在用 Claude Code，`claude remote-control` 这个命令值得今天就试试。配合 tmux + 微信语音输入，能快速找到一套适合自己的移动开发节奏。

---

**参考资料**

- [Claude Code 官方文档：Remote Control](https://code.claude.com/docs/en/remote-control)
- [Claude Code Mobile: iPhone, Android & SSH (2026) | Sealos Blog](https://sealos.io/blog/claude-code-on-phone/)
- [Claude Code on Your Phone | Builder.io](https://www.builder.io/blog/claude-code-mobile-phone)
