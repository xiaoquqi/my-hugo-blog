---
title: 如何在Mac上控制独立应用的音量
author: 孙琦(Ray)
tags:
  - MacOS
categories: []
date: 2021-03-04 09:12:00
---
我平时用Mac开会时，需要将音量调大的情况，但是有时候忘记打开了勿扰模式，导致其他应用在通知的时候声音也巨大，比如钉钉。那么如何在Mac是否有方法独立的控制每一个应用的音量呢？答案就是Background Music。

![upload successful](/images/pasted-202.png)

<!-- more -->

## 关于Background Music

Background Music是一款纯开源软件，代码托管在Github上(https://github.com/kyleneideck/BackgroundMusic)。

如下图所示，你可以针对每一个服务进行独立选择音量提示的范围，比如我就把钉钉静音了。

![upload successful](/images/pasted-203.png)

## 安装

你可以尝试使用代码编译，当然最简单的就是下载打好包的pkg文件，直接安装即可，现在安装时候需要注意，如果你是Big Sur版本，需要下载的是预览版本。

* Bug Sur版本：https://github.com/kyleneideck/BackgroundMusic/releases/tag/0.4.0-SNAPSHOT-c0ab98b
* 早期版本：https://github.com/kyleneideck/BackgroundMusic/releases/download/v0.3.2/BackgroundMusic-0.3.2.pkg

## 开机启动

【系统偏好配置】->【用于与群组】->【登陆项】->【添加】，从应用程序中选择Backgroud Music即可。

![upload successful](/images/pasted-204.png)

![upload successful](/images/pasted-205.png)

