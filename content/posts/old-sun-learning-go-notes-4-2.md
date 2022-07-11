---
title: 4.2 Go语言中包(Packages)的命名
date: 2022-07-08T14:16:06+08:00
slug: "old-sun-learning-go-notes-4-2"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 基本规则

- Go标准库使用了Unix名称命名函数
- 其他函数使用驼峰命名CamelCase，例如：ReadFile, NewWriter, 
- 使用import导入包后，跟随点(.)访问函数，例如：bytes.Buffer
- Go中包名通常使用小写字母，并且是单独的单词
- 导入包并重命名，类似Python中的as，下面例子中将bytes包命名为bar，所以可以使用bar.Buffer，注意这里顺序与Python相反，先写alias名称，再写实际包的名称，实际包使用双引号
- 要善于利用包结构来表达意思，例如：缓存处理包bufio中读取的类型是Reader而不是BufReader，因为在使用中视为整体bufio.Reader，这样简单明了而且达义
- 长名称不一定让内容更容易理解，短小精悍的例子once.Do(sync包)，once.Do(setup)读起来比once.DoOrWaitUntilDone(setup)更易懂

```go
import bar "bytes"

bar.Buffer
```

## 包名与目录的关系

包名本质上是所在目录的名称，我们在基础知识演示用例中进行扩展，进一步理解包名，执行前需要执行的命令请参考上一节，首先来看一下目录结构：

```go
├── main.go
├── src
│   ├── myfunc
│   │   └── myfunc.go
│   └── subpackage
│       └── sub
│           └── subfunc.go
└── test_package
```

此时，如果我们想使用subpackage/sub/subfunc.go时，需要import的是subpackage/sub，而不是subpackage/sub/subfunc，来看具体的实现：

```go
package subfunc

import "fmt"

func MySubFunc() {
    fmt.Println("This is a sub package func")
}
```

我们回到使用的主函数中，我们在主函数中引入"subpackage/sub"，而调用中直接使用了文件名称myfunc

```go
package main

import "myfunc"
import "subpackage/sub"

func main() {
   myfunc.MyPublicFunc()

   // NOTE(Ray): Can not call private function
   //myfunc.myPrivateFunc()

   subfunc.MySubFunc()
}
```

执行的结果如下

```go
Use my public function.
This is a sub package func
```