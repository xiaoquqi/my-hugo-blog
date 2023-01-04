---
title: Serverless发展历史
author: 孙琦(Ray)
tags:
  - Serverless
categories: []
date: 2022-02-21 07:30:00
---
最近看了很多Serverless的文章，关于发展历史看了很多版本，其实对于2010年后的时间点各种国内外说法基本一致，但是在2010年之前就有多种不同的描述方式了，本文结合各种资料对Serverless发展的历史进行一下整理。

<!-- more -->

从应用开发的历史角度看，我们的应用从运行在传统的物理服务器上，经历了到虚拟化、容器到目前的Serverless，至于Serverless之后会是什么，目前还没有看到。从应用开发角度看，这个过程实际一直在进行的事情就是“解耦”，解除应用与底层之间的关联关系，最终使得应用的开发走向轻量化，用户对于底层无感。

![upload successful](/images/pasted-166.png)

再从我们看的见的商业维度说，中关村海龙、鼎好的兴衰的过程也在印证了这一切的发展，时间回退到20年前，当初做硬件发家致富的中关村老板大有人在，包括今天的京东也是从中关村卖光盘起家的。但是如今的中关村是什么样的景象呢？这些老牌的商场纷纷面临转型，如今的繁华再也一去不复返了。

与之相呼应的是，传统的硬件集成商的日子越来越不好过了，靠卖铁度日的利润越来越薄，竞争也越来越激烈，市场也越来越透明。为什么出现这样的局面呢？原因其实就在于应用离底层越来越远，单纯的采购硬件无法解决用户的需求。虽然在传统硬件的销售也一样需要解决方案，但是在新的云计算的态势下，解决方案的复杂程度、技术含量越来越高，并非传统的“攒机”式销售就能搞定的。当然在云计算领域下还是存在这样的简单粗暴的销售产品，就是网络，这个话题并不在我们本文的范畴内。


## Zimki——最早使用Serverless模式的公司

目前公开资料认为最早使用Serverless模式的公司叫做Zimki，即Pay as you go。他们提供服务端的Javascript程序，理念在2006年被提出。这个团队来自被欧洲佳能收购的Fotango。在slidershare上还能找到他们最早的PPT资料，不过这家公司已经倒闭。

![upload successful](/images/pasted-163.png)

虽然Zimki是Serverless模式最早的缔造者，但是并不是最早使用Serverless词的公司。

有兴趣的朋友可以看一下他们早期的一些理念的介绍：

* http://radar.oreilly.com/2006/09/zimki-hosted-javascript-enviro.html
* https://www.slideshare.net/swardley/zimki-2006

## Platform-as-a-Service

在出现函数计算服务形态之前，还有一种PaaS形态，也是属于Serverless的一种形态，只不过设计的出发点不同。PaaS更注重的是完整的代码托管，开发者只需要上传自己的代码，剩下全部的交给平台。这种形态最早出现于2007年。在最近3年内，特别在容器和K8S出现之后，PaaS平台迎来了新一波的关注热度。

Heroku这家公司想必早期写博客的朋友都不会感到陌生，在那个计算资源还比较昂贵的时代，Heroku的免费资源还是非常受广大开发人员欢迎的。2007年6月Heroku开始开发，最早只支持Ruby语言(这就是为什么早期的博客工具octopress是基于Ruby开发的)，2011年的时候Ruby的首席设计师日本人松本行弘加盟了这家公司，后续又扩大了对Node.js和Clojure的支持。到目前为止，Heroku几乎覆盖了主流开发语言的。2010年Salesforce斥资两亿多美金收购了Heroku公司。

![upload successful](/images/pasted-165.png)

2008年，Google推出了Google App Engine的PaaS服务，想必如果你当时对科学上网有所研究的话，对这个平台并不陌生。当时，最著名的开源项目非GoAgent莫属，当然实现这个项目已经无法使用了。但是当时GAE平台有非常大的局限性，无论是开发语言还是开发模式，对于框架支持等都有比较严格的限制；另外由于缺少云原生服务的支持，所以应用场景有限，同时具有非常明显的厂商锁定的特性。

其实包括AWS(AWS Beanstak)、阿里云(Web应用托管服务)在内的主流公有云厂商，目前均提供了类似GAE便于用户快速构建自己的应用，在很多最佳实践中也都有提到。

国内最早提供SAE服务的，是新浪云，是的你没有听错新浪也是有云的。新浪早在2009年11月3日推出了Alpha版本的新浪SAE，当时用于支付平台费用的叫做云豆，笔者记得当时注册新浪SAE平台，会赠送相当可观的云豆用于开发和测试。虽然新浪涉及云计算领域较早，但是后劲不足。另外还有一个值得一提的一点，新浪SAE也是国内比较早期使用OpenStack的技术团队。后来，OpenStack在中国得到前所未有的发展，与新浪SAE技术与运维团队的推广有着非常直接的关系。

## 开源PaaS平台

2008年一个基于AWS EC2的PaaS项目开始开发，项目使用Java语言并且基于AWS EC2，名称叫做Cloud Foundry。2009年该项目被SpringSource公司收购，同年SpringSource又被VMWare收购。但是这个Cloud Foundry与我们现在熟知的Cloud Foundry项目完全无关，只是保留了名称。最早的Cloud Foundry项目实际是由VMware内部的一个小团队开发的B29项目。

2011年4月，Cloud Foundry正式宣布开源。2012年4月，又开源了BOSH项目用于Cloud Foundry基础资源及自身的全生命周期管理。笔者在2011年有机会从事了一部分Cloud Foundry产品开发工作，记得当时BOSH对VMware支持非常完美，但是OpenStack平台基本惨不忍睹，当然这也怪当时的OpenStack自己不够争气。
2013年，VMware和EMC正式成立了Pivotal公司，自此包括Cloud Foundry, RabbitMQ和Spring都归属于Pivotal。

同一时期，与Cloud Foundry同一类型的开源项目就是Redhat OpenShift，目前OpenShift也是国内基于Kubernetes之上的PaaS项目(CloudFoundry也开始这么定义自己了)。当然OpenShift也不是Redhat原生项目，而是在2010年收购的Makara的项目，该公司主要基于Linux Container技术实现PaaS平台。2012年5月的时候，OpenShift正式宣布开源。OpenShift v3版本开始支持Kubernetes作为容器编排引擎，Docker作为底层容器。OpenShift v4版本为了防止Docker锁定，使用CRI-O作为容器Runtime。

## ”Serverless“概念的来历

如果你使用中文搜索引擎搜索Serverless的历史，往往会提到一家公司叫做Iron.io，但是如果你搜索英文资料的时候却发现很少有提及此公司。经过一系列的搜索，终于梳理清楚了Serverless概念和定义的由来。

2012年10月，时任Iron.io BD副总裁的Ken Fromm在ReadWrite网站(互联网科技博客)上发表了一篇名为《Why The Future Of Software And Apps Is Serverless》的文章，完整的阐述了对Serverless架构的构想，其中开篇的第一句话就是：

> Even with the rise of cloud computing, the world still revolves around servers. That won’t last, though. Cloud apps are moving into a serverless world, and that will bring big implications for the creation and distribution of software and applications.

ThoughWorks提出了对Serverless架构的定义：

> A serverless architecture approach replaces long-running virtual machines with ephemeral compute power that comes into existence on request and disappears immediately after use.

> Serverless架构使用临时计算资源替代原有常态化运行的虚拟机，当有请求时资源存在，请求结束后资源自动销毁。

也许你觉得太复杂了，我们来看看Techopedia网站上对Serverless的定义：

> Serverless computing is a type of cloud computing where the customer does not have to provision servers for the back-end code to run on, but accesses services as they are needed. Instead, the cloud provider starts and stops a container platform as a service as requests come in and the provider bills accordingly.

> Serverless是云计算服务的一种，用户只需要将提供服务的代码运行在云上，而无须实现其他后端服务。云商根据访问情况，启动或者停止容器来提供服务，用户只需要根据实际消费付费。

如果你还认为复杂，可以简单的将Serverless理解为“基于事件驱动的计算服务”。

## Function-as-a-Service

2014年对于Serverless是具备里程碑的一年，AWS发布了Lambda服务——基于事件驱动的函数计算服务。最早发布的Lambda仅支持JavaScript和Node，但是目前几乎涵盖了所有主流编程语言，同时支持自定义方式。

![upload successful](/images/pasted-167.png)

在接下来的时间里，各大公有云厂商纷纷发布了自己的函数计算服务。从2014年到2018年的四年里，各大主要公有云厂商纷纷发布自己的函数计算服务并不断的迭代、演进。一方面扩大对触发器的支持范围，加强与各个云原生服务的联动性；另外一方面基于函数计算增加编排服务，方便构建更复杂的应用场景。

![upload successful](/images/pasted-168.png)

## 小结

目前，Serverless被各方认为是未来云计算服务发展的重要趋势，也是各大厂商的必争之地。我认为Serverless对于行业的影响是深远的，除了技术层面外，还包括从业者的格局。根据Gartner 2020年6月的成熟度曲线看，Serverless还有一段发展的时间，但是作为云计算行业的从业者，应该着手应对Serverless对未来产业格局的影响。后面的文章，我将继续和大家分享我对目前公有云厂商Serverless发展的看法。

![upload successful](/images/pasted-170.png)


## 参考资料

* [Serverless国内发展的纵向观察](https://mp.weixin.qq.com/s/1jhLRNaUag-Gp-kbYvzzGA)
* [Why The Future Of Software And Apps Is Serverless](https://readwrite.com/2012/10/15/why-the-future-of-software-and-apps-is-serverless/?__cf_chl_jschl_tk__=9d9134331acb78cc239f3e7db934345af67bbdc7-1613485823-0-ARJ7RlgI0rpCz7GIY2DCiOUmXfWwk0bP-j7LmFE25MHdY6rqorQ069DcGqkzOpoxRuF_6QQav0-GxS00_nMmF7lpD2gCs33ZMSva-klU-Dlc9Vg2bMzg9TiW4s4mjpmwpjG4SvaWqwsr0rTe48hjYksKmMwUn9GWWeYRjERPJUvgQ20EVTLysumFK6sOjvEt7-AlesfFVqDeCRFjjpN6-_cbDwyGHGZ-PgAxaWrgy4_dbgDFXiz98GSEb0BBhtdqcWMFpI1qkocucVqWrOwsQdKfwX6_zh_QV1joZDfefFJqKafULTlgJ8bpx7AczZOkheoMZFwMaCXRrCd2jX5SFiv2fkgf5fBq3h71pWKaQsFF_oKHxqzx-NBGidZH22_qSYf5LkbpJdGLJRUNGWURU02GZmSK_HqqPlLhRxNS_pQTHMe2qM-7pSzvMadnDRZafQ)
* [ThoughtWorks Serverless architecture](https://www.thoughtworks.com/radar/techniques/serverless-architecture)