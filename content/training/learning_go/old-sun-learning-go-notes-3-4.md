---
title: 3.4 Go语言中变量作用域(Scope)
date: 2022-06-26T22:54:06+08:00
slug: "old-sun-learning-go-notes-3-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 17
---

## 知识点

- 函数外的变量定义都是全局的
- 函数内定义的变量是局部的
- 如果全局变量和局部变量重名，则重名变量局部生效，当函数返回后，值仍然为全局变量的值

```go
package main

import "fmt"

var a int

func main() {
    a = 5
    fmt.Printf("Variable a in main function is: %d\n", a)
    f()
}

func f() {
    a := 6
    fmt.Printf("Variable a in f function is: %d\n", a)
    g()
}

func g() {
    fmt.Printf("Variable a in g function is: %d\n", a)
}
```

在上面的示例中：

- 最外侧a为全局变量，所以在main函数中首先输出的变量为5
- 紧接着调用f()，在f()中，由于重新定义了变量a并赋值为6，现在a虽然与全局变量重名，但是实际上已经成为局部变量，所以输出的值为6
- 而在最终调用的g()中，由于直接输出a，相当于也是将全局变量a进行输出，所以值为5

```go
Variable a in main function is: 5
Variable a in f function is: 6
Variable a in g function is: 5
```