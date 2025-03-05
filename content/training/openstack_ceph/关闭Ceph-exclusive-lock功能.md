---
title: 关闭Ceph exclusive-lock功能
author: 孙琦(Ray)
date: 2021-08-02 23:18:47
tags:
---
当OpenStack计算和存储一体节点强制重启后，会导致虚拟机无法启动，卡在I/O error上，究其原因是由于底层rbd设备的exclusive-lock造成的。有两种解决方案，一种是临时性的解除exclusive-lock client，一种则是关闭rbd的exclusive-lock。

<!-- more -->

## 解除exclusive-lock client

查看exclusive-lock client(pool的名字为volumes)

```
[root@compute201 ~]# rbd lock ls volumes/volume-cad6425c-4453-4489-b2d1-45050b062bd2
There is 1 exclusive lock on this image.
Locker           ID                   Address
client.14440803  auto 93942189655296  10.0.100.202:0/1431194814
```

尝试删除client

```
rbd lock remove volumes/volume-cad6425c-4453-4489-b2d1-45050b062bd2 "auto 93942189655296" client.14440803
```

最后尝试重启相应的虚拟机，此时应该可以正常进入系统。

## 关闭exclusive-lock功能

通过查看rbd info，获取当前卷是否开启了exclusive-lock

```
[root@compute201 ~]# rbd info volumes/volume-cad6425c-4453-4489-b2d1-45050b062bd2
rbd image 'volume-cad6425c-4453-4489-b2d1-45050b062bd2':
	size 50 GiB in 12800 objects
	order 22 (4 MiB objects)
	snapshot_count: 0
	id: dc59383d97f124
	block_name_prefix: rbd_data.dc59383d97f124
	format: 2
	features: layering, exclusive-lock, object-map, fast-diff, deep-flatten
	op_features:
	flags:
	create_timestamp: Fri Jun 18 16:28:44 2021
	access_timestamp: Mon Jun 21 15:17:38 2021
	modify_timestamp: Mon Aug  2 23:07:58 2021
	parent: images/9e8a401b-d407-4946-b94c-f24b94ce0f02@snap
	overlap: 8 GiB
```

关闭exclusive-lock功能，这里必须要和object-map或journaling一起关闭才能生效

```
rbd feature disable volumes/volume-cad6425c-4453-4489-b2d1-45050b062bd2 exclusive-lock,object-map
```

再次查看功能列表，features只剩下layering和deep-flattern

```
[root@compute201 ~]# rbd info volumes/volume-cad6425c-4453-4489-b2d1-45050b062bd2
rbd image 'volume-cad6425c-4453-4489-b2d1-45050b062bd2':
	size 50 GiB in 12800 objects
	order 22 (4 MiB objects)
	snapshot_count: 0
	id: dc59383d97f124
	block_name_prefix: rbd_data.dc59383d97f124
	format: 2
	features: layering, deep-flatten
	op_features:
	flags:
	create_timestamp: Fri Jun 18 16:28:44 2021
	access_timestamp: Mon Jun 21 15:17:38 2021
	modify_timestamp: Mon Aug  2 23:35:33 2021
	parent: images/9e8a401b-d407-4946-b94c-f24b94ce0f02@snap
	overlap: 8 GiB
```

批量关闭所有卷的exclusive-lock

```
for i in $(rbd ls -p volumes); do rbd feature disable volumes/$i exclusive-lock,object-map; done
```

## 关闭新创建卷的exclusive-lock功能

如果是用Ceph Deploy进行的部署，则需要将配置文件分发到各个节点，在ceph.conf中增加rbd_default_features，写明你创建的卷需要哪几种属性。

```
[global]
fsid = 74fcb885-c0f9-4c31-a8fe-89a7f0122434
public_network = 10.0.100.0/24
mon_initial_members = compute201
mon_host = 10.0.100.201
auth_cluster_required = cephx
auth_service_required = cephx
auth_client_required = cephx
rbd_default_features = "layering, deep-flatten"
```

```
ceph-deploy --overwrite-conf config  push compute201 compute202 compute203
```

此时再使用rbd create创建的卷默认就是这两种属性了

```
[root@compute201 ~]# rbd create -p volumes test --size 10G
[root@compute201 ~]# rbd info volumes/test
rbd image 'test':
	size 10 GiB in 2560 objects
	order 22 (4 MiB objects)
	snapshot_count: 0
	id: 16ef5c2dacd2da
	block_name_prefix: rbd_data.16ef5c2dacd2da
	format: 2
	features: layering, deep-flatten
	op_features:
	flags:
	create_timestamp: Mon Aug  2 23:57:23 2021
	access_timestamp: Mon Aug  2 23:57:23 2021
	modify_timestamp: Mon Aug  2 23:57:23 2021
```

最后还需要对OpenStack各个模块的ceph进行更新，如果使用kolla更新，则替换所有配置文件，并重启容器。

```
cp /etc/ceph/ceph.conf /etc/kolla/config/nova/ceph.conf
cp /etc/ceph/ceph.conf /etc/kolla/config/cinder/ceph.conf

kolla-ansible -i multinode reconfigure
```

