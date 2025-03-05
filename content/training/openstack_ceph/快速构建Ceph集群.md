---
title: 快速构建Ceph集群
author: 孙琦(Ray)
date: 2020-09-12 17:05:53
tags:
---
虽然安装环境并不是属于研发人员的本质工作，甚至有些研发人员抵触一些环境的搭建工作。在一些大型企业中，由于分工明确，造成了一些研发人员在这一方面能力的严重缺失。其实环境安装对于开发人员从整体上掌握软件架构师非常有益的，同时随着云计算、云原生的发展，对于DevOps的软件开发模式也越来越被企业接受，可以预见的是，未来DevOps将是所有研发人员必备的技能之一。

本文主要目标是帮助研发人员用最小成本搭建一套Ceph环境，为了降低搭建成本，使用了Ceph Deploy及国内源加速安装速度。我们选择目前Ceph Octopus最新的稳定版本进行安装。

<!-- more -->

## 部署架构

我们准备四台服务器，其中一台作为部署发起节点和后续Client节点使用。另外三台作为Ceph节点使用，其中第一台节点node01上，除了monitor和osd外，还将运行Manager, MDS和RGW服务，用于提供文件及对象存储服务。每一台Ceph节点都另外挂载了一块单独的磁盘，由于我使用的是虚拟机环境，所以挂载节点为/dev/vdb，如果使用是其他环境需要注意挂载点名称。

![upload successful](/images/pasted-58-1.png)

## 部署时序图

使用Ceph Deploy将大幅度简化安装过程，大体上分为以下安装步骤：

* 节点初始化配置
* Ceph Deploy节点安装
* Ceph集群初始化
* ODS节点安装、安装Mgr服务及添加ODS磁盘，完成Ceph基本安装
* CephFS安装，部署Metadata服务
* Ceph RGW安装，部署RGW服务

![upload successful](/images/pasted-59-1.png)

## （全部节点）环境准备

这是我非常常用的针对CentOS 7的设置，为了测试方便，关闭了防火墙、SELINUX，同时更新了系统和EPEL源为阿里源，最后进行系统更新，保证系统软件包更新到最新版本后，再进行环境安装。

```
## Set SELinux in permissive mode (effectively disabling it)
setenforce 0
##sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config
sed -i 's/^SELINUX=enforcing$/SELINUX=disabled/' /etc/selinux/config
 
systemctl stop NetworkManager
systemctl disable NetworkManager
 
systemctl status firewalld
systemctl stop firewalld
systemctl disable firewalld
systemctl status firewalld
firewall-cmd --state
 
curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum clean all && yum makecache
yum update -y
```

如果按照正常流程安装后，执行ceph -s，会出现restful模块无法找到，缺少pecan的安装包，所以在初始化阶段直接将缺少的包进行安装。

```
yum install -y python3-pip
pip3 install pecan werkzeug
```

## Ceph-Deploy节点安装

### （Ceph Deploy节点）安装Ceph-Deploy
```
cat << EOF > /etc/yum.repos.d/ceph.repo
[ceph-noarch]
name=Ceph noarch packages
baseurl=https://mirrors.aliyun.com/ceph/rpm-octopus/el7/noarch/
enabled=1
gpgcheck=1
type=rpm-md
gpgkey=https://mirrors.aliyun.com/ceph/keys/release.asc
EOF
```

```
yum makecache
yum install -y ceph-deploy
```
### （全部节点）设置时间同步服务

时间同步服务是分布式系统的生命线，所以安装时候先要安装NTP或者Chrony。在RHEL 7中，默认的时间同步被替换为Chrony，很多新的安装文档中也开始使用Chrony作为时间同步服务，但是NTP也被同时保留。我的环境中Chrony已经被安装并启动，如果没有请自行安装。

### （Ceph Deploy节点）无密码登录

这里为了简便，使用了root用户进行安装。配置完成后，需要让Ceph Deploy能够无密码的方式访问全部Ceph节点。

```
ssh-keygen
```

```
ssh-copy-id root@node1
ssh-copy-id root@node2
ssh-copy-id root@node3
```

## Ceph集群安装

### （Ceph Deploy节点）Ceph块存储服务安装

```
export CEPH_DEPLOY_REPO_URL=https://mirrors.aliyun.com/ceph/rpm-octopus/el7
export CEPH_DEPLOY_GPG_URL=https://mirrors.aliyun.com/ceph/keys/release.asc

## 集群初始化，这一步会生成初始化的ceph.conf，可以配置网络等信息
ceph-deploy new node01
ceph-deploy install node01 node02 node03

## 初始化monitor，并收集keys
ceph-deploy mon create-initial
ceph-deploy admin node01 node02 node03

ceph-deploy mgr create node01

ceph-deploy osd create --data /dev/vdb node01
ceph-deploy osd create --data /dev/vdb node02
ceph-deploy osd create --data /dev/vdb node03

## 检查集群状态
ceph -s
```

由于默认采用了Bluestore安装方式，如果想使用SSD作为block.db和block.wal，可以这样创建OSD

```
ceph-deploy osd create --data /dev/vdb --block-db /dev/vdc --block-wal /dev/vdc node01
```

在Ceph Deploy节点，将Ceph相关配置文件拷贝至系统的/etc/ceph目录

```
mkdir -p /etc/ceph
cp ceph.conf /etc/ceph
cp ceph.client.admin.keyring /etc/ceph
```

#### （Ceph Deploy节点）增加多个Monitor节点

添加多个Monitor节点，可以实现高可靠，但是一定为奇数。先更新配置文件，在刚才初始化集群目录下的ceph.conf中的mon_host添加所有节点IP，之后设定public network，这里我们使用了Ceph节点的网段：

```
## ceph.conf
## ...
mon_host = 192.168.10.105,192.168.10.176,192.168.10.139
public network = 192.168.10.1/24
## ...
```

分发配置文件

```
ceph-deploy --overwrite-conf admin node01 node02 node03
ceph-deploy mon add node02
ceph-deploy mon add node03


## 检查quorum状态
ceph quorum_status --format json-pretty
```


### （Ceph Deploy节点）Ceph文件系统服务安装

```
ceph-deploy mds create node01


## 添加多个Manager服务，Manager采用的是主从模式
ceph-deploy mgr create node02 node03

## 可以看到Manager主从节点状态
ceph -s
```

如果发现Ceph Monitor节点启动失败，需要到相应的节点上查看失败原因，比如我的Monitor使用Start启动，返回这样的提示

```
Job for ceph-mon@node02.service failed because start of the service was attempted too often. See "systemctl status ceph-mon@node02.service" and "journalctl -xe" for details.
To force a start use "systemctl reset-failed ceph-mon@node02.service" followed by "systemctl start ceph-mon@node02.service" again.
```

按照提示重新启动即可

```
systemctl reset-failed ceph-mon@node02.service
systemctl start ceph-mon@node02.service
```

### （Ceph Deploy节点）Ceph对象存储服务安装

```
ceph-deploy rgw create node01
```

## 测试

### 块存储测试

#### 建立存储空间

```

```

#### 挂载使用

### 文件系统测试


#### 建立存储空间

```
ceph osd pool create cephfs_data 16
ceph osd pool create cephfs_metadata 16

## ceph fs new <fs_name> <metadata> <data>
ceph fs new cephfs cephfs_metadata cephfs_data
ceph fs ls
```

#### 内核方式挂载

```
mkdir -p /mnt/mycephfs
mount -t ceph 192.168.10.11:6789:/ /mnt/mycephfs -o name=admin,secretfile=/etc/ceph/admin.secret
```

#### Fuse方式挂载

确保/etc/ceph下面已经拷贝了ceph.conf和keyring文件

```
mkdir -p /mnt/mycephfs
ceph-fuse -m 192.168.10.11:6789 /mnt/mycephfs
```

### 对象存储测试