---
title: 3.5 Go语言中将函数作为值使用
date: 2022-06-26T22:54:09+08:00
slug: "old-sun-learning-go-notes-3-5"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 变量定义中使用函数

在匿名函数中，我们已经见过这种形式，即将匿名函数体整体赋值给某个变量，此时该变量就相当于这个函数，Python中也有类似的表达方式。

```go
package main

import "fmt"

func main() {
	a := func() {
		fmt.Println("Hello")
	}
    fmt.Printf("a type is %T\n", a)
    fmt.Printf("a type is %v\n", a)    
    fmt.Println("Before run a()")
    
    // Function Excution
	a()
}
```

通过程序的输出，我们能够观察到：

- %T是输出变量类型，我们可以看到此时a的类型为func()
- %v是输出实际的值，这里返回的是地址，在指针章节，我们会对此详细分析
- 由于在匿名函数尾部并没有()，所以函数体并没有执行，所以main函数中的Print会优先输出
- 调用函数使用了a()，最后再输出函数内的Print

```go
a type is func()
a type is 0x47fba0
Before run a()
Hello
```

最后请大家思考，如果匿名函数执行了，程序还能正常运行吗？

```go
func main() {
    a := func() {
        fmt.Println("Hello")
    }()
    fmt.Printf("a type is %T\n", a)
    fmt.Println("Before run a()")
    
    // Function Excution
    //a()
}
```

答案很显然是不行的，你看看到这样的错误./test_function_values.go:8:3: (func literal)() used as value，这里面有两个问题：

- 首先，func内并没有return
- func并没有定义返回值的类型

我们尝试修复一下这个问题，我们做了以下修改：

- 在函数体内增加返回值
- 在函数体定义中增加了返回值类型string

```go
package main

import "fmt"

func main() {
	a := func() string {
		fmt.Println("Hello")
        return "Hello"
	}()
    fmt.Printf("a type is %T\n", a)
    fmt.Println("Before run a()")

	//a()
}
```

再次运行，有以下显著变化：

- 输出顺序发生改变，函数先执行了
- 返回值的类型发生了改变，现在与返回值string类型相同

```go
Hello
a type is string
Before run a()
```

## Map定义中使用函数

既然能赋值给变量，也能在map中使用，在下面的例子中，我们就将函数体赋值给map中的值，我们来分析下面的例子：

```go
package main

import "fmt"

func main() {
    var xs = map[int]func() int{
        1: func() int { return 10 },
        2: func() int { return 20 },
        3: func() int { return 30 },
    }

    fmt.Printf("xs is %v\n", xs)
    fmt.Printf("xs[1] is %d\n", xs[1])
    fmt.Printf("xs[1]() is %d\n", xs[1]())
}
```

对于输出结果，我们有以下结论：

- map中值的部分返回的是地址，所以取具体的xs[1]也是地址
- 根据上面的方式尝试去执行函数()，函数会返回10

```go
xs is map[1:0x47fe40 2:0x47fe60 3:0x47fe80]
xs[1] is 4718144
xs[1]() is 10
```

## 回调函数

由于函数可以作为值，所以很容易作为参数传给函数。这里来看一个简单的示例：

```go
package main

import "fmt"

func mycallback(x int) {
    fmt.Printf("mycallback print %v\n", x)
}

// Define a func as a parameter
func myfunc(y int, f func(int)) {
    f(y)
}

func main() {
    // Send mycallback as a parameter
    myfunc(3, mycallback)
}
```

我们来分析一下上面的代码

- 我们定义了一个回调函数mycallback
- 接着定义了一个函数myfunc，这个函数的第二个参数是一个函数类型，这个函数体内很简单，就是执行我们的回调函数，参数就是这个函数的第一个值
- 在main函数中，我们调用myfunc，同时将mycallback作为参数

```go
mycallback print 3
```

Callback函数在Javascript中非常常见，Go语言的具体应用场景还要根据实际需求确定，由于项目经验较少，这里就不胡说了，如果有比较典型场景的，欢迎留言。