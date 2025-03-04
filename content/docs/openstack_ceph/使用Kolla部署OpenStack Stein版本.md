---
title: 使用Kolla部署OpenStack Stein版本
author: 孙琦(Ray)
tags:
  - OpenStack
  - 云计算
categories: []
date: 2020-10-30 22:15:00
---
开源版本的OpenStack+Ceph的组合已经日趋稳定，所以搭建一朵私有云环境的难度在逐步降低。当然OpenStack安装问题其实一直没有得到有效的解决，学习曲线非常陡峭。本文主要介绍基于Kolla项目使用容器化快速部署OpenStack方法，该部署方法已经在内部环境得到了多次验证，安装简便容易维护。

<!-- more -->


## 1、云平台规划

在实际环境中，我们在一台2U的超微四子星服务器上进行了部署。由于是内部使用的研发环境，为了节约成本，我们并没有部署高可靠方案，而是采用了一台作为控制节点+计算节点+存储节点，另外三台作为计算节点+存储节点的方式进行部署。

由于OpenStack最新的Ussari在使用Kolla部署时，不再支持CentOS 7版本，所以这里我们选定了上一个稳定版本Stein版本进行部署。

### 硬件配置

硬件名称 | 配置规格 | 备注
--------- | ------------- | -------------
CPU | Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz	x 2 | 共40线程
内存 | DDR4 2400 MHz 64GB	|
硬盘 | 板载64 GB x 1 <br/> 240 GB Intel SSD x 1 <br/> 1.2 TB SAS x 5 | 经过测试，由于板载64GB空间过小，在控制节点需要损失一块SAS盘空间用于root分区挂载
网卡 | 千兆 x 4 <br/> 万兆 x 4 <br/> IPMI x 1|

#### 分区规划

| 磁盘 | 规划 | 备注 |
| -- | -- | -- |
| 64G | 系统盘 | 不要使用LVM分区 |
| SSD 240G | Ceph Journal<br> | 1块盘 |
| SAS 1.2 T | Ceph OSD | 5块盘 |


### 网络规划

#### 交换机配置

* 我们默认采用了VLAN模式，所以无须在交换机上进行Trunk配置

#### 网络规划

| 网卡 | 网络类型 | VLAN ID | 网段 | 说明 | 网关 | 备注 |
| -- | -- | -- | -- | -- | -- | -- |
|  | 管理网络 | 3 | 192.168.10.0/24 | OpenStack管理 | 192.168.10.1 | 192.168.10.201 - 204 |
|  | 存储网络 |  | 10.0.100.0/24 | Ceph网络 | 无需网关 | 10.0.100.201 -&nbsp;204 |
|  | External网络 | 3 | 192.168.10.0/24 | External网络 | 192.168.10.1 | 可分配地址192.168.10.100 - 192.168.10.200 |
|  | Tunnel网络 |  | 172.16.100.0/24 | VxLAN通讯网络 | <br data-mce-bogus="1"> | 172.16.100.201 - 204 |
| console | IPMI | 4 | 192.168.10.0/24 |  |  | 与管理网地址一一对应, 192.168.10.201 |

#### 网卡配置

| 主机名 | em1(管理网地址) | em2(存储网) | em3(External网络) | em4(Tunnel网络) | 备注 |
| -- | -- | -- | -- | -- | -- |
| control201 | 192.168.10.201 | 10.0.100.201 | <pre style="line-height: 1.42857;"><span class="na">DEVICE</span><span class="o">=</span><span class="s">INTERFACE_NAME</span><br><span class="na">TYPE</span><span class="o">=</span><span class="s">Ethernet</span><br><span class="na">ONBOOT</span><span class="o">=</span><span class="s">"yes"</span><br><span class="na">BOOTPROTO</span><span class="o">=</span><span class="s">"none"</span></pre> | 172.16.100.201 |  |
| compute202 | 192.168.10.202 | 10.0.100.202 | <pre style="line-height: 1.42857;"><span class="na">DEVICE</span><span class="o">=</span><span class="s">INTERFACE_NAME</span><br><span class="na">TYPE</span><span class="o">=</span><span class="s">Ethernet</span><br><span class="na">ONBOOT</span><span class="o">=</span><span class="s">"yes"</span><br><span class="na">BOOTPROTO</span><span class="o">=</span><span class="s">"none"</span></pre> | 172.16.100.202 |  |
| compute203 | 192.168.10.203 | 10.0.100.203 | <pre style="line-height: 1.42857;"><span class="na">DEVICE</span><span class="o">=</span><span class="s">INTERFACE_NAME</span><br><span class="na">TYPE</span><span class="o">=</span><span class="s">Ethernet</span><br><span class="na">ONBOOT</span><span class="o">=</span><span class="s">"yes"</span><br><span class="na">BOOTPROTO</span><span class="o">=</span><span class="s">"none"</span></pre> | 172.16.100.203 |  |
| compute204 | 192.168.10.204 | 10.10.20.204 | <pre style="line-height: 1.42857;"><span class="na">DEVICE</span><span class="o">=</span><span class="s">INTERFACE_NAME</span><br><span class="na">TYPE</span><span class="o">=</span><span class="s">Ethernet</span><br><span class="na">ONBOOT</span><span class="o">=</span><span class="s">"yes"</span><br><span class="na">BOOTPROTO</span><span class="o">=</span><span class="s">"none"</span></pre> | 172.16.100.203 |  |

### OpenStack规划

#### 安装组件

Ceph采用单独安装方式，这目前也是Kolla项目主推的方式，在U版本中已经彻底不支持通过Kolla安装Ceph了。我们主要安装OpenStack核心模块，另外安装的是日志收集ELK的相关模块，便于运维。

* Horizon
* Nova
* Keystone
* Cinder
* Glance
* Neutron
* Heat

## 2、部署准备

### 部署架构图

![upload successful](/images/pasted-60.png)

### 服务器前期准备

* BIOS配置：在BIOS中打开VT，并且正确配置IPMI地址，方便远程管理
* RAID配置：所有磁盘需要配置成NON-RAID模式
* 操作系统安装：
    * 使用CentOS 7光盘进行最小化安装
    * 不要使用LVM分区
    * 配置主机名
    * 配置第一块网卡，并配置自动启动
    
### 网卡配置

#### em1
```
cat << EOF > /etc/sysconfig/network-scripts/ifcfg-em1
TYPE=Ethernet
BOOTPROTO=static
NAME=em1
DEVICE=em1
ONBOOT=yes
IPADDR=192.168.10.201
NETMASK=255.255.255.0
GATEWAY=192.168.10.1
DNS1=114.114.114.114
EOF
```

#### em2
```
cat << EOF > /etc/sysconfig/network-scripts/ifcfg-em2
TYPE=Ethernet
BOOTPROTO=static
DEFROUTE=yes
NAME=em2
DEVICE=em2
ONBOOT=yes
IPADDR=10.0.100.201
NETMASK=255.255.255.0
EOF
```

#### em3
```
cat << EOF > /etc/sysconfig/network-scripts/ifcfg-em3
TYPE=Ethernet
BOOTPROTO=static
NAME=em3
DEVICE=em3
ONBOOT=yes
IPADDR=172.16.100.201
NETMASK=255.255.255.0
EOF
```

#### em4
```
cat << EOF > /etc/sysconfig/network-scripts/ifcfg-em4
TYPE=Ethernet
BOOTPROTO=none
NAME=em4
DEVICE=em4
ONBOOT=yes
EOF
```


## 3、安装步骤


### 3.1 准备部署节点

该节点承担了后续所有的部署流程，该节点可以作为OpenStack控制节点复用，包括运行OpenStack Kolla和Ceph Deploy。

注意：节点之间可以通过密码或者密钥方式进行访问，附录中提供了自动上传密钥的方式，建议在正式安装前配置完成，这里不提供自动化配置方法。

#### 下载初始化脚本

目前已经将常用的操作写成了Ansible脚本。

```
yum install -y git
git clone https://github.com/xiaoquqi/my_ansible_playbooks

cd my_ansible_playbooks
prepare_on_centos7.sh
```

#### 修改hosts.ini文件

修改hosts.ini文件来初始化所有节点

```
## my_ansible_playbooks/hosts.ini
compute201 ansible_host=192.168.10.201 ip=192.168.10.201 ansible_user=root
compute202 ansible_host=192.168.10.202 ip=192.168.10.202 ansible_user=root
compute203 ansible_host=192.168.10.202 ip=192.168.10.203 ansible_user=root
compute204 ansible_host=192.168.10.202 ip=192.168.10.204 ansible_user=root
```


#### 初始化节点

该步骤主要包含了，更新软件，修改主机名，增加/etc/hosts等操作。

```
./run_ansible.sh playbooks/bootstrap_centos7.yml
./run_ansible.sh playbooks/change_hostname.yml
./run_ansible.sh playbooks/update_etc_hosts.yml
./run_ansible.sh playbooks/install_docker.yml

## 安装pip和系统环境下的python docker模块，否则在precheck的时候会发现没有安装docker模块
./run_ansible.sh playbooks/install_pip2_package.yml
```

#### 安装Ceph Deploy

```
yum install -y python3-pip
pip3 install pecan werkzeug
```

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


#### 安装Kolla

由于Python Warning的提示信息导致在安装时出现如下错误，需要增加忽略Python Warning的环境变量，具体修复信息如下：https://bugs.launchpad.net/kolla-ansible/+bug/1888657

目前通过pip方式还没有8.2.1这个release，所以kolla的安装从源代码中进行。

```
Ansible 2.2.0.0 used in Stein kolla-toolbox requires paramiko (no version
constraints), which installs latest cryptography package. It results in
Python deprecation warning about Python 2:

/usr/lib64/python2.7/site-packages/cryptography/__init__.py:39: CryptographyDeprecationWarning: Python 2 is no longer supported by the Python core team. Support for it is now deprecated in cryptography, and will be removed in a future release.

This warning breaks kolla_toolbox module.
```

```
sudo yum -y install python-devel libffi-devel gcc openssl-devel libselinux-python

git clone https://github.com/openstack/kolla-ansible --branch stable/stein
cd kolla-ansible
pip install . --ignore-installed PyYAML

## 虚拟环境还需要再安装一次ansible，否则kolla-ansible会提示
## ERROR: kolla_ansible has to be available in the Ansible PYTHONPATH.
## Please install both in the same (virtual) environment.
pip install 'ansible<2.10'

mkdir -p /etc/kolla
cp -r $VENV_HOME/share/kolla-ansible/etc_examples/kolla/* /etc/kolla

mkdir -p /root/kolla
cp $VENV_HOME/share/kolla-ansible/ansible/inventory/* /root/kolla
```

生成密码，如果需要指定密码，可以到/etc/kolla/password.yml中修改。

```
kolla-genpwd
```

### 3.2 部署Ceph

#### 部署

之前有一篇软文详细介绍了使用Ceph Deploy部署Ceph的方法，这里不再赘述，下面直接给出部署命令，这里我们只部署块服务。

```
mkdir -p /root/ceph
cd /root/ceph

export CEPH_DEPLOY_REPO_URL=https://mirrors.aliyun.com/ceph/rpm-octopus/el7
export CEPH_DEPLOY_GPG_URL=https://mirrors.aliyun.com/ceph/keys/release.asc

## 如果阿里源无法使用，可以使用163源，并且可以通过指定rpm-octopus，指定安装的Ceph版本
##export CEPH_DEPLOY_REPO_URL=https://mirrors.163.com/ceph/rpm-octopus/el7
##export CEPH_DEPLOY_GPG_URL=https://mirrors.163.com/ceph/keys/release.asc

## 集群初始化，这一步会生成初始化的ceph.conf，可以配置网络等信息
##
## 如果cluster-network和public-network需要分开，可以这样定义：
## ceph-deploy new --cluster-network 172.31.6.0/24 --public-network 192.168.4.0/24 node1 node2 node3

ceph-deploy new --public-network 10.0.100.0/24 compute201
ceph-deploy install compute201 compute202 compute203 compute204

## 初始化monitor，并收集keys
ceph-deploy mon create-initial
ceph-deploy admin compute201 compute202 compute203 compute204

ceph-deploy mgr create compute201

## 需要根据实际情况修改，这里模拟的是将RocksDB存放至单独的SSD磁盘，目前文档中并没有特别指出这部分的分配比例，所以DB和WAL都是分配10G，写入的基本顺序为WAL -> DB -> DATA

pvcreate /dev/vdb
vgcreate ceph-pool /dev/vdb

## 每个OSD分配
lvcreate -n osd0.wal -L 10G ceph-pool
lvcreate -n osd0.db -L 10G ceph-pool
ceph-deploy osd create --data /dev/vdd --block-db ceph-pool/osd0.db --block-wal ceph-pool/osd0.wal compute201

## 检查集群状态
ceph -s
```

#### 生成配置文件

为Glance/Nova/Cinder创建资源池并生成鉴权文件

```
ceph osd pool create images 128
ceph auth get-or-create client.glance mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=images' -o /etc/ceph/ceph.client.glance.keyring

ceph osd pool create volumes 128
ceph auth get-or-create client.cinder mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=volumes, allow rx pool=images' -o /etc/ceph/ceph.client.cinder.keyring

ceph osd pool create backups 128
ceph auth get-or-create client.cinder-backup mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=backups' -o /etc/ceph/ceph.client.cinder-backup.keyring

ceph osd pool create vms 128
ceph auth get-or-create client.nova mon 'allow r' osd 'allow class-read object_prefix rbd_children, allow rwx pool=vms, allow rx pool=images' -o /etc/ceph/ceph.client.nova.keyring
```

注意：

### 3.3 OpenStack部署

#### kolla配置文件

##### /etc/kolla/globals.yml

```
kolla_base_distro: "centos"
kolla_install_type: "source"
openstack_release: "stein"
kolla_internal_vip_address: "192.168.10.123"

docker_registry: registry.cn-beijing.aliyuncs.com
docker_namespace: "openstack-dockers"

network_interface: "eth0"
storage_interface: "eth1"
tunnel_interface: "eth3"
neutron_external_interface: "eth2"

openstack_logging_debug: "True"
enable_haproxy: "no"
enable_ceph: "no"
enable_cinder: "yes"
enable_cinder_backup: "yes"
enable_fluentd: "no"
enable_openstack_core: "yes"
glance_backend_ceph: "yes"
glance_backend_file: "no"
glance_enable_rolling_upgrade: "no"
cinder_backend_ceph: "yes"
nova_backend_ceph: "yes"
```

##### multinode

```
[control]
compute201 ansible_host=192.168.10.123 ip=192.168.10.123 ansible_user=root

[network]
compute201 ansible_host=192.168.10.123 ip=192.168.10.123 ansible_user=root
compute202 ansible_host=192.168.10.160 ip=192.168.10.160 ansible_user=root

[compute]
compute201 ansible_host=192.168.10.123 ip=192.168.10.123 ansible_user=root
compute202 ansible_host=192.168.10.160 ip=192.168.10.160 ansible_user=root

[monitoring]
compute201 ansible_host=192.168.10.123 ip=192.168.10.123 ansible_user=root

[storage]
compute201 ansible_host=192.168.10.123 ip=192.168.10.123 ansible_user=root
compute202 ansible_host=192.168.10.160 ip=192.168.10.160 ansible_user=root
```

#### 定制服务配置文件

##### Ceph Glance

```
mkdir -p /etc/kolla/config/glance
tee /etc/kolla/config/glance/glance-api.conf << EOF
[glance_store]
stores = rbd
default_store = rbd
rbd_store_pool = images
rbd_store_user = glance
rbd_store_ceph_conf = /etc/ceph/ceph.conf
EOF
```

```
cp /etc/ceph/ceph.conf /etc/kolla/config/glance/ceph.conf
cp /etc/ceph/ceph.client.glance.keyring /etc/kolla/config/glance/ceph.client.glance.keyring
```

##### Ceph Cinder

cinder_rbd_secret_uuid是在passwords.yml中生成的。

```
mkdir -p /etc/kolla/config/cinder
mkdir -p /etc/kolla/config/cinder/cinder-volume
mkdir -p /etc/kolla/config/cinder/cinder-backup

export cinder_rbd_secret_uuid=$(grep cinder_rbd_secret_uuid /etc/kolla/passwords.yml | awk '{print $2}')

tee /etc/kolla/config/cinder/cinder-volume.conf << EOF
[DEFAULT]
enabled_backends=rbd-1

[rbd-1]
rbd_ceph_conf=/etc/ceph/ceph.conf
rbd_user=cinder
backend_host=rbd:volumes
rbd_pool=volumes
volume_backend_name=rbd-1
volume_driver=cinder.volume.drivers.rbd.RBDDriver
rbd_secret_uuid = $cinder_rbd_secret_uuid
EOF
```

```
tee /etc/kolla/config/cinder/cinder-backup.conf << EOF
[DEFAULT]
backup_ceph_conf=/etc/ceph/ceph.conf
backup_ceph_user=cinder-backup
backup_ceph_chunk_size = 134217728
backup_ceph_pool=backups
backup_driver = cinder.backup.drivers.ceph.CephBackupDriver
backup_ceph_stripe_unit = 0
backup_ceph_stripe_count = 0
restore_discard_excess_bytes = true
EOF
```

所有文件必须命名为ceph.client*

```
cp /etc/ceph/ceph.conf /etc/kolla/config/cinder/ceph.conf
cp /etc/ceph/ceph.client.cinder.keyring /etc/kolla/config/cinder/cinder-volume/ceph.client.cinder.keyring
cp /etc/ceph/ceph.client.cinder.keyring /etc/kolla/config/cinder/cinder-backup/ceph.client.cinder.keyring
cp /etc/ceph/ceph.client.cinder-backup.keyring /etc/kolla/config/cinder/cinder-backup/ceph.client.cinder-backup.keyring
```

##### Ceph Nova

```
mkdir -p /etc/kolla/config/nova

tee /etc/kolla/config/nova/nova-compute.conf << EOF
[libvirt]
images_rbd_pool=vms
images_type=rbd
images_rbd_ceph_conf=/etc/ceph/ceph.conf
rbd_user=nova
EOF
```

```
cp /etc/ceph/ceph.conf /etc/kolla/config/nova/ceph.conf
cp /etc/ceph/ceph.client.nova.keyring /etc/kolla/config/nova/ceph.client.nova.keyring
cp /etc/ceph/ceph.client.cinder.keyring /etc/kolla/config/nova/ceph.client.cinder.keyring

```

#### 检查

```
## 初始化节点，与上述我们自己的初始化有重复之处
kolla-ansible -i multinode bootstrap-servers

kolla-ansible -i multinode prechecks

## 拉取所有镜像
kolla-ansible -i multinode pull
```

#### 部署

```
kolla-ansible -i multinode deploy
kolla-ansible -i multinode post-deploy
```


## 附录


### 节点互信

节点之间互信建议采用key方式，这里并没有实现完全自动化手段，需要首先在控制节点上生成公钥和私钥。

```
ssh-keygen
```

然后将~/.ssh/id_rsa.pub文件拷贝至可以正常访问两台节点的环境中的playbooks/keys目录下，再更新所有节点。

```
./run_ansible.sh playbooks/update_authorized_keys.yml
```

### 部署出错如何调试

如果在部署中出现任何错误，可以添加更多的Verbose来判断具体问题，有可能是kolla自身bug，也有可能是配置的问题，具体可以根据详细输出进行判断。

```
kolla-ansible -vvv -i multinode deploy
```