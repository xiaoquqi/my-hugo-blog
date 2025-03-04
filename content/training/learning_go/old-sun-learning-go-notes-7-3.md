---
title: 7.3 Go语言中通过WaitGroup控制并发
date: 2023-01-05T20:00:50+08:00
slug: "old-sun-learning-go-notes-7-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 42
---

## 与Channel区别

Channel能够很好的帮助我们控制并发，但是在开发习惯上与显示的表达不太相同，所以在Go语言中可以利用sync包中的WaitGroup实现并发控制，更加直观。

## 基本使用示例

我们将之前的示例加以改造，引入sync.WaitGroup来实现并发控制。

- 首先我们在主函数中定义WaitGroup

```go
var wg sync.WaitGroup
```

- 每执行一个任务，则调用Add()方法

```go
wg.Add(1)
```

- 在主函数中我们利用Wait()方法等待并发结束

```go
wg.Wait()
```

- 在调用的函数中，我们需要将WaitGroup以指针方式传入，否则将造成Deadlock

```go
// 主函数内
go ready(5, &wg)

// 函数
func ready(s int, wg *sync.WaitGroup)
```

- 同时在函数执行完成后，调用wg.Done，我们使用defer实现

```go
defer wg.Done()
```

### 完整代码

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

func ready(s int, wg *sync.WaitGroup) {

    defer wg.Done()

    fmt.Printf("Run func in a goroutine and wait for %v\n", s)
    time.Sleep(time.Second * time.Duration(s))
    fmt.Printf("Run func in a goroutine and wait for %v end\n", s)
}

func main() {

    var wg sync.WaitGroup

    wg.Add(1)
    go ready(5, &wg)

    mainWaitSec := 2
    fmt.Printf("Run Main function and wait for %v\n", mainWaitSec)
    time.Sleep(time.Second * time.Duration(mainWaitSec))
    fmt.Printf("Run Main function and wait for %v done\n", mainWaitSec)

    wg.Wait()

}
```

### 特别提示

WaitGroup传入给函数时，需要以指针方式传递，否则会造成Deadlock

## 多任务示例

如果不想在函数中传递WaitGroup，也可以采用以下这种方式，通过并发匿名函数的方式，在主函数逻辑中对并发进行精准控制

```go
    var wg sync.WaitGroup

    for i := 0; i < 5; i++ {
        wg.Add(1)

        waitSec := i + 1
        go func() {
            defer wg.Done()
            ready(waitSec)
        }()
    }
```

### 完整代码

```go
package main

import (
    "fmt"
    "sync"
    "time"
)

func ready(s int) {
    fmt.Printf("Run func in a goroutine and wait for %v\n", s)
    time.Sleep(time.Second * time.Duration(s))
    fmt.Printf("Run func in a goroutine and wait for %v end\n", s)
}

func main() {

    var wg sync.WaitGroup

    for i := 0; i < 5; i++ {
        wg.Add(1)

        waitSec := i + 1
        go func() {
            defer wg.Done()
            ready(waitSec)
        }()
    }

    mainWaitSec := 2
    fmt.Printf("Run Main function and wait for %v\n", mainWaitSec)
    time.Sleep(time.Second * time.Duration(mainWaitSec))
    fmt.Printf("Run Main function and wait for %v done\n", mainWaitSec)

    wg.Wait()

}
```

运行结果如下

```go
Run Main function and wait for 2
Run func in a goroutine and wait for 2
Run func in a goroutine and wait for 4
Run func in a goroutine and wait for 5
Run func in a goroutine and wait for 1
Run func in a goroutine and wait for 3
Run func in a goroutine and wait for 1 end
Run Main function and wait for 2 done
Run func in a goroutine and wait for 2 end
Run func in a goroutine and wait for 3 end
Run func in a goroutine and wait for 4 end
Run func in a goroutine and wait for 5 end
```