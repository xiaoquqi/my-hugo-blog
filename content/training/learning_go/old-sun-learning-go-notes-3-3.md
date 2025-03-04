---
title: 3.3 Go语言中的main函数和init函数
date: 2022-06-26T22:54:03+08:00
slug: "old-sun-learning-go-notes-3-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 16
---

## main函数

其实从之前的示例中我们已经发现，所有的例子都包含main函数，这也是Go语言中较为特殊的函数。

- 执行的入口函数为main()
- 不接受参数，也不返回参数
- 不需要显示调用
- 每个包都必须要包含单个main包和main()函数

由于使用了很多次，这里就不再举例说明了。

## init函数

除了main函数，还有一个特殊的函数叫init，简单理解就是在main函数之前执行，由于我自己阅读Go代码有限，对应用场景还没很直观的认识，所以后续可能还需要加深理解后，再进行讲解，大家也可以参考一下参考文档中的两篇来加深理解，我直接用一个例子来进行说明。

```go
package main

import "fmt"

func init() {
    fmt.Println("First init called.")
}

func init() {
    fmt.Println("Second init called.")
}

func init() {
    fmt.Println("Third init called.")
}

func main() {
    fmt.Println("Main function called")
}
```

执行结果如下，有以下值得注意的点：

- init在main之前执行
- 可以定义多个init()
- init()按照顺序执行

```go
First init called.
Second init called.
Third init called.
Main function called
```

## 参考文档

- [https://www.geeksforgeeks.org/main-and-init-function-in-golang/?ref=lbp](https://www.geeksforgeeks.org/main-and-init-function-in-golang/?ref=lbp)
- [https://www.digitalocean.com/community/tutorials/understanding-init-in-go](https://www.digitalocean.com/community/tutorials/understanding-init-in-go)