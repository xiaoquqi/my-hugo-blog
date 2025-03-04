---
title: 防止你的钱包掉进Serverless使用的坑
author: 孙琦(Ray)
tags:
  - Serverless
categories: []
date: 2022-12-18 21:51:00
---
今天读到InfoQ一篇《应用上云2小时烧掉近50万，创始人：差点破产，简直噩梦》讲述了在使用Serverless方式开发时由于程序Bug导致快速的资源消耗，差点破产的经历。特意查询了英文原文，题目叫做《We Burnt $72K testing Firebase - Cloud Run and almost went Bankrupt》。我之前在使用函数计算时也有一次类似经历，所以写出来供大家参考，防止你的钱包掉进Serverless使用的坑。

<!-- more -->

## 钱是如何被烧掉的？

如果要理解原文中为什么出现问题，先要了解一下Google Serverless的产品体系：

* Cloud Functions: 基于事件驱动的函数计算服务
* App Engine: 上一篇讲述Serverless发展过程的时候恰好提到过这个服务，是Google的PaaS平台，开发人员可以直接将代码托管在平台上运行，具有良好的扩展性
* Cloud Run: 无状态的Serverless HTTP容器，口号是 Bringing Serverless to Containers，可以执行任何语言
* Cloud Firestore: 是一种灵活且可扩缩的数据库，适用于在Firebase和Google Cloud Platform上进行移动、Web 和服务器开发。

从账单里可以看到，用户最消耗资源的费用是来自App Engine对Cloud Firestore读取次数达到惊人的千亿次，按照原文里的说法，这里仅仅是两个个小时的成绩。在惊叹费用的同时，我们不得不感叹云原生服务性能之优异。

![upload successful](/images/pasted-171.png)

作者针对这一事件前后共发布了三篇博客，第一篇主要还原事情的脉络，以及在使用Google服务时候的坑；第二篇在剖析自身的错误；最后一篇在作者感叹了一下自己的经历被翻译成各种语言，另外写了另外一篇《How to user Cloud without losing Sleep》防止大家踩坑。

通篇看下来，作者将问题归咎于几个地方：

* 核心问题：代码中包含Bug(Deploying flawed algorithm on Cloud)，不恰当的使用递归而形成死循环(Exponential Recursion without Break: The instances wouldn’t know when to break, as there was no break statement.)
* 测试环境中，Cloud Run默认并发实例时1000，测试环境中也使用了默认值，如果在测试环境选择并发数是2，那么费用将从72,000美金降到144美金
* 在没有完全掌握Firebase时探索性的使用，没想到Firebase性能这么强大（广告嫌疑）
* 基于云开发仍然要抱有对技术的敬畏心，云原生服务降低了运维和开发的难度，但是在使用方式、价格、配置等诸多因素的复杂度必然会与传统有很大的区别，正所谓软件工程领域没有银弹

## 我在函数计算上踩过的坑

之前在测试阿里云函数计算过程时，曾经也有过一次入坑经历。当时我写了一个简单的函数，当有.png文件上传至OSS后，就自动进行Resize操作，保存成三种规格16x16, 32x32, 64x64，之后重新传回到OSS。但是我忽略了一点，我将处理好的文件重新传输回了同一个OSS Bucket内，结果造成了一个死循环。

![upload successful](/images/pasted-172.png)

其实我所犯的错误和上面公司遇到的问题是一样的，不过好在我的这次错误没有导致很严重的后果。由于时间久远，我无法找到当时的截图。我只记得我的函数计算在短时间内调用了70万次，OSS上传了几百万个小文件。还好阿里云100万次内的访问是免费的，OSS价格比较便宜，但是还是惊出了一身冷汗。赶紧把我的函数服务下线，同时写了一个脚本删除小文件，因为没有直接的命令可以删除非空的Bucket，整个善后清理工作持续了几个小时。

## 如何防止踩坑

作为新的技术趋势，在前进的过程中难免遇到各种各样的问题。目前确实还没有一套指导规范帮助研发人员有效的避免踩坑。所以也需要大家在实践中不断总结。

* 做技术的人还是要有一颗敬畏的心，任何新技术的引进都会带来风险，所以在你没有十足的把握的时候，还是小心的比较好
* 云的并发性能真的太强大了，所以一定要做好发生异常时的应对方案，让并发性在你的可控范围内进行，控制”爆炸半径“
* Serverless的开发模式对研发流程是一个全新的挑战，在上述案例中问题出现在了测试阶段，不同于传统的测试，Serverless与开发更为紧密，对于白盒测试的要求更高，一方面需要做好单元测试，另外一方面对开发者综合考虑问题的素质要求更高，或许DevTest会成为Serverless在落地实践中需要解决的问题之一
* 动手与阅读文档并行，云服务的文档就和普通商品的说明书一样，没人会去主动阅读的，只有实在搞不出来的时候才会想着看一看，但是云服务不同于普通的产品，一些细枝末节的选项太多，还是应当在使用一段时间后回过头来通读文档的内容，加深理解

## 参考链接

* https://blog.tomilkieway.com/72k-1/
* https://blog.tomilkieway.com/72k-2/
* https://sudcha.com/guide-to-cloud/