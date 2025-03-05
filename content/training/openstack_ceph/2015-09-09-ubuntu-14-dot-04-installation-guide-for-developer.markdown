---
layout: post
title: "Ubuntu 14.04 Server开发者安装指南"
date: 2015-09-09 13:50:24 +0800
comments: true
categories: [openstack, ubuntu]
---

## 为什么会写这篇Blog
近期，接触了一些OpenStack的入门者，很多人对Linux系统并不是很熟悉，导致安装出来的系统五花八门，间接地影响了后面的开发与调试，所以这里给出我的安装流程，供初学者们参考。我使用的是Ubuntu 14.04 64bit Server版本的ISO进行安装，其他版本方法类似。

<!-- more -->

## 注意
这篇Blog没有提及的地方：

* 网络，需要根据实际情况进行配置，我这里面使用的是DHCP自动获取，所以没有相关步骤
* 分区，这里面使用的是默认配置，但是生产环境的配置一般需要手动划分

## 安装步骤

* 一定要选择English，否则处理中文的时候太麻烦
![](/images/blogs/install-ubuntu/1.png)
* 正式开始进入安装
![](/images/blogs/install-ubuntu/2.png)
* 与上面的原则一致，一定要选择English
![](/images/blogs/install-ubuntu/3.png)
* Location一定要选择中国，否则默认不会使用中文的Ubuntu源，影响安装速度，这一步很多初学者不会在意
![](/images/blogs/install-ubuntu/4.png)
![](/images/blogs/install-ubuntu/5.png)
![](/images/blogs/install-ubuntu/6.png)
* 这里面主要是字符集的问题，选择United States
![](/images/blogs/install-ubuntu/7.png)
* 不需要检查键盘布局
![](/images/blogs/install-ubuntu/8.png)
* 默认使用English布局就好了
![](/images/blogs/install-ubuntu/9.png)
* 主机名设置，就是hostname
![](/images/blogs/install-ubuntu/10.png)
* 用户设置，建议建立一个普通用户
![](/images/blogs/install-ubuntu/11.png)
![](/images/blogs/install-ubuntu/12.png)
![](/images/blogs/install-ubuntu/13.png)
![](/images/blogs/install-ubuntu/15.png)
![](/images/blogs/install-ubuntu/16.png)
* 不加密Home目录
![](/images/blogs/install-ubuntu/17.png)
* 设置时区，这一步也很重要，默认情况下会自动检测到，但是如果不对，一定要修改一下，否则你的系统时间与你实际不一致，你程序里的时间跟着不对，跟调试增加难度
![](/images/blogs/install-ubuntu/18.png)
* 这里面分区用默认的就好啦，当然如果你知道该如何分区，可以采用Manual方式
![](/images/blogs/install-ubuntu/19.png)
![](/images/blogs/install-ubuntu/20.png)
![](/images/blogs/install-ubuntu/21.png)
![](/images/blogs/install-ubuntu/22.png)
![](/images/blogs/install-ubuntu/23.png)
* 如果访问网络需要使用代理，可以设置一下
![](/images/blogs/install-ubuntu/24.png)
* 不选择自动更新
![](/images/blogs/install-ubuntu/25.png)
* 默认只需要选择SSH服务，保证我们在安装后能够SSH登陆服务器即可
![](/images/blogs/install-ubuntu/26.png)
* 安装grub
![](/images/blogs/install-ubuntu/27.png)
* 重启完成安装
![](/images/blogs/install-ubuntu/28.png)

## 后记
谨记此篇Blog送给我的小徒弟周小球小朋友，希望你能利用利用最后的一年的时间努力学习，找到称心如意的工作。
