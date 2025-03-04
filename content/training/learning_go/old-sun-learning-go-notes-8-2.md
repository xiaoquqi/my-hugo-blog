---
title: 8.2 在Go语言中构建命令行
date: 2023-01-05T20:01:40+08:00
slug: "old-sun-learning-go-notes-8-2"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 45
---

命令行也是应用开发时必不可少的作用，命令行的样式相对比较统一，Go中提供了flag包用于定义命令行参数。

```go
package main

import (
    "flag"
    "fmt"
)

func main() {

    wordPtr := flag.String("word", "foo", "a string")

    numbPtr := flag.Int("numb", 42, "an int")
    forkPtr := flag.Bool("fork", false, "a bool")

    var svar string
    flag.StringVar(&svar, "svar", "bar", "a string var")

    flag.Parse()

    fmt.Println("word:", *wordPtr)
    fmt.Println("numb:", *numbPtr)
    fmt.Println("fork:", *forkPtr)
    fmt.Println("svar:", svar)
    fmt.Println("tail:", flag.Args())
}
```

运行帮助

```go
go run test_command_line.go --help
```

返回如下，基本可以满足常用命令行的构建

```go
Usage of /tmp/go-build3476798509/b001/exe/test_command_line:
  -fork
    	a bool
  -numb int
    	an int (default 42)
  -svar string
    	a string var (default "bar")
  -word string
    	a string (default "foo")
```

## 参考链接

当然也有很多第三方提供的Parser

- Kong is a command-line parser for Go([https://github.com/alecthomas/kong](https://github.com/alecthomas/kong))