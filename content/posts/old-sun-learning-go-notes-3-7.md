---
title: 3.7 Go语言中的异常处理(Panic和recovering)
date: 2022-06-26T22:54:14+08:00
slug: "old-sun-learning-go-notes-3-7"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本语法

异常处理是程序健壮性的关键，往往开发人员的开发经验的多少从异常部分处理上就能得到体现。如何适度的添加异常，往往是整个产品体验成败的关键。
Go语言中没有Try Catch Exception机制，但是提供了panic-and-recover机制。

### Panic

- 内置函数panic()
- 类似raise，能够停止正常的流程
- 当函数内调用panic，正常的流程将被终止，defer函数仍然会被执行
- Panic引起的原因可以是主动调用，也可以是运行时错误，例如数组越界

### Recover

- 内置函数，用于处理panic(panicking goroutine)
- 在defer函数中使用有意义，正常执行过程中，recover只会返回nil，而且没有其他副作用
- 如果当前Goroutine(后面讲到并发时会重点讲解，这里就是理解成程序的执行过程中)发生panicking，将自动捕获panic值给recover，同时恢复正常执行

## 示例一：recover()使用方法

本示例主要说明如何捕获异常，先来模拟一种异常情况，在一些项目中，经常有数组下标越界的情况，我们来人为构造一下

```go
package main

import "fmt"

func MyPanic() {
    fmt.Println("Running in MyPanic...")
    var a[]int
    a[3] = 5
}

func main() {
    MyPanic()
}
```

此时运行程序，很明显会出现如下问题：

```go
Running in MyPanic...
panic: runtime error: index out of range [3] with length 0

goroutine 1 [running]:
main.MyPanic()
	/root/workspace/go/test_panic_recover_basic.go:14 +0x5e
main.main()
	/root/workspace/go/test_panic_recover_basic.go:18 +0x17
exit status 2
```

尝试用recover进行异常处理

```go
package main

import "fmt"

func MyPanic() {
    defer func() {
        if x := recover(); x != nil {
            fmt.Printf("[ERROR]: My panic handle error: %s\n", x)
        }
    }()

    fmt.Println("Running in MyPanic...")
    var a[]int
    a[3] = 5
}

func main() {
    MyPanic()
}
```

就上面的代码进行一下分析：

- 首先增加了一个defer函数
- 在defer中，使用x := recover(); x != nil方式捕获异常，如果获取的值不为空，则证明有异常发生
- 获取异常信息时，直接用刚刚的变量就可以输出详细的错误信息，执行结果如下所示

```go
Running in MyPanic...
[ERROR]: My panic handle error: runtime error: index out of range [3] with length 0
```

## 实例二：panic()使用方法

本示例除了介绍panic()，还实现了一种统一的ErrorHandler方法(有点像Python中的装饰器)，来统一处理函数的异常

```go
package main

import "fmt"

func ErrorHandler(f func()) (b bool) {
    defer func() {
        if x := recover(); x != nil {
            fmt.Printf("[ERROR]Handle error here: %s\n", x)
            b = true
        }
    }()
    f()
    return
}

func CallPanic() {
    panic("Call panic")
}

func main() {
    fmt.Println(ErrorHandler(CallPanic))
}
```

我们来对代码进行一下分析：

- 定义了两个函数，一个是CallPanic()产生异常，一个是ErrorHandler()来捕获所有函数的异常
- CallPanic()逻辑很简单，就是用panic()内置函数产生异常，后面的参数就是异常的具体内容
- ErrorHandler的参数是一个函数，也就是利用函数作为值的特性，而返回值为bool类型
- ErrorHandler中对于异常捕获与示例一种相同，利用defer函数完成，而在函数体内，执行被调用的函数f()
- 从执行结果来看，ErrorHandler中输出了Call panic的异常和返回结果true