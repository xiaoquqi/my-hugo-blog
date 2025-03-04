---
title: 'AWS Certified Solutions Architecture Associate Practice'
date: 2022-03-30 21:35:00
tags: [AWS, ACA Practice]
---

该模拟题出自AWS Practice，是付费后的模拟题，一共25道题，相对来说答案比较准确，答题正确率在76%，看中文的命题相对来说对理解题目内容更简单。

总得分: 76%
主题得分:
1.0. Design Resilient Architectures 89%
2.0. Define Performant Architectures 71%
3.0. Specify Secure Applications and Architectures 50%
4.0. Design Cost-Optimized Architectures 100%
5.0. Define Operationally Excellent Architectures 100%

个人感觉，对于网络题目还是有些晕的，因为和OpenStack的SDN还是有一些区别，特别涉及到安全组、网络ACL特别含糊；另外一类题就是服务之间的互联互通时会比较晕。

<!-- more -->

## (*)您在us-west-2中运行一个应用程序，它需要始终运行6个EC2实例。
该区域有三个可用区（us-west-2a，us-west-2b和us-west-2c)可以使用，如果us-west-2中的任何可用区变得不可用，以下哪种部署可以提供容错功能？（选择两顶◊)
A. 在us-west-2a中有2个EC2实例，在us-west-2b中有2个EC2实例，在us-west-2c中有2个EC2实例
B. 在 us- west- 2 a中有3个 EC2实例，在us-west-2b中有3个 EC2实例，在us-west-2c中没有EC2实例
C. 在us-west-2a中有4个 EC2实例，在us-west-2b中有2个 EC2实例，在us-west-2c中有2个 EC2实例
D. 在 us- west- 2 a中有6个 EC2实例，在us-west-2b中有6个 EC2实例，在us-west-2c中没有EC2实例
E. 在us-west-2a中有3个 EC2实例，在us-west-2b中有3个 EC2实例，在us-west-2c中有3个 EC2实例

Answer: DE

该道题的重点是始终运行6个EC2实例，所以当一个区Down掉，仍然能保证有6台实例的答案为正确答案。

## 一家咨询公司反复使用来自很多AMS服务（包括IAM，Amazon EC2, Amazon RDS，DynamoDB和Amazon VPC)的AMS资源为客户构建大型标准化架构。顾问们有每个架构的架构图，但让他们感到沮丧的是，无法使用这些架构图自动创建资源。 哪种服务会立即为组织带来好处?
A. Elastic Beanstalk
B. CloudFormation
C. AMS CodeBuild
D. AMS CodeDeploy

Answer: B

## 解决方案架构师正在设计一种解决方案以存储和存档公司文档，并确定Amazon Glacier是正确的解决方案。必须在发出检索请求后的10分钟内提供数据。
Amazon Glacier中的哪种功能可以帮助满足该要求？
A. 文件库锁定
B. 加速检索
c. 批量检索
D. 标准检索

Answer: B

> 问：如何从该服务检索数据？
> 
> 当您请求从 S3 Glacier 检索数据时，即表示您启动了一个存档检索作业。当检索作业完成后，您的数据将在 24 小时内可供下载或通过 Amazon Elastic Compute Cloud (Amazon EC2) 访问。有三种方式可以检索数据，每种具有不同的访问时间和成本：加急、标准和批量检索。
> 
> 问：什么是加急检索？
> 
> 当您偶尔需要加急请求档案子集时，可以使用加急检索来快速访问您的数据。除了最大的存档 (250MB+) 以外，对于使用加急检索方式访问的所有数据，通常在 1-5 分钟内即可使用。有两种加急检索：按需和预置。当我们可以在 1-5 分钟内完成检索时，就可以实施按需检索。所提供的请求将确保在您需要时能够获得加急检索的能力。

## (*)一个组织的安全策略要求应用程序在写入到磁盘之前加密数据。
该组织应使用哪种解决方案以满足该要求？
A. AMS KMS API
B. AMS Certificate Manager
C. 具有 STS 的 API Gateway
D. IAM访问密钥

Answer: A

> 问：什么是 Amazon EBS 加密？
> 
> Amazon EBS 加密提供 EBS 数据卷、引导卷和快照的无缝加密，无需构建和维护安全密钥管理基础设施。EBS 加密可使用 Amazon 托管的密钥或您使用 AWS Key Management Service (KMS) 创建和管理的密钥来给您的数据加密，从而保障静态数据的安全性。加密还发生在托管 EC2 实例的服务器上，当数据在 EC2 实例和 EBS 存储之间移动时提供数据加密。有关详细信息，请参阅 Amazon EC2 用户指南中的“Amazon EBS”加密。
> 
> 问：什么是 AWS Key Management Service (KMS)？
> 
> AWS KMS 是一项托管服务，可让您轻松创建和控制加密数据所用的加密密钥。AWS Key Management Service 可与其他 AWS 服务集成，包括 Amazon EBS、Amazon S3 和 Amazon Redshift，可让您轻松使用您管理的加密密钥加密您的数据。AWS Key Management Service 还能与 AWS CloudTrail 集成，从而为您提供所有密钥的使用记录，帮助您满足监管和合规性要求。要了解有关 KMS 的更多信息，请访问 AWS Key Management Service 产品页面。
> 
## (*)一家零售商每天将其交易数据库中的数据导出到S3存储捅中。该零售商的数据仓库团队希望将这些数据导入到VPC中的现有Amazon Redshift群集◊公司安全策略规定只能在VPC中传输这些数据。
以下哪种步骤组合满足安全策略要求？（选择两顶)
A. 启用 Amazon Redshift 增强 VPC 路由。
B. 创建集群安全组以允许Amazon Redshift集群访问Amazon S3
C. 在公有子网中创建NAT网关以允许Amazon Redshift集群访问Amazon S3
D. 创建并配置Amazon S3 VPC终端节点
E. 在私有子网中设置NAT网关以允许Amazon Redshift集群访问AmazonS3

Answer: AD

> https://docs.aws.amazon.com/zh_cn/redshift/latest/mgmt/enhanced-vpc-working-with-endpoints.html
> 
> 使用 VPC 终端节点
> 可以使用 VPC 终端节点创建 VPC 中的 Amazon Redshift 集群与 Amazon Simple Storage Service (Amazon S3) 之间的托管连接。在执行此操作时，您的集群与 Amazon S3 数据之间的 COPY 和 UNLOAD 流量将保留在您的 Amazon VPC 中。可以将终端节点策略附加到您的终端节点，以便更严格地管理对数据的访问。例如，可以向 VPC 终端节点添加策略以仅允许将数据上传到您账户中的特定 Amazon S3 存储桶。
> 
> 重要
> 目前，Amazon Redshift 仅支持连接到 Amazon S3 的 VPC 终端节点。当 Amazon VPC 添加对其他 AWS 服务的支持以使用 VPC 终端节点时，Amazon Redshift 也将支持这些 VPC 终端节点连接。要使用 VPC 终端节点连接到 Amazon S3 存储桶，Amazon Redshift 集群与其连接到的 Amazon S3 存储桶必须在同一个 AWS 区域中。
> 
> 要使用 VPC 终端节点，请为集群所在的 VPC 创建 VPC 终端节点，然后为集群启用增强型 VPC 路由。可以在 VPC 中创建集群时启用增强型 VPC 路由，也可以修改 VPC 中的集群以使用增强型 VPC 路由。
> 
> VPC 终端节点使用路由表来控制 VPC 中的集群和 Amazon S3 之间的流量路由。与指定路由表关联的子网中的所有集群会自动使用该终端节点来访问服务。
> 
> 您的 VPC 使用与集群流量匹配的最具体的/最严格的路由来决定路由流量的方式。例如，假设路由表中有一条路由用于所有指向 Internet 网关和 Amazon S3 终端节点的 Internet 流量 (0.0.0.0/0)。在这种情况下，对所有传送到 Amazon S3 的流量优先使用终端节点路由。这是因为 Amazon S3 服务的 IP 地址范围比 0.0.0.0/0 更具体。在此示例中，所有其他 Internet 流量（包括定位到其他 AWS 区域内的 Amazon S3 存储桶的流量）将流向 Internet 网关。
> 
> 有关创建终端节点的更多信息，请参阅 Amazon VPC 用户指南 中的 VPC 终端节点。
> 
> 您使用终端节点策略控制从集群到包含数据文件的 Amazon S3 存储桶的访问。默认情况下，创建终端节点向导会附加一个终端节点策略，该策略不会进一步限制来自 VPC 中的任何用户或服务的访问。要实现更具体的控制，您可以选择附加一个自定义终端节点策略。有关更多信息，请参阅 Amazon VPC 用户指南 中的使用终端节点策略。
> 
> 使用终端节点不收取任何额外费用。采用标准的数据传输和资源使用计费方式。有关定价的更多信息，请参阅 Amazon EC2 定价。

> https://docs.amazonaws.cn/redshift/latest/mgmt/enhanced-vpc-routing.html
>
> Amazon Redshift 增强型 VPC 路由
>
> 在使用 Amazon Redshift 增强型 VPC 路由时，Amazon Redshift 会强制通过您的 Amazon VPC 路由集群和数据存储库之间的所有 COPY 和 UNLOAD 流量。通过使用增强型 VPC 路由，您可以使用标准 VPC 功能，例如 VPC 安全组、网络访问控制列表 (ACL)、VPC 终端节点、VPC 终端节点策略、Internet 网关和域名系统 (DNS) 服务器，如 Amazon VPC 用户指南 中所述。 您可以使用这些功能来严格管理 Amazon Redshift 集群与其他资源之间的数据流。在使用增强型 VPC 路由通过您的 VPC 路由流量时，也可以使用 VPC 流日志来监视 COPY 和 UNLOAD 流量。
> 
> 如果未启用增强型 VPC 路由，则 Amazon Redshift 会通过 Internet 路由流量，包括至 AWS 网络中的其他服务的流量。
> 
> 重要
> 由于增强型 VPC 路由影响了 Amazon Redshift 访问其他资源的方式，因此，除非您正确配置 VPC，否则 COPY 和 UNLOAD 命令可能会失败。您必须专门在集群的 VPC 和数据资源之间创建网络路径，如下所述。
> 
> 在对已启用增强型 VPC 路由的集群执行 COPY 或 UNLOAD 命令时，您的 VPC 会使用最严格 或最具体的可用网络路径来将流量路由到指定资源。

## 一家公司正在生成包含数百万行的大型数据集，必须能按列对这些数据集进行汇总◊将使用现有的商业智能工具生成日常报告。
哪种存储服务可满足这些要求？
A. Amazon Redshift
B. Amazon RDS
C. ElastiCache
D. DynamoDB

Answer: A

## 解决方案架构师正在设计一个活动注册网页；每次用户注册活动时，需要使用一个托管服务向用户发送文本消息。
架构师应使用哪种AWS服务来实现该目的？
A. Amazon STS
B. Amazon SQS
C. Lambda
D. Amazon SNS

Answer: D

> Amazon Simple Notification Service (SNS) 是一种高度可用、持久、安全、完全托管的发布/订阅消息收发服务，可以轻松分离微服务、分布式系统和无服务器应用程序。Amazon SNS 提供了面向高吞吐量、多对多推送式消息收发的主题。借助 Amazon SNS 主题，发布系统可以向大量订阅终端节点（包括 Amazon SQS 队列、AWS Lambda 函数和 HTTP/S Webhook 等）扇出消息，从而实现并行处理。此外，SNS 可用于使用移动推送、短信和电子邮件向最终用户扇出通知。

## (*)解决方案架构师正在设计一个共享服务，以便在Amazon ECS上托管来自很多客户的容器。这些容器将使用很多AWS服务。一个客户的容器无法访问其他客户的数据。
架构师应使用哪种解决方案以满足这些要求？
A. 任务的IAM角色
B. EC2实例的 IAM角色
C. EC2实例的 IAM实例配置文件
D. 安全组规则

Answer: A

> https://docs.aws.amazon.com/zh_cn/AmazonECS/latest/developerguide/task-iam-roles.html
>
> 借助 Amazon ECS 任务的 IAM 角色，您可以指定一个可由任务中的容器使用的 IAM 角色。应用程序必须使用 AWS 凭证签署其 AWS API 请求，并且此功能提供了一个管理凭证的策略以供应用程序使用，类似于 Amazon EC2 实例配置文件为 EC2 实例提供凭证的方式。您可以将 IAM 角色与 ECS 任务定义或 RunTask API 操作关联，而不是为容器创建和分配 AWS 凭证或使用 EC2 实例的角色。之后，任务的容器中的应用程序可以使用 AWS 开发工具包或 CLI 向授权的 AWS 服务发出 API 请求。

## 一家公司正在将本地10 TB MySQL数据库迁移到AWS，该公司预计数据库大小将增加3倍，业务要求是副本的滯后时间必须保持在100毫秒以内。
哪种Amazon RDS引擎满足这些要求？
A. MySQL
B. Microsoft SQL Server
C. Oracle
D. Amazon Aurora

Answer: D

> https://amazonaws-china.com/cn/rds/aurora/faqs/?nc=sn&loc=6
>
> Amazon Aurora 副本复制是毫秒级别，而MySQL是秒级别

## 管理员在AWS中运行一个高可用应用程序。管理员需要使用一个文件存储层，它可以在实例之间共享并能更轻松地扩展该应用平台。
哪种AMS服务可以执行该操作？
A. Amazon EBS
B. Amazon EFS
C. Amazon S3
D. Amazon EC2实例存储

Answer: B

## 一家公司托管一个流行的Web应用程序，它连接到在私有VPC子网中运行的Amazon RDS MySQL数据库实例，该子网是使用默认ACL设置创建的。仅允许使用SSL连接的客户访问Web服务器◊仅公有子网中的Web服务器可以访问该数据库。
哪种解决方案可满足这些要求而不会影响其他运行的应用程序？（选择两顶)
A. 在Web服务器的子网上创建一个网络ACL，允许HTTPS端口 443入站流量，并将源指定为0.0.0.0/0。
B. 创建一个允许来自Anywhere (0.0.0.0/0)的 HTTPS端口 443入站流量的Web服务器安全组，并将其应用于Web服务器。
C. 创建一个允许MySQL端口 3306入站流量的数据库服务器安全组，并将源指定为一个Web服务器安全组。
D. 在数据库子网上创建一个网络ACL，允许Web服务器的MySQL端口 3306入站流量，并拒绝所有出站流量。
E. 创建一个允许HTTPS端口 443入站流量的数据库服务器安全组，并将源指定为一个Web服务器安全组。

Answer: BC

## 一个应用程序当前在Amazon EBS卷上存储所有数据。必须在多个可用区中永久备份所有EBS卷。
备份这些卷的最灵活方法是什么？
A. 定期创建EBS快照。
B. 启用EBS卷加密。
C. 创建脚本以将数据复制到EC2实例存储。
D. 在两个EBS卷之间镜像数据。

Answer: A

## 解决方案架构师正在开发一个文档共享应用程序，并需要使用一个存储层。该存储应提供自动版本控制支持，以便用户可以轻松回滚到以前的版本或恢复删除的文档。
哪种AMS服务可满足这些要求？
A. Amazon S3
B. Amazon EBS
C. Amazon EFS
D. Amazon Storage Gateway VTL

Answer: A

## AWS中的一个数据处理应用程序必须从Internet服务中提取数据。解决方案架构师必须设计一种高可用解决方案以访问数据，并且不会对应用程序流量施加带宽限制。
哪种解决方案能满足这些要求？
A. 启动一个NAT网关并为0.0.0.0/0添加路由
B. 附加一个VPC终端节点并为0.0.0.0/0添加路由
C. 附加一个Internet网关并为0.0.0.0/0添加路由
D. 在公有子网中部署NAT实例并为0.0.0.0/0添加路由

Answer: C

> https://docs.aws.amazon.com/zh_cn/vpc/latest/userguide/VPC_Internet_Gateway.html
>
> Internet 网关是一种横向扩展、支持冗余且高度可用的 VPC 组件，可实现 VPC 中的实例与 Internet 之间的通信。因此它不会对网络流量造成可用性风险或带宽限制。
>
> NAT 网关
> 您可以使用网络地址转换 (NAT) 网关允许私有子网中的实例连接到 Internet 或其他 AWS 服务，但阻止 Internet 发起与这些实例的连接。有关 NAT 的更多信息，请参阅NAT。
> 您在账户中创建和使用 NAT 网关会产生费用。NAT 网关小时使用费率和数据处理费率适用于此。Amazon EC2 数据传输费同样适用。有关更多信息，请参阅 Amazon VPC 定价。

## (待确认)在审查您的应用程序的Auto Scaling事件时，您注意到应用程序在同一小时内扩展和缩减多次。
您可以选择哪种设计选顶以在保持弹性的同时优化成本？（选择两顶)
A. 修改Auto Scaling组终止策略以先终止最老的实例。
B. 修改Auto Scaling组终止策略以先终止最新的实例。
C. 修改Auto Scaling组冷却计时器。
D. 修改Auto Scaling策略以使用计划的缩放操作。
E. 修改触发Auto Scaling缩减策略的CloudWatch警报周期。

Answer: BC

这道题目前纠结点在于AB两个选项，从文档中可知有一种策略结束类型叫ClosestToNextInstanceHour类型更适合该题目。如果从这个角度说，新的实例好像更靠近最近计费时间点这个选项。

## 对于以下哪种工作负载，解决方案架构师应考虑使用Elastic Beanstalk?(选择两顶)
A. 使用Amazon RDS的Web应用程序
B. 企业数据仓库
C. 长时间运行的工作进程
D. 静态网站
E. 每晚运行一次的管理任务

Answer: AD

## 一家公司在AMS上运行一个服务，以便为笔记本电脑和手机上的图像提供异地备份。该解决方案必须支持数百万个客户，每个客户有数千张图像，很少会检索这些图像，但必须可以立即检索这些图像。
哪种是满足这些要求的最经济高效的存储选顶？
A. 具有加速检索的Amazon Glacier
B. Amazon S3标准-低频率访问
C. Amazon EFS
D. Amazon S3 标准

Answer: B

## 一个带有150 GB大小的关系数据库的应用程序在EC2实例上运行。该应用程序很少使用，但在早上和晚上会出现很小的高峰。
最经济高效的存储类型是什么？
A. Amazon EBS 预置 IOPS SSD
B. Amazon EBS吞吐量优化HDD
C. Amazon EBS 通用型 SSD
D. Amazon EFS

Answer: C

## 一个应用程序允许生产站点上传文件。然后，处理每个3 GB大小的文件以提取元数据，处理每个文件需要几秒钟的时间◊更新频率是无法预铡的-可能几小时内没有更新，然后同时上传几个文件。
哪种架构能以最经济高效的方式处理该工作负载？
A. 使用Kinesis数据传输流存储文件，并使用Uirtoda进行处理。
B. 使用SQS队列存储文件，然后，一组EC2实例访问该文件。
C. 将文件存储在EBS卷中，然后，其他EC2实例可以访问该文件以进行处理。
D. 将文件存储在S3存储捅中，并使用Amazon S3事件通知调用Lambda函数以处理该文件。

Answer: D

## 一家网站在ELB应用程序负载均衡器后面的多个EC2实例上运行。这些实例在跨多个可用区的Auto Scaling组中运行◊这些实例提供一些很大的文件（图像，PDF等)，这些文件存储在共享的Amazon EFS文件系统上。每次用户请求这些数字资产时，该公司需要避免从EC2实例中提供这些文件。
该公司应釆取哪些措施以改进网站的用户体验？
A. 将数字资产移到到Amazon Glacier中。
B. 使用CloudFront缓存静态内容。
C. 调整图像以使其变小。
D. 使用保留的EC2实例。

Answer: B

## 您正在Amazon EC2上部署一个应用程序，它必须调用AMS API。
应使用哪种方法可将凭证安全地传送到该应用程序？
A. 使用实例用户数据将API凭证传送到实例。
B. 将API凭证作为对象存储在Amazon S3中。
C. 将API凭证嵌入到JAR文件中。
D. 将IAM角色分配给EC2实例。

Answer: D

## 一个组织在AWS上托管着一个多语言网站◊该网站是使用CloudFront提供服务的◊语言是在HTTP请求中指定的:
• http://dllllllabcdef8.cloudfront.net/main.html?language=de
• http://dllllllabcdef8.cloudfront.net/main.html?language=en
• http://dllllllabcdef8.cloudfront.net/main.html?language=es
应如何配置CloudFront以使用正确的语言提供缓存的数据？
A. 将Cookie转发到原始地址。
B. 基于查询字符串参数。
C. 在原始地址中缓存对象。
D. 提供动态内容。

Answer: B

> https://docs.aws.amazon.com/zh_cn/AmazonCloudFront/latest/DeveloperGuide/QueryStringParameters.html
>
> 一些 Web 应用程序使用查询字符串将信息发送到源。查询字符串是 Web 请求的一部分，显示在 ? 字符之后；该字符串可以包含一个或多个使用 & 字符分隔的参数。在以下示例中，查询字符串包括两个参数 color=red 和 size=large：

## 解决方案架构师正在设计一个可高度扩展的系统以跟踪记录。记录必须保留三个月以便可立即下载，然后必须删除记录。
最适合该使用案例的决策是什么？
A. 将文件存储在Amazon EBS上，并创建一个生命周期策略以在三个月后删除这些文件。
B. 将文件存储在Amazon S3中，并创建一个生命周期策略以在三个月后删除这些文件。
C. 将文件存储在Amazon Glacier中，并创建一个生命周期策略以在三个月后删除这些文件。
D. 将文件存储在Amazon EFS上，并创建一个生命周期策略以在三个月后删除这些文件。

Answer: B

## 一个团队正在创建一个应用程序，它必须在高可用的数据存储中永久保存JSON文件并编制索引。尽管应用程序流量很高，但数据访问延迟必须保持一致。
该团队应该选择哪种服务？
A. Amazon EFS
B. Amazon RedShift
C. DynamoDB
D. AWS CloudFormation

Answer: C

## (*)一个应用程序在S3存储桶中读取和写入小对象。在完全部署该应用程序后，读取/写入流量会非常高。
架构师应如何最大限度地提高Amazon S3性能？
A. 在每个对象名称前面添加随机字符串。
B. 使用STANDARD_IA存储类
C. 在每个对象名称前面添加当前日期。
D. 在S3存储桶上启用版本控制。

Answer: C

> https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/optimizing-performance.html
>
> 当从 Amazon S3 上传和检索存储时，您的应用程序可以轻松地实现每秒数千个事务的请求性能。Amazon S3 会自动扩展至高请求速率。例如，您的应用程序可以在存储桶中实现至少每秒每个前缀 3,500 个 PUT/COPY/POST/DELETE 请求和 5,500 个 GET/HEAD 请求。对存储桶中的前缀数量没有限制。您可以通过并行读取来增加读取或写入性能。例如，如果您在 Amazon S3 存储桶中创建 10 个前缀以并行处理读取，则可以将读取性能扩展到每秒 55,000 个读取请求。
> 下面的主题介绍的最佳实践准则和设计模式用于优化使用 Amazon S3 的应用程序的性能。本指南的优先级高于之前有关优化 Amazon S3 的性能的任何指南。例如，以前的 Amazon S3 性能指南建议用哈希字符来随机化前缀命名，以便优化频繁数据检索的性能。现在，您不再需要为了提高性能随机化前缀命名，而是可以对前缀使用基于顺序日期的命名方式。有关对 Amazon S3 进行性能优化的最新信息，请参阅Amazon S3 的性能准则和Amazon S3 的性能设计模式。

> 2018年7月17日 Amazon S3 宣布提高请求速率性能(https://amazonaws-china.com/cn/about-aws/whats-new/2018/07/amazon-s3-announces-increased-request-rate-performance/)
> 
> Amazon S3 现在提供了更高的性能，支持每秒至少 3500 个数据添加请求、每秒 5500 个数据检索请求，而且无需额外费用，这可以节省大量处理时间。每个 S3 前缀均支持这些请求速率，因此可以轻松实现显著的性能提升。
>
> 目前在 Amazon S3 上运行的应用程序均可享受此性能改进，而无需实施任何更改；在 S3 上构建新应用程序的客户无需进行任何应用程序自定义即可享受此性能。Amazon S3 对并行请求的支持意味着您可以按照计算集群的系数扩展 S3 性能，而无需对应用程序进行任何自定义。性能按前缀扩展，因此您可以并行使用尽可能多的前缀，从而实现所需的吞吐量。前缀的数量没有限制。
>
> 在这种 S3 请求速率性能提升推出后，先前任何为加速性能而随机化对象前缀的指南均被淘汰。也就是说，您现在可以在 S3 对象命名中使用逻辑或顺序命名模式，而不会产生任何性能影响。所有 AWS 区域现在均已提供此改进。有关更多信息，请访问 Amazon S3 开发人员指南。