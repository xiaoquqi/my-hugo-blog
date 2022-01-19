---
title: 利用gRPC构建Python微服务(二)
slug: python-microservices-grpc-2
date: 2022-01-19T17:33:00+08:00
draft: true
author: Dan Hipschman/老孙正经胡说
---

在上一篇文章中，我们重点从理论层面上学习了微服务架构的基本概念以及与传统单体架构的区别和优势，感兴趣的同学，可以阅读老孙正经胡说的第一篇《利用gRPC构建Python微服务(一)》获取之前的内容。在本篇内容中，重点向大家介绍gRPC的一些基础概念以及相对REST的优劣势。

<!-- more -->

## 微服务示例

示例需求：

- 定义一个API接口，实现微服务
- 定义两个微服务：
    - Marketplace：简单的web程序，向用户展示图书列表
    - Recommendations：显示用户可能喜爱的图书的列表

下图展示了服务之间的通讯关系：

![](/images/python-microservices-grpc-1.png)

用户通过浏览器访问Marketplace微服务，Marketplace微服务将和Recommendations进行通讯。

Recommendations API应该包含以下功能：

- User ID：用户个性化推荐标识，为了简单起见，样例是随机生成的
- **Book category：让API增加一些趣味性，添加图书的类目**
- Max results：最大推荐数量

返回的结果是一个列表，其中包含：

- Book ID：图书唯一标识
- Boot title：图书名称

我们使用**protocol buffers正式定义API接口，**这个protocol buffers中声明了你的API。Protocol buffers是Google开发的，提供了一种正式的API接口规范。这看起来有点神秘，以下注释部分是对每一行的详细描述：

```python
# 定义了该文件使用proto3协议取代旧的proto2版本
syntax = "proto3";

# 定义图书类目
enum BookCategory {
    MYSTERY = 0;
    SCIENCE_FICTION = 1;
    SELF_HELP = 2;
}

# 定义API请求，user_id和max_results使用了int32类型，而category使用了上面定义的BookCategory类型，可以暂时忽略
message RecommendationRequest {
    int32 user_id = 1;
    BookCategory category = 2;
    int32 max_results = 3;
}

# 定义图书推荐类型
message BookRecommendation {
    int32 id = 1;
    string title = 2;
}

# 定义了微服务响应，replated关键字代表返回的是BookRecommendation的类型的列表
message RecommendationResponse {
    repeated BookRecommendation recommendations = 1;
}

# 可以看做是一个函数，输入为RecommendationRequest，输出为RecommendationResponse
service Recommendations {
    rpc Recommend (RecommendationRequest) returns (RecommendationResponse);
}
```

这里rpc就是远程调用（**remote procedure call**），类似本地调用函数，但实际可能是在远程服务器运行该函数。

## 为什么是RPC和**Protocol Buffers？**

为什么使用这种方式来定义API接口呢？如果你想让一个微服务调用另外一个微服务，最简单的方法是通过HTTP调用，并返回一个Json类型的字符串。你可以使用这种方式，但是使用**Protocol Buffers则更有优势。**

### 文档

首先，使用protocol buffers可以让你使用更优雅并且自定义样式的方式定义API。如果使用Json，则你需要在文档中记录包含的字段及其类型。与任何文档一样，你可能面临不准确，或者文档未及时更新的风险。

当你使用protocol buffers进行API定义时，从中生成Python代码。你的代码永远不会和文档不一致，文档是好的，但是代码中的自我文档是更好的方式。

### 验证

第二点优势，是自动基于类型定义的验证。例如：生成的代码不会接受错误的类型。生成的代码还内置了所有RPC样板文件。

当你使用HTTP和Json构建API时，你需要写一些代码实现请求、发送、校验返回结果等。使用protocol buffers你就像调用本地函数一样，但底层实际上是一个网络调用。

你可以使用基于HTTP和JSON框架的Swagger和RAML获得同样的优势，具体信息可以查阅其他文档。

那么是否有充足的理由使用grpc，而不选择其他的呢？答案仍然是肯定的。

### 性能

gRPC框架是比传统HTTP请求效率更高。gRPC是在HTTP/2基础上构建的，能够在一个长连接上使用现成安全的方式进行多次并发请求。连接创建相对较慢，所以在多次请求时，一次连接并共享连接以节省时间。gRPC信息是二进制的，并且小于JSON。未来，HTTP/2会提供内置的头部压缩。

gRPC内置了对流式请求和返回的支持。比基础HTTP连接更好的管理网络问题，即使是在长时间断线后，也会自动重连。他还有连接器，你会在本向导后面学习到。你甚至可以实现插件，已经有人做出了这样的Python库。最根本的，你可以完全免费试用这个伟大的架构。

### 对开发人员友好

相较于REST，很多开发人员更喜欢gRPC，这其中的原因是，你不需要像REST一样使用动词或者资源来定义功能，而是直接使用函数方式。作为一名开发人员，更习惯的是函数思考方式，这也是grpcapi的定义方式。

实现REST API定义功能通常比较麻烦，你首先要确定资源，构造路径，以及使用哪个动词。通常有多个选择，如何嵌套资源，如何使用POST或其他动词。REST和gRPC孰优孰劣又会是一个争论的焦点，但是正如之前所说的，没有最好的技术，只有最适合需求场景的技术方案。

严格来说，protocol buffers是将数据通过序列化方式在两个微服务之间传输。所以，protocol buffers和JSON或XML都是相似的方式组织数据。不同的是，protocol buffers拥有更严格的格式和更压缩的方式在网络上通讯。

另外一方面，RPC架构应该被称为gRPC或者Google RPC。这很像HTTP。但正如上述所言，gRPC实际上是基于HTTP/2构建的。

(未完待续)