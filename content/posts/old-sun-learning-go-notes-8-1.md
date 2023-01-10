---
title: Go语言中文件操作
date: 2023-01-05T20:01:38+08:00
slug: "old-sun-learning-go-notes-8-1"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

## 常用包

文件操作应该是应用程序里非常常见的一种操作，无论是哪种应用场景，几乎都离不开文件的基本操作。Go语言中提供了三个不同的包去处理文件

### os

os包提供了处理文件的API接口，遵循Unix标准，平台无关，所有操作系统都可以使用。错误处理上是Go语言独有的，失败时，返回的是错误类型而非系统错误编号，对于调试很有帮助。os包中提供了创建、删除、打开、修改权限等功能。

### 与I/O操作相关包

- io
   - I/O原语接口
   - 包装到了公共接口中，该接口抽象了功能
- ioutil
   - I/O实用功能，从Go 1.6开始，可以直接通过io后os包访问相同的功能
- bufio
   - 文件的缓冲I/O提供接口
   - 缓冲区实际是内存中的临时空间，用于存储数据并在该空间执行临时I/O操作，减少系统调用及磁盘I/O，适用于数据块传输场景，不适用于单个字符的I/O操作
   - 默认的操作都是无缓冲的

## 常用文件/目录操作

### 路径拼接

```go
package main

import (
    "fmt"
    "path"
)

func JoinPath() {
    dirs := []string{"/", "home", "ray", "workspace"}
    path := path.Join(dirs...)
    fmt.Printf("Path after join: %v\n", path)
}

func main() {
    JoinPath()
}
```

输出信息为

```go
Path after join: /home/ray/workspace
```

更多功能请参考：[https://pkg.go.dev/path/filepath#pkg-functions](https://pkg.go.dev/path/filepath#pkg-functions)

### 创建文件（touch）

改代码执行后将生成一个为空的sample.txt文件

```go
package main

import (
    "log"
    "os"
)

func CreateEmptyFile() {
	myFile, err := os.Create("sample.txt")
	if err != nil {
		log.Fatal("ERROR! ", err)
	}
	log.Println("Empty file created successfully. ", myFile)
	myFile.Close()
}

func main() {
    CreateEmptyFile()
}
```

### 获取文件信息

这里主要使用os.Stat函数

```go
package main

import (
    "fmt"
    "log"
    "os"
)

func FileInfo() {
	fileInfo, err := os.Stat("sample.txt")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("File Name:", fileInfo.Name())
	fmt.Println("Size ", fileInfo.Size(), " bytes")
	fmt.Println("Permissions:", fileInfo.Mode())
	fmt.Println("Last modified:", fileInfo.ModTime())
	fmt.Println("Is Directory: ", fileInfo.IsDir())
}

func main() {
    FileInfo()
}
```

### 读取文件内容

和其他语言类似，读取文件主要使用Open, Read等函数，文件处理最底层是基于原始字节的，在这个抽象之上，可以进一步构建更方便的接口。

```go
package main

import (
    "log"
    "os"
)

func FileRead(filePath string) {
	oFile, err := os.Open(filePath)
	if err != nil {
		log.Fatal(err)
	}
	defer oFile.Close()
	buff := make([]byte, 100)
	for no, err := oFile.Read(buff); err == nil; no, err = oFile.Read(buff) {
		if no > 0 {
			os.Stdout.Write(buff[0:no])
		}
	}
}

func main() {
    FileRead("sample.txt")
}
```

### 写入文件内容

我们尝试使用一个文件拷贝的样例，来学习写入的方式，这里除了刚才使用的os包，还是用了io包，最终将显示一共拷贝了多少字节

```go
package main

import (
    "log"
    "io"
    "os"
)

func Copy(src, dest string) {

	srcFile, err := os.Open(src)
	if err != nil {
		log.Fatal(err)
	}
	defer srcFile.Close()

	destFile, err := os.Create(dest)
	if err != nil {
		log.Fatal(err)
	}
	defer destFile.Close()

	numBytes, err := io.Copy(destFile, srcFile)
	if err != nil {
		log.Fatal(err)
	}
	log.Printf("Successfully copied %d bytes", numBytes)
	err = destFile.Sync()
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
    Copy("source.txt", "dest.txt")
}
```

## 参考资料

- 更多关于文件的操作，可以在使用过程中查询官方文档。
- Go语言文件操作大全([https://colobu.com/2016/10/12/go-file-operations/](https://colobu.com/2016/10/12/go-file-operations/))