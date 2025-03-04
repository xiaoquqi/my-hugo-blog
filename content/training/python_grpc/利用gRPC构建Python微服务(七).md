---
title: 利用gRPC构建Python微服务(七)——AsyncIO和gRPC
slug: python-microservices-grpc-7
date: 2022-01-19T20:37:00+08:00
draft: false
author: Dan Hipschman/老孙正经胡说
tags:
  - Python
  - 微服务
  - 容器
  - 云原生
categories:
  - 微服务
weight: 7
---

在上一篇中，主要讲解了关于基于gRPC构建Python微服务的一些最佳实践，本篇将介绍在gRPC中如何使用AsyncIO，本篇也是终结篇。

<!-- more -->

## 全文导航

为了方便大家阅读，这里将全部目录进行一下索引，方便大家在老孙正经胡说(https://sunqi.site)中查看相关文章：

* [利用gRPC构建Python微服务(一)——关于微服务](/posts/python-microservices-grpc-1/)
* [利用gRPC构建Python微服务(二)——gRPC基础](/posts/python-microservices-grpc-2/)
* [利用gRPC构建Python微服务(三)——实战Python gRPC](/posts/python-microservices-grpc-3/)
* [利用gRPC构建Python微服务(四)——在Kubernetes中部署](/posts/python-microservices-grpc-4/)
* [利用gRPC构建Python微服务(五)——微服务可观测性](/posts/python-microservices-grpc-5/)
* [利用gRPC构建Python微服务(六)——Python gRPC最佳实践](/posts/python-microservices-grpc-6/)
* [利用gRPC构建Python微服务(七)——AsyncIO和gRPC](/posts/python-microservices-grpc-7/)

## **AsyncIO 和 gRPC**

在官方的grpc包中AsyncIO的支持缺失了很长时间，但是最近已经被添加了。仍然属于实验性功能，目前仍然在积极开发中，但是如果你希望在你的微服务中尝试AsyncIO，这目前是最好的选择了。具体的信息请查看[gRPC AsyncIO文档](https://grpc.github.io/grpc/python/grpc_asyncio.html)。

grpclib是第三方包，实现了支持gPRC的AsyncIO，时间更久一点。

在服务端使用AsyncIO要非常小心。如果使用了阻塞代码，会让微服务陷于瘫痪。作为演示，这里使用AsyncIO编写Recommendations微服务，所有的逻辑去掉：

```python
import time

import asyncio
import grpc
import grpc.experimental.aio

from recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)
import recommendations_pb2_grpc

class AsyncRecommendations(recommendations_pb2_grpc.RecommendationsServicer):
    async def Recommend(self, request, context):
        print("Handling request")
        time.sleep(5)  # Oops, blocking!
        print("Done")
        return RecommendationResponse(recommendations=[])

async def main():
    grpc.experimental.aio.init_grpc_aio()
    server = grpc.experimental.aio.server()
    server.add_insecure_port("[::]:50051")
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        AsyncRecommendations(), server
    )
    await server.start()
    await server.wait_for_termination()

asyncio.run(main())
```

这里在17行有一个错误，在async函数中，你不小心进行了阻塞调用，这是一个非常大的禁忌。因为AsyncIO是单线程的，他阻塞了整个服务端，每次只能响应一个请求。这比现成服务器还要差。

你可以模拟使用多个并发请求：

```yaml
from concurrent.futures import ThreadPoolExecutor

import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY)
channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)

executor = ThreadPoolExecutor(max_workers=5)
a = executor.submit(client.Recommend, request)
b = executor.submit(client.Recommend, request)
c = executor.submit(client.Recommend, request)
d = executor.submit(client.Recommend, request)
e = executor.submit(client.Recommend, request)
```

虽然是五个并发请求，服务端返回情况是这样的：

```yaml
Handling request
Done
Handling request
Done
Handling request
Done
Handling request
Done
Handling request
Done
```

请求响应是串行的，这并不符合预期。

在服务端使用AsyncIO时要非常小心，一定不要阻塞。这意味着你不能使用像requests包，甚至无法将RPC请求发送到其他微服务中，除非你使用run_in_executor开启另外的线程。

还有一点需要注意的是数据库查询。很多常用的Python包并没有支持AsyncIO，所以使用时需要确认。除非你在服务端有着非常强烈的AsyncIO需要，所以需要等待更多包能够支持AsyncIO。阻塞的问题很难被找到。

如果你想了解更多AsyncIO，你可以查看[Getting Started With Async Features in Python](https://realpython.com/python-async-features/) 和 [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/).

## 结论

微服务是一种管理复杂系统的方式。随着组织的增长，这是一种天然的方式进行代码管理。正确理解如何有效的利用Python实现微服务，能够让你公司正常过程中获得真正的价值。

在这个课程中，你学到了：

- 如何基于gRPC有效实现Python微服务
- 如何将微服务部署到Kubernetes
- 如何在你的微服务中实现集成测试，拦截器，TLS和AsyncIO
- 创建微服务过程中遵循的最佳实践

你现在可以实践将你的大型Python项目，拆分为更小的微服务，让你的代码更加容易组织和维护。