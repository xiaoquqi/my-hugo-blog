---
title: 利用gRPC构建Python微服务(三)——实战Python gRPC
slug: python-microservices-grpc-3
date: 2022-01-19T19:33:00+08:00
draft: false
author: Dan Hipschman/老孙正经胡说
tags:
  - Python
  - 微服务
  - 容器
  - 云原生
categories:
  - 微服务
weight: 3
---

在上一篇中，主要向大家介绍了gRPC的一些基础概念，以及基本的定义方式，本篇将进入实战教程，如何用Python实现服务端和客户端，通过gRPC进行交互。

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

## 代码样例

现在正式进入实现部分，我们来看看protoco buffers能做什么？protobufs是简称，后续会大量出现。

正如上面提到的，你可以从protobufs生成Python代码。这个工作是作为grpcio-tools包的一部分。

首先，定义你的初始目录结构:

```python
.
├── protobufs/
│   └── recommendations.proto
|
└── recommendations/
```

protobufs包含recommendations.proto文件，这是我们上面定义的部分。

你将在recommendations目录生成Python代码。首先，你需要安装grpcio-tools，创建`recommendations/requirements.txt`

```python
grpcio-tools ~= 1.30
```

可以创建一个virtualenv环境来运行后续代码，在虚拟环境中安装依赖。

```python
virtualenv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

从protobufs生成代码

```python
$ cd recommendations
$ python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto
```

此处将生成两个文件

```python
$ ls
recommendations_pb2.py recommendations_pb2_grpc.py
```

这些文件包含与API通讯的Python类型和函数。编译器生成客户端代码并调用RPC和Server端代码实现远程调用。我们先来看一下客户端代码部分。

### RPC客户端

这里生成的代码可读性并不高

```python
>>> from recommendations_pb2 import BookCategory, RecommendationRequest
>>> request = RecommendationRequest(
...     user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
... )
>>> request.category
1
```

protobuf编译器生成了与你的protobuf类型对应的 Python 类型。到目前为止，一切顺利。你还可以看到一些类型的检查字段:

```python
>>> request = RecommendationRequest(
...     user_id="oops", category=BookCategory.SCIENCE_FICTION, max_results=3
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'oops' has type str, but expected one of: int, long
```

如果传入错误字段类型，则抛出TypeError。

在proto3中所有字段是可选的，所以你要校验是否正确设置所有值。如果其中一个未提供，如果为数值类型则默认为0，如果是字符类型默认为空：

```python
>>> request = RecommendationRequest(
...     user_id=1, category=BookCategory.SCIENCE_FICTION
... )
>>> request.max_results
0
```

因为没有设置int字段的默认值，所以返回0。

虽然protobufs为你进行了初步检查，但是仍然需要从自身业务角度验证数据的有效性，其实无论使用何种实现方式，这都是必须要做的。

生成的recommendations_pb2.py文件包含了类型定义，而recommendations_pb2_grpc.py文件则包含了客户端和服务端基本通讯框架。以下就是client在使用时需要的引入：

```python
>>> import grpc
>>> from recommendations_pb2_grpc import RecommendationsStub
```

引入grpc是为了设置与远程服务的链接。之后导入RPC客户端stub，之所以叫做stub是因为客户端本身并不包含任何功能。只是调用远程服务并传回结果。

如果你查看protobuf的定义，你会看到在service Recommendations的定义最后。protobuf的编译器使用Recommendations，并且追加从客户端的名称Stub，就构成了RecommendationStub

```python
service Recommendations {
    rpc Recommend (RecommendationRequest) returns (RecommendationResponse);
}
```

现在你可以发送RPC请求了

```python
>>> channel = grpc.insecure_channel("localhost:50051")
>>> client = RecommendationsStub(channel)
>>> request = RecommendationRequest(
...     user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3
... )
>>> client.Recommend(request)
Traceback (most recent call last):

grpc._chanel._inactivRpcError: <_InactiveRpcError...
    status = StatusCode.UNAVAILABLE
    details = "failed to connect to all addresses"
    ...
```

在代码示例中，你尝试使用非授权和非加密的方式连接本地的50051端口，这是grpc的标准端口。你可以将channel传给你的stub并实例化你的client。

现在可以调用在你微服务Recommendations中定义的Recommend方法。在protobuf中25行定义的内容：rpc Recommend (...) returns (...)。这就是Recommend方法所在。程序运行异常是由于本地服务中并没有真正运行50051的微服务，后续会实现。

下面来看一下服务端实现。

### RPC服务端

打开两个终端，一个用于调试客户端，一个用于调试服务端。从基本导入和数据开始：

```python
# recommendations/recommendations.py
from concurrent import futures
import random

import grpc

from recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)
import recommendations_pb2_grpc

books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="The Maltese Falcon"),
        BookRecommendation(id=2, title="Murder on the Orient Express"),
        BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(
            id=4, title="The Hitchhiker's Guide to the Galaxy"
        ),
        BookRecommendation(id=5, title="Ender's Game"),
        BookRecommendation(id=6, title="The Dune Chronicles"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(
            id=7, title="The 7 Habits of Highly Effective People"
        ),
        BookRecommendation(
            id=8, title="How to Win Friends and Influence People"
        ),
        BookRecommendation(id=9, title="Man's Search for Meaning"),
    ],
}
```

示例中导入了grpc的依赖并创建了一些示例数据，下面是详细的解释：

- 第二行：导入futures是因为gRPC运行需要线程池
- 第三行：导入random是为了随机生成一些推荐的图书
- 第十四行：创建books_by_categry字典，在实际的微服务项目中，这些是存在数据库中

下一步，需要创建一个类实现微服务的方法

```python
class RecommendationService(
    recommendations_pb2_grpc.RecommendationsServicer
):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(
            books_for_category, num_results
        )

        return RecommendationResponse(recommendations=books_to_recommend)
```

创建一个类实现Recommend RPC，以下是详细解释：

- 第29行，定义了RecommendationService类。这是你微服务的实现。注意子类RecommendationsServicer是实现gRPC必须要做的。
- 第32行，定义了Recommend()方法，这个名字必须和protobuf文件中定义的一样。方法中接受RecommendationRequest并且返回RecommendationResponse，和protobuf定义内容一致。content参数可以用于定义返回的状态值。
- 第33到34行，如果你得到一个未知的种类，则使用abort()方法结束请求，并将状态码设置为NOT_FOUND。由于gRPC是基于HTTP/2创建的，状态码类似标准的HTTP状态码。这样可以针对接受进行不同的处理。同时允许中间件，类似监控系统，记录有多少请求包含错误。
- 第36到40行，随机挑选一些指定种类的书。使用max_results约束最大推荐数量。使用min控制超出的范围，否则random.sample将抛出异常。
- 第38行，返回RecommendationResponses对象，包含推荐的图书。

另外一点建议，最好用raise exception方式处理异常，而不是像例子中的abort()，但是返回的状态码可能不能被正确设置，后续章节会介绍如何规避这个问题。

RecommendationService定义了微服务实现，你还是需要运行。示例如下：

```python
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
```

serve()启动了一个网络服务，用于微服务处理请求：

- 第42行，创建一个gRPC服务，使用10个现成提供服务，对于这个例子有点太多了，但是对于实际上的服务，这是一个比较推荐的默认值
- 第43行，将类关联的服务中，即服务的响应
- 第46行，将服务监听50051端口，这是gRPC的默认短开口，但是可以替换成你需要的
- 第47和48行，server.start()和server.wait_for_termination()用于启动服务并等待直到停止。唯一暂停服务的方法是在中断中使用CTRL + C。但是在生产环境中，还是需要更好的方法停止，后面会介绍到。

### 运行测试

终端中运行：

```bash
$ python recommendations.py
```

如果你的终端仍然打开，可以在console中输入：

```python
>>> import grpc
>>> from recommendations_pb2_grpc import RecommendationsStub
>>> channel = grpc.insecure_channel("localhost:50051")
>>> client = RecommendationsStub(channel)
```

发送一个请求：

```python
>>> request = RecommendationRequest(
...    user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
>>> client.Recommend(request)
recommendations {
  id: 6
  title: "The Dune Chronicles"
}
recommendations {
  id: 4
  title: "The Hitchhiker\'s Guide To The Galaxy"
}
recommendations {
  id: 5
  title: "Ender\'s Game"
}
```

成功了，你发送了一个RPC请求到你的微服务中，并得到一个请求。每次返回结果不同是因为随机选择。

现在你的服务端已经实现，可以尝试实现Marketplace微服务，并让他调用Recommendations微服务。保留Recommendations微服务运行，其他窗口可以关闭。

### 实现Marketplace

创建新的marketplace目录，并添加marketplace.py文件，现在目录结构为：

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
└── recommendations/
    ├── recommendations.py
    ├── recommendations_pb2.py
    ├── recommendations_pb2_grpc.py
    └── requirements.txt
```

marketplace下包含多个文件，可以先创建空文件，后续逐步实现。

现在可以开始实现微服务代码了。Marketplace微服务是一个Flask应用，为用户提供页面。他调用Recommendations为辅获取图书推荐并在页面展现。

在marketplace/marketplace.py中添加如下内容：

```python
# marketplace/marketplace.py
import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
recommendations_client = RecommendationsStub(recommendations_channel)

@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=3
    )
    recommendations_response = recommendations_client.Recommend(
        recommendations_request
    )
    return render_template(
        "homepage.html",
        recommendations=recommendations_response.recommendations,
    )
```

这里创建了一个Flask应用和gRPC客户端，增加了一个方法渲染主页。代码详情：

- 第10行，创建Flask应用并为用户渲染网页
- 第12到16行，创建gRPC channel和stub
- 第20到30行，用户访问时，调用render_homepage()。通过模板返回HTML页面

> 在这个示例中，你创建了一个全局性的gRPC channel和stub。通常来说，global是不推荐使用的，但是这个示例是个例外。
> gRPC channel保持一个持久性连接，避免多次重建连接。满足并发性需要，连接断掉后自动重建。但是，如果你每次是在请求时建立新的channel，然后Python再回收，无法获得长连接的最大优势。
> 你需要保持channel打开，并且不需要每次重新连接recommendations微服务。你能将channel隐藏在其他模块中，但是本地中只有一个文件，所以为了简单，使用了全局定义。

打开marketplace/tempaltes/homepage.html文件，添加如下内容：

```html
<!-- homepage.html -->
<!doctype html>
<html lang="en">
<head>
    <title>Online Books For You</title>
</head>
<body>
    <h1>Mystery books you may like</h1>
    <ul>
    {% for book in recommendations %}
        <li>{{ book.title }}</li>
    {% endfor %}
    </ul>
</body>
```

这仅是一个demo页面。全部完成后，应该显示推荐图书的清单。

如果想执行代码，你需要添加依赖，在你的marketplace/requiirements.txt中添加：

```yaml
flask ~= 1.1
grpcio-tools ~= 1.30
Jinja2 ~= 2.11
pytest ~= 5.4
```

为marketplace生成protbufs

```bash
$ cd marketplace
$ python -m grpc_tools.protoc -I ../protobufs --python_out=. \
         --grpc_python_out=. ../protobufs/recommendations.proto
```

运行Marketplace微服务

```bash
$ FLASK_APP=marketplace.py flask run
```

执行Flask app，默认端口为5000

![](/images/python-microservices-grpc-2.png)