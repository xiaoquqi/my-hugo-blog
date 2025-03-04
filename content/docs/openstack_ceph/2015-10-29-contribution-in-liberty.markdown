---
layout: post
title: "深度解读OpenStack Liberty国内代码贡献"
date: 2015-10-29 18:56:06 +0800
comments: true
categories: [OpenStack, Cloud Computing]
---

又到了OpenStack 新版本发布的季节，虽然秋意寒寒，但是仍然挡不住OpenStack再次掀起全球关注的热点。这是OpenStack第12个版本，与之前的沉稳低调相比，这次的Release中一口气多了5个新模块，也创下了OpenStack项目创建以来的最高纪录。由于天然的架构优势，让OpenStack在云计算横行天下的年代游刃有余，已经逐步成为了云平台的即成标准，从OpenStack对待AWS的API兼容的态度就能看出，OpenStack变得越来越自信。

OpenStack Liberty完整版本的翻译可见：https://wiki.openstack.org/wiki/ReleaseNotes/Liberty/zh-hans

本次OpenStack Liberty更新日志中文版本的翻译工作由我完成。由于时间仓促，难免有很多问题，欢迎各位批评指正。

<!-- more -->

## 社区贡献分析

本次统计，并没有采用Review的数量为依据，而直接采用commits的方式，也就是代码实际merge入库的数量。

我们仍然要先看一下模块的贡献情况：

![](/images/blogs/contribution-in-liberty-contribution-by-modules.png)

与之前Release的特点相似，OpenStack早期的核心模块Nova, Keystone代码commits数量出现明显下滑状态，而Neutron, Heat, Trove, Ceilometer, Cinder等模块都保持着稳中有升的态势。值得关注的是，在排名前20名的项目中，出现了两个直接与Docker有关的项目Kolla和Magnum，一个与docker间接有关的项目Murano。可以预见，OpenStack下一步发展的热点就是在与Docker之间的勾勾搭搭。

特别需要注意的是，在stackalytics.com统计的模块中，在Kilo中是259个，而到了Liberty到了389个，当然有一些项目并非完全是OpenStack的项目，但是也从一个侧面反映出OpenStack以及周边项目的蓬勃发展。

从更新日志中我们也能看到，本次Release的正式项目中，变动较大的是Neutron和Heat两个模块。在经历不断锤炼后，Neutron逐渐走向成熟，但是从生产级别角度看，Neutron的确还有很长的路要走。

## 国内社区贡献分析

![](/images/blogs/contribution-in-liberty-contributor.png)

从全球企业的贡献排名来看，排名状况基本变化不大，仍然是HP, Redhat, Mirantis, IBM, Rackspace, Intel, Cisco，但是非常欣喜的，国内的IT的航空母舰华为已经成功杀入前十名，这无疑是振奋人心的事情，希望华为未来能多一些对OpenStack社区的主导力，提高中国在OpenStack社区的地位，当然最好也能扶植一下国内的OpenStack创业公司，实现共同发展、共同进步。华为的主要代码贡献集中在dragonflow，magnum，heat等模块，特别是在dragonflow上，几乎全部是华为贡献的，magnum上也将近有五分之一的代码。

***华为社区贡献统计***

![](/images/blogs/contribution-in-liberty-huawei.png)

记得在OpenStack五周年的庆祝活动上，Intel的陈绪博士说过，国内OpenStack贡献企业，就是一朵大云，四朵小云，下面让我们来看看这几朵小云在这个版本的表现。

*** 99cloud社区贡献统计***

![](/images/blogs/contribution-in-liberty-99cloud.png)

排名第16位的是99cloud，99cloud自上一个版本排名四朵小云之首后，本次继续强劲来袭，排名创造历史新高，第16名。通过对贡献模块的分析，我们能看出99cloud最大的贡献来自于社区文档，而在项目方面的贡献则主要来自murano-dashboard，horizon，neutron等项目上，从中可以看出99cloud对murano这个applicaton catalog的项目关注程度比较高，可能会在将来的产品中有所体现。从贡献中，我们隐约看到了九州云的副总裁李开总的提交，由此可见九州云为社区贡献的积极程度。
更加难能可贵的是，Horizon的全球贡献99cloud是全球前十，Tempest全球前八，Murano项目更是进入全球前三，相当给力。

*** UnitedStack社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-unitedstack.png)

排在第30位的是UnitedStack，经过了上一个版本的短暂沉寂后，这个版本卷土重来，杀回前30。从代码贡献来看，UnitedStack的主要贡献来自python-openstackclient以及部署用到的puppet相关代码，当然对neutron、trove、kolla、heat等也有一定数量的贡献。

*** Kylin Cloud社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-kylincloud.png)

排名第38位的是麒麟云，其实麒麟云每次Release中总是有她的身影，但好像总是被忽略的。麒麟云最大的贡献来自Horizon项目，其他模块也有一定数量的贡献。总之，我们想到OpenStack企业的时候，的确应该时常提起麒麟云。

*** Easystack社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-easystack.png)

排名第70位的是Easystack，Easystack也属于OpenStack早期创业的公司，对于OpenStack的贡献也是持续的。Easystack最大的贡献来自nova，虽然数量不是很多，但是在国内企业里应该算名列前茅的啦。Easystack对Nova的贡献主要来自对libvirt层的bug修复。

*** Awcloud社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-awcloud.png)

排名第75位的是海云捷迅，海云应该算是在国内发展比较迅猛的一家OpenStack早期创业公司。他们的贡献主要来自Neutron相关的项目，看起来应该是为了解决项目中出现的实际问题所做的努力。海云的马力应该是公司内部贡献排名第一的，尤其是前一段时间发布的两篇关于"Neutron & OpenStack漫谈"，非常值得一读。

*** LeTV社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-letv.png)

*** Netease社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-netease.png)

排名第94和95位的分别是两家互联网企业，乐视和网易，乐视是最近互联网中使用OpenStack动静最大的一家了，应该能在大规模应用中发现OpenStack很多问题吧。

*** Huron社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-huron.png)

排名第122位的是我的公司——北京休伦科技有限公司，其实我们公司也算是国内最早一批从事OpenStack创业的公司，z早在2013年的时候就已经开始投入OpenStack私有云产品相关的研发。我们贡献的代码主要来自Nova和Murano两个模块中，都是我们在开发和项目使用中发现的问题，修复后回馈给社区的，我也希望我们能在下一个版本Release中贡献更多的力量。

*** China Mobile社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-chinamobile.png)

排名第133位的是中国移动，之前并没有在哪一个排名上看到过中国移动在OpenStack贡献，我也是第一次发现。中国移动应该算是国内运营商领域技术实力较强的一家，也是运营商里开始从事OpenStack预研较早的一家。中国移动有大量的IT资源和设备，理应像AT&T一样在OpenStack领域大有所为。纵观中国移动的社区贡献，主要来自Neutron和Ceilometer两个项目，几个Bug修复都是与Volume相关。

*** Lenovo社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-lenovo.png)

排名第135位的是联想。不评论了。

排名第139位的是清华大学医学院附属医院，这个有点意思。但是stackalytics.com有Bug，他们的具体统计显示不出来。

*** H3C社区贡献统计 ***
![](/images/blogs/contribution-in-liberty-h3c.png)

排名第143位的是H3C。贡献是Nova中的关于VMware的Bug Fix。

由于stackalytics并没有按照区域统计的功能，所以本次统计完全是全自动统计(全靠我自己手动)，所以难免遗漏了为OpenStack贡献的国内企业，如果发生该情况请及时告知。

## 社区贡献内容分析

![](/images/blogs/contribution-in-liberty-complete-blueprints.png)

从贡献的commits的类型来区分，国内贡献出的代码主要还是以bug为主，这可能也与我们使用的都是OpenStack较成熟的模块有关，本身这些模块成熟程度较高，所以想做blueprint很难。另外一个很重要的原因是和OpenStack管理流程有关的，现在像Nova, Cinder等项目都是需要先Review Specs的，其实就是所谓的设计文档，语言成为国内很多工程师贡献的最大障碍，所以这也导致了Blueprint的贡献度在国内并不高。

*** Huawei社区贡献——完成Blueprint ***
![](/images/blogs/contribution-in-liberty-blueprint-huawei.png)

纵观整个Blueprint的完成统计情况，华为作为国内最有实力的企业，高居全球第五名，完成最多的模块为cinder和mistral。

之后能完成Blueprint的企业还包括UnitedStack、中国移动、麒麟云、海云捷迅和九州云，但是相比来说数量较少，都是个位数字。

OpenStack在国内发展已经超过了四年的时间，但是遗憾的一点，尽管我们拥有世界上最多的开发人员，但是我们对社区仍然没有话语权，国内的用户的需求无法对社区上游形成影响，导致很多本地化定制的需求无法真正的在社区版本代码得到体现。所以如何让中国的声音出现在社区，是我们所有OpenStack人需要思考的问题。欣喜的一点，本土的巨头华为已经身先士卒，投入很大的力量搞OpenStack的社区贡献，我们更希望越来越多的国内传统IT巨头能够意识到这个问题，投身于开源的事业中，否则我们又在起跑线上输给了别人。

以上仅代表个人观点，如有任何异议，欢迎批评指正。
