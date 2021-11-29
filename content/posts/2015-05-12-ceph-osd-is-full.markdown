---
layout: post
title: "Ceph集群磁盘没有剩余空间的解决方法"
date: 2015-05-12 09:21:42 +0800
comments: true
categories: [openstack, ceph]
---

## 故障描述

OpenStack + Ceph集群在使用过程中，由于虚拟机拷入大量新的数据，导致集群的磁盘迅速消耗，没有空余空间，虚拟机无法操作，Ceph集群所有操作都无法执行。

<!-- more -->

## 故障现象

* 尝试使用OpenStack重启虚拟机无效
* 尝试直接用rbd命令直接删除块失败

``` plain
[root@controller ~]# rbd -p volumes rm volume-c55fd052-212d-4107-a2ac-cf53bfc049be
2015-04-29 05:31:31.719478 7f5fb82f7760  0 client.4781741.objecter  FULL, paused modify 0xe9a9e0 tid 6
```

* 查看ceph健康状态

``` plain ceph -s
cluster 059f27e8-a23f-4587-9033-3e3679d03b31
 health HEALTH_ERR 20 pgs backfill_toofull; 20 pgs degraded; 20 pgs stuck unclean; recovery 7482/129081 objects degraded (5.796%); 2 full osd(s); 1 near full osd(s)
 monmap e6: 4 mons at {node-5e40.cloud.com=10.10.20.40:6789/0,node-6670.cloud.com=10.10.20.31:6789/0,node-66c4.cloud.com=10.10.20.36:6789/0,node-fb27.cloud.com=10.10.20.41:6789/0}, election epoch 886, quorum 0,1,2,3 node-6670.cloud.com,node-66c4.cloud.com,node-5e40.cloud.com,node-fb27.cloud.com
 osdmap e2743: 3 osds: 3 up, 3 in
        flags full
  pgmap v6564199: 320 pgs, 4 pools, 262 GB data, 43027 objects
        786 GB used, 47785 MB / 833 GB avail
        7482/129081 objects degraded (5.796%)
             300 active+clean
              20 active+degraded+remapped+backfill_toofull
```

``` plain ceph health detail
HEALTH_ERR 20 pgs backfill_toofull; 20 pgs degraded; 20 pgs stuck unclean; recovery 7482/129081 objects degraded (5.796%); 2 full osd(s); 1 near full osd(s)
pg 3.8 is stuck unclean for 7067109.597691, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.7d is stuck unclean for 1852078.505139, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.21 is stuck unclean for 7072842.637848, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.22 is stuck unclean for 7070880.213397, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.a is stuck unclean for 7067057.863562, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.7f is stuck unclean for 7067122.493746, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.5 is stuck unclean for 7067088.369629, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.1e is stuck unclean for 7073386.246281, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.19 is stuck unclean for 7068035.310269, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.5d is stuck unclean for 1852078.505949, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.1a is stuck unclean for 7067088.429544, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.1b is stuck unclean for 7072773.771385, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.3 is stuck unclean for 7067057.864514, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.15 is stuck unclean for 7067088.825483, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.11 is stuck unclean for 7067057.862408, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.6d is stuck unclean for 7067083.634454, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.6e is stuck unclean for 7067098.452576, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.c is stuck unclean for 5658116.678331, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.e is stuck unclean for 7067078.646953, current state active+degraded+remapped+backfill_toofull, last acting [2,0]
pg 3.20 is stuck unclean for 7067140.530849, current state active+degraded+remapped+backfill_toofull, last acting [0,2]
pg 3.7d is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.7f is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.6d is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.6e is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.5d is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.20 is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.21 is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.22 is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.1e is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.19 is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.1a is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.1b is active+degraded+remapped+backfill_toofull, acting [0,2]
pg 3.15 is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.11 is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.c is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.e is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.8 is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.a is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.5 is active+degraded+remapped+backfill_toofull, acting [2,0]
pg 3.3 is active+degraded+remapped+backfill_toofull, acting [2,0]
recovery 7482/129081 objects degraded (5.796%)
osd.0 is full at 95%
osd.2 is full at 95%
osd.1 is near full at 93%
```
## 解决方案一(已验证)

增加OSD节点，这也是官方文档中推荐的做法，增加新的节点后，Ceph开始重新平衡数据，OSD使用空间开始下降

``` plain
2015-04-29 06:51:58.623262 osd.1 [WRN] OSD near full (91%)
2015-04-29 06:52:01.500813 osd.2 [WRN] OSD near full (92%)
```

## 解决方案二(理论上，没有进行验证)

如果在没有新的硬盘的情况下，只能采用另外一种方式。在当前状态下，Ceph不允许任何的读写操作，所以此时任何的Ceph命令都不好使，解决的方案就是尝试降低Ceph对于full的比例定义，我们从上面的日志中可以看到Ceph的full的比例为95%，我们需要做的就是提高full的比例，之后尽快尝试删除数据，将比例下降。

* 尝试直接用命令设置，但是失败了，Ceph集群并没有重新同步数据，怀疑可能仍然需要重启服务本身

``` plain
ceph mon tell \* injectargs '--mon-osd-full-ratio 0.98'
```

* 修改配置文件，之后重启monitor服务，但是担心出问题，所以没有敢尝试该方法，后续经过在邮件列表确认，该方法应该不会对数据产生影响，但是前提是在恢复期间，所有的虚拟机不要向Ceph再写入任何数据。

默认情况下full的比例是95%，而near full的比例是85%，所以需要根据实际情况对该配置进行调整。

``` plain /etc/ceph/ceph.conf
[global]
    mon osd full ratio = .98
    mon osd nearfull ratio = .80
```

## 分析总结

### 原因

根据Ceph官方文档中的描述，当一个OSD full比例达到95%时，集群将不接受任何Ceph Client端的读写数据的请求。所以导致虚拟机在重启时，无法启动的情况。

### 解决方法

从官方的推荐来看，应该比较支持添加新的OSD的方式，当然临时的提高比例是一个解决方案，但是并不推荐，因为需要手动的删除数据去解决，而且一旦再有一个新的节点出现故障，仍然会出现比例变满的状况，所以解决之道最好是扩容。

### 思考

在这次故障过程中，有两点是值得思考的：

* 监控：由于当时服务器在配置过程中DNS配置错误，导致监控邮件无法正常发出，从而没有收到Ceph WARN的提示信息
* 云平台本身： 由于Ceph的机制，在OpenStack平台中分配中，大多时候是超分的，从用户角度看，拷贝大量数据的行为并没有不妥之处，但是由于云平台并没有相应的预警机制，导致了该问题的发生

## 参考文档
* http://ceph.com/docs/master/rados/configuration/mon-config-ref/#storage-capacity
