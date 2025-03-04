---
title: 利用阿里云Serverless Kubernetes构建任务运行环境
author: 孙琦(Ray)
date: 2021-05-27 06:18:51
tags:
---
Kubernetes是容器编排首选平台，现在各大云商也都推出了自己的Kubernetes服务。但是搭建Kubernetes环境往往在初始节点上需要很多云主机支持，三个Master节点实现HA，三个Node作为计算节点，成本开销比较大。后来阿里云推出了部分托管版本的Kubernetes，即Master节点托管给阿里云，用户只需要根据需求创建Node节点，大大节省了开销。但是如果用户连Node节点都不想创建，希望做到真正的按需分配怎么办呢？那么，你可以使用阿里云基于容器平台ECI构建的全托管版本的Kubernetes，即Kubernetes Serverless版本。这种环境下，用户可以完全忽略Master和Node节点，你的所有服务都会自动运行在ECI容器实例中，而费用则根据你的容器实际运行的时间和存储占用收取。这种方式适合有限时间内的任务运行方式，大大节约计算资源费用支出。

<!-- more -->

## 服务创建

在服务目录找到Serverless容器服务ASK，进入后创建集群。

![upload successful](/images/pasted-245.png)

顶部选择创建ASK集群，这种才是不需要创建master和node节点的模式。

![upload successful](/images/pasted-246.png)

根据提示选择地域、版本和网络等信息。目前Kubernetes版本支持1.20.4和1.18.8两个版本，可以根据实际情况选择。另外如果你的集群有访问外网的需求，需要在选择网络的时候，确保你的VPC绑定了NAT网关，并正确配置了路由规则。

Serverless Kubernetes本身并不收取任何费用，都是通过调用的资源进行收费，在无使用的情况下，仅仅API Server使用的SLB会收取少量的费用，根据业务需求，适当选择SLB规格。如果需求不大，可以选择一个最小的。默认一天的价格大概在1.2元左右。另外，日志服务可以关闭掉，否则后期增长过快，也是一笔不小的开支。

![upload successful](/images/pasted-247.png)

配置完成后，点击创建，等待完成后，和正常的Kubernetes环境一样使用。

![upload successful](/images/pasted-248.png)

云商提供的Kubernetes所有操作都可以通过页面点击完成，即使你不会写yaml也可以使用这个集群。


## 存储创建

使用Kubernetes时需要对存储管理需要有一个认知，这里我只按照需求场景来分析一下，我们在实际使用中往往涉及到两种类型的数据：静态数据（例如配置文件）和动态数据（应用使用过程中产生的数据）。

### 静态数据

通常我使用“配置项”来对我的配置文件进行管理，配置项是一个键值对，最终在启动容器时，会以目录方式映射到容器内某个目录中。如果你对安全性有要求，还可以使用保密字典存放相关信息。

![upload successful](/images/pasted-249.png)

### 动态数据

动态数据的管理通过“存储”目录进行配置，最终映射到容器内的存储叫存储声明，而存储声明的背后是存储卷(Persistent Volume)或者存储类(Storage Class)。

![upload successful](/images/pasted-250.png)

这是Kubernetes官网对相关概念的诠释：

> StorageClass 为管理员提供了描述存储 "类" 的方法。 不同的类型可能会映射到不同的服务质量等级或备份策略，或是由集群管理员制定的任意策略。 Kubernetes 本身并不清楚各种类代表的什么。这个类的概念在其他存储系统中有时被称为 "配置文件"。
>
> 持久卷（PersistentVolume，PV）是集群中的一块存储，可以由管理员事先供应，或者 使用存储类（Storage Class）来动态供应。 持久卷是集群资源，就像节点也是集群资源一样。PV 持久卷和普通的 Volume 一样，也是使用 卷插件来实现的，只是它们拥有独立于任何使用 PV 的 Pod 的生命周期。 此 API 对象中记述了存储的实现细节，无论其背后是 NFS、iSCSI 还是特定于云平台的存储系统。

后端存储可以支持多种类型，例如：云盘、NAS或者对象存储，如果使用存储类还可以支持Ceph RBD、GlusterFS。可以根据应用的特点选择后端存储类型。存储类的配置稍微复杂，所以这里直接使用NAS作为后端存储。

#### NAS服务配置

NAS按量付费的模式，非常适合存储空间动态变化较大的场景，如果能选择合适的资源包，能做到成本最优。

![upload successful](/images/pasted-251.png)

NAS分为通用型和极速型，这里我们分别选择容量型和性能型。

![upload successful](/images/pasted-252.png)

#### 存储卷配置

回到Kubernetes存储管理中，创建存储卷，选择NAS，总量方面是指这个存储的可用量，默认通用型性能型NAS配额是1PB，而容量型是10PB，这里根据实际情况填写就可以了。另外需要选择挂载点信息。

![upload successful](/images/pasted-253.png)


## 任务创建

下面就可以正式启动容器了，这里之所以选择任务方式创建，是要有效的控制执行次数。当然这和你的业务类型有很大的关系。

![upload successful](/images/pasted-254.png)

第一步是基本信息填写，没有太特殊的。

![upload successful](/images/pasted-255.png)

第二步是主要配置，如果你的镜像仓库就是托管在阿里云容器服务内，建议使用vpc地址，这样避免产生不必要的流量。

![upload successful](/images/pasted-256.png)

下面就是对于存储的配置，在我的conf中包含两个文件，一个是oss的连接信息，另外一个secret words文件。这样每次执行完成后，会自动的将文件上传至OSS中。

另外选择我们刚刚配置的NAS存储。

![upload successful](/images/pasted-257.png)

第三步可以控制并发运行的数量。比如，我们希望并行的执行10个任务，则成功运行Pod数和并行运行的Pod数都设置成10，超时时间根据实际应用情况可以设置长一些，重启策略设置为不重启。

![upload successful](/images/pasted-258.png)

最后点击创建，任务就可以执行了。

![upload successful](/images/pasted-259.png)

最后，通过点击任务详情，查看日志，查看任务详情。

![upload successful](/images/pasted-260.png)

## 总结

使用Kubernetes Serverless特别适合按需使用的任务场景，配合各种资源包，能够大幅度降低成本，同时做到高并发。相关代码已经托管到github上，有兴趣的朋友可以一起共同完善，我的github账号为xiaoquqi。