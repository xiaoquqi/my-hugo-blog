---
title: Github 2024-09-07 Rust开源项目日报 Top10
date: 2024-09-07T07:11:18+08:00
slug: github-trendings-today-20240907
author: 老孙正经胡说
image: /images/pola-rs-polars-0.png
tags:
  - github
  - trendings
  - 数量
  - 和
  - 项目
  - 人数
  - 人
  - 提供
  - 开发
  - 语言
  - 创建
  - 周期
  - 关注
  - 贡献
  - 地址
  - 是
  - 协议
  - 类型
  - 开源
  - 使用
  - 数据
  - 中

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-09-07统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Rust项目 | 10 |
| CUE项目 | 1 |
| Python项目 | 1 |
| Go项目 | 1 |

## Polars: Rust中的DataFrame接口和OLAP查询引擎

* 创建周期：1354 天
* 开发语言：Rust, Python
* 协议类型：MIT License
* Star数量：23854 个
* Fork数量：1393 次
* 关注人数：23854 人
* 贡献人数：342 人
* Open Issues数量：1313 个
* Github地址：https://github.com/pola-rs/polars.git
* 项目首页: https://docs.pola.rs


![](/images/pola-rs-polars-0.png)

Polars是在Rust上实现的OLAP查询引擎之上的DataFrame接口，提供诸如惰性和急切执行、多线程、SIMD、查询优化、强大的表达式API和用于大于RAM数据集的混合流式传输等功能。它支持Rust、Python、Node.js、R等多种语言。

## Delta: Git、Diff、Grep和Blame输出的语法高亮分页程序

* 创建周期：1902 天
* 开发语言：Rust
* 协议类型：MIT License
* Star数量：22285 个
* Fork数量：370 次
* 关注人数：22285 人
* 贡献人数：135 人
* Open Issues数量：290 个
* Github地址：https://github.com/dandavison/delta.git
* 项目首页: https://dandavison.github.io/delta/


![](/images/dandavison-delta-0.png)

Delta是一个开源的语法高亮分页程序，用于git、diff、grep和blame输出。它提供了许多功能，并且可以高度定制化。要开始使用，大多数软件包管理器中的包名为'git-delta'，将其添加到您的~/.gitconfig中。有关更多信息和定制选项，请参阅用户手册。

![](/images/dandavison-delta-1.png)

## Vector：高性能可观察性数据管道

* 创建周期：2021 天
* 开发语言：Rust, CUE
* 协议类型：Mozilla Public License 2.0
* Star数量：15723 个
* Fork数量：1341 次
* 关注人数：15723 人
* 贡献人数：369 人
* Open Issues数量：1741 个
* Github地址：https://github.com/vectordotdev/vector.git
* 项目首页: https://vector.dev


Vector是一个开源的高性能可观察性数据管道，允许用户收集、转换和路由日志和指标到任何供应商。它实现了成本降低、数据丰富化和数据安全，并且比空间中其他替代方案快高达10倍。

## TiKV: 开源分布式事务键值数据库

* 创建周期：2949 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：14107 个
* Fork数量：2050 次
* 关注人数：14107 人
* 贡献人数：393 人
* Open Issues数量：1535 个
* Github地址：https://github.com/tikv/tikv.git
* 项目首页: https://tikv.org


TiKV 是一个开源的、分布式的、支持事务的键值数据库，旨在补充 TiDB。它不仅提供了经典的键值 API，还提供了符合 ACID 的事务 API。TiKV 使用 Rust 构建，并由 Raft 驱动，受到了谷歌分布式系统和学术成就的启发。它保证了数据一致性，支持地理复制、水平扩展、一致的分布式事务、协处理器支持，并与 TiDB 协同工作。

## Jujutsu: 强大的版本控制系统

* 创建周期：1151 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：5368 个
* Fork数量：180 次
* 关注人数：5368 人
* 贡献人数：77 人
* Open Issues数量：235 个
* Github地址：https://github.com/martinvonz/jj.git
* 项目首页: https://martinvonz.github.io/jj/


Jujutsu是一个功能强大的版本控制系统，旨在易于使用，适合新手和有经验的开发人员。它将用户界面和版本控制算法与存储系统分离，使其可以作为具有许多可能的物理后端的VCS。它结合了来自其他版本控制系统（如Git、Mercurial、Sapling、Pijul和Darcs）的设计选择和概念，同时还引入了创新功能，如工作副本作为提交、操作日志和撤消，以及自动重基和冲突解决。它还提供了实验性功能，如安全的并发复制，使其在并发场景下安全。命令行工具目前称为jj，该项目相对年轻，正在进行持续开发，并在Discord和GitHub上进行讨论。

## Kata Containers: 轻量级虚拟机与容器性能的安全性优势

* 创建周期：2235 天
* 开发语言：Rust, Go
* 协议类型：Apache License 2.0
* Star数量：4572 个
* Fork数量：1047 次
* 关注人数：4572 人
* 贡献人数：310 人
* Open Issues数量：1375 个
* Github地址：https://github.com/kata-containers/kata-containers.git


Kata Containers 是一个旨在创建轻量级虚拟机（VMs）的开源项目，旨在提供容器的性能同时提供虚拟机的安全性优势。

## librespot: Spotify的开源客户端库

* 创建周期：2488 天
* 开发语言：Rust
* 协议类型：MIT License
* Star数量：4691 个
* Fork数量：571 次
* 关注人数：4691 人
* 贡献人数：129 人
* Open Issues数量：65 个
* Github地址：https://github.com/librespot-org/librespot.git


librespot是Spotify的开源客户端库，为应用程序提供使用Spotify服务控制和播放音乐的能力。它是官方库libspotify的替代品，提供了官方库中不可用的额外功能。它专门设计用于与Spotify Premium账户配合使用。

## Fluvio: 轻量级高性能分布式数据流处理系统

* 创建周期：1834 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：3677 个
* Fork数量：503 次
* 关注人数：3677 人
* 贡献人数：64 人
* Open Issues数量：139 个
* Github地址：https://github.com/infinyon/fluvio.git
* 项目首页: https://www.fluvio.io/


Fluvio是一个轻量级高性能的分布式数据流处理系统，使用Rust和Web Assembly编写。

## Delta Lake: 为开发人员和集成商提供本机API的开源存储格式

* 创建周期：1595 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：2139 个
* Fork数量：379 次
* 关注人数：2139 人
* 贡献人数：165 人
* Open Issues数量：231 个
* Github地址：https://github.com/delta-io/delta-rs.git
* 项目首页: https://delta-io.github.io/delta-rs/


Delta Lake是一个开源存储格式，它在现有数据湖之上提供ACID事务保证、模式强制执行和可扩展的数据处理。该项目旨在通过为开发人员和集成商提供本机低级API以及为Delta Lake提供易于查询、检查和操作的高级操作API，使Delta Lake可供广泛的用户和项目使用。

## Parity Polkadot 区块链 SDK 文档和模板

* 创建周期：316 天
* 开发语言：Rust
* Star数量：1579 个
* Fork数量：545 次
* 关注人数：1579 人
* 贡献人数：376 人
* Open Issues数量：1649 个
* Github地址：https://github.com/paritytech/polkadot-sdk.git
* 项目首页: https://polkadot.network/


Parity Polkadot 区块链 SDK 提供有关 Polkadot SDK 的每个组件的文档，包括 Substrate、FRAME、Cumulus 和 XCM。它还提供了构建第一个 FRAME pallet 的指南和启动新项目的模板。

