---
title: 使用Chrome浏览器打开vCenter Web客户端
slug: use-chrome-open-vcenter-web-client
date: 2022-03-14T08:08:56+08:00
draft: false
author: 老孙正经胡说
tags:
  - vmware
  - devops
  - MacOS
  - 常用命令
---

在vCenter 5.x时代，vCenter Web Client都是基于Flash实现的，随着Flash逐步被淘汰，在Web端使用vCenter就非常不方便。最近由于需要对最新的ESXi 7.0版本进行测试，原有的vCenter 5.5版本无法直接对7.0版本进行管理，所以决定对vCenter进行升级。升级后的vCenter使用了全新的HTML5进行了重构，很方便的就可以在浏览器端使用vCenter，而无需再使用Windows环境下载客户端。

但是在我的Mac环境中，由于Chrome升级了浏览器安全性，虽然使用了https协议，但是仍然无法通过Chrome打开vCenter环境，通过查询VMware相关帮助文档，最终在安装证书后，顺利的使用Chrome浏览器打开了vCenter页面。

## 现象

先来看一下现象，按照通常情况，如果证书不被信任，Chrome会在高级选项中显示是否要继续的选项，但是打开vCenter后，并没有相关选项。通过对证书项检查，发现Chrome认为证书无效，在高级中并没有出现继续访问的提示，所以解决该问题的关键就是让Chrome能够正确识别vCenter的证书。

![2022-03-14-08-24-19](/images/2022-03-14-08-24-19.png)

## 下载证书

那么该从哪里下载证书呢？通过查询VMWare Knowledge Base(https://kb.vmware.com/s/article/2108294?lang=zh_CN#certificate_download_in_small_deployments)，得知可以直接从vCenter中获取证书，安装后即可恢复正常。

简单来说，vCenter的证书被存放在了https://vcenter_ip/certs/download.zip，下载导入到系统后就可以正常访问了。但是仍然受限与Chrome浏览器安全性要求，你仍然无法直接进行下载，此时有两个选项：通过Safari浏览器或者在Terminal中执行wget命令。

### Safari浏览器

虽然Safari浏览器也认为证书有问题，但是还是可以下载该文件。

![2022-03-14-08-36-10](/images/2022-03-14-08-36-10.png)

### wget方式

在Terminal中，执行wget指令

```
wget https://192.168.10.2/certs/download.zip --no-check-certificate
```

## 在Mac中导入证书

下载完成解压缩后，你会得到这样的一个目录结构：

```
certs
├── lin
│   ├── a5f3f954.0
│   ├── a5f3f954.r0
│   └── fadc1192.0
├── mac
│   ├── a5f3f954.0
│   ├── a5f3f954.r0
│   └── fadc1192.0
└── win
    ├── a5f3f954.0.crt
    ├── a5f3f954.r0.crl
    └── fadc1192.0.crt

3 directories, 9 files
```

其中mac路径下的a5f3f954.0和fadc1192.0是我们需要导入的证书，在Mac中打开[钥匙串访问]。

![2022-03-14-08-41-19](/images/2022-03-14-08-41-19.png)

左侧选择[证书]，并将两个文件直接拖入其中即可，如图所示。

![2022-03-14-08-43-33](/images/2022-03-14-08-43-33.png)

此时先双击其中的一个证书，在打开的页面中，展开[信任]，在[使用此证书时]后选择[始终允许]，关闭对话框时，需要输入系统密码。另外一个，也执行同样的操作。

![2022-03-14-08-45-05](/images/2022-03-14-08-45-05.png)

此时，刷新Chrome页面，已经可以正常打开vCenter页面了(因为我之前信任过，可能你的需要在高级中点击继续即可)。

![2022-03-14-08-48-29](/images/2022-03-14-08-48-29.png)

## 总结

作为虚拟化时代最重要的生产力工具，VMware ESXi依旧保持着巨大的活力，即使在云计算时代的冲击下，其强大的稳定性和轻运维、易运维的特性，仍然在企业级客户中占据一席之地。