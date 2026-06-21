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

周末下午，沙发上，一杯咖啡，顺手拿起手机——然后就这样把代码写完、测试跑完、部署上线？

听起来有点离谱。手机不是开发机，这是常识。它能查文档、看 CI 状态、紧急回一条 PR 评论，但真正的开发工作——写代码、调试、部署、验证结果——还是得坐回电脑前。

我也一直这么以为，直到接触了 Claude Code 的 Remote Control 功能。

这篇是我用自己的项目跑通这件事之后写的记录。

<!-- more -->

## 先说结论

可以。跑通之后大概是这样的状态：

晚上躺着刷手机，突然想到 SourceLens 缺一个分享机制——用户问完问题，答案应该能生成一条公开链接，分享给别人直接查看。这是个完整的功能需求：后端要设计分享表、生成短链、处理权限；前端要有分享按钮、落地页；还要考虑链接过期策略。放以前，这种需求得等坐回电脑、开好几个标签页才能开始。

现在，我把需求说给 Claude，它一个问题一个问题问我确认细节，然后开始写代码、建表、跑测试、提 PR。我躺着审 PR、说"这里改一下"，它改完继续跑。第二天早上坐地铁，功能已经合并了。

博客这边也是——以前从有想法到发出来可能要几天：整理思路、写初稿、排版、发公众号、发其他平台。现在我在手机上把观点说给 Claude，它帮我组织结构、生成初稿，我边通勤边调整，到公司之前已经同步发完了。

整个过程没有碰过电脑。当然，这不是说装个 App 就行——背后有几个前提必须提前打通，少一个都跑不顺。

## 拿什么来验证这件事？

我选了这个博客作为测试项目。

不是因为它简单——恰好相反。一篇文章从写完到发出去，要经过这些环节：本地写 Markdown、Hugo 构建预览、Git 提交推送、GitHub Actions 自动部署到服务器、最后同步发微信公众号。每个环节都有可能出问题，每个环节的结果都需要验证。

如果手机能把这条链路跑顺，我大概就能回答那个问题了。

---

## 先把 Claude 的定位想清楚

在说具体怎么搭之前，有一件事值得单独说：**这套环境里所有的搭建工作，Claude 本身就能帮你完成。**

预览环境的 CI/CD 配置、SSH 鉴权的调试、tmux 的安装和使用——这些不需要你事先都会，你只需要知道要搭什么、为什么要搭。剩下的交给 Claude，让它一步一步帮你走通。

这篇文章的重点也是这个：**讲思路，不是讲操作手册**。把逻辑想清楚了，Claude 就是你的实施工具。

---

## 三件事必须想清楚

### 一、结果必须能在手机上看到

这是最容易被跳过、也最容易踩坑的一步。

很多人上来就配 Remote Control，结果 Claude 说"改完了"，你打开手机——看不到任何变化。因为 `localhost:1313` 在手机上根本打不开，等于盲开发。

解法只有一个：**在动手之前，先搭一个手机能访问的预览环境**。

我的做法是把发布流程拆成两条线：

```
main 分支 push  →  自动部署到 preview.sunqi.site（预览，含草稿）
git tag v*      →  自动部署到 sunqi.site（生产）
```

每次提交，CI 自动跑，手机打开预览地址，直接看到真实渲染效果。确认没问题，打 tag，生产自动部署。

对应的 GitHub Actions 配置，两个独立 workflow：

```yaml
# .github/workflows/preview.yml
name: Deploy to Preview
on:
  push:
    branches: [main]
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

> **踩坑提示**：CI 里的 `REMOTE_HOST` 务必填服务器真实 IP，不要填域名。域名如果经过 Cloudflare 之类的 CDN，SSH 请求会打到 CDN 节点直接超时——我在这里排查了不少时间。

### 二、鉴权必须打通

有了预览环境，Claude 能"看到结果"。但它能帮你干多少活，取决于你给了它多少权限。

鉴权不是可选项，是 Claude 能真正替你执行的前提。

**SSH Key**——让 Claude 直接 SSH 到服务器，查日志、重启服务、排查部署问题，不需要你转述：

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub user@your-server
ssh user@your-server "echo ok"   # 验证免密登录
```

**GitHub CLI**——让 Claude 直接操作仓库：查 Actions 日志、触发重跑、设置变量、管理 PR：

```bash
gh auth login
gh auth status   # 验证
```

这两项打通之后，Claude 的能力边界完全不同。还是拿这篇文章的调试过程举例：CI 部署失败，Claude 直接 `gh run view` 拉日志、定位原因、修改 workflow、重新触发——我在手机上全程旁观，只在关键决策点说"可以"或"换个方案"。鉴权没打通的话，这些步骤每一步都得我手动来。

### 三、会话必须连续

这一点常被忽视，但它决定了手机能不能真正融入你的工作流。

如果直接在终端运行 `claude`，关掉窗口进程就死了。用 tmux 让 Claude Code 跑在后台，断网、切应用、关屏幕，会话都在：

```bash
tmux new-session -s dev      # 新建持久化会话
cd ~/my-project
claude                       # 进入 Claude Code
/rc                          # 开启 Remote Control（也可以用 /remote-control）

# Ctrl+B → D  分离会话（进程继续跑）
# tmux attach -t dev  重新接入
```

开启后，点击 Claude App 或桌面客户端顶部图标，进入 **Code** 页面，就能看到远程 session 列表，找到对应会话点进去直接接管。

但持久不只是"进程不死"，更重要的是**设备之间能无缝接力**。在地铁上开始的任务，到公司坐下来直接在电脑上接着做；晚上想起来，拿手机继续推进——同一个会话、同一段上下文，不用重新交代背景，不用来回登录切换。这才是真正意义上的随时随地。

**平台支持**：iOS 和 Android 均已支持；VS Code 扩展输入 `/rc` 同样可以开启。需要 Claude Pro 订阅（$20/月）及以上，Claude Code v2.1.51+。

![Claude Code Remote Control 工作原理](/images/claude-rc-workflow.svg)

---

## 用起来更顺手的几个技巧

### 语音输入：用第三方输入法，不用 Claude 自带的

Claude App 手机端有原生语音输入，但对中文的支持一直不太友好——准确率不稳定，遇到技术术语问题更明显，中英混输基本不可用。这不是偶发问题，是长期现状。

推荐切换到微信输入法或豆包输入法：

<div style="display:flex;gap:12px;align-items:center;margin:12px 0">
  <img src="/images/wechat-input-icon.png" width="48" height="48" style="border-radius:12px" alt="微信输入法"/>
  <img src="/images/doubao-input-icon.png" width="48" height="48" style="border-radius:12px" alt="豆包输入法"/>
</div>

这两个输入法在中英文混输上做得很扎实——说中文时夹杂几个英文单词或技术术语，识别准确率依然很高，日常开发场景完全够用。按住语音键说完，看一眼文字确认，再发给 Claude，多一步确认比发出乱码再纠错省时间得多。两个都可以试试，找到顺手的用就行。

### 别一次做太大的事：先搭框架，再逐步推进

这是手机端最重要的工作方式，无论写内容还是做开发，思路都一样——**先定结构，再填内容**。

写博客时，先让 Claude 梳理文章大框架，确认逻辑没问题，再一段一段地写。写完一段确认，再写下一段。这篇文章就是这么来的，比一次给出所有需求、最后大幅返工要顺得多。

做功能开发也是同理——先把模块拆清楚，明确每部分要做什么，再逐块推进，而不是把整个需求一股脑扔给 Claude。

手机上打字慢，遇到复杂任务描述不清楚时，可以反过来让 Claude 主动问你：

```
我想实现 [目标]，情况比较复杂，请你先一个问题一个问题问我，
把需求搞清楚再开始做。
```

### Skill：按场景装，缺什么补什么

不需要一次装很多，按自己的场景来：

**内容生产场景**（写文章、发公众号）：`wechat-draft-publisher` 是必装的，能直接把文章推到微信草稿箱，但需要提前配置好公众号的 AppID 和 AppSecret。图片生成类 skill 根据你用的工具选装。

**开发场景**：`superpower` 这类增强型 skill 比较值得装，能明显扩展 Claude Code 的基础操作能力。其他的按需来——不确定要装什么，直接告诉 Claude，让它帮你找到并安装就行。

### 推送通知：长任务不用盯着

`/config` 里开启 **Push when Claude decides**，任务完成或需要你决策时 Claude 主动推通知，不用一直盯屏幕。

---

## 有一件事必须说清楚：人要对结果负责

用手机完成完整开发是完全可行的，但有一点和用不用手机无关——**人必须对最终结果负责**。

AI 能写代码、跑测试、提 PR，但它不会替你承担后果。数据库 migration 跑错了、权限配置出了问题、支付逻辑有漏洞——锅是你的，不是 Claude 的。这跟你在手机上还是电脑前没关系，跟你有没有认真确认有关系。

遇到高风险操作，正确的姿势不是"切回电脑再说"，而是：**不确定就不提交**。

先通过对话把逻辑走一遍——让 Claude 解释每一步在做什么，让它反过来问你每个关键决策点的预期是什么，直到你自己能说清楚整个逻辑，再下达执行指令。如果在电脑前，可以额外通过看代码做一层人工审查；如果在手机上，对话确认同样能达到这个效果，只是需要更耐心一些。

这是人机协同的核心原则：AI 负责执行，人负责判断。偷懒把判断也交出去，是这套工作方式最容易出问题的地方。

---

## 环境清单

| 类别 | 工具 | 说明 |
|------|------|------|
| 持久化会话 | tmux | 进程后台持续运行，支持跨设备接入 |
| 远程控制 | Claude Code v2.1.51+ | Pro 订阅，`claude --rc` 启动 |
| 手机端 | Claude App（iOS / Android） | Code 页面接入，与电脑端同一会话 |
| 预览环境 | 公网可访问的 URL | 手机验证结果的前提 |
| 代码托管权限 | GitHub CLI (`gh auth login`) | Claude 操作 CI/CD 的前提 |
| 服务器权限 | SSH 免密登录 | Claude 远程操作服务器的前提 |
| 输入法 | 微信输入法 / 豆包输入法 | 中英混输准确率高，替代 Claude 原生语音 |

---

回到文章开头的问题：周末下午，沙发上，一杯咖啡，能不能就这样把代码写完、部署上线？

答案是可以。但更准确的说法是——这套方式改变的不是你在哪里工作，而是你什么时候可以开始工作。通勤路上、等人的间隙、出差的酒店，每一个碎片时间都可以真正推进任务，而不只是查查消息、看看状态。

手机不会替代电脑，就像电脑没有替代纸笔一样。它扩展的是边界，而不是替换原有的工作方式。真正改变的，是"必须坐在电脑前才能工作"这个假设——它不再成立了。

---

**参考资料**
- [Claude Code 官方文档：Remote Control](https://code.claude.com/docs/en/remote-control)
- [Stop losing Claude Code sessions: a tmux primer for mobile devs](https://dev.to/jagafarm/stop-losing-claude-code-sessions-a-tmux-primer-for-mobile-devs-2p48)
- [Claude Code on Your Phone | Builder.io](https://www.builder.io/blog/claude-code-mobile-phone)
