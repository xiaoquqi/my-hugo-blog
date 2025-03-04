---
title: 7.2 什么是Go语言中的管道Channel
date: 2023-01-05T20:00:43+08:00
slug: "old-sun-learning-go-notes-7-2"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 41
---

## 什么是管道Channel

为了解决与Groutines间的通讯问题，Go中提供给了管道Channel。Channel有点像是Linux系统的双向通讯管道，既可以发送消息，也可以接受消息。管道需要明确处理的数据类型，也就是在声明管道时必须还要声明类型。管道的定义方法如下：

```go
ci := make(chan int)
cs := make(chan string)
cf := make(chan interface{})
```

## 管道的使用

### 创建

我们建立这样的一个管道，这是一个没有任何缓存的bool型管道

```go
ch := make(chan bool)
```

也可以通过指定缓冲区大小定义管道的长度，下面示例中缓冲区可以存放两个元素，如果超过2个元素，则会阻塞并等待取走管道后，再进行写入，后续会有示例来详细讲解

```go
ch := make(chan bool, 2)
```

### 读取

这是读取管道的方法，程序运行时，将产生阻塞，直到从管道内读取到值

```go
value := <- ch
```

读取时，管道内将返回两个值，其中第二个值可以作为channel是否关闭的判断条件，以帮助我们更好的控制并发

```go
value, open := <-ch
if !open {
    fmt.Println("Channel is already closed")
}
```

### 写入

这是写入管道的方法，程序运行时，也将阻塞，一直等待有人将值读取走

```go
ch <- true
```

## 单并发使用示例

我们尝试来解决上一节遗留的问题，我们通过Channel在主函数中等待Channel实现异步的控制。<br />我们首先声明了一个channel，用于传输整数

```go
ch := make(chan int)
```

在ready函数中，我们在函数最后将运行时间输入管道之中

```go
c <- s
```

而在主函数中，我们读取管道内返回的值，这里管道其实并没有关闭，所以ok中返回的值仍然为true，管道仍然是打开状态

```go
value, ok := <- ch
```

这是完整的示例

```go
package main

import (
    "fmt"
    "time"
)

func ready(s int, c chan int) {
    fmt.Printf("Run func in a goroutine and wait for %v\n", s)
    time.Sleep(time.Second * time.Duration(s))
    fmt.Printf("Run func in a goroutine and wait for %v end\n", s)

    // Save wait interval to channel
    c <- s

    close(c)
}

func main() {

    ch := make(chan int)

    mainWaitSec := 2
    go ready(5, ch)

    fmt.Printf("Run Main function and wait for %v\n", mainWaitSec)
    time.Sleep(time.Second * time.Duration(mainWaitSec))
    fmt.Printf("Run Main function and wait for %v done\n", mainWaitSec)


    value, ok := <- ch
    fmt.Printf("Channel return value: %v\n", value)
    fmt.Printf("Channel ok returns: %v\n", ok)
}
```

执行结果如下

```go
Run Main function and wait for 2
Run func in a goroutine and wait for 5
Run Main function and wait for 2 done
Run func in a goroutine and wait for 5 end
Channel return value: 5
Channel ok returns: true
```

此时的执行结果按照我们预期返回并结束

## 多并发使用示例

假设我们将主函数中再异步调用一次ready函数，并且执行时间为10秒会发生什么呢？

```go
......
go ready(5, ch)
go ready(10, ch)
......
```

执行结果如下，我们并没有新增加的15秒并发ready函数退出就结束了，因为channel只接收到了第一次的ready函数的返回，后面无人处理后续管道返回，程序自然就退出返回了

```go
Run Main function and wait for 2
Run func in a goroutine and wait for 5
Run func in a goroutine and wait for 10
Run Main function and wait for 2 done
Run func in a goroutine and wait for 5 end
Channel return value: 5
Channel ok returns: true
```

解决这个问题很简单，我们可以使用select或者for循环方式，结合管道是否打开的返回，动态等待管道返回

### 使用for方式

```go
    for {
        value, ok := <- ch
        fmt.Printf("Channel return value: %v\n", value)
        fmt.Printf("Channel ok returns: %v\n", ok)

        if !ok {
            fmt.Println("No channel is open, break wait loop")
            break
        }
    }
```

这种方式下，for循环等价于，但是只能接受一个变量，不好判断channel结束，只能依靠额外的计数器进行判断

```go
for value := range ch {
    // do someting
}
```

完整代码如下所示

```go
package main

import (
    "fmt"
    "time"
)

func ready(s int, c chan int) {
    fmt.Printf("Run func in a goroutine and wait for %v\n", s)
    time.Sleep(time.Second * time.Duration(s))
    fmt.Printf("Run func in a goroutine and wait for %v end\n", s)

    // Save wait interval to channel
    c <- s

    close(c)
}

func main() {

    ch := make(chan int)

    mainWaitSec := 2
    go ready(5, ch)
    go ready(10, ch)

    fmt.Printf("Run Main function and wait for %v\n", mainWaitSec)
    time.Sleep(time.Second * time.Duration(mainWaitSec))
    fmt.Printf("Run Main function and wait for %v done\n", mainWaitSec)

    for {
        value, ok := <- ch
        fmt.Printf("Channel return value: %v\n", value)
        fmt.Printf("Channel ok returns: %v\n", ok)

        if !ok {
            fmt.Println("No channel is open, break wait loop")
            break
        }
    }

}
```

### 使用select-case方式

select块是为channel特殊设计的语法，它和switch语法非常相近。分支上它们都可以有多个case块和做多一个default块，但是也有很多不同

- select 到 括号{之间不得有任何表达式
- fallthrough关键字不能用在select里面
- 所有的case语句要么是channel的发送操作，要么就是channel的接收操作
- select里面的case语句是随机执行的，而不能是顺序执行的。设想如果第一个case语句对应的channel是非阻塞的话，case语句的顺序执行会导致后续的case语句一直得不到执行除非第一个case语句对应的channel里面的值都耗尽了。
- 如果所有case语句关联的操作都是阻塞的，default分支就会被执行。如果没有default分支，当前goroutine就会阻塞，当前的goroutine会挂接到所有关联的channel内部的协程队列上。 所以说单个goroutine是可以同时挂接到多个channel上的，甚至可以同时挂接到同一个channel的发送协程队列和接收协程队列上。当一个阻塞的goroutine拿到了数据接触阻塞的时候，它会从所有相关的channel队列中移除掉。

我们来看以下实现，需要注意的一点，break执行需要在select之外，否则就是死循环，如果有多个channel，也可以分别利用不同的标志判断管道是否完全关闭。

```go
    for {
        isOpen := true
        select {
        case value, ok := <- ch:
            fmt.Printf("Channel return value: %v\n", value)
            fmt.Printf("Channel ok returns: %v\n", ok)

            if !ok {
                isOpen = false
            }
        }
        if !isOpen {
            fmt.Println("No channel is open, break wait loop")
            break
        }
    }
```

完整代码如下所示

```go
package main

import (
    "fmt"
    "time"
)

func ready(s int, c chan int) {
    fmt.Printf("Run func in a goroutine and wait for %v\n", s)
    time.Sleep(time.Second * time.Duration(s))
    fmt.Printf("Run func in a goroutine and wait for %v end\n", s)

    // Save wait interval to channel
    c <- s

    close(c)
}

func main() {

    ch := make(chan int)

    mainWaitSec := 2
    go ready(5, ch)
    go ready(10, ch)

    fmt.Printf("Run Main function and wait for %v\n", mainWaitSec)
    time.Sleep(time.Second * time.Duration(mainWaitSec))
    fmt.Printf("Run Main function and wait for %v done\n", mainWaitSec)

    for {
        isOpen := true
        select {
        case value, ok := <- ch:
            fmt.Printf("Channel return value: %v\n", value)
            fmt.Printf("Channel ok returns: %v\n", ok)

            if !ok {
                isOpen = false
            }
        }
        if !isOpen {
            fmt.Println("No channel is open, break wait loop")
            break
        }
    }
}
```

### Deadlock异常

如果在循环内，不去判断channel关闭，会发生什么样的问题呢？错误如下：

```go
[2022-05-30 17:36:42.005288]Wait Goroutine Demo for 15 second(s) done
fatal error: all goroutines are asleep - deadlock!

goroutine 1 [chan receive]:
main.main()
	/root/workspace/go/test_goroutine_multiple_channels.go:49 +0x258
exit status 2
```

从错误信息我们可以看到，由于所有的goroutines都处于asleep状态，而主函数仍然在等待造成了死锁，所以必须显示的停止同步后，才能避免该问题的产生。

## 管道长度示例

上面已经提到管道可以指定长度方式来控制管道内的元素个数，下面通过一个示例来详细讲解

```go
package main

import (
    "fmt"
    "time"
)

func write(ch chan int) {
    for i := 1; i <= 5; i++ {
        fmt.Printf("[%d]Before Send]Current length is %d\n", i, len(ch))
        ch <- i
        fmt.Printf("[%d][After Send]Current length is %d\n", i ,len(ch))
    }

    close(ch)
}
func main() {
    ch := make(chan int, 2)
    fmt.Printf("Channel's intial cap is %d\n", cap(ch))
    fmt.Printf("Channel's intial len is %d\n", len(ch))

    go write(ch)

    time.Sleep(5 * time.Second)

    for {
        fmt.Printf("[Before Recieve]Current length is %d\n", len(ch))
        value, ok := <- ch
        fmt.Printf("[%d][After Recieve]Current length is %d\n", value, len(ch))

        time.Sleep(2 * time.Second)

        if !ok {
            break
        }
    }
}
```

我们通过输出可以看到：

- 队列初始化后，容量(cap)大小为2，而实际长度是0，表示没有元素
- 在触发异步函数后，前两个元素顺利写入
- 而到3时，Send处于阻塞状态
- 直到主函数内完成Sleep，开始接受元素后，3才发送成功
- 通过这个示例可以清楚看到，当元素个数达到我们定义的范围时，则形成阻塞，直到管道内的数据被取走后程序再继续运行

```go
Channel's intial cap is 2
Channel's intial len is 0
[1]Before Send]Current length is 0
[1][After Send]Current length is 1
[2]Before Send]Current length is 1
[2][After Send]Current length is 2
[3]Before Send]Current length is 2
[Before Recieve]Current length is 2
[1][After Recieve]Current length is 2
[3][After Send]Current length is 2
[4]Before Send]Current length is 2
[Before Recieve]Current length is 2
[2][After Recieve]Current length is 2
[4][After Send]Current length is 2
[5]Before Send]Current length is 2
[Before Recieve]Current length is 2
[3][After Recieve]Current length is 2
[5][After Send]Current length is 2
[Before Recieve]Current length is 2
[4][After Recieve]Current length is 1
[Before Recieve]Current length is 1
[5][After Recieve]Current length is 0
[Before Recieve]Current length is 0
[0][After Recieve]Current length is 0
```

## 参考文档

Channel运行逻辑及背后的一些原理，可以查看这篇文章
- Go Channel最佳实践之基本规则（[https://zhuanlan.zhihu.com/p/32521576](https://zhuanlan.zhihu.com/p/32521576)）