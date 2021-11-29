---
title: MacOS VPN拨号后自动设置路由
author: 孙琦(Ray)
date: 2020-11-11 20:04:07
tags:
---
## 目的

公司使用的VPN是L2TP协议的，平时在家远程工作时需要VPN拨入，但是又不想所有的流量都经过VPN，需要使用路由表来路由指定的网段。

<!-- more -->

## 允许L2TP共享密钥为空

公司L2TP共享密钥为空，默认MacOS是不支持的，所以需要在配置文件中特殊设定，在/etc/ppp下生成options文件。

```
sudo tee /etc/ppp/options << EOF
plugin L2TP.ppp
l2tpnoipsec
EOF
```

## 自动路由设置

原理很简单，在连接VPN后将指定网段的IP经过VPN虚拟接口即可，具体的实现如下：

```
sudo touch /etc/ppp/ip-up
sudo chmod 0755 /etc/ppp/ip-up
```

ip-up的内容如下，只需要修改SUBNET网段即可，例如：192.168.10.0/24

```
##!/bin/sh
/sbin/route add <SUBNET> -interface $1 
```

其余可利用参数如下：

* $1: VPN接口(例如：ppp0)
* $2: 未知
* $3: VPN服务器地址
* $4: VPN网关地址
* $5: 非VPN网关，本地使用