---
layout: post
title: "(Kilo)Devstack完全用户手册"
date: 2015-09-03 18:34:20 +0800
comments: true
categories: [OpenStack, Devstack, Cloud Computing]
---

Devstack作为开发OpenStack必不可少的辅助环境搭建工具，其重要性不言而喻，但是由于网络上的原因，在使用中总是出现各种各样的问题，而且也不是所有人对使用上的细节非常清晰，所以想用这篇Blog总结一下在三年多的使用过程中的心得，来帮助将要走进OpenStack开发的志愿者们。下一篇博客我将为大家介绍Devstack的源代码，以及扩展插件的开发方法。

本篇Blog主要介绍以下几个实用场景：

* 如何利用Devstack构建一套完美的开发环境
* 提高Devstack安装成功率的方法
* Devstack的实用技巧
* 各种场景下的配置和注意事项

本篇博客提到的所有方法均在2015年9月4日使用stable/kilo branch得到验证，后续版本请持续关注本博客。

<!-- more -->

## 运行环境的选择

对于刚刚接触OpenStack的开发者而言，没有太多闲置的资源，所以比较容易的上手方式就是使用虚拟机。对于桌面的虚拟机软件来说，主流的软件无外乎VMWare Workstation和Oracle Virtualbox，对于OpenStack开发而言，二者并无太大差异。以下几点可能会作为选择的主要依据：

* VMWare Workstation是收费软件，Virtualbox是免费软件
* VMWare Workstation支持nested virtualization，就是安装完的devstack virt type是kvm，节省资源，Virtualbox安装以后只能使用qemu，虽然在Virtualbox 5以上版本号称支持，但是实际验证中仍然不能生效，还在研究中
* VMWare Workstation使用NAT方式时，内部的IP可以在HOST主机直接访问到，Virtualbox还需要端口转发，所以建议单独增加一块Host-only的Apdaptor便于调试
* 使用Virtualbox时，为了让虚拟机能够访问外部网络，并且允许Host通过Floating IP对虚拟机进行访问，需要在Host层面设置NAT规则，转换到可以访问的物理网卡上，详情请见下文

## Virtualbox网络设置

![](/images/blogs/devstack-guide-network-topology.jpg)

* Nova Network网卡配置

``` plain /etc/network/interface
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet static
address 192.168.56.101
netmask 255.255.255.0

auto eth2
iface eth1 inet static
address 172.16.0.101
netmask 255.255.255.0
```

* Neutron网卡配置

``` plain /etc/network/interface
auto eth0
iface eth0 inet dhcp

auto eth1
iface eth1 inet static
address 192.168.56.101
netmask 255.255.255.0

auto eth2
iface eth2 inet manual
up ip link set dev $IFACE up
down ip link set dev $IFACE down
```

* MAC网卡NAT映射

我们将第三块网卡作为提供外部网络的接口，采用系统层面的NAT方式让该网卡能够访问外部网络。

``` plain bash
sudo sysctl net.inet.ip.forwarding=1
```

在nat-anchor后面添加

``` plain /etc/pf.conf
nat on en0 from 172.16.0.0/24 -> (en0)
```

之后加载

``` bash bash
sudo pfctl -e -f /etc/pf.conf
```

* Linux网卡NAT映射

``` plain bash
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

## Devstack快速开始

其实，Devstack本身并不需要很复杂的配置就可以成功运行，但是仍然有几个需要注意的地方：

* Ubuntu 14.04 64bit(LTS), 12.04已经逐渐退出历史舞台，所以这里推荐14.04
* 不能使用root用户，即使你使用root用户执行Devstack，默认也会为你建立一个stack用户，所以不如老老实实的直接使用普通用户运行Devstack，或者提前建立好stack用户，切换后再执行
* 默认获取Devstack进行安装，安装的是master分支的代码，但是在实际开发中(比如我们做产品的时候)，都是基于某个stable分支进行，所以一般情况在clone devstack的时候需要指定stable分支

下面给出一个最简安装步骤：

``` plain
# adduser stack
# apt-get install sudo -y
# echo "stack ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# sudo su - stack

(stack)$ git clone https://git.openstack.org/openstack-dev/devstack --branch=stable/kilo
(stack)$ cd devstack && ./stack.sh
```

## 提高Devstack安装成功率

估计在国内使用Devstack的人基本都遇到过安装失败的状况，为了节约大家的时间，先分析一下Devstack为什么会失败，我们先从这张时序图看一下Devstack执行的过程：

![](/images/blogs/devstack-guide-flow.png)

从上述流程图中可以很清楚的看到Devstack有以下几个地方需要访问网络：

* 安装依赖时，需要访问Ubuntu的源
* 执行get_pip.sh时，地址是彻底被墙的，需要访问https://bootstrap.pypa.io/get-pip.py
* 从github clone源代码，github在国内访问速度并不很快而且间歇性被墙
* 安装过程中执行pip install requirements，需要访问pip repo
* 下载镜像，这一步骤取决于你需要安装的模块，如果默认安装只会下载cirros镜像，但是如果是安装类似Trove的模块，可能需要下载的更多

---

所以综上所述，为了提高devstack的安装成功率，需要从这几个方面着手优化：

* 使用国内源

``` plain /etc/apt/sources.list
deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
```

* 从国内源获取get-pip.py，从源代码可以分析出，检测get-pip.py的方式，这里面有两种方式一种是手动下载get-pip.py之后，注释代码，还有一种就是修改PIP_GET_PIP_URL的地址，但是这里只能通过修改install_pip.sh的方式，暂时无法从环境变量里获取

``` bash devstack/tools/install_pip.sh
FILES=$TOP_DIR/files

PIP_GET_PIP_URL=https://bootstrap.pypa.io/get-pip.py
LOCAL_PIP="$FILES/$(basename $PIP_GET_PIP_URL)"

function install_get_pip {
    # The OpenStack gate and others put a cached version of get-pip.py
    # for this to find, explicitly to avoid download issues.
    #
    # However, if DevStack *did* download the file, we want to check
    # for updates; people can leave their stacks around for a long
    # time and in the mean-time pip might get upgraded.
    #
    # Thus we use curl's "-z" feature to always check the modified
    # since and only download if a new version is out -- but only if
    # it seems we downloaded the file originally.
    if [[ ! -r $LOCAL_PIP || -r $LOCAL_PIP.downloaded ]]; then
        curl --retry 6 --retry-delay 5 \
            -z $LOCAL_PIP -o $LOCAL_PIP $PIP_GET_PIP_URL || \
            die $LINENO "Download of get-pip.py failed"
        touch $LOCAL_PIP.downloaded
    fi
    sudo -H -E python $LOCAL_PIP
}
```

修改为我在coding.net上缓存的get-pip脚本


``` bash devstack/tools/install_pip.sh
PIP_GET_PIP_URL=https://coding.net/u/xiaoquqi/p/pip/git/raw/master/contrib/get-pip.py
```

* 国内的代码托管服务器有从github上定期同步源代码的，但是经过实际测试都不是很理想，所以可能这是最不稳定的一部分，但是可以提前使用脚本，人工的下载所有代码，之后我会尝试在我自己的源中定时同步OpenStack源代码，敬请关注
* 现在pip的安装速度明显提升，原来还需要使用国内源，例如豆瓣，现在即使不修改也能很快的进行安装
* 镜像下载建议使用一些下载工具，然后放到指定的目录中，这样最有效

## 无网络状况下安装Devstack
因为我们是做OpenStack的产品的公司，所以就要求我们的Devstack要能够满足无网络状况下的安装，之前也写过一篇详细介绍无网络安装Devstack博客,由于时间关系，可能一些内容已经过时了，这里面再进行一下更新，思路还是上面的思路，这里给出一些使用的工具，如果不清楚如何使用的话，可以参考我之前的博客。

* 本地源的缓存使用apt-mirror，这是一个需要时间的工作，第一次同步的时间会非常长，准备好大约100G左右的空间吧
* 缓存get-pip.py，这个比较容易，搭建一个Apache服务器，但是需要把端口修改为10000，否则在安装好OpenStack后，会占用80端口，重新执行Devstack时候会出现错误
* 建立本地的Gerrit，并且上传所有代码
* 从requirements项目中，下载所有的pip，建立本地的pip缓存源，如果是搭建研发环境，可能还需要下载test-requirements的内容和tox
* 将镜像下载到刚刚创建的Apache服务器

完成以上步骤，你可以尽情断掉外网，愉快的进行Devstack的安装了，稍后我会将以上步骤进行进一步完善。

## OFFLINE模式下安装Devstack
在Devstack中提供了一种OFFLINE的方式，这种方式的含义就是，当你第一次完成安装后，所有需要的内容已经下载到本地，再次运行就没有必要访问网络了(前提是你不想升级)，所以可以将安装模式设置为OFFLINE，避免网络的访问，方法为：

``` bash devstack/localrc
OFFLINE=True
```

## 虚拟机重启后，如何利用rejoin-stack.sh，免重新安装
其实使用OFFLINE模式，可以在离线状态下无数次重新运行devstack，但是如果不是为了重新配置，我们并没有需要每次重新运行stack.sh。在Devstack中提供了另外一个脚本叫做rejoin-stack.sh，原理很简单就是把所有的进程重新组合进screen，所以我们借助这个脚本完全可以不重新执行stack.sh，快速恢复环境。但是当虚拟机重启后，cinder使用的卷组并不会自动重建，所以在运行rejoin之前，需要将恢复卷组的工作，放入开机启动的脚本中。

``` bash /etc/init.d/cinder-setup-backing-file
losetup /dev/loop1 /opt/stack/data/stack-volumes-default-backing-file
losetup /dev/loop2 /opt/stack/data/stack-volumes-lvmdriver-1-backing-file
exit 0
```

``` bash Run as root
chmod 755 /etc/init.d/cinder-setup-backing-file
ln -s /etc/init.d/cinder-setup-backing-file /etc/rc2.d/S10cinder-setup-backing-file
```

``` bash Run as normal user
cd $HOME/devstack
./rejoin-stack.sh
```

## Scenario 0: 公共部分
``` bash devstack/localrc
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
```

## Scenario 1: 单节点Nova-Network的安装

这应该就是Devstack默认的模式，有以下几点需要注意：

* 根据上面的网卡配置

> 第一块网卡为NAT方式，用于访问外部网络
>
> 第二块为Host-only Adaptor，用于访问云平台
>
> 第三块为Host-only Adaptor，用于虚拟机桥接网路
>
> 需要注意的是：这种方式下并不能让虚拟机正常访问外部网络，可以通过将eth2设置为Bridge模式，但是这样会造成DHCP冲突(如果外部网络有DHCP)，所以暂时没有完美的解决方案

* 打开novnc和consoleauth，否则无法访问VNC

这里给出的配置方案是第一种网络配置，即虚拟机无法网络外部网络的情况

``` bash devstack/localrc
# Nova
enable_service n-novnc n-cauth

FLAT_INTERFACE=eth1
# eth1 address
HOST_IP=192.168.56.101
FIXED_RANGE=172.24.17.0/24
FIXED_NETWORK_SIZE=254
FLOATING_RANGE=172.16.0.128/25
```

## Scenario 2: 双节点Nova-Network的安装

* 控制节点

``` bash devstack/localrc
# Nova
enable_service n-novnc n-cauth
disable_service n-cpu n-net n-api-meta c-vol

# current host ip
HOST_IP=192.168.56.101
FLAT_INTERFACE=eth1
MULTI_HOST=1
```

* 计算节点

``` bash devstack/localrc
# Nova
enable_service n-novnc n-cauth
ENABLED_SERVICES=n-cpu,n-net,n-api-meta,c-vol

# current host ip
HOST_IP=192.168.56.101
FLAT_INTERFACE=eth1
# needed by cinder-volume service
DATABASE_TYPE=mysql

# controller ip
SERVICE_HOST=192.168.56.101
MYSQL_HOST=$SERVICE_HOST
RABBIT_HOST=$SERVICE_HOST
GLANCE_HOSTPORT=$SERVICE_HOST:9292
NOVA_VNC_ENABLED=True
NOVNCPROXY_URL="http://$SERVICE_HOST:6080/vnc_auto.html"
VNCSERVER_LISTEN=$HOST_IP
VNCSERVER_PROXYCLIENT_ADDRESS=$VNCSERVER_LISTEN
```

## Scenario 3: 单节点Neutron的安装

* 基本配置

``` bash devstack/localrc
# Nova
enable_service n-novnc n-cauth

# Neutron
disable_service n-net
ENABLED_SERVICES+=,q-svc,q-agt,q-dhcp,q-l3,q-meta,neutron
ENABLED_SERVICES+=,q-lbaas,q-vpn,q-fwaas

HOST_IP=192.168.56.101
FIXED_RANGE=20.0.0.0/24
NETWORK_GATEWAY=20.0.0.1
FLOATING_RANGE=172.16.0.0/24
PUBLIC_NETWORK_GATEWAY=172.16.0.1
Q_FLOATING_ALLOCATION_POOL=start=172.16.0.101,end=172.16.0.200
```

* OVS设置

由于在Devstack安装过程中，将br-ex的地址也设置成了PUBLIC_NETWORK_GATEWAY的地址，但是实际使用过程中，我们建立的Host Apdator充当了gateway的角色，所以为了避免冲突，直接将br-ex地址清除掉。

``` bash bash
sudo ip addr flush dev br-ex
```

之后将eth2作为br-ex的port，之后创建的虚拟机就可以通过eth2访问网络了，Host也可以通过floating ip访问虚拟机了。

``` bash bash
sudo ovs-vsctl add-port br-ex eth2
```

## Scenario 4: 多节点Neutron的安装(控制/网络+计算节点)

* 控制/网络节点
``` plain devstack/localrc
# Nova
enable_service n-novnc n-cauth
HOST_IP=192.168.56.101
disable_service n-cpu n-net n-api-meta c-vol

# Neutron
disable_service n-net
ENABLED_SERVICES+=,q-svc,q-agt,q-dhcp,q-l3,q-meta
FIXED_RANGE=20.0.0.0/24
NETWORK_GATEWAY=20.0.0.1
FLOATING_RANGE=172.16.0.0/24
PUBLIC_NETWORK_GATEWAY=172.16.0.1
Q_FLOATING_ALLOCATION_POOL=start=172.16.0.101,end=172.16.0.200
```

* 计算节点
``` plain devstack/localrc
# Nova
disable_all_services
ENABLED_SERVICES=n-cpu,rabbit,neutron,q-agt,c-vol

# current host ip
HOST_IP=192.168.56.103
# needed by cinder-volume service
DATABASE_TYPE=mysql

# controller ip
SERVICE_HOST=192.168.56.101
MYSQL_HOST=$SERVICE_HOST
RABBIT_HOST=$SERVICE_HOST
GLANCE_HOSTPORT=$SERVICE_HOST:9292
NOVA_VNC_ENABLED=True
NOVNCPROXY_URL="http://$SERVICE_HOST:6080/vnc_auto.html"
VNCSERVER_LISTEN=$HOST_IP
VNCSERVER_PROXYCLIENT_ADDRESS=$VNCSERVER_LISTEN
Q_HOST=$SERVICE_HOST
```

* OVS设置

由于在Devstack安装过程中，将br-ex的地址也设置成了PUBLIC_NETWORK_GATEWAY的地址，但是实际使用过程中，我们建立的Host Apdator充当了gateway的角色，所以为了避免冲突，直接将br-ex地址清除掉。

``` bash bash
sudo ip addr flush dev br-ex
```

之后将eth2作为br-ex的port，之后创建的虚拟机就可以通过eth2访问网络了，Host也可以通过floating ip访问虚拟机了。

``` bash bash
sudo ovs-vsctl add-port br-ex eth2
```

## Scenario 5: 从源代码安装客户端

新的Devstack里面默认不再提供client的源代码的安装方式，需要使用localrc中的环境变量进行开启，否则将直接从master获取的client代码进行安装，当然这样会造成系统无法正常使用。那么如何才能确定client在当前Devstack可用的版本呢？最简单的方法可以先从pip中安装包，之后通过pip list | grep client的方式获取client的源代码。这里面提供我在Kilo中使用的版本依赖。

``` bash devstack/localrc
KEYSTONECLIENT_BRANCH=1.3.1
CINDERCLIENT_BRANCH=1.1.1
GLANCECLIENT_BRANCH=0.17.1
HEATCLIENT_BRANCH=0.4.0
NEUTRONCLIENT_BRANCH=2.4.0
NOVACLIENT_BRANCH=2.23.0
SWIFTCLIENT_BRANCH=2.4.0

# client code
LIBS_FROM_GIT=python-keystoneclient,python-glanceclient,python-novaclient,python-neutronclient,python-swiftclient,python-cinderclient
```

## Scenario 6: 安装Ceilometer/Heat/Trove/Sahara/Swift

``` bash devstack/localrc
# Ceilometer
enable_service ceilometer-acompute ceilometer-acentral ceilometer-anotification ceilometer-collector ceilometer-api
enable_service ceilometer-alarm-notifier ceilometer-alarm-evaluator

# Heat
enable_service heat h-api h-api-cfn h-api-cw h-eng

# Trove
enable_service trove tr-api tr-tmgr tr-cond

# Sahara
enable_service sahara

# Swift
enable_service s-proxy s-object s-container s-account
SWIFT_REPLICAS=1
SWIFT_HASH=011688b44136573e209e
```

## Scenario 7: 安装Ceph
``` bash devstack/localrc
# Ceph
ENABLED_SERVICES+=,ceph
CEPH_LOOPBACK_DISK_SIZE=200G
CEPH_CONF=/etc/ceph/ceph.conf
CEPH_REPLICAS=1

# Glance - Image Service
GLANCE_CEPH_USER=glance
GLANCE_CEPH_POOL=glance-pool

# Cinder - Block Device Service
CINDER_DRIVER=ceph
CINDER_CEPH_USER=cinder
CINDER_CEPH_POOL=cinder-pool
CINDER_CEPH_UUID=1b1519e4-5ecd-11e5-8559-080027f18a73
CINDER_BAK_CEPH_POOL=cinder-backups
CINDER_BAK_CEPH_USER=cinder-backups
CINDER_ENABLED_BACKENDS=ceph
CINDER_ENABLED_BACKENDS=ceph

# Nova - Compute Service
NOVA_CEPH_POOL=nova-pool
```

## Scenario 8: 安装Murano

想通过这个例子演示，对于一个新的OpenStack项目，如何使用Devstack尝鲜。

``` bash bash
cd /opt/stack.kilo
git clone https://github.com/openstack/murano --branch=stable/kilo
cd murano/contrib/devstack
cp lib/murano ${DEVSTACK_DIR}/lib
cp lib/murano-dashboard ${DEVSTACK_DIR}/lib
cp extras.d/70-murano.sh ${DEVSTACK_DIR}/extras.d
```

``` plain devstack/localrc
# Enable Neutron
ENABLED_SERVICES+=,q-svc,q-agt,q-dhcp,q-l3,q-meta,neutron

# Enable Heat
enable_service heat h-api h-api-cfn h-api-cw h-eng

# Enable Murano
enable_service murano murano-api murano-engine
```
