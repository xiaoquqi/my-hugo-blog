---
title: 2.6 Go语言中的Map
date: 2022-06-18T21:24:17+08:00
slug: "old-sun-learning-go-notes-2-6"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本语法

Map属于引用型(References)，指向Hash Table，类似Python中的dict

### 基本定义

```go
var mymap map[string]int
```

这样定义出来的map实际上是一个nil，这里不包含任何元素你也不能赋值，如果赋值的话会提示assignment to entry in nil map，所以需要定义并初始化。

```go
var mymap map[string]int{key1: value1, ..., keyN: valueN}
```

来看以下的示例

```go
package main

import "fmt"

func main() {
    monthdays := map[string]int{
        "Jan": 31, "Feb": 28, "Mar": 31,
        "Apr": 30, "May": 31, "Jun": 30,
        "Jul": 31, "Aug": 31, "Sep": 30,
        "Oct": 31, "Nov": 30, "Dec": 31,
    }
    fmt.Printf("monthdays = %v\n", monthdays)
}
```

注意：maps定义最后的逗号是必须的，如果没有的话，编译会报语法错误

```go
./test_maps.go:10:40: syntax error: unexpected newline, expecting comma or }
```

### 使用make定义

在不确定初始值的情况下，可以使用make进行声明，之后就可以进行赋值操作

```go
mymap := make(map[Key_Type]Value_Type, initial_Capacity)
mymap := make(map[Key_Type]Value_Type)
```

来看以下示例，和上面的基本定义做一个对比。

```go
package main

import "fmt"

func main() {
    var mymap map[int]string
    // panic: assignment to entry in nil map
    //mymap[1] = "one"
    fmt.Printf("var define map is %v\n", mymap)

    mymakemap := make(map[int]string)
    mymakemap[1] = "one"
    fmt.Printf("var define map is %v\n", mymakemap)
}
```

正如上面提到的，通过基本定义方式定义的map是无法赋值的，而通过make定义后返回的是一个初始化的map，所以可以被赋值。

## 常用操作

### 读取Map值

这里使用了for和range读取哈希值，与其他语言中的使用方法类似

```go
package main

import "fmt"

func main() {
    monthdays := map[string]int{
        "Jan": 31, "Feb": 28, "Mar": 31,
        "Apr": 30, "May": 31, "Jun": 30,
        "Jul": 31, "Aug": 31, "Sep": 30,
        "Oct": 31, "Nov": 30, "Dec": 31,
    }

    year := 0
    // We ignore the key value, so use _ here, and we can not use _
    // as variable or you will get 'cannot use _ as value'
    for _, days := range monthdays {
        year += days
    }
    fmt.Printf("year = %d\n", year)

    // Test show loop values
    for month, days := range monthdays {
        fmt.Printf("current line key = %s, value = %d\n", month, days)
    }
}
```

输出结果

```go
year = 365
current line key = Jan, value = 31
current line key = Apr, value = 30
current line key = Oct, value = 31
current line key = Nov, value = 30
current line key = Dec, value = 31
current line key = Feb, value = 28
current line key = Mar, value = 31
current line key = May, value = 31
current line key = Jun, value = 30
current line key = Jul, value = 31
current line key = Aug, value = 31
current line key = Sep, value = 30
```

### CURD操作

采用直接赋值的方式就可以对Map进行值更新，而判断Map中是否包含key时，只需要增加一个变量ok，通过该变量的

```go
package main

import "fmt"

func main() {
    monthdays := map[string]int{
        "Jan": 31, "Feb": 28, "Mar": 31,
        "Apr": 30, "May": 31, "Jun": 30,
        "Jul": 31, "Aug": 31, "Sep": 30,
        "Oct": 31, "Nov": 30, "Dec": 31,
    }

    // Add a new key in maps
    monthdays["newmonth"] = 100
    fmt.Printf("monthdays = %v\n", monthdays)

    // Update current key value
    monthdays["newmonth"] = 101
    fmt.Printf("monthdays = %v\n", monthdays)

    // Test key exsits
    //  It’s more Go like to name present “ok”, and use: v, ok := monthdays["Jan"].
    // In Go we call this the “comma ok” form.
    value, ok := monthdays["newmonth"]
    fmt.Printf("value = %d, present = %t\n", value, ok)

    // Test key not exists
    // NOTE(Ray): As we already define variable ok above, if the key is used again
    // we will get error: "no new variables on left side of :="
    // We can use new variable or just use = instead :=
    value, ok = monthdays["none"]
    fmt.Printf("value = %d, present = %t\n", value, ok)

    // Delete key
    delete(monthdays, "newmonth")
    fmt.Printf("monthdays = %v\n", monthdays)
}
```

输出结果

```go
monthdays = map[Apr:30 Aug:31 Dec:31 Feb:28 Jan:31 Jul:31 Jun:30 Mar:31 May:31 Nov:30 Oct:31 Sep:30 newmonth:100]
monthdays = map[Apr:30 Aug:31 Dec:31 Feb:28 Jan:31 Jul:31 Jun:30 Mar:31 May:31 Nov:30 Oct:31 Sep:30 newmonth:101]
value = 101, present = true
value = 0, present = false
monthdays = map[Apr:30 Aug:31 Dec:31 Feb:28 Jan:31 Jul:31 Jun:30 Mar:31 May:31 Nov:30 Oct:31 Sep:30]
```