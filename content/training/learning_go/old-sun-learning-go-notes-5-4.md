---
title: 5.4 Go语言中自定义类型与结构体(Struct)
date: 2022-07-25T18:10:22+08:00
slug: "old-sun-learning-go-notes-5-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 32
---

## Go是面向对象的语言吗

在很多文章中都提到，Go语言中的struct某种意义就是对应其他语言中的class，就该问题特意阅读了Go语言官网的常见问题，有这样的描述

> Is Go an object-oriented language?
>
> Yes and no. Although Go has types and methods and allows an object-oriented style of programming, there is no type hierarchy. The concept of “interface” in Go provides a different approach that we believe is easy to use and in some ways more general. There are also ways to embed types in other types to provide something analogous—but not identical—to subclassing. Moreover, methods in Go are more general than in C++ or Java: they can be defined for any sort of data, even built-in types such as plain, “unboxed” integers. They are not restricted to structs (classes).
>
> Also, the lack of a type hierarchy makes “objects” in Go feel much more lightweight than in languages such as C++ or Java.

但是又舍弃了很多类在继承的特性，让Go语言变得更轻。

## 类型定义

使用type字段进行自定义类型的定义，基本结构为type <Your Type> <Go Type>。
下面这个例子是一个利用结构体定义的新类型。

```go
package main

import "fmt"

type NameAge struct {
	name string // Both non exported fields.
	age  int
}

func main() {
	a := new(NameAge)
	a.name = "Pete"
	a.age = 42
	fmt.Printf("struct values = %v\n", a)
	fmt.Printf("struct full = %+v\n", a)
	fmt.Printf("struct a.name = %s\n", a.name)
}
```

输出结果为，如果使用%v只输出值而不输出字段，使用%+v，可以同时输出字段，如果访问其中的值，则使用.<field name>的方式

```go
struct values = &{Peter 42}
struct full = &{name:Peter age:42}
struct a.name = Peter
```

## 结构体匿名字段

结构体匿名字段其实是一种类似继承的手段，我们来分析如下例子：

```go
package main

import "fmt"

type Group struct {
    name string
}

type User struct {
    name string
    age int
    Group // anonymous field, include all group fields
}

func main() {
    user := User{"Tom", 23, Group{"GroupA"}}

    fmt.Printf("user = %v\n", user)
    fmt.Printf("user with fields = %+v\n", user)
    fmt.Printf("user name = %v\n", user.name)
    fmt.Printf("user group name = %v\n", user.Group.name)
}
```

我们定义了两个结构体，一个是组，一个是用户。其中User的结构体中引用了Group，默认也就是具备了所有Group的字段。在初始化时，指定字段后，得到这样的输出结果：

```go
user = {Tom 23 {GroupA}}
user with fields = {name:Tom age:23 Group:{name:GroupA}}
user name = Tom
user group name = GroupA
```

## 结构体与方法

使用结构体定义函数的Reciver，需要注意的一点，Reciever默认传值，而非引用传递，也可以传输指针。

```go
package main

import "fmt"

type Rect struct {
    width, height float64
}

func (r Rect) AreaValuePass() float64 {
    fmt.Println("Area Value Pass")
    fmt.Printf("r = %v\n", r)
    fmt.Printf("r type = %T\n", r)
    return r.width * r.height
}

func (r *Rect) AreaPointerPass() float64 {
    fmt.Println("Area Pointer Pass")
    fmt.Printf("r = %v\n", r)
    fmt.Printf("r type = %T\n", r)
    return r.width * r.height
}

func main() {
    rect := Rect{2, 4}
    resultValue := rect.AreaValuePass()
    fmt.Printf("Rect result = %v\n", resultValue)

    fmt.Println("-----------------------")

    resultPointer := rect.AreaPointerPass()
    fmt.Printf("Rect result = %v\n", resultPointer)
}
```

根据输出结果可以发现，Reciever是一个指针时，无须使用&r去获取值，直接使用r.width获取相应字段的值，行为与默认值传参相同。

```go
Area Value Pass
r = {2 4}
r type = main.Rect
Rect result = 8
-----------------------
Area Pointer Pass
r = &{2 4}
r type = *main.Rect
Rect result = 8
```

## 结构体重定义

严格意义上来说，Go中并没有继承，但是可以利用结构体实现类似继承的效果。我们在同一个程序中定义了两个重名的函数SayHi，但是Reciever分别使用了不同的结构体进行定义，程序可以正常编译和执行。

```go
package main

import "fmt"

type Base struct {
    name string
    age  int
}

type ExtendBase struct {
    Base
    birth string
}

func (p *Base) SayHi() {
    fmt.Printf("struct base = %v\n", p)
    fmt.Printf("struct base = %+v\n", p)
}

func (p *ExtendBase) SayHi() {
    fmt.Printf("struct extend = %v\n", p)
    fmt.Printf("struct extend = %+v\n", p)
}

func main() {
    baseStruct := Base{"Tom", 34}
    baseStruct.SayHi()

    extendStruct := ExtendBase{Base{"Mary", 18}, "1982-04-30"}
    extendStruct.SayHi()
}
```

输出结果如下所示

```go
struct base = &{Tom 34}
struct base = &{name:Tom age:34}
struct extend = &{{Mary 18} 1982-04-30}
struct extend = &{Base:{name:Mary age:18} birth:1982-04-30}
```