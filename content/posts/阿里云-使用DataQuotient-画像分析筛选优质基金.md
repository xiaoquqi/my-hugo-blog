---
title: '[阿里云]使用DataQuotient 画像分析筛选优质基金'
author: 孙琦(Ray)
date: 2020-04-14 11:10:17
tags:
---
该教程是阿里云帮助文档一部分，这里做了进一步完善：https://help.aliyun.com/document_detail/160711.html?spm=a2c4g.11174283.6.603.682fa00bJ7AHYK

## 需求描述

4433法则通过对同类基金（例如股票类基金）长期和短期的表现进行分析，为您在众多基金中筛选少数优质基金。

<pre>
4433法则如下：
4：代表近一年收益率排名前1/4的基金。
4：代表近两年、三年、五年以来，收益率排名前1/4的基金。
3：指近六个月收益率排名前1/3的基金。
3：指近三个月以来收益率排名前1/3的基金。
</pre>

本教程为您演示如何从当日的1126个股票类的基金产品中，筛选出符合4433法则的69条优质基金。

<!-- more -->

## 实现流程
![upload successful](/images/pasted-0.png)

### 准备数据
* 获取基金数据，从天天基金网接口获取股票型基金的不同时间区间的收益率数据
* 数据输入MaxCompute

### 创建基金信息标签系统
* 新建实体，用于将数源和待分析的对象绑定在一起
* 绑定标签，将数据源与标签进行绑定

### 筛选并导出优质基金群体
* 同步标签至RDS，这个例子中因为只是从MaxCompute到RDS，真实环境中有可能从多个数据源同步至目标RDS中，该服务支持数据的合并等
* 根据上述预先建立好的模型，新建长期和短期表现较好群体
* 计算群体
* 导出优质基金列表

## 实现过程

### 前提条件
本教程基于DataQuotient 画像分析、MaxCompute和RDS产品，请确保您已购买该产品。

### 获取基础数据

根据教程提供的线索，从天天基金网获取了全部股票型基金的数据，脚本已经提交到Github上，有需要的可以直接拿过去用。

```
git clone https://github.com/xiaoquqi/fund
cd fund
python fund-cli.py -d -v
```

### 在MaxCompute导入数据

#### 开通MaxCompute服务

之前我并没有开通过MaxCompute服务，所以需要开通一下DataWorks，才能使用MaxCompute服务。

![upload successful](/images/pasted-1.png)

这个就是DataWorks控制台，从操作上看局限性很高（比如不支持删除表
![upload successful](/images/pasted-2.png)

），所以建议采用IntelliJ IDEA中的MaxCompute Studio插件，安装方式见：https://www.alibabacloud.com/help/zh/doc-detail/50889.htm?spm=a2c63.p38356.b99.275.5e652ea3SZgau1
![upload successful](/images/pasted-41.png)

#### 创建MaxCompute表

由于做的时候才发现数据源并没有近五年的数据，所以修改了一下创建语句，先把表名建立起来，之后进入DDL模式进行表创建：

```
create table if not exists fund_profit_stocktype
( `fundid` bigint comment '基金编号',
 `fundname` string comment '基金名称',
 `latest3months` double comment '近三月',
 `latest6months` double comment '近六月',
 `latest1year` double comment '近一年',
 `latest2years` double comment '近两年',
 `latest3years` double comment '近三年',
 `currentyear` double comment '今年来',  
 `fromcreated` double comment '成立来',
) comment '基金信息' ;
```

![upload successful](/images/pasted-3.png)



#### 导入数据

原有文档是通过DDL去创建的数据，由于我们已经将数据保存在CSV文件中，所以我们选择导入方式试一下。

![upload successful](/images/pasted-4.png)


![upload successful](/images/pasted-5.png)


![upload successful](/images/pasted-7.png)

不知道什么原因，下拉菜单选择并不生效，于是我决定将原有CSV无用字段全部删除，便于后续测试。删除字段的时候，发现我获取的数据并不包含近五年的项，但是包含成立以来的数据，所以对字段进行一下修改。上面的SQL是我修改过的。页面好像并没有删除表的功能，所以为了不影响测试，我重新建了一张表来导入数据。

![upload successful](/images/pasted-8.png)

### 关联云计算资源
回到画像服务，继续进行配置

![upload successful](/images/pasted-13.png)


![upload successful](/images/pasted-14.png)

我用的主账号的AK/KS竟然提示我权限不足，于是我去查了半天RAM文档，以为MaxCompute需要更精确的授权，结果发现是提示信息误导了我，只是我的project写错了，最后project信息还是回到DataWorks控制台才找到，如下图所示。

需要添加这么多信息感觉不是特别方便，都是阿里云的资源感觉没有必要使用AK/KS去通讯吧？

![upload successful](/images/pasted-15.png)

![upload successful](/images/pasted-16.png)

配置好后的云计算资源

![upload successful](/images/pasted-17.png)

### 标签管理

配置好后，可以继续进行标签配置。

![upload successful](/images/pasted-9.png)

![upload successful](/images/pasted-10.png)

#### 关联MaxCompute表

![upload successful](/images/pasted-11.png)

如果你没有正确配置云计算资源，是无法看到MaxCompute下的表。
![upload successful](/images/pasted-12.png)

绑定表和字段
![upload successful](/images/pasted-18.png)

![upload successful](/images/pasted-19.png)

![upload successful](/images/pasted-20.png)

字段绑定后无法删除，需要到详情中删除
![upload successful](/images/pasted-21.png)

![upload successful](/images/pasted-22.png)

最开始显示为0，后来又显示出数据总量，但是根据上方提示，MaxCompute是不支持显示的。
![upload successful](/images/pasted-23.png)

过了一会又出现了1185的数据总量，不知道为什么
![upload successful](/images/pasted-33.png)

![upload successful](/images/pasted-25.png)

### 筛选出优质基金群体

#### 同步标签至RDS

![upload successful](/images/pasted-24.png)

![upload successful](/images/pasted-26.png)

![upload successful](/images/pasted-27.png)

![upload successful](/images/pasted-28.png)

![upload successful](/images/pasted-29.png)

显示同步成功，但是发现输出的信息里有红色的信息，以为是错误，但是仔细一看又是INFO级别的日志，而且显示的太长了。
![upload successful](/images/pasted-31.png)

![upload successful](/images/pasted-32.png)

#### 群体画像

需要切换至群体画像的工作空间。
![upload successful](/images/pasted-30.png)

新建短期表现优质的基金。
![upload successful](/images/pasted-34.png)

如果配置正确，可以从结果中看出筛选出的结果。
![upload successful](/images/pasted-35.png)

![upload successful](/images/pasted-36.png)

新建长期表现优质的基金。
![upload successful](/images/pasted-37.png)

使用群体计算，找出二者的交集。这个就是我们希望得到的结果。
![upload successful](/images/pasted-38.png)

![upload successful](/images/pasted-39.png)

利用下载功能，可以下载我们筛选出来的基金。
![upload successful](/images/pasted-40.png)

## 总结

使用阿里云DataQuotient服务可以快速帮助用户构建用户画像，能够满足多种应用场景，利用函数计算进行数据爬取定期导入到MaxCompute，可以很容易定制出优质基金筛选功能的API接口，供上层业务场景使用。
