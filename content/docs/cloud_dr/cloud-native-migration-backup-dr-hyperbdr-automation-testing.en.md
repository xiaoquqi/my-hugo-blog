---
title: "Automated Testing Practices for the Cloud-Native Disaster Recovery Product HyperBDR"
date: 2023-02-06T14:28:40+08:00
slug: "cloud-native-migration-backup-dr-hyperbdr-automation-testing"
author: Ray Sun
tags:
  - Automated Testing
  - Python
  - Terraform
categories:
  - Product R&D
draft: false
---

HyperBDR is a migration and disaster recovery product built on cloud-native principles. Its core business scenario is synchronizing source-side data to cloud-native storage at the block level using incremental differentials. It currently supports both Block Storage and Object Storage. After synchronization, it leverages the patented Boot-in-Cloud technology to restore business systems to a running state with a single click — fully exploiting cloud-native orchestration capabilities to address the distinct needs of migration and disaster recovery scenarios.

HyperBDR currently supports nearly 10 major source-side operating system families (Windows / CentOS / Redhat / Ubuntu / SUSE / domestic OS), with minor versions exceeding several hundred, and has progressively added support for nearly 40 target cloud platforms (public cloud, dedicated cloud, private cloud, hyper-converged, virtualization, etc.) — a number that continues to grow. If we were to run a full coverage test across all source operating systems against every target platform, the combined test cases could exceed 10,000.

At this scale, relying solely on manual effort to achieve test coverage is clearly impractical. Automated testing must be introduced to cover core business scenarios. This not only satisfies automated testing requirements, but also enables developers to promptly assess the impact of new features on core workflows during day-to-day development — further improving product stability and reliability.

## Pain Points

Let us first examine several pain points in manual testing of HyperBDR:

### Pain Point 1: Too Many Test Cases, Insufficient Headcount

Given the scale of sources and targets described above, even a basic smoke test requires well over a hundred scenario combinations per full test run. For example:

- Source side (19 variants): CentOS (6/7/8), Redhat (6/7/8), SUSE (11/12), Ubuntu (14.04/16.04/18.04/20.04), Windows (2003/2008/2012/2016/2019), Oracle Linux, domestic OS

- Target side (9 variants): OpenStack, AWS, Alibaba Cloud, Tencent Cloud, Huawei Cloud, China Mobile Cloud, ZStack, hyper-converged product, hyper-converged product

That adds up to 171 scenario combinations per test run. Some might say that doesn't sound like much and shouldn't take long to execute — but that leads us to the second pain point: test cycle duration.

### Pain Point 2: Long Test Cycles

Unlike functional business testing, testing a single HyperBDR scenario is extremely time-consuming. Setting aside resource preparation and configuration time, let's analyze just the data synchronization and boot phases:

- Data synchronization: In simple terms, data sync reads the effective data (not allocated capacity) from the source OS at the block level and writes it to cloud-native storage on the target side. The first sync is a full copy; subsequent syncs are permanent incrementals. Taking Windows as an example — assume 500 GB of effective data. At 80% utilization of a gigabit LAN, the transfer speed is approximately 800 Mbps (about 80 MB/s), giving a transfer time of roughly 1 hour and 8 minutes.

- Host boot: Boot time varies greatly depending on the cloud-native storage type. For Huawei Cloud Block Storage, because of its snapshot mechanism and ability to swap system disks, boot time is nearly independent of data volume and can typically be kept within 5 minutes. However, most domestic cloud platforms lack such capabilities. Alibaba Cloud, for instance, throttles reads from snapshot-backed volumes at 40 MB/s, which significantly extends recovery time. Using Object Storage as an example — restoring Object Storage data to Block Storage over an internal network for a 500 GB effective-data disk takes approximately 40 minutes.

So a single-host test run takes at least 2 hours. Under the scenario assumptions above, an entire day of testing may not even complete a full sweep of a single cloud platform. One might ask: why not run them concurrently? That brings us to the third pain point: cost.

### Pain Point 3: Testing Cost

The reason we cannot run everything concurrently is network bandwidth constraints. In our internal R&D environment, our external bandwidth is only 40 Mbps. Under the test scenarios described, fully transmitting 500 GB of data at full bandwidth utilization takes approximately 35 hours — which further extends the overall test cycle.

In addition to network, there are other environmental constraints: virtualization platform licenses, cloud vendor spend, server resource consumption, and so on.

## Automation Solution

For each pain point above, we developed a corresponding solution:

### For Too Many Test Cases: Use Terraform to Create Source Test VMs on Public Cloud

Terraform is an infrastructure-as-code tool that lets us rapidly and reliably create and destroy test resources. Terraform's provider ecosystem already covers major domestic and international public clouds, as well as the OpenStack private cloud we use internally — no custom code needed; simply use the cloud vendor's official provider.

Based on the analysis above, we can use Terraform to quickly prepare source environments for testing, and after testing completes, use Terraform to tear them down immediately, eliminating resource waste. The same approach applies to preparing target-side environments on various cloud platforms.

### For Long Test Cycles: Concurrent Execution

Concurrency operates at two levels. First, when testing against a single public cloud, we can use multiple cloud accounts simultaneously to run parallel tests. Second, across different public clouds, tests can run concurrently, maximizing our available bandwidth.

### For Cost: On-Demand Cloud Resources

By managing test resource lifecycles with Terraform, we can spin up resources when needed and tear them down immediately after testing — eliminating waste and significantly reducing testing costs.

## Test Framework

The overall HyperBDR automated test framework consists of the following components:

### 1. Source Environment Preparation

Use Terraform to rapidly prepare the source environment required for testing, including HyperBDR Agent installation.

### 2. HyperBDR Business Driver

Via a Python SDK, call HyperBDR's business API to drive automated scenario execution. The core workflow is:

- Configure storage platform
- Create sync policy
- Add source host
- Execute sync operation
- Execute boot operation
- Execute shutdown operation
- Delete host

### 3. Result Verification

After the host boots, test network connectivity to determine whether the boot succeeded. Verify that business processes are running normally, and confirm that data disks are mounted correctly.

### 4. Test Reporting

Use Robot Framework's built-in report generation to render test results in HTML format for easy review.

## CI/CD Integration

We integrated the framework with Jenkins. When a developer triggers a Jenkins job, a series of test scenarios executes automatically. We also configured scheduled Jenkins jobs that trigger automatically every night at midnight, ensuring test results are produced every day.

## Future Plans

Our automated test framework is still at an early stage and has many areas to improve:

1. Expanding test cases: Our current test cases remain relatively limited. As the product evolves, we will continuously expand coverage.

2. Improving test reports: The current report format is fairly basic. Future iterations can add richer charts and visualizations to make reports more intuitive.

3. Test environment management: Environment management is currently simple. Future improvements may introduce additional tooling such as Ansible and SaltStack for better environment control.
