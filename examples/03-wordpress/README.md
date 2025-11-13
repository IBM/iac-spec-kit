# WordPress Deployment Example

This example demonstrates how to deploy a production-ready WordPress infrastructure using IaC Spec Kit. It's perfect for showing how the framework handles real-world, non-technical requirements like "I want to deploy WordPress".

## Learning Objectives

- Handle non-technical user requirements and translate them into proper infrastructure specifications
- See how the same requirements work across AWS, Azure, GCP, and IBM Cloud
- Understand the Baseline vs Enhanced complexity pattern
- Learn how principles establish governance while remaining mostly cloud-agnostic
- Experience the complete workflow from principles to implementation

## Use Case

**Scenario**: You need to deploy WordPress for a small production environment with a budget of $500/month. The site needs to handle moderate traffic, be secure, and have automated backups.

**What the framework will create**:
- Compute resources for running WordPress
- Managed database service (MySQL/MariaDB)
- Object storage for media files
- Load balancer for traffic distribution
- Networking (VPC/VNet with public/private subnets)
- Security groups and access controls
- Backup and monitoring

## Complexity Level

**Medium** (45-60 minutes)

This example uses **Baseline** complexity for cost optimization while maintaining production-grade security and reliability suitable for a small WordPress site.

## Prerequisites

Before starting, ensure you have:

- IaC Spec Kit installed
- Your chosen cloud provider account with appropriate permissions
- Terraform installed (or your preferred IaC tool)
- An AI coding assistant with IaC Spec Kit commands available

## Cloud-Specific Workflows

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS](./cloud-workflows/aws.md)** - Uses ECS/Fargate, RDS, S3, ALB
- **[Azure](./cloud-workflows/azure.md)** - Uses Container Instances, Azure Database for MySQL, Blob Storage, Application Gateway
- **[GCP](./cloud-workflows/gcp.md)** - Uses Cloud Run, Cloud SQL, Cloud Storage, Cloud Load Balancing
- **[IBM Cloud](./cloud-workflows/ibm-cloud.md)** - Uses Code Engine, Databases for MySQL, Cloud Object Storage, Application Load Balancer

## What You'll Learn

1. **How principles work**: You'll see that governance rules (security defaults, progressive complexity, testing requirements) are the same across all clouds—only the curated module library preference changes

2. **Tech-agnostic specifications**: The `/iac.specify` prompt and generated spec.md use generic terms like "managed database service" and "object storage" rather than "RDS" or "S3"

3. **Cloud-specific planning**: The `/iac.plan` step is where you specify your cloud provider and preferred services, and the framework generates cloud-specific architecture

4. **Simple prompts, powerful results**: You only need to provide 1-2 line prompts to each slash command—the framework generates comprehensive documentation and code

## Expected Costs

- **AWS**: ~$150-250/month (Fargate + RDS + S3 + ALB)
- **Azure**: ~$150-250/month (Container Instances + Azure Database + Storage + App Gateway)
- **GCP**: ~$120-200/month (Cloud Run + Cloud SQL + Storage + Load Balancing)
- **IBM Cloud**: ~$150-250/month (Code Engine + Database + COS + ALB)

Actual costs depend on traffic, storage usage, and regional pricing.

## Next Steps

After completing this example:

1. Try modifying the requirements (e.g., higher traffic, multi-region, enhanced security)
2. Explore the [Landing Zone example](../04-landing-zone/) for enterprise patterns
3. Learn about the [Data Pipeline example](../06-data-pipeline/) for different architecture styles
4. Apply these patterns to your own infrastructure projects
