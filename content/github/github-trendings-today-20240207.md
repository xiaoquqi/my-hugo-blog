---
title: Github 2024-02-07 C开源项目日报 Top10
date: 2024-02-07T07:11:29+08:00
slug: github-trendings-today-20240207
author: 老孙正经胡说
image: /images/microsoft-mimalloc-0.png
tags:
  - github
  - trendings
  - 数量
  - 人数
  - 人
  - 和
  - 项目
  - 开发
  - 语言
  - 贡献
  - 协议
  - 创建
  - 周期
  - 关注
  - 地址
  - 是
  - 类型
  - 实现
  - 安全
  - 提供
  - 软件
  - 开源

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-02-07统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| C项目 | 10 |
| CMake项目 | 1 |

## 我的电视 - 安卓电视直播软件

* 创建周期：40 天
* 开发语言：C
* Star数量：649 个
* Fork数量：124 次
* 关注人数：649 人
* 贡献人数：1 人
* Open Issues数量：23 个
* Github地址：https://github.com/lizongying/my-tv.git


我的电视是一个开源的安卓电视直播应用，内置了直播源。

## FreeRDP: 远程桌面协议实现

* 创建周期：4605 天
* 开发语言：C
* 协议类型：Apache License 2.0
* Star数量：9780 个
* Fork数量：25046 次
* 关注人数：9780 人
* 贡献人数：311 人
* Open Issues数量：433 个
* Github地址：https://github.com/FreeRDP/FreeRDP.git
* 项目首页: http://www.freerdp.com/


FreeRDP是远程桌面协议（RDP）的免费实现，根据Apache许可发布。它允许用户在任何地方以任何方式使用他们的软件，促进互操作性，解放计算体验。

## mimalloc: 优异性能的紧凑通用分配器

* 创建周期：1694 天
* 开发语言：C
* 协议类型：MIT License
* Star数量：9153 个
* Fork数量：752 次
* 关注人数：9153 人
* 贡献人数：72 人
* Open Issues数量：307 个
* Github地址：https://github.com/microsoft/mimalloc.git


![](/images/microsoft-mimalloc-0.png)

mimalloc是一个紧凑的通用分配器，性能优异。它是malloc的即插即用替代品，可用于包括Windows、macOS、Linux和BSD在内的各种系统。其设计的显著特点包括小而一致的库大小，自由列表分片以减少碎片化，急切页面清除和安全功能。在基准测试中，它的性能优于其他主要分配器，并且对大型操作系统页面有良好的支持。

## xxHash - 非常快速的哈希算法

* 创建周期：3570 天
* 开发语言：C
* 协议类型：Other
* Star数量：8130 个
* Fork数量：789 次
* 关注人数：8130 人
* 贡献人数：90 人
* Open Issues数量：26 个
* Github地址：https://github.com/Cyan4973/xxHash.git
* 项目首页: http://www.xxhash.com/


![](/images/cyan4973-xxhash-0.png)

xxHash是一种非常快速的非加密哈希算法，可以以RAM速度限制进行处理。它具有高度的可移植性，并且在所有平台上生成相同的哈希值。该库包括XXH32、XXH64和XXH3算法，所有这些算法都成功通过了SMHasher测试套件。基准测试显示，XXH3和XXH128实现了高带宽和小数据速度，使它们适用于各种应用。

## Greenplum数据库 - 开源大规模并行数据平台

* 创建周期：3029 天
* 开发语言：C
* 协议类型：Apache License 2.0
* Star数量：6121 个
* Fork数量：1702 次
* 关注人数：6121 人
* 贡献人数：249 人
* Open Issues数量：452 个
* Github地址：https://github.com/greenplum-db/gpdb.git
* 项目首页: http://greenplum.org


Greenplum数据库是基于PostgreSQL的开源大规模并行数据平台，专为分析、机器学习和人工智能而设计。它提供强大的分析功能，可处理PB级数据量，并由先进的基于成本的查询优化器驱动。该项目在Apache 2许可下发布，并欢迎社区贡献。

## Arm A-Profile架构的安全世界软件参考实现

* 创建周期：3761 天
* 开发语言：C
* 协议类型：Other
* Star数量：1767 个
* Fork数量：1300 次
* 关注人数：1767 人
* 贡献人数：341 人
* Open Issues数量：12 个
* Github地址：https://github.com/ARM-software/arm-trusted-firmware.git
* 项目首页: https://developer.trustedfirmware.org/dashboard/view/6/


Trusted Firmware-A（TF-A）是Arm A-Profile架构的安全世界软件的参考实现，为安全世界引导和运行时固件的产品化提供了一个起点。它实现了Arm接口标准，并设计为可在基于Armv8-A和Armv7-A架构的硬件平台和软件模型上进行移植和重复使用。鼓励用户对从TF-A衍生的任何安全世界代码进行安全验证。

## Grafana Beyla: 基于eBPF和OpenTelemetry的零代码自动仪器化

* 创建周期：352 天
* 开发语言：C
* 协议类型：Apache License 2.0
* Star数量：1015 个
* Fork数量：59 次
* 关注人数：1015 人
* 贡献人数：25 人
* Open Issues数量：48 个
* Github地址：https://github.com/grafana/beyla.git


Grafana Beyla是一个开源项目，提供了基于eBPF和OpenTelemetry的零代码自动仪器化功能，适用于HTTP和HTTPS服务。它提供了一种自动仪器化服务的方式，无需手动编码。

## 启用UEFI系统上的可调整大小的BAR项目及NvStrapsReBar工具

* 创建周期：575 天
* 开发语言：C
* 协议类型：MIT License
* Star数量：903 个
* Fork数量：34 次
* 关注人数：903 人
* 贡献人数：2 人
* Open Issues数量：18 个
* Github地址：https://github.com/xCuri0/ReBarUEFI.git


![](/images/xcuri0-rebaruefi-0.png)

该项目旨在启用几乎任何UEFI系统上的可调整大小的BAR，并为NVIDIA Turing GPU（20或16系列）提供了名为NvStrapsReBar的特定工具。

## Pico TPMSniffer: 用于联想笔记本电脑的实验性TPM嗅探器

* 创建周期：4 天
* 开发语言：C, CMake
* 协议类型：Other
* Star数量：150 个
* Fork数量：25 次
* 关注人数：150 人
* 贡献人数：1 人
* Open Issues数量：0 个
* Github地址：https://github.com/stacksmashing/pico-tpmsniffer.git


Pico TPMSniffer是一个简单的、实验性的LPC总线TPM嗅探器，专为某些联想笔记本电脑设计。它不适用于专业或生产使用，目前固件仅支持LPC，不支持SPI TPMs。

## Leaky Vessels动态检测器

* 创建周期：7 天
* 开发语言：C
* 协议类型：Apache License 2.0
* Star数量：69 个
* Fork数量：11 次
* 关注人数：69 人
* 贡献人数：4 人
* Open Issues数量：1 个
* Github地址：https://github.com/snyk/leaky-vessels-dynamic-detector.git


Leaky Vessels Dynamic Detector是一个开源项目，为runc和Docker漏洞提供了基于eBPF的运行时检测的参考实现。它钩入Linux系统调用和Docker守护程序的函数调用，以识别特定漏洞的利用。

