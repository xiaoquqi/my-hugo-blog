---
title: 5.5 Go语言中的类型转换
date: 2022-07-25T18:10:24+08:00
slug: "old-sun-learning-go-notes-5-5"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 33
---

## 类型转换关系
| From | b []byte | i []int | r []rune | s string | f float32/float64 | i int |
| --- | --- | --- | --- | --- | --- | --- |
| **To** |  |  |  |  |  |  |
| []byte | · |  |  | []byte(s) |  |  |
| []int |  | · |  | []int(s) |  |  |
| []rune |  |  |  | []rune(s) |  |  |
| string | string(b) | string(i) | string(r) | · |  |  |
| float32 |  |  |  |  | · | float32(i) |
| int |  |  |  |  | int(f) | · |

## 示例：类型转换测试

```go
package main

import "fmt"

func main() {
    mystring := "hello this is string,中文测试"
    byteslice := []byte(mystring)

    fmt.Printf("string to byteslice = %v\n", byteslice)

    runeslice := []rune(mystring)
    fmt.Printf("     string to rune = %v\n", runeslice)

    b := []byte{'h','e','l','l','o'}
    s := string(b)
    fmt.Printf("     byte to string = %v\n", s)

    i := []rune{20013, 25991}
    r := string(i)
    fmt.Printf("     rune to string = %v\n", r)
}
```

输出的结果如下，rune在输出的时候是按照unicode

```go
string to byteslice = [104 101 108 108 111 32 116 104 105 115 32 105 115 32 115 116 114 105 110 103 44 228 184 173 230 150 135 230 181 139 232 175 149]
     string to rune = [104 101 108 108 111 32 116 104 105 115 32 105 115 32 115 116 114 105 110 103 44 20013 25991 27979 35797]
     byte to string = hello
     rune to string = 中文
```