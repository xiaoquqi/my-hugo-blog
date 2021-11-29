---
title: 关闭Mac系统开机启动音
author: 孙琦(Ray)
tags:
  - MacOS
categories: []
date: 2021-03-05 07:31:00
---
不知道你是否和我有一样的困惑，宁静的早晨打开iMac，一声浑然天成的开机声响彻屋内。虽然以Mac系统稳定性来说不必关机，但是对于iMac这种没有电池的主机，我还是有定期关机的习惯，只不过开机声这个问题让我很困扰。

<!-- more -->

## Big Sur关闭开机音

在macOS Big Sur 11或者以上版本中，可以直接通过系统菜单就将开机启动声音进行关闭，具体的设置路径如下：

系统左上角 >【系统偏好设置】>【声音】>【声音效果】，取消【启动时播放声音】即可。

![upload successful](/images/pasted-206.png)

## 低版本关闭开机音

那么对于低版本的Mac系统如何关闭声音呢，答案只能通过命令行的方式了。在【终端】中输入：

```
sudo nvram StartupMute=%01
```

恢复开机音：

```
sudo nvram StartupMute=%00
```