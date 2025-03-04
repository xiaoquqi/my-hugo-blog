---
title: 使用镜像源加速Github Clone速度
author: 孙琦(Ray)
tags:
  - Git
categories: []
date: 2021-01-25 09:11:00
---
Github被屏蔽已经不是什么太新鲜的事情了，但是对开发人员下载速度确实造成很大的困扰，所以需要使用镜像源来加速下载速度。但是，我在clone的时候又不想每次破坏原有的链接，那有没有什么自动的方法来帮助我们来修改呢？

<!-- more -->

## 设定gitconfig自动实现替换

通过在HOME目录下的.gitconfig文件可以实现自动的对github.com进行替换的目的，具体的方式如下：

```
git config --global url."https://gitclone.com/".insteadOf https://github.com
```

在$HOME/.gitconfig会发现增加了如下行：

```
[url "https://gitclone.com/"]
	insteadOf = https://github.com
```

## 其他镜像源

目前国内提供github镜像源还包括以下地址，但是通过网站测速（https://tool.chinaz.com/sitespeed）来看，目前相对于北京最稳定和快速的是gitclone.com，所以可以根据不同地域灵活进行选择以下地址：

* fastgit.org: https://doc.fastgit.org/
* gitclone.com: https://gitclone.com/
* gitee: https://gitee.com/mirrors
* cnpmjs.org: https://github.com.cnpmjs.org/

## 文件下载

还有一种情况是要从github下载某个文件，由于raw.githubusercontent.com属于长期被屏蔽状态，所以基本通过wget进行下载，比如要下载的文件为：

```
curl -O https://raw.githubusercontent.com/xiaoquqi/dockprom/master/docker-compose.vmware.exporters.yml
```

可以替换为：

```
https://raw.staticdn.net/xiaoquqi/dockprom/master/docker-compose.vmware.exporters.yml
```