---
title: 3.6 Go语言函数的延迟调用(Deferred Code)
date: 2022-06-26T22:54:11+08:00
slug: "old-sun-learning-go-notes-3-6"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 19
---

先解释一下这篇Blog延期的原因，本来已经准备好了全部内容，但是当我重新回顾实例三的时候，发现自己还是存在认知不足的地方，于是为了准确表述，查阅了大量的资料，重新编写了第三部分，导致延期。感谢持续关注本笔记更新的朋友，后期我将逐步通过3-5分钟视频方式为大家对笔记内容进行讲解，帮助更多的朋友能够快速掌握Go语言的基础。
本节将介绍Go语言函数和方法中的延迟调用，正如名称一样，这部分定义不会立即执行，一般会在函数返回前再被调用，我们通过下面的几个示例来了解一下延迟调用的使用场景。

## 基本功能

在以下这段代码中，我们操作一个文件，无论成功与否都需要关闭文件句柄。这里在三处不同的位置都调用了file.Close()方法，代码显得非常冗余。

```go
func ReadWrite() bool {
    file.Open("file")
    // Do your thing
    if failureX {
        file.Close()
        return false
    }

    if failureY {
        file.Close()
        return false
    }
    file.Close()
    return true
}
```

我们利用延迟调用来优化代码。定义后的defer代码，会在return之前返回，让代码显得更加紧凑，且可读性变强，对上面的代码改造如下：

```go
func ReadWrite() bool {
    file.Open("filename")
    // Define a defer code here
    defer file.Close()
    // Do your thing
    if failureX {
        return false
    }
    if failureY {
        return false
    }
    return true
}
```

## 示例一：延迟调用执行顺序

我们通过这个示例来看一下延迟调用与正常代码之间的执行顺序

```go
package main

import "fmt"

func TestDefer(x int) {
    defer fmt.Println("Defer code called")
    switch x {
    case 1:
        fmt.Println("Case 1 triggered!")
        return
    case 10:
        fmt.Println("Case 10 triggered!")
        return
    default:
        fmt.Println("Case default triggered!")
        return
    }
}

func main() {
    TestDefer(100)
    TestDefer(1)
    TestDefer(10)
}
```

先简单分析一下代码逻辑：

- 首先定义了一个公共的TestDefer函数，这个函数接受一个整型的参数
- 函数体内定义了defer部分，会输出一句Defer code called
- switch case会根据输入的整型参数，输出相应的trigger语句
- 按照上面对延迟调用的分析，每次满足case语句后，才会输出Defer code called

从输出中，我们可以观察到如下现象：

- 首次执行，default条件满足，Case default triggered先输出，再输出defer内容
- 第二次调用，1条件满足，最后输出defer内容
- 第三次调用，10条件满足，最后输出defer内容

从这个实例中，我们很明显观察到，defer语句是在return之前执行

```go
Case default triggered!
Defer code called
Case 1 triggered!
Defer code called
Case 10 triggered!
Defer code called
```

## 示例二：多defer使用方法

如果一个函数内定义了多个defer，则调用顺序为LIFO（后进先出）方式执行。

```go
package main

import "fmt"

func TestDefer(x int) {
    defer fmt.Println("1st defined Defer code called")
    defer fmt.Println("2nd defined Defer code called")
    defer fmt.Println("3rd defined Defer code called")
    switch x {
    case 1:
        fmt.Println("Case 1 triggered!")
        return
    case 10:
        fmt.Println("Case 10 triggered!")
        return
    default:
        fmt.Println("Case default triggered!")
        return
    }
}

func main() {
    TestDefer(100)
}
```

仍然是相同的例子，但是在TestDefer中我们定义了三个defer输出，根据LIFO原则，输出的顺序是3rd->2nd->1st，根据最后的结果，也是逆向向上执行defer输出。

```go
Case default triggered!
3rd defined Defer code called
2nd defined Defer code called
1st defined Defer code called
```

## 实例三：defer与局部变量、返回值的关系

就在整理这篇笔记的时候，发现了自己的认知误区，主要是本节实例三中发现的，先来看一下英文的描述：

> A defer statement pushes a function call onto a list. The list of saved calls is executed after the surrounding function returns. Defer is commonly used to simplify functions that perform various clean-up actions.

对于上面的这段话的理解：

- defer定义的函数会被放入list中
- 存储的defer函数会在周边函数返回后执行
- defer一般用于环境清理

### 原则一：defer函数的参数值，取决于defer函数调用时变量的值

```go
package main

import "fmt"

func a() int {
    i := 0
    fmt.Printf("func i = %v\n", i)
    defer fmt.Printf("defer i = %v\n", i)
    i++
    fmt.Printf("func i = %v\n", i)
    defer fmt.Printf("defer after i++ = %v\n", i)
    return i
}

func main() {
    i := a()
    fmt.Printf("main i = %v\n", i)
}
```

下面是代码执行输出，我们来一起分析一下：

- 在函数a中，定义了局部变量i
- 在函数执行过程中进行了自增操作i++
- 分别在i++前后，对i值进行了输出，也就是我们下面输出结果前两行，与预期一致
- 分别在i++前后，定义两个defer语句，都是用fmt输出i的值，输出的顺序与示例二的逻辑一致，先输出的是defer after，再输出defer
- 根据原则一，在defer after的输出中，由于i++完成自增，所以当时i的值已经变为了1，所以输出为1
- 同样是根据原则一，在defer的输出中，i并没有进行自增，所以在当时情况下，i的值仍然为0，所以输出为0
- 最后返回的i值为1，主函数中输出i的值为1

```go
func i = 0
func i = 1
defer after i++ = 1
defer i = 0
main i = 1
```

### 原则二：defer可以读取或修改显示定义的返回值

```go
package main

import "fmt"

func a() (i int) {
    fmt.Printf("func initial i = %v\n", i)
    defer func() {
        fmt.Printf("defer func initial i++ = %v\n", i)
        i++
        fmt.Printf("defer func after i++ = %v\n", i)
    }()
    fmt.Printf("func before return i = %v\n", i)
    return 10
}

func main() {
    i := a()
    fmt.Printf("main i = %v\n", i)
}
```

虽然在a()函数内，显示的返回了10，但是main函数中得到的结果是defer函数自增后的结果，我们来分析一下代码：

- 在a函数定义时，我们显示的定义了返回变量i和类型int
- 在刚刚进入函数时，i的初始化值位0，返回前也是0
- 在最后的return时，直接返回了10
- 接着我们再来看defer函数执行情况，刚刚进入defer函数时，返回值i得到的值正是刚才返回的10
- 而在自增后，i的值变成了11
- 最后我们在主函数中，获得的返回值也是11，印证了我们原则中的defer函数对于返回值的读取和修改

```go
func initial i = 0
func before return i = 0
defer func initial i++ = 10
defer func after i++ = 11
main i = 11
```

在这篇文章的上一版，我曾经尝试用指针取解释defer修改返回值的类型，但是感觉不够透彻，也让阅读者非常困惑，索性参考了一下go官方blog中的一篇文章，在此基础上进行了扩展。如需要阅读原文，可以参考下面的文章。

## 参考文档

- [https://go.dev/blog/defer-panic-and-recover](https://go.dev/blog/defer-panic-and-recover)