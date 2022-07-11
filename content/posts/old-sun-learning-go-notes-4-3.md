---
title: 4.3 Go语言包(Packages)文档
date: 2022-07-08T14:16:08+08:00
slug: "old-sun-learning-go-notes-4-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 简述

什么是好代码？每个人心里的标准答案可能都不同，我认为有三个要素：代码本身的逻辑、文档和单元测试。换言之，这是代码完成的标准，很多时候为了项目，疲于奔命的完成第一点就算不错了，技术债越欠越多，最后只能推翻了重写。做了这么久的研发管理，发现越是简单的越好用，代码外的文档更多是从架构层对项目进行描述、设计等定义，而文档内的代码应该是让看的人，一下子就明白内部的逻辑。

Go语言默认就提供了文档生成方式，无须额外的手段，后续我还想整理一个关于Go语言规范的内容，可能还会对如何写好一段语言内的文档给出进一步的最佳实践。

## 包头部文档

```go
// The even package implements a fast function for detecting if an integer
// is even or not.
package even
```

使用go doc时，会显示头部的注释内容

```bash
go doc
```

也可以使用/*...*/方式定义，注意这里增加了一些空格，让段落更加突出、可读性更强。在实际项目中，很多开发人员写的文档逻辑性很差，究其原因是语文问题

```go
/*
    The even package implements a fast function for detecting if an integer
    is even or not.
*/
package even
```

如果是较大型的项目，通常使用doc.go单独对包文档进行定义

## 函数文档

在每个函数头部都应有相应的文档进行描述，即使是私有函数

```go
// Even returns true of i is even. Otherwise false is returned.
func Even(i int) bool {
    ......
}

// odd is the opposite of Even.
func odd(i int) bool {
    ......
}
```