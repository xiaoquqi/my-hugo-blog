---
title: 4.5 使用Go Modules自定义模块
date: 2022-07-08T14:16:13+08:00
slug: "old-sun-learning-go-notes-4-5"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

在我们开发项目时，总会使用到第三方的库来简化我们的开发，所以几乎每一种开发语言都会有自身的包管理机制，例如：Python中的PIP，Java中的Maven，Node.js中的NPM等。如果有看过一些Go的项目，会发现代码的根目录都会有go.mod文件，这是Go中对项目模块集中管理的方式，也是可以将自身作为模块供其他模块使用的方式。本文档主要参考官方的教程《Tutorial: Create a Go module》([https://go.dev/doc/tutorial/create-module](https://go.dev/doc/tutorial/create-module))思路，对内容部分进行了简化和调整。

上一节中，GOPATH方式虽然解决了包的引用问题，但是从不够灵活，也不利于包的传输，所以在1.1版本推出了Go Modules，到了1.4版本已经是生产可用状态，我们看到目前很多大型项目基本都是采用这种方式来管理自己的包，这一部分将会在Go Modules单独进行讲解。所以在开始之前，一定要确认GO111MODULE状态，要将GO111MODULE设置为on。

```go
# 查看状态
go env GO111MODULE

# 通过环境变量设置状态(临时)
export GO111MODULE=on

# 永久生效
# go env -w GO111MODULE=on
```

另外在上一节，由于我们改变了默认的GOPATH位置，所以我们首先要还原一下GOPATH，默认的GOPATH就是用户$HOME/go路径，后续使用命令安装的包也会缓存于此。

```go
go env -w GOPATH=""
```

## 常用命令

Go的模块管理工具是内置的，不需要单独安装。Go中与Modules管理主要使用go mod命令，命令列表如下，不用纠结这些命令该如何使用，通过下面的例子我们加以理解。

```go
Go mod provides access to operations on modules.

Note that support for modules is built into all the go commands,
not just 'go mod'. For example, day-to-day adding, removing, upgrading,
and downgrading of dependencies should be done using 'go get'.
See 'go help modules' for an overview of module functionality.

Usage:

	go mod <command> [arguments]

The commands are:

	download    download modules to local cache
	edit        edit go.mod from tools or scripts
	graph       print module requirement graph
	init        initialize new module in current directory
	tidy        add missing and remove unused modules
	vendor      make vendored copy of dependencies
	verify      verify dependencies have expected content
	why         explain why packages or modules are needed

Use "go help mod <command>" for more information about a command.
```

## 创建一个模块

### 目录结构

我们先来看一下目录结构，我们首先将建立一个greetings的Module，其中包含greetings.go文件。

```go
test_go_mod
├── greetings
│   ├── go.mod
│   └── greetings.go
```

首先我们在test_go_mod下建立greetings目录

```go
mkdir -p $HOME/test_go_mod

cd $HOME/test_go_mod
mkdir -p greetings
```

### 创建greetings Module

我们来初始化Module的信息，命令执行后将生成go.mod文件

```bash
cd greetings
go mod init example.com/greetings
```

命令行中返回的信息如下

```bash
go: creating new go.mod: module example.com/greetings
```

此时如果查看go.mod，会看到如下信息，其中包含我们的module名称和go的版本

```bash
module example.com/greetings

go 1.17
```

我们来实现一下我们的greetings module，文件内容如下。代码内容较为简单，传入一个字符串后，组成我们期望的格式后进行返回

```bash
package greetings

import "fmt"

// Hello returns a greeting for the named person.
func Hello(name string) string {
    // Return a greeting that embeds the name in a message.
    message := fmt.Sprintf("Hi, %v. Welcome!", name)
    return message
}
```

到此为止，我们的greetings的module就建立好了

## 使用模块

### 目录结构

刚刚我们建立了一个新的greetings模块，接下来我们需要新建一个新的模块，并且使用刚刚建立的模块，目录结构如下

```bash
test_go_mod
├── greetings
│   ├── go.mod
│   └── greetings.go
└── hello
    ├── go.mod
    └── hello.go
```

### 创建hello Module

我们仍然采用刚刚的步骤

```bash
cd $HOME/test_go_mod
mkdir -p hello
```

初始化hello Module，生成的go.mod文件内容与刚刚是一致的，这里不再赘述

```bash
cd hello
go mod init example.com/hello
```

我们来实现hello.go，代码很简单，引用我们刚刚创建好的greetings Module，调用Hello方法。

```go
package main

import (
    "fmt"
    
    "example.com/greetings"
)

func main() {
    // Get a greeting message and print it.
    message := greetings.Hello("Gladys")
    fmt.Println(message)
}
```

### 代码执行

可以看到我们在import中引用了我们刚刚建立的greetings Module，那么如果此时尝试运行代码会发生什么呢？

```go
go run hello.go
```

我们发现程序并不能正确执行，而是返回

```go
hello.go:6:5: no required module provides package example.com/greetings; to add it:
	go get example.com/greetings
```

在执行时，Go发现并没有example.com/greetings这个包，所以建议你使用get命令去添加，我们尝试执行一下

```go
go get example.com/greetings
```

得到如下返回信息

```go
go get: module example.com/greetings: reading https://goproxy.cn/example.com/greetings/@v/list: 404 Not Found
	server response: not found: example.com/greetings@latest: unrecognized import path "example.com/greetings": reading https://example.com/greetings?go-get=1: 404 Not Found
```

我们看到get命令通过接口直接访问Module的仓库尝试查找，这里由于我们设置了代理，所以地址为goproxy.cn。由于是自定义的库，所以肯定无法查找到，我们来尝试修复该问题。

### 修正Module路径

此时我们需要将greetings Module路径指向本地目录，这里使用go mod命令，仍然在当前路径下执行

```go
go mod edit -replace example.com/greetings=../greetings
```

如果执行成功，没有任何返回信息，此时查看go.mod文件

```go
module example.com/hello

go 1.17

replace example.com/greetings => ../greetings

# 默认生成部分
# module example.com/hello

# go 1.17
```

我们发现在go.mod中，添加了一句replace语句，也就是当代码中引用example.com/greetings Module时，路径指向../greetings目录，即我们刚刚创建好的Module目录中。
但此时仍然无法执行代码，还需要使用go mod tidy命令来让同步Module信息，这样代码中才能正确使用该包的内容。

```go
go mod tidy
```

返回如下信息

```go
go: found example.com/greetings in example.com/greetings v0.0.0-00010101000000-000000000000
```

我们再来查看go.mod，我们发现在尾部增加了一个新的require语句，后面的数字是一串伪版本号，如果正式发布的Module一般使用v1.0.0这样版本号

```go
module example.com/hello

go 1.17

replace example.com/greetings => ../greetings

require example.com/greetings v0.0.0-00010101000000-000000000000
```

### 再次执行

此时再次运行代码，可以正常得到结果了。

```go
Hi, Gladys. Welcome!
```