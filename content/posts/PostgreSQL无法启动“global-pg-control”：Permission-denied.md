---
title: PostgreSQL无法启动“global/pg_control”：Permission denied
author: 孙琦(Ray)
tags:
  - 数据库
categories: []
date: 2021-02-11 08:44:00
---
昨天在为用户进行迁移后，用户Windows 2012系统上PostgreSQL服务无法启动，日志中提示“global/pg_control”：Permission denied，于是上网一顿搜索终于解决了这个问题。

<!-- more -->

## 检查

如果端口没有被占用，那么你可以用PostgreSQL原生的命令启动它。进入postgresql安装路径下的 bin 文件夹，在这里打开命令行，执行下面的命令：

```
.\pg_ctl start -D ..\data
```
 

如果程序报出如下错误：

```
ERROR: could not open control file “global/pg_control”: Permission denied
```

![upload successful](/images/pasted-159.png)

则说明当前操作系统用户丢失了data文件夹及其内容的权限。

## 解决方案

1. 首先，进入postgresql 的安装路径，右键data文件夹，依次点击属性——安全——编辑，你能看到所有用户或用户组的权限。

![upload successful](/images/pasted-160.png)

2. 确保System 和 Administrator 拥有“完全控制”权限。Users 用户组默认只拥有“读取和执行”，“列出文件夹内容”和“读取”3种权限。当启动数据库提示“权限不足”时，应再添加“修改”和 “写入”。我这次出现问题就在这里，User没有修改和写入权限，添加后即可启动成功。

![upload successful](/images/pasted-161.png)

3. 保存并尝试再次在bin 文件夹下执行：

```
.\pg_ctl start -D ..\data
```

观察PostgreSQL数据库能否启动。
        
        
## 参考链接

* https://blog.csdn.net/international24/article/details/89710703