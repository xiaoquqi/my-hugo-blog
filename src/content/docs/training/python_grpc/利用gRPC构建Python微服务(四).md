---
title: 利用gRPC构建Python微服务(四)——在Kubernetes中部署
date: 2022-01-19T12:33:00.000Z
tags:
  - Python
  - 微服务
  - 容器
  - 云原生
authors:
  - Dan Hipschman/老孙正经胡说
---

上一篇中，主要向大家讲解了在Python中，基于gRPC protobufs实现客户端和服务端通讯，最后通过REST API对外界提供访问接口，在本篇文章中，向大家介绍如何利用在容器平台部署微服务模块。一些原有文章中对于容器的讲解被精简了。



## 全文导航

为了方便大家阅读，这里将全部目录进行一下索引，方便大家在老孙正经胡说(https://sunqi.site)中查看相关文章：

* [利用gRPC构建Python微服务(一)——关于微服务](/training/python_grpc/利用grpc构建python微服务一/)
* [利用gRPC构建Python微服务(二)——gRPC基础](/training/python_grpc/利用grpc构建python微服务二/)
* [利用gRPC构建Python微服务(三)——实战Python gRPC](/training/python_grpc/利用grpc构建python微服务三/)
* [利用gRPC构建Python微服务(四)——在Kubernetes中部署](/training/python_grpc/利用grpc构建python微服务四/)
* [利用gRPC构建Python微服务(五)——微服务可观测性](/training/python_grpc/利用grpc构建python微服务五/)
* [利用gRPC构建Python微服务(六)——Python gRPC最佳实践](/training/python_grpc/利用grpc构建python微服务六/)
* [利用gRPC构建Python微服务(七)——AsyncIO和gRPC](/training/python_grpc/利用grpc构建python微服务七/)

## 生产环境就绪的Python微服务

本节主要介绍使用容器来运行Python微服务环境，这里只保留Dockerfile部分内容。

### Recommendations Dockerfile

```yaml
FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
WORKDIR /service/recommendations
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]
```

构建

```bash
$ docker build . -f recommendations/Dockerfile -t recommendations
```

运行

```bash
$ docker run -p 127.0.0.1:50051:50051/tcp recommendations
```

### Marketplace Dockerfile

```yaml
FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY marketplace/ /service/marketplace/
WORKDIR /service/marketplace
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto

EXPOSE 5000
ENV FLASK_APP=marketplace.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
```

构建

```bash
$ docker build . -f marketplace/Dockerfile -t marketplace
```

执行

```bash
$ docker run -p 127.0.0.1:5000:5000/tcp marketplace
```

### 网络问题

在marketplace.py文件中

```python
recommendations_channel = grpc.insecure_channel("localhost:50051")
```

通过环境变量获取连接地址

```python
recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
```

重新构建，并启动

```bash
$ docker build . -f marketplace/Dockerfile -t marketplace
$ docker run -p 127.0.0.1:5000:5000/tcp --network microservices \
             -e RECOMMENDATIONS_HOST=recommendations marketplace
```

### Docker Compose

采用Docker compse文件降低编排复杂度

```yaml
version: "3.8"
services:

    marketplace:
        build:
            context: .
            dockerfile: marketplace/Dockerfile
        environment:
            RECOMMENDATIONS_HOST: recommendations
        image: marketplace
        networks:
            - microservices
        ports:
            - 5000:5000

    recommendations:
        build:
            context: .
            dockerfile: recommendations/Dockerfile
        image: recommendations
        networks:
            - microservices

networks:
    microservices:
```

现在的目录结构

```bash
.
├── marketplace/
│   ├── marketplace.py
│   ├── requirements.txt
│   └── templates/
│       └── homepage.html
|
├── protobufs/
│   └── recommendations.proto
|
├── recommendations/
│   ├── recommendations.py
│   ├── recommendations_pb2.py
│   ├── recommendations_pb2_grpc.py
│   └── requirements.txt
│
└── docker-compose.yaml
```

启动

```bash
$ docker-compose up
```

## 部署到Kubernetes

原文在这方面介绍的好细致，值得称赞，不过这里默认读者已经全部掌握了，不再赘述。

### Marketplace

```yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
    name: marketplace
    labels:
        app: marketplace
spec:
    replicas: 3
    selector:
        matchLabels:
            app: marketplace
    template:
        metadata:
            labels:
                app: marketplace
        spec:
            containers:
                - name: marketplace
                  image: hidan/python-microservices-article-marketplace:0.1
                  env:
                      - name: RECOMMENDATIONS_HOST
                        value: recommendations
```

### Recommendations

```yaml
---
apiVersion: apps/v1
kind: Deployment
metadata:
    name: recommendations
    labels:
        app: recommendations
spec:
    replicas: 3
    selector:
        matchLabels:
            app: recommendations
    template:
        metadata:
            labels:
                app: recommendations
        spec:
            containers:
                - name: recommendations
                  image: hidan/python-microservices-article-recommendations:0.1
```

### Recommendation Service定义

```yaml
---
apiVersion: v1
kind: Service
metadata:
    name: recommendations
spec:
    selector:
        app: recommendations
    ports:
        - protocol: TCP
          port: 50051
          targetPort: 50051
```

### Marketplace Service定义

```yaml
---
apiVersion: v1
kind: Service
metadata:
    name: marketplace
spec:
    type: LoadBalancer
    selector:
        app: marketplace
    ports:
        - protocol: TCP
          port: 5000
          targetPort: 5000
```

### 部署

```bash
$ kubectl apply -f kubernetes.yaml
```
