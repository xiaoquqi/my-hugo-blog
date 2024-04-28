---
title: Github 2024-04-29 开源项目周报 Top15
date: 2024-04-29T07:11:08+08:00
slug: github-trendings-weekly-20240429
author: 老孙正经胡说
image: /images/ollama-ollama-0.png
tags:
  - github
  - trendings
  - 数量
  - 人
  - 人数
  - 和
  - 语言
  - 项目
  - 模型
  - 开发
  - 创建
  - 周期
  - 关注
  - 贡献
  - 地址
  - 协议
  - 是
  - 类型
  - 微调
  - 大型
  - 开源
  - 并

categories:

draft: false
---


根据Github Trendings的统计，本周(2024-04-29统计)共有15个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Python项目 | 11 |
| TypeScript项目 | 3 |
| Go项目 | 1 |
| Svelte项目 | 1 |
| Jupyter Notebook项目 | 1 |
| Swift项目 | 1 |

## Ollama: 本地大型语言模型设置与运行

* 创建周期：248 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：42421 个
* Fork数量：2724 次
* 关注人数：42421 人
* 贡献人数：138 人
* Open Issues数量：709 个
* Github地址：https://github.com/ollama/ollama.git
* 项目首页: https://ollama.com


![](/images/ollama-ollama-0.png)

Ollama是一个开源项目，帮助用户在本地设置和利用诸如Llama 2、Mistral和Gemma等大型语言模型。

## Dify.AI: 开源的LLM应用程序开发平台

* 创建周期：299 天
* 开发语言：Python, TypeScript
* 协议类型：Other
* Star数量：14984 个
* Fork数量：2007 次
* 关注人数：14984 人
* 贡献人数：79 人
* Open Issues数量：52 个
* Github地址：https://github.com/langgenius/dify.git
* 项目首页: https://dify.ai


![](/images/langgenius-dify-0.png)

Dify.AI是一个开源的LLM应用程序开发平台，集成了后端作为服务和LLMOps。它涵盖了构建生成式AI原生应用所需的核心技术栈，包括内置的RAG引擎。Dify已经帮助构建了超过10万个应用程序，并允许用户基于任何LLMs部署自己的助手API和GPTs版本。

## MyShell: 即时语音克隆和开发者社区

* 创建周期：39 天
* 开发语言：Python
* 协议类型：Other
* Star数量：9975 个
* Fork数量：738 次
* 关注人数：9975 人
* 贡献人数：7 人
* Open Issues数量：37 个
* Github地址：https://github.com/myshell-ai/OpenVoice.git
* 项目首页: https://research.myshell.ai/open-voice


MyShell通过开源技术提供即时语音克隆。加入他们的Discord社区，获取开发者专属讨论和合作机会。

## 简化大型语言模型微调的项目

* 创建周期：331 天
* 开发语言：Python
* 协议类型：Apache License 2.0
* Star数量：17269 个
* Fork数量：2074 次
* 关注人数：17269 人
* 贡献人数：56 人
* Open Issues数量：60 个
* Github地址：https://github.com/hiyouga/LLaMA-Factory.git


该项目旨在简化大型语言模型的微调过程，使其更加高效。它为Colab和本地机器提供了资源。

## Meta Llama 3 模型权重和分词器下载

* 创建周期：37 天
* 开发语言：Python
* 协议类型：Other
* Star数量：7323 个
* Fork数量：506 次
* 关注人数：7323 人
* 贡献人数：19 人
* Open Issues数量：40 个
* Github地址：https://github.com/meta-llama/llama3.git


Meta Llama 3 GitHub 网站提供模型权重和分词器的下载。用户需要访问 Meta Llama 网站，接受许可协议，然后通过电子邮件收到一个签名的 URL，使用提供的脚本开始下载。先决条件包括安装 wget 和 md5sum。链接在 24 小时后过期，并且有下载限制，但如果用户遇到 '403: Forbidden' 等错误，可以重新请求链接。

## 开放式WebUI（前身为Ollama WebUI）

* 创建周期：147 天
* 开发语言：Svelte
* 协议类型：MIT License
* Star数量：7242 个
* Fork数量：641 次
* 关注人数：7242 人
* 贡献人数：59 人
* Open Issues数量：67 个
* Github地址：https://github.com/open-webui/open-webui.git
* 项目首页: https://openwebui.com


开放式WebUI（前身为Ollama WebUI）是一个用户友好的界面，支持LLM运行器，如Ollama和兼容OpenAI的API。

## Code Llama: 大型代码语言模型

* 创建周期：241 天
* 开发语言：Python
* 协议类型：Other
* Star数量：14497 个
* Fork数量：1545 次
* 关注人数：14497 人
* 贡献人数：11 人
* Open Issues数量：88 个
* Github地址：https://github.com/meta-llama/codellama.git


Code Llama是一系列用于代码的大型语言模型，提供了最先进的性能、填充能力、对大型输入上下文的支持，以及编程任务的零射击指令跟随能力。这些模型涵盖了多种应用程序，包括基础模型、Python专业化模型和具有不同参数的指令跟随模型。它们是在16k标记序列上进行训练的，并且在最多100k标记的输入上显示出改进。Code Llama是通过使用更高采样的代码对Llama 2进行微调而开发的，并且对模型的微调版本应用了相当多的安全缓解措施。Code Llama的最新版本现在可供各种规模的个人、创作者、研究人员和企业使用，包括预训练和微调的Llama语言模型的模型权重和起始代码。

## Llama中文社区：Llama3在线体验和微调模型开放

* 创建周期：280 天
* 开发语言：Python
* Star数量：10001 个
* Fork数量：921 次
* 关注人数：10001 人
* 贡献人数：14 人
* Open Issues数量：161 个
* Github地址：https://github.com/LlamaFamily/Llama-Chinese.git
* 项目首页: https://llama.family


Llama中文社区开放了Llama3在线体验和微调模型，实时更新最新的Llama3学习资料，并提供完全开源可商用的中文Llama大模型。

## Llama Recipes: 用于微调Meta Llama模型的存储库

* 创建周期：279 天
* 开发语言：Jupyter Notebook
* Star数量：8589 个
* Fork数量：1195 次
* 关注人数：8589 人
* 贡献人数：56 人
* Open Issues数量：161 个
* Github地址：https://github.com/meta-llama/llama-recipes.git


Llama Recipes是一个提供可扩展库用于微调Meta Llama模型的存储库，还包括示例脚本和笔记本，用于各种用例。它支持在本地、云端和本地运行Meta Llama，并展示了如何在领域适应和构建应用程序中使用模型。

## 快速调优Mistral、Gemma和Llama

* 创建周期：110 天
* 开发语言：Python
* 协议类型：Apache License 2.0
* Star数量：4492 个
* Fork数量：206 次
* 关注人数：4492 人
* 贡献人数：5 人
* Open Issues数量：89 个
* Github地址：https://github.com/unslothai/unsloth.git
* 项目首页: https://unsloth.ai


![](/images/unslothai-unsloth-0.png)

这个开源项目旨在以70%更少的内存使用量，将Mistral、Gemma和Llama的微调速度提高2-5倍。

## Delta: iOS经典游戏模拟器

* 创建周期：3330 天
* 开发语言：Swift
* Star数量：3458 个
* Fork数量：258 次
* 关注人数：3458 人
* 贡献人数：5 人
* Open Issues数量：176 个
* Github地址：https://github.com/rileytestut/Delta.git


![](/images/rileytestut-delta-0.png)

Delta是一个iOS应用程序，允许您模拟并玩多种经典游戏系统的视频游戏，包括Game Boy Advance、Nintendo 64和Nintendo DS。它是GBA4iOS的精神继承者，从头开始重建，具有现代iOS功能和对更多系统的支持。

## Firecrawl: 将网站转换为LLM-ready markdown

* 创建周期：6 天
* 开发语言：TypeScript
* 协议类型：Apache License 2.0
* Star数量：1056 个
* Fork数量：61 次
* 关注人数：1056 人
* 贡献人数：4 人
* Open Issues数量：13 个
* Github地址：https://github.com/mendableai/firecrawl.git
* 项目首页: https://firecrawl.dev


Firecrawl是Mendable.ai的一个开源项目，旨在爬取并将任何网站转换为LLM-ready markdown。该项目处于早期开发阶段，致力于合并自定义模块，以利用清洁数据提高LLM响应的准确性。它还没有准备好完全自行托管。

## 多人国际象棋平台

* 创建周期：8 天
* 开发语言：TypeScript
* Star数量：347 个
* Fork数量：179 次
* 关注人数：347 人
* 贡献人数：11 人
* Open Issues数量：54 个
* Github地址：https://github.com/code100x/chess.git


正在开发一个多人国际象棋平台，允许用户注册、创建或加入比赛，在比赛过程中下棋，并实施类似标准国际象棋评级的评级系统。

## Maestro - 用Opus和Haiku智能分解和执行子代理的框架

* 创建周期：39 天
* 开发语言：Python
* Star数量：867 个
* Fork数量：118 次
* 关注人数：867 人
* 贡献人数：5 人
* Open Issues数量：11 个
* Github地址：https://github.com/Doriandarko/maestro.git


Maestro是一个Python脚本，演示了使用Anthropic API进行AI辅助任务分解和执行工作流程。它利用了两个AI模型，Opus和Haiku，将一个目标分解成子任务，执行每个子任务，并将结果细化为一个连贯的最终输出。

## 考试中心随机分配脚本

* 创建周期：17 天
* 开发语言：Python
* 协议类型：MIT License
* Star数量：272 个
* Fork数量：85 次
* 关注人数：272 人
* 贡献人数：8 人
* Open Issues数量：17 个
* Github地址：https://github.com/moest-np/center-randomize.git


考试中心随机分配脚本旨在为学生分配考试中心。

