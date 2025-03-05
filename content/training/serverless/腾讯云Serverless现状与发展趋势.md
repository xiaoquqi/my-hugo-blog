---
title: 腾讯云Serverless现状与发展趋势
author: 孙琦(Ray)
tags:
  - Serverless
categories: []
date: 2021-02-21 15:47:00
---
上一篇主要和大家分析了Serverless整体的格局，以及重点就AWS在Serverless的现状和发展趋势进行了简单分析，今天来和大家一起来看一下腾讯云。

其实我对腾讯云Serverless的了解是通过云开发开始的，当时我的个人博客托管在Github Pages上，由于众所周知的原因，Github访问越来越慢，所以无奈之下将个人博客托管回国内。当时恰好看到了云开发的广告，9.9元网站托管赞助计划。在将网站部署到腾讯云开发过程中，逐步开始了解了腾讯的Serverless体系。

![upload successful](/images/pasted-184.png)

<!-- more -->

第二点开始对腾讯Serverless有所了解的是通过一个开源项目Serverless，目前这个项目的中文版本和社区(serverlesscloud.cn)都是腾讯维护的。

![upload successful](/images/pasted-185.png)

从公开的新闻看，腾讯与serverless.com在2019年达成战略合作协议（是否存在投资关系不确定，从公开资料看，目前serverless.com三家投资机构分别是：Trinity/Heavybit/Lightspeed）。

> 2019年11月6日，在由腾讯云主办的首届Techo开发者大会上，腾讯云宣布与全球最流行的Serverless开发平台Serverless.com达成战略合作，成为Serverless.com的全球战略合作伙伴以及大中华区独家合作伙伴。

第三点了解是在去年（2020年）11月腾讯小程序开发峰会上，发现腾讯小程序的开发已经与Serverless进行了深度整合，我们来看一下微信开发者工具，在顶部直接提供了云开发入口。这样小程序的开发变得更为完整，对于基于小程序生态进行开发变得更加容易，同时让前端工程师手伸的更长。

![upload successful](/images/pasted-187.png)


## 产品体系与生态

我们先从Serverless相关的产品体系来看，腾讯云对于自身的产品家族定位分为云服务、开发者平台和应用方案，另外还包括Serverless生态体系的支持。

![upload successful](/images/pasted-183.png)

函数服务和API网关属于底层的云原生服务，在中间层上提供了聚合的Serverless Framework，无论Serverless HTTP还是Serverless SSR都是基于Serverless Framework封装的应用场景。Serverless HTTP倾向于API的提供，而SSR像是Google App Engine的PaaS服务。

基于产品体系，又推出了Serverless生态支持。包含了存储服务、应用服务、应用性能管理、开发者工具以及开发平台。

![upload successful](/images/pasted-194.png)

基于Serverless架构，腾讯进一步封装出云开发CloudBase，上面我们也提到，云开发与微信小程序生态有着非常紧密的结合。

之前曾经参加过一次关于云开发的在线培训课程，除了底层基础服务外，腾讯云在组装Serverless向上的趋势非常明显。从开发者角度来看，目前腾讯提供的Serverless生态注重轻应用的构建。我首先从Serverless Framework和云开发角度进一步说明，当然我们首先来看一下函数计算。

## 云函数SCF

### 用户体验

云函数设计的界面很清爽，左侧导航栏并不非常多，只有概览、函数服务和层三个功能菜单。

![upload successful](/images/pasted-199.png)

区别于AWS的UE设计，云函数还是保留了传统的技术风格，开发者可以通过模板创建或者自定义创建方式。在模板库里内置了很多场景化的组件供开发者选择，可以帮助开发者很快速的构建出应用场景。

![upload successful](/images/pasted-200.png)


### 触发器

从国内的云平台提供的函数服务来看，二者从发展思路上有很大的差别，这一点从触发器角度看非常明显。腾讯的触发器种类不是非常多，但是基本都是非常实用的触发器类型。

![upload successful](/images/pasted-195.png)

定时触发：在AWS中，需要使用CloudWatch Events服务间接的实现定时触发，而腾讯函数计算服务直接提供了定时触发的方式，可以按照既定的规则，或者干脆自己写crontab表达式。

![upload successful](/images/pasted-196.png)

另外几种实用的触发器包括：对象存储COS触发，消息服务CMQ主题触发，消息队列Kafka触发。一种比较特殊的服务是视频处理MPS，还可以通过日志触发CLS和负载均衡触发CLB。

![upload successful](/images/pasted-197.png)

![upload successful](/images/pasted-198.png)

虽然触发器种类不多，但是对于用户来说不必受到云平台的深度绑定，还是有很大的灵活和自主性。

### 开发模式

与AWS相同，云函数中同样提供了在线开发和CLI方式进行开发。CLI方面原有腾讯的开发工具叫做sls，不过从2020年2月不再维护，转而建议用户使用兼容性更好的serverless，这个就是我们上面提到的serverless.com开源的产品。我个人对serverless.com的理解就是无服务领域的Terrafrom，不仅仅单纯的编排函数计算一种资源，serverless还可以包括对数据库、消息队列、对象存储等一系列serverless服务进行统一编排，同时提供了良好的扩展性，未来可以满足更多服务的编排。用户在构建serverless framework时更方便的对资源进行统一管理与发布。后面我会单独就serverless.com使用方法进行说明。

![upload successful](/images/pasted-201.png)

## 云开发

在之前一篇《基于Serverless架构进行应用开发》中，曾经给大家贴出这张云开发未来发展的架构图，今天再来回顾一下。(http://sunqi.site/2021/02/06/%E5%9F%BA%E4%BA%8EServerless-Framework%E8%BF%9B%E8%A1%8C%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91/)

![upload successful](/images/pasted-135.png)

云开发对云原生资源进行了进一步整合，从应用开发到应用运维的全生命周期提供支持。进而向上一层提供开发者工具IDE、低代码平台等。同时提供各种SDK产品，为多端接入提供良好的支持。在之前那篇Blog中，我们也看到通过微信小程序与云开发生态整合，更快的进行轻应用开发，同时最大程度的节省成本。从云开发的发展规划不难看出，云开发未来还将更深度支持各种轻量级应用开发。

### 微信开发者工具

我们在开篇提到微信开发者工具与云开发进行了深度整合，进入微信开发者工具后，其中提供了常用的云开发支持。包括数据库、存储、云函数等。

![upload successful](/images/pasted-188.png)

虽然云函数已经支持了很多种语言，但是目前在云开发内，应用开发者还是只能使用运行环境为NodeJS 10.15的环境。不知道这样的考虑是不是因为微信很多开发者都是Node.js生态的。

![upload successful](/images/pasted-189.png)

我们再来看看费用，之前曾经讲到过，Serverless的一个目标就是真正的让应用开发者按需使用资源，所以目前云开发的全部资源计费模式基本都是按照使用量计费的。云开发提供了套餐方式和单独资源付费的模式，如果你的应用访问不是很大，基础版1的免费版本完全可以满足你的需求。从这个角度来看，如果开发者能够合理优化自己的代码实现，很大程度上能节省掉很多成本。

![upload successful](/images/pasted-190.png)

## 总体评价

腾讯的Serverless提供轻应用开发支持的感觉更强，特别是将零散的云原生服务进行二次封装，让开发者更简单的使用Serverless架构进行开发。同时通过Serverless Framework解决了无服务在编排上的问题，更容易组织复杂一点的无服务化应用程序。同时，由于微信这个金牛，一下子为云开发提供了巨大的流量入口，也让基于微信生态的小程序应用开发更容易、加快应用层创新速度。