---
title: Github 2024-03-09 Rust开源项目日报 Top10
date: 2024-03-09T07:11:06+08:00
slug: github-trendings-today-20240309
author: 老孙正经胡说
image: /images/pola-rs-polars-0.png
tags:
  - github
  - trendings
  - 数量
  - 人数
  - 人
  - 项目
  - 语言
  - 和
  - 开发
  - 类型
  - 是
  - 创建
  - 周期
  - 协议
  - 关注
  - 贡献
  - 地址
  - 中
  - 查询
  - 运行
  - 提供
  - 开源

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-03-09统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Rust项目 | 10 |
| Python项目 | 1 |
| Scala项目 | 1 |
| CUE项目 | 1 |

## InfluxDB Edge: 开源实时时序数据库

* 创建周期：3817 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：27405 个
* Fork数量：3468 次
* 关注人数：27405 人
* 贡献人数：319 人
* Open Issues数量：1898 个
* Github地址：https://github.com/influxdata/influxdb.git
* 项目首页: https://influxdata.com


InfluxDB Edge是用Rust编写的开源时序数据库，专注于为各种类型的观测数据提供实时缓冲。最新版本（3.x）可以通过SQL或InfluxQL进行查询，并将数据批量持久化到对象存储中作为Parquet文件。它可以作为独立系统在单个进程中运行，并提供商业版本，用于具有企业安全功能的集群化、分布式时序数据库。

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

## ZLUDA：在AMD GPU上运行CUDA应用程序的开源项目

* 创建周期：1524 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：6718 个
* Fork数量：364 次
* 关注人数：6718 人
* 贡献人数：9 人
* Open Issues数量：50 个
* Github地址：https://github.com/vosen/ZLUDA.git


ZLUDA是一个开源项目，它可以在AMD GPU上以接近原生性能运行未经修改的CUDA应用程序。目前处于alpha质量阶段，但已确认可以与各种本地CUDA应用程序一起使用，如Geekbench、3DF Zephyr、Blender等。

## Gleam：构建可扩展的类型安全系统的友好语言

* 创建周期：2809 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：6298 个
* Fork数量：310 次
* 关注人数：6298 人
* 贡献人数：157 人
* Open Issues数量：130 个
* Github地址：https://github.com/gleam-lang/gleam.git
* 项目首页: https://gleam.run


Gleam是一种友好的语言，用于构建可扩展的类型安全系统。

## DataFusion：Rust中的高速数据查询引擎

* 创建周期：1015 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：4523 个
* Fork数量：827 次
* 关注人数：4523 人
* 贡献人数：398 人
* Open Issues数量：935 个
* Github地址：https://github.com/apache/arrow-datafusion.git
* 项目首页: https://arrow.apache.org/datafusion


DataFusion是一个高速、可扩展的查询引擎，用于在Rust中构建高质量的数据中心系统，使用Apache Arrow内存格式。它提供了SQL和Dataframe API，出色的性能，内置支持各种数据格式，广泛的定制化以及强大的社区。

## ord - 一种实验性的satoshis管理软件

* 创建周期：818 天
* 开发语言：Rust
* 协议类型：Creative Commons Zero v1.0 Universal
* Star数量：3029 个
* Fork数量：1042 次
* 关注人数：3029 人
* 贡献人数：75 人
* Open Issues数量：350 个
* Github地址：https://github.com/ordinals/ord.git
* 项目首页: https://ordinals.com


ord是一种实验性软件，用于管理satoshis的索引、区块浏览器和命令行钱包。它为satoshis分配序数，允许它们被收集和交易。该项目是开源的，由社区资助，当前的首席维护者是raphjaph。它依赖于比特币核心进行私钥管理和交易签名，并鼓励用户捐赠以支持其维护和开发。

## 本地 Rust UI 库：细粒度反应性

* 创建周期：403 天
* 开发语言：Rust
* 协议类型：MIT License
* Star数量：1990 个
* Fork数量：93 次
* 关注人数：1990 人
* 贡献人数：39 人
* Open Issues数量：45 个
* Github地址：https://github.com/lapce/floem.git
* 项目首页: https://docs.rs/floem


这是一个具有细粒度反应性的本地 Rust UI 库。该项目仍在不断发展中，我们将在达到 v1 版本的过程中偶尔进行重大更改并添加缺失的功能。

## Gitu: 一个受Magit启发的终端用户界面Git客户端

* 创建周期：77 天
* 开发语言：Rust
* 协议类型：MIT License
* Star数量：352 个
* Fork数量：6 次
* 关注人数：352 人
* 贡献人数：3 人
* Open Issues数量：10 个
* Github地址：https://github.com/altsem/gitu.git


Gitu是受Magit启发的终端用户界面(TUI) Git客户端，提供了一个在Emacs之外的Git界面。它允许用户直接从终端与Git进行交互，为管理版本控制提供了一种便捷高效的方式。

## Comet: Apache Spark插件利用Apache Arrow DataFusion提高查询效率和运行时

* 创建周期：54 天
* 开发语言：Rust, Scala
* 协议类型：Apache License 2.0
* Star数量：283 个
* Fork数量：48 次
* 关注人数：283 人
* 贡献人数：15 人
* Open Issues数量：29 个
* Github地址：https://github.com/apache/arrow-datafusion-comet.git
* 项目首页: https://arrow.apache.org/datafusion-comet


Comet是一个Apache Spark插件，利用Apache Arrow DataFusion作为本机运行时来提高查询效率和运行时。它使用本机DataFusion运行时运行Spark SQL查询，比基于JVM的运行时更快、资源利用更高效。Comet旨在支持本机Parquet实现，完整实现Spark运算符和内置表达式，并提供UDF框架，使用户能够将现有的UDF迁移到本机。

