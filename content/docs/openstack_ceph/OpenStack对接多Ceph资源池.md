---
title: OpenStack对接多Ceph资源池
author: 孙琦(Ray)
tags:
  - OpenStack
  - Ceph
  - 云计算
categories: []
date: 2020-09-14 16:52:00
---
OpenStack支持与多个不同的Ceph资源池进行对接，通过cinder的volume type与backend进行对应，创建时只需要选择不同的volume type就可以实现指定资源池创建。配置OpenStack对接分为两个部分：

* Cinder配置：主要配置存储资源池与Volume Type和Backend对应关系
* Libvirt配置：配置与Ceph之间的鉴权关系

<!-- more -->

## Cinder配置

其中rbd_secret_uuid可以使用uuidgen命令生成

```
## /etc/cinder/cinder.conf
[DEFAULT]
......
## 与下面的段落对应
enabled_backends = rbd-1, rbd-2
......

[rbd-1]
volume_driver = cinder.volume.drivers.rbd.RBDDriver

## 与上面的enabled_backends对应
volume_backend_name = rbd-1

rbd_pool = volumes

## 需要从Ceph集群拷贝这两个配置文件到相应目录
rbd_ceph_conf = /etc/ceph/ceph-1.conf
rbd_keyring_conf = /etc/ceph/ceph.client.cinder1.keyring

rbd_flatten_volume_from_snapshot = false
rbd_max_clone_depth = 5
rbd_store_chunk_size = 4
rados_connect_timeout = 4
rbd_user = admin
rbd_secret_uuid = 5774b929-0690-4513-a1f7-41aac49cbb31
report_discard_supported = True
image_upload_use_cinder_backend = True
 
[rbd-2]
volume_driver = cinder.volume.drivers.rbd.RBDDriver
volume_backend_name = rbd-2
rbd_pool = volumes
rbd_ceph_conf = /etc/ceph/ceph-2.conf
rbd_keyring_conf = /etc/ceph/ceph.client.cinder2.keyring
rbd_flatten_volume_from_snapshot = false
rbd_max_clone_depth = 5
rbd_store_chunk_size = 4
rados_connect_timeout = 4
rbd_user = admin
rbd_secret_uuid = 0563c419-bc4c-4794-972a-685498248869
report_discard_supported = True
image_upload_use_cinder_backend = True
```

### 建立与Volume Type对应关系

```
cinder type-create rbd-1
cinder type-key rbd-1 set volume_backend_name=rbd-1
cinder extra-specs-list

cinder type-create rbd-2
cinder type-key rbd-2 set volume_backend_name=rbd-2
cinder extra-specs-list
```

## Libvirt配置

在/etc/libvirt/secretes建立与上述rbd_secret_uuid同名的两个文件，后缀为.xml和.base64，两个文件的内容为

```
## 5774b929-0690-4513-a1f7-41aac49cbb31.xml
<secret ephemeral='no' private='no'>
  <uuid>5774b929-0690-4513-a1f7-41aac49cbb31</uuid>
  <usage type='ceph'>
    <name>client.cinder1 secret</name>
  </usage>
</secret>
```

其中base64文件的内容就是keyring文件中key的值

```
[client.admin]
	key = AQB/E15f42WdABAAR32oTiidCbVGpwhYbWcKAw==
```

```
## 5774b929-0690-4513-a1f7-41aac49cbb31.xml
AQB/E15f42WdABAAR32oTiidCbVGpwhYbWcKAw==
```

最后执行如下命令完成配置：

```
virsh secret-define --file 5774b929-0690-4513-a1f7-41aac49cbb31.xml
virsh secret-set-value --secret 5774b929-0690-4513-a1f7-41aac49cbb31 --base64 $(cat 5774b929-0690-4513-a1f7-41aac49cbb31.base64)
systemctl restart libvirtd
```