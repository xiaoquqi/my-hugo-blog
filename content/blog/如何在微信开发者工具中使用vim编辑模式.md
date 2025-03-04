---
title: 如何在微信开发者工具中使用vim编辑模式
author: 孙琦(Ray)
date: 2021-01-27 07:52:10
tags:
---
随着云计算技术的发展特别是无服务化的发展，在业务系统的研发上，前端和后端的边界逐步被打破。微信小程序便是这一方面的典型代表，特别是结合了腾讯Serverless云开发的套件后，小程序融会贯通成为业务开发非常重要的载体。今年疫情期间，基于小程序开发的健康码充分发挥了小程序这一方面的特点。小程序上手开发难度不高，基本都是基于Javascript生态构建，对于前端开发或者后端开发来说，无疑都是福音，让大家真正的做一次全栈开发。

作为一名10多年的开发人员，vim是我最常使用的编辑器，但是在微信开发者工具中并没有直接提供vim的开发模式。经过不断的探索，终于发现微信开发者工具对VS Code插件的兼容模式，于是按照文档将VS Code vim插件安装在微信开发者工具中。果然，我熟悉的vim模式又回来了，这篇文章就为大家简单分享一下。

<!-- more -->

## 在VS Code安装vim插件

首先在VS Code中安装vim模拟器，如图所示，我安装的是1.18.5版本。我使用的是mac系统，安装完成后，插件会存放在用户HOME目录下的$HOME/.vscode/extensions/vscodevim.vim-1.18.5中。

![upload successful](/images/pasted-116.png)

## 在微信开发者工具安装VS Code插件

1、在微信开发者工具中点击“设置”->"扩展设置"

![upload successful](/images/pasted-117.png)

2、在打开的窗口中选择“编辑器自定义扩展”，因为我已经安装过了，所以截图中已经包含了vscode.vim插件

![upload successful](/images/pasted-118.png)

3、点击上方的“打开扩展文件夹”，此时会打开微信开发者插件目录，而你要做的就是将vscode插件拷贝过去。

![upload successful](/images/pasted-119.png)

但是由于从Finder中无法直接访问隐藏目录，先在左侧选择HOME目录。

![upload successful](/images/pasted-121.png)

使用“前往文件夹”选项，填入.vscode/extensions。将.vscode/extensions/vscodevim.vim-1.18.5拷贝之刚才打开的微信开发者工具的扩展目录中。

![upload successful](/images/pasted-120.png)

4、重启微信开发者工具后，就能在“编辑器自定义扩展”中看到vim插件，启动插件后，再次退出重启，此时编辑器里已经可以使用vim模式了。

![upload successful](/images/pasted-122.png)
