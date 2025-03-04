---
title: 2.7 Go语言中的if-else
date: 2022-06-23T07:53:34+08:00
slug: "old-sun-learning-go-notes-2-7"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 10
---

从本节开始学习Go语言中的控制结构，其实每一种语言的控制结构非常雷同，只是在关键字、格式上略有差别。

## 基本语法if-else

Go中基本if-else的使用方法

```go
package main

import {
    "fmt"
}

func main() {
    if 5 > 1 {
        fmt.Println("bigger!")
    } else {
        fmt.Println("smaller!")
    }
}
```

## 多重条件if-else if-else

这里有几个知识点需要注意：

- Go语言中else if的表达方法
- 对于条件，可以有括号，也可以没有括号，根据计算优先级都是一样的
- 或操作是||，并且是&&，否是!
- Go语言中还有Switch的表达方式，如果有else if太多了，Switch是不错的选择

```go
package main

import "fmt"

func main() {
    i := 8

    if !( i > 0 ) {
        fmt.Println("i is below zero")
    } else if ( i > 0 ) && ( i <= 3 ) {
        fmt.Println("i is between 0 and 3")
    } else if ( i > 3 && i <= 7 ) {
        fmt.Println("i is between 4 and 7")
    } else if ( ( i > 7 ) && ( i <= 10 ) ) {
        fmt.Println("i is between 7 and 10")
    } else {
        fmt.Println("i is bigger than 10")
    }
}
```

## 常用类型的空判断

这里罗列出常用变量类型的为空判断，可以看到整型、浮点型默认值等于0，布尔型为false，而数组和Map为nil

```go
package main

import "fmt"

func main() {
    var b bool
    if !b {
        fmt.Printf("bool b default is %v\n", b)
    }

    var i int
    if i == 0 {
        fmt.Printf("i == 0: %v\n", i == 0)
    }

    var f float64
    if f == 0 {
        fmt.Printf("f == 0: %v\n", f == 0)
        fmt.Printf("f == 0.0: %v\n", f == 0.0)
    }

    var str string
    if str == "" {
        fmt.Printf("str == \"\": %v\n", str == "")
    }

    var myarray []int
    if myarray == nil {
        fmt.Printf("myarray == nil: %v\n", myarray == nil)
    }

    var mymap map[int]string
    if mymap == nil {
        fmt.Printf("mymap == nil: %v\n", mymap == nil)
    }
}
```