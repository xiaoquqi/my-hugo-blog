---
title: 2.3 Go语言中的字符型和常量定义
date: 2022-06-18T09:01:00+08:00
slug: "old-sun-learning-go-notes-2-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 字符类型

字符类型也是常用的类型之一，Go语言中的字符类型使用string关键字，我们对最早的hello, world示例进行改造。

```go
package main

import "fmt"

func main() {
    var s string
    s = "Hello, World"

    fmt.Println(s)
}
```

string类型的默认值就是一个空值，就是""，我们来看下面的例子

```go
package main

import "fmt"

func main() {
    var s string

    fmt.Printf("Default string is empty: %v\n", s == "")
}
```

在使用字符串时，以下两点需要注意：

- Go中的字符串都是UTF-8的字符，使用双引号定义，如果用单引号则是定义了一个字符。也就是单引号定义的字符实质上是byte类型即int32，我们来看下面的例子

```go
package main

import "fmt"

func main() {
    a := 'a'
    b := "b"

    fmt.Printf("a Value is %v\n", a)
    fmt.Printf("a Type is %T\n", a)

    fmt.Printf("b Value is %v\n", b)
    fmt.Printf("b Type is %T\n", b)
}
```

这段代码执行的结果如下，很明确看出我们分别用单引号定义的变量类型和双引号是完全不一样的

```go
a Value is 97
a Type is int32
b Value is b
b Type is string
```

- 同时，不能像Python语言中利用List随意修改字符串内的值，我们参考以下例子

```go
package main

import "fmt"

func main() {
    s := "hello"
    c := []rune(s)
    c[0] = 'c'
    s2 := string(c)
    fmt.Printf("%s\n", s2)
}

# 输出结果
# cello
```

在上面的例子中，需要使用类型转换的方式，先将字符串转为我们后面要介绍的数组类型后，修改其中的值，最后再转换成string类型的方式。这里用到了rune，下面是对rune的解释，可以看到rune实际上就是int32的别名。

> rune is an alias for int32 and is equivalent to int32 in all ways.
> It is used, by convention, to distinguish character values from integer values.
> [https://pkg.go.dev/builtin#rune](https://pkg.go.dev/builtin#rune)

### 字符串连接

与其他语言类似，Go中也可以使用+号对不同字符串形成连接，示例如下：

```go
func main() {
    fmt.Println("Hello!" + "!")
}
```

### 字符串操作模块

字符串操作的常用模块是strings，使用时只需要导入即可，这里只是进行基本使用方法介绍，在实际项目中，根据需求查询即可，参考官方文档：[https://pkg.go.dev/strings](https://pkg.go.dev/strings)

```go
import "strings"
```

这里列举一些常用的函数

| 函数名称 | 功能 |
| --- | --- |
| Compare() | 比较字符串是否相等 |
| Contains() | 字符串是否包含给定的子字符串 |
| Replaces() | 字符串替换 |
| ToLower() | 将字符串转换为小写 |
| ToUppper() | 将字符串转换为大写 |
| Split() | 将字符串分离 |

我们来看一个字符串比较的样例

```go
package main

import (
  "fmt"
  "strings"
)

func main() {
  // create three strings
  string1 := "Programiz"
  string2 := "Programia"
  string3 := "Programiz"

  // comparing strings
  fmt.Println(strings.Compare(string1, string2))  // 1
  fmt.Println(strings.Compare(string2, string3))  // -1
  fmt.Println(strings.Compare(string1, string3))  // 0
}
```

返回的结果如注释内容所示，我们发现Compare返回的并不是单纯的true/false，而是根据字符串的字典顺序进行的比较。

## 常量

### 基本使用方法

常量是开发中比较重要的静态数据管理手段，常量是不能够改变值的，Go语言中使用const进行定义，基本格式为

```go
const variableName [type] = value
```

这里的type只包含：

- 布尔型
- 数值型（整数型、浮点型和复数）
- 字符串型

来看一个简单的例子，我们来计算原型的面积，那么很显然圆周率PI就是常量

```go
package main

import "fmt"

const PI float64 = 3.14

func main() {
    var area float64
    radius := 3.0
    area = PI * radius * radius

    fmt.Printf("Area = %v\n", area)
}
```

### 批量定义

之前的章节提到，像import, const都可以进行批量定义，但是注意后面使用的是小括号，而非大括号，反正我总是写错。例如我们在定义任务状态机常量时，可以这样定义：

```go
package main

import "fmt"

const (
    SUCCESS = "success"
    FAIL = "fail"
)

func main() {
    fmt.Printf("Success const = %v\n", SUCCESS)
}
```

### iota定义自增常量

iota是一个可以被编译器修改的特殊常量，比如我们想批量定义一批常量，分别为从0到2，可以这样利用iota实现：

```go
package main

 import "fmt"

 func main() {
     const (
         a = iota
         b
         c
     )

     fmt.Println(a)
     fmt.Println(b)
 }

# 输出结果
# 0
# 1
# 2
```

关于为什么是iota，这里有一段解释，原来这个和技术无关的话题

> iota: not one iota, not the slightest difference(一丝不差)
> in reference to a phrase in the New Testament: “until heaven and earth pass away, not an iota, not a dot, will pass from the Law.”
> 新约中的一句话：“直到天地都过去了，没有一点，没有一点，将从法律中过去。”
> 参考链接：[https://splice.com/blog/iota-elegant-constants-golang/](https://splice.com/blog/iota-elegant-constants-golang/)