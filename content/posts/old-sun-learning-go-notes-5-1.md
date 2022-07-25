---
title: 5.1 Go语言中的指针
date: 2022-07-25T18:10:16+08:00
slug: "old-sun-learning-go-notes-5-1"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本概念

Go语言中仍然有指针，但是没有指针运算，所以不同于C语言指针，更像是引用。Go语言调用函数时，是传递的值，所以为了提高效率，仍然保留指针。

- 使用*进行定义，例如：var p *int，现在p是一个指向int类型的指针
- 所有新声明的变量都分配了相应的零值，指针也不例外。新声明或未指向的指针，值为nil
- 让指针指向时使用操作符address-of-operator(&)

## 示例一：指针与地址

```go
package main

import "fmt"

func main() {
    var p *int
    fmt.Printf("initial pointer p = %v\n", p)

    var i int
    p = &i
    fmt.Printf("point to int p = %v\n", p)
    fmt.Printf("point to int value p = %v\n", *p)
}
```

输出如下，在未指向任何变量前p的值为nil，指向整型i后，p的值为地址，p的值为整型的默认值

```go
initial pointer p = <nil>
point to int p = 0xc0000bc000
point to int value p = 0
```

## 示例二：指针++

因为指针没有运算，所以*p++等同于(*p)++

```go
package main

import "fmt"

func main() {
    var p *int
    var i int

    p = &i

    *p++
    fmt.Printf("*p++ = %v\n", *p)

    (*p)++
    fmt.Printf("(*p)++ = %v\n", *p)
}
```

输出结果为

```go
*p++ = 1
(*p)++ = 2
```