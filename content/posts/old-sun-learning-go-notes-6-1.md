---
title: 6.1 Go语言中接口使用样例
date: 2022-11-23T08:25:53+08:00
slug: "old-sun-learning-go-notes-6-1"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

正如前文提到，Go语言并没有类的定义，接口可以说Go语言最接近于类的实现方式，但是更轻量。对于接口的学习，如果从原理层面理解学习起来比较慢，所以建议先从代码使用维度进行理解，最终回归到原理层面加深理解。

## 需求与分析

假设我们有一组图形，需要计算每个图形的面积，并计算他们的面积之和。那么最简单的方法就是分别计算他们的面积，并进行相加，我们来尝试实现一下。

## 不使用接口的实现

在这个代码实现中，我们需要将两种不同形状，矩形(rect)和圆形(circle)的面积求和，因此我们定义了如下内容：

- 两个结构体，矩形是长和宽，圆形是半径
- 分别实现了两个求面积的方法area()，矩形的面积等于长乘以宽，而圆形面积则是半径的平方乘以Pi
- 在求和部分，我们直接定义了一个float64的数组，将面积直接存入该数组中
- 通过循环进行求和

虽然上述方式能够满足我们的需求，但是如果我们需要增加一个计算周长的方法时，我们的代码会变得非常冗余并且可读性变差，因此我们用接口尝试来改造我们的代码。

```go
package main

import (
    "fmt"
    "math"
)

type rect struct {
    width float64
    height float64
}

func (r rect) area() float64 {
    return r.width * r.height
}

type circle struct {
    radius float64
}

func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}

func main() {
    var areaSum float64
    
    // Intial circle and rect struct type
    c1 := circle{2.5}
    r1 := rect{3, 4}
    
    // Save all area results into an array
    shapeAreas := []float64{c1.area(), r1.area()}
    
    // Sum all area together
    areaSum = 0
    for _, area := range shapeAreas {
        areaSum += area
    }
    
    fmt.Printf("Sum area = %v\n", areaSum)
}
```

## 使用接口的实现

相较于上述代码，我们做了如下优化：

- 定义了一个新的interface shape，包含一个area()方法，即实现了area()的struct，就实现了shape接口
- 在结构体定义，area()计算部分我们并没有修改
- 在主函数中，我们重新定义了一个类型为shape interface的数组，该数组中无须再计算area()，只需要将两个不通类型存放在该数组中
- 在循环过程中，我们直接调用每个shape interface中的area()方法，即可完成面积求和

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

func (r rect) area() float64 {
    return r.width * r.height
}

type circle struct {
    radius float64
}

func (c circle) area() float64 {
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
    shapes := []shape{c1, r1}
    
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

## 接口作为函数参数

进一步优化代码，我们将接口作为参数，在主函数中调用时，只需要传入相应类型就会自动根据类型调用相应的计算面积的方法。

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

// NOTE: 接口类型为rect
func (r rect) area() float64 {
    return r.width * r.height
}

type circle struct {
    radius float64
}

// NOTE: 接口类型为circle
func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}

func getArea(s shape) float64 {
    return s.area()
}

func main() {
    var areaSum float64

    // Intial circle and rect struct type
    c1 := circle{2.5}
    r1 := rect{3, 4}

    // Previous: Save all area results into an array
    // Previous: shapeAreas := []float64{c1.area(), r1.area()}

    // Define an array with new shape interface
    shapes := []shape{c1, r1}

    // Previous: Sum all area together
    areaSum = 0
    // Previous: for _, area := range shapeAreas {
    // Previous:     areaSum += area
    // Previous: }

    // Implement a new loop
    for _, shape := range shapes {
        areaSum += getArea(shape)
    }

    fmt.Printf("Sum area = %v\n", areaSum)
}
```