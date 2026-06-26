---
title: "Why Data Flow Is the Core Capability of Hybrid Cloud?"
description: "Why free data flow across clouds — enabled by migration and DR technology — is the critical hybrid cloud capability, examined through China's state vs. private cloud debate."
date: 2022-07-20T08:29:00+08:00
slug: "why-data-exchange-is-key-feature-of-hybird-cloud"
author: Ray Sun
tags:
  - Trend Analysis
  - Cloud Computing
  - cloud
categories:
  - Trend Analysis
draft: false
---

Since entering the 2010s, cloud computing has gradually supplanted traditional infrastructure to become the new foundation of information systems. In October 2020, I wrote an article titled *Thoughts on Migration and Disaster Recovery Under the Cloud-Native Trend* ([https://sunqi.site/posts/cloud-migration-dr-on-cloud-native/](https://sunqi.site/posts/cloud-migration-dr-on-cloud-native/)), which analyzed in detail how data protection — critical to users — would change under this new infrastructure paradigm. The present article builds on that foundation, incorporating two years of industry practice and recent domestic hot-button events for a deeper analysis and synthesis.

## Cloud Platforms — State-Owned or Privately-Owned?

Just this week (July 12, 2022), a bombshell landed in the cloud computing world. The WeChat official account "State-Owned Assets Xinhua" published a major announcement: *SASAC Convenes a Work Promotion Meeting on Deepening Specialized Integration Among Central Enterprises*.

![2022-07-20-08-31-13](/images/2022-07-20-08-31-13.png)

The cloud computing-related content drew significant attention:

> The meeting noted that in recent years, central enterprises have **implemented specialized integration with broader industry coverage, wider levels of participation, and a higher degree of refinement**, achieving notable results in serving national strategies, optimizing the layout of the state-owned economy, and driving high-quality development.

> **China Telecom has brought in multiple central enterprise strategic investors to build a national cloud company, coordinating technology innovation, infrastructure construction, and security deployment to accelerate the development of an indigenous cloud technology ecosystem.**

China Telecom's specific moves were described as:

> China Telecom, centered on its cloud transformation and digital transition strategy and leveraging specialized integration, is building a "one cloud, two wings" business cluster. Around the development of a digital society, **it has brought in central enterprise strategic investors including China Electronics, CETC, China Chengtong, and China Reform, establishing the equity-diversified Tianyi Cloud Technology Co., Ltd.**, actively promoting the consolidation of cloud computing resources among central enterprises. By deepening joint R&D with central enterprises such as China Electronics and prestigious universities such as Tsinghua University, it is building a complete, independently controllable indigenous cloud technology ecosystem. Consolidating internal resources, Tianyi Cloud has established subsidiaries in all 31 provinces, building a sound cloud-network integrated operations system. Today, Tianyi Cloud is the world's largest telecom operator cloud and China's largest hybrid cloud, and its framework as the national cloud is essentially in place.

According to corporate information databases, Tianyi Cloud Technology Co., Ltd. remains 100% owned by China Telecom — the ownership change has not yet been formalized — but given the clarity of direction, everything is expected to accelerate.

![2022-07-20-08-31-37](/images/2022-07-20-08-31-37.png)

The establishment of the "national cloud" also seems to put to rest last year's widely circulated "state-owned cloud" rumors. On August 12, 2021, the Tianjin SASAC's *Implementation Plan for Accelerating the Migration of State-Owned Enterprises to the Cloud and Improving the State-Owned Cloud System*, in Part 3, Key Tasks, Point 2, explicitly stated:

> Information systems that enterprises have already deployed on third-party public cloud platforms (such as "Huawei Cloud," "Alibaba Cloud," "Tencent Cloud," "Wo Cloud," "Tianyi Cloud," "China Mobile Cloud," etc.) must be fully migrated to the state-owned cloud within 2 months of their lease expiration, with a hard deadline of September 30, 2022, at the latest. Effective immediately, enterprises may no longer sign new or renewed cloud resource rental contracts with third-party public cloud platforms.

With less than two months remaining before September 30, the actual progress of policy enforcement remains unclear. Will the formal designation of a national cloud influence prior compliance efforts? Could there be redundant migration? From the outside, the specifics are unknown.

One of the triggers for all these changes was an incident in early 2021, when a major internet company quietly completed an unauthorized overseas listing, providing access to large amounts of sensitive public data. On June 10 of the same year, the 29th Session of the Standing Committee of the 13th National People's Congress passed the *Data Security Law of the People's Republic of China* ([http://www.npc.gov.cn/npc/c30834/202106/7c9af12f51334a73b56d7938f99a788a.shtml](http://www.npc.gov.cn/npc/c30834/202106/7c9af12f51334a73b56d7938f99a788a.shtml)), which states:

> Article 14: The state shall implement the big data strategy, promote the construction of data infrastructure, and encourage and support innovative applications of data across industries and sectors. Provincial-level governments and above shall incorporate digital economy development into their economic and social development plans and, where necessary, formulate digital economy development plans.

State-owned enterprises are well-known pillars of the national economy and a key battleground for every cloud vendor. The designation of the national cloud seems to settle the question of state-owned vs. privately-owned, and China's cloud computing sector will inevitably chart a path with distinctly Chinese characteristics. But is this the endpoint for Chinese cloud computing? Clearly not — policies always lag technology, and the final form will continue to evolve as technology advances. For enterprise users, the only constant is change. To navigate this change, the most important new "state asset" — *data* — must be free to flow, enabling users to better embrace an uncertain future.

## Hybrid Cloud — Protecting Existing Investments, Embracing Change

Faced with constant change, hybrid cloud is clearly a path suited to China's development trajectory. From a growth perspective, the past decade of cloud computing has given rise to a proliferation of public and private cloud vendors — by conservative estimates, at least 20 public clouds are currently in operation, and private cloud brands are even more numerous. From an investment protection perspective, enterprises cannot simply abandon their prior investments in cloud computing and infrastructure, making hybrid cloud the comprehensive infrastructure approach that serves both enterprise interests and national strategy.

From a technical standpoint, no foundational platform can be replaced overnight; system-building must follow its own laws and proceed step by step. As noted above, data flow enables users to handle changes in cloud infrastructure with greater agility, and data flowing between different clouds in a hybrid environment is the most effective way to prevent the formation of new "data silos" in the cloud era.

![2022-07-20-08-31-54](/images/2022-07-20-08-31-54.png)

## The Evolution of Hybrid Cloud Management — From Platform to Toolset

In 2018, Gartner mentioned in an article ([https://blogs.gartner.com/marco-meinardi/2018/01/22/upcoming-research-cloud-management-platforms/](https://blogs.gartner.com/marco-meinardi/2018/01/22/upcoming-research-cloud-management-platforms/)) the ten modules of Cloud Management Platforms. Among them, Cloud Migration and DR existed as a standalone module — one of the ten most closely tied to user data flow. Yet in practice, because early cloud data volumes were small and data flow needs were not prominent, very few cloud management platforms were able to offer such a specialized service module. Only a handful of forward-looking users recognized this latent need and acted on it — for example, the article *Cloud-Native Migration Services in Haitong Securities' Hybrid Financial Cloud Platform Ecosystem* published in *Trading Technology Frontiers*, Issue 40 of the Shanghai Stock Exchange (September 2020), which documented such best practices and provided a reference for other brokerages exploring hybrid cloud data flow.

![2022-07-20-08-32-06](/images/2022-07-20-08-32-06.png)

Why can't such an important service be offered directly by cloud management platforms? I see two reasons: data volume and technical barriers. On the data volume side, as noted above, early cloud platforms had low data volumes and "manual labor" was sufficient for data flow needs. But as application counts grew and data volumes exploded, traditional "throwing bodies at the problem" could no longer meet the service-oriented data flow needs of cloud users. The technical barrier, however, is the greatest obstacle preventing cloud management platforms from offering these services. Cloud Migration and DR technology draws partly from traditional disaster recovery techniques and partly from cloud-native resource and orchestration technologies — it is a cross-domain technical integration and innovation that is no less challenging than building a cloud management platform itself. The pressure of project delivery leaves cloud management platform vendors little capacity for additional innovation.

This was confirmed by Gartner's April 2022 report, *Market Guide for Cloud Management Tooling* ([https://www.gartner.com/doc/reprints?id=1-29PBZLL4&ct=220413&st=sb&elqTrackId=adedc2cde73f4497b990cb119e448714&elqaid=7083&elqat=2](https://www.gartner.com/doc/reprints?id=1-29PBZLL4&ct=220413&st=sb&elqTrackId=adedc2cde73f4497b990cb119e448714&elqaid=7083&elqat=2)). A very notable change is the terminology itself — what we habitually called "Cloud Management Platform" is redefined in the report as "Cloud Management Tooling," which can simply be understood as a cloud management toolset. Gartner recognizes that as cloud management services mature, specialized vendors are focused on abstracting services into automated tools. In the report, third-party specialized cloud management tools and traditional cloud management platforms appear as parallel modules, jointly providing multi-cloud management capabilities to MSPs. Gartner also added Backup to the Cloud Migration and DR module, which unifies the scenario-based applications we define as "data flow."

![2022-07-20-08-32-18](/images/2022-07-20-08-32-18.png)

## What Is Data Flow? — The Foundation of Broad-Sense Cloud Migration and Cloud DR

Is cloud migration a one-time business? Many people have asked me this — partners, investors, and others. Let me state my view directly: "cloud migration," depending on its purpose, can be divided into narrow-sense and broad-sense cloud migration. Narrow-sense cloud migration refers to project-based activities such as migrating to the cloud, migrating off the cloud, or switching clouds. Broad-sense cloud migration, by contrast, is one application mode of data flow, and its downstream scenarios include cloud DR, backup, data east-west transfer, and more. From the perspective of hybrid cloud development trends, cloud migration is absolutely not a one-time need — it is one of the cloud's standard services.

### Narrow-Sense Cloud Migration — Project-Driven Application Scenarios

Starting with narrow-sense cloud migration: during the peak migration wave (before 2010), cloud migration was the best way to solve the "highway with no cars" problem — rapidly stimulating capacity expansion in underlying infrastructure to offset vendors' upfront project losses.

![2022-07-20-08-32-32](/images/2022-07-20-08-32-32.png)

Over time, however, various "cloud switching" needs emerged. Here are some common scenarios:

**Scenario 1: Original platform left unmaintained.** Early cloud platform solutions and vendors were immature, with many products pioneering uncharted territory. Eventually, for various reasons, platforms were left without maintenance while business continued to run exposed, making it necessary to switch clouds to move the workloads.

**Scenario 2: Competition among vendors.** This scenario has little to do with technology and more to do with commercial interests. Since acquiring new customers from traditional on-premises environments is costly, vendors target each other's existing cloud customers instead. There is also the case where users intended to experiment with "free" open-source solutions, only to find they gradually lost control or performance didn't meet requirements, forcing a switch to commercial solutions — a dynamic seen with both cloud platforms and underlying cloud storage.

**Scenario 3: The platform cannot upgrade itself.** The most typical example is OpenStack cross-version upgrades. Although OpenStack eventually provided upgrade capabilities, vendor-customized OpenStack builds contain large amounts of functionality that cannot be contributed upstream, making upgrades practically impossible. When users want to move to a newer version, they can only do so via cloud migration — replacing the old platform and adding the original hardware back into the resource pool. This problem is not unique to OpenStack; some commercial cloud platforms face the same challenge.

Migrating off the cloud is, relative to migrating onto the cloud, a form of cloud switching — but it specifically refers to moving from public cloud to private cloud, so it warrants separate discussion. Public cloud has genuinely helped time-sensitive vendors accelerate innovation and seize opportunities, but as companies mature, financial pressures inevitably push wild growth toward precision management. At that point, enterprises must weigh the economics of public cloud vs. self-built infrastructure.

In the narrow sense, cloud migration resembles a passive action — just one part of a solution, and in that context it is indeed non-repeatable.

### Broad-Sense Cloud Migration — Data-Flow-Driven Application Scenarios

Broad-sense cloud migration is a cloud-native service centered on data flow, providing tenant-level data orchestration. Exactly as Gartner defines it: in a hybrid cloud environment, data flow capabilities enable data to move across platforms, providing a range of upper-layer application scenarios including — but not limited to — migration, DR, and backup services.

![2022-07-20-08-32-45](/images/2022-07-20-08-32-45.png)

In traditional physical environments, data flow was theoretically possible but practically insignificant — platforms were relatively homogeneous and upper-layer data-driven applications were few. But in the cloud-native era, the richness of services creates the conditions for data-driven business innovation.

Data flow capabilities must make sound use of cloud-native storage resources and expose upper-layer scenarios based on either compute orchestration or storage orchestration. Taking the compute orchestration layer as an example: resources can be restored on any platform, supporting diverse use cases including migration, DR, and simulation. The storage orchestration layer, meanwhile, provides a channel for data-driven innovation, connecting to various storage interfaces to supply data sources to upper-layer containers, big data platforms, and AI platforms.

As I noted in a previous article, because of the characteristics of cloud-native architecture, data is distributed across various cloud-native services. A data flow platform must therefore be compatible with diverse cloud-native services — hosts, RDS, containers, etc. — while intelligently leveraging the properties of cloud-native storage to achieve optimal cost.

![2022-07-20-08-32-56](/images/2022-07-20-08-32-56.png)

## Conclusion

"Data" is a critical new enterprise asset. How to mine innovation and even generate profit from data in the cloud era is a question enterprises must think through as part of their digital transformation. Data flow capabilities enable enterprise data to circulate within the hybrid cloud, providing the foundation and assurance for subsequent innovation. From a product development perspective, we exist in an era of rapid technological change, and cloud computing's development is creating new opportunities for a generation of infrastructure-layer products. The key to product success lies in rationally leveraging the common properties of cloud-native resources while combining them with one's own technical strengths from traditional domains. This article has primarily used the trajectory of cloud computing development in China to forecast and interpret how data will be applied in hybrid cloud environments. Drawing on Gartner's evolving definition of cloud management platforms, it proposes the concept of broad-sense cloud migration and arrives at the conclusion that data flow is the core capability of hybrid cloud.
