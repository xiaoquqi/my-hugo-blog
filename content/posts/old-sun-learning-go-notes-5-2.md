---
title: 5.2 Go语言中的内存分配
date: 2022-07-25T18:10:18+08:00
slug: "old-sun-learning-go-notes-5-2"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

Go语言中有自动垃圾回收的机制(garbage collection)，不需要为内存回收担心。而内存分配的有两种操作方式，new和make，本节重点讲述这两种操作方式。

## new

内置函数new与其他语言类似，new(T)为T类型分配一个零空间，并返回其地址，即*T类型的值。或者换句话说，它返回一个指向新分配的T类型零值的指针，这一点需要牢记。

bytes.Buffer 的文档指出“Buffer 的零值是一个可以使用的空缓冲区”。 同样，sync.Mutex没有显式构造函数或Init方法。 相反，sync.Mutex 的零值被定义为未锁定的互斥锁。

### 参数定义

> func new(Type) *Type
> 
> The new built-in function allocates memory. The first argument is a type, not a value, and the value returned is a pointer to a newly allocated zero value of that type.

## make

内置的make(T)仅用于创建slices, maps和channels，返回类型T的初始化值(非零!)，并且不是一个指针*T。产生这种区别的原因，是在使用前引用的数据类型必须进行初始化。

### 参数定义

> func make(t Type, size ...IntegerType) Type
> 
> The make built-in function allocates and initializes an object of type slice, map, or chan (only). Like new, the first argument is a type, not a value. Unlike new, make's return type is the same as the type of its argument, not a pointer to it. The specification of the result depends on the type:
> 
> Slice: The size specifies the length. The capacity of the slice is equal to its length. A second integer argument may be provided to specify a different capacity; it must be no smaller than the length. For example, make([]int, 0, 10) allocates an underlying array of size 10 and returns a slice of length 0 and capacity 10 that is backed by this underlying array. 
> Map: An empty map is allocated with enough space to hold the specified number of elements. The size may be omitted, in which case a small starting size is allocated. 
> Channel: The channel's buffer is initialized with the specified buffer capacity. If zero, or the size is omitted, the channel is unbuffered.

## 区别

new只负责分配，make负责初始化，区别点：

- new(T)返回指针，*T指向零值T
- make(T)返回初始化后的T