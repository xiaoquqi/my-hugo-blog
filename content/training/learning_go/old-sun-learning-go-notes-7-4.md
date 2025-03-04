---
title: 7.4 Go语言中并发运行数量
date: 2023-01-05T20:01:01+08:00
slug: "old-sun-learning-go-notes-7-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 43
---

## 基本概念

自 Go 1.5 开始，Go的GOMAXPROCS 默认值已经设置为CPU的核数，这允许我们的Golang程序充分使用机器的每一个 CPU, 最大程度的提高我们程序的并发性能。Golang的调度器采用M-P-G

- G 代表 goroutine，即用户创建的 goroutines
- P 代表 Logical Processor，是类似于 CPU 核心的概念，其用来控制并发的 M 数量
- M 是操作系统线程。在绝大多数时候，P 的数量和 M 的数量是相等的。每创建一个 P, 就会创建一个对应的 M

![2023-01-10-22-38-44](/images/2023-01-10-22-38-44.png)

通过设置GOMAXPROCS环境变量可以控制P的数量

```go
export GOMAXPROCS=1
```

来看下程序中通过runtime获取该变量

```go
package main

import (
    "fmt"
    "runtime"
)

func main() {
    fmt.Printf("NumCPU: %d, GOMAXPROCS: %d\n", runtime.NumCPU(), runtime.GOMAXPROCS(-1))
}
```

输出的内容

```go
NumCPU: 8, GOMAXPROCS: 1
```

更多详细的原理部分，请查阅参考文档，在一些特定场景下（例如容器），可能会遇到与并发量有关的问题，需要合理的对参数进行设定。

## 参考文档

- GOMAXPROCS 的坑——容器环境中使用 runtime.GOMAXPROCS 需谨慎([https://pandaychen.github.io/2020/02/28/GOMAXPROCS-POT/](https://pandaychen.github.io/2020/02/28/GOMAXPROCS-POT/))