---
title: 4.7 Go语言常用包
date: 2022-07-16T09:57:03+08:00
slug: "old-sun-learning-go-notes-4-7"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 28
---

在本章节的最后一部分，我们来看一下系统中常用的一些包的介绍，方便大家在有需要时使用。

## 获取GOROOT

如何查看已经安装的系统模块呢？可以到$GOROOT/src下进行查看，获取GOROOT的方法

```go
go env GOROOT
```

## 常用模块

| 包名称 | 功能 |
| --- | --- |
| fmt | 格式化的输入输出，等同于C语言中的printf和scanf，格式化的动词来自于C语言，但是更简单，常用的动词有：<br>- %v - 根据值类型输出，如果需要输出为结构体，使用加号%+v，可以输出字段名称<br>- %#v - Go语法，代表值<br>- %T - Go语法，代表值类型 |
| io | I/O的基础接口封装 |
| bufio | 实现缓存I/O，封装了io.Reader和io.Writer对象 |
| sort | 用于数组和用户定义的Collection排序 |
| strconv | 字符类型与普通类型的转换 |
| os | 操作系统操作封装 |
| sync | 同步封装，例如实现互斥锁 |
| flag | 命令行标志解析 |
| encoding/json | Json的encoding和decoding |
| html/template | 生成文本的输出的数据驱动模板 |
| net/http | http封装，提供了可扩展的服务端和客户端 |
| unsafe | 提供绕过Go安全类型的能力，通常不需要 |
| reflect | 实现运行时反射 |
| os/exec | 执行外部命令 |