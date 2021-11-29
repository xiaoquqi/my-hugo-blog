---
title: 公有云奇亚币(Chia)挖矿存储性能与成本分析
author: 孙琦(Ray)
date: 2021-05-15 08:15:18
tags:
---
在上一篇Blog中，主要针对使用NVMe云主机和Serverless两种方式进行了对比，通过对比我们可以看到，程序在运行时对于CPU、内存和网络要求并不高，在耕地过程中甚至可以无网情况下进行。那么问题的核心就来到了存储层面，通过观察，NVMe磁盘性能远远没有发挥到极致，那么是否有更经济同时又能保障一定效率的方法呢？

<!-- more -->

## 测试场景

为了测试简便，本次测试使用了云主机，直接选择高性能云硬盘作为临时盘，而NAS存储作为临时最终存储，对象存储作为最终资源的存储。主要配置为：

* 云主机规格：4核16G CentOS 7.5 64位 5Mbps按流量计费网络
* 磁盘：800GiB (41800 IOPS)

本次测试的目标是，在一定时间内，同时进行三个耕地，最后统计完成时间和成本。

## 测试结论

### 时间成本

#### 任务一

```
Starting phase 1/4: Forward Propagation into tmp files... Fri May 14 08:43:12 2021
Computing table 1
F1 complete, time: 518.681 seconds. CPU (59.49%) Fri May 14 08:51:50 2021
......
Time for phase 4 = 1201.084 seconds. CPU (61.850%) Fri May 14 21:41:05 2021
Approximate working space used (without final file): 269.269 GiB
Final File size: 101.315 GiB
Total time = 46673.510 seconds. CPU (82.100%) Fri May 14 21:41:05 2021
Copied final file from "/plots-tmp/1/plot-k32-2021-05-14-08-43-557d4b8d88279c4a6044080fd819bc93bbe1c0b74d51b1fecc120fca1358fa2b.plot.2.tmp" to "/plots-final/plot-k32-2021-05-14-08-43-557d4b8d88279c4a6044080fd819bc93bbe1c0b74d51b1fecc120fca1358fa2b.plot.2.tmp"
Copy time = 1549.110 seconds. CPU (9.160%) Fri May 14 22:07:03 2021
```

#### 任务二

```
Starting phase 1/4: Forward Propagation into tmp files... Fri May 14 08:43:42 2021
Computing table 1
F1 complete, time: 535.486 seconds. CPU (56.69%) Fri May 14 08:52:38 2021
......
Time for phase 4 = 1084.804 seconds. CPU (67.540%) Fri May 14 22:01:37 2021
Approximate working space used (without final file): 269.358 GiB
Final File size: 101.363 GiB
Total time = 47874.679 seconds. CPU (80.640%) Fri May 14 22:01:37 2021
Copied final file from "/plots-tmp/2/plot-k32-2021-05-14-08-43-279a5ec90eb78e42f19cd53c3fa6499c91b182539556fd1c9700793b18dc38b7.plot.2.tmp" to "/plots-final/plot-k32-2021-05-14-08-43-279a5ec90eb78e42f19cd53c3fa6499c91b182539556fd1c9700793b18dc38b7.plot.2.tmp"
Copy time = 1406.686 seconds. CPU (9.020%) Fri May 14 22:25:04 2021
```

#### 任务三

```
Starting phase 1/4: Forward Propagation into tmp files... Fri May 14 08:44:11 2021
Computing table 1
F1 complete, time: 560.029 seconds. CPU (53.53%) Fri May 14 08:53:31 2021
.....
Time for phase 4 = 1032.731 seconds. CPU (71.880%) Fri May 14 22:07:25 2021
Approximate working space used (without final file): 269.441 GiB
Final File size: 101.407 GiB
Total time = 48193.223 seconds. CPU (80.600%) Fri May 14 22:07:25 2021
Copied final file from "/plots-tmp/3/plot-k32-2021-05-14-08-44-d1bbf61fafb6284291bd3e2c181b3b0dea1853b5138f6f41a330ef814781cebe.plot.2.tmp" to "/plots-final/plot-k32-2021-05-14-08-44-d1bbf61fafb6284291bd3e2c181b3b0dea1853b5138f6f41a330ef814781cebe.plot.2.tmp"
Copy time = 1182.271 seconds. CPU (10.580%) Fri May 14 22:27:11 2021
```

#### 统计分析

|任务|生成时间(小时)|拷贝时间（小时）|总体耗时（小时)|
|  --  | --  | -- | -- |
|任务一|12.96|0.43|13.39|
|任务二|13.3|0.39|13.69|
|任务三|13.4|0.33|13.73|

通过分析可知，在这个规格上，并发完成三次耕地的成本约为14小时以内。


### 系统资源分析


#### 临时磁盘性能

![upload successful](/images/pasted-241.png)

![upload successful](/images/pasted-243.png)

#### 主机性能

![upload successful](/images/pasted-242.png)

#### 网络性能

![upload successful](/images/pasted-244.png)


### 费用

* 云主机费用：1.14 元/小时
* 临时硬盘费用：1.68 元/小时
* 总体费用：39 元，平均一块地的成本为13 元

## 结论

从费用角度来说，这种部署架构的成本与Serverless相差不大，但是构建的复杂性上要低于Serverless方式，适合对于技术不甚了解的朋友进行挖矿尝鲜。

另外从性能角度看，在并发环境下，磁盘性能差异性逐渐被放大，这时磁盘越快的确对并发挖矿的速度越有帮助。不过个人觉得这其实就是和应用架构的逻辑是一样的，虽然纵向扩展能够提高单体并发性，但是横向扩展能够通过时间换数量，最终在结果上取得优势，毕竟奇亚币是以数量取胜的。

但是这也引发了我另外的思考，分布式系统要解决的是管理问题，如果想提高并发挖矿能力，对于挖矿的控制就变得非常重要了。当然，这对于搞云计算的人来说并不复杂，利用各种自动化手段可以轻易实现最佳的成本控制。虽然官方也提供了一些手段，但是从成本最优的角度看，还远远不足，所有有兴趣的小伙伴可以一起来做一个开源项目满足这方面的需求。

最后有兴趣的朋友可以入群讨论：

![upload successful](/images/pasted-239.png)

如果加群失败，请添加个人微信号入群

![upload successful](/images/pasted-240.png)
