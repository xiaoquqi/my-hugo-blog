---
title: 3.8 Go语言中函数可变参数(Variadic Parameter)
date: 2022-07-07T17:27:10+08:00
slug: "old-sun-learning-go-notes-3-8"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本语法

在Python中，在函数参数不确定数量的情况下，可以使用如下方式动态在函数内获取参数，args实质上是一个list，而kwargs是一个dict

```python
def myFun(*args, **kwargs):
```

在Go语言中，也有类似的实现方式，只不过Go中只能实现类似*args的数组方式，而无法实现**kwargs的方式。实现这种方式，其实也是利用数组的三个点表达方式，我们这里来回忆一下。

> ### 关于三个点(...)Ellipsis的说明
> 我们经常在Go中看到这种方式，首先三个点的英文是Ellipsis，翻译成中文叫做“省略”，可能各位看到这个词就比较好理解三个点的作用了。在不同的位置上有不同的作用，比如在上述数组的定义中，省略了数组长度的声明，而是根据数组初始化值来决定。在函数定义中，我们还会看到类似的使用方法，我们再进行详细的说明。

其实本质上三个点的表达方式就是利用数组这一特性，实现可变参数。来看一下定义格式:

```
// arg will be [...]int
func myfunc(arg ...int) {}

// paras will be [...]string
func myfunc(arg, paras ... string) {}
```

## 示例一：函数中获取可变参数

循环获取可变参数，并且将部分arguments传入子函数

```go
package main

import "fmt"

func myfunc(arg ... string) {
    fmt.Printf("arg type is %T\n", arg)
    for index, value := range arg {
        fmt.Printf("And the index is: %d\n", index)
        fmt.Printf("And the value is: %v\n", value)
    }
}

func main() {
    myfunc("1st", "2nd", "3rd")
}
```

对上面的例子进行分析：

- 可变参数arg类型为[]string
- 通过for进行循环并获取值

```
arg type is []string
And the index is: 0
And the value is: 1st
And the index is: 1
And the value is: 2nd
And the index is: 2
And the value is: 3rd
```

## 示例二：将切片传给可变参数

我们在上面程序的基础上实现一个新的函数mySubFunc，尝试将切片(Slice)传递给该函数

```go
package main

import "fmt"

func myfunc(arg ... string) {
    fmt.Printf("arg type is %T\n", arg)
    for index, value := range arg {
        fmt.Printf("And the index is: %d\n", index)
        fmt.Printf("And the value is: %v\n", value)
    }

    // Call sub funcation with arguments
    fmt.Printf("Pass arguments: %v to mySubFunc\n", arg[1:])
    mySubFunc(arg[1:] ...)
}

func mySubFunc(arg ... string) {
    for index, value := range arg {
        fmt.Printf("SubFunc: And the index is: %d\n", index)
        fmt.Printf("SubFunc: And the value is: %v\n", value)
    }
}

func main() {
    myfunc("1st", "2nd", "3rd")
}
```

我们来分析一下这段代码:

- 与上面的代码大部分逻辑相同，这里利用切片arg[1:]获取部分可变参数的值
- 在传输给子函数mySubFunc()时，使用了这样的表达方式mySubFunc(arg[1:] ...)，这里补充一下...对于切片用法的说明
> ... signifies both pack and unpack operator but if three dots are in the tail position, it will unpack a slice.
> 在末尾位置的三个点会unpack一个切片

## 示例三：多参数

我们再来看一个多参数的例子

```go
package main

import "fmt"

func myfunc(num int, arg ... int) {
    fmt.Printf("num is %v\n", num)
    for _, value := range arg {
        fmt.Printf("arg value is: %d\n", value)
    }
}

func main() {
    myfunc(1, 2, 3)
}
```

来分析一下这个代码：

- 函数参数一个为整型变量num，和可变变量arg
- 主函数中第一个参数为num，而后面的则存储于arg中
- 所以输出结果如下

```go
num is 1
arg value is: 2
arg value is: 3
```