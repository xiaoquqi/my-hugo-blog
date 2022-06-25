---
title: 2.10 Go语言中的注释、关键字、内置函数和操作符
date: 2022-06-23T07:53:42+08:00
slug: "old-sun-learning-go-notes-2-10"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Blog
draft: false
---

## 注释

一段好的代码就像艺术品，让读的人越看越有味道。注释是帮助他人理解代码最好的途径，合理添加的注释大幅度提高代码可读性。代码中的注释每个人原则都不同，我的原则是让读我代码的人，不需要问我的情况下就可以看懂全部内容。

Go语言中的注释与C语言中保持一致，一种是双斜线开头的//，一种是区域注释/* ... */

### 双斜线注释

//后面的空格并不是必须得，但是从美观角度来说，建议加上

```go
// Copyright © 2018 Inanc Gumus
// Learn Go Programming Course
// License: https://creativecommons.org/licenses/by-nc-sa/4.0/
//
// For more tutorials  : https://learngoprogramming.com
// In-person training  : https://www.linkedin.com/in/inancgumus/
// Follow me on twitter: https://twitter.com/inancgumus

// package main is a special package
// it allows Go to create an executable file
```

### 区域注释

```go
/*
This is a multi-line comment.
import keyword makes another package available
for this .go "file".
import "fmt" lets you access fmt package's functionality
here in this file.
*/
```

### 代码内部注释

当然代码注释内部既可以写在顶部，也可以写在和代码同行的尾部，我个人习惯写在顶部，这样比较容易区分，写在代码尾部的注释类似评论，能更快速的解释代码，所以呢，还是看需求。

```go
package main

import (
	"fmt"
)

func main() {
	// Print “Hello, World!” to console
	fmt.Println("Hello, World!") // Use fmt to print out
}

```

## 常用关键字(按照字母顺序)

| 关键字 | 说明 |
| --- | --- |
| break | 阻断for循环，2.8节已经讲过了 |
| case | 用于和swtich...case或select...case，其中switch...case在2.9节讲到，select...case会在并发中的channel提到 |
| chan | 管道定义，会在并发章节中提到 |
| const | 常量定义关键字，2.3节讲过了 |
| continue | 进入下一次循环，2.8节讲过了 |
| default | 默认行为，在switch...case中用到过，2.9节有示例 |
| defer | 延迟函数，下一章函数会讲到 |
| else | 与if搭配，在2.7节讲过了 |
| fallthrough | 在2.9节switch...case中讲到，用于继续执行switch中其他case |
| for | 循环，2.8节讲过了 |
| func | 函数定义，下一章就要讲到 |
| go | 这个不是外部命令go，而是用于实现Goroutines的关键字，并发章节会讲到 |
| goto | 强制改变代码执行逻辑，破坏代码执行逻辑，所以没有讲 |
| if | 条件判断，2.7节已经讲过了 |
| import | 用于导入Module关键字，这些例子一直在用 |
| interface | 接口定义关键字，接口章节会用到 |
| map | Go语言中的哈希，2.6节讲到 |
| package | 包定义关键字，Packages会讲到 |
| range | 搭配for，能够对数组、切片、Map、字符串、Channel进行循环，2.8节讲过，后面讲到并发Channel时还会用到 |
| return | 函数返回，函数章节会讲到 |
| select | 和switch相似，主要用于Channel，并发章节会讲到 |
| stuct | 结构体定义，进阶章节会讲到 |
| switch | if elseif的另一种表达方式，2.9节已经讲到 |
| type | 自定义类型定义关键字，后面讲到进阶中的结构体时会大量用到 |
| var | 变量定义关键字，在例子中大量出现 |

## 常用内置函数(按关键字排序)

| 函数名称 | 说明 |
| --- | --- |
| close | 用于关闭channel，并发章节会讲到 |
| delete | 删除maps的元素，2.6节Map的CURD操作用到过 |
| len | 多种对象的长度，包括字符、maps、slice和数组，很多例子中出现了，2.5节特别提到过与cap区别 |
| cap | 类似len，返回对象的实际容量，2.5节讲过 |
| new | Go语言中数据类型分配内存，与make有类似的作用，没有特别提到或用到，主要使用make方法较多，这一部分也许后面会出单独的一节来重点讲解和make区别 |
| make | 内部类型分配内存 |
| append | 在slice中增加元素，在2.5节讲到 |
| copy | 拷贝slice，在2.5节讲到 |
| panic | 用于异常处理，函数章节会讲到 |
| recover | 用于异常处理，函数章节会讲到 |
| print | 底层打印函数，主要用于调试，我们代码的例子都是用fmt模块中的print方法 |
| println | 底层打印函数，主要用于调试 |
| complex/real/imag | 主要用于处理compex numbers，没有特别讲到，如有需要后续会单独去讲这一部分 |

## 操作符优先级

| **Precedence** | **Operator(s)** | **备注** |
| --- | --- | --- |
| Highest | * / % << >> & &^ | & |
|  | `+ - | + 可以用于证书、浮点、复杂数字的连接 |
|  | == != < <= > >= |  |
|  | <- |  |
|  | && | && 和 |
| Lowest | &#124;&#124; |  |