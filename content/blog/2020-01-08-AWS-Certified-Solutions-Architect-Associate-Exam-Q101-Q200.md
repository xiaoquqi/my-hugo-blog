---
title: AWS Certified Solutions Architect - Associate Exam(Q101-Q200)
date: 2022-03-08 15:36:23
tags: [AWS, ACA Exam]
---

通过之前100道题的梳理，发现这个网站竟然有这么多争议的题目，我觉得有可能是有些题目已经跟不上AWS自身发展速度了，有了更多的方法。总之，通过这些题目的梳理，对AWS服务细节层面有了更多的了解，希望能够一次性通过ACA考试。这篇继续这个网站101到200题的学习工作，希望能提高点速度。

<!-- more -->

## (争议)A Solutions Architect needs to use AWS to implement pilot light disaster recovery for a three-tier web application hosted in an on-premises datacenter. Which solution allows rapid provision of working, fully-scaled production environment?

A. Continuously replicate the production database server to Amazon RDS. Use AWS CloudFormation to deploy the application and any additional servers if necessary.
B. Continuously replicate the production database server to Amazon RDS. Create one application load balancer and register on-premises servers. Configure ELB Application Load Balancer to automatically deploy Amazon EC2 instances for application and additional servers if the on-premises application is down.
C. Use a scheduled Lambda function to replicate the production database to AWS. Use Amazon Route 53 health checks to deploy the application automatically to Amazon S3 if production is unhealthy.
D. Use a scheduled Lambda function to replicate the production database to AWS. Register on-premises servers to an Auto Scaling group and deploy the application and additional servers if production is unavailable.

Answer: B

* 分析：有人说答案是A，因为题目中的这个词pilot light(A pilot light is a small gas flame)，准确的翻译没查到，从字面理解应该就是简单轻量级的意思。A选项的方式是当出现灾难时，使用CloudFormation进行除数据库外的重建。所以很多人认为这种方式更符合题目的要求。但是从B选项看，更符合一个容灾的场景，当发生灾难时，通过B中的配置，可以做到马上接管的效果，比A选项更像是一个容灾的解决方案。

## A Solutions Architect notices slower response times from an application. The CloudWatch metrics on the MySQL RDS indicate Read IOPS are high and fluctuate significantly when the database is under load. How should the database environment be re-designed to resolve the IOPS fluctuation?

A. Change the RDS instance type to get more RAM.
B. Change the storage type to Provisioned IOPS.
C. Scale the web server tier horizontally.
D. Split the DB layer into separate RDS instances.

Answer: B

## A Solutions Architect is designing a solution that can monitor memory and disk space utilization of all Amazon EC2 instances running Amazon Linux and
Windows. Which solution meets this requirement?

A. Default Amazon CloudWatch metrics.
B. Custom Amazon CloudWatch metrics.
C. Amazon Inspector resource monitoring.
D. Default monitoring of Amazon EC2 instances.

Answer: B

* 分析：这道题又是原网站给出的错题，原来给出的答案是A。我曾经对AWS两个行为比较纳闷：一个是为什么没有VNC，另外一个是为什么不提供内存监控，直到又一次和AWS的架构师聊才理解了AWS的良苦用心。AWS始终把用户安全放在第一位，但凡用户的东西我是坚决不能碰的，而无论是VNC还是内存监控无疑与这一原则相违背的。所以内存不可能是默认监控的范畴，必须通过custom脚本完成，同样磁盘利用率也是类似的方式。

## A Solutions Architect is creating a new relational database. The Compliance team will use the database, and mandates that data content must be stored across three different Availability Zones. Which of the following options should the Architect Use?

A. Amazon Aurora
B. Amazon RDS MySQL with Multi-AZ enabled
C. Amazon DynamoDB
D. Amazon ElastiCache

Answer: A

> 问：Amazon Aurora 如何提高我的数据库对磁盘故障的容错能力？
>
> Amazon Aurora 会将您的数据库卷分成分散在很多个磁盘上的 10GB 的区段。每 10GB 的数据库卷组块都能在三个可用区间用六种方法进行复制。Amazon Aurora 的设计可透明应对多达两个数据副本的损失，而不会影响数据库写入可用性，还能在不影响读取可用性的情况下应对多达三个副本。Amazon Aurora 存储还具有自我修复能力。可连续扫描数据块和磁盘有无出错并自动修复之。

## A company needs to quickly ensure that all files created in an Amazon S3 bucket in us-east-1 are also available in another bucket in ap-southeast-2. Which option represents the SIMPLIEST way to implement this design?

A. Add an S3 lifecycle rule to move any files from the bucket in us-east-1 to the bucket in ap-southeast-2.
B. Create a Lambda function to be triggered for every new file in us-east-1 that copies the file to the bucket in ap-southeast-2.
C. Use SNS to notify the bucket in ap-southeast-2 to create a file whenever the file is created in the bucket in us-east-1.
D. Enable versioning and configure cross-region replication from the bucket in us-east-1 to the bucket in ap-southeast-2.

Answer: D

* 分析：这道题要求的是最简单的方法，B理论上是可以的，但是与D相比过于复杂。

## An organization has a long-running image processing application that runs on Spot Instances that will be terminated when interrupted. A highly available workload must be designed to respond to Spot Instance interruption notices. The solution must include a two-minute warning when there is not enough capacity. How can these requirements be met?

A. Use Amazon CloudWatch Events to invoke an AWS Lambda function that can launch On-Demand Instances.
B. Regularly store data from the application on Amazon DynamoDB. Increase the maximum number of instances in the AWS Auto Scaling group.
C. Manually place a bid for additional Spot Instances at a higher price in the same AWS Region and Availability Zone.
D. Ensure that the Amazon Machine Image associated with the application has the latest configurations for the launch configuration.

Answer: A

* Taking Advantage of Amazon EC2 Spot Instance Interruption Notices(https://aws.amazon.com/cn/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/)
> In January 2018, the Spot Instance interruption notice also became available as an event in Amazon CloudWatch Events. This allows targets such as AWS Lambda functions or Amazon SNS topics to process Spot Instance interruption notices by creating a CloudWatch Events rule to monitor for the notice.

* 分析：网站给出的答案是B，但是这道题目考察的应该是合理利用Spot Instance的通知是这道题目的关键，"must include a two-minute warning" => Need CloudWatch

## A company has an Amazon RDS-managed online transaction processing system that has very heavy read and write. The Solutions Architect notices throughput issues with the system. How can the responsiveness of the primary database be improved?

A. (争议)Use asynchronous replication for standby to maximize throughput during peak demand.
B. Offload SELECT queries that can tolerate stale data to READ replica.
C. Offload SELECT and UPDATE queries to READ replica.
D. Offload SELECT query that needs the most current data to READ replica.

Answer: B

* 分析：原网站给出的答案是A，大部分反对的理由是RDS之间的复制是同步的并不是异步的。

## A company is designing a failover strategy in Amazon Route 53 for its resources between two AWS Regions. The company must have the ability to route a user's traffic to the region with least latency, and if both regions are healthy, Route 53 should route traffic to resources in both regions. Which strategy should the Solutions Architect recommend?

A. Configure active-active failover using Route 53 latency DNS records.
B. Configure active-passive failover using Route 53 latency DNS records.
C. Configure active-active failover using Route 53 failover DNS records.
D. Configure active-passive failover using Route 53 failover DNS records.

Answer: A

* 分析：这道题很明显是需要AA模式的，with least latency，所以需要latency。

> Active-Active Failover
> Use this failover configuration when you want all of your resources to be available the majority of the time. When a resource becomes unavailable, Route 53 can detect that it's unhealthy and stop including it when responding to queries.
>
> In active-active failover, all the records that have the same name, the same type (such as A or AAAA), and the same routing policy (such as weighted or latency) are active unless Route 53 considers them unhealthy. Route 53 can respond to a DNS query using any healthy record.

## A company is developing several critical long-running applications hosted on Docker. How should a Solutions Architect design a solution to meet the scalability and orchestration requirements on AWS?

A. Use Amazon ECS and Service Auto Scaling.
B. Use Spot Instances for orchestration and for scaling containers on existing Amazon EC2 instances.
C. Use AWS OpsWorks to launch containers in new Amazon EC2 instances.
D. Use Auto Scaling groups to launch containers on existing Amazon EC2 instances.

Answer: A

> Amazon Elastic Container Service (Amazon ECS) 是用于在可扩展群集上运行 Docker 应用程序的 Amazon Web Service。在本教程中，您将了解如何在负载均衡器后面的 Amazon ECS 集群上运行支持 Docker 的示例应用程序，对该示例应用程序进行测试，然后删除您的资源以免产生费用。

## (争议)A Solutions Architect is developing a new web application on AWS. The Architect expects the application to become very popular, so the application must scale to support the load. The Architect wants to focus on software development and deploying new features without provisioning or managing instances. What solution is appropriate?

A. Amazon API Gateway and AWS Lambda
B. Elastic Load Balancing with Auto Scaling groups and Amazon EC2
C. Amazon API Gateway and Amazon EC2
D. Amazon CloudFront and AWS Lambda

Answer: A

* 分析：题目的需求是：1、不想运维；2、集中精力去做开发。这是非常典型的Serverless的需求，将底层交给云原生服务，专注于业务开发。首先应该选择AWS Lambda服务，则AD作为选项。原答案给出的是D，但是CloudFront作为CDN服务，好像并没有向外提供接口的能力，AWS Lambda服务并不像阿里的函数计算提供了Http trigger，所以无法对外提供API接口的能力，从这个角度看A更合理一些。

## A Solutions Architect is deploying a new production MySQL database on AWS. It is critical that the database is highly available. What should the Architect do to achieve this goal with Amazon RDS?

A. Create a read replica of the primary database and deploy it in a different AWS Region.
B. Enable multi-AZ to create a standby database in a different Availability Zone.
C. Enable multi-AZ to create a standby database in a different AWS Region.
D. Create a read replica of the primary database and deploy it in a different Availability Zone.

Answer: B

* 分析：原题目给出的是A，但是B明显是正确答案。

> https://aws.amazon.com/cn/rds/ha/?nc1=h_ls
> Amazon Relational Database Service (Amazon RDS) supports two easy-to-use options for ensuring High Availability of your relational database.
> For your MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server database (DB) instances, you can use Amazon RDS Multi-AZ deployments. When you provision a Multi-AZ DB instance, Amazon RDS automatically creates a primary DB instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby DB instance. Since the endpoint for your DB instance remains the same after a failover, your application can resume database operation without the need for manual administrative intervention. Learn more >>

## An organization designs a mobile application for their customers to upload photos to a site. The application needs a secure login with MFA. The organization wants to limit the initial build time and maintenance of the solution. Which solution should a Solutions Architect recommend to meet the requirements?

A. Use Amazon Cognito Identity with SMS-based MFA.
B. Edit AWS IAM policies to require MFA for all users.
C. Federate IAM against corporate AD that requires MFA.
D. Use Amazon API Gateway and require SSE for photos.

Answer: A

## (争议)A Solutions Architect is designing a solution to monitor weather changes by the minute. The frontend application is hosted on Amazon EC2 instances. The backend must be scalable to a virtually unlimited size, and data retrieval must occur with minimal latency. Which AWS service should the Architect use to store the data and achieve these requirements?

A. Amazon S3
B. Amazon DynamoDB
C. Amazon RDS
D. Amazon EBS

Answer: A

* 分析：这道题很多人都认为B是正确的，但是从篇气象公司最佳实践看，确实采用的是S3方案。

> AWS Case Study: The Weather Company(https://aws.amazon.com/cn/solutions/case-studies/the-weather-company/)
> The platform ingests information from more than 100 different sources and generates close to one-half terabyte (TB) of data each time it updates. The information is mapped and processed into forecast points that can be retrieved in real time, based on queries coming into the system. All data is stored in Amazon Simple Storage Service (Amazon S3), leveraging the efficiency of cloud storage as opposed to an on-premises storage solution and eliminating the hassle of managing a storage platform.

## A company hosts a website on premises. The website has a mix of static and dynamic content, but users experience latency when loading static files. Which AWS service can help reduce latency?

A. Amazon CloudFront with on-premises servers as the origin
B. ELB Application Load Balancer
C. Amazon Route 53 latency-based routing
D. Amazon EFS to store and server static files

Answer: A

## A company wants to analyze all of its sales information aggregated over the last 12 months. The company expects there to be over 10TB of data from multiple sources. What service should be used?

A. Amazon DynamoDB
B. Amazon Aurora MySQL
C. Amazon RDS MySQL
D. Amazon Redshift

Answer: D

## A media company has deployed a multi-tier architecture on AWS. Web servers are deployed in two Availability Zones using an Auto Scaling group with a default Auto Scaling termination policy. The web servers' Auto Scaling group currently has 15 instances running. Which instance will be terminated first during a scale-in operation?

A. The instance with the oldest launch configuration.
B. The instance in the Availability Zone that has most instances.
C. The instance closest to the next billing hour.
D. The oldest instance in the group.

Answer: B

* 控制在缩小过程中终止哪些 Auto Scaling 实例(https://docs.aws.amazon.com/zh_cn/autoscaling/ec2/userguide/as-instance-termination.html#default-termination-policy)

> 当达到缩减策略的阈值时，策略生效，Auto Scaling 组终止其中一个实例。如果您没有为该组分配特定的终止策略，则使用默认终止策略。它选择有两个实例的可用区，并终止从最旧启动配置启动的实例。如果这些实例是从同一启动配置启动的，则 Auto Scaling 组选择最接近下一个计费小时的实例并终止该实例。

## A retail company has sensors placed in its physical retail stores. The sensors send messages over HTTP when customers interact with in-store product displays. A Solutions Architect needs to implement a system for processing those sensor messages; the results must be available for the Data Analysis team. Which architecture should be used to meet these requirements?

A. Implement an Amazon API Gateway to server as the HTTP endpoint. Have the API Gateway trigger an AWS Lambda function to process the messages, and save the results to an Amazon DynamoDB table.
B. Create an Amazon EC2 instance to server as the HTTP endpoint and to process the messages. Save the results to Amazon S3 for the Data Analysis team to download.
C. Use Amazon Route 53 to direct incoming sensor messages to a Lambda function to process the message and save the results to a Amazon DynamoDB table.
D. Use AWS Direct Connect to connect sensors to DynamoDB so that data can be written directly to a DynamoDB table where it can be accessed by the Data Analysis team.

Answer: A

* 分析：原来AWS Lambda的HTTP trigger是这么实现的

## A client is migrating a legacy web application to the AWS Cloud. The current system uses an Oracle database as a relational database management system solution. Backups occur every night, and the data is stored on-premises. The Solutions Architect must automate the backups and identity a storage solution while keeping costs low. Which AWS service will meet these requirements?

A. Amazon RDS
B. Amazon RedShift
C. Amazon DynamoDB Accelerator
D. Amazon ElastiCache

Answer: A

## (争议)A company has an Amazon RDS database backing its production website. The Sales team needs to run queries against the database to track training program effectiveness. Queries against the production database cannot impact performance, and the solution must be easy to maintain. How can these requirements be met?

A. Use an Amazon Redshift database. Copy the product database into Redshift and allow the team to query it.
B. Use an Amazon RDS read replica of the production database and allow the team to query against it.
C. Use multiple Amazon EC2 instances running replicas of the production database, placed behind a load balancer.
D. Use an Amazon DynamoDB table to store a copy of the data.

Answer: B

* 争议：原有答案给出的是A，根据题目描述看起来是一个数据仓库的需求。从easy to maintain的角度说B，更简单

## A company must collect temperature data from thousands of remote weather devices. The company must also store this data in a data warehouse to run aggregations and visualizations. Which services will meet these requirements? (Choose two.)

A. Amazon Kinesis Data Firehouse
B. Amazon SQS
C. Amazon Redshift
D. Amazon SNS
E. Amazon DynamoDB

Answer: AC

* 分析：A负责接收数据并处理，C作为数据仓库存储下来
