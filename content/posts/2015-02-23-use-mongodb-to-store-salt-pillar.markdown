---
layout: post
title: "使用MongoDB作为Salt Pillar后端存储数据"
author: Ray Sun
date: 2015-02-23 15:19:21 +0800
comments: true
categories: [OpenStack, Salt, Cloud Computing]
---

今天在查找salt中pillar嵌套pillar的方法时，无意之间发现了pillar除了可以直接使用文件(sls)外，也同时支持多种后端的数据存储方式。例如：MySQL, MongoDB, Ldap, json, cobbler甚至是puppet。这无疑为开发中的接口提供了极大的便利。

<!-- more -->

详细的支持列表可见：http://docs.saltstack.com/en/latest/ref/pillar/all/index.html#all-salt-pillars

严格意义上来说，这篇博文并非完全原创，英文原文请参考：http://www.tmartin.io/articles/2014/salt-pillar-mongodb/

下面就来说说详细的配置方式，假定你已经有了一个部署好的salt环境，并且正确配置了salt master和salt minion，并且完成认证，主机名为salt-master.salt.com，这里我们使用Ubuntu 12.04 64bit作为演示环境。

## 安装MongoDB和Python MongoDB

```
apt-get install mongodb python-pymongo python-pymongo-ext
```

确保你能连接到MongoDB

```
mongo
```

    MongoDB shell version: 2.2.3
    connecting to: test
    >

## 创建MongoDB数据库和存放Pillar的Collection

* 创建数据库pillar
```
use pillar
```

* 在数据库中插入pillar数据
```
db.pillar.insert({
    _id: 'salt-master.salt.com',
    mongo_pillar: {
        key1: "value1",
        key2: "value2",
    }})
```
注意：这里的_id必须要和你的minion节点的主机名一致，并且无法使用通配符，也就是一个节点都有自己一套独立的pillar，这一点和文件中定义pillar有很大的不同。mongo_pillar部分中是定义的是pillar中的内容，也就是我们可以直接引用的部分。

### 配置Salt Master

* 下一步就是告诉Salt Master，我们在MongoDB中存放了pillar数据，需要劳您大驾，移步MongoDB读取数据。修改：

    /etc/salt/master

添加
```
mongo.db: "pillar"
mongo.host: "localhost"
ext_pillar:
    - mongo: {}
```
注意：如果需要使用不同于标准安装接口，请使用mongo.port，如果需要配置用户名和密码，请使用mongo.user和mongo.password。其他参数定义，请详见：http://docs.saltstack.com/en/latest/ref/pillar/all/salt.pillar.mongo.html#module-documentation

* 测试
```
salt salt-master.salt.com pillar.item mongo_pillar
```
返回

    salt-master.salt.com:
        ----------
        mongo_pillar:
            ----------
            key1:
                value1
            key2:
                value2

* 如果想在sls中直接使用
```
{% raw %}{{ salt['pillar.get']('mongo_pillar:key1') }}{% endraw %}
```

## 总结

pillar应该是salt中一个比较灵活的配置选项，个人理解pillar的作用就像puppet中init定义的初始化的参数的默认值，每次部署时，只需要更改pillar的文件就可以啦。但是随着代码的增长(主要用于部署OpenStack)，发现pillar的管理越来越难，pillar本身对如何组织结构并没有严格的限制，而且嵌套(extend)功能暂时还不能很完美的支持(https://github.com/saltstack/salt/issues/3991)，这也给pillar的管理提高了复杂度。
