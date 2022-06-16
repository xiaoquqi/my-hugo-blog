---
title: 2.2 Go语言中的布尔型和整型
date: 2022-06-16T23:10:52+08:00
slug: "old-sun-learning-go-notes-2-2"
author: 老孙正经胡说
tags:
  - Go
  - Linux
categories:
  - Go
draft: false
---

## 变量类型

上一节对Go语言中的变量的定义方法进行了介绍，定义的方式一种是显示，一种为隐式。显示定义需要明确变量类型，而隐式定义则根据赋予的值来决定变量的类型。那么Go语言中到底有多少种变量类型呢？可以分为以下几种：

- 基本类型：数值、字符串、布尔型、常量等
- 集合类型：数组和结构体
- 引用类型：指针，切片(Slice)，Maps，函数和Channel
- 接口(Interface)类型

本节我们从基本类型开始学习，后续将为大家介绍数组、切片和Maps。

## 布尔型(bool)

布尔型是每一种语言中最常用的变量，Go语言中的关键字为bool, 允许的值为true或false，默认值为false，我们通过一段程序来看一下Go语言中的默认值。

```go
package main

import "fmt"

func main() {
    var a bool

    fmt.Printf("Bool default value: %v\n", a)
}
```

根据上一节的内容，我们也可以这样初始化bool类型的变量。

```go
a := false
```

## 数值类型(Numerical)

数值类型是所有语言中最常用的变量类型，Go语言中与数值类型相关的主要包括整型(int)，无符号整型(uint8)，浮点型(float32/float64，注意没有float类型)。

| Go变量类型 | 允许范围 | 默认值 |
| --- | --- | --- |
| int<br>int8<br>int16<br> rune → int32<br> int64 | uint8  : 0 to 255<br> uint16 : 0 to 65535 <br> uint32 : 0 to 4294967295 <br> uint64 : 0 to 18446744073709551615  | 0 |
| byte → uint8<br> uint16<br> uint32<br> uint64 | int8   : -128 to 127 <br> int16  : -32768 to 32767 <br> int32  : -2147483648 to 2147483647 <br> int64  : -9223372036854775808 to 9223372036854775807 | 0 |
| float32<br> float64 | math.SmallestNonzeroFloat32<br> math.MaxFloat32<br> math.SmallestNonzeroFloat64<br> math.MaxFloat64 | 0 |

- 对于32位的环境，整型为32位，对于64位的环境，整型为64位；当显示定义时，即使是32位系统，整型或浮点型64仍然是64
- float32和float64的最大最小值可以使用math模块的SmallestNonzeroFloat32和MaxFloat32获取，如果64位，则尾数修改为64

```go
package main

import (
    "fmt"
    "math"
)

func main() {
    fmt.Printf("min float64: %.50e\n", math.SmallestNonzeroFloat64)
    fmt.Printf("max float64: %.50e\n", math.MaxFloat64)

    fmt.Printf("min float32: %.50e\n", math.SmallestNonzeroFloat32)
    fmt.Printf("max float32: %.50e\n", math.MaxFloat32)
}
```

输出结果为

```go
min float64: 4.94065645841246544176568792868221372365059802614325e-324
max float64: 1.79769313486231570814527423731704356798070567525845e+308
min float32: 1.40129846432481707092372958328991613128026194187652e-45
max float32: 3.40282346638528859811704183484516925440000000000000e+38
```