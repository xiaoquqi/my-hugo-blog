---
title: 用 Claude Code 实现手机端远程开发：从环境搭建到最佳实践
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

真正的移动端开发，不是"在手机上看 Claude 打字"，而是**能在手机上做出决策、验证结果、推进任务**。这两者之间差了一个关键前提：你的开发结果必须能在手机上看到。

本文以这个博客本身的开发流程为例，讲清楚搭建一套完整手机端远程开发环境需要什么，以及如何用它实现真正的随时随地开发。

<!-- more -->

## 为什么单靠 Claude Code Remote Control 还不够

Claude Code 的 Remote Control 功能（2026 年 2 月发布）让你可以用手机接管一个正在运行的本地 Claude Code 会话——发指令、看输出、做决策。

但如果你在开发一个 Web 应用或博客，Claude 告诉你"已经修改完成"，你怎么知道改得对不对？在手机上打开 `localhost:1313`？打不开。去找代码看？还不如回到电脑前。

**没有可以在手机上访问的预览环境，远程开发就是盲开发**。

所以，完整的手机端远程开发环境需要三层配合：

| 层 | 工具 | 作用 |
|----|------|------|
| **指令层** | Claude Code Remote Control | 手机上发指令、看 Claude 工作进度 |
| **持久层** | tmux | 让 Claude Code 进程在后台持续运行 |
| **验证层** | 预览环境（手机可访问的 URL） | 手机上看到真实的渲染结果 |

三层缺一不可。

## 以这个博客为例：我们的完整环境

这篇文章本身就是用这套流程写出来的，以下是整套配置的具体实现。

### 发布流程设计

```
master 分支 push
    └─→ GitHub Actions 自动部署到 preview.sunqi.site（预览环境）

git tag v*
    └─→ GitHub Actions 自动部署到 sunqi.site（生产环境）
```

这样每次提交后，我可以直接在手机上打开预览地址，看到真实的渲染效果——文章格式、图片、代码块、导航——和读者看到的完全一致。确认没问题，打 tag，发布生产。

对应的 GitHub Actions 配置（两个独立的 workflow）：

**预览环境（`.github/workflows/preview.yml`）**：

```yaml
name: Deploy to Preview

on:
  push:
    branches:
      - master

jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-go@v5
        with:
          go-version: '1.23'
          cache: true
      - name: Install Hugo extended
        run: |
          wget -O /tmp/hugo.deb \
            https://github.com/gohugoio/hugo/releases/download/v0.161.1/hugo_extended_0.161.1_linux-amd64.deb
          sudo dpkg -i /tmp/hugo.deb
      - name: Build (with drafts)
        run: hugo --gc --minify --buildDrafts
      - name: Deploy to preview path
        run: |
          rsync -avz --delete \
            -e "ssh -p ${{ vars.REMOTE_PORT }}" \
            public/ \
            ${{ vars.REMOTE_USER }}@${{ secrets.REMOTE_HOST }}:${{ vars.REMOTE_PATH_PREVIEW }}/
```

**生产环境（`.github/workflows/main.yml`）**：

```yaml
name: Deploy to Production

on:
  push:
    tags:
      - 'v*'

# ... 与预览相同，但不加 --buildDrafts，部署到 REMOTE_PATH
```

GitHub 仓库里需要配置的变量：
- `REMOTE_PATH`：生产目录（已有）
- `REMOTE_PATH_PREVIEW`：预览目录（新增）
- `SSH_PRIVATE_KEY` / `REMOTE_HOST` / `REMOTE_PORT` / `REMOTE_USER`：已有

## 搭建 Claude Code Remote Control

有了预览环境，再配合 Remote Control，就能形成完整的远程开发闭环。

![Claude Code Remote Control 工作原理](/images/claude-rc-workflow.svg)

### 前置检查

```bash
# 需要 v2.1.51 或更新
claude --version
claude update

# 必须用 claude.ai 账号登录（不支持纯 API Key）
claude auth login
```

订阅要求：Claude Pro（$20/月）及以上均可，不需要 Max 计划。iOS / Android / 浏览器全平台支持。

### 用 tmux 保持会话存活

这是最常被忽略但最重要的一步。

如果直接在普通终端跑 `claude`，一旦 Terminal 关闭或 SSH 断开，进程就结束了。手机上的指令没有执行环境。tmux 让会话在后台持续运行，断线重连也不丢失。

```bash
# 新建会话
tmux new-session -s dev

# 进入项目目录
cd ~/my-hugo-blog
```

常用快捷键：

| 操作 | 按键 |
|------|------|
| 分离会话（进程保持后台运行） | `Ctrl+B` → `D` |
| 重新接入会话 | `tmux attach -t dev` |
| 查看所有会话 | `tmux ls` |

### 开启 Remote Control

**从新会话开始**（推荐）：

```bash
claude --rc "博客开发"
```

**在已有会话中开启**：

```
/rc 博客开发
```

**服务器模式**（支持多设备并发连接）：

```bash
claude remote-control --name "博客开发"
# 终端显示 URL，按空格键显示二维码
```

### 手机端连接

打开 Claude App → 底部 **Code** 标签 → 找到刚建立的会话（绿点表示在线）。

会话在同步状态下，本机终端和手机可以同时发消息，实时互通。

![Remote Control 的架构模型：本地执行，手机只是窗口](/images/claude-remote-control-how-it-works.png)

### 安全说明

本机不开放任何入站端口。所有消息经由 Anthropic API 中转（TLS 加密），本地文件系统、MCP 工具、项目配置全部在本机，手机端只是一个控制窗口，你的代码不会上传到 Anthropic 的服务器。

## 进阶：推送通知与 CI/CD 集成

### 推送通知

```
/config
```

开启 **Push when Claude decides**，长任务完成或需要你决策时，Claude 会主动推送到手机。你可以把任务扔给它去做，放下手机，等通知。

### 集成 CI/CD 查日志

在 Claude Code 的上下文里，可以直接让 Claude 帮你：
- 查看 GitHub Actions 最近一次构建的失败日志
- 检查线上服务状态
- 分析部署后的错误

出差途中收到监控告警，不用回到电脑前，手机上用 Remote Control 让 Claude 帮你定位和处理。

## 语音输入：最被低估的提效细节

Remote Control + 语音输入，是真正实现"不碰键盘开发"的组合。但有一个坑很多人踩过：

**Claude App 自带的语音识别，中文准确率明显不如微信输入法。**

Claude 原生语音识别对中文夹杂技术术语时表现不稳定，误识率高；微信输入法背后积累了大量中文训练数据，识别准确度要高得多。

**实际推荐的用法**：

1. Claude App 输入框里切换到微信输入法
2. 按住微信语音键说出需求
3. 确认文字无误后发送

多了一步确认，但比用 Claude 原生语音说错了再纠错要快。

实际测试下来，通勤、散步等场景完全可以用语音驱动开发：描述需求、确认方向、做出决策，基本不需要打字。

## 完整环境清单

想复现这套流程，需要准备以下内容：

**设备与工具**

- Mac 或 Linux 开发机（需保持开机和网络）
- tmux（`brew install tmux`）
- Claude Code CLI v2.1.51+，已用 claude.ai 账号登录
- Claude Pro 或以上订阅
- iPhone 或 Android 安装 Claude App

**预览环境**

- 一台可公网访问的服务器（或 Cloudflare Pages / Netlify 等）
- 配置一个预览域名（如 `preview.yoursite.com`）
- CI/CD 配置：master push → 自动部署到预览环境

**可选但推荐**

- 微信输入法（替代 Claude 原生语音识别）
- 手机推送通知（`/config` 里开启）

## 小结

这套流程的核心逻辑是：**手机端能看到的预览 + Claude Code 的远程控制 + 语音输入**，三者缺一不可。

这篇文章本身就是用这套方式完成的：在 Mac 上用 tmux 跑着 Claude Code，手机上通过 Remote Control 发指令，每次提交后在预览环境上确认效果。整个过程不需要坐在电脑前。

如果你有一个正在维护的项目，把预览环境搭起来，然后试试 `claude --rc`，可能会对"在哪儿开发"这件事产生新的看法。

---

**参考资料**

- [Claude Code 官方文档：Remote Control](https://code.claude.com/docs/en/remote-control)
- [Claude Code Mobile: iPhone, Android & SSH (2026) | Sealos Blog](https://sealos.io/blog/claude-code-on-phone/)
- [Claude Code on Your Phone | Builder.io](https://www.builder.io/blog/claude-code-mobile-phone)
