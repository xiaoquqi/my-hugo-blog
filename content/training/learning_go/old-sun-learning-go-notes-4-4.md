---
title: 4.4 Go语言中的单元测试
date: 2022-07-08T14:16:11+08:00
slug: "old-sun-learning-go-notes-4-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Blog
draft: false
weight: 25
---

## 基本概念

上一节提到，代码完成的标准之一还包含了单元测试，这部分也是很多开发流程中不规范的地方。写过单元测试的开发人员应该理解，单元测试最核心的价值是为了证明：为什么我写的代码是正确的？也就是从逻辑角度帮你检查你的代码。但是另外一方面，如果从单元测试覆盖率角度来看，单元测试也是非常耗时的，几乎是三倍于你代码的开发时间，所以在很多迭代速度非常快的项目中，单元测试就几乎没人要求了。但是单元测试真的能够从根本上提高代码质量，降低低级错误出现的概率。

## 示例一：取整函数基本测试

### 前置条件

Go语言内置了单元测试执行的指令，由于尚未使用Go Modules方法，我们仍然要设置环境变量，才能正确进行测试

```bash
export GO111MODULE=off
go test
```

### 代码

假设我们对以下函数进行测试

```bash
package even

func Even(i int) bool {
    return i % 2 == 0
}
```

### 单元测试建立步骤

创建一个单元测试，包括如下步骤：

- 在相同目录下创建一个名为*_test.go的文件
- 执行go test进行测试，将自动识别这些文件
- 引入testing包
- 每一个Case的命名都是以func TestXxx(t *testing.T)

### 编写单元测试

这里分别对两种场景进行测试，一种是为偶数的情况，一种是为奇数的情况，来检查我们的程序是否按照预期返回，如果不是则抛出异常信息

```go
package even

import "testing"

func TestEven(t *testing.T) {
    if !Even(2) {
        t.Log("2 should be even!")
        t.Fail()
    }
}

func TestNotEven(t *testing.T) {
    if Even(3) {
        t.Log("3 should not be even!")
        t.Fail()
    }
}
```

执行go test后

```bash
PASS
ok  	_/root/workspace/go/test_unittest	0.003s
```

## 示例二：Fail()函数

func (t *T) Fail() 让测试失败，同一个测试用例中的测试继续执行，后续的测试也会继续执行

```go
package even

import "testing"

func TestTestingFail(t *testing.T) {
    // Let create a fake case, we will call FailNow
    if Even(2) {
        t.Log("All test cases after Fail will still run")
        t.Fail()
    }

    if Even(2) {
        t.Log("The test after Fail will still run")
        t.Fail()
    }
}

func TestAfterFailCase(t *testing.T) {
    if Even(2) {
        t.Log("This test case after Fail will still run")
        t.Fail()
    }
}
```

执行测试后，TestTestingFail中的第二部分也可以继续执行。

```go
--- FAIL: TestTestingFail (0.00s)
    even_fail_test.go:8: All test cases after Fail will still run
    even_fail_test.go:13: The test after Fail will still run
--- FAIL: TestAfterFailCase (0.00s)
    even_fail_test.go:20: This test case after Fail will still run
FAIL
exit status 1
FAIL	_/root/workspace/go/test_unittest	0.004s
```

## 示例三：FailNow函数

func (t *T) FailNow() 让测试失败，同一个测试用例中的测试不再执行，后续的测试也会继续执行

```go
package even

import "testing"

func TestTestingFailNow(t *testing.T) {
    // Let create a fake case, we will call FailNow
    if Even(2) {
        t.Log("All test cases after FailNow will not run")
        t.FailNow()
    }

    if Even(2) {
        t.Log("The test after FailNow will be skipped")
        t.FailNow()
    }
}

func TestAfterFailNowCase(t *testing.T) {
    if Even(2) {
        t.Log("This test case after FailNow will still run")
        t.FailNow()
    }
}
```

执行后TestTestingFailNow中的第二段测试不再执行，而后面的TestAfterFailNowCase继续执行

```go
--- FAIL: TestTestingFailNow (0.00s)
    even_failnow_test.go:8: All test cases after FailNow will not run
--- FAIL: TestAfterFailNowCase (0.00s)
    even_failnow_test.go:20: This test case after FailNow will still run
FAIL
exit status 1
FAIL	_/root/workspace/go/test_unittest	0.003s
```

## 实例四：Log和Fetal函数

- func (t *T) Log(args ...interface{}) 使用默认格式记录日志，等同于Print()，记录错误日志
- func (t *T) Fatal(args ...interface{}) 与Log功能相似，但是输出日志后会调用FailNow

```go
package even

import "testing"

func TestTestingFatal(t *testing.T) {
    // Let create a fake case, we will call FailNow
    if Even(2) {
        t.Fatal("All test cases after FailNow will not run")
    }

    if Even(2) {
        t.Fatal("The test after Fatal will not run")
    }
}

func TestAfterFatalCase(t *testing.T) {
    if Even(2) {
        t.Fatal("This test case after Fatal will still run")
    }
}
```

Fatal的执行过程与FailNow相似

```go
--- FAIL: TestTestingFatal (0.00s)
    even_fatal_test.go:8: All test cases after FailNow will not run
--- FAIL: TestAfterFatalCase (0.00s)
    even_fatal_test.go:18: This test case after Fatal will still run
FAIL
exit status 1
FAIL	_/root/workspace/go/test_unittest	0.005s
```