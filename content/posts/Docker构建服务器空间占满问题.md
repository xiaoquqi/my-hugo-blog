---
title: Docker构建服务器空间占满问题
author: 孙琦(Ray)
date: 2020-11-13 14:19:41
tags:
---
## 现象描述

今天Jenkins构建突然出现问题，检查Jenkins Job日志发现no space left，于是登录到Jenkins Build服务器上，发现容器所在的/var/lib空间被完全满了。

<!-- more -->

![upload successful](/images/pasted-94.png)

## 排查过程

### 检查容器空间

首先从容器层面检查一下空间占用情况：

```
docker system df
```

发现有容器的占用空间达到了1个多TB的空间。

![upload successful](/images/pasted-95.png)

### 清理无用的容器和镜像

先用prune进行一下清理，为了保险起见，过滤一下时间

```
docker system prune -a -f --filter "until = 1h"
```

清理完成后，空间仍然没有释放，于是继续排查。

### 检查/var/lib下的空间占用

通过检查发现/var/lib/docker/overlay2中的66d44a19ee93a191cc0585efac45e10696edfd0381d0dc96d9646080337f629e目录空间占用巨大，进入后发现其中有tmp目录没有及时清理。由于没有Jenkins任务在执行，所以手动清理了/tmp/tmp*的目录，空间被立即释放了。

![upload successful](/images/pasted-96.png)

那么此时问题清晰了，这一层属于Jenkins，进入容器后发现Jenkins的/tmp目录没有被及时清理，属于Build逻辑有缺陷造成了，及时修复Pipeline的Jenkinsfile后，该问题不再出现。


