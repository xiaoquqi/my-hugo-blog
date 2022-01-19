---
title: 利用gRPC构建Python微服务(六)——Python gRPC最佳实践
slug: python-microservices-grpc-6
date: 2022-01-19T20:35:00+08:00
draft: false
author: Dan Hipschman/老孙正经胡说
tags:
  - Python
  - 微服务
  - 容器
  - 云原生
categories:
  - 微服务
---

在上一篇中，主要讲解了如何使用拦截器让微服务具备可观测性，本篇聊一下微服务的最佳实践，涉及代码组织结构、通讯加密等话题。

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

## 最佳实践

我们已经成功使用Python构建了微服务模块，并进行了测试、最终部署到了Kubernetes，同时使用拦截器进行监控。现在你可以创建更多的微服务模块。但是在开始之前有一些最佳实践还是有必要了解一下。

### 如何在代码仓库存储Protobuf文件

通常我们需要将protobuf的定义和你的微服务实现分离。客户端可以使用任何语言实现，如果你将protobuf文件写入了Python wheel或其他什么地方，如果有人想使用Ruby或者Go实现客户端，对于他们很难找到protobuf文件。

即使你的所有代码都是用Python开发的，为什么为了写一个客户端，而需要安装整个微服务呢？

解决方案之一是将你的protobuf文件存放在单独的Git代码库中，不和微服务模块代码放在一起。很多公司将所有微服务使用的protobuf文件存放在单独的仓库中。这样很容易找到所有微服务，共享通用protobuf结构，让使用更容易。

如果你选择将你的protobuf文件存放在一个仓库，需要注意组织结构，避免微服务间循环引用。

### Protobuf版本

API版本很难控制，主要原因是当你改变了API，并且更新了微服务，而其他的微服务可能还在使用旧的接口。特别是在客户端在用户本地的情况，像移动端或者桌面软件。

你不能简单强制升级，即使你可以，网络的延时也会引起竞争，你的微服务仍然会收到旧版本的API请求。好的API一定是能够向后兼容或者进行版本控制的。

为了实现向后兼容，使用protobufs v3版本的微服务可以接受请求，即使某些新字段不存在。所以如果你添加了一个新字段，是没有问题的。你可以先部署微服务，在没有发送新字段的情况下，仍然响应原有API请求。微服务自身处理好新字段就可以了。

如果你的改动较大，你需要给给你的API指定版本。Protobufs可以让你将API放入一个包含版本号的包命名空间中。如果你的改动很大，需要建立一个新的版本。微服务仍然能响应旧版本请求。当推出一个新版本API时，可以逐步淘汰旧版本。

遵循以上约定，你可以避免破坏性修改。在公司内部，通常认为临时性的修改是可以接受的，因为他们可以控制所有的客户端。这取决于你的决定，但是值得注意的一点，进行破坏性的更改需要协调客户端和微服务部署，让回滚变得很复杂。

在微服务生命周期早期，没有生产应用的情况下是可以的。但是一旦应用于生产环境，最好形成良好的习惯，不间断微服务的改变。

### Protobuf连接

确保不破坏更改Protobufs的方法是使用linter。比较常用的是buf。你可以将其设置为你CI系统的一部分，以应对临时性变更。

### 检查Protobuf生成代码

Mypy是一个用于严格检查Python代码的项目。如果你对静态检查不了解，请阅读Python Type Checking具体了解。

protoc生成的代码有点粗糙，而且没有类型注释。如果你使用Mypy检查代码，你会得到很多错误，而正正的错误例如字段拼写错误等问题被掩盖了。幸运的是，Dropbox的开发人员编写了一个protoc插件用于生成stubs类型。这些不会和gRPC stubs混淆。

如果要使用这个插件，需要安装mypy-protobuf包，并且更新命令行。注意新的参数—mypy_out选项：

```yaml
$ python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. --mypy_out=. ../protobufs/recommendations.proto
```

大部分Mypy错误都消失了，但是仍然有关于grpc包没有类型的错误信息。你可以安装非官方的gRPC type stubs并且添加如下Mypy配置：

```yaml
[mypy-grpc.*]
ignore_missing_imports = True
```

类型检查还是非常有用的，能够捕获拼写错误等问题，这对于在生产部署前发现问题很重要。

### 友好关闭应用

当你在开发环境运行微服务时，你使用CTRL + C去停止。这会引起Python拦截器发生KeyboardInterrupt异常。

当你的微服务运行在Kubernetes中时，你需要停止服务并进行滚动升级，将发送一个信号到你的微服务。具体来说，先发送SIGTERM信号，等待30秒。如果微服务仍然没有退出，则发送SIGKILL信号。

你可以，并且应该捕获SIGTERM，你可以处理完当前请求并且拒绝掉新请求。你可以在serve()中实现：

```yaml
from signal import signal, SIGTERM

...

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ...
    server.add_insecure_port("[::]:50051")
    server.start()

    def handle_sigterm(*_):
        print("Received shutdown signal")
        all_rpcs_done_event = server.stop(30)
        all_rpcs_done_event.wait(30)
        print("Shut down gracefully")

    signal(SIGTERM, handle_sigterm)
    server.wait_for_termination()
```

- 第1行引入signal，用于捕捉信号
- 第11行定义了函数捕获SIGTERM。这个函数在收到SIGTERM时被调用，并且传入两个参数。但是你不需要参数，用*_忽略他们
- 第13行调用server.stop(30)友好的关闭服务。并且拒绝新的服务，并等待30秒等到最终响应完成。他将立即返回threading.Event对象。
- 第14行等待Event对象，不至于过早退出
- 第17行注册你的handler

当你部署一个新的微服务，Kubernetes将发送信号关闭和退出微服务。让服务友好退出，保证请求不中断。

## **Channels加密**

目前我们使用了不安全的gRPC Channels，这意味着如下几件事情：

1、客户端无法确认是否将请求发送到了指定的服务端。有人可以创建一个冒名顶替的微服务，注入客户端可能发送请求的某个地方。例如，注入负载均衡发送请求的Pod中。

2、服务端也无法确认客户端是否向其发送了请求。只要有人可以连接到服务端，就可以发送任意gRPC请求。

3、传输也是非加密的，任何路由节点也能看到信息。

这一节将介绍如何添加TLS认证和加密。

注意：这一节的目的并不是用户认证，而是微服务进程本身。

你讲学习到两种方式设置TLS：

1、直接方式，客户端能验证服务端，而服务端不验证客户端

2、复杂方式，双向TLS，客户端和服务端互相验证

两种情况下，传输都是加密的。

#### **TLS基础**

在深入介绍之前，先简单了解一下TLS：通常来说就是客户端验证服务端。例如，当你访问Amazon.com，你的浏览器验证是不是真的Amazon.com，而不是钓鱼网站。要做到这一点，就必须从第三方权威机构获取获取某种保证，就像你信任一个新的朋友因为你们有一个共同的朋友为他担保一样。

使用TLS，客户端必须信任“证书颁发机构”（简称CA）。CA将签署服务服务端的某些东西，让客户端能够加以验证。这就像你们共同的朋友在纸条上签字，你能认识他们的笔记。更多信息，请查询[互联网安全是如何实现的：TLS、SSL和CA](https://opensource.com/article/19/11/internet-security-tls-ssl-certificate-authority)。

你的浏览器默认信任了一些CA机构，像GoDaddy, DigiCert或者Verisign。其他公司，例如Amazon，向CA公司付费签名了证书，所以你的浏览器也信任他们。例如，CA公司在签署证书前，先验证Amazon是否拥有Amazon.com。这种情况下，拦截方式不会拥有Amazon.com的签名证书，你的浏览器就直接屏蔽了钓鱼网站。

使用微服务时，你并不需要向CA结构签署你的证书，因为你的微服务是在内部运行。CA架构当然乐于你付费进行证书签名，但这是不切实际的。这种情况下，你可以将自己作为CA机构，自行签署证书，gRPC客户端会信任服务服务端。

#### 服务端鉴权

下面的命令会生成一个CA证书用于服务端签名认证：

```yaml
openssl req -x509 -nodes -newkey rsa:4096 -keyout ca.key -out ca.pem \
              -subj /O=me
```

这里生成了两个文件：

1、ca.key是私钥

2、ca.pem是公钥

此时你可以为你的服务端建立证书，签署你的CA认证：

```yaml
$ openssl req -nodes -newkey rsa:4096 -keyout server.key -out server.csr \
              -subj /CN=recommendations
$ openssl x509 -req -in server.csr -CA ca.pem -CAkey ca.key -set_serial 1 \
              -out server.pem
```

此时会生成三个新文件：

1、server.key是服务端私钥

2、server.csr是中间文件

3、server.pem是服务端公钥

注意：这些命令这是演示。私钥也并没有加密。如果你想为公司生成，需要咨询你的安全团队。他们会根据策略生成、储存和回收密钥。

你可以将这些命令添加到Recommendations微服务的Dockerfile中。向容器镜像安全的添加密钥，但是可以使用这种方式：

```yaml
# syntax = docker/dockerfile:1.0-experimental
# DOCKER_BUILDKIT=1 docker build . -f recommendations/Dockerfile \
#                     -t recommendations --secret id=ca.key,src=ca.key

FROM python

RUN mkdir /service
COPY infra/ /service/infra/
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
COPY ca.pem /service/recommendations/

WORKDIR /service/recommendations
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto
RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations \
                -keyout server.key -out server.csr
RUN --mount=type=secret,id=ca.key \
    openssl x509 -req -in server.csr -CA ca.pem -CAkey /run/secrets/ca.key \
                 -set_serial 1 -out server.pem

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]
```

下面是对高亮部分的解释：

- 第一行是开启secrets
- 第二行和第三行显示如何构建容器的命令行
- 第11行将生成的CA公钥拷贝至镜像
- 第18行和19行生成一个新的服务端密钥和证书
- 第20到22行临时加载CA私钥，这样可以给服务端证书签名。然后，他并不会被保留在镜像中

注意：更多关于`‑‑mount=type=secret`，可以查看[Docker官方文档](https://docs.docker.com/develop/develop-images/build_enhancements/#new-docker-build-secret-information)。未来这个功能会被放入正式版本，那个时候你无须再在Dockerfile头部添加`syntax = docker/dockerfile:1.0-experimental`

根据版本控制策略，实验性的语法也不会被删除，你可以一直使用。

现在你的镜像中含有以下文件：

- `ca.pem`
- `server.csr`
- `server.key`
- `server.pem`

你可以更新recommendations.py中的serve()方法：

```yaml
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )

    with open("server.key", "rb") as fp:
        server_key = fp.read()
    with open("server.pem", "rb") as fp:
        server_cert = fp.read()

    creds = grpc.ssl_server_credentials([(server_key, server_cert)])
    server.add_secure_port("[::]:443", creds)
    server.start()
    server.wait_for_termination()
```

更新内容如下：

- 第7-10行，加载服务端私钥和证书
- 第12-13行，服务端使用TLS。仅仅接受TLS加密的连接请求

同时，marketplace.py也需要加载CA证书。客户端只需要公钥证书：

```yaml
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
with open("ca.pem", "rb") as fp:
    ca_cert = fp.read()
creds = grpc.ssl_channel_credentials(ca_cert)
recommendations_channel = grpc.secure_channel(
    f"{recommendations_host}:443", creds
)
recommendations_client = RecommendationsStub(recommendations_channel)
```

Marketplace Dockerfile需要添加`COPY ca.pem /service/marketplace/`

现在运行以加密方式运行客户端和服务端，客户端会验证服务端，使用docker-compose更新环境。目前，docker-compose还不支持secrets功能的构建，只能用手动方式替代docker-compose build。

启动时仍然可以使用docker-compose up，更新docker-compose.yaml并且移除build段落：

```yaml
version: "3.8"
services:

    marketplace:
        environment:
            RECOMMENDATIONS_HOST: recommendations
        # DOCKER_BUILDKIT=1 docker build . -f marketplace/Dockerfile \
        #                   -t marketplace --secret id=ca.key,src=ca.key
        image: marketplace
        networks:
            - microservices
        ports:
            - 5000:5000

    recommendations:
        # DOCKER_BUILDKIT=1 docker build . -f recommendations/Dockerfile \
        #                   -t recommendations --secret id=ca.key,src=ca.key
        image: recommendations
        networks:
            - microservices

networks:
    microservices:
```

现在流量已经被加密，验证是否被连接至正确的服务端。

### 双向认证

服务端目前是可以证明被信任的了，但是服务端还没有。幸运的是，TLS支持双向验证。更新Marketplace的Dockerfile文件如下：

```yaml
# syntax = docker/dockerfile:1.0-experimental
# DOCKER_BUILDKIT=1 docker build . -f marketplace/Dockerfile \
#                     -t marketplace --secret id=ca.key,src=ca.key

FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY marketplace/ /service/marketplace/
COPY ca.pem /service/marketplace/

WORKDIR /service/marketplace
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto
RUN openssl req -nodes -newkey rsa:4096 -subj /CN=marketplace \
                -keyout client.key -out client.csr
RUN --mount=type=secret,id=ca.key \
    openssl x509 -req -in client.csr -CA ca.pem -CAkey /run/secrets/ca.key \
                 -set_serial 1 -out client.pem

EXPOSE 5000
ENV FLASK_APP=marketplace.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
```

These changes are similar to the ones you made for the Recommendations microservice in the preceding section.

这个变更和上述Recommendations微服务的修改差不多。

注意：如果你将私钥放入Dockerfiles，不要放入公共的代码库中。最好在启动时加载私钥，通过网络或者服务端通过VPN。

在recommendations.py中更新serve()客户端鉴权如下：

```yaml
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )

    with open("server.key", "rb") as fp:
        server_key = fp.read()
    with open("server.pem", "rb") as fp:
        server_cert = fp.read()
    with open("ca.pem", "rb") as fp:
        ca_cert = fp.read()

    creds = grpc.ssl_server_credentials(
        [(server_key, server_cert)],
        root_certificates=ca_cert,
        require_client_auth=True,
    )
    server.add_secure_port("[::]:443", creds)
    server.start()
    server.wait_for_termination()
```

加载CA证书并且要求客户端鉴权。

最后，更新marketplace.py，将证书发送至服务端：

```yaml
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
with open("client.key", "rb") as fp:
    client_key = fp.read()
with open("client.pem", "rb") as fp:
    client_cert = fp.read()
with open("ca.pem", "rb") as fp:
    ca_cert = fp.read()
creds = grpc.ssl_channel_credentials(ca_cert, client_key, client_cert)
recommendations_channel = grpc.secure_channel(
    f"{recommendations_host}:443", creds
)
recommendations_client = RecommendationsStub(recommendations_channel)
```

这将加载证书，并且发送至服务端校验。

如果你用其他的客户端连接服务端，即使使用了TLS方式，但是是未知的证书，服务端也会拒绝，提示`PEER_DID_NOT_RETURN_A_CERTIFICATE`错误。

重要：虽然可以使用这种方式管理双向TLS，但是要做到这一点也并不容易。比如，你只想让特定某些微服务访问其他的，这就变得很困难。

如果你需要按照这种方式提高安全性，最好使用服务网格（service mesh）实现证书和授权的管理。在拦截器一章提及的lstio也可以管理双向TLS和每个服务的认证。它更加安全，因为他为你管理secrets并且更频发的办法证书。

这一篇总结了微服务间通讯的方式。接下来，我们要学习在微服务中如何使用AsyncIO。