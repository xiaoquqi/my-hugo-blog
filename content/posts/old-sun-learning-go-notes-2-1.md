---
title: 2.1 Go语言中的变量定义
date: 2022-06-15T23:30:43+08:00
slug: "old-sun-learning-go-notes-2-1"
author: 老孙正经胡说
tags:
  - Go
  - Linux
categories:
  - Go
draft: false
---

## 变量定义

- 变量的赋值和分配值是两个过程，但是可以合二为一，简单来说，:=相当于声明类型并赋值，而=与我们常规理解的等号操作相似

```go
var a int
a = 15

// 相当于===>

a := 15
```

## 批量定义

- 可以成组定义变量
- const和import也可以这样使用

```go
var (
    x int
    b bool
)
```

- 也可以批量定义同一类型的变量

```go
var x, y int
```

- 或者批量赋值

```go
a, b := 20, 16
```

- 特殊的变量名称是_，该变量在赋值后会被丢弃，类似Unix系统的/dev/null
- 以下代码在编译阶段出现./test_var.go:7:16: cannot use _ as value

```go
package main

 import "fmt"

 func main() {
     _, b := 2, 3
     fmt.Println(_)
 }
```
