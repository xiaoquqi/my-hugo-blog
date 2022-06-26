---
title: 3.1 Go语言中的函数与方法
date: 2022-06-26T22:53:58+08:00
slug: "old-sun-learning-go-notes-3-1"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Blog
draft: false
---

## 函数定义语法

与大部分语言一致，Go语言中的函数定义与其他语言基本一致

```go
func function_name(Parameter-list) {
    // function body...
}

func function_name(Parameter-list) Return-Type {
    // function body...
}

func function_name(Parameter-list) (Multiple Return-Types){
    // function body..
}
```

- func: 函数定义关键字
- function_name: 函数名称，Go语言主要使用camel-case(驼峰)命名的方式，还根据函数的性质，用首字母大小写区分作用，具体会在后面专门的章节讲解Go语言的规范
- Parameter-list: 参数列表，如果没有可以忽略
- Return-Type/Multiple Return-Types: 返回值的类型，即return返回值的类型，这里特别将三种形式进行了区分：
   - 无返回值/单一返回值/多返回值
   - 另外两种的细小的区别在于括号的使用，单一返回类型一般不再添加括号，而多返回值则需要添加括号
   - 另外为了美观，参数列表后面的括号，建议与返回类型之间有一个空格

## 函数定义示例

### 无返回值函数

```go
func HelloFunc() {
    fmt.Println("Hello, World")
}
```

### 单一返回值函数

本示例中演示了参数定义方法和返回值类型定义方法

```go
func HelloFunc(msg string) string {
    return "Hello, " + msg
}
```

### 多返回值函数

第二个返回值的类型通常用于回传错误，这样方便程序进行异常处理

```go
func HelloFunc(msg string) (string, error) {
    return "Hello, " + msg, nil
}
```

我们再来看一下完整的代码实现，主函数中调用HelloFunc时，也需要两个变量接收相应的值

```go
package main

import "fmt"

func HelloFunc(msg string) (string, error) {
    return "Hello, " + msg, nil
}

func main() {
    printString, err := HelloFunc("World")
    if err == nil {
        fmt.Println(printString)
    }
}
```

## 方法(Method)定义

Go语言中并没有类，所以在Go语言中提供了一种类似函数定义的方法定义，通过在函数名称前增加Reciever类型，实现一种类似类中方法的定义，方法可以使用Reciver的属性。我们来看一下语法：

```go
func (Reciever-Name Type) function_name(Parameter-list) (Multiple Return-Types){
    // function body..
}
```

由于大部分定义内容与上述函数定义相同，这里就不再赘述，只介绍一下新增的部分：

- Reciever-Name：类型必须是自定义类型，不能是内置的int, string等，使用的话，在编译阶段就会报错

## 方法(Method)示例

### 基本类型

我们来看一个通过基本类型实现的方法，这里使用到了一个未曾学习到的知识点——自定义类型type，后面还会详细讲解，不用在此处纠结。这句含义就是通过自定义类型mystring再次定义的变量，本质上与string同一类型。

```go
type mystring string
```

这里注意我们的函数定义，在函数名前，多了(msg mystring)的定义，而在函数体内，我们也可以直接使用msg

```go
func (msg mystring) HelloFunc() {
    str := "Hello, " + msg
    fmt.Println(str)
}
```

而在main函数中进行调用时，与上面的函数调用不同，我们直接使用调用mymsg的方法HelloFunc，实现了与上面例子类似的方法

```go
var mymsg mystring
mymsg = "World"
mymsg.HelloFunc()
```

完整代码如下所示

```go
package main

import "fmt"

type mystring string

func (msg mystring) HelloFunc() {
    str := "Hello, " + msg
    fmt.Println(str)
}

func main() {
    var mymsg mystring
    mymsg = "World"
    mymsg.HelloFunc()
}
```

### 结构体类型

其实从各个项目的源代码来看，方法还是更多的与结构体(struct)和接口(interface)一起使用，这些都会在后面进行详细讲解，这里只需要了解即可。这里介绍一个简单的例子，我们来计算长方形的面积。

- 定义了一个结构体rect，其中包含长和宽两个属性
- 计算面积的方法area()，Reciver定义为结构体类型，这样方法体内，就可以使用长和宽计算面积
- 主函数中，定义了一个结构体，并且初始化长和宽分别为3和4
- 调用自定义结构体的r.area()完成面积计算

```go
package main

import "fmt"

type rect struct {
    width float64
    height float64
}

func (r rect) area() float64 {
    return r.width * r.height
}

func main() {
    r := rect{3, 4}
    rectArea := r.area()
    fmt.Printf("Rect area is %v\n", rectArea)
}
```