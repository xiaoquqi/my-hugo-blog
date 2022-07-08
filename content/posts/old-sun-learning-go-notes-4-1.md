---
title: 4.1 Go语言中包(Packages)基础知识
date: 2022-07-08T14:16:04+08:00
slug: "old-sun-learning-go-notes-4-1"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本概念

- 包是函数和数据的集合
- 使用package关键字进行定义
- 文件名可以不完全与包名相同
- 包名通常使用小写字母定义
- 包里可以有很多文件，但是他们共享同一个包名
- 通过函数名称的大小写区分私有还是可被外部使用的
   - 大写，可以被外部使用(exported)
   - 小写，私有函数(private)
   - 请注意，“大写”一词不仅限于 US-ASCII——它还扩展到所有双字字母（拉丁文、希腊文、西里尔文、亚美尼亚文和科普特文）

## 示例：公有和私有函数及Go中包管理方式

### 代码及结构

先看一下目录结构，注意这里的src名称是必须的，go在设置了GOPATH后，默认会添加src去寻找package，暂未查询是否有方法不按照src查询

```go
├── main.go
└── src
    └── myfunc
        └── myfunc.go
```

```go
package main

import "myfunc"

func main() {
   myfunc.MyPublicFunc()

   // NOTE(Ray): Can not call private function
   //myfunc.myPrivateFunc()
}
```

根据上面的描述，Go语言中通过包中函数的名称来区分公共函数和私有函数，我们在main函数中是无法调用myPrivateFunc的

```go
package myfunc

import "fmt"

func MyPublicFunc() {
    fmt.Println("Use my public function.")
}

// NOTE(Ray): This is private function, can not be used outside
func myPrivateFunc() {
    fmt.Println("Use my public function.")
}
```

此时如果执行通过go run方式执行，会看到如下的提示信息，这与大部分语言对于包管理方式相关，所以我们通过两种不同的方法来让代码执行起来

```go
main.go:3:8: package myfunc is not in GOROOT (/usr/local/go/src/myfunc)
```

### 通过设置GOPATH执行

```go
go env
```

返回如下，这里面对我们后续执行有影响的两个参数GO111MODULE和GOPATH

- GO111MODULE是在Go 1.11引入的Go模块，需要搭配go.mod使用
- GOPATH则是Go语言中旧的依赖管理模式，该模式下无法对依赖的版本进行控制

```go
GO111MODULE="on"
GOARCH="amd64"
GOBIN=""
GOCACHE="/root/.cache/go-build"
GOENV="/root/.config/go/env"
GOEXE=""
GOEXPERIMENT=""
GOFLAGS=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOINSECURE=""
GOMODCACHE="/root/workspace/go/test_package/pkg/mod"
GONOPROXY=""
GONOSUMDB=""
GOOS="linux"
GOPATH=""
GOPRIVATE=""
GOPROXY="https://goproxy.cn"
GOROOT="/usr/local/go"
GOSUMDB="sum.golang.org"
GOTMPDIR=""
GOTOOLDIR="/usr/local/go/pkg/tool/linux_amd64"
GOVCS=""
GOVERSION="go1.17.6"
GCCGO="gccgo"
AR="ar"
CC="gcc"
CXX="g++"
CGO_ENABLED="1"
GOMOD=""
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build3817126445=/tmp/go-build -gno-record-gcc-switches"
```

如果要使用gopath模式引用包，则需要关闭mod模式

```go
export GO111MODULE=off
```

设置GOPATH为当前路径，即main.go所在的路径

```go
go env -w GOPATH=$(pwd)
```

此时再查看go env时，GOPATH已经发生改变

```go
GOPATH="/root/workspace/go/test_package"
```

我们再次尝试执行代码

```go
go run main.go
```

可以看到public函数被调用

```go
Use my public function.
```