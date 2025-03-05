---
title: OpenStack没落了吗？
author: 孙琦(Ray)
tags:
  - 趋势分析
  - OpenStack
categories: []
date: 2020-04-29 21:20:00
---
## OpenStack回顾

OpenStack在2010年7月由NASA和Rackspace宣布启动，2010年10月Austin Release后，除了Bexar、Cactus、Diablo版本外，后续版本都遵循6个月发布周期，如今正在开发的是Ussuri版本，最新的稳定版本是去年10月份发布的Train版本。

![upload successful](/images/pasted-42.png)


## OpenStack没落了吗？

我是从2012年初开始参与到OpenStack社区，这几年见证了OpenStack从一个开源项目逐渐成为开源产品的全过程。大概在两三年前每次发布前都会写一些关于OpenStack新版本功能和社区分析的文章，但是随着我的工作重心转移，对OpenStack社区关注逐渐减少。

<!-- more -->

随着容器、K8S等新兴技术的崛起，OpenStack无疑受到了很大的冲击，在之前两年经常看到一些唱衰OpenStack的文章。但是不可否认，目前OpenStack已经进入到了一个稳定阶段，很多私有云、专有云项目都是基于OpenStack提供解决方案。所以我认为并不存在OpenStack没落一说，只是技术发展的必经阶段：当底层逐渐稳定后，关注度往上发展。

同时，我们也看到，OpenStack基金会也在通过吸纳更多的项目来维持自身的影响力，比如：安全容器项目Kata Container，边缘计算项目StarlingX。

这是我对目前国内云计算市场的一张不完全总结，从这张图中我们应该可以很清晰的看到OpenStack对国内云计算市场深远的影响。同时，大家也能看出来谁才是真正的OpenStack这个开源项目的既得利益者。

![upload successful](/images/pasted-44.png)

## OpenStack社区大数据

从A版本开始到今天（2020年4月29日），总共有442家公司为OpenStack社区贡献过代码。排名前三位的分别是：Red Hat, Rackspace和Mirantis。中国唯一入选前十的是华为。

![upload successful](/images/pasted-45.png)

OpenStack总共出现了706个Official项目，提交代码次数最多的是nova, neutron和cinder项目。

![upload successful](/images/pasted-46.png)

总共有8523名开发者成功提交过1个以上的commits。从名字分析，前十名中有两位中国人：Zhong Shengping（麒麟云，主要贡献在自动化安装OpenStack相关项目puppet和ansible）和Qiming Teng（IBM 滕启明博士，主要贡献在senlin项目）。当然，我知道国内为OpenStack项目贡献的人很多，在这就不一一列举了。

![upload successful](/images/pasted-47.png)

## OpenStack社区贡献变化趋势

参与贡献的公司已经呈现明显下降趋势，从国内情况来看，很多OpenStack初创公司也在积极投身K8S相关项目的研究，产品上提供基于容器的PaaS平台，丰富自己的解决方案。
从图中可以看到，OpenStack参与公司最多的是在Ocata Release中，参与公司达到了210家，从时间看是在2016年到2017年之间的时间点。这也是国内客户对OpenStack普遍接受的时间点。
另外从C版本开始一直到O版本（2011年到2017年）基本每个版本迭代维持20%以上的增长，可见在这个阶段绝大多数公司都看好OpenStack的未来。国内开源领域在这个阶段感觉也是最活跃的，毕竟只有当商业利益和开源目标相吻合时，这个开源项目才能得到最大的支持力度。
从O版本之后，参与的公司呈现小幅度下降趋势，不是很明显，大概在10%以内，下跌最明显的阶段是在S版本到T版本，也就是2019年。S版本有161家公司提交代码，而T版本只有126家，而目前U版本已经下降到了119家公司。

![upload successful](/images/pasted-48.png)

从开发者数量看也呈现出相同的趋势，参与人数最多的是N版本，有2422人提交了commit。而到了S版本开发者仅为1189人，下降了一半还多。

![upload successful](/images/pasted-49.png)

最后一张图，我们来看一下OpenStack模块数量。在早期OpenStack中一个新的项目获得批准是需要技术委员会批准的，也就是TC Approved，这样的项目到今天为止一共只有20个，主要是OpenStack基础的计算、存储和网络服务，包括：Nova, Neutron, Cinder, Heat, Horizon, Keystone, Ironic, Swift, Ceilometer, Glance, Sahara, Trove, Designate, neutron-lib, sahara的各种插件。
但是在2015年，社区决定采用Big Tent模式。Big Tent模式本意是基于OpenStack底层的计算、存储和网络等基础组件，构建更庞大的云原生应用场景，类似AWS。但是由于OpenStack自身部署、升级的复杂性，是社区力量更加分散，这样的设计并没有带来意料之中的效果。我个人理解，这样的生态建设更适合K8S。
在A版本中仅有8个模块，到了最新的T版本中，模块数量变为609个，还没有Release的U版本中，模块数量增长为627个。

![upload successful](/images/pasted-50.png)

## 总结

由于OpenStack提供的服务属于基础架构层，从生态角度看，团结了各个层面的公司。从硬件的服务器、处理器、网络、存储厂商，到操作系统厂商，再到OpenStack创业公司，应用厂商，直到最终用户。
之前我们总说OpenStack是仅次于Linux的世界上第二大开源社区，不知道现在这种说法是否还准确。但是不可否认，OpenStack出现给了原来默默耕耘的开发者们走到前台充分展现的机会，也将国内开源的热潮推向了一个新的高度。