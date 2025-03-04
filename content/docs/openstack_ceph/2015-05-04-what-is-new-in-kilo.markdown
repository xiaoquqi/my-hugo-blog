---
layout: post
title: "OpenStack Kilo版本新功能分析"
author: Ray Sun
date: 2015-05-04 10:37:22 +0800
comments: true
categories: [OpenStack, Cloud Computing]
---

OpenStack Kilo版本已经于2015年4月30日正式Release，这是OpenStack第11个版本，距离OpenStack项目推出已经整整过去了5年多的时间。在这个阶段OpenStack得到不断的增强，同时OpenStack社区也成为即Linux之后的第二大开源社区，参与的人数、厂商众多，也成就了OpenStack今天盛世的局面。虽然OpenStack在今年经历了Nebula的倒闭，但是随着国内的传统行业用户对OpenStack越来越重视，我们坚信OpenStack明天会更好。

OpenStack Kilo版本的完整翻译版本可见：https://wiki.openstack.org/wiki/ReleaseNotes/Kilo/zh-hans

OpenStack Kilo版本的翻译工作由我和我的同事裴莹莹(Wendy)共同完成，翻译校对工作由裴莹莹完成。如果翻译有任何问题，请各位多多指正。

<!-- more -->

## 社区贡献分析

我们先来看一下OpenStack在最近的4个稳定版本发布中，每一个项目的贡献情况：

![](/images/blogs/what-is-new-in-kilo-contribution-by-modules.jpg)

我们能够很明显的发现，OpenStack最早的几大核心模块(Nova, Cinder, Glance, Keystone, Horizon, Swift)的代码贡献所占比例呈明显下降趋势，这里强调一下，是比例而不是数量，从数量上来看，版本之间相差并不大，以Nova为例，从Havana版本的24%下降到如今的10%。这从一个侧面反映了OpenStack的核心模块日趋稳定，更多的关注集中到更高层次或者功能优化上。

Neutron模块则一直处于稳中有升的状态,从Havana版本的7%上升到10%，说明Neutron仍然处于需要进一步完善的状态。

对于Ceilometer，Heat，Sahara，Ironic, Trove等新晋的核心模块，都处于稳步增长的阶段。贡献的比例在四个版本中基本保持持平的态势。在Kilo版本中，Sahara和Heat进入了前十名。

从Kilo版本的比例来看，Others的比例过半，Others主要包括了OpenStack测试相关项目，例如Rally；开发相关项目，例如Devstack;以及一些新的模块，例如：Manila，Magnum等众多进入孵化器的项目;还包括所有的Client以及Spec等。可以预见，OpenStack的开发重心逐步从底层的核心模块，逐步向更高层次、提供更丰富功能的方向发展。

## 国内社区贡献分析

![](/images/blogs/what-is-new-in-kilo-contributor.png)

从企业贡献排名来看，几大巨头企业牢牢占据贡献榜的前几名，OpenStack最成功的公司-Mirantis排名紧追Redhat成为第二贡献大户。排名前几位的公司还包括：IBM, Rackspace, Cisco, Suse, VMware, Intel等。

国内方面，华为继续稳定在第13名，但Review的数量从Juno版本的1353提升到2548个，贡献的项目几乎涵盖所有的项目，主要贡献来自Heat，Ceilometer, Horizon，Neutron, Nova等项目。

国内排名第2的贡献企业是九州云，排名达到了21位，看来龚永生的到来为九州云添加了无限活力。九州云的贡献主要来自Horizon和Neutron两个项目，龚永生不愧为Neutron的Core，在网络方面的贡献，九州云的确很给力。

排名第3的企业是海云捷迅，排名为44位，海云是国内比较早的一批OpenStack创业企业，贡献方面以Sahara，Neutron，Nova，oslo.messaging以及Cinder为主，从之前了解的情况来看，海云的项目不少，可能提交的修改是与在实际项目中遇到的问题有关。

排名之后的企业还有Kylin Cloud，UnitedStack，EasyStack等。由于是手工统计，在统计过程中如有遗漏，希望大家多多指正。

## Horizon新功能

Horizon在K版本除了增强了对新增模块的支持，从UE的角度也为我们带来了很多新功能

* 支持向导式的创建虚拟机，现在还处于beta版本，如果想在Horizon里激活，可以通过设置local_setting.py的配置实现：

``` plain local_setting.py
LAUNCH_INSTANCE_NG_ENABLED = True
```

![](/images/blogs/what-is-new-in-kilo-instance-guide1.png)

![](/images/blogs/what-is-new-in-kilo-instance-guide2.png)

* 支持简单的主题，主要通过修改_variables.scss和_style.scss完成对主题颜色和简单样式的修改，但是格局不能改变，修改local_settings.py

``` plain local_setting.py
CUSTOM_THEME_PATH = 'static/themes/blue'
```

``` plain static/themes/blue/_variables.scss
$gray:                   #2751DB !default;
$gray-darker:            #94A5F2 !default;
$gray-dark:              #0C0CED !default;
$gray-light:             #C7CFF2 !default;
$gray-lighter:           #DCE1F5 !default;

$brand-primary:         #375A7F !default;
$brand-success:         #00bc8c !default;
$brand-info:            #34DB98 !default;
$brand-warning:         #F39C12 !default;
$brand-danger:          #E74C3C !default;
```

``` plain static/themes/blue/_style.scss
// Blue
// ----

@mixin btn-shadow($color) {
  @include gradient-vertical-three-colors(lighten($color, 3%), $color, 6%, darken($color, 3%));
  filter: none;
  border: 1px solid darken($color, 10%);
}

// Buttons ====================================================================

.btn-default,
.btn-default:hover {
  @include btn-shadow($btn-default-bg);
}

.btn-primary,
.btn-primary:hover {
  @include btn-shadow($btn-primary-bg);
}
```

![](/images/blogs/what-is-new-in-kilo-horizon-theme1.png)

![](/images/blogs/what-is-new-in-kilo-horizon-theme2.png)

## Nova新功能

### Nova Scheduler

* 标准化了conductor，compute与scheduler的接口，为之后的接口分离做好准备，对于部分直接访问nova数据库的filters进行了优化，不再允许直接访问，参考链接：https://github.com/openstack/nova-specs/blob/master/specs/kilo/approved/isolate-scheduler-db-filters.rst
* 对Scheduler做了一些优化，例如：Scheduler对于每一个请求都会重新进行Filters/Weighers，为了优化这个问题，将filter/weighter的初始化从handler移到scheduler，这样每次请求的时候都可以重新使用了。

### Libvirt NFV相关功能

* NUMA(Non Uniform Memory Architecture)，在这个架构下，每个处理器都会访问“本地”的内存池，从而在CPU和存储之间有更小的延迟和更大的带宽。
* 在Kilo版本中针对此功能的实现包括：基于NUMA的调度的实现；可以将vCPU绑定在物理CPU上；超大页的支持。以上提到的三点都是通过Flavor的Extra Spces完成定义的。

### EC2 API

* EC2 API被从Nova中踢出去了
* 取而代之的是在stackforge的EC2 API转换服务

### API Microversioning

先来解释一下为什么需要API的微版本：主要原因在于现在这种API扩展方式，对于API实现的代码的增加或减少管理非常不方便，容易导致不一致性。引入微版本主要目的就是让开发人员在修改API代码时能够向前兼容，而不是加入一个新的API扩展；用户通过指定API的版本，在请求时也能决定是使用的具体的动作。

包含版本的返回:
``` plain Result
GET /
{
     "versions": [
        {
            "id": "v2.1",
            "links": [
                  {
                    "href": "http://localhost:8774/v2/",
                    "rel": "self"
                }
            ],
            "status": "CURRENT",
            "version": "5.2"
            "min_version": "2.1"
        },
   ]
}
```

客户端的Header信息：
``` plain Header
X-OpenStack-Nova-API-Version: 2.114
```

### 一个已知的问题：Evacuate

这个问题的产生主要是因为Evacuate的清理机制，主机名的变化会导致nova-compute重启过程中误删所有虚拟机，所以一个变通的方法是设置

``` plain nova.conf
destroy_after_evacuate=False
```

这个问题会在Liberty中得到修复，相关的Spec：https://review.openstack.org/#/c/161444/3/specs/liberty/approved/robustify_evacuate.rst

## Glance新功能

* 自动进行镜像格式转化，例如，Ceph是使用RAW格式的，假如我们上传的是QCOW2，创建虚拟机时，就会经历一番上传下载的过程，速度异常缓慢。而且RAW格式通常都是原始大小，上传时候非常慢，完全可以通过上传小镜像自动转换为指定格式。
* Glance支持多字段排序
``` plain API
/images?sort_key=status&sort_dir=asc&sort_key=name&sort_dir=asc&sort_key=created_at&sort_dir=desc
```
* 临时将镜像设置为非活跃状态，假如一个镜像里有病毒，管理员就会将该镜像设置为非活跃状态，在清理后重新发布该镜像，在这个过程中，所有非管理员用户都无法使用或者下载这个镜像
* 免重启动态加载配置文件，配置文件改动后重启服务，现在可以给glance服务发送SIGHUP触发，这样升级就可以零当机时间。
* 使用多个Swift容器存储镜像，减少大规模部署时的请求瓶颈

## Cinder新功能

* 实现服务逻辑代码与数据库结构之间的解耦，支持Rolling更新
* 一致性组是指具备公共操作的卷，逻辑上化为一组。在K版本中对增强一致性组的功能：可以添加、删除卷，从已经存在的快照创建新的组，关于一致性组的详细操作可以参考：http://docs.openstack.org/admin-guide-cloud/content/consistency-groups.html

``` plain cinder
cinder consisgroup-update
[--name NAME]
[--description DESCRIPTION]
[--add-volumes UUID1,UUID2,......]
[--remove-volumes UUID3,UUID4,......]
CG
```

``` plain cinder
cinder consisgroup-create-from-src
[--cgsnapshot CGSNAPSHOT]
[--name NAME]
[--description DESCRIPTION]
```

* 卷类型的增强功能主要包含两个：为某一项目创建私有的卷类型和为卷类型增加描述信息

``` plain cinder
cinder type-create <name> --is-public
cinder type-create <name> <description>
```

## Neutron新功能
* DVR支持OVS中的VLANs
* 新的V2版本的LBaas的API
* 新的插件的更新，详情请见更新日志中
* 一些高级服务的分离，例如：L3, ML2, VPNaaS, LBaaS

网络方面我不是权威，希望有高人能出来讲讲Kilo中的Neutron新功能。

## Keystone新功能
* 项目嵌套，创建一个新的Project时候，可以指定parent的Project

``` plain keystone
POST /projects

{
    "project": {
        "description": "Project space for Test Group",
        "domain_id": "1789d1",
        "enabled": true,
        "name": "Test Group",
        "parent_id": "7fa612"
    }
}
```

* Keystone与Keystone的联盟，有了这个功能两个或者更多的云服务提供者就可以共享资源，这个功能在J版本引入，在K版本中主要针对该功能的进一步增强，具体的使用方法可参考这篇博文：http://blog.rodrigods.com/playing-with-keystone-to-keystone-federation/
* 针对新人授权的一些增强功能
* keystone的配置中有部分配置发生了变化，例如：keystone.token.backends.memcache被keystone.token.persistence.backends.memcache取代，更多详细内容请参考更新日志

## Swift新功能
* 纠删码的加入应该是这个版本最大的亮点，但是纠删码作为beta版本发布，并不推荐应用于生产环境，关于纠删码的详细介绍可以参考：http://docs.openstack.org/developer/swift/overview_erasure_code.html
* 复合型令牌，简而言之就是需要用户加上服务的Token才能对Swfit存放的内容进行操作，如下图所示：

``` plain swift
client
   \
    \   <request>: <path-specific-to-the-service>
     \  x-auth-token: <user-token>
      \
    SERVICE
       \
        \    PUT: /v1/SERVICE_1234/<container>/<object>
         \   x-auth-token: <user-token>
          \  x-service-token: <service-token>
           \
          Swift
```

具体的设计文档：http://docs.openstack.org/developer/swift/overview_backing_store.html

* 全局性的集群复制优化，大幅提高效率，避免经过广域网传播的数据

## Ceilometer新功能
* 支持Ceph对象存储监控，当对象存储为Ceph而不是Swfit的时候，使用Polling机制，使用Ceph的Rados Gateway的API接口获取数据，具体的设计文档：https://github.com/openstack/ceilometer-specs/blob/master/specs/kilo/ceilometer_ceph_integration.rst
* Ceilometer API RBAC - 更细粒度的权限控制: https://github.com/openstack/ceilometer-specs/blob/master/specs/kilo/ceilometer-rbac.rst
``` plain Ceilometer
{
    "context_is_admin": [["role:admin"]]
}
```
更细粒度的控制
``` plain Ceilometer
{
     "context_is_admin": [["role:admin"]],
     "admin_or_cloud_admin": [["rule:context_is_admin"],
              ["rule:admin_and_matching_project_domain_id"]],
     "telemetry:alarm_delete": [["rule:admin_or_cloud_admin"]]
}
```
* 接口中的模糊查询，增加了一个新的查询符号=~
* 支持更多的测量，包括Hyper-V，IPMI相关的

## Ironic新功能
* iLO的优化
* 使用Config Drive替代Metadata服务
* 全盘镜像支持，可以跳过raddisk和kernel，这样就可以部署Windows的镜像了
* 使用本地盘启动，替代PXE方式，可以通过设置flavor的capabilities:boot_option实现

## Oslo

解决了很多之前遗留的技术债，还有一些命名规范的问题。olso.messaging实现了心跳，olso.log在所有项目中使用，优化了oslo.db的代码。

## OpenStack文档

优化了docs.openstack.org页面，也可以从中选择相应的语言。有专门的团队负责安装、网络和高可靠的文档。

## 其他模块

对于Sahara, Heat, Trove等模块的更新没有在这里Highlight出来，大家可以参考更新日志里的内容，或者查看specs中的具体描述。

## 总结

通过Kilo的一些更新可以看到，Kilo版本在不断优化代码结构的基础上，增加了一些新功能，也偿还了一些技术债，总体来说是一种稳中有升的态势，但是总体感觉并没有太多的惊喜和出人意料。相信随着更多的孵化项目进入正式版本中，OpenStack一定会向更多元化的方向发展。
