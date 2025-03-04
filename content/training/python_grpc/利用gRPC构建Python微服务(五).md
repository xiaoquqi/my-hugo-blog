---
title: 利用gRPC构建Python微服务(五)——微服务可观测性
slug: python-microservices-grpc-5
date: 2022-01-19T20:34:00+08:00
draft: false
author: Dan Hipschman/老孙正经胡说
tags:
  - Python
  - 微服务
  - 容器
  - 云原生
categories:
  - 微服务
weight: 5
---

在上一篇中，主要讲解了如何将开发好的微服务模块部署到Kubernetes中，本篇将介绍拦截器的使用方法。

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

## 使用拦截器(Interceptors)对微服务进行监控

一旦你在云中使用了微服务，你需要具备可观测性。你需要监控的项目包括：

- 每个微服务收到的请求
- 错误请求，以及错误内容
- 请求延时
- 异常堆栈帮助后续调查

下面就介绍一些方法。

### 为什么不用装饰器(**Decorators**)

对于Python开发人员自然想到在每个微服务端点使用装饰器（Decorator）。这种情况下，使用装饰器有以下缺点：

- 新的微服务开发时，开发人员需要记住在每个方法前添加装饰器
- 如果你有很多监控，你可能在各种装饰器的堆栈中结束
- 如果你有几个装饰器，开发人员可能顺序排错了
- 你可能想把所有的监控写入单一装饰器中，但是这只能让一切变得更加混乱

这个装饰器堆栈是你想避免的：

```python
class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    @catch_and_log_exceptions
    @log_request_counts
    @log_latency
    def Recommend(self, request, context):
        ...
```

以上实现非常丑陋并且重复，违反了DRY programming原则：不要重复制造轮子。装饰器开发中也具有挑战，特别是接受了很多参数。

### 拦截器(**Interceptors)**

这里面介绍一下gRPC中提供的类似装饰器的方式——拦截器，比装饰器的实现更加干净。

#### 实现拦截器

很不幸，Python实现gRPC拦截器API非常复杂，因为过于灵活。但grpc-inteceptor包对此进行了简化。

将他们添加到`recommendations/requirements.txt`

```yaml
grpc-interceptor ~= 0.12.0
grpcio-tools ~= 1.30
pytest ~= 5.4
```

更新你的virtualenv环境

```bash
$ python -m pip install recommendations/requirements.txt
```

以下是一个拦截器的示例

```python
from grpc_interceptor import ServerInterceptor

class ErrorLogger(ServerInterceptor):
    def intercept(self, method, request, context, method_name):
        try:
            return method(request, context)
        except Exception as e:
            self.log_error(e)
            raise

    def log_error(self, e: Exception) -> None:
        # ...
```

当发生未捕获异常时，会调用log_error，你可以尝试实现，将异常发送至APM系统等。

使用这个拦截器，你只需要传给grpc.server()

```python
interceptors = [ErrorLogger()]
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                     interceptors=interceptors)
```

使用这段代码，所有微服务的请求和返回都经过你的拦截器，这样你就可以统计有多少请求是错误的。

grpc-interceptor也为每个gRPC状态码提供了异常拦截器`ExceptionToStatusInterceptor`。如果微服务抛出异常，然后`ExceptionToStatusInterceptor`将设置了gRPC状态码。这可以让你轻松的简化你的代码，如下面的高亮部分：

```python
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

# ...

class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            raise NotFound("Category not found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=interceptors
    )
    # ...
```

代码的可读性更高，你能从很多函数中抛出异常，无须传给context，通过调用context.abort()实现。拦截器将为你捕获抛出的异常，无须自行实现。

#### 测试拦截器

如果你想开发自己的拦截器，你应该测试他们。但是使用mock方式测试拦截器很危险。举个例子，你可以在测试中调用.intercept()，确保返回你预期内容，但是不会测试真实的输入甚至不会被调用。

为了优化测试，可以运行带拦截器的gRPC微服务。grpc-interceptor提供一个框架去实现。下面，为ErrorLogger拦截器写一个测试。这仅仅是一个测试，不需要在代码中实现，如果需要加入项目中，则需要添加到单独的测试文件中。

```python
from grpc_interceptor.testing import dummy_client, DummyRequest, raises

class MockErrorLogger(ErrorLogger):
    def __init__(self):
        self.logged_exception = None

    def log_error(self, e: Exception) -> None:
        self.logged_exception = e

def test_log_error():
    mock = MockErrorLogger()
    ex = Exception()
    special_cases = {"error": raises(ex)}

    with dummy_client(special_cases=special_cases, interceptors=[mock]) as client:
        # Test no exception
        assert client.Execute(DummyRequest(input="foo")).output == "foo"
        assert mock.logged_exception is None

        # Test exception
        with pytest.raises(grpc.RpcError) as e:
            client.Execute(DummyRequest(input="error"))
        assert mock.logged_exception is ex
```

在某些场景下，可以使用service mesh实现拦截器。所有微服务的请求和返回都会经过代理，从代理层面可以自动处理日志或者记录错误次数。为了获取更精确地错误输出，你的微服务需要正确设置状态码。在某些场景下，你的拦截器能实现server mesh。一种流行的server mesh是lstio。