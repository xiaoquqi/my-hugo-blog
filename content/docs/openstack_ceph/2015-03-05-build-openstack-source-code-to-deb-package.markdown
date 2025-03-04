---
layout: post
title: "(Havana)将OpenStack Havana源代码编译为DEB包"
date: 2015-03-05 21:57:16 +0800
comments: true
categories: [openstack, ubuntu, deb]
---

## Why

我想有以下有几个原因促使我写这篇Blog：

* 很多人开始OpenStack之旅是从Ubuntu开始，但是却没有一篇文章系统的介绍如何将修改后的代码重新编译回DEB包。
* 如果我们采用源代码直接安装的方式对OpenStack模块进行管理，一致性很难保证，难以维护。
* Debian类系统的打包看起来比RPM包复杂很多。

## Who

谁需要看这篇文章呢？

* 不了解如何编译DEB包
* 想把修改过的OpenStack源代码重新发布，供内部使用
* 希望改变直接维护源代码

当然，如果您已经是这方面的高手，欢迎给我指正我Blog中的不足，十分感谢。

<!-- more -->

## Quick Start

我已经将整个的编译过程集成在Vagrant脚本中，你可以直接安装Vagrant后，下载我的源代码，启动后就能看到整个的编译过程。

Vagrant 版本要求为1.3.5，Virtualbox版本要求为4.1或者4.2均可。

## Let's play some magic

```
git clone https://github.com/xiaoquqi/vagrant-build-openstack-deb
cd vagrant-build-openstack-deb
vagrant up
```

虚拟机启动后，将会自动从github(这里使用的是csdn code的镜像代码)同步最新代码，然后使用编译脚本，执行打包操作。如果不考虑下载的时间，整个过程大概持续5分钟左右的时间，编译好的Deb包将会存放在/root/build目录下。

```
vagrant ssh
```

即可登陆到虚拟机，切换到root目录就可以查看到所有打包好的DEB的情况了，当然你也可以直接使用dpkg -i命令进行安装。

```
sudo -s
cd /root/build
ls -lrt *.deb
dpkg -i python-glance_2013.2.2.dev1.g5cd7a22~precise-0ubuntu1_all.deb
```

## Step by Step

看过了整个的编译过程，下面来介绍一点点细节。

全部的编译部分代码都在这个文件中：https://github.com/xiaoquqi/vagrant-build-openstack-deb/blob/master/scripts/build.sh

下面让我们来仔细分析一下整个编译过程。

* 添加必要的源

这里面我们用的源包含sohu的Ubuntu 12.04源以及Ubuntu的Havana源

    deb http://mirrors.sohu.com/ubuntu/ precise main restricted
    deb http://mirrors.sohu.com/ubuntu/ precise-updates main restricted
    deb http://mirrors.sohu.com/ubuntu/ precise universe
    deb http://mirrors.sohu.com/ubuntu/ precise-updates universe
    deb http://mirrors.sohu.com/ubuntu/ precise multiverse
    deb http://mirrors.sohu.com/ubuntu/ precise-updates multiverse
    deb http://mirrors.sohu.com/ubuntu/ precise-backports main restricted universe multiverse
    deb http://mirrors.sohu.com/ubuntu/ precise-security main restricted
    deb http://mirrors.sohu.com/ubuntu/ precise-security universe
    deb http://mirrors.sohu.com/ubuntu/ precise-security multiverse
    deb http://ubuntu-cloud.archive.canonical.com/ubuntu precise-updates/havana main

* 安装必要的编译软件

```
apt-get install -y debootstrap equivs schroot
apt-get install -y devscripts
apt-get install -y build-essential checkinstall sbuild
apt-get install -y dh-make
apt-get install -y bzr bzr-builddeb
apt-get install -y git
apt-get install -y python-setuptools
```

* 编译脚本的源代码仓库

Ubuntu维护源代码编译脚本是使用叫做bzr的工具，常使用Launchpad的朋友应该比较熟悉，这是一套类似于git的分布式管理工具，不同的是这是一套完全用python语言实现的管理工具，不仅具有代码版本控制功能并且与Launchpad高度整合，作为Ubuntu维护不可缺少的重要工具之一。例如，这里面用到的glance编译脚本就可以在这里找到：

https://code.launchpad.net/~ubuntu-server-dev/glance/havana

页面上方有下载代码的方式：

```
bzr branch lp:~ubuntu-server-dev/glance/havana
git clone https://code.csdn.net/openstack/glance.git --branch "stable/havana" glance_source
```

* 准备环境

在Vagrant启动一台新虚拟机之后，并没有pip，如果不安装pip，则会在python setup.py sdist过程中，把pip安装到源代码目录中，引起Build失败。将//vagrant/pip/pip-1.4.1.tar.gz解压缩并安装，之后安装pbr：

```
tar zxvf pip-1.4.1.tar.gz
cd pip-1.4.1
sudo python setup.py install
sudo pip install pbr
```

* 生成source文件

进入glance_source目录，执行

```
python setup.py sdist
```

生成的tar.gz文件会在glance_source/dist下，注意此时该文件的名称为：

    glance-2013.2.2.dev1.g5cd7a22.tar.gz

接下来我们需要将该文件重命名为：

    glance_2013.2.2.dev1.g5cd7a22~precise.orig.tar.gz

特别注意：glance后面已经变为下划线！！！

把文件移动到与glance和glance_source同一级别的目录，这样在编译的时候，才能找到source文件。此时的目录结构为：

    ├── glance
    │   ├── debian
    ├── glance_source
    ├── glance_2013.2.2.dev1.g5cd7a22~precise.orig.tar.gz

* 安装依赖包

为了保证顺利的完成编译，我们需要安装要编译包的所有依赖包，简单来说就是glance/debian/control文件中定义的Depends部分的内容。当然在编译的时候我们也可以完全忽略依赖，但是并不推荐。

```
mk-build-deps -i -t 'apt-get -y' debian/control
```

这样系统就会自动安装所有依赖包，并且生成一个glance-build-deps_1.0_all.deb文件。

* 生成日志信息

开始编译前，我们还需要告诉编译器我们要编译的版本，还记得刚才生成的dist包吗，把那个版本拿出来作为我们commit的版本。

```
cd glance
dch -b -D precise --newversion "1:2013.2.2.dev1.g5cd7a22~precise-0ubuntu1" 'This is a build test.'
debcommit
```

这样在glance/debian/changelog中就会增加一条新的日志。

* 开始编译

万事俱备，只欠东风。我们利用bzr提供的builddeb开始编译，这里我们忽略签名问题。

```
cd glance
bzr builddeb -- -sa -us -uc
```

大功告成啦。快去/root/build/glance下看看你的deb包吧。

## 总结

Debian包的编译的确涉及很多知识点，而且可使用的编译工具很多，关系很复杂。这篇博文，只为了帮助大家对DEB包的编译有一个快速的认识，如果想了解更多关于编译的知识，请关注后续的博文。

最后，我们仍然希望有更多的热爱OpenStack的朋友们加入我们公司，如果有意向的请与我联系

* 邮箱：xiaoquqi@gmail.com
* 新浪微博：@RaySun(http://weibo.com/xiaoquqi)
