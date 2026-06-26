---
title: How to Change the Storage Pool Type During Migration
date: 2021-12-03T07:08:26+08:00
author: Ray Sun
tags:
  - Cloud Migration
  - Storage
  - HyperMotion
categories:
  - Cloud Migration
draft: false
---

During cloud migration, the selection and management of storage pools is an important topic. Sometimes we choose a certain type of storage pool at the start of a migration, but need to switch to another type partway through. This article explains how to change the storage pool type in HyperMotion.

<!-- more -->

## Storage Pool Types

In cloud migration, there are mainly two types of storage pools:

### 1. Object Storage

Object Storage is a highly available and highly reliable storage method, suited for storing large amounts of unstructured data. Major cloud platforms offer the following object storage services:
- Alibaba Cloud OSS
- Tencent Cloud COS
- AWS S3
- Huawei Cloud OBS

Characteristics of object storage:
- Low cost: Object storage is cheaper than block storage
- Unlimited capacity: Can store data of any size
- Higher access latency: Compared to block storage, object storage has higher access latency

### 2. Block Storage

Block Storage is a low-latency, high-performance storage method suited for scenarios that require frequent reads and writes. Major cloud platforms offer the following block storage services:
- Alibaba Cloud EBS (Elastic Block Storage)
- Tencent Cloud CBS (Cloud Block Storage)
- AWS EBS
- Huawei Cloud EVS

Characteristics of block storage:
- High performance: Low latency, high IOPS
- Higher cost: More expensive than object storage
- Limited capacity: Subject to cloud platform restrictions, individual disks have an upper capacity limit

## Why Change the Storage Pool Type?

Reasons you might need to change the storage pool type during migration:

1. **Cost optimization**: You initially chose a high-performance but costly block storage, but discovered during migration that object storage can meet your needs, so you switch to reduce costs.

2. **Changing performance requirements**: You initially assessed that object storage performance would be sufficient, but found during actual migration that recovery times were too long and needed to switch to block storage for better performance.

3. **Quota limitations**: Due to cloud platform quota restrictions, you can no longer continue using the original storage type and need to switch to another type.

## Changing the Storage Pool in HyperMotion

HyperMotion provides flexible storage pool management capabilities, allowing users to change the storage pool type during migration.

### Steps

1. **Stop data synchronization**: Before changing the storage pool, you must first stop any ongoing data synchronization tasks.

2. **Create a new storage pool**: In the HyperMotion console, create a new storage pool of the desired type and configure the relevant parameters.

3. **Migrate data**: Migrate existing data from the old storage pool to the new one. This process may take some time depending on the volume of data.

4. **Update configuration**: After data migration is complete, update the host's storage pool configuration to point to the new storage pool.

5. **Restart synchronization**: Once the configuration is updated, restart the data synchronization tasks.

### Notes

- During the storage pool changeover, ensure data integrity and consistency are maintained.
- Changing the storage pool will cause a period of data synchronization interruption; plan the time window in advance.
- After the switch is complete, perform comprehensive testing to ensure the migration tasks can run normally.

## Best Practices

In practice, we recommend:

1. Before the migration project starts, thoroughly assess your storage requirements and choose the appropriate storage type.
2. If unsure, you can first use object storage for testing and then decide whether to switch to block storage based on actual conditions.
3. Before changing the storage pool, ensure adequate backups and testing have been performed.
