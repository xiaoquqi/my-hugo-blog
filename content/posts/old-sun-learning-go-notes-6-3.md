---
title: 6.3 利用Go语言接口进行Mock单元测试
date: 2022-11-23T08:25:58+08:00
slug: "old-sun-learning-go-notes-6-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

单元测试重点是对代码逻辑进行测试，也就是证明：为什么你的代码是正确的。Mock测试是单元测试中常用的一种手段，特别是对于代码运行时对环境有严重依赖的，可以在不具备相应环境的情况下运行。例如：数据库、中间件、或者第三方接口等情况。

利用接口可以很容易的构造Mock环境，方便对代码进行单元测试。

## 原有实现

在这个实现中，我们定义了一个Obj的结构体，并且定义了getData方法。这里我们假定getData是从第三方服务中获取数据并进行处理。另外我们有一个showTotal的函数用于调用结构体的方法，并且显示出来，相当于后续的程序处理。

如果我们对showTotal进行单元测试的时候，我们会发现需要构建getData的依赖环境才能进行单元测试，所以此时我们可以使用interface构建一个MockObj来伪造getData返回数据，进行不同的场景测试。

```go
package original

import "fmt"

type Obj struct {
    name string
}

// This is a real function to connect third party service, like database
func (o Obj) getData() int {
    fmt.Printf("This is [%s] environment\n", o.name)
    // if we fetch data here
    data := map[string]int{
        "total": 10,
    }

    return data["total"]
}

func showTotal(o Obj) int {
    total := o.getData()
    fmt.Printf("Total count: %v\n", total)
}

func main() {
    o := Obj{"Production"}
    showTotal(o)
}

```

## 代码改造

### 定义接口

首先我们先定义一个接口，定义接口的目的是能让我们的Mock结构体生效

```go
type objInterface interface {
    getData() int
}
```

### 改造函数

我们对showTotal的函数入参进行调整，原有入参只接收了Obj这个结构体，我们改成接收接口参数。

```go
func showTotal(o objInterface) int {
    total := o.getData()
    fmt.Printf("Total count: %v\n", total)
    return total
}
```

### Mock结构体

我们新建一个main_test.go的单元测试文件，我们新增一个Mock结构体及Mock的getData方法。

```go
type MockObj struct {}

func (o MockObj) getData() int {
    fmt.Printf("This is a mock function using interface\n")
    return 100
}
```

### Mock测试

我们新增一个测试用例，如果showTotal能够返回100，则测试成功，否则抛出异常。在测试用例中，我们将定义好的MockObj传给了showTotal，此时showTotal调用了我们定义的Mock方法，所以返回100，单元测试构建成功。

```go
func TestShowTotal(t *testing.T) {
    mo := MockObj{}
    total := showTotal(mo)
    if total != 100 {
        t.Log("Mock show total failed!")
        t.Fail()
    }
}
```

## 完整代码

### 主体函数

```go
package main

import "fmt"

type objInterface interface {
    getData() int
}

type Obj struct {
    name string
}

// This is a real function to connect third party service, like database
func (o Obj) getData() int {
    fmt.Printf("This is [%s] environment\n", o.name)
    // if we fetch data here
    data := map[string]int{
        "total": 10,
    }

    return data["total"]
}

func showTotal(o objInterface) int {
    total := o.getData()
    fmt.Printf("Total count: %v\n", total)
    return total
}

func main() {
    o := Obj{"Production"}
    showTotal(o)
}
```

### 测试用例

```go
package main

import (
    "fmt"
    "testing"
)

type MockObj struct {}

func (o MockObj) getData() int {
    fmt.Printf("This is a mock function using interface\n")
    return 100
}

func TestShowTotal(t *testing.T) {
    mo := MockObj{}
    total := showTotal(mo)
    if total != 100 {
        t.Log("Mock show total failed!")
        t.Fail()
    }
}
```

### 运行及结果

运行go test之前，记得要设定环境变量

```go
export GO111MODULE=off
go test
```

返回如下，我们很清楚的看到了测试中调用了我们的Mock方法

```go
This is a mock function using interface
Total count: 100
PASS
ok  	_/root/workspace/go/test_interface_unittest	0.003s
```