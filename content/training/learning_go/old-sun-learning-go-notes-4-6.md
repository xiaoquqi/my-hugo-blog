---
title: 4.6 使用第三方Go Modules
date: 2022-07-16T09:57:00+08:00
slug: "old-sun-learning-go-notes-4-6"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 27
---

在实际开发中，往往通过使用每一种开发语言丰富的库可以避免重复制造轮子，同时缩短项目开发周期。在Go语言中也可以引用官方或者第三方的Modules，提高开发效率。

## 官方仓库

类似其他语言，Go中也有一个第三方的仓库，官方的地址是：[https://pkg.go.dev/](https://pkg.go.dev/)

![2022-07-16-10-01-34](/images/2022-07-16-10-01-34.png)

我们来搜索一下著名的WEB框架gin

![2022-07-16-10-01-54](/images/2022-07-16-10-01-54.png)

点击查看信息

![2022-07-16-10-02-08](/images/2022-07-16-10-02-08.png)

下方有详细的方法说明

![2022-07-16-10-02-21](/images/2022-07-16-10-02-21.png)

## 利用Gin实现一个简单的WEB服务

### 初始化模块

接下来我们利用Gin模块构建一个简单的Web服务，进一步掌握Go Modules使用方法，根据上述的方法，我们来建立一个新的模块。

```go
mkdir -p test_gin_samples
cd test_gin_samples
go mod init example.com/myweb
```

初始化完成后，我们得到我们的go.mod文件。

```go
module example.com/myweb

go 1.17
```

### 添加gin依赖

如果需要在仓库中使用某个模块，只需要执行go get命令，就会自动在go.mod文件中添加响应的依赖。正如我们上面提到的，该命令执行完成后，所以的依赖包会统一下载到GOPATH中即$HOME/go

```go
go get github.com/gin-gonic/gin
```

我们先来看一下go.mod的变化

```go
module example.com/myweb

go 1.17

require (
	github.com/gin-contrib/sse v0.1.0 // indirect
	github.com/gin-gonic/gin v1.8.1 // indirect
	github.com/go-playground/locales v0.14.0 // indirect
	github.com/go-playground/universal-translator v0.18.0 // indirect
	github.com/go-playground/validator/v10 v10.10.0 // indirect
	github.com/goccy/go-json v0.9.7 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/leodido/go-urn v1.2.1 // indirect
	github.com/mattn/go-isatty v0.0.14 // indirect
	github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421 // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/pelletier/go-toml/v2 v2.0.1 // indirect
	github.com/ugorji/go/codec v1.2.7 // indirect
	golang.org/x/crypto v0.0.0-20210711020723-a769d52b0f97 // indirect
	golang.org/x/net v0.0.0-20210226172049-e18ecbb05110 // indirect
	golang.org/x/sys v0.0.0-20210806184541-e5e7981a1069 // indirect
	golang.org/x/text v0.3.6 // indirect
	google.golang.org/protobuf v1.28.0 // indirect
	gopkg.in/yaml.v2 v2.4.0 // indirect
)
```

我们发现go.mod中有以下变化：

- go.mod中除了添加了gin自身依赖，还添加了依赖的依赖
- 依赖中包含了版本号
- indirect表示代码中并未引用该模块，后续会使用go mod tidy进行自动更新
- 除了生成go.mod，同时生成的还有go.sum文件，用于记录依赖和哈希值。

```go
......
github.com/gin-contrib/sse v0.1.0 h1:Y/yl/+YNO8GZSjAhjMsSuLt29uWRFHdHYUb5lYOV9qE=
github.com/gin-contrib/sse v0.1.0/go.mod h1:RHrZQHXnP2xjPF+u1gW/2HnVO7nvIa9PG3Gm+fLHvGI=
github.com/gin-gonic/gin v1.8.1 h1:4+fr/el88TOO3ewCmQr8cx/CtZ/umlIRIs5M4NTNjf8=
github.com/gin-gonic/gin v1.8.1/go.mod h1:ji8BvRH1azfM+SYow9zQ6SZMvR8qOMZHmsCuWR9tTTk=
github.com/go-playground/assert/v2 v2.0.1/go.mod h1:VDjEfimB/XKnb+ZQfWdccd7VUvScMdVu0Titje2rxJ4=
github.com/go-playground/locales v0.14.0 h1:u50s323jtVGugKlcYeyzC0etD1HifMjqmJqb8WugfUU=
github.com/go-playground/locales v0.14.0/go.mod h1:sawfccIbzZTqEDETgFXqTho0QybSa7l++s0DH+LDiLs=
......
```

### 代码实现

根据代码样例，我们实现了一个简单的Web服务，端口为18080，如果访问http://<your_ip>:18080/ping，会得到{"message": "pong"}

```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"message": "pong",
		})
	})
    r.Run(":18080") // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
```

### 清理未使用的依赖

我们使用go mod tidy对go.mod进行清理。

```go
go mod tidy
```

此时我们发现go.mod中有一个显示的变化，gin依赖从刚刚的require被独立出来，并且后面的注释indirect不见了

```go
module example.com/myweb

go 1.17

require github.com/gin-gonic/gin v1.8.1

require (
	github.com/gin-contrib/sse v0.1.0 // indirect
	github.com/go-playground/locales v0.14.0 // indirect
	github.com/go-playground/universal-translator v0.18.0 // indirect
	github.com/go-playground/validator/v10 v10.10.0 // indirect
	github.com/goccy/go-json v0.9.7 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/leodido/go-urn v1.2.1 // indirect
	github.com/mattn/go-isatty v0.0.14 // indirect
	github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421 // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/pelletier/go-toml/v2 v2.0.1 // indirect
	github.com/ugorji/go/codec v1.2.7 // indirect
	golang.org/x/crypto v0.0.0-20210711020723-a769d52b0f97 // indirect
	golang.org/x/net v0.0.0-20210226172049-e18ecbb05110 // indirect
	golang.org/x/sys v0.0.0-20210806184541-e5e7981a1069 // indirect
	golang.org/x/text v0.3.6 // indirect
	google.golang.org/protobuf v1.28.0 // indirect
	gopkg.in/yaml.v2 v2.4.0 // indirect
)
```

## 离线构建

有很多种情况需要使用离线构建，比如加速构建速度或无网情况下，所以我们要解决依赖安装的问题。当然我们可以搭建一个本地的私有Go Modules仓库，但是略微复杂，最简单的思路是通过go mod vendor命令，命令执行后，go会自动更具go.mod中的内容将依赖下载到当前项目中的vendors目录中，一起构建即可。例如在上面例子的目录执行：

```go
go mod vendor
```

执行完成后，在项目根目录生成vendor，目录结构为

```go
vendor
├── github.com
│   ├── gin-contrib
│   ├── gin-gonic
│   ├── goccy
│   ├── go-playground
│   ├── json-iterator
│   ├── leodido
│   ├── mattn
│   ├── modern-go
│   ├── pelletier
│   └── ugorji
├── golang.org
│   └── x
├── google.golang.org
│   └── protobuf
├── gopkg.in
│   └── yaml.v2
└── modules.txt
```