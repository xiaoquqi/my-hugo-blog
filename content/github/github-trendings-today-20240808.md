---
title: Github 2024-08-08 Go开源项目日报 Top10
date: 2024-08-08T07:11:15+08:00
slug: github-trendings-today-20240808
author: 老孙正经胡说
image: /images/fatedier-frp-0.png
tags:
  - github
  - trendings
  - 数量
  - 人
  - 人数
  - 开发
  - 项目
  - 是
  - 语言
  - 创建
  - 协议
  - 贡献
  - 周期
  - 类型
  - 关注
  - 地址
  - 开源
  - 并
  - 和
  - 库
  - 工具
  - 用于

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-08-08统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Go项目 | 10 |
| Rust项目 | 1 |

## frp: 一个开源的快速反向代理

* 创建周期：2946 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：75872 个
* Fork数量：12424 次
* 关注人数：75872 人
* 贡献人数：93 人
* Open Issues数量：102 个
* Github地址：https://github.com/fatedier/frp.git


![](/images/fatedier-frp-0.png)

frp是一个开源的快速反向代理，允许用户将位于NAT或防火墙后面的本地服务器暴露到互联网上。

## GORM：面向Golang的开发者友好的ORM库

* 创建周期：3730 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：34522 个
* Fork数量：3830 次
* 关注人数：34522 人
* 贡献人数：359 人
* Open Issues数量：312 个
* Github地址：https://github.com/go-gorm/gorm.git
* 项目首页: https://gorm.io


GORM是一个面向Golang的开源ORM库，旨在使开发人员更加友好。

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

## go-github: 用于访问GitHub API v3的Go客户端库

* 创建周期：3933 天
* 开发语言：Go
* 协议类型：BSD 3-Clause "New" or "Revised" License
* Star数量：9975 个
* Fork数量：1978 次
* 关注人数：9975 人
* 贡献人数：445 人
* Open Issues数量：65 个
* Github地址：https://github.com/google/go-github.git
* 项目首页: https://pkg.go.dev/github.com/google/go-github/v59/github


go-github是一个用于访问GitHub API v3的Go客户端库。它需要Go版本1.13或更高版本，并跟踪Go的版本支持政策。对于那些有兴趣使用GraphQL API v4的人，推荐的库是shurcooL/githubv4。

## Ginkgo: 一个成熟的Go测试框架

* 创建周期：3870 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：7861 个
* Fork数量：638 次
* 关注人数：7861 人
* 贡献人数：178 人
* Open Issues数量：82 个
* Github地址：https://github.com/onsi/ginkgo.git
* 项目首页: http://onsi.github.io/ginkgo/


![](/images/onsi-ginkgo-0.png)

Ginkgo是一个成熟的Go测试框架，帮助编写表达性强的规范。它建立在Go的测试基础之上，并由Gomega匹配库补充。它易于启动并开始编写您的第一个规范。

## Encore: 事件驱动分布式系统的后端开发平台

* 创建周期：1268 天
* 开发语言：Go, Rust
* 协议类型：Mozilla Public License 2.0
* Star数量：5641 个
* Fork数量：253 次
* 关注人数：5641 人
* 贡献人数：55 人
* Open Issues数量：64 个
* Github地址：https://github.com/encoredev/encore.git
* 项目首页: https://encore.dev


![](/images/encoredev-encore-0.png)

Encore是一个专为构建分布式系统和事件驱动应用程序而设计的后端开发平台。它提供了一个专门的工作流程，用于创建事件驱动和分布式系统，从本地开发到部署在AWS和GCP上。Encore包括一个适用于TypeScript和Go的后端框架，一个带有跟踪工具的本地开发环境，以及用于自动化CI/CD和云基础架构配置的云平台。

![](/images/encoredev-encore-1.png)

## Tau：开发人员喜爱的自托管云计算平台

* 创建周期：392 天
* 开发语言：Go
* 协议类型：BSD 3-Clause "New" or "Revised" License
* Star数量：2830 个
* Fork数量：72 次
* 关注人数：2830 人
* 贡献人数：14 人
* Open Issues数量：18 个
* Github地址：https://github.com/taubyte/tau.git
* 项目首页: https://tau.how


Tau是一个开源的分布式平台即服务（PaaS），是Vercel、Netlify和Cloudflare的自托管替代方案。它旨在成为一个低维护且高度可扩展的云计算平台，深受开发人员喜爱。Tau是一个单一的二进制文件，除了标准系统库外几乎没有外部依赖，并且需要最少的配置。主要步骤包括安装Tau、配置它，然后启动它。有关详细说明，请参阅“部署Tau”指南。如果安装了Go，使用“go build”命令构建Tau非常简单。

## Argo Rollouts - 为Kubernetes提供渐进式交付

* 创建周期：2091 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：2627 个
* Fork数量：828 次
* 关注人数：2627 人
* 贡献人数：262 人
* Open Issues数量：429 个
* Github地址：https://github.com/argoproj/argo-rollouts.git
* 项目首页: https://argo-rollouts.readthedocs.io/


![](/images/argoproj-argo-rollouts-0.png)

Argo Rollouts是一个为Kubernetes提供渐进式交付的开源项目。它允许用户逐渐发布应用程序的新版本，监视其行为，并在必要时回滚更改。

## SpoofDPI: 用Go编写的反审查工具

* 创建周期：952 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：955 个
* Fork数量：42 次
* 关注人数：955 人
* 贡献人数：7 人
* Open Issues数量：15 个
* Github地址：https://github.com/xvzc/SpoofDPI.git


SpoofDPI是一个用Go语言编写的开源反审查工具，旨在绕过深度数据包检测。这是一个简单快速的软件，欢迎社区贡献。

