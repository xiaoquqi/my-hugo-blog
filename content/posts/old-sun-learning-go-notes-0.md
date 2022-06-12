---
title: 老孙Go语言学习笔记-第零章
date: 2022-06-12T06:41:54+08:00
slug: "old-sun-learning-go-notes-0"
author: 老孙正经胡说
tags:
  - Go
  - Linux
  - Training
categories:
  - Go
draft: false
---

## 我为什么要学习Go?
- 我司是从事基础架构、云原生工具类开发的，因为新产品方向的开发需要，需要引入Go语言来作为新的模块开发语言
- 很多与基础架构有关的软件都使用了Go语言，像Docker、Kubernetes等
- 可编译，跨平台，依赖少，执行速度快，之前使用Python时，模块依赖问题非常头疼，而Go语言可编译、依赖性少的特点非常适合我们未来的需求
- 具备可编译语言的能力，但是在开发层面又设计简单，例如：接口、指针

## 该笔记参考了哪些文档？
主要参考了这些文档

- Learning Go: [https://miek.nl/go/](https://miek.nl/go/)
- Effective Go: [https://go.dev/doc/effective_go](https://go.dev/doc/effective_go)
- Go语言设计与实现：[https://draveness.me/golang/](https://draveness.me/golang/)
- 还有众多的博客，一一在各个章节列出

## 该笔记对哪些人有帮助？

- 因为我的需求是能够读懂和开发Go的项目，所以该笔记重视实战和应用，所以你想快速上手Go语言并进行开发，可以阅读本笔记
- 对于高深的原理和底层逻辑，尽量用代码逻辑去解释或给出参考链接
- 如果对于Go语言底层实现有兴趣的，推荐参考《Go语言设计与实现》

## 该笔记的架构

- 本笔记大的架构还是参考了Learning Go，但是对于内容顺序部分略有调整和删减
- 一、二、三、四章属于基础篇，主要是语言基础部分，
- 第五、六、七章开始属于语言特性篇
- 第八章属于应用与实战
- 后续可能持续更新像代码规范、常见的Go框架、Go项目代码分析(restic，因为我需要研究该项目)等内容，敬请期待

## Go语言发展历史

- 英文的维基百科写的比较有意思，推荐阅读：[https://en.wikipedia.org/wiki/Go_(programming_language)](https://en.wikipedia.org/wiki/Go_(programming_language))
- 简单来说Go语言是2007年在Google内部设计出来，本意是提高在特定领域的开发效率
- 由背景响当当的三位大牛设计，本着共同对C++的厌恶，设计了Go语言，简单来说就是取其精华去其糟粕
- ，一般的资料没有给出他们的年龄，我这里特意查了一下，我想大家能看出我们和美国之间的软件行业的差距了吧
   - Ken Thompson(1943年)
   - Rob Pike(1956年)
   - Robert Griesemer(1964年)

## Go语言应用情况

这是TIOBE给出的Go语言排名变化情况，可以看到Go语言爆发期是在2016到2017年之间，这两年应该也是容器领域最为活跃和火爆的两年。
![2022-06-12-06-48-23](/images/2022-06-12-06-48-23.png)


Kubernetes贡献情况统计
![2022-06-12-06-48-38](/images/2022-06-12-06-48-38.png)

这是docker/cli项目的贡献情况统计
![2022-06-12-06-48-53](/images/2022-06-12-06-48-53.png)

从Github第四季度统计情况来看，Go语言在Pull Requests排名第5位，处于上升趋势。
![2022-06-12-06-49-07](/images/2022-06-12-06-49-07.png)
