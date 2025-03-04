---
title: 7.1 Go语言中什么是Goroutines
date: 2023-01-05T20:00:35+08:00
slug: "old-sun-learning-go-notes-7-1"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 40
---

## 基本概念

Goroutine是一个被Go运行时管理的轻量级线程(A goroutine is a lightweight thread managed by the Go runtime)。<br />为什么没有采用现有的表示并发名词来解释Go语言中的并发呢？因为现有的线程、协程、进程等都无法准确表达Goroutine。

## Goroutines使用方法

### 函数并发执行

与普通函数类似，我们调用Goroutines时只需要在函数前加上go关键字。下面的例子中go ready()就会并发执行。

```go
package main

import (
    "fmt"
    "time"
)

func ready() {
    fmt.Println("Run func in a goroutine")
}

func main() {

    go ready()

    time.Sleep(time.Second * 3)
    fmt.Println("Main function done")
}
```

### 匿名并发函数

如果你不想单独定义，则可以使用匿名方式

```go
package main

import (
    "fmt"
    "time"
)

func main() {

    go func() {
        fmt.Println("Run anonymous func in goroutine.")
    }()

    time.Sleep(time.Second * 3)
    fmt.Println("Main function done")
}
```

## 如何控制并发

上面的示例中，我们在主函数刻意的等待了3秒，如果没有这3秒会发生什么呢？我们将time.Sleep注释掉，另外由于time模块没有使用，也需要注释掉

```go
package main

import (
    "fmt"
    //"time"
)

func ready() {
    fmt.Println("Run func in a goroutine")
}

func main() {

    go ready()

    //time.Sleep(time.Second * 3)
    fmt.Println("Main function done")
}
```

此时我们发现Goroutine好像并没有执行，因为只有main函数中print语句输出了结果：

```go
Main function done
```

那么究竟Goroutine到底有没有被触发呢？我们再通过这个例子看一下，这个例子中，main函数需要等待2秒，而Goroutine内执行的函数则需要等待5秒

```go
package main

import (
    "fmt"
    "time"
)

func ready(s int) {
    fmt.Printf("Run func in a goroutine and wait for %v\n", s)
    time.Sleep(time.Second * time.Duration(s))
    fmt.Printf("Run func in a goroutine and wait for %v end\n", s)
}

func main() {

    mainWaitSec := 2

    go ready(5)

    fmt.Printf("Run Main function and wait for %v\n", mainWaitSec)
    time.Sleep(time.Second * time.Duration(mainWaitSec))
    fmt.Printf("Run Main function and wait for %v done\n", mainWaitSec)
}
```

程序运行后，虽然mian函数和ready函数中都print了开始执行的语句，但是很明显，在Goroutine内的函数并没有执行完成。所以我们为了更精准的控制Goroutine的并发，需要使用Channel进行控制。

```go
Run Main function and wait for 2
Run func in a goroutine and wait for 5
Run Main function and wait for 2 done
```