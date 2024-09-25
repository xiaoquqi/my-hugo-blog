---
title: Github 2024-09-26 Go开源项目日报 Top10
date: 2024-09-26T07:11:22+08:00
slug: github-trendings-today-20240926
author: 老孙正经胡说
image: /images/grpc-ecosystem-grpc-gateway-0.png
tags:
  - github
  - trendings
  - 数量
  - 人
  - 人数
  - 项目
  - 和
  - 语言
  - 开发
  - 协议
  - 是
  - 创建
  - 周期
  - 类型
  - 关注
  - 贡献
  - 地址
  - 支持
  - 开源
  - 并
  - 进行
  - 实现

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-09-26统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Go项目 | 10 |
| C项目 | 1 |

## Prometheus监控系统和时间序列数据库

* 创建周期：4149 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：52463 个
* Fork数量：8709 次
* 关注人数：52463 人
* 贡献人数：357 人
* Open Issues数量：927 个
* Github地址：https://github.com/prometheus/prometheus.git
* 项目首页: https://prometheus.io/


Prometheus是一个开源的监控系统和时间序列数据库。它从配置的目标收集指标，评估规则表达式，显示结果，并在观察到指定条件时触发警报。其特点包括多维数据模型、强大的查询语言（PromQL）、不依赖于分布式存储、支持拉取和推送模型的时间序列收集、通过服务发现或静态配置进行目标发现、多种图形和仪表板支持，以及对层次和水平联邦的支持。

## Gorilla WebSocket: Go 语言的 WebSocket 实现

* 创建周期：3998 天
* 开发语言：Go
* 协议类型：BSD 2-Clause "Simplified" License
* Star数量：22147 个
* Fork数量：3469 次
* 关注人数：22147 人
* 贡献人数：80 人
* Open Issues数量：42 个
* Github地址：https://github.com/gorilla/websocket.git
* 项目首页: https://gorilla.github.io


Gorilla WebSocket 是一个用于 Go 语言的快速、经过充分测试和广泛使用的 WebSocket 实现。它是 WebSocket 协议的 Go 语言实现。

## gRPC-Go: 高性能、开源的通用RPC框架的Go语言实现

* 创建周期：3356 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：19531 个
* Fork数量：4256 次
* 关注人数：19531 人
* 贡献人数：387 人
* Open Issues数量：133 个
* Github地址：https://github.com/grpc/grpc-go.git
* 项目首页: https://grpc.io


gRPC-Go是gRPC的Go语言实现，是一个高性能、开源的通用RPC框架，将移动和HTTP/2放在首位。它设计高效，并且有很好的文档，易于采用。

## gRPC-Gateway: 将RESTful HTTP API转换为gRPC的工具

* 创建周期：3212 天
* 开发语言：Go
* 协议类型：BSD 3-Clause "New" or "Revised" License
* Star数量：16976 个
* Fork数量：2252 次
* 关注人数：16976 人
* 贡献人数：345 人
* Open Issues数量：130 个
* Github地址：https://github.com/grpc-ecosystem/grpc-gateway.git
* 项目首页: https://grpc-ecosystem.github.io/grpc-gateway/


![](/images/grpc-ecosystem-grpc-gateway-0.png)

gRPC-Gateway 是一个工具，用于生成反向代理服务器，将 RESTful HTTP API 转换为 gRPC。它读取协议缓冲区服务定义，并根据服务定义中的 google.api.http 注释生成服务器，从而同时以 gRPC 和 RESTful 风格提供 API。

## Argo Workflows: Kubernetes上的容器本机工作流引擎

* 创建周期：2474 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：14419 个
* Fork数量：3089 次
* 关注人数：14419 人
* 贡献人数：425 人
* Open Issues数量：1059 个
* Github地址：https://github.com/argoproj/argo-workflows.git
* 项目首页: https://argo-workflows.readthedocs.io/


Argo Workflows是一个专为在Kubernetes上编排并行作业而设计的开源容器本机工作流引擎。它被实现为Kubernetes CRD，允许用户定义工作流程，其中每个步骤都表示为一个容器。它支持将多步骤工作流程建模为一系列任务，或者使用有向无环图（DAG）来捕获任务之间的依赖关系。Argo Workflows特别适用于在Kubernetes上运行机器学习或数据处理的计算密集型作业。此外，它是一个Cloud Native Computing Foundation（CNCF）毕业项目。

## MediaMTX: 一个多功能且不再局限于RTSP协议的即插即用媒体服务器

* 创建周期：1615 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：10339 个
* Fork数量：1353 次
* 关注人数：10339 人
* 贡献人数：68 人
* Open Issues数量：137 个
* Github地址：https://github.com/bluenviron/mediamtx.git


MediaMTX是一个即插即用、零依赖的实时媒体服务器和媒体代理，允许发布、读取、代理、记录和播放视频和音频流。它可以同时在单独的路径上服务多个流，支持不同协议之间的实时流转换，并提供诸如流记录、回放、用户认证和通过API进行控制等功能。它兼容Linux、Windows和macOS，不需要任何依赖或解释器，是一个单独的可执行文件。它以前被称为rtsp-simple-server，并已发展成一个更加多功能且不再局限于RTSP协议的产品。

## Explore Profiles UI: 简化性能分析数据的全新方式

* 创建周期：1365 天
* 开发语言：Go, C
* 协议类型：GNU Affero General Public License v3.0
* Star数量：9927 个
* Fork数量：593 次
* 关注人数：9927 人
* 贡献人数：175 人
* Open Issues数量：331 个
* Github地址：https://github.com/grafana/pyroscope.git
* 项目首页: https://grafana.com/oss/pyroscope/


![](/images/grafana-pyroscope-0.png)

持续性性能分析平台是一个开源项目，引入了Explore Profiles UI，这是一种全新的探索和分析性能分析数据的方式。它提供了一种无需查询且直观的体验，可以可视化性能分析数据，简化了整个过程，无需编写复杂的查询。

![](/images/grafana-pyroscope-1.png)

## OAuth2 代理：多身份提供者认证的反向代理

* 创建周期：2554 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：9490 个
* Fork数量：1562 次
* 关注人数：9490 人
* 贡献人数：349 人
* Open Issues数量：134 个
* Github地址：https://github.com/oauth2-proxy/oauth2-proxy.git
* 项目首页: https://oauth2-proxy.github.io/oauth2-proxy


一个反向代理，提供与Google、Azure、OpenID Connect等多个身份提供者的身份验证。它还充当静态文件服务器，并支持通过电子邮件、域或组进行帐户验证。该项目最初是从bitly/OAuth2_Proxy进行分叉，并自此与原始分支有所不同。它以前托管在pusher/oauth2_proxy，现已更名为oauth2-proxy/oauth2-proxy，所有图像将可在quay.io/oauth2-proxy/oauth2-proxy获得。

## 开源的开发环境管理器

* 创建周期：41 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：4411 个
* Fork数量：150 次
* 关注人数：4411 人
* 贡献人数：19 人
* Open Issues数量：42 个
* Github地址：https://github.com/daytonaio/daytona.git
* 项目首页: https://daytona.io


![](/images/daytonaio-daytona-0.png)

开源的开发环境管理器允许用户通过单个命令激活完全配置的开发环境，支持各种类型和架构的计算机。它还提供配置文件支持、预构建系统、IDE支持、Git提供程序集成、多项目工作区、反向代理集成、可扩展性、安全功能和VPN连接，以确保对所有端口的安全访问。

## k8sgpt: 为每个人赋予 Kubernetes 超能力

* 创建周期：293 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：3871 个
* Fork数量：433 次
* 关注人数：3871 人
* 贡献人数：56 人
* Open Issues数量：28 个
* Github地址：https://github.com/k8sgpt-ai/k8sgpt.git
* 项目首页: http://k8sgpt.ai


k8sgpt 是一个用于扫描 Kubernetes 集群、诊断和处理问题的工具，使用简单的英语进行交流。它将 SRE 经验融入其分析器，并利用人工智能丰富信息。它具有与 OpenAI、Azure、Cohere、Amazon Bedrock 和本地模型的即插即用集成。可以通过 CLI 进行安装。

