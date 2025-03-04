---
title: 8.3 在Go语言中执行外部命令
date: 2023-01-05T20:01:41+08:00
slug: "old-sun-learning-go-notes-8-3"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
weight: 46
---

执行外部命令是开发中常见的需求，本节重点介绍如何在Go语言中执行外部命令，并且合理的进行控制。

## 执行命令

Go中执行命令主要是通过os/exec，我们来看下面的例子

```go
package main

import (
    "log"
    "os/exec"
)

func main() {

    cmd := exec.Command("ls", "-lrt")

    err := cmd.Run()

    if err != nil {
        log.Fatalf("Command run failed due to %v\n", err)
    }
}
```

以上代码执行后，将不会有任何输出，因为我们并没有对标准输入或错误进行处理。如果想测试异常部分，可以将ls命令改完一个不存在的命令。
如果命令行有多个参数，则每一个参数都是单独的字符串，例如：

```go
prg := "echo"

arg1 := "there"
arg2 := "are three"
arg3 := "falcons"

cmd := exec.Command(prg, arg1, arg2, arg3)
```

Run底层实际上是调用的Start()和Wait()方法

```go
// Run starts the specified command and waits for it to complete.
//
// The returned error is nil if the command runs, has no problems
// copying stdin, stdout, and stderr, and exits with a zero exit
// status.
//
// If the command starts but does not complete successfully, the error is of
// type *ExitError. Other error types may be returned for other situations.
//
// If the calling goroutine has locked the operating system thread
// with runtime.LockOSThread and modified any inheritable OS-level
// thread state (for example, Linux or Plan 9 name spaces), the new
// process will inherit the caller's thread state.
func (c *Cmd) Run() error {
	if err := c.Start(); err != nil {
		return err
	}
	return c.Wait()
}
```

## 将运行结果输入到标准输出和标准错误

将Command执行的结果，直接输出到标准输出(os.Stdout)和标准错误(os.Stderr)中。

```go
package main

import (
    "log"
    "os"
    "os/exec"
)

func main() {

    cmd := exec.Command("ls", "-lrt")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr

    err := cmd.Run()
    if err != nil {
        log.Fatalf("Command run failed due to %v\n", err)
    }
}
```

该程序运行后，会将ls -lrt的结果输出的标准输出中。

## 标准输出作为参数输入

假设我们需要执行这样一条指令，将所有标准输出的内容转换为大写字母

```go
echo 'hello, world' | tr a-z A-Z
```
我们可以将hello, world输出到标准输出中，再执行命令的方式实现该管道操作，实现精准控制。
```go
package main

import (
    "bytes"
    "fmt"
    "log"
    "os/exec"
    "strings"
)

func main() {
    cmd := exec.Command("tr", "a-z", "A-Z")

    cmd.Stdin = strings.NewReader("hello, world")

    var out bytes.Buffer
    cmd.Stdout = &out

    err := cmd.Run()

    if err != nil {
        log.Fatal(err)
    }

    fmt.Printf("translated phrase: %q\n", out.String())
}
```

首先我们将我们想转换文字，输出到标准输入中

```go
cmd.Stdin = strings.NewReader("hello, world")
```

关于NewReader的定义在这：[https://pkg.go.dev/strings#NewReader](https://pkg.go.dev/strings#NewReader)

> NewReader returns a new Reader reading from s. It is similar to bytes.NewBufferString but more efficient and read-only.

再定义一个bytes.Buffer，并且将标准输出定向到这个变量中，后期还可以对标准输出进行后续操作。

```go
var out bytes.Buffer
cmd.Stdout = &out
```

最后执行该程序，执行结果为

```go
translated phrase: "HELLO, WORLD"
```

## 通过变量获取标准输出

我们还有一种比较简单的方法来获取标准输出

```go
package main

import (
    "fmt"
    "log"
    "os/exec"
)

func main() {

    out, err := exec.Command("ls", "-l").Output()

    if err != nil {
        log.Fatalf("Error message is: %v\n", err)
    }

    fmt.Printf("Command returns: %v\n", string(out))
}
```

在执行Command后，通过调用Output就可以将输出存入变量out中

```go
out, err := exec.Command("ls", "-l").Output()
```

如果是错误的执行，则通过err输出并包含退出错误编码，例如我们将ls命令修改为lsa，则会出现如下错误

```go
2022/06/05 20:34:09 Error message is: exec: "lsa": executable file not found in $PATH
exit status 1
```

## Linux管道实现

我们在Linux中经常使用管道将上一个命令的输入，作为下一个命令的输出，利用Go中的os/exec提供的StderrPipe、StdinPipe和StdoutPipe可以实现管道。本内容来自([https://colobu.com/2020/12/27/go-with-os-exec/](https://colobu.com/2020/12/27/go-with-os-exec/))

我们先来看一个基本实现，假设我们要实现以下命令

```go
ls | wc -l
```

### 基本实现

将管道建立好后，利用Start和Wait方法进行开始和等待

```go
package main

import (
    "log"
    "os"
    "os/exec"
)

func main() {
    cmdls := exec.Command("ls")
    lsout, err := cmdls.StdoutPipe()
    if err != nil {
        log.Fatalf("failed to get StdoutPipe of ls: %v", err)
    }

    cmdWC := exec.Command("wc", "-l")
    cmdWC.Stdin = lsout
    cmdWC.Stdout = os.Stdout

    err = cmdls.Start()
    if err != nil {
        log.Fatalf("failed to call cmdls.Run(): %v", err)
    }

    err = cmdWC.Start()
    if err != nil {
        log.Fatalf("failed to call cmdWC.Start(): %v", err)
    }

    cmdls.Wait()
    cmdWC.Wait()
}
```

### 通用实现

上面的实现不具有通用型，如果要执行的管道过多，则代码的冗余性会很多，所以这篇文章中提供了一个通用的方法([https://colobu.com/2020/12/27/go-with-os-exec/](https://colobu.com/2020/12/27/go-with-os-exec/))

```go
package main

import (
    "log"
    "os/exec"
)

func main() {
	cmdls := exec.Command("ls", "/")
	cmdWC := exec.Command("wc", "-l")

	data, err := pipeCommands(cmdls, cmdWC)
	if err != nil {
		log.Fatalf("failed to call pipeCommands(): %v", err)
	}

	log.Printf("output: %s", data)
}
func pipeCommands(commands ...*exec.Cmd) ([]byte, error) {
	for i, command := range commands[:len(commands) - 1] {
		out, err := command.StdoutPipe()
		if err != nil {
			return nil, err
		}

		command.Start()
		commands[i+1].Stdin = out
	}

	final, err := commands[len(commands) -1].Output()
	if err != nil {
		return nil, err
	}

	return final, nil
}
```

## 参考文章

命令执行有很多知识点，建议随用随查就好了，这里给出两个参考的总结性用法

- go os/exec 简明教程([https://colobu.com/2020/12/27/go-with-os-exec/](https://colobu.com/2020/12/27/go-with-os-exec/))
- Go exec command([https://zetcode.com/golang/exec-command/](https://zetcode.com/golang/exec-command/))