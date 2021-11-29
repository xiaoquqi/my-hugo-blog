---
title: "[Python]利用ZooKeeper构建分布式定时任务"
date: 2020-03-24 20:39:06
tags: ['Zookeeper', '微服务', '分布式', 'Python', 'tooz']
---

本文涉及的源代码路径：[https://github.com/xiaoquqi/openstackclient-demo/tree/master/tooz](https://github.com/xiaoquqi/openstackclient-demo/tree/master/tooz)

## 一、目前现状及存在的问题
在实际业务系统中，经常有需要定时执行的任务，例如任务状态的定时更新、定时发送状态信息等。在我们的云迁移产品中，允许用户可以设定周期同步规则，定期执行数据同步并调用云平台接口执行快照操作。在单机版本中，通常在同一时间点并发任务量较少的情况下，问题并不是很突出，但是随着我们将云迁移服务从单机版本改造为平台版本后，当多个用户的多台主机同时触发快照任务时，一方面传统的设计方式就成为了瓶颈，无法保证用户的同步任务在同一时间点被触发（需要排队）；另外一方面，目前Active-Passive（简称AP方式）的高可靠部署方式无法利用集群横向扩展能力，无法满足高并发的要求。

![](/images/blogs/2020-03-24/1.png)

<!-- more -->

### 软件架构设计
目前云迁移平台的各个服务模块在设计上使用了OpenStack方式，即大部分模块复用了类似Nova的实现框架。即API层直接集成oslo.service中定义好的WSGI Service基类，Worker采用了olso.service中定义好的Service基类，即Eventlet协程方式，API与Worker通讯使用RabbitMQ，API南向接口除少量直接更新数据库操作采用同步接口外，其余所有接口全部使用异步方式。API发送请求后，得到202 Accepted回复，后续通过GET接口不断轮询任务接口等到任务完成。

### 高可靠部署
根据OpenStack官方的HA部署文档（[https://docs.openstack.org/ha-guide/](https://docs.openstack.org/ha-guide/)），将服务分为无状态和有状态两种。无服务状态只需要直接部署多份即可，有状态服务往往需要通过Pacemaker控制副本数量，来保证高可靠。在云迁移平台部署中，我们将全部服务部署于K8S集群中，所以并不需要Pacemaker+Corosync这样的组件（Pacemaker节点上线为16）。但是，由于需要保持定时任务在单一节点被触发（避免任务被重复执行），所以承载定时快照的模块只能同时存在一个容器在运行，无法构成Active-Active（简称AA方式）模式。这样的部署方式，也造成了上述提到的AP模式对扩展性的瓶颈。

## 二、问题思路及解决方案

### 思路一、利用消息队列解耦任务分配与任务执行
从上述对现状的描述，我们不难看出，现有任务分配与任务执行是在同一个任务中执行的，当存在大量任务时，任务执行会对任务产生产生很大的影响。同时，由于任务执行唯一性的需要，在部署上只能采用上述的AP模式，导致任务无法由多个任务同时执行。<br />所以，我们可以将任务分解为分配和执行两个阶段。任务分配上，单纯的进行任务生成，由于任务生成相对较快，生成后的任务发送至消息队列，由无状态性的Worker接收后执行。这样就解决了单点执行的效率低下问题。<br />但是这样的解决方案仍然存在缺陷，我们在任务生成的模块仍然必须需要采用AP模式部署，来保证任务的唯一性。如果在任务数量非常庞大时，该部分仍然是一个瓶颈；另外一方面这样的实现方式，我们需要将任务生成部分单独拆分出一个模块，同时增加了开发和部署上的复杂度，所以我们来看一下第二种解决思路。

![](/images/blogs/2020-03-24/2.png)

### 思路二、利用Zookeeper构建可扩展的分布式定时任务
为了解决思路一的局限性，我们本质上要解决的是任务执行的分布式问题，即如何让Worker不重复的判定任务的归属后再执行，由被动改为主动。

我们来看以下几种场景：<br />1、假定我们现在有3个Worker可以用于任务生成，在某一个时间点，将同时产生100个任务。如何由这3个Worker主动产生属于自身负责的任务？<br />2、我们知道大部分云平台目前都有云原生的弹性扩展服务，如果我们结合云平台的弹性扩展服务自动将我们用于任务生成的Worker动态进行调整时，例如变为6个时，还能保证这100个任务能够被自动的由6个节点不重复的产生呢？<br />3、当负载降低后，节点数量由6个变为3个后，如何恢复场景1的状态呢？保证任务不漏生成呢？

![](/images/blogs/2020-03-24/3.png)

如果想达到以上场景需求，需要以下几个条件：<br />1、节点之间能够准确知道其他节点的存在——利用Zookeeper进行服务发现<br />2、尽量合理的进行任务（对象）分布，同时兼顾节点增加和减少时，降低对象分配时的位移——利用一致性哈希环

## 三、技术要点

### 1、Zookeeper
对于Zookeeper的解释网络上有各种各样的详细集成，这里就不再赘述了，这里我直接引用了这篇文章（https://www.jianshu.com/p/50becf121c66）中开头的内容：
> 官方文档上这么解释zookeeper，它是一个分布式服务框架，是Apache Hadoop 的一个子项目，它主要是用来解决分布式应用中经常遇到的一些数据管理问题，如：统一命名服务、状态同步服务、集群管理、分布式应用配置项的管理等。
> 上面的解释有点抽象，简单来说zookeeper=文件系统+监听通知机制。

![](/images/blogs/2020-03-24/4.png)

从我们应用场景的角度看，Zookeeper帮我们解决了Worker之间相互认识的过程，及时、准确的告诉我们：到底现在有多少个和我相同的活跃节点存在。至于底层是如何实现的，感兴趣的同学可以查看具体的Zookeeper实现原理文档，这里只介绍与我们实现相关的内容。

### 2、一致性Hash

又是一个经典的算法，相关的文章也很多，这里推荐大家几篇，这里摘抄出对理解我们实现有价值的内容。 参考文档：

* 《面试必备：什么是一致性Hash算法？》[https://zhuanlan.zhihu.com/p/34985026](https://zhuanlan.zhihu.com/p/34985026)
* 《五分钟看懂一致性哈希算法》[https://juejin.im/post/5ae1476ef265da0b8d419ef2](https://juejin.im/post/5ae1476ef265da0b8d419ef2)
* 《一致性hash在分布式系统中的应用》[http://www.firefoxbug.com/index.php/archives/2791/](http://www.firefoxbug.com/index.php/archives/2791/)

#### 2.1 关于一致性哈希算法

> 一致性哈希算法在1997年由麻省理工学院的Karger等人在解决分布式Cache中提出的，设计目标是为了解决因特网中的热点(Hot spot)问题，初衷和CARP十分类似。一致性哈希修正了CARP使用的简单哈希算法带来的问题，使得DHT可以在P2P环境中真正得到应用。但现在一致性hash算法在分布式系统中也得到了广泛应用。

#### 2.2 一致性哈希算法在缓存技术中的应用

![](/images/blogs/2020-03-24/5.png)

> 上述的方式虽然提升了性能，我们不再需要对整个Redis服务器进行遍历！但是，使用上述Hash算法进行缓存时，会出现一些缺陷，主要体现在服务器数量变动的时候，所有缓存的位置都要发生改变！
> 试想一下，如果4台缓存服务器已经不能满足我们的缓存需求，那么我们应该怎么做呢？很简单，多增加几台缓存服务器不就行了！假设：我们增加了一台缓存服务器，那么缓存服务器的数量就由4台变成了5台。那么原本hash(a.png) % 4 = 2 的公式就变成了hash(a.png) % 5 = ？ ， 可想而知这个结果肯定不是2的，这种情况带来的结果就是当服务器数量变动时，所有缓存的位置都要发生改变！换句话说，当服务器数量发生改变时，所有缓存在一定时间内是失效的，当应用无法从缓存中获取数据时，则会向后端数据库请求数据（还记得上一篇的《缓存雪崩》吗？）！
> 同样的，假设4台缓存中突然有一台缓存服务器出现了故障，无法进行缓存，那么我们则需要将故障机器移除，但是如果移除了一台缓存服务器，那么缓存服务器数量从4台变为3台，也是会出现上述的问题！
> 所以，我们应该想办法不让这种情况发生，但是由于上述Hash算法本身的缘故，使用取模法进行缓存时，这种情况是无法避免的，为了解决这些问题，Hash一致性算法（一致性Hash算法）诞生了！

#### 2.3 一致性哈希在缓存中的应用

初始状态，将节点映射到哈希环中

![](/images/blogs/2020-03-24/6.png)

将对象映射到换后，找到负责处理的Node节点。

![](/images/blogs/2020-03-24/7.png)

容错性，Node C出现故障后，只需要将Object C迁移到Node D上。

![](/images/blogs/2020-03-24/8.png)

增加节点，此时增加了Node X，在Node C右侧，那么此时只有Object C需要移动到Node X节点。

![](/images/blogs/2020-03-24/9.png)

### 3、tooz和kazoo

Python中操作zookeeper的项目叫kazoo（[https://kazoo.readthedocs.io/en/latest/](https://kazoo.readthedocs.io/en/latest/)）。<br />tooz是OpenStack中为简化开发人员操作分布式系统一致性所开发的组件，利用底层组件抽象出一致性组成员管理、分布式锁、选举、构建哈希环等。tooz除支持zookeeper作为后端，还可以支持Memcached、Redis、IPC、File、PostgreSQL、MySQL、Etcd、Consul等。<br />有关于tooz的发展历史可以参考：[https://julien.danjou.info/python-distributed-membership-lock-with-tooz/](https://julien.danjou.info/python-distributed-membership-lock-with-tooz/)<br />这里我们主要使用tooz操作zookeeper实现我们的一致性组及一致性哈希。

### 4、oslo相关项目
这几年一直在做OpenStack项目，从OpenStack项目中学习到很多设计、架构、研发管理等各种新知识、新理念。oslo项目就是在OpenStack不断的迭代中产生的公共项目库，这些库可以让你非常轻松的构建基于Python的构建近似于OpenStack的分布式、可扩展的微服务系统。<br />之前在从事OpenStack开发培训过程中，有专门的一节课去讲解OpenStack中用到的公共库，其中oslo相关项目就是非常重要的一部分内容。olso项目设计的库非常多，在这个内容中会涉及到oslo.config、oslo.log、oslo.service、oslo.utils和oslo.messaging项目。严格意义上来说，为了更精准控制任务，我们还应该引入oslo.db项目由数据库持久化的维护任务运行状态，包括任务回收等工作，但是本次内容主要讲解的是zookeeper，所以这部分的内容需要开发者在实际项目中去实现。<br />关于olso开发的内容，我会以视频课程的形式为大家讲解，敬请期待。

## 四、实现过程

### 1、Zookeeper部署
```bash
docker-compose -f zookeeper.yml -d up
```

启动完成后，将使用本地的三个容器作为zookeeper的三个节点和三个不同的端口（2181/2182/2183）便于zookeeper连接。如果在生产环境中部署时，可以使用云原生服务或部署在多个可用区的方式，保证高可靠。

![](/images/blogs/2020-03-24/10.png)

#### Zookeeper常用命令行
进入容器，就可以使用zkCli.sh进入zookeeper的CLI模式。如果是初次接触zookeeper，可以把zookeeper理解成一个文件系统，这里我们常用的命令就是ls。
```bash
docker exec -it zookeeper_zoo1_1 bash
cd bin
zkCli.sh
```

看到这样的提示，就表示连接成功了。

![](/images/blogs/2020-03-24/11.png)

如上面提到的zookeeper的存储结构所示，我们先从根节点（/）进行获取。
```bash
ls /
```

此时返回

![](/images/blogs/2020-03-24/12.png)

这里zookeeper目录属于保留的目录，我们来看一下tooz的内容。
```bash
ls /tooz
```

此时返回

![](/images/blogs/2020-03-24/13.png)

如果我们想继续查看distribution_tasks的内容，可以继续使用ls命令获取。
```bash
ls /tooz/distribution_tasks
```

通常我们会为每一个加入的节点取一个唯一的标识，当节点加入后我们使用ls命令就可以看到，如果离开了，则返回为空。

![](/images/blogs/2020-03-24/14.png)

zookeeper常用的命令还包括get，stat等获取value和更详细的信息，还包含更新节点操作set和删除节点rm。这里面就不做一一介绍了，我们直接操作zookeeper主要是为了帮助大家更好的理解程序逻辑。<br />具体的命令行信息可以参考：[https://www.tutorialspoint.com/zookeeper/zookeeper_cli.htm](https://www.tutorialspoint.com/zookeeper/zookeeper_cli.htm)

### 2、tooz基本使用方法
关于tooz的两个示例主要来自于这篇博客：[https://dzone.com/articles/scaling-a-polling-python-application-with-tooz](https://dzone.com/articles/scaling-a-polling-python-application-with-tooz)<br />原文中的例子是有些Bug的，这里面进行重新进行了优化和整理，并且使用zookeeper替代etcd3驱动。

#### 2.1 组成员（tooz/test_tooz/test_group_members.py）
在这个例子中，我们主要为大家演示tooz如何进行组成员的管理。结合我们自身的需求，这里的成员就是每一个Worker。通过这个列子我们将观察三种不同场景的变化：<br />1、初始状态下，我们只能看到一个成员；<br />2、当启动了一个新的进程时，第一个成员马上会发现有第二个成员的加入；<br />3、同时，当我们用CTRL + C结束某一个进程时，另外一个活着的进程会立即发现组成员的变化。

##### 时序图
这里为了更直观表达，用时序图来说明程序的运行逻辑。

![](/images/blogs/2020-03-24/15.png)

##### 完整的代码
```python
##!/usr/bin/env python
## -*- coding: utf-8 -*-

from datetime import datetime
import sys
import time

from tooz import coordination

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ZOOKEEPER_URL = "zookeeper://localhost:2181"

## Check that a client and group ids are passed as arguments
if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

## Get the Coordinator object
c = coordination.get_coordinator(ZOOKEEPER_URL, sys.argv[1].encode())
## Start it (initiate connection).
c.start(start_heart=True)

group = sys.argv[2].encode()

## Create the group
try:
    c.create_group(group).get()
except coordination.GroupAlreadyExist:
    pass

## Join the group
c.join_group(group).get()

try:
    while True:
#        # Print the members list
#        #c.run_watchers()
        members = c.get_members(group).get()
        print("[%s]Current nodes in cluster: %s" % (
            current_time(), members))
        time.sleep(1)
except KeyboardInterrupt as e:
    print("CTRL C is pressed!")
finally:
#    # Leave the group
    c.leave_group(group).get()
    print("[%s]After leave cluster nodes: %s" % (
        current_time(), c.get_members(group).get()))
#    # Stop when we're done
    c.stop()
```

##### 执行效果

第一个成员
```bash
python test_group_members.py client1 group1
```

![](/images/blogs/2020-03-24/16.png)

第二个成员加入，观察第一个成员的标准输出，为了观察加入集群的时间，我们加入了date
```bash
date && python test_group_members.py client2 group1
```

![](/images/blogs/2020-03-24/17.png)

第一个脚本的标准输出，在16:07:27秒的时候加入了集群:

![](/images/blogs/2020-03-24/18.png)

将第二个成员关闭，直接在第二个成员脚本按CTRL + C，首先观察第二个成员的输出：

![](/images/blogs/2020-03-24/19.png)

第一个成员的输出，在16:08:51分时，集群中已经没有了第二个成员了：

![](/images/blogs/2020-03-24/20.png)

#### 2.2 一致性哈希（tooz/test_tooz/test_ping.py）

这个模拟测试中，使用分布式任务去ping某一个C类网段(255个IP地址)中的全部IP地址，如果由一个任务去完成，那么只能顺序执行，无法满足并发需求，这里采用一致性哈希算法，让任务分布在各个Worker上。为了节省时间，我们将原有程序中的实际ping换成了time.sleep等待方式。<br />另外在程序启动后，我们默认等待10秒等待其他成员(member)加入，在实际开发过程中，还需要对任务的状态进行严格控制，防止同一任务重复被执行，在演示代码中主要偏重演示分布式，所以并没有在任务状态上增加过多处理。

##### 时序图

![](/images/blogs/2020-03-24/21.png)

代码需要说明的几点：<br />0、在程序开始时，我们默认等待了10秒，等待其他节点加入，如果在循环开始后，再有新加入的节点时，由于并不知道第一个节点已经处理过的任务，所以在第二个Worker加入后根据当时哈希环对之前的任务重新分配并执行，造成了重复执行，这个问题需要通过额外的手段（例如数据库记录先前执行的任务状态）监控任务状态来防止任务重新执行。<br />1、代码中使用了tooz内置的Hash环，但是也可以在外部自己构建哈希环，我们在后续最终的例子中还是采用了外部构建哈希环的方法。<br />2、Tooz partitioner依赖于watchers，所以在每次循环的时候必须要调用run_watchers即使获取成员的加入和离开。<br />3、无论是group还是member在变量传递时都要变成bytes类型，这样可以确保对象的唯一性，所以在代码处理上都用到了encode()方法。<br />4、__tooz_hash__方法需要在使用Partition时自己实现，能够唯一标识出对象的方法，例如ID、名称等信息。

##### 完整的代码
```python
##!/usr/bin/env python
## -*- coding: utf-8 -*-

from datetime import datetime
import sys
import subprocess
import time

from tooz import coordination

def current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ZOOKEEPER_URL = "zookeeper://localhost:2181"

## Check that a client and group ids are passed as arguments
if len(sys.argv) != 3:
    print("Usage: %s <client id> <group id>" % sys.argv[0])
    sys.exit(1)

## Get the Coordinator object
c = coordination.get_coordinator(ZOOKEEPER_URL, sys.argv[1].encode())

## Start it (initiate connection).
c.start(start_heart=True)

group = sys.argv[2].encode()

## Join the partitioned group
p = c.join_partitioned_group(group)

class Host(object):
    def __init__(self, hostname):
        self.hostname = hostname

    def __tooz_hash__(self):
        """Returns a unique byte identifier so Tooz
           can distribute this object."""
        return self.hostname.encode()

    def __str__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.hostname)

    def ping(self):
        time.sleep(2)
        return True

hosts_to_ping = [Host("192.168.10.%d" % i) for i in range(20)]

print("[%s]Waiting 10 seconds for other members..." % current_time())
time.sleep(10)
print("[%s]Current members: %s" % (
    current_time(), c.get_members(group).get()))

try:
    while True:
        for host in hosts_to_ping:
            c.run_watchers()
            if p.belongs_to_self(host):
                print("[%s]%s belongs to %s" % (
                    current_time(), host, p.members_for_object(host)))
                if host.ping():
                    pass
        print("=" * 60)
        print("Waiting for next loop...")
        time.sleep(10)
except KeyboardInterrupt as e:
    print("CTRL C is pressed!")
finally:
#    # Leave the group
    c.leave_group(group).get()

#    # Stop when we're done
    c.stop()
```

##### 执行效果
我们分别使用两个不同的窗口，同时启动两个Worker，我们可以很明显的看到主机被分配到两个不同的Worker中。
```bash
python test_ping.py client1 group1
python test_pring.py client2 group1
```
![](/images/blogs/2020-03-24/22.png)

加入第三个Worker，可以看到一部分任务又被分配给了第三个Worker上
```bash
python test_ping.py client3 group2
```

![](/images/blogs/2020-03-24/23.png)

### 
暂停第二个Worker，我们看到第二个Worker被停止后，任务重新被平衡到Worker1和Worker2上。

![](/images/blogs/2020-03-24/24.png)

### 3、构建分布式定时任务
为了保持代码的兼容性，所以这里的实现是基于目前OpenStack体系的实现。另外，将任务发送给消息的部分在这个例子中并没有体现。示例代码仍然重复实现上述ping的例子，部分代码参考于Sahara项目的实现。

由于代码量较大，这里不贴出全部代码，仅仅对核心实现进行分析，完整代码请参考：[https://github.com/xiaoquqi/openstackclient-demo/tree/master/tooz/distribute_periodic_tasks](https://github.com/xiaoquqi/openstackclient-demo/tree/master/tooz/distribute_periodic_tasks)

#### 代码结构
```
.
├── coordinator.py -> 一致性哈希的实现，该类中并没有直接使用上述tooz的partition，而是自己重新实现了HashRing
├── periodic.py -> 定时任务，基于oslo_service的PeriodicTasks基类
├── service.py -> Service类，继承于oslo.service的Service基类
└── test_periodic_task.py -> 程序入口
```

#### coordinator.py
Coordinator是关键实现，所以这里重点对该类进行解释，在period task中需要调用coordinator即可实现分布式触发定时任务。

在coordinator.py中共实现了两个类，Coordinator和HashRing。<br />1、Coordinator类主要是针对tooz中对group members相关操作的封装，类似我们在tooz中的第一个例子；<br />2、HashRing是继承于Coordinator类，在功能上接近于tooz中Hash和Partition的实现，但是更简洁，tooz构建HashRing的用的PartitionNumber是32(2^5)，而我们用的是40，更大的数字会带来更均匀的分布但是会导致构建成本增加<br />3、HashRing中最重要的方法就是get_subset，通过映射到HashRing上的ID来判断Object的归属Worker

![](/images/blogs/2020-03-24/25.png)

```python
class HashRing(Coordinator):
    def __init__(self, backend_url, group_id):
        self.group_id = group_id
        self.replicas = CONF.hash_ring_replicas_count
        super(HashRing, self).__init__(backend_url)
        self.join_group(group_id)

    @staticmethod
    def _hash(key):
        return int(
            hashlib.md5(str(key).encode('utf-8')).hexdigest(), 16)  # nosec

    def _build_ring(self):
        ring = {}
        members = self.get_members(self.group_id)
        LOG.info("Coordinator members: %s" % members)
        for member in members:
            for r in range(self.replicas):
                hashed_key = self._hash('%s:%s' % (member, r))
                ring[hashed_key] = member

        return ring, sorted(ring.keys())

    def _check_object(self, object, ring, sorted_keys):
        """Checks if this object belongs to this member or not"""
        hashed_key = self._hash(object.id)
        position = bisect.bisect(sorted_keys, hashed_key)
        position = position if position < len(sorted_keys) else 0
        return ring[sorted_keys[position]] == self.member_id

    def get_subset(self, objects):
        """Returns subset that belongs to this member"""
        if self.coordinator:
            ring, keys = self._build_ring()
            if ring:
                return [obj for obj in objects if self._check_object(
                    obj, ring, keys)]
            return []
        return objects
```

#### 运行效果
分别在两个Terminal中运行脚本，可以看到Host被均匀的分布在两个Worker中执行。
```python
python test_periodic_task.py
```

![](/images/blogs/2020-03-24/26.png)

## 五、总结
通过以上实例，我们了解了如何通过zookeeper构建分布式系统并进行任务调度，当然zookeeper在分布式系统还有更多的应用场景值得我们去学习。另外，OpenStack中很多抽象出来的模块对快速构建Python分布式系统是非常有帮助的，值得我们学习。
