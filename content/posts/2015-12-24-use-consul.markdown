---
layout: post
title: "Consul主要使用场景"
date: 2015-12-24 18:07:24 +0800
comments: true
categories: [Cloud Computing, Docker, Consul]
---

假设你已经按照之前的Consul安装方法部署了一套具备环境，具体方法可以参考：http://xiaoquqi.github.io/blog/2015/12/07/consul-installation/

这篇文章里主要介绍Consul的使用场景，服务和健康检查。

<!-- more -->

## Service

服务注册有点像OpenStack Keystone的Endpoints，可以通过API方式查询到所有服务的端点信息。

在Agent的节点上添加一个service，之后重启服务。

* 添加一个服务

```
$ echo '{"service": {"name": "web", "tags": ["rails"], "port": 80}}' \
    >/etc/consul.d/web.json
```

* 重启agent

重新加载新的服务并不需要杀死进程重启服务，只需要给进程直接发送一个SIGHUP。

```
$ kill -HUP $(ps -ef | grep agent | grep -v grep | awk '{print $2}')
```

* 日志输出

从输出的日志上都可以看到加载了新的服务web。

```
==> Caught signal: hangup
==> Reloading configuration...
==> WARNING: Expect Mode enabled, expecting 3 servers
    2015/12/24 12:01:11 [INFO] agent: Synced service 'web'
```

* 利用API查询

我们在任意节点上利用REST API查看服务。

```
$ curl http://localhost:8500/v1/catalog/service/web
```

```
[{"Node":"server1.consul.com","Address":"200.21.1.101","ServiceID":"web","ServiceName":"web","ServiceTags":["rails"],"ServiceAddress":"","ServicePort":80}]
```

## Health Check

健康检查的方法主要是通过运行一小段脚本的方式，根据运行的结果判断检查对象的健康状况。所以可以通过任意语言定义这个脚本，脚本运行将通过和consul执行的相同用户执行。

* 添加一个健康检查

每30秒ping google.com

```
$ echo '{"check": {"name": "ping",
  "script": "ping -c1 google.com >/dev/null", "interval": "30s"}}' \
    > /etc/consul.d/ping.json
```

为刚才的服务添加健康检查

```
$ echo '{"service": {"name": "web", "tags": ["rails"], "port": 80,
  "check": {"script": "curl localhost >/dev/null 2>&1", "interval": "10s"}}}' \
    > /etc/consul.d/web.json
```

* 重启agent

```
$ kill -HUP $(ps -ef | grep agent | grep -v grep | awk '{print $2}')
```

* 日志输出

从输出的日志上都可以看到加载了新的服务web。

```
==> Caught signal: hangup
==> Reloading configuration...
==> WARNING: Expect Mode enabled, expecting 3 servers
    2015/12/24 12:43:56 [INFO] agent: Synced service 'web'
    2015/12/24 12:43:56 [INFO] agent: Synced check 'ping'
```

经过一段时间后出现了critical和warning日志

```
    2015/12/24 12:43:58 [WARN] agent: Check 'service:web' is now critical
    2015/12/24 12:44:08 [WARN] agent: Check 'ping' is now warning
```

* 利用API查询

Health check的状态包含了很多种，有any, unkown, passing, warning, critical。any包含了所有状态。

```
$ curl http://localhost:8500/v1/health/state/critical
```

```
[{"Node":"server1.consul.com","CheckID":"service:web","Name":"Service 'web' check","Status":"critical","Notes":"","Output":"","ServiceID":"web","ServiceName":"web"}]
```

## 参考文档

* http://www.consul.io/docs/agent/http/catalog.html
* http://www.consul.io/docs/agent/http/health.html
