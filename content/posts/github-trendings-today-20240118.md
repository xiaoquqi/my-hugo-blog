---
title: Github 2024-01-18 Go开源项目日报 Top10
date: 2024-01-18T07:11:42+08:00
slug: github-trendings-today-20240118
author: 老孙正经胡说
image: /images/grpc-ecosystem-grpc-gateway-0.png
tags:
  - github
  - trendings
  - 数量
  - 人数
  - 人
  - 项目
  - 和
  - 开发
  - 语言
  - 并
  - 创建
  - 周期
  - 协议
  - 关注
  - 贡献
  - 地址
  - 是
  - 类型
  - 用于
  - 工具
  - 开源
  - 中

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-01-18统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Go项目 | 10 |
| JavaScript项目 | 1 |

## Trivy: 多功能安全扫描工具

* 创建周期：1743 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：20035 个
* Fork数量：2008 次
* 关注人数：20035 人
* 贡献人数：345 人
* Open Issues数量：202 个
* Github地址：https://github.com/aquasecurity/trivy.git
* 项目首页: https://aquasecurity.github.io/trivy


Trivy是一款全面而多功能的安全扫描工具，用于查找容器、Kubernetes、代码仓库、云等中的漏洞、配置错误、秘密和SBOM。它支持对容器镜像、文件系统、Git仓库、虚拟机镜像、Kubernetes和AWS进行扫描，并能够找到操作系统软件包、软件依赖、已知漏洞、基础设施即代码问题、敏感信息、秘密和软件许可证。Trivy支持多种流行的编程语言、操作系统和平台。

## go-redis：与Uptrace一起监视Redis的Go客户端

* 创建周期：4194 天
* 开发语言：Go
* 协议类型：BSD 2-Clause "Simplified" License
* Star数量：18615 个
* Fork数量：2240 次
* 关注人数：18615 人
* 贡献人数：270 人
* Open Issues数量：204 个
* Github地址：https://github.com/redis/go-redis.git
* 项目首页: https://redis.uptrace.dev


Redis Go客户端go-redis是Go编程语言的Redis客户端。它由uptrace/uptrace维护，并可与Uptrace一起使用，Uptrace是一个支持分布式跟踪、度量和日志的开源APM工具。Uptrace可以监视应用程序并设置自动警报，通过电子邮件、Slack、Telegram等渠道接收通知。有一个OpenTelemetry示例可用于演示如何使用Uptrace监视go-redis。

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

## Migrate：Go语言编写的数据库迁移工具

* 创建周期：2190 天
* 开发语言：Go
* 协议类型：Other
* Star数量：13234 个
* Fork数量：1284 次
* 关注人数：13234 人
* 贡献人数：207 人
* Open Issues数量：312 个
* Github地址：https://github.com/golang-migrate/migrate.git


Migrate是一个用Go语言编写的开源项目，提供数据库迁移功能。它可以作为CLI工具使用，也可以作为库导入。Migrate从源中读取迁移并按正确顺序应用到数据库中。该项目保持数据库驱动程序的轻量级，并确保逻辑是无懈可击的。

## Toxiproxy：模拟网络条件的开源框架

* 创建周期：3423 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：10031 个
* Fork数量：434 次
* 关注人数：10031 人
* 贡献人数：61 人
* Open Issues数量：87 个
* Github地址：https://github.com/Shopify/toxiproxy.git
* 项目首页: https://github.com/shopify/toxiproxy


Toxiproxy是一个用于模拟网络条件的开源框架，专为测试、CI和开发环境而设计。它允许对连接进行确定性篡改，并支持随机混乱和定制化。它由用Go语言编写的TCP代理和通过HTTP与代理通信的客户端组成。Toxiproxy有助于通过测试证明应用程序没有单点故障，并自2014年10月以来在Shopify的开发和测试环境中得到成功使用。

## 零分配JSON记录器

* 创建周期：2442 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：9307 个
* Fork数量：533 次
* 关注人数：9307 人
* 贡献人数：140 人
* Open Issues数量：143 个
* Github地址：https://github.com/rs/zerolog.git


zerolog包是一个专注于JSON输出的快速简单的记录器。它提供了一个独特的链接API，可以通过避免分配和反射来编写JSON（或CBOR）日志事件。Zerolog旨在提供出色的开发人员体验和令人惊叹的性能，利用了Uber的zap库开创的概念，并通过更简单的API和更好的性能将其推向了一个新的水平。它专注于高效的结构化日志记录，并提供了一个控制台写入器用于美观的日志记录。

## Kubernetes Autoscaler存储库

* 创建周期：2472 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：7384 个
* Fork数量：3773 次
* 关注人数：7384 人
* 贡献人数：409 人
* Open Issues数量：280 个
* Github地址：https://github.com/kubernetes/autoscaler.git


Kubernetes Autoscaler存储库包含用于Kubernetes的自动缩放相关组件。

## Karpenter: Kubernetes节点自动缩放器

* 创建周期：1288 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：5451 个
* Fork数量：725 次
* 关注人数：5451 人
* 贡献人数：256 人
* Open Issues数量：224 个
* Github地址：https://github.com/aws/karpenter-provider-aws.git
* 项目首页: https://karpenter.sh


Karpenter 是一个开源的 Kubernetes 节点自动缩放器，旨在通过根据工作负载要求进行节点的预配和移除，从而提高效率和降低成本。

## Kyverno: Kubernetes原生策略管理

* 创建周期：1809 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：4777 个
* Fork数量：718 次
* 关注人数：4777 人
* 贡献人数：262 人
* Open Issues数量：330 个
* Github地址：https://github.com/kyverno/kyverno.git
* 项目首页: https://kyverno.io


Kyverno是一个开源项目，提供Kubernetes原生的策略管理。它允许用户为在Kubernetes集群上运行的容器化应用程序定义和执行策略。

## 分布式实时聊天平台项目

* 创建周期：3 天
* 开发语言：Go, JavaScript
* Star数量：118 个
* Fork数量：13 次
* 关注人数：118 人
* 贡献人数：1 人
* Open Issues数量：0 个
* Github地址：https://github.com/JoyalAJohney/Realtime-Distributed-Chat.git


![](/images/joyalajohney-realtime-distributed-chat-0.png)

这是一个包含前端（React.js）、后端（Go-Fiber）和基础设施（Terraform、CI/CD）代码的开源项目，用于构建分布式、实时、可扩展的消息平台。该项目旨在帮助开发人员学习系统设计并了解端到端项目开发。项目所有者还计划就各种功能撰写文章，例如配置nginx作为负载均衡的反向代理，实现用于HTTPS通信的TLS/SSL证书，以及使用Terraform设置基础设施。

