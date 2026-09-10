---
title: "给 Kopia 装上 AI 大脑"
description: "Kopia 的去重、加密是硬功夫，但 CLI 靠背参数、KopiaUI 也不好用，备份完的数据基本就进了黑箱。HyperFileLens 的 Agent 直接构建在 Kopia 之上，把配置流程收成三步，还接了 AI 引擎 SourceLens 直接读快照——本文是一份从部署到用 AI 提问的完整实操记录。"
author: 老孙正经胡说
date: 2026-09-09T08:00:00+08:00
categories:
  - AI工具实践
tags:
  - AI
  - 备份
  - Kopia
  - 对象存储
  - 开源
  - HyperFileLens
draft: true
---

Kopia 在自建备份圈子里名气不小，内容寻址去重、端到端加密、不锁定存储后端，这几个硬指标很扎实。但吐槽也是真吐槽：CLI 全靠背参数，KopiaUI 也谈不上好用，好几台机器、好几个仓库放一起，全靠自己记，想翻一份半年前的文件还得先 `kopia mount` 出来再找。

HyperFileLens 正是为了解决这个问题而生：用简单的三步流程完成配置，方便用户统一管理；还巧妙地和 AI 结合，直接在备份数据里搜索、阅读、推理，轻松洞察你的备份数据。

这篇文章记录的就是这一整套实操：部署开源项目 [HyperFileLens](https://github.com/HyperBDR/hyperfilelens)，把本地目录备份起来，再接入 AI 模型，最后直接对着自己的备份文件提问。用什么主机、存储用哪家不重要，讲清楚的是这一整套怎么装、怎么配、怎么用——每一步用到的命令、配置字段和实际界面截图都会列出来。

## 需要准备什么

- 一台能跑 Docker 的 Linux 主机（物理机、虚拟机都行，配置要求见下文）；
- 一个阿里云账号，开通 OSS；
- 一台需要备份的机器（本文用 macOS 举例，HyperFileLens 的 Agent 同时支持 Linux、macOS、Windows）；
- 一个阿里云百炼（DashScope）的 API Key，用来接入 DeepSeek 和 Qwen 模型。

流程分两部分：先把 HyperFileLens 部署起来、把数据备份好，再接入模型、开始用 AI 查数据。

## 第一步：准备一台主机

官方给出的最低配置是 4 核 8GB，推荐 8 核 16GB，系统用 Ubuntu 20.04 / 22.04 / 24.04（amd64），`/opt` 目录至少留 20GB 空闲空间。物理机、虚拟机都行，能跑 Docker、能访问公网即可，不需要公网 IP。

> **[待补截图]** 主机的 CPU/内存/磁盘规格

## 第二步：一条命令装好 HyperFileLens

SSH 登录到这台主机，装好 Docker（HyperFileLens 依赖 Docker Engine 24.0.0+ 和 Docker Compose V2 2.20.0+），确认好之后跑安装脚本：

```bash
curl -fsSL https://raw.githubusercontent.com/oneprolabs/hyperfilelens/main/deploy/online/install.sh \
  | sudo bash -s -- --mirror cn
```

国内网络访问 GitHub 不稳定，用 `--mirror cn` 走国内镜像。装完用这条命令确认状态：

```bash
sudo /opt/hyperfilelens/install.sh status
```

如果这台主机开了 ufw 之类的本地防火墙，记得放行 `11442–11445/TCP` 这几个端口，只对内网开放就够。

安装脚本跑完会打印出两个访问地址：

- `HyperFileLens · 11443`：备份、恢复、Insights 和管理控制台；
- `Platform Ops · 11444`：AI 模型配置和平台管理。

同时会打印一个初始邮箱和密码，记下来，登录用得到。地址默认是这台机器的内网 IP。

> **[待补截图]** 安装脚本执行完成后的终端输出，展示两个访问地址和初始邮箱密码

## 第三步：登录控制台，改掉默认密码

浏览器打开 `HyperFileLens · 11443` 对应的地址，语言切到简体中文，选密码登录方式，输入安装输出里的邮箱和密码，登录进去。

登录成功后第一件事：改掉初始密码。顺手确认一下时区设置和系统时间一致，避免后面备份任务的时间戳对不上。

> **[待补截图]** 登录页，展示邮箱密码登录表单

## 第四步：把要备份的电脑接进来

进入 **Protection → Backup Wizard**，点 **Add Source**，选 **Source Host**，操作系统选 macOS（如果是 Windows 或 Linux 机器，这里选对应系统）。

界面会给出一段安装命令，复制到本机终端里执行，等它提示安装完成。回到 Backup Wizard 刷新数据源列表，确认新加的这台机器状态是 **Registered**（已注册）、**Online**（在线）。

> **[待补截图]** Backup Wizard 里数据源列表，展示新增主机的类型、注册状态和在线状态

## 第五步：配置阿里云 OSS 作为备份目标

在阿里云控制台建一个 OSS Bucket，另外建一个 RAM 子账号，只授予这个 Bucket 的读写和列举权限，拿到 AccessKey ID 和 AccessKey Secret——不要用主账号的 AK/SK。

回到 HyperFileLens，在备份配置里点 **Add Repository**，选 **Alibaba Cloud OSS**，依次填：

- Endpoint（按 Bucket 所在地域自动带出）；
- Region；
- Access Key / Secret Key；
- Bucket 名称；
- Object Prefix（比如填 `hfl/`，方便后续在 Bucket 里区分这批数据）。

保存后点验证，等状态变成 **Status: Created**、**Connectivity: Online** 就说明这一步通了。

Secret Key 只在创建时显示一次，截图、聊天记录、代码仓库里都不要留底。

> **[待补截图]** Add Repository 表单，展示 Alibaba Cloud OSS 的 Endpoint/Region/Bucket 配置字段（AK/SK 已打码）

## 第六步：选路径，跑第一次备份

回到数据源列表，点刚才注册的这台机器的编辑图标，把目标仓库指定成上一步建好的 OSS Repository，确认目标列显示出仓库名、存储类型和在线状态。

进入 Backup Setup，展开这台机器的目录树，勾选要备份的工作文件夹，确认它出现在 **Selected Paths** 里。第一次先不设 Backup Policy 和 File Filter，跑通流程要紧，定时策略和排除规则等确认没问题了再加。

Review 页面会把源目录、目标仓库、压缩方式、策略、过滤规则汇总展示一遍，确认无误后创建。回到数据源，确认在线状态没问题，点 **Backup Now**，等任务状态变成 **Succeeded**。

任务跑的过程中不要关掉本机的 Agent，也不要改 OSS 的 AK/SK。

> **[待补截图]** Backup Setup 目录树选择页，以及任务列表中状态为 Succeeded 的备份任务

## 第七步：确认真的备份成功了

进这台机器的详情页，切到 **Snapshot Points** 标签，确认状态是 **Available**，能看到这次快照的大小、还原后大小、文件和目录数量。

再用 **File and Directory Browser** 展开看一下，确认里面能看到具体的文件名和目录结构，跟本机实际内容对得上。

> **[待补截图]** Snapshot Points 列表和文件浏览器展示的目录结构

## 第八步：顺手验证一下能不能恢复

备份和能恢复是两回事，光看快照状态是 Available 不代表数据真的完整。挑一个文件测一下：

进这台机器点 **Restore**，选 **Create New Restore Task**，选中刚才验证过的快照，目标还是这台机器，冲突策略选 **Skip**（避免覆盖本机现有文件），源路径填想恢复的那个文件，目标目录填一个新目录，比如 `~/HFL-Restore-Test`。

确认还原路径无误后提交，等任务状态变成 **Succeeded**，打开恢复出来的文件，跟原文件内容和哈希值核对一致。

这一步过了，说明这套备份不是摆设，真的能在需要的时候取回数据。

> **[待补截图]** Restore 任务的参数配置页和最终 Succeeded 状态

## 第九步：接入 AI 模型

浏览器打开 `Platform Ops · 11444` 对应的地址，用管理员账号登录，进 **AI Engine → AI Models**，点 **Add AI Model**。

这里加两个模型，分工不同：

- **DeepSeek-V3**：处理文本类的问答和推理，走阿里云百炼（DashScope）的 OpenAI 兼容接口；
- **Qwen-VL-Plus**：处理截图、图片这类多模态内容，同样走百炼的兼容接口。

两个模型的 API Base URL 都填百炼的兼容模式地址，Model ID 分别填对应的模型名，API Key 用百炼账号下申请的 Key。保存后点击 **Test Connection**，测通了再把其中一个设成 **Default Agent**（默认用文本模型 DeepSeek-V3，图片类任务会按需调用 Qwen-VL-Plus）。

> **[待补截图]** AI Models 列表，展示 DeepSeek-V3 和 Qwen-VL-Plus 两条记录，状态均为 Active

## 第十步：真正开始"问"自己的数据

回到 `HyperFileLens · 11443`，进 **Insights → AI Copilot**，点 **New Chat**。

选之前配置好的数据源和对应的快照（默认用最新快照），把要分析的文件加进来——可以是某份技术方案，也可以是一批带截图的资料。分析类型选 **Knowledge Q&A**，数据处理方式选 **Public Data Gateway**，确认这次分析基于的是受保护的快照数据，点 **Start Chat**，等数据准备完。

准备好之后就可以直接提问了，比如：

- "把这份 2025 年的方案和现在这份对比一下，接口设计上改了哪些地方？"
- "这几张报销截图里，金额加起来一共多少？"
- "去年那次线上问题的复盘记录里，根因是什么，当时怎么解决的？"

AI 会基于备份里的原始文件直接回答，答案会带上引用来源，能追溯到具体是哪个文件、哪一段内容，不是凭空生成的。这一步会把相关文件内容从 OSS 读回这台机器处理，跨公网的下行流量 OSS 是按量计费的，个人这点数据量基本感觉不到，问得比较勤的话留意一下账单就行。

> **[待补截图]** AI Copilot 对话界面，展示一次真实提问和带引用来源的回答

## 跑完这一圈，到底省下了什么

对比一下直接用 Kopia 命令行或者 KopiaUI 的方式：

- **备份引擎没换**：去重、端到端加密这些 Kopia 自带的硬核能力原样保留，没有推倒重做；
- **配置流程从背命令变成点几下**：加数据源、加存储、点 Backup Now，三步跑完，不用记 Kopia 的 repository connect 参数和策略命令；
- **多机器多仓库有了统一视图**：不用再对着命令行和几个 KopiaUI 分别看状态；
- **AI 直接读原始文件**：不需要提前做 Embedding、建向量库、搭一套 RAG 流水线，SourceLens 直接搜索、阅读、推理 Kopia 快照里的原始文件；
- **模型按需换**：文本用 DeepSeek，图片用 Qwen，哪个模型合适用哪个，不绑定单一供应商；
- **不用给任何云厂商交服务器月租**：只有 OSS 存储按量付费。

这套流程从部署到能用 AI 提问，一次跑下来大概花一到两个小时，之后的备份可以设成定时任务，自己不用再管。

## 开源地址

HyperFileLens 采用 Apache 2.0 协议开源：

- 主项目：<https://github.com/HyperBDR/hyperfilelens>
- AI 引擎 SourceLens：<https://github.com/HyperBDR/sourcelens>
- 遇到问题提 Issue：<https://github.com/HyperBDR/hyperfilelens/issues>

如果不想自己部署，也可以直接用 <https://hyperfilelens.com> 的免费 SaaS 版本，跳过部署这一步，直接从加数据源开始。

## 加入 OneProLabs 开源交流群

如果你在体验过程中遇到问题，或者想参与共建、交流开源经验，欢迎扫码加入微信群。

{{< figure src="/images/backups-help-ai-understand-business/wechat-group-qrcode.webp" alt="OneProLabs 开源交流群微信二维码，扫码加入技术交流、开源共建、资源共享、项目协作社区" caption="扫码加入 OneProLabs 开源交流群" >}}
