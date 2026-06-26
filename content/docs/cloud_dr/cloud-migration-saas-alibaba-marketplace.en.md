---
title: How a Cloud Migration SaaS Product Joins the Alibaba Cloud Marketplace
slug: how-to-join-cloud-migration-saas-into-aliyun-marketplace
aliases:
  - /2021/12/01/%E4%BA%91%E8%BF%81%E7%A7%BBsaas%E5%A6%82%E4%BD%95%E5%85%A5%E9%A9%BB%E9%98%BF%E9%87%8C%E4%BA%91%E5%B7%A5%E5%85%B7%E5%BA%94%E7%94%A8%E5%B8%82%E5%9C%BA/
date: 2021-12-01T09:08:17+08:00
draft: false
author: Ray Sun
tags:
  - Alibaba Cloud
  - HyperMotion
  - Cloud Migration
  - Cloud Disaster Recovery
---

HyperMotion SaaS is a cloud migration and cloud DR SaaS platform developed under the Cloud Native philosophy. In July 2020, the HyperMotion migration version officially joined the Alibaba Cloud Marketplace. After logging in to Alibaba Cloud, users can use the product directly in SaaS mode without having to launch an instance from the cloud marketplace. Because the system is fully integrated with Alibaba Cloud's user management, RAM authorization, and payment systems, the user experience is far more seamless. Thanks to Alibaba Cloud's traffic advantage, HyperMotion SaaS accumulated nearly 400 customers through organic traffic alone in its first year on the marketplace — with no special promotion or marketing campaigns. The Alibaba Cloud Marketplace is undoubtedly the best embodiment of Alibaba Cloud's "be integrated" philosophy, providing fertile ground for IaaS SaaS software. This article shares the complete process of joining the Alibaba Cloud Marketplace from a technical perspective.

<!-- more -->

## User Experience

### How It Feels to Use

Let's first look at how users interact with the product after it joins the Alibaba Cloud Marketplace.

![2021-12-01-10-53-53](/images/2021-12-01-10-53-53.png)

Users enter the product without any installation and go directly into the usage workflow.

![2021-12-01-11-03-51](/images/2021-12-01-11-03-51.png)

### Purchase Flow

Because the system is fully integrated with Alibaba Cloud's payment system, users can pay for and purchase the product directly.

![2021-12-01-11-18-07](/images/2021-12-01-11-18-07.png)

### Permission Provisioning

When users purchase the product, Alibaba Cloud pre-configures all the RAM permissions required for the product during use, according to the application's requirements. This reduces the configuration burden on the customer and delivers a true out-of-the-box experience.

## Value of Joining the Marketplace

So why join the Alibaba Cloud Marketplace, and how does it benefit the business?

### Advantage 1: Market Value

Whether for cloud migration or cloud DR products, our development has always been guided by the Cloud Native philosophy, and having these two products deeply integrated with a cloud platform has been the biggest goal of the entire team. We had previously tried communicating in depth with Alibaba Cloud through multiple channels, but for various reasons those efforts never led anywhere. The Alibaba Cloud Marketplace model happened to be exactly what we needed. At the same time, having our product recognized by Alibaba Cloud and successfully joining the marketplace is the greatest recognition and endorsement for both the company and the R&D team.

### Advantage 2: Customer Traffic

The Alibaba Cloud console is a massive traffic entrance, and the traffic includes a large proportion of valuable enterprise users. Securing a visible presence in the console in this way is without question a huge channel for product promotion. We are soon to formally release our Cloud Native DR platform, which will also join the Alibaba Cloud Marketplace. We look forward to collaborating with more of Alibaba Cloud's business teams to jointly promote our products and win the trust of more customers.

### Advantage 3: Streamlining the Procurement Process

In the enterprise market, procurement is often an extremely cumbersome process. By fully integrating with Alibaba Cloud's payment workflow, we save enterprises their procurement overhead and enable business teams to make and execute decisions more quickly. The following is a comparison between the traditional procurement flow and the Alibaba Cloud Marketplace procurement flow:

![2021-12-01-14-37-06](/images/2021-12-01-14-37-06.png)

## Key Timeline and Costs

We began initial conversations with the Alibaba Cloud Marketplace team in February 2020. In March, we held separate discussions with the relevant architecture and security teams to plan the early-stage architecture, reviewed the front-end development and API development specifications, and provided a test environment for subsequent development work.

Because the R&D team already had a committed development schedule, formal development didn't start until mid-to-late April. In early April, we only finalized the page style and UX with Alibaba Cloud's front-end team. The R&D cycle was approximately one month and covered:

* Developing the UI according to Alibaba Cloud's design specifications
* Adjusting all API interfaces to conform to Alibaba Cloud's development specifications, and updating the front end to connect to the new interfaces
* Integrating with the marketplace
* Adjusting security policies, including the source-side agent and security group policies
* Modifying the SDK to meet the Alibaba Cloud Marketplace's authorization requirements
* Moving the API scheduling portion of the original data synchronization agent for the cloud platform back to the server side to comply with security requirements

From early June to the final go-live on July 10, we adjusted our CI/CD pipeline (HyperMotion is classified as a tooling product but covers a broad scope and has a complex build — a dedicated article will cover this later) and conducted final end-to-end testing, going live on July 10.

### What We Gained from the Product

During this integration, in-depth conversations with various Alibaba Cloud teams were highly valuable. From a product security perspective, the teams made constructive suggestions that greatly helped us improve the security of our own product. Additionally, this process prompted us to re-examine our CI/CD pipeline, providing an excellent reference for better supporting multi-version releases in the future.

## Technical Integration Details

### Overall Architecture

HyperMotion's control plane is built on OpenStack's asynchronous microservices framework and adopts a containerized deployment model. It can be deployed on a single machine or in a Kubernetes cluster. The overall architecture diagram is as follows:

![2021-12-01-13-37-04](/images/2021-12-01-13-37-04.png)

This is the complete architecture diagram for Alibaba Cloud ISV integration:

![2021-12-01-13-38-15](/images/2021-12-01-13-38-15.png)

Backend modules are deployed in a Kubernetes cluster. Because our scenario also includes functions such as agent downloads, we additionally requested object storage resources.

### UI

To maintain visual consistency with Alibaba Cloud, the Alibaba Cloud front-end team provided us with a complete set of front-end design specifications.

![2021-12-01-13-41-20](/images/2021-12-01-13-41-20.png)

Although HyperMotion supports migration between multiple clouds, a dedicated Alibaba Cloud version was customized specifically for the marketplace (as shown at the beginning of this article).

Embedding into Alibaba Cloud's front-end ecosystem also requires some additional configuration. For Vue 3.0, the following options need to be added in `vue.config.js`:

![2021-12-01-13-46-23](/images/2021-12-01-13-46-23.png)

### API Layer

For security reasons, we could not use our existing API framework — instead, we needed to re-wrap our interfaces according to Alibaba Cloud's API specifications.

Per the specification requirements, all calls to our own services use the GET interface, defined as follows:

```
GET http://${isv_ip}/api/${action}?userinfo=${userinfo}&accessToken=${accessToken}&params=${params}&traceId=${traceId}
```

The API modification work was relatively heavy on the R&D side, requiring changes to both the front end and the back end simultaneously. Because HyperMotion strictly followed the microservices development philosophy during its development, the changes were not difficult — it was simply a matter of adding a thin wrapper around the interfaces.

### Security Adjustments

After close collaboration with Alibaba Cloud's security team, we ultimately made adjustments in the following two areas:

#### Communication Direction

Before joining Alibaba Cloud, to ensure communication efficiency, our product used a bidirectional communication model between the source-side host (e.g., a physical machine) and the control plane. The control plane also used a unidirectional push model when operating the cloud sync gateway (a cloud VM within the Alibaba Cloud tenant). According to Alibaba Cloud's security policy requirements, the network where our service resides must be strictly isolated from the outside world — even if the user's cloud VM is an Alibaba Cloud VM, it is not permitted to initiate inbound connections. We therefore changed all communication between the control plane and the source-side hosts and cloud sync gateways to be unidirectional (initiating upward to our control plane), satisfying the security requirements.

#### Interface Security

When users use the product, they need to deploy an agent program on the source-side host or within the virtualization platform, which requires a download. The original approach did not have a sufficiently robust security mechanism and could potentially allow unauthorized registration. Following the advice of the Alibaba Cloud security team, we adopted a key-based approach to encrypt critical information, preventing the information from being cracked and also preventing unauthorized and dangerous operations.

### Release and Go-Live

HyperMotion's build process is divided into two major parts: Agent builds and container builds. Because many operating systems (Linux/Windows) and kernel versions are involved, the Agent build is relatively complex. The container build is comparatively straightforward. Per the go-live requirements, we consolidated all builds on Alibaba Cloud's DevOps platform (Yunxiao), placed all artifacts into the designated artifact repository, and then the Alibaba Cloud team completed the go-live process by updating the Kubernetes environment.

## Suggestions for Improvement

The Alibaba Cloud Marketplace is also a relatively new team within Alibaba Cloud. There were quite a few pain points during the actual integration process. We were among the early seed customers — as far as I know, many enterprises that attempted integration ultimately chose to give up. The main reasons are as follows:

1. **No separate development and testing environment was provided.** Although Alibaba Cloud provided a test environment at the beginning, this was in fact the final production environment. Once the system went live, we had no other platform available for debugging. While rapid iterations can be used to fix bugs in production, for a rigorous commercial software product — especially one involving user data — we would much prefer ample time for thorough pre-release testing.

2. **No operations entry point was provided.** Currently, if issues arise in the live environment, we must rely on the Alibaba Cloud liaison to pull logs on our behalf. We cannot quickly locate problems ourselves, which lengthens the time to resolve incidents.

3. **The cost of modifying the existing system is too high.** From the integration process described above, the changes required at the API layer are a non-trivial challenge for many companies.

4. **Traffic referral is not prominent enough.** Despite multiple redesigns to attract traffic to the Alibaba Cloud Marketplace, many customers are still completely unaware of it. At the same time, the Alibaba Cloud Marketplace team collaborates too little with other internal teams. We recommend more joint promotion initiatives with business teams to reach more customers.

Despite the many areas still worth improving in the Alibaba Cloud Marketplace, as a pioneer in China's cloud computing ecosystem that upholds the "be integrated" philosophy and provides a fair competitive environment for ecosystem partners, we hope to continue going further together with Alibaba Cloud.
