---
title: AWS Certified Solutions Architect - Associate Exam(Q1-Q100)
date: 2022-03-31 09:11:55
tags: [AWS, ACA Exam]
---

参考链接：https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-associate/view/

一直对AWS情有独钟，也想尝试考取最高认证，但是苦于无法集中精力学习。2019年由于和AWS合作的原因，所以痛下决心一定要考取AWS各种认证。另外，在AWS的学习过程中，也逐渐帮我梳理了以前在OpenStack开发过程中不是很清晰的设计理念。并且AWS的文档和最佳实践堪称各个公有云的典范，非常具有学习价值。考试不是最终的目的，学以致用才是。

由于备考AWS ACA考试，所以从网上看到这套模拟试题，在学习过程中对试题进行系统性分析和记录。发现有很多问题答案并非十分准确，所以也尝试做出分析和更正。

<!-- more -->

## A Solutions Architect is designing an application that will encrypt all data in an Amazon Redshift cluster. Which action will encrypt the data at rest?

A. Place the Redshift cluster in a private subnet.
B. Use the AWS KMS Default Customer master key.
C. Encrypt the Amazon EBS volumes.
D. Encrypt the data using SSL/TLS.

Answer: B

* 参考链接：https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html
* 分析：Amazon Redshift 使用加密密钥层次结构来加密数据库。您可以使用 AWS Key Management Service (AWS KMS) 或硬件安全模块 (HSM) 来管理该层次结构中的顶级加密密钥。Amazon Redshift 用于加密的流程因您管理密钥的方式而异。Amazon Redshift 自动与 AWS KMS 集成，而不与 HSM 集成。当您使用 HSM 时，必须使用客户端和服务器证书在 Amazon Redshift 和 HSM 之间配置受信任的连接。

## A website experiences unpredictable traffic. During peak traffic times, the database is unable to keep up with the write request. Which AWS service will help decouple the web application from the database?

A. Amazon SQS
B. Amazon EFS
C. Amazon S3
D. AWS Lambda

Answer: A

* 参考链接：https://aws.amazon.com/cn/sqs/faqs/
* 分析：关键词是unpredictable traffic, keep up with write request, decouple the web application, 所以通过消息队列服务可以让写入请求排队，从而实现前端应用和后端数据库的解耦。

## A legacy application needs to interact with local storage using iSCSI. A team needs to design a reliable storage solution to provision all new storage on AWS. Which storage solution meets the legacy application requirements?

A. AWS Snowball storage for the legacy application until the application can be re-architected.
B. AWS Storage Gateway in cached mode for the legacy application storage to write data to Amazon S3.
C. AWS Storage Gateway in stored mode for the legacy application storage to write data to Amazon S3.
D. An Amazon S3 volume mounted on the legacy application server locally using the File Gateway service.

Answer: C

* 分析：关键词是local stroage with iSCSI, 并且需要将所有新的存储用AWS提供，所以排除A选项；因为用到了iSCSI协议，所以S3使用文件网关方式也不适用，排除D；剩下的B和C区别在于存储模式，因为需要本地应用请求，所以需要使用存储模式，而不能用缓存模式，所以最终选择C。

## A Solutions Architect is designing an architecture for a mobile gaming application. The application is expected to be very popular. The Architect needs to prevent the Amazon RDS MySQL database from becoming a bottleneck due to frequently accessed queries. Which service or feature should the Architect add to prevent a bottleneck?

A. Multi-AZ feature on the RDS MySQL Database
B. ELB Classic Load Balancer in front of the web application tier
C. Amazon SQS in front of RDS MySQL Database
D. Amazon ElastiCache in front of the RDS MySQL Database

Answer: D

* 分析：该问题的关键在于bottleneck due to frequently accessed queries，查询变成瓶颈，可以使用ElastiCache服务作为缓存，降低读取频率解决问题。

## A company is launching an application that it expects to be very popular. The company needs a database that can scale with the rest of the application. The schema will change frequently. The application cannot afford any downtime for database changes. Which AWS service allows the company to achieve these objectives?

A. Amazon Redshift
B. Amazon DynamoDB
C. Amazon RDS MySQL
D. Amazon Aurora

Answer: B

* 分析：原网站给出的答案是A，但是经过分析觉得有些问题，这道题的几个关键词：scale with the rest of the application, schema will change frequently, cannot afford any downtime for database changes. 首先，schema总是变更，所以这里需要的非关系型数据库，排除C和D。Redshift是数据仓库，其实也是数据仓库，从第一点上就可以排除。另外从这个链接（http://braindump2go.hatenablog.com/entry/2019/11/05/123057）分析上，还有一点除了DynamoDB可以真正做到scale时候zero downtime，其他的都不行。所以原网站给出的答案是错误的。

## A Solution Architect is designing a disaster recovery solution for a 5 TB Amazon Redshift cluster. The recovery site must be at least 500 miles (805 kilometers) from the live site. How should the Architect meet these requirements?

A. Use AWS CloudFormation to deploy the cluster in a second region.
B. Take a snapshot of the cluster and copy it to another Availability Zone.
C. Modify the Redshift cluster to span two regions.
D. Enable cross-region snapshots to a different region.

Answer: D

* 参考链接：https://aws.amazon.com/cn/blogs/aws/automated-cross-region-snapshot-copy-for-amazon-redshift/

## A customer has written an application that uses Amazon S3 exclusively as a data store. The application works well until the customer increases the rate at which the application is updating information. The customer now reports that outdated data occasionally appears when the application accesses objects in Amazon S3. What could be the problem, given that the application logic is otherwise correct?

A. The application is reading parts of objects from Amazon S3 using a range header.
B. The application is reading objects from Amazon S3 using parallel object requests.
C. The application is updating records by writing new objects with unique keys.
D. The application is updating records by overwriting existing objects with the same keys.

Answer: D

* 分析：这道题也是争论很大的一道题，原网站答案为A。问题简单描述为客户端访问不到最新的数据，发生的时间点在于应用上传信息时候速率提高导致的，所以问题应该出现在写入的时候，这样排除A和B读取的问题。因为S3同一object永远是覆盖，所以最有可能的问题是在same key的情况下，所以选择D。

## A Solutions Architect is designing a new social media application. The application must provide a secure method for uploading profile photos. Each user should be able to upload a profile photo into a shared storage location for one week after their profile is created. Which approach will meet all of these requirements?

A. Use Amazon Kinesis with AWS CloudTrail for auditing the specific times when profile photos are uploaded.
B. Use Amazon EBS volumes with IAM policies restricting user access to specific time periods.
C. Use Amazon S3 with the default private access policy and generate pre-signed URLs each time a new site profile is created.
D. Use Amazon CloudFront with AWS CloudTrail for auditing the specific times when profile photos are uploaded.

Answer: C

## An application requires block storage for file updates. The data is 500 GB and must continuously sustain 100 MiB/s of aggregate read/write operations. Which storage option is appropriate for this application?

A. Amazon S3
B. Amazon EFS
C. Amazon EBS
D. Amazon Glacier

Answer: C

* 分析：没想到这道题原网站给出的答案是B，争议比较大，但是从题目描述需要Block Storage角度来看，选择C才是最合理的。这道题还需要进一步确认一下。

## A mobile application serves scientific articles from individual files in an Amazon S3 bucket. Articles older than 30 days are rarely read. Articles older than 60 days no longer need to be available through the application, but the application owner would like to keep them for historical purposes. Which cost-effective solution BEST meets these requirements?

A. Create a Lambda function to move files older than 30 days to Amazon EBS and move files older than 60 days to Amazon Glacier.
B. Create a Lambda function to move files older than 30 days to Amazon Glacier and move files older than 60 days to Amazon EBS.
C. Create lifecycle rules to move files older than 30 days to Amazon S3 Standard Infrequent Access and move files older than 60 days to Amazon Glacier.
D. Create lifecycle rules to move files older than 30 days to Amazon Glacier and move files older than 60 days to Amazon S3 Standard Infrequent Access.

Answer: C

* 分析：很明显的排除A和B，S3可以自定义规则，那么问题就是30天后和60天后需要哪种存储的问题了，根据题目C是明显正确的。

## An organization is currently hosting a large amount of frequently accessed data consisting of key-value pairs and semi-structured documents in their data center. They are planning to move this data to AWS. Which of one of the following services MOST effectively meets their needs?

A. Amazon Redshift
B. Amazon RDS
C. Amazon DynamoDB
D. Amazon Aurora

Answer: C

## A Lambda function must execute a query against an Amazon RDS database in a private subnet. Which steps are required to allow the Lambda function to access the Amazon RDS database? (Select two.)

A. Create a VPC Endpoint for Amazon RDS.
B. Create the Lambda function within the Amazon RDS VPC.
C. Change the ingress rules of Lambda security group, allowing the Amazon RDS security group.
D. Change the ingress rules of the Amazon RDS security group, allowing the Lambda security group.
E. Add an Internet Gateway (IGW) to the VPC, route the private subnet to the IGW.

Answer: BD

* 分析：又是原网站一道错题，原网站答案为AD。D选项是允许Lambda服务访问RDS，所以在进方向允许。
* 目前VPC支持Endpoint的服务：https://docs.aws.amazon.com/zh_cn/vpc/latest/userguide/vpc-endpoints.html

> Amazon API Gateway
> Amazon AppStream 2.0
> AWS App Mesh
> Amazon Athena
> AWS CloudFormation
> AWS CloudTrail
> Amazon CloudWatch
> Amazon CloudWatch Events
> Amazon CloudWatch Logs
> AWS CodeBuild
> AWS CodeCommit
> AWS CodePipeline
> AWS Config
> AWS DataSync
> Amazon EC2 API
> Elastic Load Balancing
> Amazon Elastic Container Registry
> Amazon Elastic Container Service
> AWS Glue
> AWS Key Management Service
> Amazon Kinesis Data Firehose
> Amazon Kinesis Data Streams
> Amazon Rekognition
> Amazon SageMaker 和 Amazon SageMaker 运行时
> Amazon SageMaker 笔记本
> AWS Secrets Manager
> AWS Security Token Service
> AWS Service Catalog
> Amazon SNS
> Amazon SQS
> AWS Systems Manager
> AWS Storage Gateway
> AWS Transfer for SFTP
> 其他 AWS 账户托管的终端节点服务
>
> 网关终端节点是一个网关，作为您在路由表中指定的路由的目标，用于发往受支持的 AWS 服务的流量。支持以下 AWS 服务：
> Amazon S3
> DynamoDB

## (待实际环境验证)A Solutions Architect needs to build a resilient data warehouse using Amazon Redshift. The Architect needs to rebuild the Redshift cluster in another region. Which approach can the Architect take to address this requirement?

A. Modify the Redshift cluster and configure cross-region snapshots to the other region.
B. Modify the Redshift cluster to take snapshots of the Amazon EBS volumes each day, sharing those snapshots with the other region.
C. Modify the Redshift cluster and configure the backup and specify the Amazon S3 bucket in the other region.
D. Modify the Redshift cluster to use AWS Snowball in export mode with data delivered to the other region.

Answer: A

* 分析：又是一道错题，Redhift备份是通过S3实现的, 所以不存在B的情况，我个人有点倾向于C，但是A确实是Redshift在快照时默认的格式，可能是更容易恢复吧，这道题需要在实际环境进行一下验证。另外国际版本的Redshift和国内的应该比国内的高很多。

> 问：Amazon Redshift 如何备份数据？ 如何从备份中还原我的集群？
>
> 在加载数据时，Amazon Redshift 会复制数据仓库集群内的所有数据并将其连续备份至 S3。Amazon Redshift 始终尝试维持至少三份数据（计算节点上的正本数据、副本数据和 Amazon S3 上的备份数据）。Redshift 还能将您的快照异步复制到另一个区域的 S3 中进行灾难恢复。
>
> 默认情况下，Amazon Redshift 以一天的保留期启用数据仓库群集的自动化备份。您可将其配置为 35 天之久。
>
> 免费备份存储受限于数据仓库群集中节点上的总存储大小，并仅适用于已激活的数据仓库群集。例如，如果您有 8TB 的数据仓库总存储大小，那么我们将提供最多 8TB 的备份存储而不另外收费。如果您想将备份保留期延长为超过一天，那么您可以使用 AWS 管理控制台或 Amazon Redshift API 来实现这一目的。有关自动快照的更多信息，请参阅《Amazon Redshift 管理指南》。Amazon Redshift 仅备份已更改的数据，因此大多数快照仅占用少量的免费备份存储。
>
> 如果您需要还原备份，则可以在备份保留期内访问所有自动备份。在您选择某个要还原的备份后，我们将预置一个新的数据仓库集群并将数据还原至此集群中。

## A popular e-commerce application runs on AWS. The application encounters performance issues. The database is unable to handle the amount of queries and load during peak times. The database is running on the RDS Aurora engine on the largest instance size available. What should an administrator do to improve performance?

A. Convert the database to Amazon Redshift.
B. Create a CloudFront distribution.
C. Convert the database to use EBS Provisioned IOPS.
D. Create one or more read replicas.

Answer: C

* 分析：这道题我最开始选择的是D，但是评论区的一种解释有一定的道理：这个网站应用类型为电商，原题中没有很清楚说明queris and load的压力有多大，很可能我们建立了read replicas只能临时性解决问题，并不是一劳永逸的方式。并且根据https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html

> 因此，所有 Aurora 副本均返回相同的查询结果数据，且副本滞后时间非常短 - 通常远远少于主实例写入更新后的 100 毫秒。副本滞后因数据库更改速率而异。也就是说，在对数据库执行大量写入操作期间，您可能发现副本滞后时间变长。

如果读副本在这个延时上，很可能对业务系统造成很大的影响。

## A Solutions Architect is designing the architecture for a new three-tier web-based e-commerce site that must be available 24/7. Requests are expected to range from 100 to 10,000 each minute. Usage can vary depending on time of day, holidays, and promotions. The design should be able to handle these volumes, with the ability to handle higher volumes if necessary. How should the Architect design the architecture to ensure the web tier is cost-optimized and can handle the expected traffic? (Select two.)

A. Launch Amazon EC2 instances in an Auto Scaling group behind an ELB.
B. Store all static files in a multi-AZ Amazon Aurora database.
C. Create an CloudFront distribution pointing to static content in Amazon S3.
D. Use Amazon Route 53 to route traffic to the correct region.
E. Use Amazon S3 multi-part uploads to improve upload times.

Answer: AC

* 分析：A是很明显的，弹性伸缩，节约成本，其他几项和题干没有太多关系，所以选的C。

## A Solution Architect is designing a three-tier web application. The Architect wants to restrict access to the database tier to accept traffic from the application servers only. However, these application servers are in an Auto Scaling group and may vary in quantity. How should the Architect configure the database servers to meet the requirements?

A. Configure the database security group to allow database traffic from the application server IP addresses.
B. Configure the database security group to allow database traffic from the application server security group.
C. Configure the database subnet network ACL to deny all inbound non-database traffic from the application-tier subnet.
D. Configure the database subnet network ACL to allow inbound database traffic from the application-tier subnet.

Answer: B

* 分析：这好像又是一道错题，原给出的答案是C。首先要明确的一点是SG是工作在instance级别，NACL是在子网级别，SG默认全部Deny，NACL默认全部Allow。A不对的原因是insance在Auto Scaling里，IP地址是不固定的。D不对的原因是NACL默认全都是Allow的。其实本质上考察的是如何选择安全组还是网络防火墙的问题。不选择C的原因是因为配置NACL规则至少需要阻止和允许，而通过安全组只需要配置一条即可。但是也有一种声音认为题目中关键词restrict意味着需要deny流量。

> 问：VPC 中的安全组和 VPC 中的网络 ACL 有什么区别？
>
> VPC 中的安全组指定允许传入或传出 Amazon EC2 实例的流量。网络 ACL 则在子网级别上运作，评估进出某个子网的流量。网络 ACL 可通过设置允许和拒绝规则来进行使用。Network ACL 不能筛选同一子网中实例之间的流量。此外，网络 ACL 执行无状态筛选，而安全组则执行有状态筛选。

## An Internet-facing multi-tier web application must be highly available. An ELB Classic Load Balancer is deployed in front of the web tier. Amazon EC2 instances at the web application tier are deployed evenly across two Availability Zones. The database is deployed using RDS Multi-AZ. A NAT instance is launched for Amazon EC2 instances and database resources to access the Internet. These instances are not assigned with public IP addresses. Which component poses a potential single point of failure in this architecture?

A. Amazon EC2
B. NAT instance
C. ELB Classic Load Balancer
D. Amazon RDS

Answer: B

* 分析：这道题竟然给出了C的答案，很意外。

> https://aws.amazon.com/articles/high-availability-for-amazon-vpc-nat-instances-an-example/
>
> Instances in a private subnet can access the Internet without exposing their private IP address by routing their traffic through a Network Address Translation (NAT) instance in a public subnet. A NAT instance, however, can introduce a single point of failure to your VPC's outbound traffic. This situation is depicted in the diagram below.

## A call center application consists of a three-tier application using Auto Scaling groups to automatically scale resources as needed. Users report that every morning at 9:00 AM the system becomes very slow for about 15 minutes. A Solution Architect determines that a large percentage of the call center staff starts work at 9:00 AM, so Auto Scaling does not have enough time to scale out to meet demand. How can the Architect fix the problem?

A. Change the Auto Scaling group's scale out event to scale based on network utilization.
B. Create an Auto Scaling scheduled action to scale out the necessary resources at 8:30 AM every morning.
C. Use Reserved Instances to ensure the system has reserved the right amount of capacity for the scale-up events.
D. Permanently keep a steady state of instances that is needed at 9:00 AM to guarantee available resources, but leverage Spot Instances.

Answer: B

* 分析：竟然又是一道错题，记得在AWS听过这道题的分析。原答案是A，但是可能并不是由于网络引起的访问缓慢。

## An e-commerce application is hosted in AWS. The last time a new product was launched, the application experienced a performance issue due to an enormous spike in traffic. Management decided that capacity must be doubled the week after the product is launched. Which is the MOST efficient way for management to ensure that capacity requirements are met?

A. Add a Step Scaling policy.
B. Add a Dynamic Scaling policy.
C. Add a Scheduled Scaling action.
D. Add Amazon EC2 Spot Instances.

Answer: B

* 分析：又是一道争议比较大的题目，争议最大的是C选项，因为题目中有几个词在暗示时间，但是又不明确。既然现有性能上无法应对高峰访问，那么从这个角度还是通过Dynamic配置一个规则进行动态规则最为有效。所以还是选择B。

## A customer owns a simple API for their website that receives about 1,000 requests each day and has an average response time of 50 ms. It is currently hosted on one c4.large instance. Which changes to the architecture will provide high availability at the LOWEST cost?

A. Create an Auto Scaling group with a minimum of one instance and a maximum of two instances, then use an Application Load Balancer to balance the traffic.
B. Recreate the API using Amazon API Gateway and use AWS Lambda as the service backend.
C. Create an Auto Scaling group with a maximum of two instances, then use an Application Load Balancer to balance the traffic.
D. Recreate the API using Amazon API Gateway and integrate the new API with the existing backend service.

Answer: A

* 分析：这道题有个陷阱，Simple API，确实如果在不考虑开发的前提下B确实是最佳选项，但是重构也是要花成本的。所以我坚持选A。

## A Solution Architect is designing an application that uses Amazon EBS volumes. The volumes must be backed up to a different region. How should the Architect meet this requirement?

A. Create EBS snapshots directly from one region to another.
B. Move the data to an Amazon S3 bucket and enable cross-region replication.
C. Create EBS snapshots and then copy them to the desired region.
D. Use a script to copy data from the current Amazon EBS volume to the destination Amazon EBS volume.

Answer: C

## A company is using an Amazon S3 bucket located in us-west-2 to serve videos to their customers. Their customers are located all around the world and the videos are requested a lot during peak hours. Customers in Europe complain about experiencing slow downloaded speeds, and during peak hours, customers in all locations report experiencing HTTP 500 errors. What can a Solutions Architect do to address these issues?

A. Place an elastic load balancer in front of the Amazon S3 bucket to distribute the load during peak hours.
B. Cache the web content with Amazon CloudFront and use all Edge locations for content delivery.
C. Replicate the bucket in eu-west-1 and use an Amazon Route 53 failover routing policy to determine which bucket it should serve the request to.
D. Use an Amazon Route 53 weighted routing policy for the CloudFront domain name to distribute the GET request between CloudFront and the Amazon S3 bucket directly.

Answer: B

* 分析：网站给出的答案竟然是D，但是B很明显是正确的。

## A Solutions Architect is designing a solution that includes a managed VPN connection. To monitor whether the VPN connection is up or down, the Architect should use:

A. an external service to ping the VPN endpoint from outside the VPC.
B. AWS CloudTrail to monitor the endpoint.
C. the CloudWatch TunnelState Metric.
D. an AWS Lambda function that parses the VPN connection logs.

Answer: C

> Monitoring VPN Tunnels Using Amazon CloudWatch(https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html)

## A social networking portal experiences latency and throughput issues due to an increased number of users. Application servers use very large datasets from an Amazon RDS database, which creates a performance bottleneck on the database. Which AWS service should be used to improve performance?

A. Auto Scaling
B. Amazon SQS
C. Amazon ElastiCache
D. ELB Application Load Balancer

Answer: C

## A Solutions Architect is designing network architecture for an application that has compliance requirements. The application will be hosted on Amazon EC2 instances in a private subnet and will be using Amazon S3 for storing data. The compliance requirements mandate that the data cannot traverse the public Internet. What is the MOST secure way to satisfy this requirement?

A. Use a NAT Instance.
B. Use a NAT Gateway.
C. Use a VPC endpoint.
D. Use a Virtual Private Gateway.

Answer: C

> New – VPC Endpoint for Amazon S3(https://aws.amazon.com/cn/blogs/aws/new-vpc-endpoint-for-amazon-s3/)

## Developers are creating a new online transaction processing (OLTP) application for a small database that is very read-write intensive. A single table in the database is updated continuously throughout the day, and the developers want to ensure that the database performance is consistent. Which Amazon EBS storage option will achieve the MOST consistent performance to help maintain application performance?

A. Provisioned IOPS SSD
B. General Purpose SSD
C. Cold HDD
D. Throughput Optimized HDD

Answer: A

## A Solutions Architect is designing a log-processing solution that requires storage that supports up to 500 MB/s throughput. The data is sequentially accessed by an Amazon EC2 instance. Which Amazon storage type satisfies these requirements?

A. EBS Provisioned IOPS SSD (io1)
B. EBS General Purpose SSD (gp2)
C. EBS Throughput Optimized HDD (st1)
D. EBS Cold HDD (sc1)

Answer: C

## A company's development team plans to create an Amazon S3 bucket that contains millions of images. The team wants to maximize the read performance of
Amazon S3. Which naming scheme should the company use?

A. Add a date as the prefix.
B. Add a sequential id as the suffix.
C. Add a hexadecimal hash as the suffix.
D. Add a hexadecimal hash as the prefix.

Answer: A

* 分析：这道题的旧答案是D，不过根据最新文档档案为A。

> https://docs.aws.amazon.com/AmazonS3/latest/dev/optimizing-performance.html
>
> For example, previously Amazon S3 performance guidelines recommended randomizing prefix naming with hashed characters to optimize performance for frequent data retrievals. You no longer have to randomize prefix naming for performance, and can use sequential date-based naming for your prefixes.

* 什么是Prefix?

> For example, your application can achieve at least 3,500 PUT/COPY/POST/DELETE and 5,500 GET/HEAD requests per second per prefix in a bucket. There are no limits to the number of prefixes in a bucket. You can increase your read or write performance by parallelizing reads. For example, if you create 10 prefixes in an Amazon S3 bucket to parallelize reads, you could scale your read performance to 55,000 read requests per second.

> However, if the new limits are not sufficient, prefixes would need to be used. A prefix has no fixed number of characters. It is any string between a bucket name and an object name, for example:
> bucket/folder1/sub1/file
> bucket/folder1/sub2/file
> bucket/1/file
> bucket/2/file
> Prefixes of the object 'file' would be: /folder1/sub1/ , /folder1/sub2/, /1/, /2/.

## A Solutions Architect needs to design a solution that will enable a security team to detect, review, and perform root cause analysis of security incidents that occur in a cloud environment. The Architect must provide a centralized view of all API events for current and future AWS regions. How should the Architect accomplish this task?

A. Enable AWS CloudTrail logging in each individual region. Repeat this for all future regions.
B. Enable Amazon CloudWatch logs for all AWS services across all regions and aggregate them in a single Amazon S3 bucket.
C. Enable AWS Trusted Advisor security checks and report all security incidents for all regions.
D. Enable AWS CloudTrail by creating a new trail and apply the trail to all regions.

Answer: D

* 分析：这道题肯定使用CloudTrail，区别在于设定范围。

> https://aws.amazon.com/cn/about-aws/whats-new/2015/12/turn-on-cloudtrail-across-all-regions-and-support-for-multiple-trails/
>You can now turn on a trail across all regions for your AWS account. CloudTrail will deliver log files from all regions to the Amazon S3 bucket and an optional CloudWatch Logs log group you specified. Additionally, when AWS launches a new region, CloudTrail will create the same trail in the new region. As a result, you will receive log files containing API activity for the new region without taking any action. Using the CloudTrail console, you can specify that a trail applies to all regions. For more details, refer to the Applying a trail to all regions section of the CloudTrail FAQ.

## A company has a legacy application using a proprietary file system and plans to migrate the application to AWS. Which storage service should the company use?

A. Amazon DynamoDB
B. Amazon S3
C. Amazon EBS
D. Amazon EFS

Answer: C

* 分析：这道题有点蒙人，关键词在proprietary（专有的），EFS未必支持，只有EBS才能100%满足。

## A company plans to use AWS for all new batch processing workloads. The company's developers use Docker containers for the new batch processing. The system design must accommodate critical and non-critical batch processing workloads 24/7. How should a Solutions Architect design this architecture in a cost-efficient manner?

A. Purchase Reserved Instances to run all containers. Use Auto Scaling groups to schedule jobs.
B. Host a container management service on Spot Instances. Use Reserved Instances to run Docker containers.
C. Use Amazon ECS orchestration and Auto Scaling groups: one with Reserve Instances, one with Spot Instances.
D. Use Amazon ECS to manage container orchestration. Purchase Reserved Instances to run all batch workloads at the same time.

* 分析：绕嘴，多读两遍。主要是应对两种不同类型的任务。

## A company is evaluating Amazon S3 as a data storage solution for their daily analyst reports. The company has implemented stringent requirements concerning the security of the data at rest. Specifically, the CISO asked for the use of envelope encryption with separate permissions for the use of an envelope key, automated rotation of the encryption keys, and visibility into when an encryption key was used and by whom. Which steps should a Solutions Architect take to satisfy the security requirements requested by the CISO?

A. Create an Amazon S3 bucket to store the reports and use Server-Side Encryption with Customer-Provided Keys (SSE-C).
B. Create an Amazon S3 bucket to store the reports and use Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3).
C. Create an Amazon S3 bucket to store the reports and use Server-Side Encryption with AWS KMS-Managed Keys (SSE-KMS).
D. Create an Amazon S3 bucket to store the reports and use Amazon s3 versioning with Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3).

Answer: C

* 分析：用S3 + KMS服务。

## (争议)A customer has a production application that frequently overwrites and deletes data, the application requires the most up-to-date version of the data every time it is requested. Which storage should a Solutions Architect recommend to bet accommodate this use case?

A. Amazon S3
B. Amazon RDS
C. Amazon RedShift
D. AWS Storage Gateway

Answer: A

* 分析：这道题的争议点在答案B，因为S3提供eventual consistency for overwirte PUTS and DELETES，可能会导致无法获取最新数据的问题。不确定该问题是否会考到，暂时没有找到更合理的解释。

> Amazon S3 Data Consistency Model(https://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html)
> Amazon S3 provides read-after-write consistency for PUTS of new objects in your S3 bucket in all Regions with one caveat. The caveat is that if you make a HEAD or GET request to the key name (to find if the object exists) before creating the object, Amazon S3 provides eventual consistency for read-after-write.
>
> Amazon S3 offers eventual consistency for overwrite PUTS and DELETES in all Regions.
>
> Updates to a single key are atomic. For example, if you PUT to an existing key, a subsequent read might return the old data or the updated data, but it never returns corrupted or partial data.

## A Solutions Architect is designing a photo application on AWS. Every time a user uploads a photo to Amazon S3, the Architect must insert a new item to a
DynamoDB table. Which AWS-managed service is the BEST fit to insert the item?

A. Lambda@Edge
B. AWS Lambda
C. Amazon API Gateway
D. Amazon EC2 instances

Answer: B

* 参考链接：https://aws.amazon.com/cn/blogs/machine-learning/build-your-own-face-recognition-service-using-amazon-rekognition/

## An application relies on messages being sent and received in order. The volume will never exceed more than 300 transactions each second. Which service should be used?

A. Amazon SQS
B. Amazon SNS
C. Amazon ECS
D. AWS STS

Answer: A

> 问：Amazon SNS 与 Amazon SQS 有何不同？
>
> Amazon Simple Queue Service (SQS) 和 Amazon SNS 都是 AWS 中的消息收发服务，但为开发人员提供了不同的优势。Amazon SNS 允许应用程序通过“推送”机制向多个订阅者发送时间关键型消息，并且无需定期检查或“轮询”更新。Amazon SQS 是一种供分布式应用程序使用的消息队列服务，通过轮询模式交换消息，可用于分离收发组件。Amazon SQS 使应用程序的分布式组件可以灵活地收发消息，并且不要求每个组件同时可用。
>
> 一种常见的模式是使用 SNS 将消息发布到 Amazon SQS 队列，进而以可靠的方式将消息异步发送到一个或多个系统组件。

## A Solutions Architect is designing an application on AWS that uses persistent block storage. Data must be encrypted at rest. Which solution meets the requirement?

A. Enable SSL on Amazon EC2 instances.
B. Encrypt Amazon EBS volumes on Amazon EC2 instances.
C. Enable server-side encryption on Amazon S3.
D. Encrypt Amazon EC2 Instance Storage.

Answer: B

* New EBS Encryption for Additional Data Protection(https://aws.amazon.com/cn/blogs/aws/protect-your-data-with-new-ebs-encryption/)

## (争议)A company is launching a static website using the zone apex (mycompany.com). The company wants to use Amazon Route 53 for DNS. Which steps should the company perform to implement a scalable and cost-effective solution? (Choose two.)

A. Host the website on an Amazon EC2 instance with ELB and Auto Scaling, and map a Route 53 alias record to the ELB endpoint.
B. Host the website using AWS Elastic Beanstalk, and map a Route 53 alias record to the Beanstalk stack.
C. Host the website on an Amazon EC2 instance, and map a Route 53 alias record to the public IP address of the Amazon EC2 instance.
D. Serve the website from an Amazon S3 bucket, and map a Route 53 alias record to the website endpoint.
E. Create a Route 53 hosted zone, and set the NS records of the domain to use Route 53 name servers.

Answer: DE

* 分析：又是一道争议非常大的题，原来的答案是CD，从cost-effective的角度说C确实不够经济。参考AWS如何构建静态网站的最佳实践：https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html

## (争议)A manufacturing company captures data from machines running at customer sites. Currently, thousands of machines send data every 5 minutes, and this is expected to grow to hundreds of thousands of machines in the near future. The data is logged with the intent to be analyzed in the future as needed. What is the SIMPLEST method to store this streaming data at scale?

A. Create an Amazon Kinesis Firehouse delivery stream to store the data in Amazon S3.
B. Create an Auto Scaling group of Amazon EC2 servers behind ELBs to write the data into Amazon RDS.
C. Create an Amazon SQS queue, and have the machines write to the queue.
D. Create an Amazon EC2 server farm behind an ELB to store the data in Amazon EBS Cold HDD volumes.

Answer: A

* 分析：很奇怪为什么原有答案给出B，这道题明显是暗指实时计算Kinesis服务。

## A bank is writing new software that is heavily dependent upon the database transactions for write consistency. The application will also occasionally generate reports on data in the database, and will do joins across multiple tables. The database must automatically scale as the amount of data grows. Which AWS service should be used to run the database?

A. Amazon S3
B. Amazon Aurora
C. Amazon DynamoDB
D. Amazon Redshift

Answer: B

* 分析：很明显需要关系型数据库。

## A Solutions Architect is designing a new application that needs to access data in a different AWS account located within the same region. The data must not be accessed over the Internet. Which solution will meet these requirements with the LOWEST cost?

A. Add rules to the security groups in each account.
B. Establish a VPC Peering connection between accounts.
C. Configure Direct Connect in each account.
D. Add a NAT Gateway to the data account.

Answer: B

* 分析：B的方案是成本最低的。

## A Solutions Architect is designing a mobile application that will capture receipt images to track expenses. The Architect wants to store the images on Amazon S3. However, uploading images through the web server will create too much traffic. What is the MOST efficient method to store images from a mobile application on Amazon S3?

A. Upload directly to S3 using a pre-signed URL.
B. Upload to a second bucket, and have a Lambda event copy the image to the primary bucket.
C. Upload to a separate Auto Scaling group of servers behind an ELB Classic Load Balancer, and have them write to the Amazon S3 bucket.
D. Expand the web server fleet with Spot Instances to provide the resources to handle the images.

Answer: C

* 分析：A选项相较于题目中描述的并没有本质区别。

> A presigned URL gives you access to the object identified in the URL, provided that the creator of the presigned URL has permissions to access that object. That is, if you receive a presigned URL to upload an object, you can upload the object only if the creator of the presigned URL has the necessary permissions to upload that object.
>
> All objects and buckets by default are private. The presigned URLs are useful if you want your user/customer to be able to upload a specific object to your bucket, but you don't require them to have AWS security credentials or permissions. When you create a presigned URL, you must provide your security credentials and then specify a bucket name, an object key, an HTTP method (PUT for uploading objects), and an expiration date and time. The presigned URLs are valid only for the specified duration.

## A company requires that the source, destination, and protocol of all IP packets be recorded when traversing a private subnet. What is the MOST secure and reliable method of accomplishing this goal.

A. Create VPC flow logs on the subnet.
B. Enable source destination check on private Amazon EC2 instances.
C. Enable AWS CloudTrail logging and specify an Amazon S3 bucket for storing log files.
D. Create an Amazon CloudWatch log to capture packet information.

Answer: A

* 分析：启动VPC流表日志, CloudTrail没有此能力

## A Solutions Architect has a multi-layer application running in Amazon VPC. The application has an ELB Classic Load Balancer as the front end in a public subnet, and an Amazon EC2-based reverse proxy that performs content-based routing to two backend Amazon EC2 instances hosted in a private subnet. The Architect sees tremendous traffic growth and is concerned that the reverse proxy and current backend set up will be insufficient. Which actions should the Architect take to achieve a cost-effective solution that ensures the application automatically scales to meet traffic demand? (Select two.)

A. Replace the Amazon EC2 reverse proxy with an ELB internal Classic Load Balancer.
B. Add Auto Scaling to the Amazon EC2 backend fleet.
C. Add Auto Scaling to the Amazon EC2 reverse proxy layer.
D. Use t2 burstable instance types for the backend fleet.
E. Replace both the frontend and reverse proxy layers with an ELB Application Load Balancer.

Answer: BE

* 分析：又是一道错题，原答案是AB。根据题目分析，出现瓶颈的地方来自于两处：反向代理和后端服务。后端服务的扩展没有什么争议，所以B很明显是正确的。最大的争议来自于是使用什么方式替代目前成为瓶颈的反向代理EC2。原题里反向代理EC2作为content-based routing，那么问题的关键就是CLB、ELB谁能做content-based routing了。根据目前最新的内容，所以需要使用Application Load Balancer来提供content-based routing了。

> There are three types of Elastic Load Balancer (ELB) on AWS:
>
> Classic Load Balancer (CLB) – this is the oldest of the three and provides basic load balancing at both layer 4 and layer 7.
>
> Application Load Balancer (ALB) – layer 7 load balancer that routes connections based on the content of the request.
>
> Network Load Balancer (NLB) – layer 4 load balancer that routes connections based on IP protocol data.
>
> Note: The Classic Load Balancer may be phased out over time and Amazon are promoting the ALB and NLB for most use cases within VPC.

> Introducing Amazon EC2 Fleet
> Posted On: May 2, 2018
>
> Amazon EC2 Fleet is a new feature that simplifies the provisioning of Amazon EC2 capacity across different Amazon EC2 instance types, Availability Zones and across On-Demand, Amazon EC2 Reserved Instances (RI) and Amazon EC2 Spot purchase models. With a single API call, now you can provision capacity across EC2 instance types and across purchase models to achieve desired scale, performance and cost.
>
> You can create an EC2 Fleet specification defining target capacity, which EC2 instance types work for you, and how much of your fleet should be filled using On-Demand, RI and Spot purchase models. You can also indicate whether EC2 Fleet should take into account the number of cores and amount of memory on each instance or consider all instances equal when scaling. EC2 Fleet then launches the lowest price combination of instances to meet the target capacity based on these preferences. EC2 fleet enables you to use multiple instance types and purchase models to provision capacity cost effectively, with just a few clicks in the AWS Management Console.
>
> Amazon EC2 Fleet is now available in all public Regions. To learn more about simplifying the provisioning of Amazon EC2 capacity across different Amazon EC2 instance types, AWS Availability Zones and across On-Demand, RI and Spot purchase models using Amazon EC2 Fleet, visit this blog. To learn more about Amazon EC2 pricing models, visit this page.

* EC2 Fleet – Manage Thousands of On-Demand and Spot Instances with One Request(https://amazonaws-china.com/blogs/aws/ec2-fleet-manage-thousands-of-on-demand-and-spot-instances-with-one-request/)
* New – Advanced Request Routing for AWS Application Load Balancers(https://amazonaws-china.com/blogs/aws/new-advanced-request-routing-for-aws-application-load-balancers/)
* ELASTIC LOAD BALANCING(https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/)

## A company is launching a marketing campaign on their website tomorrow and expects a significant increase in traffic. The website is designed as a multi-tiered web architecture, and the increase in traffic could potentially overwhelm the current design. What should a Solutions Architect do to minimize the effects from a potential failure in one or more of the tiers?

A. Migrate the database to Amazon RDS.
B. Set up DNS failover to a statistic website.
C. Use Auto Scaling to keep up with the demand.
D. Use both a SQL and a NoSQL database in the design.

Answer: C

* 分析：明天就上线了，改啥都来不及了，还是价格Auto scaling策略吧。

## A web application experiences high compute costs due to serving a high amount of static web content. How should the web server architecture be designed to be the MOST cost-efficient?

A. Create an Auto Scaling group to scale out based on average CPU usage.
B. Create an Amazon CloudFront distribution to pull static content from an Amazon S3 bucket.
C. Leverage Reserved Instances to add additional capacity at a significantly lower price.
D. Create a multi-region deployment using an Amazon Route 53 geolocation routing policy.

Answer: B

## A web application experiences high compute costs due to serving a high amount of static web content. How should the web server architecture be designed to be the MOST cost-efficient?

A. Create an Auto Scaling group to scale out based on average CPU usage.
B. Create an Amazon CloudFront distribution to pull static content from an Amazon S3 bucket.
C. Leverage Reserved Instances to add additional capacity at a significantly lower price.
D. Create a multi-region deployment using an Amazon Route 53 geolocation routing policy.

Answer: B

## A Solutions Architect plans to migrate NAT instances to NAT gateway. The Architect has NAT instances with scripts to manage high availability. What is the MOST efficient method to achieve similar high availability with NAT gateway?

A. Remove source/destination check on NAT instances.
B. Launch a NAT gateway in each Availability Zone.
C. Use a mix of NAT instances and NAT gateway.
D. Add an ELB Application Load Balancer in front of NAT gateway.

Answer: B

* NAT 实例与 NAT 网关的比较(https://docs.aws.amazon.com/zh_cn/vpc/latest/userguide/vpc-nat-comparison.html)

> 每个 NAT 网关都在特定可用区中创建，并在该可用区进行冗余实施。您可以在一个可用区中创建的 NAT 网关存在数量限制。有关更多信息，请参阅 Amazon VPC 限制。
>
> 注意:
> 如果您在多个可用区中拥有资源，并且它们共享一个 NAT 网关，则在该 NAT 网关的可用区不可用时，其他可用区中的资源将无法访问 Internet。要创建不依赖于可用区的架构，请在每个可用区中都创建一个 NAT 网关，并配置路由以确保这些资源使用自身可用区中的 NAT 网关。

## A Solutions Architect is designing a solution to store a large quantity of event data in Amazon S3. The Architect anticipates that the workload will consistently exceed 100 requests each second. What should the Architect do in Amazon S3 to optimize performance?

A. Randomize a key name prefix.
B. Store the event data in separate buckets.
C. Randomize the key name suffix.
D. Use Amazon S3 Transfer Acceleration.

Answer: A

* 分析：这道题和上面有道题类似，目前S3建议使用时间作为prefix，原来是建议使用hash方式。
* 最佳实践设计模式：优化 Amazon S3 性能(https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/dev/optimizing-performance.html)

> 下面的主题介绍的最佳实践准则和设计模式用于优化使用 Amazon S3 的应用程序的性能。本指南的优先级高于之前有关优化 Amazon S3 的性能的任何指南。例如，以前的 Amazon S3 性能指南建议用哈希字符来随机化前缀命名，以便优化频繁数据检索的性能。现在，您不再需要为了提高性能随机化前缀命名，而是可以对前缀使用基于顺序日期的命名方式。有关对 Amazon S3 进行性能优化的最新信息，请参阅Amazon S3 的性能准则和Amazon S3 的性能设计模式。

## A user is testing a new service that receives location updates from 3,600 rental cars every hour. Which service will collect data and automatically scale to accommodate production workload?

A. Amazon EC2
B. Amazon Kinesis Firehose
C. Amazon EBS
D. Amazon API Gateway

Answer: B

* 分析：又是一道争议题，大部分给出的答案是B，就应用场景上看Kinesis更适合实时计算场景。

## A Solutions Architect is designing a web application. The web and application tiers need to access the Internet, but they cannot be accessed from the Internet. Which of the following steps is required?

A. Attach an Elastic IP address to each Amazon EC2 instance and add a route from the private subnet to the public subnet.
B. Launch a NAT gateway in the public subnet and add a route to it from the private subnet.
C. Launch Amazon EC2 instances in the public subnet and change the security group to allow outbound traffic on port 80.
D. Launch a NAT gateway in the private subnet and deploy a NAT instance in the private subnet.

Answer: B

## An application stack includes an Elastic Load Balancer in a public subnet, a fleet of Amazon EC2 instances in an Auto Scaling group, and an Amazon RDS MySQL cluster. Users connect to the application from the Internet. The application servers and database must be secure. How should a Solutions Architect perform this task?

A. Create a private subnet for the Amazon EC2 instances and a public subnet for the Amazon RDS cluster.
B. Create a private subnet for the Amazon EC2 instances and a private subnet for the Amazon RDS cluster.
C. Create a public subnet for the Amazon EC2 instances and a private subnet for the Amazon RDS cluster.
D. Create a public subnet for the Amazon EC2 instances and a public subnet for the Amazon RDS cluster.

Answer: B

* 分析：答案给出的是C，有多种方式证明这个答案是错误的。
* How do I connect a public-facing load balancer to EC2 instances that have private IP addresses?(https://amazonaws-china.com/premiumsupport/knowledge-center/public-load-balancer-private-ec2/)
* AWS Best Practices: 3-Tier Infrastructure(https://blog.stratus10.com/aws-best-practices-3-tier-infrastructure)

## A Solutions Architect is designing a solution for a media company that will stream large amounts of data from an Amazon EC2 instance. The data streams are typically large and sequential, and must be able to support up to 500 MB/s. Which storage type will meet the performance requirements of this application?

A. EBS Provisioned IOPS SSD
B. EBS General Purpose SSD
C. EBS Cold HDD
D. EBS Throughput Optimized HDD

Answer: D

## (争议)A legacy application running in premises requires a Solutions Architect to be able to open a firewall to allow access to several Amazon S3 buckets. The Architect has a VPN connection to AWS in place. How should the Architect meet this requirement?

A. Create an IAM role that allows access from the corporate network to Amazon S3.
B. Configure a proxy on Amazon EC2 and use an Amazon S3 VPC endpoint.
C. Use Amazon API Gateway to do IP whitelisting.
D. Configure IP whitelisting on the customer's gateway.

Answer: B

* 分析：争议较大的一道题，这里采用了这个解释：https://d0.awsstatic.com/aws-answers/Accessing_VPC_Endpoints_from_Remote_Networks.pdf

## A Solutions Architect is designing a database solution that must support a high rate of random disk reads and writes. It must provide consistent performance, and requires long-term persistence. Which storage solution BEST meets these requirements?

A. An Amazon EBS Provisioned IOPS volume
B. An Amazon EBS General Purpose volume
C. An Amazon EBS Magnetic volume
D. An Amazon EC2 Instance Store

Answer: A

## A Solutions Architect is designing solution with AWS Lambda where different environments require different database passwords. What should the Architect do to accomplish this in a secure and scalable way?

A. Create a Lambda function for each individual environment.
B. Use Amazon DynamoDB to store environmental variables.
C. Use encrypted AWS Lambda environmental variables.
D. Implement a dedicated Lambda function for distributing variables.

Answer: C

## A news organization plans to migrate their 20 TB video archive to AWS. The files are rarely accessed, but when they are, a request is made in advance and a 3 to 5-hour retrieval time frame is acceptable. However, when there is a breaking news story, the editors require access to archived footage within minutes. Which storage solution meets the needs of this organization while providing the LOWEST cost of storage?

A. Store the archive in Amazon S3 Reduced Redundancy Storage.
B. Store the archive in Amazon Glacier and use standard retrieval for all content.
C. Store the archive in Amazon Glacier and pay the additional charge for expedited retrieval when needed.
D. Store the archive in Amazon S3 with a lifecycle policy to move this to S3 Infrequent Access after 30 days.

Answer: C

> 问：从 Amazon S3 Glacier 检索数据如何收费？
>
> 从 Amazon S3 Glacier 检索数据的方式有三种：加急、标准和批量检索。每种方式具有不同的每 GB 检索费和每存档请求费（即请求一个存档计为一个请求）。有关不同 AWS 区域的 S3 Glacier 定价的详细信息，请访问 Amazon S3 Glacier 定价页面。
>
> 定价标准： https://amazonaws-china.com/cn/glacier/pricing/

## A Solutions Architect is building a multi-tier website. The web servers will be in a public subnet, and the database servers will be in a private subnet. Only the web servers can be accessed from the Internet. The database servers must have Internet access for software updates. Which solution meets the requirements?

A. Assign Elastic IP addresses to the database instances.
B. Allow Internet traffic on the private subnet through the network ACL.
C. Use a NAT Gateway.
D. Use an egress-only Internet Gateway.

Answer: C

## A Solutions Architect is designing a Lambda function that calls an API to list all running Amazon RDS instances. How should the request be authorized?

A. Create an IAM access and secret key, and store it in the Lambda function.
B. Create an IAM role to the Lambda function with permissions to list all Amazon RDS instances.
C. Create an IAM role to Amazon RDS with permissions to list all Amazon RDS instances.
D. Create an IAM access and secret key, and store it in an encrypted RDS database.

Answer: B

> 教程：配置 Lambda 函数以访问 Amazon VPC 中的 Amazon RDS
>
> 打开 IAM 控制台中的“角色”页面。
> 选择 Create role (创建角色)。
> 创建具有以下属性的角色。
> Trusted entity (可信任的实体) – Lambda.
> 权限 – AWSLambdaVPCAccessExecutionRole。
> 角色名称 (角色名称) – lambda-vpc-role。
> AWSLambdaVPCAccessExecutionRole 具有函数管理与 VPC 的网络连接所需的权限。

## A Solutions Architect is building an application on AWS that will require 20,000 IOPS on a particular volume to support a media event. Once the event ends, the IOPS need is no longer required. The marketing team asks the Architect to build the platform to optimize storage without incurring downtime. How should the Architect design the platform to meet these requirements?

A. Change the Amazon EC2 instant types.
B. Change the EBS volume type to Provisioned IOPS.
C. Stop the Amazon EC2 instance and provision IOPS for the EBS volume.
D. Enable an API Gateway to change the endpoints for the Amazon EC2 instances.

Answer: B

> 打开 Amazon EC2 控制台 https://console.aws.amazon.com/ec2/。
>
> 选择 Volumes，选择要修改的卷，然后依次选择 Actions、Modify Volume。
>
> Modify Volume 窗口显示卷 ID 和卷的当前配置，包括类型、大小和 IOPS。您可以在单个操作中更改任何或所有这些设置。设置新的配置值，如下所述：
>
> 要修改类型，请为 Volume Type 选择一个值。
>
> 要修改大小，请为 Size 输入一个允许的整数值。
>
> 如果选择预配置 IOPS SSD (io1) 作为卷类型，请为 IOPS 输入一个允许的整数值。
>
> 完成更改卷设置后，请选择 Modify (修改)。当系统提示您确认时，请选择 Yes。
>
> 在扩展卷的文件系统以使用新的存储容量之前，修改卷大小没有实际效果。有关更多信息，请参阅调整卷大小后扩展 Linux 文件系统。

## A Solutions Architect is building a new feature using a Lambda to create metadata when a user uploads a picture to Amazon S3. All metadata must be indexed. Which AWS service should the Architect use to store this metadata?

A. Amazon S3
B. Amazon DynamoDB
C. Amazon Kinesis
D. Amazon EFC

Answer: B

* Building and Maintaining an Amazon S3 Metadata Index without Servers(https://amazonaws-china.com/cn/blogs/big-data/building-and-maintaining-an-amazon-s3-metadata-index-without-servers)

> In this post, I walk through an approach for building such an index using Amazon DynamoDB and AWS Lambda. With these technologies, you can create a high performance, low-cost index that scales and remains highly available without the need to maintain traditional servers.

## An interactive, dynamic website runs on Amazon EC2 instances in a single subnet behind an ELB Classic Load Balancer. Which design changes will make the site more highly available?

A. Move some Amazon EC2 instances to a subnet in a different way(different AZ).
B. Move the website to Amazon S3.
C. Change the ELB to an Application Load Balancer.
D. Move some Amazon EC2 instances to a subnet in the same Availability Zone.

Answer: A

* 分析：这道题的选项A可能是写错了，根据评论区是different AZ，那么选择A就比较容易理解了。评论区有一种声音是选择C，但是从高可用性上讲，C选项并没有实质的价值。

## A Solutions Architect is designing a web application that is running on an Amazon EC2 instance. The application stores data in DynamoDB. The Architect needs to secure access to the DynamoDB table. What combination of steps does AWS recommend to achieve secure authorization? (Select two.)

A. Store an access key on the Amazon EC2 instance with rights to the Dynamo DB table.
B. Attach an IAM user to the Amazon EC2 instance.
C. Create an IAM role with permissions to write to the DynamoDB table.
D. Attach an IAM role to the Amazon EC2 instance.
E. Attach an IAM policy to the Amazon EC2 instance.

Answer: CD

* 分析：AWS一向重视安全性，所以更推荐使用STS方式进行接口调用

## (争议)A Solutions Architect is about to deploy an API on multiple EC2 instances in an Auto Scaling group behind an ELB. The support team has the following operational requirements:
1 They get an alert when the requests per second go over 50,000
2 They get an alert when latency goes over 5 seconds
3 They can validate how many times a day users call the API requesting highly-sensitive data
Which combination of steps does the Architect need to take to satisfy these operational requirements? (Select two.)

A. Ensure that CloudTrail is enabled.
B. Create a custom CloudWatch metric to monitor the API for data access.
C. Configure CloudWatch alarms for any metrics the support team requires.
D. Ensure that detailed monitoring for the EC2 instances is enabled.
E. Create an application to export and save CloudWatch metrics for longer term trending analysis.

Answer: BC

* 分析：原题给出的答案是BD，但是EC2的详细监控其实并没有包含API级别的监控，ELB的监控才包含了API访问的监控。

## (争议)A Solutions Architect is designing a highly-available website that is served by multiple web servers hosted outside of AWS. If an instance becomes unresponsive, the Architect needs to remove it from the rotation. What is the MOST efficient way to fulfill this requirement?

A. Use Amazon CloudWatch to monitor utilization.
B. Use Amazon API Gateway to monitor availability.
C. Use an Amazon Elastic Load Balancer.
D. Use Amazon Route 53 health checks.

Answer: A

* 分析：不同网站给出不同答案，原网站给出的答案是C，但是从题目分析关键词是the Architect needs to remove it，所以看起来A更合理一些。但是ELB增加health check之后应该可以自动的将不可用节点移除掉。

## A company hosts a popular web application. The web application connects to a database running in a private VPC subnet. The web servers must be accessible only to customers on an SSL connection. The RDS MySQL database server must be accessible only from the web servers. How should the Architect design a solution to meet the requirements without impacting running applications?

A. Create a network ACL on the web server's subnet, and allow HTTPS inbound and MySQL outbound. Place both database and web servers on the same subnet.
B. Open an HTTPS port on the security group for web servers and set the source to 0.0.0.0/0. Open the MySQL port on the database security group and attach it to the MySQL instance. Set the source to Web Server Security Group.
C. Create a network ACL on the web server's subnet, and allow HTTPS inbound, and specify the source as 0.0.0.0/0. Create a network ACL on a database subnet, allow MySQL port inbound for web servers, and deny all outbound traffic.
D. Open the MySQL port on the security group for web servers and set the source to 0.0.0.0/0. Open the HTTPS port on the database security group and attach it to the MySQL instance. Set the source to Web Server Security Group.

Answer: B

## Which service should an organization use if it requires an easily managed and scalable platform to host its web application running on Nginx?

A. AWS Lambda
B. Auto Scaling
C. AWS Elastic Beanstalk
D. Elastic Load Balancing

Answer: C

> AWS Elastic Beanstalk 是一项易于使用的服务，用于在熟悉的服务器（例如 Apache 、Nginx、Passenger 和 IIS ）上部署和扩展使用 Java、.NET、PHP、Node.js、Python、Ruby、GO 和 Docker 开发的 Web 应用程序和服务。
> 您只需上传代码，Elastic Beanstalk 即可自动处理包括容量预配置、负载均衡、自动扩展和应用程序运行状况监控在内的部署工作。同时，您能够完全控制为应用程序提供支持的 AWS 资源，并可以随时访问底层资源。
> Elastic Beanstalk 不额外收费 – 您只需为存储和运行应用程序所需的 AWS 资源付费。

## An Administrator is hosting an application on a single Amazon EC2 instance, which users can access by the public hostname. The administrator is adding a second instance, but does not want users to have to decide between many public hostnames. Which AWS service will decouple the users from specific Amazon EC2 instances?

A. Amazon SQS
B. Auto Scaling group
C. Amazon EC2 security group
D. Amazon ELB

Answer: D

* 分析：这道题原网站给出答案是B，但是明显应该是D

## A Solutions Architect is designing a microservices-based application using Amazon ECS. The application includes a WebSocket component, and the traffic needs to be distributed between microservices based on the URL. Which service should the Architect choose to distribute the workload?

A. ELB Classic Load Balancer
B. Amazon Route 53 DNS
C. ELB Application Load Balancer
D. Amazon CloudFront

Answer: C

* 参考链接：https://docs.aws.amazon.com/aws-technical-content/latest/microservices-on-aws/microservices-on-aws.pdf?icmpid=link_from_whitepapers_page

## A Solutions Architect is designing the storage layer for a production relational database. The database will run on Amazon EC2. The database is accessed by an application that performs intensive reads and writes, so the database requires the LOWEST random I/O latency. Which data storage method fulfills the above requirements?

A. Store data in a filesystem backed by Amazon Elastic File System (EFS).
B. Store data in Amazon S3 and use a third-party solution to expose Amazon S3 as a filesystem to the database server.
C. Store data in Amazon Dynamo DB and emulate relational database semantics.
D. Stripe data across multiple Amazon EBS volumes using RAID 0.

Answer: D

## A Solutions Architect is designing a VPC. Instances in a private subnet must be able to establish IPv6 traffic to the Internet. The design must scale automatically and not incur any additional cost. This can be accomplished with:

A. an egress-only internet gateway
B. a NAT gateway
C. a custom NAT instance
D. a VPC endpoint

Answer: A

* 参考链接：https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html
> An egress-only Internet gateway. This enables instances in the private subnet to send requests to the Internet over IPv6 (for example, for software updates). An egress-only Internet gateway is necessary if you want instances in the private subnet to be able to initiate communication with the Internet over IPv6. For more information, see Egress-Only Internet Gateways.

## A web application stores all data in an Amazon RDS Aurora database instance. A Solutions Architect wants to provide access to the data for a detailed report for the Marketing team, but is concerned that the additional load on the database will affect the performance of the web application. How can the report be created without affecting the performance of the application?

A. Create a read replica of the database.
B. Provision a new RDS instance as a secondary master.
C. Configure the database to be in multiple regions.
D. Increase the number of provisioned storage IOPS.

Answer: A

* 分析：原有网站给出的答案是B，明显是A，搞这么复杂干啥

## A company has an application that stores sensitive data. The company is required by government regulations to store multiple copies of its data. What would be the MOST resilient and cost-effective option to meet this requirement?

A. Amazon EFS
B. Amazon RDS
C. AWS Storage Gateway
D. Amazon S3

Answer: D

## A company is using AWS Key Management Service (AWS KMS) to secure their Amazon RDS databases. An auditor has recommended that the company log all use of their AWS KMS keys. What is the SIMPLEST solution?

A. Associate AWS KMS metrics with Amazon CloudWatch.
B. Use AWS CloudTrail to log AWS KMS key usage.
C. Deploy a monitoring agent on the RDS instances.
D. Poll AWS KMS periodically with a scheduled job.

Answer: B

## A Solutions Architect is designing a stateful web application that will run for one year (24/7) and then be decommissioned. Load on this platform will be constant, using a number of r4.8xlarge instances. Key drivers for this system include high availability, but elasticity is not required. What is the MOST cost-effective way to purchase compute for this platform?

A. Scheduled Reserved Instances
B. Convertible Reserved Instances
C. Standard Reserved Instances
D. Spot Instances

Answer: C

* 分析：根据题目要求7*24小时不停机，所以需要排除A和D两个选项, B选项在这个场景下并不需要，所以选C

> Exchanging Convertible Reserved Instances: You can exchange one or more Convertible Reserved Instances for another Convertible Reserved Instance with a different configuration, including instance family, operating system, and tenancy. There are no limits to how many times you perform an exchange, as long as the target Convertible Reserved Instance is of an equal or higher value than the Convertible Reserved Instances that you are exchanging.

## A media company asked a Solutions Architect to design a highly available storage solution to serve as a centralized document store for their Amazon EC2 instances. The storage solution needs to be POSIX-compliant, scale dynamically, and be able to serve up to 100 concurrent EC2 instances. Which solution meets these requirements?

A. Create an Amazon S3 bucket and store all of the documents in this bucket.
B. Create an Amazon EBS volume and allow multiple users to mount that volume to their EC2 instance(s).
C. Use Amazon Glacier to store all of the documents.
D. Create an Amazon Elastic File System (Amazon EFS) to store and share the documents.

Answer: D

* 分析：需要文件接口，并且同时访问，那么只有EFS能够满足

## A Solution Architect has a two-tier application with a single Amazon EC2 instance web server and Amazon RDS MySQL Multi-AZ DB instances. The Architect is re-architecting the application for high availability by adding instances in a second Availability Zone. Which additional services will improve the availability of the application? (Choose two.)

A. Auto Scaling group
B. AWS CloudTrail
C. ELB Classic Load Balancer
D. Amazon DynamoDB
E. Amazon ElastiCache

Answer: AC

* 分析：原网站给出的答案是AE，E显然没什么用对于目标

## A company is migrating its data center to AWS. As part of this migration, there is a three-tier web application that has strict data-at-rest encryption requirements. The customer deploys this application on Amazon EC2 using Amazon EBS, and now must provide encryption at-rest. How can this requirement be met without changing the application?

A. Use AWS Key Management Service and move the encrypted data to Amazon S3.
B. Use an application-specific encryption API with AWS server-side encryption.
C. Use encrypted EBS storage volumes with AWS-managed keys.
D. Use third-party tools to encrypt the EBS data volumes with Key Management Service Bring Your Own Keys.

Answer: C

## A Solutions Architect is developing software on AWS that requires access to multiple AWS services, including an Amazon EC2 instance. This is a security sensitive application, and AWS credentials such as Access Key ID and Secret Access Key need to be protected and cannot be exposed anywhere in the system. What security measure would satisfy these requirements?

A. Store the AWS Access Key ID/Secret Access Key combination in software comments.
B. Assign an IAM user to the Amazon EC2 instance.
C. Assign an IAM role to the Amazon EC2 instance.
D. Enable multi-factor authentication for the AWS root account.

Answer: C

## An AWS workload in a VPC is running a legacy database on an Amazon EC2 instance. Data is stored on a 200GB Amazon EBS (gp2) volume. At peak load times, logs show excessive wait time. What solution should be implemented to improve database performance using persistent storage?

A. Migrate the data on the Amazon EBS volume to an SSD-backed volume.
B. Change the EC2 instance type to one with EC2 instance store volumes.
C. Migrate the data on the EBS volume to provisioned IOPS SSD (io1).
D. Change the EC2 instance type to one with burstable performance.

Answer: C

* 分析：原有答案给出的是D，但是从性能角度看C明显是正确的

## A company's website receives 50,000 requests each second, and the company wants to use multiple applications to analyze the navigation patterns of the users on their website so that the experience can be personalized. What can a Solutions Architect use to collect page clicks for the website and process them sequentially for each user?

A. Amazon Kinesis Stream
B. Amazon SQS standard queue
C. Amazon SQS FIFO queue
D. AWS CloudTrail trail

Answer: A

* Create real-time clickstream sessions and run analytics with Amazon Kinesis Data Analytics, AWS Glue, and Amazon Athena(https://aws.amazon.com/cn/blogs/big-data/create-real-time-clickstream-sessions-and-run-analytics-with-amazon-kinesis-data-analytics-aws-glue-and-amazon-athena/)
* Amazon Kinesis – Real-Time Processing of Streaming Big Data(https://aws.amazon.com/cn/blogs/aws/amazon-kinesis-real-time-processing-of-streamed-data/)

## A company wants to migrate a highly transactional database to AWS. Requirements state that the database has more than 6 TB of data and will grow exponentially. Which solution should a Solutions Architect recommend?

A. Amazon Aurora
B. Amazon Redshift
C. Amazon DynamoDB
D. Amazon RDS MySQL

Answer: A

* 分析：A和D的区别没有找到合适的解释，Aurora的扩展性更好，而且是AWS云原生的。

## (争议)A company hosts a two-tier application that consists of a publicly accessible web server that communicates with a private database. Only HTTPS port 443 traffic to the web server must be allowed from the Internet. Which of the following options will achieve these requirements? (Choose two.)

A. Security group rule that allows inbound Internet traffic for port 443.
B. Security group rule that denies all inbound Internet traffic except port 443.
C. Network ACL rule that allows port 443 inbound and all ports outbound for Internet traffic.
D. Security group rule that allows Internet traffic for port 443 in both inbound and outbound.
E. Network ACL rule that allows port 443 for both inbound and outbound for all Internet traffic.

Answer: AC

* 分析：答案给出的是AE，根据Network ACL的描述，默认情况为白名单，是无状态性的，返回的端口不会自动允许，所以需要C选项打开所有返回的端口。
* 临时端口(https://docs.aws.amazon.com/zh_cn/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports)

> 临时端口
> 上一个部分中的网络 ACL 实例使用了临时端口范围 32768-65535。但是，您可能需要根据自己使用的或作为通信目标的客户端的类型为网络 ACL 使用不同的范围。
> 发起请求的客户端会选择临时端口范围。根据客户端的操作系统不同，范围也随之更改。
> 许多 Linux 内核（包括 Amazon Linux 内核）使用端口 32768-61000。
> 生成自 Elastic Load Balancing 的请求使用端口 1024-65535。
> Windows 操作系统通过 Windows Server 2003 使用端口 1025-5000。
> Windows Server 2008 及更高版本使用端口 49152-65535。
> NAT 网关使用端口 1024 - 65535。
> AWS Lambda 函数使用端口 1024-65535。
> 例如，如果一个来自 Internet 上的 Windows XP 客户端的请求到达您的 VPC 中的 Web 服务器，则您的网络 ACL 必须有相应的出站规则，以支持目标为端口 1025-5000 的数据流。
> 如果您的 VPC 中的一个实例是发起请求的客户端，则您的网络 ACL 必须有入站规则来支持发送到实例类型（Amazon Linux、Windows Server 2008 等）特有的临时端口的数据流。
> 在实际中，为使不同客户端类型可以启动流量进入您 VPC 中的公有实例，您可以开放临时端口 1024-65535。但是，您也可以在 ACL 中添加规则以拒绝任何在此范围内的来自恶意端口的数据流。请务必将拒绝 规则放在表的较前端，先于开放一系列临时端口的允许 规则。

## A Solutions Architect is designing an Amazon VPC. Applications in the VPC must have private connectivity to Amazon DynamoDB in the same AWS Region. The design should route DynamoDB traffic through:

A. VPC peering connection.
B. NAT gateway
C. VPC endpoint
D. AWS Direct Connect

Answer: C

## A Solutions Architect is architecting a workload that requires a performant object-based storage system that must be shared with multiple Amazon EC2 instances. Which AWS service meets this requirement?

A. Amazon EFS
B. Amazon S3
C. Amazon EBS
D. Amazon ElastiCache

Answer: B

* 分析：这道题给出的答案竟然是A，不明白这个网站是不是专门负责坑人的。object-based storage system，很明显是S3.

## A Solutions Architect is developing a solution for sharing files in an organization. The solution must allow multiple users to access the storage service at once from different virtual machines and scale automatically. It must also support file-level locking. Which storage service meets the requirements of this use case?

A. Amazon S3
B. Amazon EFS
C. Amazon EBS
D. Cached Volumes

Answer: B

## A company runs a legacy application with a single-tier architecture on an Amazon EC2 instance. Disk I/O is low, with occasional small spikes during business hours. The company requires the instance to be stopped from 8 PM to 8 AM daily. Which storage option is MOST appropriate for this workload?

A. Amazon EC2 instance storage
B. Amazon EBS General Purpose SSD (gp2) storage
C. Amazon S3
D. Amazon EBS Provision IOPS SSD (io1) storage

Answer: B

* 分析：原始答案给出的是C，一个legcy application为什么会用S3呢？这可是需要应用改造的。

## (争议)As part of securing an API layer built on Amazon API gateway, a Solutions Architect has to authorize users who are currently authenticated by an existing identity provider. The users must be denied access for a period of one hour after three unsuccessful attempts. How can the Solutions Architect meet these requirements?

A. Use AWS IAM authorization and add least-privileged permissions to each respective IAM role.
B. Use an API Gateway custom authorizer to invoke an AWS Lambda function to validate each user's identity.
C. Use Amazon Cognito user pools to provide built-in user management.
D. Use Amazon Cognito user pools to integrate with external identity providers.

Answer: B

* 分析：正义点在答案D，参考链接：https://serverless-stack.com/chapters/cognito-user-pool-vs-identity-pool.html

## An organization runs an online media site, hosted on-premises. An employee posted a product review that contained videos and pictures. The review went viral and the organization needs to handle the resulting spike in website traffic. What action would provide an immediate solution?

A. Redesign the website to use Amazon API Gateway, and use AWS Lambda to deliver content.
B. Add server instances using Amazon EC2 and use Amazon Route 53 with a failover routing policy.
C. Serve the images and videos via an Amazon CloudFront distribution created using the news site as the origin.
D. Use Amazon ElasticCache for Redis for caching and reducing the load requests from the origin.

Answer: C

## A client notices that their engineers often make mistakes when creating Amazon SQS queues for their backend system. Which action should a Solutions Architect recommend to improve this process?

A. Use the AWS CLI to create queues using AWS IAM Access Keys.
B. Write a script to create the Amazon SQS queue using AWS Lambda.
C. Use AWS Elastic Beanstalk to automatically create the Amazon SQS queues.
D. Use AWS CloudFormation Templates to manage the Amazon SQS queue creation.

Answer: D

* 教程：创建 Amazon SQS 队列(https://docs.aws.amazon.com/zh_cn/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-create-queue.html#create-queue-cloudformation)

## (争议)A development team is building an application with front-end and backend application tiers. Each tier consists of Amazon EC2 instances behind an ELB Classic Load Balancer. The instances run in Auto Scaling groups across multiple Availability Zones. The network team has allocated the 10.0.0.0/24 address space for this application. Only the front-end load balancer should be exposed to the Internet. There are concerns about the limited size of the address space and the ability of each tier to scale. What should the VPC subnet design be in each Availability Zone?

A. One public subnet for the load balancer tier, one public subnet for the front-end tier, and one private subnet for the backend tier.
B. One shared public subnet for all tiers of the application.
C. One public subnet for the load balancer tier and one shared private subnet for the application tiers.
D. One shared private subnet for all tiers of the application.

Answer: C

* 分析：答案给出的是A，但是题目中说道only the front-end load balancer should be exposed to the internet，所以A答案中为front-end tier一个公网subnet有点多余了

## A Solutions Architect must select the storage type for a big data application that requires very high sequential I/O. The data must persist if the instance is stopped. Which of the following storage types will provide the best fit at the LOWEST cost for the application?

A. An Amazon EC2 instance store local SSD volume.
B. An Amazon EBS provisioned IOPS SSD volume.
C. An Amazon EBS throughput optimized HDD volume.
D. An Amazon EBS general purpose SSD volume.

Answer: C

* 分析：这道题需要高顺序I/O和低成本，显然C正确

## Two Auto Scaling applications, Application A and Application B, currently run within a shared set of subnets. A Solutions Architect wants to make sure that Application A can make requests to Application B, but Application B should be denied from making requests to Application A. Which is the SIMPLEST solution to achieve this policy?

A. Using security groups that reference the security groups of the other application
B. Using security groups that reference the application server's IP addresses
C. Using Network Access Control Lists to allow/deny traffic based on application IP addresses
D. Migrating the applications to separate subnets from each other

Answer: A

## Legacy applications currently send messages through a single Amazon EC2 instance, which then routes the messages to the appropriate destinations. The Amazon EC2 instance is a bottleneck and single point of failure, so the company would like to address these issues. Which services could address this architectural use case? (Choose two.)

A. Amazon SNS
B. AWS STS
C. Amazon SQS
D. Amazon Route 53
E. AWS Glue

Answer: AC

* 分析：根据题目是要解决消息的问题，消息服务有两种SNS和SQS，因为题目里并没有说消息模式，所以这两种也许能解决需求。

## A Solutions Architect needs to design an architecture for a new, mission-critical batch processing billing application. The application is required to run Monday, Wednesday, and Friday from 5 AM to 11 AM. Which is the MOST cost-effective Amazon EC2 pricing model?

A. Amazon EC2 Spot Instances
B. On-Demand Amazon EC2 Instances
C. Scheduled Reserved Instances
D. Dedicated Amazon EC2 Instances

Answer: C

## A workload consists of downloading an image from an Amazon S3 bucket, processing the image, and moving it to another Amazon S3 bucket. An Amazon EC2 instance runs a scheduled task every hour to perform the operation. How should a Solutions Architect redesign the process so that it is highly available?

A. Change the Amazon EC2 instance to compute optimized.
B. Launch a second Amazon EC2 instance to monitor the health of the first.
C. Trigger a Lambda function when a new object is uploaded.
D. Initially copy the images to an attached Amazon EBS volume.

Answer: C

* 分析：Lambda的触发器很适合做这个

## An application is running on an Amazon EC2 instance in a private subnet. The application needs to read and write data onto Amazon Kinesis Data Streams, and corporate policy requires that this traffic should not go to the internet. How can these requirements be met?

A. Configure a NAT gateway in a public subnet and route all traffic to Amazon Kinesis through the NAT gateway.
B. Configure a gateway VPC endpoint for Kinesis and route all traffic to Kinesis through the gateway VPC endpoint.
C. Configure an interface VPC endpoint for Kinesis and route all traffic to Kinesis through the gateway VPC endpoint.
D. Configure an AWS Direct Connect private virtual interface for Kinesis and route all traffic to Kinesis through the virtual interface.
 
Answer: C

* 分析：误选了B，从题目说是Kinesis需要读取EC2的数据，所以应该是在VPC interface上建立一个endpoint

## A Solutions Architect is building an application that stores object data. Compliance requirements state that the data stored is immutable. Which service meets these requirements?

A. Amazon S3
B. Amazon Glacier
C. Amazon EFS
D. AWS Storage Gateway

Answer: B

> Data stored in Amazon Glacier is immutable, meaning that after an archive is created it cannot be updated. This ensures that data such as compliance and regulatory records cannot be altered after they have been archived.

* 分析：从这道题我们可以看出，考试的时候选中文的重要性，不会因为一个单词意思不明确导致整个题目判断失误，关键词是immutalbe，不可改变的

## (争议)A Solutions Architect is defining a shared Amazon S3 bucket where corporate applications will save objects. How can the Architect ensure that when an application uploads an object to the Amazon S3 bucket, the object is encrypted?

A. Set a CORS configuration.
B. Set a bucket policy to encrypt all Amazon S3 objects.
C. Enable default encryption on the bucket.
D. Set permission for users.

Answer: B

* 分析：争议点在于答案C，从界面操作上看BC好像是在做同一件事情
* 如何为 Amazon S3 存储桶启用默认加密？(https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/user-guide/default-bucket-encryption.html)
* How to Prevent Uploads of Unencrypted Objects to Amazon S3(https://aws.amazon.com/cn/blogs/security/how-to-prevent-uploads-of-unencrypted-objects-to-amazon-s3/)

## An application tier currently hosts two web services on the same set of instances, listening on different ports. Which AWS service should a Solutions Architect use to route traffic to the service based on the incoming request path?

A. AWS Application Load Balancer
B. Amazon CloudFront
C. Amazon Classic Load Balancer
D. Amazon Route 53

Answer: A

## A data analytics startup company asks a Solutions Architect to recommend an AWS data store options for indexed data. The data processing engine will generate and input more than 64 TB of processed data every day, with item sizes reaching up to 300 KB. The startup is flexible with data storage and is more interested in a database that requires minimal effort to scale with a growing dataset size. Which AWS data store service should the Architect recommend?

A. Amazon RDS
B. Amazon Redshift
C. Amazon DynamoDB
D. Amazon S3

Answer: C

## (争议)A Solutions Architect needs to allow developers to have SSH connectivity to web servers. The requirements are as follows:
✑ Limit access to users origination from the corporate network.
✑ Web servers cannot have SSH access directly from the Internet.
✑ Web servers reside in a private subnet.
Which combination of steps must the Architect complete to meet these requirements? (Choose two.)

A. Create a bastion host that authenticates users against the corporate directory.
B. Create a bastion host with security group rules that only allow traffic from the corporate network.
C. Attach an IAM role to the bastion host with relevant permissions.
D. Configure the web servers' security group to allow SSH traffic from a bastion host.
E. Deny all SSH traffic from the corporate network in the inbound network ACL.

Answer: BD

* 分析：原有答案给出的是AC，感觉并不能完全解决该问题
* How to Record SSH Sessions Established Through a Bastion Host(https://aws.amazon.com/blogs/security/how-to-record-ssh-sessions-established-through-a-bastion-host/)
