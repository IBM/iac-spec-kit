# Example: Three-Tier Web Application

**Complexity**: Medium
**Estimated Time**: 1-2 hours
**Best For**: Web application teams, full-stack developers, standard business applications

## Overview

This example demonstrates the classic three-tier architecture pattern used by most web applications: a load balancer tier, application tier, and database tier. This architecture separates concerns, improves scalability, and enables independent scaling of each tier.

## What You'll Build

A production-ready three-tier web application infrastructure:

- **Load Balancer Tier**: Distributes traffic across application instances
- **Web/Application Tier**: Auto-scaling compute instances or containers
- **Database Tier**: Managed relational database with replication
- **Caching Layer**: In-memory cache (Redis/Memcached) for performance
- **Monitoring and Logging**: Application and infrastructure observability
- **Security**: Network isolation, security groups, encryption

## Use Case

**Scenario**: You're deploying a standard web application (e-commerce, SaaS product, internal portal) that needs to handle variable traffic, maintain high availability, and separate presentation, business logic, and data layers for security and scalability.

## Learning Objectives

This example teaches you:

1. **Multi-tier architecture**: How to describe layered application requirements
2. **Auto-scaling compute**: Specifying dynamic capacity without cloud-specific services
3. **Database requirements**: Expressing HA, backup, and performance needs generically
4. **Caching strategies**: Describing in-memory caching for performance
5. **Security layers**: Network isolation, encryption at rest/transit

## Prerequisites

- Cloud account (AWS, Azure, GCP, or IBM Cloud)
- IaC Spec Kit installed (`iac-specify check`)
- Terraform installed
- AI coding assistant running
- Application code ready to deploy (or use sample app)

## Get Started

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS Workflow](./cloud-workflows/aws.md)** - ALB, ECS/EC2, RDS, ElastiCache
- **[Azure Workflow](./cloud-workflows/azure.md)** - App Gateway, App Service/VMs, Azure Database, Redis Cache
- **[GCP Workflow](./cloud-workflows/gcp.md)** - Cloud Load Balancing, Compute Engine/Cloud Run, Cloud SQL, Memorystore
- **[IBM Cloud Workflow](./cloud-workflows/ibm-cloud.md)** - Load Balancer, VPC instances/Code Engine, Databases, Cache

## Architecture Pattern

```
Internet → Load Balancer → Application Tier → Database Tier
                              ↓
                         Cache Layer
```

**Traffic flow**: Users hit load balancer → Load balancer distributes to healthy app instances → Apps query cache first, then database if cache miss → Apps write to database, invalidate cache

## What Makes This Example Medium Complexity

- **Multiple tiers**: Load balancer, app, database, cache all need configuration
- **Auto-scaling logic**: Dynamic capacity based on metrics
- **Database management**: Backups, replication, connection pooling
- **Inter-tier networking**: Security groups, private subnets, service communication
- **Monitoring requirements**: Application and infrastructure metrics

## Next Steps

After completing this example:

1. Add **CI/CD pipeline** for automated deployments
2. Implement **[07-microservices](../07-microservices/)** to break monolith into services
3. Add **[06-data-pipeline](../06-data-pipeline/)** for analytics on application data
