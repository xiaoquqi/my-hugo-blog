---
title: 6.5 Go语言中接口和指针
date: 2022-11-23T08:26:02+08:00
slug: "old-sun-learning-go-notes-6-5"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

我们知道在传递变量时，尽量使用指针方式能够节约资源，我们来看一下在接口中如何应用指针，我们直接对接口的使用样例的代码进行改造。我们首先将area()的reciver类型修改为指针，再将传递到接口中的变量变为&c1方式，就可以在接口中使用指针。

```go
// Define a new interface, contain a method define and type is float64
type shape interface {
    area() float64
}

type rect struct {
    width float64
    height float64
}

func (r *rect) area() float64 {
    return r.width * r.height
}

.....

shapes := []shape{&c1, &r1}

.....
```

完整代码如下

```go
package main

import (
    "fmt"
    "math"
)

// Define a new interface, contain a method define and type is float64
type shape interface {
    area() float64
}

type rect struct {
    width float64
    height float64
}

func (r *rect) area() float64 {
    return r.width * r.height
}

type circle struct {
    radius float64
}

func (c *circle) area() float64 {
    return math.Pi * c.radius * c.radius
}

func main() {
    var areaSum float64

    // Intial circle and rect struct type
    c1 := circle{2.5}
    r1 := rect{3, 4}

    // Previous: Save all area results into an array
    // Previous: shapeAreas := []float64{c1.area(), r1.area()}

    // Define an array with new shape interface
    shapes := []shape{&c1, &r1}

    // Previous: Sum all area together
    areaSum = 0
    // Previous: for _, area := range shapeAreas {
    // Previous:     areaSum += area
    // Previous: }

    // Implement a new loop
    for _, shape := range shapes {
        areaSum += shape.area()
    }

    fmt.Printf("Sum area = %v\n", areaSum)
}
```