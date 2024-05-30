---
title: Github 2024-05-31 开源项目日报 Top10
date: 2024-05-31T07:01:33+08:00
slug: github-trendings-today-20240531
author: 老孙正经胡说
image: /images/danielmiessler-fabric-0.png
tags:
  - github
  - trendings
  - 数量
  - 人数
  - 人
  - 项目
  - 开发
  - 语言
  - 创建
  - 贡献
  - 和
  - 是
  - 周期
  - 关注
  - 地址
  - 开源
  - 协议
  - 类型
  - 客户端
  - 生成
  - 中
  - 旨在

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-05-31统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Python项目 | 4 |
| TypeScript项目 | 3 |
| Jupyter Notebook项目 | 2 |
| Vue项目 | 1 |
| Cuda项目 | 1 |
| Elixir项目 | 1 |

## 简单、纯净的C/CUDA中的LLM培训

* 创建周期：3 天
* 开发语言：Cuda
* 协议类型：MIT License
* Star数量：9433 个
* Fork数量：789 次
* 关注人数：9433 人
* 贡献人数：8 人
* Open Issues数量：18 个
* Github地址：https://github.com/karpathy/llm.c.git


LLM在简单的、纯净的C/CUDA中进行培训，无需像PyTorch或cPython这样庞大的依赖。该项目旨在提供干净、单文件实现，能够立即编译和运行，并且能够匹配PyTorch的性能。目前的工作包括直接的CUDA实现以提高速度，使用SIMD指令优化CPU版本，以及探索更现代的架构，如Llama2和Gemma。

## Fabric: 用人工智能增强人类能力的开源框架

* 创建周期：40 天
* 开发语言：Python, JavaScript
* 协议类型：MIT License
* Star数量：5128 个
* Fork数量：406 次
* 关注人数：5128 人
* 贡献人数：22 人
* Open Issues数量：2 个
* Github地址：https://github.com/danielmiessler/fabric.git


![](/images/danielmiessler-fabric-0.png)

Fabric 是一个开源框架，旨在利用人工智能增强人类能力。它提供了将问题分解为组件的哲学，并提供了一种提示的框架方法。该框架包括快速入门指南、设置 fabric 客户端、使用模式、创建 fabric mill、结构、组件、CLI-native 特性、直接调用模式、示例以及主要贡献者的详细信息。

## ChatTTS：日常对话生成式语音模型

* 创建周期：4 天
* 开发语言：Jupyter Notebook
* 协议类型：Other
* Star数量：8202 个
* Fork数量：780 次
* 关注人数：8202 人
* 贡献人数：2 人
* Open Issues数量：91 个
* Github地址：https://github.com/2noise/ChatTTS.git
* 项目首页: https://2noise.com/


ChatTTS是一个为日常对话场景设计的生成式语音模型，例如LLM助手。它支持英语和中文两种语言，并且经过了超过100,000小时的中英文数据训练。HuggingFace上的开源版本是一个40,000小时的预训练模型，不包括SFT。

## YOLOv10: 实时端到端目标检测

* 创建周期：4 天
* 开发语言：Python
* 协议类型：GNU Affero General Public License v3.0
* Star数量：1352 个
* Fork数量：107 次
* 关注人数：1352 人
* 贡献人数：119 人
* Open Issues数量：27 个
* Github地址：https://github.com/THU-MIG/yolov10.git
* 项目首页: https://arxiv.org/abs/2405.14458v1


YOLOv10 是一个开源的实时端到端目标检测项目。YOLOv10 的官方PyTorch实现已经推出，已更新了新的检查点、类名，并集成到X-AnyLabeling中。此外，还提供了Transformers.js、colab、HuggingFace的演示，以及不同YOLOv10模型的onnx权重。

## LlamaFS: 自组织文件系统

* 创建周期：18 天
* 开发语言：Jupyter Notebook, TypeScript
* 协议类型：MIT License
* Star数量：1248 个
* Fork数量：72 次
* 关注人数：1248 人
* 贡献人数：4 人
* Open Issues数量：13 个
* Github地址：https://github.com/iyaja/llama-fs.git


LlamaFS是一个开源的自组织文件系统，旨在提供高效可扩展的文件存储和检索。它利用自组织的方法在存储节点集群中分发和管理文件数据，优化性能和可靠性。

## XIAOJUSURVEY：快速打造专属问卷系统

* 创建周期：209 天
* 开发语言：TypeScript, Vue
* 协议类型：Apache License 2.0
* Star数量：836 个
* Fork数量：110 次
* 关注人数：836 人
* 贡献人数：12 人
* Open Issues数量：21 个
* Github地址：https://github.com/didi/xiaoju-survey.git
* 项目首页: https://xiaojusurvey.didi.cn


![](/images/didi-xiaoju-survey-0.png)

XIAOJUSURVEY是一套轻量、安全的问卷系统基座，提供面向个人和企业的一站式产品级解决方案，快速满足各类线上调研场景。内部系统已沉淀40+种题型，累积精选模板100+，适用于市场调研、客户满意度调研、在线考试、投票、报道、测评等众多场景。数据能力上，经过上亿量级打磨，沉淀了分题统计、交叉分析、多渠道分析等在线报表能力，快速满足专业化分析。开源项目以打造调研基座为核心，围绕平台能力、工程架构、研发体系进行建设，大家可以快速打造专属问卷系统：快速了解生态发展理念。

## GoogleApis: Elixir客户端库访问Google API

* 创建周期：2471 天
* 开发语言：Elixir
* 协议类型：Apache License 2.0
* Star数量：846 个
* Fork数量：315 次
* 关注人数：846 人
* 贡献人数：21 人
* Open Issues数量：207 个
* Github地址：https://github.com/googleapis/elixir-google-api.git
* 项目首页: https://hex.pm/users/google-cloud


GoogleApis 是一个包含 Elixir 客户端库以访问 Google API 的存储库。这些客户端库位于 clients/ 目录下，每个客户端库都有自己的 README。主文件夹包含生成这些客户端库所需的代码。重要提示：这些生成的客户端仍在开发中，应被视为实验性产品！

## MusePose: 一个姿势驱动的虚拟人图像到视频框架

* 创建周期：7 天
* 开发语言：Python
* 协议类型：Other
* Star数量：653 个
* Fork数量：32 次
* 关注人数：653 人
* 贡献人数：3 人
* Open Issues数量：14 个
* Github地址：https://github.com/TMElyralab/MusePose.git


MusePose是一个受姿势等信号控制的虚拟人图像到视频生成框架。它是Muse开源系列的最后一个构建模块，旨在实现具有全身运动和互动能力的虚拟人生成。该项目感谢AnimateAnyone的学术论文和Moore-AnimateAnyone的代码库对AIGC社区和MusePose发展的贡献。

## V-Express: 条件性丢失用于渐进式肖像视频生成

* 创建周期：10 天
* 开发语言：Python
* Star数量：486 个
* Fork数量：45 次
* 关注人数：486 人
* 贡献人数：1 人
* Open Issues数量：11 个
* Github地址：https://github.com/tencent-ailab/V-Express.git


V-Express是一个开源项目，旨在利用参考图像、音频和一系列V-Kps图像生成说话头视频。它利用条件性丢失来进行渐进式训练，用于肖像视频生成。

## 人工智能销售代表聊天机器人

* 创建周期：6 天
* 开发语言：TypeScript
* Star数量：157 个
* Fork数量：62 次
* 关注人数：157 人
* 贡献人数：1 人
* Open Issues数量：2 个
* Github地址：https://github.com/webprodigies/corinna-ai.git


该项目是一个开源的人工智能聊天机器人，旨在充当销售代表。它仅限于教育用途许可，并且商业用途需要单独购买许可。

