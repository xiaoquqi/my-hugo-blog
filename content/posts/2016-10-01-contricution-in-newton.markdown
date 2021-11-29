---
layout: post
title: "深度解读OpenStack Newton国内代码贡献"
date: 2016-10-01 09:00:49 +0800
comments: true
categories: [OpenStack, Cloud Computing]
---

今天是十一黄金周开始的第一天，在2016年10月6日，OpenStack马上要迎来第14个版本的发布，也是Big Tent后的第三个版本，计划Release项目达到32个，比Mitaka版本多了3个。

这是继OpenStack Liberty贡献分析后的第三篇系列文章，我们很欣喜的看到在每次的OpenStack Release之后，我们总是可以发现有很多新的中国企业投身于OpenStack生态圈中，无论如何，随着时间的推移，像OpenStack这样的开源软件势必在企业市场中有越来越多的应用。在当今房价飞速增长的今天，整个的社会充满了浮躁，能出现一个像OpenStack一样的项目实属不易。我们的国家、我们的民族太需要一些脚踏实地的人做一些真正的“自主可控”的技术积累，否则我们的未来仍然摆脱不了表面强大的现实。

最近一段时间一直在接触客户，也在思考为什么OpenStack无法像苹果手机那样轻松落地、供不应求，当然这个对比并不恰当。记得寄云科技的时博士曾经说过：越接近于用户底层的应用越难落地。现实也的确如此，就好像用户盖了一栋大楼，这时候你告诉用户，我这有个地基比你原来的好，来我给你换了；又或者你告诉用户说，我这个地基比你以前的好，我给你重新搭个地基，你再盖个楼。我想如果我是用户，我也不会答应的。所以，在用户基础架构已经非常成熟的企业中，OpenStack在落地过程中势必会遇到痛点不痛，落地困难的问题。我觉得解决这个问题无外乎几个方面：第一，有一位高瞻远瞩的领导，像携程的叶总、恒丰银行的张总；第二，把OpenStack的解决方案做的像VMWare一样完整，比如用户原来的业务系统怎么无缝迁移过来，用户原有资产怎么重新利用，怎么让OpenStack适用用户现有的网络架构，怎么让OpenStack适用用户现有的管理流程；第三，将OpenStack和刺中用户痛点的应用结合起来，进而推进OpenStack在企业中的应用，这也是我一直在寻找的方向。这仅仅是我在从事四年多OpenStack研发、销售过程中的一点点思考，也欢迎各位一起进行讨论。

还是那句话，排名并不是这篇文章的真正目的。我们希望能有更多的用户看到，我们中国企业在OpenStack上的影响力，让更多的用户了解OpenStack，从而能够在未来的应用中使用OpenStack，形成真正的OpenStack的生态圈。

OpenStack Liberty深度解读请见：http://xiaoquqi.github.io/blog/2015/10/29/contribution-in-liberty/

OpenStack Mitaka深度解读请见：http://xiaoquqi.github.io/blog/2016/04/07/contribution-in-mitaka/

<!-- more -->

## Release项目简介

Openstack官方的Release的网站已经更新为：http://releases.openstack.org/

下面是最近三个版本Release的详细对比：

![](/images/blogs/contribution-in-newton-projects.png)

让我们来关注这次Release中的三个新项目：

### Panko(计量服务事件消息存储)

Panko是计量模块中的一部分，主要是为了计量模块提供事件消息存储，众所周知，在上一个OpenStack Release中，Ceilometer被一分为三，分别为aodh(告警服务)/Gnocchi(基于时间的数据库服务)/Ceilometer，为了解决当前Ceilometer中存在的性能问题，提高更好的扩展性。

现在Panko的文档并不是很丰富，如果有需要了解更多详细内容的，可以关注Developer的文档：http://docs.openstack.org/developer/panko/

### Vitrage(广大OpenStack管理员的福音，平台问题定位分析服务)

Vitrage是一个OpenStack RCA(Root Cause Analysis)服务，用于组织、分析和扩展OpenStack的告警和事件，在真正的问题发生前找到根本原因。

众所周知，OpenStack平台最大的优势来自于架构的可扩展性，这也是OpenStack能够在基础架构曾一枝独秀的重要原因。分布式架构最大的优势在于扩展，但是过于灵活的扩展性为运维带来的极大的困难，所以Vitrage的出现在一定程度上缓解了OpenStack运维上的痛点。

我们来简单看一下他的架构，更多详细的介绍请查看WIKI：https://wiki.openstack.org/wiki/Vitrage

![](/images/blogs/contribution-in-newton-vitrage-architecture.png)

### Watcher(OpenStack平台优化服务)

从名字上看，我们并不能理解这个模块的具体左右，我们通过文档中用户应用场景来了解一下Watcher的作用：

作为一名云平台的管理员在云平台使用一段时间后，想根据一些物理特性对云平台虚拟机的分布进行重新平衡，例如服务器的温度、电源的状态等信息，那么这时候就可以通过watcher，利用Nova虚拟机的在线迁移对整个数据中心云平台的虚拟机进行一些优化处理，从而达到某种平衡。我认为这其实类似于VMWare的DRS功能。

当然Watcher还有更多的应用场景，更多详细的介绍请查看：https://wiki.openstack.org/wiki/Watcher

我们来简单看一下他的架构，更多架构方面的详细的介绍请查看：http://docs.openstack.org/developer/watcher/architecture.html

![](/images/blogs/contribution-in-newton-watcher-architecture.svg)

## 社区贡献总体分析

本次统计的方法仍然为commits和blueprints的方式，统计范围为stackalystatics默认统计的全部项目。

从总体参与的公司和贡献者来说，都有所上升，这也不难理解，随着OpenStack模块增加，势必涉及更多的领域，所以更多的公司加入了这个生态圈。

![](/images/blogs/contribution-in-newton-companies-contributors.png)

从commits角度进行分析，传统几大好强几乎没有变化，日本的Fujitsu在commits上挤掉了华为，进入了前十名的位置。模块方面，核心模块的贡献仍然位于前十名，也说明是应用最多的模块，所以才会不断的发现问题。本次统计的总项目数量为629个，可能stackalytics在统计策略上有所调整。

![](/images/blogs/contribution-in-newton-companies-modules-commits.png)

单从commits角度统计其实有失偏颇，真正能够体现公司在OpenStack实力的指标应该是Blueprints。我认为完成Blueprints至少具备三个必要条件：英语要好、在社区有一定的影响力、架构设计能力。这些都是需要不断在社区进行积累和沉淀的。

本次release周期内，能够完成Blueprints的公司为64个，国内的华为和九州云均进入前10名，排名比较靠前的国内企业还包括：Easystack、中兴。

完成Blueprints最多的仍然是核心模块，排在第二名的是kolla，看来在上一个周期中，kolla项目的活跃程度是较高的。

![](/images/blogs/contribution-in-newton-companies-modules-blueprints.png)

## OpenStack国内社区分析

看完总体的状况，再来关注一些国内的贡献情况，与去年相比，今年上榜的国内企业达到了21家，创历年之最，比去年的15家企业整整多了7家，并且我们发现在这些新增企业中大部分都是提供企业服务的公司，说明OpenStack在国内的企业级市场开始站稳脚跟。下面我们来做一个详细的分析：

### 贡献企业

在最近的三个版本连续对社区有贡献的企业包括：华为，Easystack，九州云，海云捷迅，华三，Unitedstack，乐视，中国移动和北京休伦科技(Huron)。

本次爬升最快的企业：中兴，从108位攀升至13位。

本次统计新增的7家企业：云途腾(t2cloud)，大唐高鸿数据(GohighSec)，华云数据，烽火通信，爱数，北京国电通，云英，中国银联，赛特斯信息。

本次排名中OpenStack的直接用户：中国移动和中国银联。中国移动更是参选了OpenStack SuperAward的评比，预祝他们能顺利当选。

![](/images/blogs/contribution-in-newton-china-companies.png)

### 人员投入分析

我们再来从人员投入来分析贡献情况一下：

* 投入人数最多的仍然是华为，有65名工程师贡献了本次的commits
* 中兴无疑是本次人员投入增长最快的，从6名工程师一下子扩张到61名，也是唯一能和华为抗衡的
* 超过2位数人员投入的包括，Easystack，九州云和Unitedstack，另外海云捷迅有9人，华三有8人，中国移动有7人参与社区贡献

![](/images/blogs/contribution-in-newton-companies-effort.png)

### 模块贡献分析

从模块贡献角度来分析，国内企业的贡献仍然没有出现一个统一的趋势，与Mitaka Release相比，贡献涉及模块的总量从192个增加至Newton Release的246个，一方面说明OpenStack本身模块的增加，也说明国内企业使用或开发OpenStack在方向上的多元化。

从贡献的模块来看，华为主导的dargonflow高居榜首，紧随其后的是手册和clients两个项目，随后的贡献集中在OpenStack的核心模块，与Docker相关的几个模块中。Kolla项目无疑是最近关注的热点，随着Docker的快速发展，OpenStack和Docker不断碰撞出新的火花。

![](/images/blogs/contribution-in-newton-modules.png)

### 投入产出比

这个问题仍然是比较敏感的问题，只有每个公司的CEO能够回答这个问题，这里面我从融资的角度来回顾一下2015至2016年之间在OpenStack领域发生过什么。

* 2015年9月17日，英特尔投资部门披露了此前投资的中国8家公司名单。投资总额达6700万美元，领域覆盖了新材料、智能设备、物联网、云服务等领域。其中包含九州云和海云捷迅两家OpenStack企业。(http://tech.qq.com/a/20150917/038604.htm)
* 2015年10月17日，中国最大的独立公有云提供商UCloud和全球领先的OpenStack厂商Mirantis在东京的OpenStack峰会上正式宣布成立合资公司UMCloud，以求更好的在中国做OpenStack。(http://www.doit.com.cn/article/1027290510.html)
* 2015年12月16日，UnitedStack有云宣布完成C轮融资，该轮融资由思科和红杉资本投资，具体数额未公布(http://www.infoq.com/cn/news/2015/12/unitedstack-financing)
* 2016年5月20日，云途腾(T2Cloud)完成A轮3650万融资(http://iimedia.cn/42262.html)
* 2016年9月21日，腾讯与海云捷迅昨日下午在京共同宣布达成战略投资合作关系，海云捷迅接受腾讯的战略投资(http://www.36dsj.com/archives/62353)

## 总结

回到开篇的那句话，OpenStack贡献量只能反应中国企业对于开源项目的重视程度，无法反应真实的用户需求。VMWare花了将近10年的时间教育用户，说服用户把应用从物理机迁移至虚拟机。OpenStack从2011年出生到现在也仅仅短短的5年，可见OpenStack还有很长的路要走。
