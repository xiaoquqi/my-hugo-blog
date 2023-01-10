---
title: 利用Go语言构建HTTP客户端和服务端
date: 2023-01-05T20:01:46+08:00
slug: "old-sun-learning-go-notes-8-4"
author: 老孙正经胡说
tags:
  - Linux
  - Go
categories:
  - Go
draft: false
---

HTTP也是常用的一种操作，Go语言处理http请求的包主要是net/http，其中包含Get、Post等常用操作。

## 客户端

在这个示例中，主要包含利用http.Get访问“历史上的今天”接口，显示的部分包含状态信息和状态的可读信息，最后显示返回的内容

```go
package main

import (
    "fmt"
    "log"
    "net/http"
    "io/ioutil"
)

func main() {
    resp, err := http.Get("https://api.oick.cn/lishi/api.php")
    if err != nil {
        log.Fatalln(err)
    }

    // Print the HTTP Status Code and Status Name
    fmt.Println("HTTP Response Status:",
                resp.StatusCode,
                http.StatusText(resp.StatusCode))

    body, err := ioutil.ReadAll(resp.Body)
    resp.Body.Close()
    if err == nil {
        fmt.Printf("%s\n", string(body))
    }
}
```

运行结果如下

```go
HTTP Response Status: 200 OK
{"code":"1","day":"06/ 06","result":[{"date":"1599年06月06日","title":"西班牙画家委拉士开兹出生"},{"date":"1606年06月06日","title":"法国作家皮埃尔·高乃依出生"},{"date":"1660年06月06日","title":"瑞典和丹麦在哥本哈根结束两国战争"},{"date":"1683年06月06日","title":"英国牛津大学阿什莫尔博物馆正式开放"},{"date":"1799年06月06日","title":"俄国诗人、现实主义奠基人普希金诞生"},{"date":"1861年06月06日","title":"意大利首任总理加富尔去世"},{"date":"1875年06月06日","title":"德国作家托马斯·曼出生"},{"date":"1901年06月06日","title":"印度尼西亚独立运动领袖苏加诺出生"},{"date":"1916年06月06日","title":"北洋军阀领袖袁世凯病逝"},{"date":"1961年06月06日","title":"精神病学先驱卡尔·古斯塔夫·荣格去世"},{"date":"1976年06月06日","title":"石油大王保罗·盖蒂去世"},{"date":"1981年06月06日","title":"中国农学家袁隆平荣获中国第一个特等发明奖"},{"date":"1984年06月06日","title":"帕基特诺夫推出游戏俄罗斯方块"},{"date":"1986年06月06日","title":"苏联用一枚火箭一次成功发射八颗卫星"},{"date":"2012年06月06日","title":"美国知名科幻、奇幻、恐怖小说作家雷·布莱伯利逝世"}]}
```

### 参考文档

- Go官方帮助文档：[https://pkg.go.dev/net/http](https://pkg.go.dev/net/http)
- Making HTTP requests in Go: [https://blog.logrocket.com/making-http-requests-in-go/](https://blog.logrocket.com/making-http-requests-in-go/)

## 服务端

除了利用net/http构建Client，也能很容易的实现一个http server端，Handler是net/http处理逻辑的基本概念，在开发过程中，主要通过http.HandlerFunc实现路由与方法的关系。

```go
package main

import (
    "fmt"
    "net/http"
)

func hello(w http.ResponseWriter, req *http.Request) {
    fmt.Fprintf(w, "hello\n")
}

func headers(w http.ResponseWriter, req *http.Request) {
    for name, headers := range req.Header {
        for _, h := range headers {
            fmt.Fprintf(w, "%v: %v\n", name, h)
        }
    }
}

func main() {
    http.HandleFunc("/hello", hello)
    http.HandleFunc("/headers", headers)

    fmt.Println("HTTP server is starting at port 8090...")
    http.ListenAndServe(":8090", nil)
}
```

在上面的例子中，访问/hello浏览器会显示hello，如果访问/headers，则显示出所有请求对象的信息，程序默认端口为8090。