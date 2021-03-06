---
title: Gitlab之间进行同步备份
slug: schedule-sync-gitlab
date: 2022-02-14T07:23:44+08:00
aliases:
  - /posts/gitlab之间进行同步备份/
draft: false
author: 老孙正经胡说
tags:
  - devops
  - gitlab
  - python
  - 容器
categories:
  - DevOps
---

目前，我们公司有两个研发团队，分别在北京和武汉，考虑到访问速度的问题，原有武汉的研发环境在近端部署。也就是北京和武汉分别有两套独立的研发管理环境，虽然这解决了近端访问速度的问题，但是管理上较为分散，比如研发环境备份和恢复就是最重要的问题之一。最近，处于对安全性和合规性的考虑，希望将北京和武汉的源代码，统一的集中备份，防止公司资产流失。

## Gitlab同步备份需求分析

由于历史原因，北京团队使用Gerrit进行代码审核和管理的工具，但是对于很多开发人员来说，入门比较陡峭，需要记忆很多git命令，所以考虑团队扩展性的需要，将Gerrit环境逐步切换至Gitlab中，而武汉团队则是直接选择了Gitlab进行代码管理。

在选择目标侧环境时，原本想使用阿里云效和腾讯的Coding环境进行备份，以我们目前体量来看，是完全免费的。但是考虑到随着公司增长，后期可能会产生成本，所以决定利用现有的K8S生产环境部署一套Gitlab，用于代码备份。

所以本次要解决的问题就是将两个团队Gitlab环境下的所有项目定期备份至远程的Gitlab中。在最初期的方案设计中，想使用最简单的Sehll脚本进行同步，但是会出现以下几个问题要解决：

* 在前期配置过程中，如果待同步项目较多，则在目标端进行预配置的工作较多，增加了管理成本，所以希望将整组的项目进行完整的增量同步
* 如果在源端有新的代码库增加，则需要至少维护同步脚本和备份端的Gitlab环境进行修改
* 如果还想同步Gitlab上诸如Wiki等文档类页面，则需要额外的手段进行

## 解决过程及思考

基于以上几点考虑，期望寻求一种自动化手段解决该问题，争取实现零运维的效果。

### 方案一：利用Gitlab原生机制

在Gitlab中提供了一种仓库(projects)级别的同步方式，具体配置如下：
1. 进入仓库的的Settings，点击Repository
2. 打开Mirroring repositories
3. 配置目标仓库地址及同步方式

![2022-02-14-14-10-21](/images/2022-02-14-14-10-21.png)

在开源版本中，只支持Push方式，而商业版本则支持Push和Pull两种方式。这个功能的优势是实时性，每当有代码提交后，则自动触发同步，避免了不必要的负载。

但是遗憾的是，在本地进行了测试时，只显示正在同步，但是一直没有同步成功，也没有给出具体的任务状态或失败原因。同时，并没有在组级别上提供同步能力，每次新增项目时，仍然需要手动在源端和目标端进行频繁操作，维护成本较高，所以最终放弃了该方案。

### 方案二：开源项目

在放弃第一个解决方案后，开始在Github上寻找开源项目。有一个基于Shell开发的gitlab-mirrors的项目引起了我的关注，这个项目由多个shell脚本组成。目标端支持除gitlab之外的多种Git仓库，看起来可以满足我们的需要。但是经过调研，发现gitlab-mirrors是以project为单位，无法按照组级别进行同步，所以也无法满足我们的需要。经过多番搜索，并没有一个项目能够百分之百满足我们组级别同步备份需求的项目。

### 方案三：自主实现自动化流程

由于以上两种方式均无法满足需求，所以决定基于Gitlab开放的Python库进行二次开发，满足需求。基本的思路为：

1. 在源端获取待同步组内的所有项目、子组
2. 克隆代码、所有分支、tags
3. 判断目标端Gitlab是否存在该组或者项目，如果没有则创建
4. Push代码、分支、tags

在满足了以上需求后，需要定期执行脚本实现周期性增量同步，那么如何利用Docker实现最简单的部署呢？所以需求进一步更新为：

1. 构建一个容器，该容器能够支持定期执行同步任务
2. 容器要利用系统的crontab，支持灵活配置
3. 任务在执行时要避免重复执行

基于以上需求，我开发了gitlab-sync脚本及容器(https://github.com/xiaoquqi/gitlab-sync)，改代码已经上传到github中，以下就为大家介绍详细的使用方法。

## 使用方法

通过以下配置，你可以轻松完成从Gitlab A中的Group A周期同步至Gitlab B中的Group B中。

### 前提条件

在开始配置gitlab-sync前，以下信息是必须提前获取的：

* LOCAL_GTILAB_URL: 源端的Gitlab的WEB地址及端口
* LOCAL_GITLAB_TOKEN: 源端Gitlab的Token，需要读取的权限
* LOCAL_GITLAB_GROUP: 源端Gitlab待同步的组，该组下所有项目及后续新增项目都会自动同步到目标端
* REMOTE_GTILAB_URL: 目标端Gitlab的WEB地址及端口
* REMOTE_GTILAB_TOKEN: 目标端Gitlab的Token，需要读取和写入权限
* REMOTE_GTILAB_GROUP: 目标端的组，可以与源端不一样
* REMOTE_GTILAB_PUSH_URL: 目标端Push地址，用于作为git push的目标端

除了这些信息外，Docker启动会默认将$HOME/.ssh路径挂载至容器内，所以需要你的key已经加入到源端和目标端的Gitlab中，以保证正确的Clone和Push的操作。

### 获取代码及配置

在代码中，提供了docker-compose.yml文件，可以直接使用。

```
git clone https://github.com/xiaoquqi/gitlab-sync

cd gitlab-sync
cp env.sample .env
cp crontab/cron.exmaple crontab/cron
```

* 在.env文件中，根据提前准备好的变量进行配置
* cron是crontab的配置文件，根据需求设定周期同步策略，后面的命令行不建议修改，其中flock是为了避免任务被重复运行

### 启动同步

完成配置后，启动容器开始同步。

```
docker-compose up -d
```

可以在Host主机的/var/log/gitlab-sync/gitlab-sync.log获取执行过程中的日志。

## 总结

在整个过程中，原本是想以脚本方式做最简单的处理，但是考虑到了后期运维成本等问题，最终决定考虑一种全自动化方式进行运维。

在处理容器运行crontab时，遇到用户环境变量无法获取的问题，目前采用的一种方式是一种Work Around，在容器启动后，将当前用户环境变量Dump到根分区下固定文件，在执行period_task.sh脚本中去加载这个脚本，从而获取环境变量。如果有更好的方法进行优化，欢迎提交Pull Request。

如果大家在使用过程中有任何问题，欢迎反馈，我会持续优化代码。