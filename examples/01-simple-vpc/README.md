# Example: Simple VPC

**Complexity**: Low
**Estimated Time**: 15-20 minutes
**Best For**: Learning the IaC Spec Kit workflow

## Overview

This example demonstrates the most fundamental infrastructure component: a virtual private network (VPC) with basic security controls. It's intentionally simple to help you learn the IaC Spec Kit workflow without getting overwhelmed by complex requirements.

## What You'll Build

A basic network infrastructure including:

- Isolated virtual network (VPC)
- Public subnet for internet-facing resources
- Private subnet for internal resources
- Internet gateway for public subnet connectivity
- NAT gateway for private subnet outbound access
- Bastion host for secure SSH access to private resources
- Network security controls (security groups/NSGs)

## Use Case

**Scenario**: You're setting up a new project and need a basic network foundation that follows security best practices. You want public resources (like load balancers) in one subnet and private resources (like application servers) in another subnet, with a secure way to access private instances for administration.

## Learning Objectives

This example teaches you:

1. **Basic IaC Spec Kit workflow**: All 6 commands from `/iac.principles` to `/iac.implement`
2. **Cloud-agnostic specifications**: How to describe networking requirements without cloud-specific terms
3. **Progressive complexity**: Starting with a simple, cost-effective baseline
4. **Multi-cloud deployment**: Same spec works on AWS, Azure, GCP, and IBM Cloud

## Prerequisites

- Cloud account (choose one: AWS, Azure, GCP, or IBM Cloud)
- IaC Spec Kit installed (`iac-specify check`)
- Terraform installed
- AI coding assistant running in your project directory

## Get Started

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS Workflow](./cloud-workflows/aws.md)** - VPC, subnets, Internet Gateway, NAT Gateway
- **[Azure Workflow](./cloud-workflows/azure.md)** - Virtual Network, subnets, NAT Gateway, Bastion
- **[GCP Workflow](./cloud-workflows/gcp.md)** - VPC Network, subnets, Cloud NAT, Bastion Host
- **[IBM Cloud Workflow](./cloud-workflows/ibm-cloud.md)** - VPC, subnets, Public Gateway

## What Makes This Example Simple

- **Single region deployment**: No multi-region complexity
- **Basic networking only**: No compute, storage, or application layers
- **Minimal components**: Just essential networking building blocks
- **Low cost**: Most components have free tier or minimal charges

## Next Steps

After completing this example:

1. Try **[02-static-website](../02-static-website/)** to add storage and CDN
2. Progress to **[03-wordpress](../03-wordpress/)** to add compute and database
3. Learn enterprise patterns with **[04-landing-zone](../04-landing-zone/)**
