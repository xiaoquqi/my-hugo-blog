---
title: Github 2024-05-30 Go开源项目日报 Top10
date: 2024-05-30T07:11:31+08:00
slug: github-trendings-today-20240530
author: 老孙正经胡说
image: /images/minio-minio-0.png
tags:
  - github
  - trendings
  - 数量
  - 人数
  - 人
  - 协议
  - 和
  - 语言
  - 是
  - 项目
  - 开发
  - 创建
  - 周期
  - 类型
  - 关注
  - 贡献
  - 地址
  - 流
  - 工作
  - 使用
  - 工具
  - 高性能

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-05-30统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Go项目 | 10 |

## MinIO：高性能对象存储系统

* 创建周期：3424 天
* 开发语言：Go
* 协议类型：GNU Affero General Public License v3.0
* Star数量：44763 个
* Fork数量：5178 次
* 关注人数：44763 人
* 贡献人数：421 人
* Open Issues数量：36 个
* Github地址：https://github.com/minio/minio.git
* 项目首页: https://min.io/download


![](/images/minio-minio-0.png)

MinIO是一个高性能的对象存储系统，发布在GNU Affero通用公共许可证v3.0下。它与Amazon S3云存储服务兼容，可用于构建用于机器学习、分析和应用数据工作负载的高性能基础设施。本自述文件提供了在裸金属硬件和基于容器的安装上运行MinIO的快速入门说明，并建议在Kubernetes环境中使用MinIO Kubernetes Operator。

## Helm：Kubernetes 资源管理工具

* 创建周期：3054 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：25676 个
* Fork数量：6990 次
* 关注人数：25676 人
* 贡献人数：377 人
* Open Issues数量：632 个
* Github地址：https://github.com/helm/helm.git
* 项目首页: https://helm.sh


Helm 是一个用于管理 Charts 的工具，Charts 是预配置的 Kubernetes 资源包。它允许用户查找和使用打包为 Helm Charts 的热门软件在 Kubernetes 中运行，分享他们自己的应用程序作为 Helm Charts，创建可重现的 Kubernetes 应用程序构建，智能地管理 Kubernetes 清单文件，并管理 Helm 包的发布。

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

## Cilium: 一个基于eBPF的网络、可观测性和安全性解决方案

* 创建周期：2948 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：17530 个
* Fork数量：2575 次
* 关注人数：17530 人
* 贡献人数：400 人
* Open Issues数量：1149 个
* Github地址：https://github.com/cilium/cilium.git
* 项目首页: https://cilium.io


Cilium是一个基于eBPF的数据平面的开源网络、可观测性和安全性解决方案。它提供了一个简单的平面3层网络，支持多集群，具有L7协议意识，分布式负载平衡，以及集成网关、带宽管理和服务网格等高级功能。它利用eBPF技术实现安全、网络和可见性逻辑的高效灵活实现。

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

## Temporal：可靠的执行平台

* 创建周期：1688 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：10263 个
* Fork数量：750 次
* 关注人数：10263 人
* 贡献人数：193 人
* Open Issues数量：434 个
* Github地址：https://github.com/temporalio/temporal.git
* 项目首页: https://docs.temporal.io


![](/images/temporalio-temporal-0.png)

Temporal是一个耐用的执行平台，使开发人员能够构建可扩展的应用程序，而不会影响生产力或可靠性。它以一种有弹性的方式执行称为工作流的应用程序逻辑，自动处理间歇性故障，并重试失败的操作。Temporal起源于Uber的Cadence的分支，由Cadence的创始人创立的创业公司Temporal Technologies开发。

## Dex - 一个联合的OpenID Connect提供者

* 创建周期：3209 天
* 开发语言：Go
* 协议类型：Apache License 2.0
* Star数量：9119 个
* Fork数量：1651 次
* 关注人数：9119 人
* 贡献人数：203 人
* Open Issues数量：417 个
* Github地址：https://github.com/dexidp/dex.git
* 项目首页: https://dexidp.io


Dex是一个身份服务，使用OpenID Connect来驱动其他应用程序的身份验证。它通过'连接器'作为到其他身份提供者的门户，如LDAP服务器、SAML提供者、GitHub、Google和Active Directory，允许客户端编写他们的身份验证逻辑一次，然后dex处理给定后端的协议。

## fscan - 内网综合扫描工具

* 创建周期：1294 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：8401 个
* Fork数量：1371 次
* 关注人数：8401 人
* 贡献人数：21 人
* Open Issues数量：140 个
* Github地址：https://github.com/shadow1ng/fscan.git


![](/images/shadow1ng-fscan-0.png)

fscan是一款内网综合扫描工具，提供一键自动化、全方位的漏洞扫描。它支持主机存活探测、端口扫描、各种服务的爆破、漏洞扫描、Web指纹识别、漏洞利用等功能。用户可以通过简单用法或完整参数来使用该工具，并且可以查看运行截图以了解其功能。同时，工具的使用需遵守免责声明。

## 现代化终端文件管理器

* 创建周期：72 天
* 开发语言：Go
* 协议类型：MIT License
* Star数量：4048 个
* Fork数量：72 次
* 关注人数：4048 人
* 贡献人数：26 人
* Open Issues数量：26 个
* Github地址：https://github.com/yorukot/superfile.git
* 项目首页: https://superfile.netlify.app


这是一个现代化和复杂的开源终端文件管理器，旨在执行常见的文件操作。

