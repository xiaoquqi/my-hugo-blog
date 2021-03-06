---
title: 云迁移SaaS如何入驻阿里云工具应用市场
slug: how-to-join-cloud-migration-saas-into-aliyun-marketplace
aliases:
  - /2021/12/01/%E4%BA%91%E8%BF%81%E7%A7%BBsaas%E5%A6%82%E4%BD%95%E5%85%A5%E9%A9%BB%E9%98%BF%E9%87%8C%E4%BA%91%E5%B7%A5%E5%85%B7%E5%BA%94%E7%94%A8%E5%B8%82%E5%9C%BA/
date: 2021-12-01T09:08:17+08:00
draft: false
tags:
  - 阿里云
  - HyperMotion
  - 云迁移
  - 云灾备
---

HyperMotion SaaS是一款基于云原生理念开发的云迁移和云灾备的SaaS平台，2020年7月，HyperMotion迁移版本正式入驻阿里云工具应用市场。用户登陆阿里云后，可以直接以SaaS模式使用产品，而无须再到云市场启动实例的方式。由于与阿里云的用户体系、RAM系统、支付系统彻底打通，用户在使用感受上更加便捷。同样，借助阿里云的流量优势，HyperMotion SaaS在入驻一年多的时间里，在无特别运营和推广的前提下，获得了将近400个客户的自然流量。阿里云应用工具市场无疑是对阿里云被集成理念的最好诠释，也为IaaS SaaS软件提供了非常好的土壤。本文就从技术角度分享一下入驻阿里云应用工具市场的全过程。

<!-- more -->

## 用户体验

### 使用感受

先来看一下入驻阿里云工具市场后，用户是如何使用产品的。

![2021-12-01-10-53-53](/images/2021-12-01-10-53-53.png)

用户进入产品无须安装，直接进入使用流程。

![2021-12-01-11-03-51](/images/2021-12-01-11-03-51.png)

### 购买流程

由于与阿里云的支付系统打通，用户可以直接付费购买产品。

![2021-12-01-11-18-07](/images/2021-12-01-11-18-07.png)

### 权限开通

在购买产品的同时，阿里云会根据应用的要求提前为用户配置好产品使用过程中所有RAM权限，减少客户后期的配置成本，真正做到开箱即用。

## 入驻价值

那么为什么要入驻阿里云平台，入驻后又对企业有哪些帮助呢？

### 优势一：市场价值

无论是云迁移还是云灾备产品我们都是秉承着云原生理念进行的开发，而让这两款产品与云平台进行深度整合是整个团队最大的心愿。之前也曾通过多个不同渠道与阿里云进行了深度沟通，但是由于种种原因都是无疾而终，而阿里云工具市场的模式恰好满足了我们的诉求。同时，产品能够被阿里云认可，并顺利完成入驻，是对公司及研发团队最大的褒奖和认可。

### 优势二：客户引流

阿里云的控制台是个巨大的流量入口，并且这个流量中还有很多宝贵的企业用户流量，能够以这样明显的方式在控制台中占据一席之地，对于产品的推广无疑是一个巨大的渠道。最近，我们即将正式发布面向云原生场景的灾备平台，同时也将入驻阿里云应用工具市场，也期待与阿里云更多的业务团队共同推广，获取更多客户的认可。

### 优势三：打通商务流程任督二脉

在企业级市场中，采购流程往往是一个非常繁琐的过程，通过与阿里云支付流程的彻底打通，节省企业在采购中的商务成本，业务团队能够更快速的进行相关决策并执行。以下是传统流程和阿里云应用市场采购流程的对比：

![2021-12-01-14-37-06](/images/2021-12-01-14-37-06.png)

## 关键进度及成本

从2020年2月开始与应用工具市场团队进行了初步沟通，在3月份时候又分别与相关架构团队、安全等团队进行了前期的架构规划，阅读前端开发及接口开发规范，并提供了测试环境用于后续的开发工作。

由于研发团队有排期中的任务，所以正式开发的时间是在4月中下旬，四月初只是与阿里云的前端团队确定了页面风格和用户体验部分。研发周期大约在一个月左右的时间，涉及内容包括：

* 根据阿里云设计规范开发UI
* 根据阿里云开发规范调整全部API接口，前端对接新接口
* 应用市场对接
* 安全策略调整，包括源端代理、安全组策略等
* 针对阿里云工具应用市场鉴权要求，修改SDK
* 将原有数据同步代理对云平台API接口调度部分回收至服务端，以符合安全要求

从6月初到7月10日最终上线，针对我们的CI/CD流程进行调整（HyperMotion产品虽然是工具类型产品，但是涉及面较广，构建较为复杂，后续有专门文章介绍），并进行最终的完整性测试，于7月10日最终上线。

### 产品收获

在本次对接中与阿里云各个团队进行了深入沟通受益颇多，在产品安全性层面对产品提出了建设性建议，对我们提高自身产品的安全性有非常大的帮助。另外在这个过程中，也对我们的CI/CD流程进行了重新梳理，为了后续更好的面向多种版本发布提供了很好的参考依据。

## 技术对接细节

### 整体架构

HyperMotion控制层是基于OpenStack的异步微服务框架开发的，采用容器化部署方案，可以部署在单机上，也可以部署在K8S集群中。整体架构示意图如下：

![2021-12-01-13-37-04](/images/2021-12-01-13-37-04.png)

这是阿里云ISV对接的完整架构图：

![2021-12-01-13-38-15](/images/2021-12-01-13-38-15.png)

后端模块部署在K8S集群中，而由于在我们的场景中还包括Agent下载等功能，所以额外申请了对象存储资源。

### UI部分

为了与阿里云风格保持一致，由阿里云前端团队为我们提供了一整套前端设计规范。

![2021-12-01-13-41-20](/images/2021-12-01-13-41-20.png)

虽然HyperMotion支持多云之间的互相迁移，但是为了满足阿里云的需要，专门定制了一个阿里云专用版本（如开头所示）。

嵌入到阿里云的前端体系，还需要进行一些额外的配置，以Vue 3.0为例，需要在vue.config.js中增加如下选项：

![2021-12-01-13-46-23](/images/2021-12-01-13-46-23.png)

### 接口部分

由于安全性的原因，我们不能使用我们现有的接口体系，而是需要按照阿里云的接口规范，对接口进行重新包装。

根据规范要求，我们在调用自身服务时都是使用的GET接口，接口定义如下：

```
GET http://${isv_ip}/api/${action}?userinfo=${userinfo}&accessToken=${accessToken}&params=${params}&traceId=${traceId}
```

接口修改工作应该是研发比较重的工作，涉及到前端和后端同时修改，由于HyperMotion在开发阶段严格遵守了微服务的开发理念，所以修改起来并不困难，只需要对接口进行简单的包装即可。

### 安全性调整

通过与阿里云安全团队进行密切沟通，最终我们在以下两部分做出了调整：

#### 通讯方向

在入驻阿里云前，为了保证通讯的效率，我们产品在源端主机（比如一台物理机）和控制端进行通讯时采用的是双向方式。而控制端在操纵云同步网关时（阿里云租户内的一台云主机），又使用了单向下发的方式。根据阿里云的安全策略要求，我们服务所在的网络是严格与外界隔离的，即使用户的云主机是阿里云主机也不可以。所以我们将控制端与源端主机和云同步网关的通讯全部修改为单向向上的访问，满足了安全性的要求。

#### 接口安全

用户在使用产品时，需要在源端主机内或者虚拟化平台中部署代理程序，这需要进行下载。产品原有方式中，安全机制不够健全，可能有越权注册的情况发生。根据阿里云安全团队的建议，我们采用密钥的方式对关键信息进行加密处理，防止信息被破解，同时也避免了越权等危险操作行为的发生。

### 发布上线

HyperMotion产品的构建主要分为两大部分：Agent和容器构建。由于涉及的操作系统（Linux/Windows）和内核较多，Agent构建相对来说比较复杂。而容器的构建则比较简单。根据上线要求，我们统一在云效上进行构建，并将制品统一放入制定的制品库，之后由阿里云同事，在K8S更新环境完成上线过程。

## 优化建议

阿里云应用工具市场在阿里云内部应该也算是比较全新的团队，在实际对接过程中，还是有很多槽点。我们属于比较早期的种子客户，据我说知有很多企业在尝试对接后最终选择了放弃，这其中的原因有几下几点：

1、没有单独提供开发测试平台。虽然在前期阿里云提供测试平台，但实际这就是最终的生产平台，当系统完成上线后，我们就没有其他可以进行调试的平台了。虽然可以通过快速迭代完成对线上Bug的修复，但是对于一款严谨的商业软件，尤其是涉及到用户数据部分，我们还是希望能有充足的时间进行前期的测试工作。

2、没有提供运维入口。目前如果线上出现问题，只能依靠阿里云对接同事帮我们取出日志，无法快速的定位问题，拉长了故障解决的时间。

3、对原有系统改造代价过大，从上面对接过程来看，在接口层面的修改是对很多企业不小的挑战。

4、导流不够明显，虽然阿里云应用工具市场经过数次改造来吸引流量，但仍然有很多客户对此一无所知，同时阿里云应用工具市场团队与其他团队横向合作过少，建议与业务团队能够开展更多的合作推广活动。

虽然阿里云应用工具市场目前还有很多值得优化的点，但作为国内云计算平台的先驱，能够秉承“被集成”的理念，为生态合作伙伴提供一个公平竞争的环境，也希望我们能一起携手阿里云走的更远。