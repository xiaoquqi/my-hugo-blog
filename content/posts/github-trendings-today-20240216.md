---
title: Github 2024-02-16 开源项目日报 Top9
date: 2024-02-16T07:01:19+08:00
slug: github-trendings-today-20240216
author: 老孙正经胡说
image: /images/psf-black-0.png
tags:
  - github
  - trendings
  - 数量
  - 项目
  - 人数
  - 人
  - 和
  - 开发
  - 语言
  - 创建
  - 类型
  - 是
  - 周期
  - 协议
  - 关注
  - 贡献
  - 地址
  - 并
  - 工具
  - 支持
  - 开源
  - 代理

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-02-16统计)共有9个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Python项目 | 4 |
| TypeScript项目 | 3 |
| Rust项目 | 3 |
| Jupyter Notebook项目 | 1 |
| JavaScript项目 | 1 |

## Black：不妥协的Python代码格式化工具

* 创建周期：2146 天
* 开发语言：Python
* 协议类型：MIT License
* Star数量：35977 个
* Fork数量：2371 次
* 关注人数：35977 人
* 贡献人数：413 人
* Open Issues数量：372 个
* Github地址：https://github.com/psf/black.git
* 项目首页: https://black.readthedocs.io/en/stable/


![](/images/psf-black-0.png)

Black 是一种不妥协的 Python 代码格式化工具，提供速度、确定性，并且不受 pycodestyle 对格式的挑剔。它确保代码在不同项目中看起来相同，并通过生成尽可能小的差异，使代码审查更快速。

## Poetry: 简化Python包装和依赖管理

* 创建周期：2179 天
* 开发语言：Python
* 协议类型：MIT License
* Star数量：28492 个
* Fork数量：2248 次
* 关注人数：28492 人
* 贡献人数：439 人
* Open Issues数量：673 个
* Github地址：https://github.com/python-poetry/poetry.git
* 项目首页: https://python-poetry.org


![](/images/python-poetry-poetry-0.png)

Poetry是一个工具，帮助声明、管理和安装Python项目的依赖关系，用简单的基于pyproject.toml的项目格式替换了setup.py，requirements.txt，setup.cfg，MANIFEST.in和Pipfile。

## Hurl：多功能命令行HTTP请求工具

* 创建周期：1266 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：8091 个
* Fork数量：263 次
* 关注人数：8091 人
* 贡献人数：50 人
* Open Issues数量：125 个
* Github地址：https://github.com/Orange-OpenSource/hurl.git
* 项目首页: https://hurl.dev


Hurl是一个多功能的命令行工具，用于使用纯文本运行和测试HTTP请求。它可用于单个和基于会话的请求，并支持链式多个请求、捕获值以及对标头和主体响应进行查询评估。由libcurl支持，Hurl快速、高效，并且支持HTTP/3。它还提供各种测试功能，如不同类型的查询和断言、测试HTTP端点、检查响应字节，并生成各种格式的报告。

## Danswer: 一个开源的问题答案工具

* 创建周期：295 天
* 开发语言：Python, TypeScript
* 协议类型：MIT License
* Star数量：6943 个
* Fork数量：746 次
* 关注人数：6943 人
* 贡献人数：45 人
* Open Issues数量：129 个
* Github地址：https://github.com/danswer-ai/danswer.git
* 项目首页: https://docs.danswer.dev/


![](/images/danswer-ai-danswer-0.png)

Danswer是一个开源工具，允许用户提出问题并获得私人来源支持的答案。它可以连接到诸如Slack、GitHub和Confluence等各种工具。Danswer的部署非常简单，可以在本地运行，也可以通过单个docker compose命令部署在虚拟机上。它还内置了对Kubernetes的部署支持，并提供相关文件供参考。

## GitButler: 允许多分支工作的灵活git客户端

* 创建周期：379 天
* 开发语言：TypeScript, Rust
* 协议类型：Other
* Star数量：2169 个
* Fork数量：87 次
* 关注人数：2169 人
* 贡献人数：15 人
* Open Issues数量：59 个
* Github地址：https://github.com/gitbutlerapp/gitbutler.git
* 项目首页: https://gitbutler.com


![](/images/gitbutlerapp-gitbutler-0.png)

GitButler是一个git客户端，允许同时在多个分支上工作，将文件更改组织到单独的分支中，并将分支单独推送到远程或创建拉取请求。

## ZLUDA：在AMD GPU上运行CUDA应用程序的开源项目

* 创建周期：1503 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：4172 个
* Fork数量：181 次
* 关注人数：4172 人
* 贡献人数：8 人
* Open Issues数量：29 个
* Github地址：https://github.com/vosen/ZLUDA.git


ZLUDA是一个开源项目，它可以在AMD GPU上以接近原生性能运行未经修改的CUDA应用程序。目前处于alpha质量阶段，但已确认可以与各种原生CUDA应用程序一起使用，如Geekbench、3DF Zephyr、Blender等。

## 稳定级联

* 创建周期：22 天
* 开发语言：Jupyter Notebook
* 协议类型：MIT License
* Star数量：2623 个
* Fork数量：142 次
* 关注人数：2623 人
* 贡献人数：3 人
* Open Issues数量：37 个
* Github地址：https://github.com/Stability-AI/StableCascade.git


Stable Cascade是一个开源项目，提供基于Würstchen架构的训练和推断脚本，以及各种模型。它实现了高达42的压缩因子，允许将1024x1024的图像编码为24x24，同时保持清晰的重建。该模型旨在提高效率，从而实现更快的推断和更便宜的训练。它还支持已知的扩展，如微调、LoRA、ControlNet和IP-Adapter，并在视觉和评估方面展现了令人印象深刻的结果。

## AgentKit: 基于LangChain的代理应用程序快速构建工具包

* 创建周期：21 天
* 开发语言：TypeScript, Python
* 协议类型：MIT License
* Star数量：550 个
* Fork数量：56 次
* 关注人数：550 人
* 贡献人数：3 人
* Open Issues数量：3 个
* Github地址：https://github.com/BCG-X-Official/agentkit.git
* 项目首页: https://agentkit.infra.x.bcg.com/


AgentKit是由BCG X开发的基于LangChain的入门套件，用于构建代理程序。它允许开发人员快速尝试使用美观的用户界面构建受限代理架构，并构建可扩展到生产级MVP的全栈基于聊天的代理程序。该工具包提供的优势包括快速构建高质量的代理应用程序，为代理设计的灵活的响应式UI/UX，专注于可靠性，并设置为可扩展，具有现成的队列管理、认证、缓存和监控。

## Mario Kart 3.js - JavaScript/WebGL 马里奥卡丁车

* 创建周期：24 天
* 开发语言：JavaScript
* 协议类型：MIT License
* Star数量：607 个
* Fork数量：69 次
* 关注人数：607 人
* 贡献人数：3 人
* Open Issues数量：4 个
* Github地址：https://github.com/Lunakepio/Mario-Kart-3.js.git
* 项目首页: https://mario-kart-3-js.vercel.app


Mario Kart 3.js是一个旨在使用JavaScript和WebGL重新创建马里奥卡丁车游戏的开源项目。尽管项目仍在进行中，但大约已完成了50%的工作。这是一项耗时的工作，但开发人员鼓励用户享受到目前为止所取得的进展。

