---
title: CentOS 7和Docker初始化安装
author: 孙琦(Ray)
tags:
  - 常用命令
  - CentOS
  - Docker
categories: []
date: 2020-07-31 09:34:00
---
## CentOS 7初始化

该安装脚本为搭建研发环境常用的脚本，记录在Blog中便于查阅。

<!-- more -->

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

## Docker国内源安装

```
## Install Docker
curl -sSL https://get.daocloud.io/docker | sh -s -- "--mirror" "Aliyun"
 
## Replace docker repo
mkdir -p /etc/docker
cat > /etc/docker/daemon.json <<EOF
{
  "registry-mirrors": ["https://6m7d428u.mirror.aliyuncs.com"],
  "dns": ["114.114.114.114"],
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2",
  "storage-opts": [
    "overlay2.override_kernel_check=true"
  ]
}
EOF
 
systemctl enable docker && systemctl daemon-reload && systemctl restart docker
 
curl -L https://get.daocloud.io/docker/compose/releases/download/1.28.4/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```
