---
title: Github 2024-02-29 Go开源项目日报 Top10
date: 2024-02-29T07:11:16+08:00
slug: github-trendings-today-20240229
author: 老孙正经胡说
image: /images/ollama-ollama-0.png
tags:
  - github
  - trendings
  - 数量
  - 和
  - 人
  - 人数
  - 项目
  - 语言
  - 开发
  - 容器
  - 协议
  - 类型
  - 创建
  - 周期
  - 关注
  - 贡献
  - 地址
  - 是
  - 提供
  - 用于
  - 日志
  - 使用

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-02-29统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Go项目 | 10 |

## Moby 项目 - 软件容器化的开源工具集

* 创建周期：4059 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：67419 个
* Fork数量：18497 次
* 关注人数：67419 人
* 贡献人数：402 人
* Open Issues数量：3359 个
* Github地址：https://github.com/moby/moby.git
* 项目首页: https://mobyproject.org/


Moby项目是Docker推出的开源项目，旨在促进和加速软件容器化。它提供了一套工具组件，用于构建定制的基于容器的系统，并为容器爱好者和专业人士提供了一个合作和创新的平台。

## Go Ethereum: 以太坊Go语言官方实现

* 创建周期：3717 天
* 开发语言：Go
* 协议类型：GNU Lesser General Public License v3.0
* Star数量：45047 个
* Fork数量：18609 次
* 关注人数：45047 人
* 贡献人数：431 人
* Open Issues数量：360 个
* Github地址：https://github.com/ethereum/go-ethereum.git
* 项目首页: https://geth.ethereum.org


Go Ethereum是以Go编程语言实现的以太坊协议的官方实现。它为以太坊提供了执行层，并为稳定版本和不稳定的主分支提供了自动化构建。可以在https://geth.ethereum.org/downloads/找到二进制存档。

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

## PocketBase: 开源实时后端

* 创建周期：555 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：30029 个
* Fork数量：1330 次
* 关注人数：30029 人
* 贡献人数：37 人
* Open Issues数量：38 个
* Github地址：https://github.com/pocketbase/pocketbase.git
* 项目首页: https://pocketbase.io


![](/images/pocketbase-pocketbase-0.png)

PocketBase是一个开源的Go后端，包括嵌入式SQLite数据库与实时订阅，内置文件和用户管理，方便的管理面板UI，以及简单的REST-ish API。它仍在积极开发中，在达到v1.0.0之前不能保证完全向后兼容。

## Vault - 开源秘密管理与加密服务

* 创建周期：3277 天
* 开发语言：Go
* 协议类型：Other
* Star数量：29288 个
* Fork数量：4127 次
* 关注人数：29288 人
* 贡献人数：392 人
* Open Issues数量：1318 个
* Github地址：https://github.com/hashicorp/vault.git
* 项目首页: https://www.vaultproject.io/


Vault是一个开源工具，用于秘密管理、加密服务和特权访问管理。它提供了一个统一的界面，用于安全地访问和控制各种类型的秘密，如API密钥、密码和证书。Vault提供了安全的秘密存储、动态秘密生成、数据加密、租约和续约以及撤销支持等功能。它还为安全自动化提供了文档、入门指南和认证考试。

## Consul：动态分布式基础架构连接和配置解决方案

* 创建周期：3720 天
* 开发语言：Go
* 协议类型：Other
* Star数量：27465 个
* Fork数量：4436 次
* 关注人数：27465 人
* 贡献人数：362 人
* Open Issues数量：1283 个
* Github地址：https://github.com/hashicorp/consul.git
* 项目首页: https://www.consul.io


Consul是一个分布式、高可用且数据中心感知的解决方案，用于在动态分布式基础架构中连接和配置应用程序。它提供了诸如多数据中心支持、用于安全通信的服务网格、API网关、服务发现、健康检查和动态应用程序配置等功能。

## Loki: Prometheus日志聚合系统

* 创建周期：2145 天
* 开发语言：Go
* 协议类型：GNU Affero General Public License v3.0
* Star数量：21630 个
* Fork数量：3161 次
* 关注人数：21630 人
* 贡献人数：449 人
* Open Issues数量：1385 个
* Github地址：https://github.com/grafana/loki.git
* 项目首页: https://grafana.com/loki


Loki是受Prometheus启发的横向扩展、高可用性、多租户日志聚合系统。它旨在成本效益高且易于操作，使用标签来表示日志流而不是索引日志内容。它特别适合存储Kubernetes Pod日志，并在Grafana中具有原生支持。基于Loki的日志堆栈由3个组件组成：promtail、loki和Grafana。Loki专注于日志而不是指标，并通过推送而不是拉取来传递日志。

## cAdvisor（容器顾问）- 运行中的守护程序，用于收集、汇总、处理和导出有关运行容器资源使用情况和性能特征的信息

* 创建周期：3552 天
* 开发语言：Go
* 协议类型：Other
* Star数量：16081 个
* Fork数量：2255 次
* 关注人数：16081 人
* 贡献人数：297 人
* Open Issues数量：712 个
* Github地址：https://github.com/google/cadvisor.git


cAdvisor（容器顾问）是一个运行中的守护程序，用于收集、汇总、处理和导出有关运行容器的资源使用情况和性能特征的信息。它为用户提供了对每个容器的资源使用情况、历史使用情况和网络统计的理解，原生支持 Docker 容器和其他容器类型。

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

## Gatus: 开发者健康仪表板

* 创建周期：1639 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：4896 个
* Fork数量：362 次
* 关注人数：4896 人
* 贡献人数：71 人
* Open Issues数量：130 个
* Github地址：https://github.com/TwiN/gatus.git
* 项目首页: https://gatus.io


Gatus是一个面向开发者的健康仪表板，允许使用各种类型的查询来监视服务，并使用条件评估结果。它还支持通过多个平台进行警报，并可以部署在Kubernetes中。

