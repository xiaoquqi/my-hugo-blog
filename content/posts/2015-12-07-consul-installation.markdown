---
layout: post
title: "Consul的安装方法"
date: 2015-12-07 10:00:13 +0800
comments: true
categories: [Cloud Computing, Docker, Consul]
---

## 什么是Consul?

Consul拥有众多的组件，简言之，就是一个用于在你的基础设施中，发现和配置服务的工具。包含以下关键功能：服务发现、健康检查、键值存储和多数据中心支持。再说的通俗一点，就是用于管理分布式系统的利器。

<!-- more -->

## 安装Consul

Consul的安装比较简单，下载之后直接解压缩就可以了，下载地址：https://www.consul.io/downloads.html

我们把consul直接放在/usr/local/bin目录中。

## Consul Server

```
$ /usr/local/bin/consul agent -server -bootstrap-expect 3 -data-dir /tmp/consul -node=server1 -bind=10.10.10.10
```

### 参数说明

* -server - Serve模式
* -bootstrap-expect - Server数量
* -data-dir - 数据目录
* -node - Node名称
* -bind - 集群通讯地址

### 输出

```
==> WARNING: Expect Mode enabled, expecting 3 servers
==> WARNING: It is highly recommended to set GOMAXPROCS higher than 1
==> Starting Consul agent...
==> Starting Consul agent RPC...
==> Consul agent running!
         Node name: 'server1.consul.com'
        Datacenter: 'dc1'
            Server: true (bootstrap: false)
       Client Addr: 127.0.0.1 (HTTP: 8500, HTTPS: -1, DNS: 8600, RPC: 8400)
      Cluster Addr: 200.21.1.101 (LAN: 8301, WAN: 8302)
    Gossip encrypt: false, RPC-TLS: false, TLS-Incoming: false
             Atlas: <disabled>

==> Log data will now stream in as it occurs:

    2015/12/23 03:13:36 [WARN] memberlist: Binding to public address without encryption!
    2015/12/23 03:13:36 [INFO] serf: EventMemberJoin: server1.consul.com 200.21.1.101
    2015/12/23 03:13:36 [WARN] memberlist: Binding to public address without encryption!
    2015/12/23 03:13:36 [INFO] serf: EventMemberJoin: server1.consul.com.dc1 200.21.1.101
    2015/12/23 03:13:36 [INFO] raft: Node at 200.21.1.101:8300 [Follower] entering Follower state
    2015/12/23 03:13:36 [INFO] consul: adding server server1.consul.com (Addr: 200.21.1.101:8300) (DC: dc1)
    2015/12/23 03:13:36 [INFO] consul: adding server server1.consul.com.dc1 (Addr: 200.21.1.101:8300) (DC: dc1)
    2015/12/23 03:13:36 [ERR] agent: failed to sync remote state: No cluster leader
    2015/12/23 03:13:37 [WARN] raft: EnableSingleNode disabled, and no known peers. Aborting election.
    2015/12/23 03:13:51 [ERR] agent: failed to sync remote state: No cluster leader
==> Newer Consul version available: 0.6.0
    2015/12/23 03:14:17 [ERR] agent: failed to sync remote state: No cluster leader
```

### 查看成员

```
$ consul members
```

```
Node                Address            Status  Type    Build  Protocol  DC
server1.consul.com  200.21.1.101:8301  alive   server  0.5.2  2         dc1
```

## Consul Agent

```
$ /usr/local/bin/consul agent -data-dir /tmp/consul -node=agent1 -bind=10.10.10.100 -config-dir /etc/consul.d
```

* 输出

```
==> WARNING: It is highly recommended to set GOMAXPROCS higher than 1
==> Starting Consul agent...
==> Starting Consul agent RPC...
==> Consul agent running!
         Node name: 'agent1.consul.com'
        Datacenter: 'dc1'
            Server: false (bootstrap: false)
       Client Addr: 127.0.0.1 (HTTP: 8500, HTTPS: -1, DNS: 8600, RPC: 8400)
      Cluster Addr: 200.21.1.201 (LAN: 8301, WAN: 8302)
    Gossip encrypt: false, RPC-TLS: false, TLS-Incoming: false
             Atlas: <disabled>

==> Log data will now stream in as it occurs:

    2015/12/24 08:09:51 [WARN] memberlist: Binding to public address without encryption!
    2015/12/24 08:09:51 [INFO] serf: EventMemberJoin: agent1.consul.com 200.21.1.201
    2015/12/24 08:09:51 [ERR] agent: failed to sync remote state: No known Consul servers
    2015/12/24 08:09:56 [INFO] agent.rpc: Accepted client: 127.0.0.1:42794
    2015/12/24 08:09:56 [INFO] agent: (LAN) joining: [200.21.1.101 200.21.1.102 200.21.1.103]
    2015/12/24 08:09:56 [INFO] serf: EventMemberJoin: server1.consul.com 200.21.1.101
    2015/12/24 08:09:56 [INFO] consul: adding server server1.consul.com (Addr: 200.21.1.101:8300) (DC: dc1)
    2015/12/24 08:09:58 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:10:02 [INFO] agent: (LAN) joined: 1 Err: <nil>
    2015/12/24 08:10:02 [INFO] agent.rpc: Accepted client: 127.0.0.1:42800
==> Newer Consul version available: 0.6.0
    2015/12/24 08:10:21 [WARN] agent: Check 'ping' is now warning
    2015/12/24 08:10:22 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:10:43 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:11:01 [WARN] agent: Check 'ping' is now warning
    2015/12/24 08:11:02 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:11:23 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:11:41 [WARN] agent: Check 'ping' is now warning
    2015/12/24 08:11:43 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:12:12 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:12:21 [WARN] agent: Check 'ping' is now warning
    2015/12/24 08:12:36 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
    2015/12/24 08:13:01 [WARN] agent: Check 'ping' is now warning
    2015/12/24 08:13:03 [ERR] agent: failed to sync remote state: rpc error: No cluster leader
```

* server日志输出

```
    2015/12/24 08:09:58 [INFO] serf: EventMemberJoin: agent1.consul.com 200.21.1.201
```

### 查看成员

```
$ consul members
```

```
Node                Address            Status  Type    Build  Protocol  DC
server1.consul.com  200.21.1.101:8301  alive   server  0.5.2  2         dc1
agent1.consul.com   200.21.1.201:8301  alive   client  0.5.2  2         dc1
```

## 最终结果

```
$ consul members
```

```
Node                Address            Status  Type    Build  Protocol  DC
server1.consul.com  200.21.1.101:8301  alive   server  0.5.2  2         dc1
agent1.consul.com   200.21.1.201:8301  alive   client  0.5.2  2         dc1
agent2.consul.com   200.21.1.202:8301  alive   client  0.5.2  2         dc1
server2.consul.com  200.21.1.102:8301  alive   server  0.5.2  2         dc1
server3.consul.com  200.21.1.103:8301  alive   server  0.5.2  2         dc1
agent3.consul.com   200.21.1.203:8301  alive   client  0.5.2  2         dc1
```

## 参考文档

* https://www.consul.io/intro/getting-started/install.html
