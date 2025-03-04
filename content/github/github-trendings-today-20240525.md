---
title: Github 2024-05-25 Rust开源项目日报 Top10
date: 2024-05-25T07:11:17+08:00
slug: github-trendings-today-20240525
author: 老孙正经胡说
image: /images/rustdesk-rustdesk-0.png
tags:
  - github
  - trendings
  - 数量
  - 项目
  - 人
  - 和
  - 人数
  - 开发
  - 是
  - 语言
  - 创建
  - 贡献
  - 周期
  - 协议
  - 类型
  - 关注
  - 地址
  - 提供
  - 工具
  - 使用
  - 中
  - 开源

categories:

draft: false
---


根据Github Trendings的统计，今日(2024-05-25统计)共有10个项目上榜。根据开发语言中项目的数量，汇总情况如下：

| 开发语言 | 项目数量 |
|  ----  | ----  |
| Rust项目 | 10 |
| Svelte项目 | 1 |
| TypeScript项目 | 1 |
| Python项目 | 1 |
| Go项目 | 1 |
| Dart项目 | 1 |

## RustDesk: 用Rust编写的开源远程桌面软件

* 创建周期：1218 天
* 开发语言：Rust, Dart
* 协议类型：GNU Affero General Public License v3.0
* Star数量：58141 个
* Fork数量：6255 次
* 关注人数：58141 人
* 贡献人数：230 人
* Open Issues数量：49 个
* Github地址：https://github.com/rustdesk/rustdesk.git
* 项目首页: https://rustdesk.com


![](/images/rustdesk-rustdesk-0.png)

RustDesk是一款用Rust编写的开源远程桌面软件，可作为TeamViewer的替代品。它可以直接使用，无需配置，提供完全的数据控制和安全性。用户可以使用提供的会合/中继服务器，自行设置，或编写自己的服务器。该项目欢迎所有人的贡献，并提供常见问题解答、二进制下载和每夜构建。

## ripgrep（rg）- 递归搜索工具

* 创建周期：2997 天
* 开发语言：Rust
* 协议类型：The Unlicense
* Star数量：45437 个
* Fork数量：1889 次
* 关注人数：45437 人
* 贡献人数：370 人
* Open Issues数量：108 个
* Github地址：https://github.com/BurntSushi/ripgrep.git


![](/images/burntsushi-ripgrep-0.png)

ripgrep（rg）是一种面向行的搜索工具，可以在当前目录中递归搜索正则表达式模式。默认情况下，ripgrep会遵守gitignore规则，并自动跳过隐藏文件/目录和二进制文件。（要禁用默认情况下的所有自动过滤，请使用rg -uuu .）ripgrep在Windows、macOS和Linux上具有一流的支持，并且类似于其他流行的搜索工具，如The Silver Searcher、ack和grep。它在MIT或UNLICENSE下具有双重许可。

## Ruff: 极速Python代码检查器和格式化工具

* 创建周期：655 天
* 开发语言：Rust
* 协议类型：MIT License
* Star数量：27379 个
* Fork数量：874 次
* 关注人数：27379 人
* 贡献人数：420 人
* Open Issues数量：867 个
* Github地址：https://github.com/astral-sh/ruff.git
* 项目首页: https://docs.astral.sh/ruff


Ruff是一个极快的Python代码检查器和代码格式化工具，用Rust编写，旨在比现有的检查器和格式化工具如Flake8和Black快10-100倍。它可通过pip安装，支持pyproject.toml，并兼容Python 3.12。Ruff提供了与Flake8、isort和Black的兼容性，内置缓存、修复支持、800多条内置规则，以及针对VS Code等编辑器的官方集成。它适用于单存储库，并且在Apache Airflow、FastAPI、Hugging Face和Pandas等主要开源项目中得到积极使用。

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

## Biome: 高性能网络项目工具链

* 创建周期：268 天
* 开发语言：Rust
* 协议类型：Apache License 2.0
* Star数量：10153 个
* Fork数量：331 次
* 关注人数：10153 人
* 贡献人数：382 人
* Open Issues数量：141 个
* Github地址：https://github.com/biomejs/biome.git
* 项目首页: https://biomejs.dev


![](/images/biomejs-biome-0.png)

Biome是一个高性能的网络项目工具链，为JavaScript、TypeScript、JSX和JSON提供快速格式化和检查工具。它提供了来自ESLint、typescript-eslint和其他来源的200多条规则，并输出详细的诊断信息，帮助改善代码质量。Biome旨在与编辑器进行交互式使用，在编写代码时对其进行格式化和检查。

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

## 可滚动的平铺式Wayland合成器

* 创建周期：226 天
* 开发语言：Rust
* 协议类型：GNU General Public License v3.0
* Star数量：1545 个
* Fork数量：39 次
* 关注人数：1545 人
* 贡献人数：19 人
* Open Issues数量：48 个
* Github地址：https://github.com/YaLTeR/niri.git
* 项目首页: https://matrix.to/#/#niri:matrix.org


![](/images/yalter-niri-0.png)

一种可滚动的平铺式Wayland合成器，将窗口排列在无限向右滚动的列中，打开新窗口不会导致现有窗口调整大小。每个显示器都有自己独立的窗口条，窗口永远不会“溢出”到相邻的显示器。工作区是动态的，垂直排列，每个显示器都有独立的工作区集，并始终存在一个空的工作区。工作区布局在断开和连接显示器时会得到保留。

## Amber: 编译为Bash的高级编程语言

* 创建周期：675 天
* 开发语言：Rust
* 协议类型：GNU General Public License v3.0
* Star数量：2197 个
* Fork数量：34 次
* 关注人数：2197 人
* 贡献人数：10 人
* Open Issues数量：16 个
* Github地址：https://github.com/Ph0enixKM/Amber.git
* 项目首页: https://amber-lang.com


Amber是一种高级编程语言，可编译为Bash，使得创建shell脚本变得容易。它特别适用于云服务，但重要的是要注意，该软件尚未准备好用于长时间使用。

## jsr.io: 现代JavaScript和TypeScript的开源软件包注册表

* 创建周期：87 天
* 开发语言：Rust, TypeScript
* 协议类型：MIT License
* Star数量：1846 个
* Fork数量：77 次
* 关注人数：1846 人
* 贡献人数：40 人
* Open Issues数量：129 个
* Github地址：https://github.com/jsr-io/jsr.git
* 项目首页: https://jsr.io


jsr.io是一个面向现代JavaScript和TypeScript的开源软件包注册表。它是新JavaScript注册表的源代码，专为那些有兴趣为注册表做贡献的人设计。

## CADmium: 在浏览器中运行的新型CAD程序

* 创建周期：265 天
* 开发语言：Rust, Svelte
* 协议类型：Other
* Star数量：627 个
* Fork数量：20 次
* 关注人数：627 人
* 贡献人数：6 人
* Open Issues数量：18 个
* Github地址：https://github.com/CADmium-Co/CADmium.git
* 项目首页: https://cadmium-co.github.io/CADmium/


CADmium是一个全新的CAD程序，从头开始开发，旨在在Web浏览器中运行。它旨在捕捉80%的最常见CAD使用情况，同时只做不到10%的工作，针对的是想要为3D打印设计简单物体的家庭爱好者。该项目处于早期原型阶段，源代码可以在Github上免费获取。

