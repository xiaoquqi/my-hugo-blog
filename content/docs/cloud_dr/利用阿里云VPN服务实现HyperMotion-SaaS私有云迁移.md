---
title: 利用阿里云VPN服务实现HyperMotion SaaS私有云迁移
author: 孙琦(Ray)
date: 2021-02-10 10:35:16
tags:
---
目前云原生迁移平台HyperMotion SaaS主要应用场景在公有云上，但是在我们平时的测试场景中，由于上行带宽的限制，每次向公有云同步比较消耗时间，特别是在验证启动流程时，需要等待半天到一天的时间进行数据同步，非常不划算。在我们内部环境中，我们经常测试的一种场景是从VMWare迁移到私有化部署的OpenStack上。但是由于网络的限制不可能将OpenStack及Floating IP资源在公网上一一映射（如果是客户场景，通常是私有化部署的HyperMotion解决）。那么，是否可以将线上VPC与本地的机房网络环境利用VPN隧道打通，实现利用HyperMotion SaaS进行私有云环境的迁移呢？本文就为你分享利用阿里云VPN服务实现上述场景的需求。

<!-- more -->

## 需求与场景分析

HyperMotion SaaS是部署在阿里云Kubernetes托管版集群中，即Kubernetes Master节点由阿里云负责，阿里云为我们在指定VPC内启动了两台ECS实例作为Worker节点。在我们自身需求中，需要解决两个流量问题：

* 控制流：HyperMotion SaaS每个租户可以添加指定的目标云平台，HyperMotion SaaS后台模块通过VPC关联的NAT网关访问云平台API接口及资源，但是如果添加的是我们内部的OpenStack，则需要SaaS侧与OpenStack控制网络想通；另外HyperMotion会自动利用云平台的云主机资源安装云存储网关，所以也需要访问OpenStack Floating IP的地址（具体看云平台规划，也许是Fixed IP）。
* 数据流：在数据层面上，我们仍然希望数据层面通过内网传输，没有必要将数据流入公网，好在HyperMotion SaaS的设计满足了这样的需求

![upload successful](/images/pasted-133.png)

所以在这个解决方案中，重点是利用阿里云VPN网关和本地打通后（前提是公司出口路由有固定的公网IP），通过合理的设置路由规则实现我们上述的需求。

注意：文章中使用的截图并非全部都是真实截图，所以在实际配置过程中要根据实际情况进行。

## 配置流程

配置过程中主要涉及阿里云VPN服务和H3C路由器，基本流程如下：

* 1、阿里云建立VPN网关，这个最低购买力度是包月
* 2、拿到阿里云VPN网关后，在路由器上进行相关配置
* 3、回到阿里云配置用户网关及IPsec连接，查看连接是否成功
* 4、阿里云侧路由设置

## 1、阿里云VPN网关配置

VPN需要关联到VPC和交换机上，根据带宽的不同，价格也不同，最低是按照包1个月5 Mbps。

![upload successful](/images/pasted-147.png)

配置好后，会得到一个公网IP，这个公网IP需要在后续配置到路由器上。

![upload successful](/images/pasted-134.png)


## 2、H3C路由器设置

目前我们机房使用的路由器属于非常入门级的企业级路由器（H3C ER3200G2），但是基本能满足我们的需求了，并且支持IPsec VPN方式。之前一直很惧怕配置IPsec VPN，相较于L2TP等简单方案，配置起来太复杂了。但是经过几次折腾，也基本摸清楚是怎么回事了，真是应了那句话：人类的恐惧来自于无知。

我并不是网络方面的专家，也对IPsec原理没什么研究，我只想记录一下我是怎么配置的。我认为IPsec在配置的时候，最重要的一点是两头配置一样，无法连接往往是由于配置信息不一致导致的。这是一张原理图，加深我们对配置过程的理解。

![upload successful](/images/pasted-143.png)

H3C配置的基本流程为：虚接口->IKE安全提议->IKE对等体->IPsec安全提议->IPsec安全策略。

### 2.1、虚接口配置

虚接口应该是定义与外界互连的通道，配置很简单，只要指明对外服务的接口（比如：WAN1）就可以了。

![upload successful](/images/pasted-134.png)

### 2.2、IKE安全提议

IKE是因特网密钥交换的缩写(Internet Key Exchange)，从名字上可以猜出这与互联网进行交换数据时加密有关。验证算法和加密算法一定要与对端配置一致，关于DH组，每一个平台选项不一样，比如截图中叫DH2 modp1024，到了阿里云就叫做group2了，所以也必须要配置一致。

![upload successful](/images/pasted-139.png)

阿里云侧DH组选项

![upload successful](/images/pasted-140.png)

### 2.3、IKE对等体

和对端的VPN网关进行连接，对端IP是需要首先在对端建立VPN网关后，会得到相应的地址，填入即可。

![upload successful](/images/pasted-141.png)

协商模式上，阿里云的配置是英文的，主模式叫做main，而野蛮模式被称为aggresive。

![upload successful](/images/pasted-142.png)

共享密钥是自定义的，两端必须一致，DPD阿里云默认是开启的，而H3C上是关闭的，保持统一即可。

### 2.4、IPsec安全提议

按照我粗浅的认知，IKE主要负责两端连接，同时简化了IPsec交互，而真正的数据交互还是要在IPsec上进行控制。所以要对IPsec也要进行相应的安全配置。安全协议类型，我们选择了默认的ESP，阿里云侧默认也应该采用的是此协议。在配置对端时，仍然是保持一致即可。

![upload successful](/images/pasted-144.png)

### 2.5、IPsec安全策略

这一步最关键的是本地子网IP和对端子网IP及掩码的设置，双方是相反的，如果本地是192.168.0.0/24，源端是172.16.0.0/24。则在阿里云侧的配置就是本地是172.16.0.0/24，远端是192.168.0.0/24。

![upload successful](/images/pasted-145.png)

还有一个就是PFS的设置，和IKE的DH组是一样的，在阿里云侧也被称为IPsec的DH组。也必须设置一致。

![upload successful](/images/pasted-146.png)

## 3、阿里云IPsec连接配置

### 3.1、用户网关设置

用户网关设置比较简单，只要在阿里云测配置你路由的公网IP即可。

![upload successful](/images/pasted-149.png)

### 3.2、IPsec连接

这是最关键的一步，经常在这一步配置失败，提示在第一阶段或者第二阶段失败，目前在我遇到的情况中，基本都是上述配置不一致导致的。配置过程基本分为三个阶段，基本配置、高级配置中的IKE配置和IPsec配置。

#### 3.2.1 基本配置

注意图中标出的本端网络、对端网络和预共享密钥的配置，一定要填对。

![upload successful](/images/pasted-150.png)

#### 3.2.2 IKE配置

点开下方的高级设置，能够看到IKE和IPsec设置。

配置只要按照我们在H3C的配置选择相应的内容即可，LocalId和RemoteId都是自动根据VPN填写的，并不需要输入。

![upload successful](/images/pasted-151.png)

#### 3.2.3 IPsec配置

图中标注的选项一定要保持一致，提交配置后，等待连接。

![upload successful](/images/pasted-152.png)

### 3.3、查看连接状态

如果连接状态为第二阶段协商成功，就证明VPN已经建立成功，否则请检查配置，多半是由于配置不一致导致的。

![upload successful](/images/pasted-153.png)

## 4、设置路由

我们次此设置路由的目的是为了阿里云侧能够访问我们内网，所以接下来需要在阿里云VPC内设置路由表，当访问我们的内网时，需要使用VPN网关。进入VPC服务的路由表配置中，找到VPC。将目标IP段吓一跳设置为VPN网关。因为阿里云的ACL还处于内测阶段，所以暂时无须考虑ACL的设定。

![upload successful](/images/pasted-154.png)

## 总结

网络对于未来混合云的场景有至关重要的作用，本文重点描述的是以VPN方式来打通云上和云下环境，但是VPN最大的带宽规格只有200 Mbps，如果真实的需求更大，则需要考虑云联网，通过运营商底层基础设施，实现不同云之间的互联互通。