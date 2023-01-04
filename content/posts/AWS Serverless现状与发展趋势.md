---
title: AWS Serverless现状与发展趋势
author: 孙琦(Ray)
tags:
  - Serverless
categories: []
date: 2022-02-21 07:30:00 +08:00
---
Serverless架构是最近一直非常关注的技术方向，基础架构在应用构建中的地位被被进一步弱化的趋势不可逆转。Serveless让开发者更加关注业务本身逻辑的特性决定了技术演进的趋势。

目前，很多人可能很难认可这样的观点，大部分人还是认为Kubernetes能够带来更多的灵活性。但是Kubernetes对于应用开发者来说，仍然要顾及底层架构。Serverless的终极目标就是彻底打消这层的关系。但不可否认的一点，Kubernetes、OpenStack等基础平台作为Serverless的底层支撑一定会长期存在，所以二者之间并非竞争关系，而是发展的阶段的不同。从另外一个角度看，在公有云最佳实践中，函数计算已经成为构建应用必不可少的一环。

<!-- more -->

我大概在2018年左右接触了AWS Lambda服务，后续一直在关注着Serverless趋势，所以本文就结合我的一点粗浅理解来分析一下AWS、阿里云和腾讯云在Serverless架构发展的趋势（分为三篇）。本文中的观点是我自身使用公有云相关服务的经验，难免存在片面性，如有不妥之处，请各位给予批评和指正。

这里先借用一张InfoQ在《Serverless国内发展纵向观察》的一张图，前面的文章中我也讲到这个问题，对于云来说，Serverless架构很重要的两个部分就是函数即服务（Function-as-a-Service）和后端即服务（Backend-as-a-Service）两部分，这两种服务类型有都属于云原生的范畴。

![upload successful](/images/pasted-162.png)

由上图可知，FaaS和BaaS是成就Serverless的关键服务能力。函数计算的执行是通过各个云原生服务触发的（触发器执行），所以作为Serverless架构中的业务逻辑实现层，函数计算及其相关服务的发展策略基本代表了一家云商对于Serverless架构的态度。每个云其实都会有自己对Serverless的独特理解，有共性也有差别，同时又都有自身对于Serverless未来场景的理解。

## AWS Serverless现状

我在上一篇关于《Serverless发展历史》的中提到，2014年AWS发布函数计算服务Lambda，开启了新Serverless的篇章，自此以后各大公有云纷纷推出自己的函数计算服务。截止目前为止，AWS仍然是公有云领域的引领者，也是为数不多盈利的公有云公司，其发展方向一直是其他友商追逐的目标。

从局部角度看，函数计算服务在整个云计算架构中像一个粘合剂，巧妙的串联了各个云原生服务，让“不可变”的云原生服务具备了“可变性”，巧妙的解决了云原生服务之间最后一公里的问题。目前，这种使用方式几乎涵盖了AWS所有的最佳实践。

## AWS Serverless架构

根据AWS的定义，将Serverless架构定义为三层服务类别：计算、应用集成和数据存储。

### 计算

计算层主要包括Lambda和Fargate服务。Lambda是函数计算服务，Fargate是AWS的容器编排引擎，Fargate服务包含两种不同不同的方式：一种是自有的引擎(ECS服务)，另外一种是基于Kubernetes底座的。相较于AWS EC2服务，容器编排层好像并不是AWS关注的重点，这一点从容器服务与其他服务联动性能够隐约感觉出来。但是，AWS Lambda服务绝对足够强大。

![upload successful](/images/pasted-173.png)

### 应用集成

应用集成类主要包含了用于串联函数计算的相关服务。SQS/SNS/API都是非常常用的触发器；AppSync提供了GraphQL的接口，能够从函数计算获取数据；EventBridge提供了事件驱动的架构，扩展了函数计算的事件触发类别，同时也可以进行自定义。

![upload successful](/images/pasted-177.png)

Step Functions通过状态机的定义，很好的让多个函数计算有序运行，降低Serverless架构控制难度。

![upload successful](/images/pasted-178.png)

### 数据存储

在任何应用场景下，数据都是用户最宝贵的资源，特别是在当今社会下，数据被供奉在一个前所未有的高度。在与Lambda配合使用的持久化存储方面，除了常规的对象存储和非关系型数据库，还支持了RDS Proxy和Aurora Serverless。

![upload successful](/images/pasted-179.png)

RDS Proxy主要解决并发访问RDS数据库连接数量的限制，由于函数计算随时启停的特点，无法像我们在开发传统应用时使用统一的数据库连接资源池来控制数据库的访问连接数。当并发量非常大时，会超过最大连接数导致失败的情况，所以RDS Proxy就是专门用于解决这一问题的服务。

![upload successful](/images/pasted-182.png)


## 函数服务Lambda

### 开发语言支持

目前函数计算服务几乎覆盖了主流的高级开发语言，如果你的语言比较特殊，还可以基于容器自定义，提供了最大灵活度，这也是大部分厂商通用的做法。

![upload successful](/images/pasted-181.png)

### 触发器

我们重点来看看Lmabda服务，函数计算是由事件触发的，以目前的认知，AWS Lambda与国内的公有云相比，是触发器最多的云平台(Google和AZure我没有对比过)。能够触发Lambda的，除了传统的数据库、消息队列、对象存储等，还包括了物联网设备，包括loT和Alexa音箱。

![upload successful](/images/pasted-174.png)

除了云原生服务外，还通过EventBridge支持第三方服务直接触发Lambda，为应用开发提供了极大的便利性。

![upload successful](/images/pasted-175.png)

### 目标配置

另外值得称道的是Lambda除了提供了丰富的触发器资源，在函数执行结束后也提供了异常处理能力以及后续触发调用能力，让基于Lambda开发的应用更加健壮，也更加简单。

![upload successful](/images/pasted-176.png)

AWS还支持流式调用的映射，方便更实时的利用Lambda处理数据。

![upload successful](/images/pasted-180.png)

### 开发与调试

我在使用函数过程中，最大的感触就是函数计算的开发和调试是比较麻烦的，因为牵扯到各种云服务，所以在本地调试的时候会有很多限制，在线上调试又担心出现问题。AWS除了提供在线的编辑器外，CLI工具包括了AWS CLI和AWS SAM(AWS Serverless Application Model)。如果是开发函数计算，还是推荐SAM，毕竟是面向函数计算开发设计的。

### 日志、监控与权限控制

在实际使用过程中，函数计算追踪往往是初学者遇到的最大的挑战。其实用了这么久的云，在云原生服务关联性方面你是能真真切切感受到AWS的设计感的。函数计算也不例外，与IAM、日志以及CloudWatch监控服务都有比较良好的互动性，包括上面提到的CLI工具，底层也是调用了CloudFormation编排的能力实现的。所以Lambda的整个开发者生态还是非常完善和友好的。

## 发展趋势

AWS Lambda是函数计算的里程碑，也是目前为止生态最为完整的函数计算服务。由于Lambda与其他AWS服务的良好的互动性，所以往往在整个Serverless架构中，Lambda作为连接云原生服务之间的能力体现的更加淋漓尽致一些。特别是在一些最佳实践中，通过Lambda的合理利用，往往可以降低在云架构设计和开发的成本。从另外一个层面上讲，对Lambda的特性使用的越多，对AWS依赖就会越强，对用户形成一定的锁定性。
