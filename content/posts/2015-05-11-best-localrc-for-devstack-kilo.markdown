---
layout: post
title: "(Kilo)Devstack Kilo版本localrc推荐"
date: 2015-05-11 11:33:44 +0800
comments: true
categories: [openstack, cloud computing, devstack, kilo]
---

Devstack在Kilo版本中发生了一些变化，其中一个commit(279cfe75198c723519f1fb361b2bff3c641c6cef)的就是优化默认启动的程序，尽量减小对硬件的要求。如果不修改默认的配置进行安装，会产生一些问题，例如VNC无法打开，Heat模块没有加载等。这里给出一个个人比较常用的localrc，供大家参考。该配置在Ubuntu 14.04 Server LTS进行了测试。

<!-- more -->

该配置文件中开启了所有的OpenStack的核心模块，以下几点需要注意：

* 为了运行Neutron，服务器必须是双网卡，否则外网不会通
* 我的实验网段为200.21.0.0/16，eth0的IP为200.21.1.61，eth1与eth0为同一网段
* eth1为公网访问网络，floating网络范围200.21.50.1/24，配置的GATEWAY为200.21.50.2
* 保证eth1所处的网段能够连接外网，但是配置为manual模式，配置如下：

``` plain /etc/network/interface
auto eth1
iface eth1 inet manual
up ifconfig $IFACE 0.0.0.0 up
down ifconfig $IFACE 0.0.0.0 down
```
* localrc的配置

``` plain localrc
# Misc
ADMIN_PASSWORD=sysadmin
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD
SERVICE_TOKEN=$ADMIN_PASSWORD

# Target Path
DEST=/opt/stack.kilo

# Enable Logging
LOGFILE=$DEST/logs/stack.sh.log
VERBOSE=True
LOG_COLOR=True
SCREEN_LOGDIR=$DEST/logs

# Nova
enable_service n-novnc n-cauth

# Neutron
disable_service n-net
ENABLED_SERVICES+=,q-svc,q-agt,q-dhcp,q-l3,q-meta,neutron
ENABLED_SERVICES+=,q-lbaas,q-vpn,q-fwaas

# Ceilometer
enable_service ceilometer-acompute ceilometer-acentral ceilometer-anotification ceilometer-collector ceilometer-api
enable_service ceilometer-alarm-notifier ceilometer-alarm-evaluator

# Enable Heat
enable_service heat h-api h-api-cfn h-api-cw h-eng

# Trove
enable_service trove tr-api tr-tmgr tr-cond

# Sahara
enable_service sahara

#FIXED_RANGE=10.0.0.0/24
HOST_IP=200.21.1.61
FLOATING_RANGE=200.21.50.1/24
PUBLIC_NETWORK_GATEWAY=200.21.50.2
Q_FLOATING_ALLOCATION_POOL=start=200.21.50.100,end=200.21.50.150
```

* 确认br-ex是否存在
``` plain sudo ovs-vsctl show
Bridge br-ex
    Port br-ex
        Interface br-ex
            type: internal
    Port "qg-7ec5be02-69"
        Interface "qg-7ec5be02-69"
            type: internal
ovs_version: "2.0.2"
```

* 将eth1作为br-ex的接口
``` bash
sudo ovs-vsctl add-port br-ex eth1
```

``` plain sudo ovs-vsctl show
Bridge br-ex
    Port br-ex
        Interface br-ex
            type: internal
    Port "qg-7ec5be02-69"
        Interface "qg-7ec5be02-69"
            type: internal
    Port "eth1"
        Interface "eth1"
ovs_version: "2.0.2"
```
