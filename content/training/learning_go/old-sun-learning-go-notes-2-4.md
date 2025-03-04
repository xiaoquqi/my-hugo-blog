---
title: 2.4 Go语言中的数组(Array)
date: 2022-06-18T21:24:04+08:00
slug: "old-sun-learning-go-notes-2-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 7
---

## 基本语法

数组是各种语言必备的一种数据类型，Go语言也不例外，如下面的示例，定义的方法主要指明长度和类型。不同于Python中的List类型，可以随意存放各种类型的数据，Go语言中的数组一旦确定类型，只能存放本类型的数据。

```go
var array_name [length]Type
array_name[index] = variable

// 初始化值
var array_name [length]Type{item1, item2, item3, ...itemN}
```

## 数组声明示例

```go
var arr [10]int
arr[0] = 42
fmt.Printf("The first element is %d\n", arr[0])
```

## 数组初始化示例

```go
// 显示定义
a := [3]int{1, 2, 3}

// 自动计算数组长度
a := [...]int{1, 2, 3}
```

### 关于三个点(...)Ellipsis的说明

我们经常在Go中看到这种方式，首先三个点的英文是Ellipsis，翻译成中文叫做“省略”，可能各位看到这个词就比较好理解三个点的作用了。在不同的位置上有不同的作用，比如在上述数组的定义中，省略了数组长度的声明，而是根据数组初始化值来决定。在函数定义中，我们还会看到类似的使用方法，我们再进行详细的说明。

## 多维数组初始化示例

```go
a := [2][2]int{ {1, 2}, {3, 4} }
```

## 数组比较

直接使用等号就可以对数组进行比较，见下面的例子

```go
package main

import "fmt"

func main() {
    // Arrays
    arr1:= [3]int{9,7,6}
    arr2:= [...]int{9,7,6}
    arr3:= [3]int{9,5,3}

    // Comparing arrays using == operator
    fmt.Println(arr1==arr2) // true
    fmt.Println(arr2==arr3) // false
    fmt.Println(arr1==arr3) // false

    // This will give and error because the
    // type of arr1 and arr4 is a mismatch
    //arr4:= [4]int{9,7,6}
    //fmt.Println(arr1==arr4)
}
```

注意在注释区域，如果两个数组长度不一样，如果进行比较则会得到这样的错误

```go
./test_array_compare.go:19:21: invalid operation: arr1 == arr4 (mismatched types [3]int and [4]int)
```

## 知识点

- 如果将数组赋值给另外一个变量，会拷贝所有元素
- 如果将array传给函数，也是拷贝元素，并非指向，这一点与Python不同
- 为了控制篇幅，缩短大家的阅读时间，关于数组的遍历方法，我们会在控制结构中For进行讲解

## 参考文档

- [https://www.geeksforgeeks.org/arrays-in-go/?ref=lbp](https://www.geeksforgeeks.org/arrays-in-go/?ref=lbp)
- [https://www.geeksforgeeks.org/how-to-use-ellipsis-in-golang/](https://www.geeksforgeeks.org/how-to-use-ellipsis-in-golang/)
- [http://liupzmin.com/2019/07/31/golang/golang-three-dots/](http://liupzmin.com/2019/07/31/golang/golang-three-dots/)