---
title: 5.3 Go语言中构造函数与复合声明(Constructors and composite literals)
date: 2022-07-25T18:10:20+08:00
slug: "old-sun-learning-go-notes-5-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 31
---

## 构造函数

单纯使用new进行初始化无法满足初始化需求，必须需要初始化的构造函数，例如以下这个例子：

```go
func NewFile(fd int, name string) *File {
    if fd < 0 {
        return nil
    }
    f := new(File)
    f.fd = fd
    f.name = name
    f.dirinfo = nil
    f.nepipe = 0
    return f
}
```

虽然使用了new进行了初始化，但是后续的一些属性初始化较为复杂，所以使用复合声明，大幅度简化代码复杂程度。

```go
func NewFile(fd int, name string) *File {
    if fd < 0 {
        return nil
    }
    f := File{fd, name, nil, 0}
    return &f
}
```

局部变量返回的是变量地址，这个变量在函数返回后仍然有效。

## 复合声明

当然上述例子中，也可以使用复合声明方式直接进行返回。

```go
return &File{fd, name, nil, 0}
```

上述例子中，复合声明的参数必须要按照顺序，而且必须都存在。也可以这样按照任意顺序，并且省略为0值的声明。

```go
return &File{fd: fd, name: name}
```

new(File)和&File{}是一样的，但是不推荐使用new方式声明。复合声明还可以用于数组、Slices和Maps的初始化。

```go
package main

import "fmt"

func main() {
    arrayDemo := []int{1, 2, 3, 4}
    fmt.Printf("arrayDemo = %v\n", arrayDemo)

    mapDemo := map[string]string{"one": "one", "two": "two"}
    fmt.Printf("mapDemo = %v\n", mapDemo)
    fmt.Printf("mapDemo[one] = %v\n", mapDemo["one"])

    ar := [...]string{1: "no error", 2: "invalid argument"}
    fmt.Printf("ar = %v\n", ar)
}
```

输出内容

```go
arrayDemo = [1 2 3 4]
mapDemo = map[one:one two:two]
mapDemo[one] = one
ar = [ no error invalid argument]
```