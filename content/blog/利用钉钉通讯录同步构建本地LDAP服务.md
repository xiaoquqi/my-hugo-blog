---
title: 利用钉钉通讯录同步构建本地LDAP服务
author: 孙琦(Ray)
tags:
  - 云计算
  - Node.js
categories: []
date: 2020-10-31 18:24:00
---
目前钉钉已经成为很多企业日常处理流程的必备工具，但是由于钉钉并没有开放鉴权接口，无法让钉钉作为本地系统的统一鉴权系统使用，每次有同事加入或者离开时，都需要人为的对本地系统进行维护，非常繁琐。那么有没有一种方法可以让钉钉作为本地的统一鉴权系统使用呢？

<!-- more -->

目前，在我们公司使用OpenLDAP服务作为各个服务统一鉴权的入口，使用的应用系统包括：Gerrit/Jenkins/Yapi/Wiki/进度跟踪等，目前所有的系统都支持LDAP鉴权，所以如果能将钉钉的通讯录定期同步至LDAP中就可以实现统一鉴权的需求。但是由于钉钉的密码无法同步回本地，所以密码层面仍然是独立的。

本文章的实现思路参考了[《基于钉钉 + Virtual-LDAP + KeyCloak 的内网统一认证系统
》](https://xujiwei.com/blog/2020/02/internal-authorize-based-on-dingtalk-virtual-ldap-keyclaok/)，感谢原作者的思路及贡献的virtual-ldap模块，本文所有的优化都是基于此文章基础上进行的优化。

## 实现思路

简单来说，我们希望能通过钉钉提供的LDAP作为统一鉴权方式，但是由于钉钉没有开放这个能力，那么我们需要将钉钉模拟一个LDAP服务。模拟出的LDAP环境，在内网环境中，我们对于LDAP信息的使用基本上围绕着用户名和密码，其他的信息以钉钉为准。所以，除了开放LDAP接口外，我们还需要提供用户界面，允许用户在内网修改密码。

整体的实现思路如下：

* 钉钉开发者平台：需要在钉钉开发者平台新建一个程序，获取鉴权信息后，赋予通讯录同步权限，提供给VirtualLDAP进行数据同步
* VirtualLDAP：该组件是上面提到的作者开发的虚拟LDAP组件，主要功能为同步钉钉通讯录，并以LDAP协议对外提供服务
* KeyCloak：对于这个场景过重，但是暂时没有发现更好的方案，可以触发自动同步并且可以让内网用户进行密码修改
* 本地的全部系统按照LDAP配置方式即可实现鉴权

![upload successful](/images/pasted-90.png)

### 钉钉开发者平台

这里我创建的是H5微应用，配置时有几点需要注意：

* IP地址白名单：需要为你未来运行VirtualLDAP配置访问IP白名单，目前钉钉开发者平台对于同一个IP只能给一个应用使用，但是可以通过通配符进行配置，例如：192.168.10.*的方式，那么192.168.10网段所有地址均可以访问
* 权限：需要为该应用开放所有通讯录只读权限即可

![upload successful](/images/pasted-92.png)

### VirtualLDAP

这是基于Node.js开发的一款组件，主要用于同步钉钉通讯录和模拟LDAP协议。基于原作者版本，为了满足自身应用场景，进行了如下修改：

* 由于作者没有提供Docker运行方式，所以在github的pull request中有人进行了改造
* 仍然是在同一个pull request中，增加了pinyin组件，在LDAP中增加了一个pinyin属性，方便业务系统使用
* 登录名和密码：为了防止公司人员重复，所以特别采用了全拼名称+电话号码后四位方式，作为唯一的用户名，而初始密码为全名名称+电话号码前四位，例如：张三的电话号码为13812345678，则登录名称为zhangsan5678，密码为zhangsan1381,
* 在使用VirtualLDAP时，需要使用MySQL存储持久化数据，例如用户修改后的密码，所以对鉴权规则进行了修改，先检查数据库密码是否匹配，再检查LDAP
* 实现了整体组件的编排，增加了docker-compose.yaml，方便用户使用，该编排文件中包含了KeyCloak、VirtualLDAP和MySQL

### KeyCloak

KeyCloak两部分需要进行配置：

* 管理员在第一次使用时配置VirtualLDAP的信息，用于用户同步，方便新用户修改密码
* 新用户自行修改密码

正如之前所说，KeyCloak功能过于强大，这里用到的功能非常有限，如果有新的应用场景，欢迎留言。

![upload successful](/images/pasted-93.png)

## 搭建方式

这里提供了完整的编排文件，直接使用即可完成整套环境的快速建立。

```
git clone https://github.com/xiaoquqi/virtual-ldap
cd virtual-ldap/docker-compose
docker-compose up -d0
```

### 配置文件

* VirtualLDAP配置文件修改。所有配置在virtual-ldap/docker-compose/config.js中进行修改，需要修改钉钉的appKey和appSecret，以及root DN的信息，配置文件有比较详细的介绍，所以这里不再赘述。
* KeyCloak的默认密码修改在docker-compose.yaml中

### 登录相关信息

* URL: ldap://ip:1389
* ManageDN: cn=admin,dc=oneprocloud,dc=com
* ManagePassword: password
* User Search Base: ou=People,o=department,dc=oneprocloud,dc=com
* User Search Filter: uid={0}
* Display Name LDAP attribute: cn
* Email Address LDAP attribute: mail

## 待优化

* 目前对于LDAP的组没有充分利用，配置文件中允许创建特定组，并且通过用户email进行匹配，如果需要可以进行配置
* 如果有外部用户，暂时无方法进行创建，例如：如果需要在LDAP中增加一个非钉钉用户暂时无法实现，需要进行开发实现