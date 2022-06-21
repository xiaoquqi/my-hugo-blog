---
title: 2.5 Go语言中的切片(Slice)
date: 2022-06-18T21:24:08+08:00
slug: "old-sun-learning-go-notes-2-5"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本概念

-  与数组很相似，但是Slices长度是可变的，操作方式与Python的list类型相似，例如新增一个元素。 
-  区别在于Slices通过指针指向数组，所以Slices是引用类型(Reference type) 
-  如果将slice复制给其他元素，则二者均是指向同一个底层数组 
-  对于函数传参时，也会指向统一底层数组 
-  切片可以由数组一部分进行截取 
   - len返回的是长度
   - cap返回的是容量
   - 以下示例说明array的长度和容量是相同的，而对于slice，len是实际数组的长度，cap则大于len

![2022-06-21-10-39-25](/images/2022-06-21-10-39-25.png)

```go
package main

import "fmt"

func main() {
    var my_array [100]int
    my_slice := my_array[0:50]

    fmt.Printf("Slice len = %d\n", len(my_slice))
    fmt.Printf("Slice cap = %d\n", cap(my_slice))
}

```

输出结果

```python
Slice len = 50
Slice cap = 100
```

## 常用操作

### 通过make定义slice

```go
slice := make([]int, 10)
```

#### 关于make

在《Effective Go》中的解释为
> The built-in function make takes a type T, which must be a slice, map or channel type, optionally followed by a type-specific list of expressions.
> It returns a value of type T (not *T).
> The memory is initialized as described in the section on initial values.

对于上述描述的需要理解的是：

- make主要用于创建切片(slice)，以及我们后面要讲到的Maps和Channel三种类型
- 返回的值是T，而非*T(即指针T)
- 内存初始化按照初始值进行

#### 参考资料

- [https://go.dev/doc/effective_go#allocation_make](https://go.dev/doc/effective_go#allocation_make)
- [https://dave.cheney.net/2014/08/17/go-has-both-make-and-new-functions-what-gives](https://dave.cheney.net/2014/08/17/go-has-both-make-and-new-functions-what-gives)

### 截取指定元素

- 只支持正数，无法像Python一样使用负数反向截取

```go
package main

import "fmt"

func main() {
    a := [...]int{1, 2, 3, 4, 5}

    s1 := a[2:4]
    fmt.Printf("s1 = %d\n", s1)
    fmt.Printf("s1 = %v\n", s1)

    s2 := a[1:5]
    fmt.Printf("s2 = %v\n", s2)

    s3 := a[:]
    fmt.Printf("s3 = %v\n", s3)

    s4 := a[:4]
    fmt.Printf("s4 = %v\n", s4)

    s5 := s2[:]
    fmt.Printf("s5 = %v\n", s5)

    s6 := a[2:4:5]
    fmt.Printf("s6 = %v\n", s6)
}
```

输出结果 

```go
s1 = [3 4]
s1 = [3 4]
s2 = [2 3 4 5]
s3 = [1 2 3 4 5]
s4 = [1 2 3 4]
s5 = [2 3 4 5]
s6 = [3 4]
```

   - slice越界后提示Error: "throw: index out of range”

```go
package main

func main() {
	var array [100]int
	slice := array[0:99]

	slice[98] = 1 3
  // ERROR: index out of range
	slice[99] = 2 4
}
```

### Slice扩展(append)

```go
package main

import "fmt"

func main() {
    s0 := []int{0, 0}
    s1 := append(s0, 2)
    s2 := append(s1, 3, 5, 7)

    // Append slice instead of value, add ...
    s3 := append(s2, s0...)

    fmt.Println("s0 = %v", s0)
    fmt.Println("s1 = %v", s1)
    fmt.Println("s2 = %v", s2)
    fmt.Println("s3 = %v", s3)
}
```

如果追加的是slice，在后面加三个点，普通值直接追加即可 

```go
s0 = %v [0 0]
s1 = %v [0 0 2]
s2 = %v [0 0 2 3 5 7]
s3 = %v [0 0 2 3 5 7 0 0]
```

### Slice复制(Copy)

- slice操作，copy，将源拷贝至目标，并且返回拷贝的数量

> copy( destSlice, srcSlice []T) int

```go
package main

import "fmt"

func main() {
    var a = [...]int{0, 1, 2, 3, 4, 5, 6, 7}
    var s = make([]int, 6)
    fmt.Printf("initial a = %v\n", a)
    fmt.Printf("initial s = %v\n", s)

    n1 := copy(s, a[0:])
    fmt.Printf("n1 = %v\n", n1)
    fmt.Printf("a = %v\n", a)
    fmt.Printf("s = %v\n", s)

    fmt.Printf("s[2:] = %v\n", s[2:])
    n2 := copy(s, s[2:])
    fmt.Printf("n2 = %v\n", n2)
    fmt.Printf("a = %v\n", a)
    fmt.Printf("s = %v\n", s)
}
```

输出结果 

```go
initial a = [0 1 2 3 4 5 6 7]
initial s = [0 0 0 0 0 0]
n1 = 6
a = [0 1 2 3 4 5 6 7]
s = [0 1 2 3 4 5]
s[2:] = [2 3 4 5]
n2 = 4
a = [0 1 2 3 4 5 6 7]
s = [2 3 4 5 4 5]
```