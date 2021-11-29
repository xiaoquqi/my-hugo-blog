---
title: '[Digitalcloud.Training]AWS CERTIFIED SOLUTIONS ARCHITECT ASSOCIATE'
date: 2020-01-14 16:49:16
tags: [AWS, ACA Exam]
---

该模拟题出自DigitalCloud Training的模拟题，一共20道题，相对来说答案比较准确，第一次答正确率只有60%，看起来还有不太扎实的知识点，并且英文多了不太爱仔细阅读也是准确率低的原因。

另外，今天在AWS培训官网上看到ACA考试在3月份会推出全新的试题，所以还需要抓紧时间考过。

<!-- more -->

## 答题情况统计

Categories
AWS Analytics 100%
AWS Application Integration 100%
AWS Compute 33.33%
AWS Database 66.67%
AWS Management & Governance 100%
AWS Networking & Content Delivery 33.33%
AWS Security, Identity, & Compliance 50%
AWS Storage 33.33%

## 1. Question
A Solutions Architect has been asked to suggest a solution for analyzing data in S3 using standard SQL queries. The solution should use a serverless technology.
Which AWS service can the Architect use?

A. Amazon RedShift
B. AWS Data Pipeline
C. AWS Glue
D. Amazon Athena

Answer: D

Correct
Explanation:
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run
Amazon RedShift is used for analytics but cannot analyze data in S3
AWS Glue is a fully managed extract, transform, and load (ETL) service that makes it easy for customers to prepare and load their data for analytics. It is not used for analyzing data in S3
AWS Data Pipeline is a web service that helps you reliably process and move data between different AWS compute and storage services, as well as on-premises data sources, at specified intervals

References:
https://aws.amazon.com/athena/

## 2. Question

A systems integration company that helps customers migrate into AWS repeatedly build large, standardized architectures using several AWS services. The Solutions Architects have documented the architectural blueprints for these solutions and are looking for a method of automating the provisioning of the resources.
Which AWS service would satisfy this requirement?

A. AWS OpsWorks
B. AWS CloudFormation
C. AWS CodeDeploy
D. Elastic Beanstalk

Answer: B

Correct
Explanation:
CloudFormation allows you to use a simple text file to model and provision, in an automated and secure manner, all the resources needed for your applications across all regions and accounts
Elastic Beanstalk is a PaaS service that helps you to build and manage web applications
AWS OpsWorks is a configuration management service that helps you build and operate highly dynamic applications, and propagate changes instantly
AWS CodeDeploy is a deployment service that automates application deployments to Amazon EC2 instances, on-premises instances, or serverless Lambda functions

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-cloudformation/

## 3. Question
A data-processing application runs on an i3.large EC2 instance with a single 100 GB EBS gp2 volume. The application stores temporary data in a small database (less than 30 GB) located on the EBS root volume. The application is struggling to process the data fast enough, and a Solutions Architect has determined that the I/O speed of the temporary database is the bottleneck.
What is the MOST cost-efficient way to improve the database response times?

A. Enable EBS optimization on the instance and keep the temporary files on the existing volume
B. Put the temporary database on a new 50-GB EBS gp2 volume
C. Move the temporary database onto instance storage
D. Put the temporary database on a new 50-GB EBS io1 volume with a 3000 IOPS allocation

Answer: C

Incorrect
Explanation:
EC2 Instance Stores are high-speed ephemeral storage that is physically attached to the EC2 instance. The i3.large instance type comes with a single 475GB NVMe SSD instance store so it would be a good way to lower cost and improve performance by using the attached instance store. As the files are temporary, it can be assumed that ephemeral storage (which means the data is lost when the instance is stopped) is sufficient.
Enabling EBS optimization will not lower cost. Also, EBS Optimization is a network traffic optimization, it does not change the I/O speed of the volume.
Moving the DB to a new 50-GB EBS gp2 volume will not result in a performance improvement as you get IOPS allocated per GB so a smaller volume will have lower performance.
Moving the DB to a new 50-GB EBS io1 volume with a 3000 IOPS allocation will improve performance but is more expensive so will not be the most cost-efficient solution.

References:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/amazon-ebs/

## 4. Question

An application you are designing receives and processes files. The files are typically around 4GB in size and the application extracts metadata from the files which typically takes a few seconds for each file. The pattern of updates is highly dynamic with times of little activity and then multiple uploads within a short period of time.
What architecture will address this workload the most cost efficiently?

A. Upload files into an S3 bucket, and use the Amazon S3 event notification to invoke a Lambda function to extract the metadata
B. Place the files in an SQS queue, and use a fleet of EC2 instances to extract the metadata
C. Store the file in an EBS volume which can then be accessed by another EC2 instance for processing
D. Use a Kinesis data stream to store the file, and use Lambda for processing

Answer: A

Correct
Explanation:
Storing the file in an S3 bucket is the most cost-efficient solution, and using S3 event notifications to invoke a Lambda function works well for this unpredictable workload
Kinesis data streams runs on EC2 instances and you must therefore provision some capacity even when the application is not receiving files. This is not as cost-efficient as storing them in an S3 bucket prior to using Lambda for the processing
SQS queues have a maximum message size of 256KB. You can use the extended client library for Java to use pointers to a payload on S3 but the maximum payload size is 2GB
Storing the file in an EBS volume and using EC2 instances for processing is not cost efficient

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-s3/
https://docs.aws.amazon.com/AmazonS3/latest/dev/NotificationHowTo.html

## 5. Question

A Solutions Architect needs to deploy an HTTP/HTTPS service on Amazon EC2 instances that will be placed behind an Elastic Load Balancer. The ELB must support WebSockets.
How can the Architect meet these requirements?

A. Launch an Application Load Balancer (ALB)
B. Launch a Network Load Balancer (NLB)
C. Launch a Classic Load Balancer (CLB)
D. Launch a Layer-4 Load Balancer

Answer: A

Correct
Explanation:
Both the ALB and NLB support WebSockets. However, only the ALB supports HTTP/HTTPS listeners. The NLB only supports TCP, TLS, UDP, TCP_UDP.
The CLB does not support WebSockets.
A “Layer-4 Load Balancer” is not suitable, we need a layer 7 load balancer for HTTP/HTTPS.

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/
https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html
https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html

## 6. Question
You are building an application that will collect information about user behavior. The application will rapidly ingest large amounts of dynamic data and requires very low latency. The database must be scalable without incurring downtime. Which database would you recommend for this scenario?

A. RDS with Microsoft SQL
B. RedShift
C. DynamoDB
D. RDS with MySQL

Answer: C

Correct
Explanation:
Amazon Dynamo DB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability
Push button scaling means that you can scale the DB at any time without incurring downtime
DynamoDB provides low read and write latency
RDS uses EC2 instances so you have to change your instance type/size in order to scale compute vertically
RedShift uses EC2 instances as well, so you need to choose your instance type/size for scaling compute vertically, but you can also scale horizontally by adding more nodes to the cluster
Rapid ingestion of dynamic data is not an ideal use case for RDS or RedShift

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-dynamodb/

## 7. Question

You are running an Auto Scaling Group (ASG) with an Elastic Load Balancer (ELB) and a fleet of EC2 instances. Health checks are configured on the ASG to use EC2 status checks. The ELB has determined that an EC2 instance is unhealthy and has removed it from service. However, you noticed that the instance is still running and has not been terminated by the ASG.
What would be an explanation for this behavior?

A. The health check grace period has not yet expired
B. The ELB health check type has not been selected for the ASG and so it is unaware that the instance has been determined to be unhealthy by the ELB and has been removed from service
C. Connection draining is enabled and the ASG is waiting for in-flight requests to complete
D. The ASG is waiting for the cooldown timer to expire before terminating the instance

Answer: B

Incorrect
Explanation:
If using an ELB it is best to enable ELB health checks as otherwise EC2 status checks may show an instance as being healthy that the ELB has determined is unhealthy. In this case the instance will be removed from service by the ELB but will not be terminated by Auto Scaling
Connection draining is not the correct answer as the ELB has taken the instance out of service so there are no active connections
The health check grace period allows a period of time for a new instance to warm up before performing a health check
More information on ASG health checks:
By default uses EC2 status checks
Can also use ELB health checks and custom health checks
ELB health checks are in addition to the EC2 status checks
If any health check returns an unhealthy status the instance will be terminated
With ELB an instance is marked as unhealthy if ELB reports it as OutOfService
A healthy instance enters the InService state
If an instance is marked as unhealthy it will be scheduled for replacement
If connection draining is enabled, Auto Scaling waits for in-flight requests to complete or timeout before terminating instances
The health check grace period allows a period of time for a new instance to warm up before performing a health check (300 seconds by default)

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/aws-auto-scaling/

## 8. Question
A solutions Architect is designing a new workload where an AWS Lambda function will access an Amazon DynamoDB table.
What is the MOST secure means of granting the Lambda function access to the DynamoDB table?

A. Create an identity and access management (IAM) role allowing access from AWS Lambda and assign the role to the DynamoDB table
B. Create an identity and access management (IAM) role with the necessary permissions to access the DynamoDB table, and assign the role to the Lambda function
C. Create a DynamoDB username and password and give them to the Developer to use in the Lambda function
D. Create an identity and access management (IAM) user and create access and secret keys for the user. Give the user the necessary permissions to access the DynamoDB table. Have the Developer use these keys to access the resources

Answer: B

Correct
Explanation:
The most secure method is to use an IAM role so you don’t need to embed any credentials in code and can tightly control the services that your Lambda function can access. You need to assign the role to the Lambda function, NOT to the DynamoDB table
You should not provide a username and password to the Developer to use with the function. This is insecure – always avoid using credentials in code!
You should not use an access key and secret ID to access DynamoDB. Again, this means embedding credentials in code which should be avoided.

References:
https://aws.amazon.com/blogs/security/how-to-create-an-aws-iam-policy-to-grant-aws-lambda-access-to-an-amazon-dynamodb-table/

## 9. Question

Your company has offices in several locations around the world. Each office utilizes resources deployed in the geographically closest AWS region. You would like to implement connectivity between all of the VPCs so that you can provide full access to each other’s resources. As you are security conscious you would like to ensure the traffic is encrypted and does not traverse the public Internet. The topology should be many-to-many to enable all VPCs to access the resources in all other VPCs.
How can you successfully implement this connectivity using only AWS services? (choose 2)

A. Use inter-region VPC peering
B. Use software VPN appliances running on EC2 instances
C. Use VPC endpoints between VPCs
D. Implement a fully meshed architecture
E. Implement a hub and spoke architecture

Answer: AD

Incorrect
Explanation:
Peering connections can be created with VPCs in different regions (available in most regions now)
Data sent between VPCs in different regions is encrypted (traffic charges apply)
You cannot do transitive peering so a hub and spoke architecture would not allow all VPCs to communicate directly with each other. For this you need to establish a mesh topology
A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC endpoint services, it does not provide full VPC to VPC connectivity
Using software VPN appliances to connect VPCs together is not the best solution as it is cumbersome, expensive and would introduce bandwidth and latency constraints (amongst other problems)

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

## 10. Question

A research company is developing a data lake solution in Amazon S3 to analyze huge datasets. The solution makes infrequent SQL queries only. In addition, the company wants to minimize infrastructure costs.
Which AWS service should be used to meet these requirements?

A. Amazon Athena
B. Amazon Redshift Spectrum
C. Amazon Aurora
D. Amazon RDS for MySQL

Answer: A

Correct
Explanation:
Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run – this satisfies the requirement to minimize infrastructure costs for infrequent queries.
Amazon RedShift Spectrum is a feature of Amazon Redshift that enables you to run queries against exabytes of unstructured data in Amazon S3, with no loading or ETL required. However, RedShift nodes run on EC2 instances, so for infrequent queries this will not minimize infrastructure costs.
Amazon RDS and Aurora are not suitable solutions for analyzing datasets on S3 – these are both relational databases typically used for transactional (not analytical) workloads.

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-athena/
https://docs.aws.amazon.com/athena/latest/ug/what-is.html

## 11. Question

An Architect is designing a serverless application that will accept images uploaded by users from around the world. The application will make API calls to back-end services and save the session state data of the user to a database.
Which combination of services would provide a solution that is cost-effective while delivering the least latency?

A. Amazon CloudFront, API Gateway, Amazon S3, AWS Lambda, DynamoDB
B. Amazon S3, API Gateway, AWS Lambda, Amazon RDS
C. API Gateway, Amazon S3, AWS Lambda, DynamoDB
D. Amazon CloudFront, API Gateway, Amazon S3, AWS Lambda, Amazon RDS

Answer: A

Incorrect
Explanation:
Amazon CloudFront caches content closer to users at Edge locations around the world. This is the lowest latency option for uploading content. API Gateway and AWS Lambda are present in all options. DynamoDB can be used for storing session state data
The option that presents API Gateway first does not offer a front-end for users to upload content to
Amazon RDS is not a serverless service so this option can be ruled out
Amazon S3 alone will not provide the least latency for users around the world unless you have many buckets in different regions and a way of directing users to the closest bucket (such as Route 3 latency based routing). However, you would then need to manage replicating the data

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-cloudfront/
https://aws.amazon.com/blogs/aws/amazon-cloudfront-content-uploads-post-put-other-methods/

## 12. Question

A training provider hosts a website using Amazon API Gateway on the front end. Recently, there has been heavy traffic on the website and the company wants to control access by allowing authenticated traffic from paying students only.
How should the company limit access to authenticated users only? (choose 2)

A. Deploy AWS KMS to identify users
B. Allow X.509 certificates to authenticate traffic
C. Assign permissions in AWS IAM to allow users
D. Limit traffic through API Gateway
E. Allow users that are authenticated through Amazon Cognito

Answer: CE
Incorrect
Explanation:

API Gateway supports multiple mechanisms for controlling and managing access to your API. These include resource policies, standard IAM roles and policies, Lambda authorizers, and Amazon Cognito user pools.
Amazon Cognito user pools let you create customizable authentication and authorization solutions for your REST APIs. Amazon Cognito user pools are used to control who can invoke REST API methods.
IAM roles and policies offer flexible and robust access controls that can be applied to an entire API or individual methods. IAM roles and policies can be used for controlling who can create and manage your APIs as well as who can invoke them.
Limiting traffic through the API Gateway will not filter authenticated traffic, it will just limit overall invocations. This may prevent users from connecting who have a legitimate need.
X.509 certificates are not a method of authentication you can use with API Gateway.
AWS KMS is used for key management not user identification.

References:
https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-api-gateway/

## 13. Question

An Auto Scaling Group is unable to respond quickly enough to load changes resulting in lost messages from another application tier. The messages are typically around 128KB in size.
What is the best design option to prevent the messages from being lost?

A. Launch an Elastic Load Balancer
B. Store the messages on Amazon S3
C. Use larger EC2 instance sizes
D. Store the messages on an SQS queue

Answer: D

Correct
Explanation:
In this circumstance the ASG cannot launch EC2 instances fast enough. You need to be able to store the messages somewhere so they don’t get lost whilst the EC2 instances are launched. This is a classic use case for decoupling and SQS is designed for exactly this purpose
Amazon Simple Queue Service (Amazon SQS) is a web service that gives you access to message queues that store messages waiting to be processed. SQS offers a reliable, highly-scalable, hosted queue for storing messages in transit between computers. An SQS queue can be used to create distributed/decoupled applications
Storing the messages on S3 is potentially feasible but SQS is the preferred solution as it is designed for decoupling. If the messages are over 256KB and therefore cannot be stored in SQS, you may want to consider using S3 and it can be used in combination with SQS by using the Amazon SQS Extended Client Library for Java
An ELB can help to distribute incoming connections to the back-end EC2 instances however if the ASG is not scaling fast enough then there aren’t enough resources for the ELB to distributed traffic to

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/application-integration/amazon-sqs/

## 14. Question

Your company would like to restrict the ability of most users to change their own passwords whilst continuing to allow a select group of users within specific user groups.
What is the best way to achieve this? (choose 2)

A. Under the IAM Password Policy deselect the option to allow users to change their own passwords
B. Create an IAM Policy that grants users the ability to change their own password and attach it to the individual user accounts
C. Create an IAM Policy that grants users the ability to change their own password and attach it to the groups that contain the users
D. Create an IAM Role that grants users the ability to change their own password and attach it to the groups that contain the users
E. Disable the ability for all users to change their own passwords using the AWS Security Token Service

Answer:AC

Incorrect
Explanation:
A password policy can be defined for enforcing password length, complexity etc. (applies to all users)
You can allow or disallow the ability to change passwords using an IAM policy and you should attach this to the group that contains the users, not to the individual users themselves
You cannot use an IAM role to perform this function
The AWS STS is not used for controlling password policies

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/security-identity-compliance/aws-iam/

## 15. Question
A Solutions Architect has created a VPC design that meets the security requirements of their organization. Any new applications that are deployed must use this VPC design.
How can project teams deploy, manage, and delete VPCs that meet this design with the LEAST administrative effort?

A. Deploy an AWS CloudFormation template that defines components of the VPC
B. Use AWS Elastic Beanstalk to deploy both the VPC and the application
C. Clone the existing authorized VPC for each new project
D. Run a script that uses the AWS Command Line interface to deploy the VPC

Answer: A

Correct
Explanation:
CloudFormation allows you to define your infrastructure through code and securely and repeatably deploy the infrastructure with minimal administrative effort. This is a perfect use case for CloudFormation.
You can use a script to create the VPCs using the AWS CLI however this would be a lot more work to create and manage the scripts.
You cannot clone VPCs.
You cannot deploy the VPC through Elastic Beanstalk – you need to deploy the VPC first and then deploy your application using Beanstalk.

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/management-tools/aws-cloudformation/
https://aws.amazon.com/cloudformation/

## 16. Question
Your organization has a data lake on S3 and you need to find a solution for performing in-place queries of the data assets in the data lake. The requirement is to perform both data discovery and SQL querying, and complex queries from a large number of concurrent users using BI tools.
What is the BEST combination of AWS services to use in this situation? (choose 2)

A. AWS Glue for the ad hoc SQL querying
B. AWS Lambda for the complex queries
C. RedShift Spectrum for the complex queries
D. Amazon Athena for the ad hoc SQL querying

Answer: CD

Incorrect
Explanation:
Performing in-place queries on a data lake allows you to run sophisticated analytics queries directly on the data in S3 without having to load it into a data warehouse
You can use both Athena and Redshift Spectrum against the same data assets. You would typically use Athena for ad hoc data discovery and SQL querying, and then use Redshift Spectrum for more complex queries and scenarios where a large number of data lake users want to run concurrent BI and reporting workloads
AWS Lambda is a serverless technology for running functions, it is not the best solution for running analytics queries
AWS Glue is an ETL service

References:
https://docs.aws.amazon.com/aws-technical-content/latest/building-data-lakes/in-place-querying.html
https://aws.amazon.com/redshift/
https://aws.amazon.com/athena/

## 17. Question
You have recently enabled Access Logs on your Application Load Balancer (ALB). One of your colleagues would like to process the log files using a hosted Hadoop service. What configuration changes and services can be leveraged to deliver this requirement?

A. Configure Access Logs to be delivered to DynamoDB and use EMR for processing the log files
B. Configure Access Logs to be delivered to S3 and use Kinesis for processing the log files
C. Configure Access Logs to be delivered to S3 and use EMR for processing the log files
D. Configure Access Logs to be delivered to EC2 and install Hadoop for processing the log files

Answer: C

Correct
Explanation:
Access Logs can be enabled on ALB and configured to store data in an S3 bucket. Amazon EMR is a web service that enables businesses, researchers, data analysts, and developers to easily and cost-effectively process vast amounts of data. EMR utilizes a hosted Hadoop framework running on Amazon EC2 and Amazon S3
Neither Kinesis or EC2 provide a hosted Hadoop service
You cannot configure access logs to be delivered to DynamoDB

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/analytics/amazon-emr/
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/compute/elastic-load-balancing/

## 18. Question
A company is deploying a big data and analytics workload. The analytics will be run from a fleet of thousands of EC2 instances across multiple AZs. Data needs to be stored on a shared storage layer that can be mounted and accessed concurrently by all EC2 instances. Latency is not a concern however extremely high throughput is required.
What storage layer would be most suitable for this requirement?

A. Amazon EFS in General Purpose mode
B. Amazon EFS in Max I/O mode
C. Amazon S3
D. Amazon EBS PIOPS

Answer: B

Correct
Explanation:
Amazon EFS file systems in the Max I/O mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for file operations
Amazon S3 is not a storage layer that can be mounted and accessed concurrently
Amazon EBS volumes cannot be shared between instances

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/storage/amazon-efs/
https://docs.aws.amazon.com/efs/latest/ug/performance.html

## 19. Question
An application launched on Amazon EC2 instances needs to publish personally identifiable information (PII) about customers using Amazon SNS. The application is launched in private subnets within an Amazon VPC.
Which is the MOST secure way to allow the application to access service endpoints in the same region?

A. Use a proxy instance
B. Use a NAT gateway
C. Use AWS PrivateLink
D. Use an Internet Gateway

Answer: C

Correct
Explanation:
To publish messages to Amazon SNS topics from an Amazon VPC, create an interface VPC endpoint. Then, you can publish messages to SNS topics while keeping the traffic within the network that you manage with the VPC. This is the most secure option as traffic does not need to traverse the Internet.
Internet Gateways are used by instances in public subnets to access the Internet and this is less secure than an VPC endpoint.
A NAT Gateway is used by instances in private subnets to access the Internet and this is less secure than an VPC endpoint.
A proxy instance will also use the public Internet and so is less secure than a VPC endpoint.

References:
https://docs.aws.amazon.com/sns/latest/dg/sns-vpc-endpoint.html
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/networking-and-content-delivery/amazon-vpc/

## 20. Question
A retail organization is deploying a new application that will read and write data to a database. The company wants to deploy the application in three different AWS Regions in an active-active configuration. The databases need to replicate to keep information in sync.
Which solution best meets these requirements?

A. Amazon Aurora Global Database
B. Amazon DynamoDB with global tables
C. Amazon Athena with Amazon S3 cross-region replication
D. AWS Database Migration Service with change data capture

Answer: B

Incorrect
Explanation:
Amazon DynamoDB global tables provide a fully managed solution for deploying a multi-region, multi-master database. This is the only solution presented that provides an active-active configuration where reads and writes can take place in multiple regions with full bi-directional synchronization.
Amazon Athena with S3 cross-region replication is not suitable. This is not a solution that provides a transactional database solution (Athena is used for analytics), or active-active synchronization.
Amazon Aurora Global Database provides read access to a database in multiple regions – it does not provide active-active configuration with bi-directional synchronization (though you can failover to your read-only DBs and promote them to writable).

References:
https://digitalcloud.training/certification-training/aws-solutions-architect-associate/database/amazon-dynamodb/
https://aws.amazon.com/blogs/database/how-to-use-amazon-dynamodb-global-tables-to-power-multiregion-architectures/
