---
title: 3.2 Go语言中的匿名函数
date: 2022-06-26T22:54:01+08:00
slug: "old-sun-learning-go-notes-3-2"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Blog
draft: false
---

Go不允许函数嵌套，但是可以定义匿名函数，后续配合Goroutine的使用，很轻松的构建并发程序。

## 语法定义

匿名函数一般是在函数体内的独立逻辑，与函数定义类似，但是由于其特殊位置，在使用时需要注意：

- 在定义时主要为参数列表和返回值，如果不定义返回值类型，就不要使用return
- 在定义的尾部不要忘了执行，即()，否则会看到定义未使用的提示(func literal evaluated but not used)；当然在Go语言中我们是可以将函数整体复制给变量的，后续只需要变量后面加()执行即可
- 与正常带返回值的函数一样，接受返回值的时候，需要提供一个变量

```go
func(Parameter-list) (Return-Type){
// code..

// Use return statement if Return-Type are given
// if Return-Type is not given, then do not 
// use return statement
return
}()
```

## 无返回值

```go
package main

import "fmt"

func main() {
    func () {
        fmt.Println("Hello, World")
    }()
}
```

## 有返回值

```go
package main

import "fmt"

func main() {
    msg := func () string {
        return "Hello, World"
    }()

    fmt.Println(msg)
}
```

## 传入参数

```go
package main

import "fmt"

func main() {
    func (s string) {
        fmt.Println(s)
    }("Hello, World")
}
```

## 函数赋值给变量

```go
package main

import "fmt"

func main() {
    myFunc := func (s string) {
        fmt.Println(s)
    }

    myFunc("Hello, World")
}
```