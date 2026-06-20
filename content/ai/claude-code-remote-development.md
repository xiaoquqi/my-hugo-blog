---
title: 手机能成为真正的开发终端吗？我用这个博客验证了一下
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

这个问题我想了很久：手机能不能成为真正的开发终端？

不是"查查文档、看看监控"那种意义上的，而是完整意义上的——写代码、调试、部署、验证结果，整个研发闭环都在手机上完成。听说有 Anthropic 的工程师每天趴在沙发上，靠手机和 Claude Code 对话完成日常开发工作（来源待核实，欢迎知道的朋友补充）。

这篇文章是我自己验证这个问题的记录。

<!-- more -->

## 先说结论

可以，但有几个前提条件必须提前准备好，缺一不可。本文的重点不是某个工具的使用说明，而是这套环境的搭建逻辑——把这个想清楚，无论你开发的是博客、业务系统还是 API 服务，流程都是一样的。

## 我用来验证的场景

我选了一个自己日常在维护的项目：这个博客。

看起来简单，但实际涉及的链路不短：Markdown 写作、Hugo 构建、Git 版本管理、SSH 部署到服务器、CI/CD 自动化、微信公众号同步发布。这个场景的复杂度足够有代表性，跑通了，其他系统开发同理。

---

## 前提一：先把预览环境建好

**这是最容易被忽视、也最关键的一步。**

很多人上来就折腾 Remote Control，结果 Claude 说"修改完成了"，你根本不知道改得对不对——手机打不开 `localhost:1313`，看不到渲染结果，等于盲开发。

正确的做法是：**在动手之前，先搭一个手机能访问的预览环境**。

我的方案是把发布流程拆成两条线：

```
master 分支 push  →  自动部署到 preview.sunqi.site（预览，含草稿）
git tag v*        →  自动部署到 sunqi.site（生产）
```

每次提交后，用手机打开预览地址，直接看到真实渲染效果。确认没问题，打 tag，发布生产。

对应的 GitHub Actions 配置很简单，两个独立的 workflow 文件：

```yaml
# .github/workflows/preview.yml
name: Deploy to Preview
on:
  push:
    branches: [master]
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Build
        run: hugo --gc --minify --buildDrafts
      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_rsa
          chmod 600 ~/.ssh/id_rsa
          echo "StrictHostKeyChecking no" >> ~/.ssh/config
      - name: Deploy
        run: |
          rsync -avz --delete \
            -e "ssh -p ${{ vars.REMOTE_PORT }} -o StrictHostKeyChecking=no" \
            public/ \
            ${{ vars.REMOTE_USER }}@${{ secrets.REMOTE_HOST }}:${{ vars.REMOTE_PATH_PREVIEW }}/
```

> **调试提示**：CI 里的 `REMOTE_HOST` 务必填服务器真实 IP，而不是域名。域名可能经过 CDN（比如 Cloudflare），SSH 请求到了 CDN 就超时了——这个坑我踩过，排查花了不少时间。

---

## 前提二：把鉴权打通，这才是核心

光有 Remote Control 还不够。Claude Code 在手机上能帮你干多少活，完全取决于你给了它多少权限。

**必须提前配置好的鉴权：**

**SSH Key**——让 Claude 可以直接 SSH 到你的服务器，查日志、重启服务、排查问题，不需要你手动操作。

```bash
# 把公钥放到服务器
ssh-copy-id -i ~/.ssh/id_rsa.pub user@your-server
# 验证免密登录
ssh user@your-server "echo ok"
```

**GitHub CLI**——让 Claude 可以直接操作 GitHub，查 Actions 日志、设置变量、管理 PR，这些在手机上自己操作非常低效。

```bash
gh auth login
# 验证
gh auth status
```

这一步的重要性怎么强调都不过分。以这篇文章的调试过程为例：CI 部署失败，Claude 直接通过 `gh run view` 拉取日志、分析原因、修改 workflow、重新触发，整个过程我在手机上全程旁观，只需要在关键决策点说"可以"或"换个方案"。如果 GitHub 权限没打通，这些步骤每一步都得我手动来。

---

## 第三步：tmux + Claude Code Remote Control

鉴权打通之后，再来配 Remote Control。

**为什么需要 tmux？**

如果直接在终端运行 `claude`，关掉 Terminal 窗口进程就死了，手机发的指令没有执行环境。tmux 让 Claude Code 在后台持续运行，断网重连也不丢失。

```bash
# 新建持久化会话
tmux new-session -s dev

# 进入项目目录，启动 Remote Control
cd ~/my-project
claude --rc "项目名称"
```

常用 tmux 快捷键：

| 操作 | 按键 |
|------|------|
| 分离会话（后台运行） | `Ctrl+B` → `D` |
| 重新接入 | `tmux attach -t dev` |
| 查看所有会话 | `tmux ls` |

启动后终端会显示一个会话 URL，按**空格键**显示二维码，用手机扫码即可在 Claude App 里接入。

![Claude Code Remote Control 工作原理](/images/claude-rc-workflow.svg)

**平台支持**：iOS 和 Android 均已支持；VS Code 扩展输入 `/rc` 同样可以开启。需要 Claude Pro 订阅（$20/月）及以上，Claude Code v2.1.51+。

---

## 让手机端体验真正好用的几个技巧

### 技巧一：用微信输入法替代 Claude 原生语音

Claude App 自带的语音识别，中文准确率相当不稳定，夹杂技术术语时问题更明显。

微信输入法的语音转文字在中文识别上要好得多——切换到微信输入法，按住语音键说完，看一眼文字确认无误，再发给 Claude。多了一步确认，但比发出去乱码再纠错省时间得多。

### 技巧二：复杂需求让 Claude 来问你

遇到需要交代大量背景的复杂任务时，不要试图一次性描述清楚——手机上打字太慢，说不清楚还容易遗漏。

换个方向：**让 Claude 一个问题一个问题地问你**。

```
我想实现 [目标]，但情况比较复杂，请你先一个问题一个问题问我，
把需求搞清楚再开始做。
```

这个体验比直接给 Claude 一大段需求描述要好得多，也比 Codex 那种模式更符合移动端的交互节奏——你只需要回答，不需要组织。

### 技巧三：提前安装好必要的 Skill

Claude Code 支持通过 Skill 扩展能力。不需要装很多，1-2 个能覆盖你核心研发流程的就够。

我自己用的：
- **superpower**：增强 Claude Code 的基础操作能力
- **openspecs**：处理 API 规范和接口文档相关的任务

原则是：能覆盖你研发流程的关键环节就够了，不要为了装而装。

### 技巧四：推送通知

在 Claude Code 里运行 `/config`，开启 **Push when Claude decides**。长任务跑完或需要你决策时，Claude 会主动推送通知到手机，不用一直盯着屏幕。

---

## 一个必须说清楚的边界

手机上能做的事越来越多，但有一类情况我仍然建议回到电脑前处理：**涉及复杂逻辑判断、高风险操作的代码审查**。

AI 很强，但不会替你坐牢。数据库 migration、权限变更、支付相关逻辑——这些在手机小屏幕上草草确认，风险是你的。

比较合适的做法：在手机上让 Claude 把方案整理成文字，自己通过对话逐步确认逻辑，真正执行前切回电脑完整审查一遍。

---

## 完整环境清单

| 类别 | 工具 | 说明 |
|------|------|------|
| 持久化会话 | tmux | 防止终端关闭导致进程退出 |
| 远程控制 | Claude Code v2.1.51+ | Pro 订阅，`claude --rc` 启动 |
| 手机端 | Claude App（iOS / Android） | 扫码接入 |
| 预览环境 | 公网可访问的 URL | 手机验证结果的关键 |
| 代码托管权限 | GitHub CLI (`gh auth login`) | Claude 操作 CI/CD 的前提 |
| 服务器权限 | SSH 免密登录 | Claude 远程操作服务器的前提 |
| 输入法 | 微信输入法语音 | 替代 Claude 原生语音识别 |

---

这套流程跑通之后，我的日常开发节奏有了明显变化：通勤时推进任务、等待时处理 review、出差时处理线上问题，不再需要等到坐回电脑前。

手机不会完全替代电脑，但它可以把"必须坐在电脑前"这个限制，缩小到真正需要精细操作的那部分。

---

**参考资料**
- [Claude Code 官方文档：Remote Control](https://code.claude.com/docs/en/remote-control)
- [Stop losing Claude Code sessions: a tmux primer for mobile devs](https://dev.to/jagafarm/stop-losing-claude-code-sessions-a-tmux-primer-for-mobile-devs-2p48)
- [Claude Code on Your Phone | Builder.io](https://www.builder.io/blog/claude-code-mobile-phone)
