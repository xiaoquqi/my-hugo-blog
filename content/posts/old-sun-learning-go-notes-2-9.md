---
title: 2.9 Go语言中的Switch 
date: 2022-06-23T07:53:40+08:00
slug: "old-sun-learning-go-notes-2-9"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本语法

在讲述if-else时已经提到，如果有多个判断条件，Go语言中提供了Switch-Case的方式。如果switch后面不带条件相当于switch true

```go
// Convert hexadecimal character to an int value
 switch {
 case '0' <= c && c <= '9':
     return c - '0'
 case 'a' <= c && c <= 'f':
     return c - 'a' + 10
 case 'A' <= c && c <= 'F':
     return c - 'A' + 10
 }
 return 0
```

## fallthrough使用方法

默认情况下，case满足执行后会进行break，后面case即使满足条件也不再循环，如果想继续执行，则需要添加fallthrough，

```go
package main

import "fmt"

func main() {
    i := 3
    switch i {
    case i > 0:
        fmt.Println("condition 1 triggered")
        fallthrough
    case i > 2:
        fmt.Println("condition 2 triggered")
        fallthrough
    default:
        fmt.Println("Default triggered")
    }
}

```

此时所有的case都会被执行

```go
condition 1 triggered
condition 2 triggered
Default triggered
```

## 多条件匹配

如果同一个条件满足，也可以这样罗列到同一条件，相当于或条件

```go
switch i {
    case 0, 1:
        f()
    default:
        g()
}
```

## 判断接口(interface)类型

### 空接口

后面我们会讲到接口，通过switch可以对type进行判断，获取接口的真实类型。

```go
package main
  
import "fmt"
  
func main() {
    var value interface{}
    switch q:= value.(type) {
       case bool:
       fmt.Println("value is of boolean type")
       case float64:
       fmt.Println("value is of float64 type")
       case int:
       fmt.Println("value is of int type")
       default:
       fmt.Printf("value is of type: %T", q)
   }
}

```

在上面的例子中，我们定义了一个空接口

```go
var value interface{}
```

同时使用switch来判断类型

```go
switch q:= value.(type) {
```

由于空接口没有内容，所以类型为nil，触发了default

```go
value is of type: <nil>
```

### 获取实际类型

我们对上面的例子进行改造，同时让空接口拥有实际的值，再来看看执行的效果

```go
package main

import "fmt"

func valueType(i interface{}) {
    switch q:= i.(type) {
       case bool:
       fmt.Println("value is of boolean type")
       case float64:
       fmt.Println("value is of float64 type")
       case int:
       fmt.Println("value is of int type")
       default:
       fmt.Printf("value is of type: %T\n", q)

   }
}

func main() {
    person := make(map[string]interface{}, 0)

    person["name"] = "Alice"
    person["age"] = 21
    person["height"] = 167.64

    fmt.Printf("%+v\n", person)

    for _, value := range person {
        valueType(value)
    }
}
```

这里有几个还没有讲到的知识点：

- 函数的定义方法
- 定义了一个map，但是值的类型为空接口，意思就是可以是任何类型的值，这在接口章节还会详细讲解，所以大家看到这里不要纠结，继续往下看
- 赋值时，特意给value不同的类型, string/int/float类型

最后通过循环将变量传给valueType函数，看看程序输出什么结果

```go
map[age:21 height:167.64 name:Alice]
value is of type: string
value is of int type
value is of float64 type
```