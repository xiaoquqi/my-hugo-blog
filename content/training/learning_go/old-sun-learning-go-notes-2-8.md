---
title: 2.8 Go语言中的for循环, break和continue
date: 2022-06-23T07:53:38+08:00
slug: "old-sun-learning-go-notes-2-8"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 11
---

## 基本语法

- 和C语言同源的语法格式，有始有终的循环，for init; condition; post { }
- 带条件的while循环，for condition { }
- 无限循环，for { }

### 有始有终的条件循环

```go
sum := 0
for i := 0; i < 10; i++ {
    sum = sum + i
}
```

> 注意：i变量在循环结束后无法使用

### 带条件的循环

```go
count := 0
for count < 10 {
    fmt.Printf("Current count = %v\n", count)
    count++
}
```

### 无限循环

由于循环不会停止，这里使用break来中断循环，后面还会详细介绍

```go
 count := 0
 for {
     fmt.Printf("current count = %v\n", count)
     count++

     if count > 10 {
         break
     }
 }
```

## 数组循环

### 使用计数器循环

类似C语言中的循环，我们可以通过计数器结合数组长度实现对数组的遍历，同时能获取数组索引，如下面例子所示

```go
package main

import "fmt"

func main() {
    myarray := []string{"a", "b", "c", "d"}

    for i := 0; i < len(myarray); i++ {
        fmt.Printf("Array index is %v, value is %v\n", i, myarray[i])
    }
}
```

### 利用range循环

利用range可以更容易的进行循环，并且range还能用于slice，channel和map的循环中

```go
package main

import "fmt"

func main() {
    myarray := []string{"a", "b", "c", "d"}

    for index, item := range myarray {
        fmt.Printf("current index is %v, value is %v\n", index, item)
    }
}
```

## Map循环

在介绍Map时，我们已经尝试用for循环对Map进行遍历，我们再来巩固一下

```go
package main

import "fmt"

func main() {
    mymap := map[int]string{1 : "a", 2 : "b", 3 : "c"}

    for key, value := range mymap {
        fmt.Printf("current key is %v, value is %v\n", key, value)
    }
}
```

如果只想获取key，则可以使用，省略value

```go
for key := range mymap {
```

或者使用_，前面介绍过_无法用于变量，像个占位符

```go
for _, value := range mymap {
```

## string的遍历

下面的示例是对string类型的遍历，除了普通的字符，对于Unicode字符切分，字符通常是8位的，UTF-8的字符最高可能是32位的

```go
package main

import "fmt"

func main() {
    mystr := "abc"
    for pos, char := range mystr {
        fmt.Printf("character '%c' starts at byte position %d\n", char, pos)
    }

    for pos, char := range "Gő!" {
        fmt.Printf("character '%c' starts at byte position %d\n", char, pos)
    }
}
```

```go
character 'G' starts at byte position 0
character 'ő' starts at byte position 1
character '!' starts at byte position 3
```

## Break和Continue

与大部分语言一致

- Break结束当前循环
- Continue开始下一次循环

```go
package main

import "fmt"

func main() {
    for i := 0; i < 10; i++ {
        if i == 3 {
            fmt.Printf("For continue at here: %d\n", i)
            continue
        }
        if i > 5 {
            fmt.Printf("For break at here: %d\n", i)
            break
        }
        fmt.Printf("Current for count: %d\n", i)
    }

    fmt.Println("For loop end here")
}
```

- 输出结果

```go
Current for count: 0
Current for count: 1
Current for count: 2
For continue at here: 3
Current for count: 4
Current for count: 5
For break at here: 6
For loop end here
```

### 不推荐方式

- Go中也支持Lable方式，类似Goto，一般不使用

```go
J:  for j := 0; j < 5; j++ {
             for i := 0; i < 10; i++ {
                 if i > 5 {
                     break J
                 }
                 fmt.Println(i)
             }
         }
```