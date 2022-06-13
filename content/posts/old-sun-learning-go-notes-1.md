---
title: 第一章 Go语言安装及开发环境配置
date: 2022-06-13T20:34:03+08:00
slug: "old-sun-learning-go-notes-1"
author: 老孙正经胡说
tags:
  - Go
  - Linux
categories:
  - Go
draft: false
---

## 下载与安装
### 官网
访问Golang官网的下载链接，可以直接下载安装包，访问地址为：[https://go.dev/dl/](https://go.dev/dl/)
![2022-06-13-20-37-46](/images/2022-06-13-20-37-46.png)

### 国内
国内也有很多做了Go镜像的站点，如果被墙，也可以从以下地址下载：

- [https://studygolang.com/dl](https://studygolang.com/dl)
### Linux(CentOS & Ubuntu)安装

```bash
# Block if you can not visit official website
curl -O https://golang.google.cn/dl/go1.18.1.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.18.1.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```
## 环境变量设置
众所周知，由于墙的原因，在后期下载Go包时，并不是非常方便，所以建议提前设置好环境变量，否则会遇到常见问题1中的错误信息。以下三个地址，任选其一就可以：
```go
# ~/.bashrc
export GOPROXY=https://goproxy.cn
export GOPROXY=https://mirrors.aliyun.com/goproxy/
export GOPROXY=https://goproxy.cn
```
## 命令行下开发
如果你和我一样使用VIM开发，可以使用这样的方式进行调试和编译
### 开发模式执行
```bash
go run main.go
```
### 编译
编译后得到可执行文件
```bash
go build main.go
```
编译后的大小，源文件是133B，编译后是1.8M
```bash
-rwxr-xr-x  1 ray  staff   133B  1  1  2021 hello.go
-rwxr-xr-x  1 ray  staff   1.8M  4 13 08:59 hello
```
## IDE下开发
这个选择因人而异，每一种IDE都可以支持Go语言，这里推荐微软的VS Code，对于很多语言都有比较好的支持，对于我这样的VIM用户也可以响应的Mapping。

### 插件安装
对于常使用VS Code，这个步骤不陌生，主要是扩展语言的支持，我安装了前两个插件。
![2022-06-13-20-38-12](/images/2022-06-13-20-38-12.png)

### 安装依赖工具
**注意：在执行该步骤前，建议参考常见问题1，进行环境变量配置，防止由于网络问题导致失败**
使用快捷键打开命令面板：

- Windows: Shift + Ctrl + P
- Mac: Shift + Command + P

![2022-06-13-20-38-30](/images/2022-06-13-20-38-30.png)
![2022-06-13-20-38-37](/images/2022-06-13-20-38-37.png)
![2022-06-13-20-38-47](/images/2022-06-13-20-38-47.png)

### 运行
我们可以在VS Code中打开Terminal方式执行命令，当然你也可以利用IDE的相关特性。我们在VS Code中按【Command + Shift + `】，就是ESC下面的【`】，可以快速打开终端执行相关命令
![2022-06-13-20-38-58](/images/2022-06-13-20-38-58.png)

## 常见问题
### 1、dial tcp 172.217.160.113:443: i/o timeout
在安装Go模块时(go get命令)，由于众所周知的问题，可能无法顺利方法，建议在环境变量添加代理，以下地址任选其一就可以。

```python
# ~/.bashrc
export GOPROXY=https://goproxy.cn
export GOPROXY=https://mirrors.aliyun.com/goproxy/
export GOPROXY=https://goproxy.cn
```
### 2、VS Code不能完美显示zsh问题
该问题的解决参考了：[https://blog.csdn.net/albertjone/article/details/86760661](https://blog.csdn.net/albertjone/article/details/86760661)
在我的VS Code中打开zsh terminal时，显示的不够完美，出现红框中标识的问题。

![2022-06-13-20-41-09](/images/2022-06-13-20-41-09.png)

但是在iTerm中显示是这样的

![2022-06-13-20-41-18](/images/2022-06-13-20-41-18.png)

首先要获取iTerm使用的非Ascii字符集

![2022-06-13-20-41-26](/images/2022-06-13-20-41-26.png)

在VS Code里，使用【Command + ,】打开字体设置，添加'Hack Nerd Font'

![2022-06-13-20-41-37](/images/2022-06-13-20-41-37.png)

配置完成后，立即生效

![2022-06-13-20-41-46](/images/2022-06-13-20-41-46.png)