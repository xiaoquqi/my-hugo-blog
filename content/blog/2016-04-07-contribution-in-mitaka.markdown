---
layout: post
title: "深度解读OpenStack Mitaka国内代码贡献"
date: 2016-04-07 23:19:39 +0800
comments: true
categories: [OpenStack, Cloud Computing]
---

转眼间，OpenStack又迎来了新版本发布的日子，这是OpenStack第13个版本，也是Big Tent后的第二个版本，秉承“公开公正”的原则，OpenStack Release的项目达到了29个，比Liberty多出了8个。

去年的时候，对国内的OpenStack Liberty贡献进行了深度解读后引起了广泛的关注，在今年Mitaka版本发布之后，类似的解读已经遍布朋友圈，但是在看过后，发现并非国内贡献的全部统计，所以决定还是自己写一篇完整的深度解读系列文章，来帮助国内用户对国内OpenStack的现状有一个全面的了解和认识。

这几天一直在思考写这篇文章的目的和意义，我们搞分析也好，搞排名也罢，到底是为了什么？Mitaka版本更新后，各个公司也以排名作为企业宣传的最好的武器，我觉得这些都无可厚非。但是我觉得更重要的一点是在当前去IOEV的大形势下，我们应该告诉国内的企业用户，有一批热衷于追求Geek精神的年轻人在为中国未来的IT产业变革做着不懈的努力，他们用数字证明了国外公司能做到的我们国内公司也能做到，这个世界上不仅有IOEV，还有中国制造的OpenStack。

对于友商们已经分析的数据，这里不再赘述，本文主要通过stackalytics.com提供的API对国内社区贡献进行一次深度挖掘和整理。

OpenStack Liberty深度解读请见：http://xiaoquqi.github.io/blog/2015/10/29/contribution-in-liberty/

<!-- more -->

## Release项目简介

Openstack官方的Release的网站已经更新为：http://releases.openstack.org/

在Big Tent公布之后，OpenStack的项目被分为Core Projects和Big Tent Projects。

![](/images/blogs/contribution-in-mitaka-big-tent.jpg)

让我们来看一下在Mitaka版本中，多了哪些新项目。

* 几个与Docker相关的项目被发布出来，magnum, senlin, solum
* 数据备份容灾的项目：freezer
* 计费的项目：cloudkitty
* NFV相关的项目：tracker
* 监控相关的项目：monasca

关于这些新项目的一些介绍，我将放在另外一篇博客里，敬请关注。

![](/images/blogs/contribution-in-mitaka-projects.png)

## 社区贡献总体分析

本次统计的方法仍然为commits的方式，统计范围为stackalystatics默认统计的全部项目。

从总体参与的公司数量来看，Mitaka版本略有下降，但是参与的人数多了100多人。

![](/images/blogs/contribution-in-mitaka-companies-contributors.png)

整个社区的公司贡献排名上没有明显的变化，传统的几大豪强仍然霸占公司排名的前十位，华为表现依然强劲，是中国区唯一能进入前十名的公司。

在模块方面，整体统计的绝大部分比例已经被others所占据，说明在Big Tent计划下，OpenStack正在朝更多元化的方向演进。在Mitaka排名前十位的项目中，fuel相关的两个项目都进入了前十，说明fuel在OpenStack部署的地位已经越来越重要了。同时，核心项目中的nova，neutron，cinder项目仍然在前十名的范围内，贡献量基本保持不变。值得一提的是，在Mitaka统计的项目数量已经从Liberty的708个增长到了829个，可见在短短的6个月内，OpenStack社区的蓬勃发展。

![](/images/blogs/contribution-in-mitaka-companies-modules.png)

## OpenStack国内社区分析

看完了整体统计，我们再回到国内，因为已经有文章做了我在Liberty时候的分析，所以这里我换个角度来看国内的社区贡献，首先是统计排名的变化。

### 贡献企业

在Liberty中，有13家国内企业为社区做了贡献，在Mitaka中这个数量增加到了15家企业，这里简单的将这些企业做了一下分类：

* 互联网用户：乐视、新浪、网易
* 电信用户：中国移动
* 传统IT服务商：华为、中兴、华三
* 私有云服务商：Easystack、九州云、海云捷迅、北京有云、麒麟云、UMCloud、象云、Huron(休伦科技)

![](/images/blogs/contribution-in-mitaka-china-companies.png)

### 行业分析

通过行业的分析我们可以看出，国内的主要贡献仍然来自私有云服务商和传统IT服务商，换言之来自于以OpenStack提供产品或者服务的公司。厂商们贡献的目的很明确，主要为了展示自身在开源项目中的积累和专家形象。而用户的贡献主要来自平时在使用OpenStack时候遇到Bug，就是在实际应用过程中出现的问题。

![](/images/blogs/contribution-in-mitaka-china-by-industry.png)

### 人员投入分析

单纯的社区贡献排名的比较仅仅是一个维度，下面我们来看一下各个公司的人员投入情况：

* 排名前几位的公司对社区投入的人力基本都是两位数，相对于Liberty版本，人员均有所增加
* 在人均贡献投入上，99cloud是国内最高的，平均达到了59天，甚至超过了华为，这个统计不仅仅包含了代码贡献，还包含了邮件、Review、Blueprint的时间，基本可以衡量每个公司在OpenStack社区贡献方面的投入力量
* 人员投入来看，Easystack和中国移动无疑是最下本的两家，Easystack从Liberty的3人，增长到了23人，一下子增加了20人；中国移动也从最初的4个人，增加到了13个人，可见中国移动未来对OpenStack的野心

![](/images/blogs/contribution-in-mitaka-companies-effort.png)

### 贡献模块分析

从模块的角度进行统计，国内企业的贡献情况并未出现一个统一的趋势，总体的贡献项目为193个，项目几乎涉及OpenStack所有最活跃的项目，从排名前十的项目来看：

* 得益于华为的主导，dargonflow项目的贡献量超高
* 紧随其后的，也是当下的热点，容器相关的两个项目
* 几大OpenStack老模块贡献量也高居前十位，说明这些模块是在解决方案中使用频率较高的

![](/images/blogs/contribution-in-mitaka-modules.png)

### 投入产出比

这是一个很敏感的话题，每个公司对社区的投入到底换来多少项目上的回报呢？可能这只有每个公司的CEO能够回答的问题了。我在这里就不多做过多的分析，留给大家充分讨论的空间吧。

## 总结

刚刚结束在南京的OpenStack开发培训，也了解到5G的通信网络上已经确定引入了OpenStack，虽然我说不清楚他的具体用途，但是我相信这对OpenStack这个项目、社区是一个重大的利好消息。我也相信，通过国内企业的集体努力，一定能让OpenStack在中国遍地开花结果。
