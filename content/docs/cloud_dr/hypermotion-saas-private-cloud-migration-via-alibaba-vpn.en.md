---
title: Migrating Private Cloud to HyperMotion SaaS via Alibaba Cloud VPN
description: "Step-by-step guide to connecting an on-premises private cloud to HyperMotion SaaS using an Alibaba Cloud VPN Gateway for secure, low-latency migration."
date: 2021-02-10 10:35:16
author: Ray Sun
tags:
  - Alibaba Cloud
  - VPN
  - Cloud Migration
  - HyperMotion
categories:
  - Cloud Migration
draft: false
---

HyperMotion SaaS is a cloud-based migration service that helps enterprises quickly move workloads from private clouds or on-premises data centers to public clouds. This article explains how to use Alibaba Cloud VPN to enable HyperMotion SaaS to migrate private cloud environments.

<!-- more -->

## Background

The architecture of HyperMotion SaaS places the control plane in the cloud, while the data plane requires direct connectivity to the source environment. For public-cloud-to-public-cloud migrations, network connectivity is usually not an issue. However, for migrations from private clouds or on-premises data centers, a secure network connection must be established.

Alibaba Cloud VPN Gateway provides a straightforward way to create an encrypted network connection between an Alibaba Cloud VPC and an on-premises data center or private cloud.

## Architecture Design

The overall architecture is as follows:

1. HyperMotion SaaS is deployed on Alibaba Cloud
2. The source private cloud environment connects to the Alibaba Cloud VPC through an Alibaba Cloud VPN Gateway
3. HyperMotion SaaS accesses the source environment through the VPC network

## Configuration Steps

### 1. Create an Alibaba Cloud VPN Gateway

In the Alibaba Cloud console, create a VPN Gateway:
- Select an appropriate bandwidth specification (at least 100 Mbps recommended)
- Enable the IPsec-VPN feature

### 2. Create a Customer Gateway

Configure the VPN gateway information for the on-premises data center or private cloud:
- Enter the public IP address of the local VPN device
- Configure the peer routing information

### 3. Create a VPN Connection

Create an IPsec VPN connection:
- Select Pre-shared Key authentication
- Configure IKE and IPsec parameters

### 4. Configure the Local VPN Device

Based on the Alibaba Cloud VPN Gateway configuration, configure the local VPN device (router or firewall) accordingly:
- Configure the IPsec tunnel
- Configure routing policies

### 5. Verify Network Connectivity

After configuration is complete, verify network connectivity between the Alibaba Cloud VPC and the on-premises environment:

```bash
# Ping the local server from an Alibaba Cloud ECS instance
ping <local-server-ip>

# Ping the Alibaba Cloud ECS from the local server
ping <ecs-ip>
```

### 6. Configure HyperMotion SaaS

Once network connectivity is established, configure HyperMotion SaaS:
- Add source hosts (using private IP addresses)
- Select the target cloud platform
- Start data synchronization

## Notes

1. **Bandwidth planning**: VPN bandwidth affects the speed of data migration. Plan appropriately based on data volume and migration window.

2. **Security group configuration**: Ensure that Alibaba Cloud security groups allow traffic from the VPN subnet.

3. **Routing configuration**: Ensure the Alibaba Cloud VPC routing table has the correct routes pointing to the on-premises network.

4. **VPN stability**: The stability of the VPN connection affects the reliability of data migration. Thorough testing before migration is strongly recommended.

## Summary

Using Alibaba Cloud VPN, HyperMotion SaaS can securely and efficiently migrate private cloud environments. This approach is easy to configure, secure, and reliable, and meets the requirements of most private cloud migration scenarios.
