---
title: 6.4 Go语言中的空接口
date: 2022-11-23T08:25:59+08:00
slug: "old-sun-learning-go-notes-6-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 38
---

空接口即interface{}，也就是其中并没有对任务方法进行描述，既然没有约束，那么任务对象都满足空接口，简言之，空接口就是通配符。

## 空接口示例

```go
package main

import "fmt"

func main() {
    person := make(map[string]interface{}, 0)

    person["name"] = "Alice"
    person["age"] = 21
    person["height"] = 167.64

    fmt.Printf("%+v\n", person)
}
```

输出如下，不同于之前map定义时方式，value值的类型是空接口，也就是可以是任何的对象，所以这里无论值为string, int或是floay64都可以。

```go
map[age:21 height:167.64 name:Alice]
```

## 修改空接口对象值

对于上述示例，如果我们想修改其中的值，该如何处理呢？如果我们直接在输出前，添加

```go
person["age"] = person["age"] + 1
```

则在运行时出现如下错误：

```go
./test_empty_interface_modify.go:12:35: invalid operation: person["age"] + 1 (mismatched types interface {} and int)
```

为什么会出现这种情况，是因为值里其实存放的是interface{}，并非是int，所以要使用下面的方法进行类型转化后，再进行加法运算。

```go
package main

import "fmt"

func main() {
    person := make(map[string]interface{}, 0)

    person["name"] = "Alice"
    person["age"] = 21
    person["height"] = 167.64

    age, ok := person["age"].(int)
    if !ok {
        fmt.Println("could not assert value to int")
        return
    }

    person["age"] = age + 1

    fmt.Printf("%+v\n", person)
}
```

输出结果为

```go
map[age:22 height:167.64 name:Alice]
```

## 什么情况使用空函数

简单来说，如果你能清楚的知道所定义的对象的类型时，就不需要使用空接口。但是如果是一些不可预知的类型，可以考虑使用空接口，例如在json解析时，就额可以这样定义，无论json结构如何，都会存放于result中

```go
var result map[string]interface{}
json.Unmarshal(html, &result)
```