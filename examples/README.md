# IaC Spec Kit Examples

This directory contains real-world examples demonstrating how to use the IaC Spec Kit for various infrastructure use cases, ranging from simple to complex scenarios.

## Multi-Cloud Support

All examples in this directory work with **any cloud provider**. Each example shows the exact commands and prompts to use with:

- AWS
- Azure
- Google Cloud Platform (GCP)
- IBM Cloud

The workflow commands (`/iac.principles`, `/iac.specify`, `/iac.plan`, etc.) remain the same across clouds—only the prompts and cloud selections differ.

## Available Examples

| Example | Complexity | Time | Description |
|---------|------------|------|-------------|
| [01-simple-vpc](./01-simple-vpc/) | Low | 15-20 min | Basic virtual private network with public/private subnets and bastion host. Great for learning the framework. |
| [02-static-website](./02-static-website/) | Low | 20-30 min | Static website hosting with object storage, CDN, and custom domain. Perfect for marketing teams. |
| [03-wordpress](./03-wordpress/) | Medium | 45-60 min | WordPress deployment with compute, managed database, object storage, and load balancer. Demonstrates how to handle non-technical requirements like "I want to deploy WordPress". |
| [04-landing-zone](./04-landing-zone/) | Medium-High | 1-2 hours | Enterprise-grade landing zone with multi-account/subscription setup, networking hub, identity management, security baseline, and centralized logging. Shows governance controls and compliance. |
| [05-three-tier-webapp](./05-three-tier-webapp/) | Medium | 1-2 hours | Three-tier web application with load balancer, web tier, app tier, database tier, and caching. Standard architecture for web applications. |
| [06-data-pipeline](./06-data-pipeline/) | High | 2-3 hours | Multi-region data processing pipeline with serverless compute, message queues, data lakes, and orchestration. For data engineering teams. |
| [07-microservices](./07-microservices/) | High | 3-4 hours | Microservices platform with container orchestration, service mesh, API gateway, and comprehensive observability. For cloud-native applications. |

## How to Use These Examples

1. **Choose an example** that matches your use case and skill level
2. **Read the example's README** to understand the learning objectives
3. **Select your cloud provider** and open the corresponding workflow guide:
   - `cloud-workflows/aws.md`
   - `cloud-workflows/azure.md`
   - `cloud-workflows/gcp.md`
   - `cloud-workflows/ibm-cloud.md`
4. **Copy and run the commands** shown in the workflow guide
5. **Learn from the process** and adapt the patterns to your own projects

## Understanding the Structure

Each example follows this structure:

```
01-example-name/
├── README.md           # Learning objectives and overview
└── cloud-workflows/    # Cloud-specific command workflows
    ├── aws.md          # Commands and prompts for AWS
    ├── azure.md        # Commands and prompts for Azure
    ├── gcp.md          # Commands and prompts for GCP
    └── ibm-cloud.md    # Commands and prompts for IBM Cloud
```

## Key Learning Points

These examples demonstrate:

- **Simple Command-Based Workflow**: Just run slash commands with simple prompts—the framework generates all the specs, plans, and tasks
- **Cloud-Agnostic Principles**: Governance rules (security, testing, progressive complexity) stay the same across clouds
- **Cloud-Agnostic Specifications**: Requirements use generic terms ("managed database", "object storage", "serverless compute") not cloud-specific services
- **Cloud-Specific Implementation**: The `/iac.plan` step is where you specify AWS, Azure, GCP, or IBM Cloud and the framework generates cloud-specific architectures
- **Progressive Complexity**: Examples show the Baseline vs Enhanced pattern for scaling infrastructure based on environment needs

## Getting Started

If you're new to IaC Spec Kit, we recommend starting with:

1. **[01-simple-vpc](./01-simple-vpc/)** - Learn the basic workflow and commands
2. **[03-wordpress](./03-wordpress/)** - Understand how to handle real-world application requirements
3. **[04-landing-zone](./04-landing-zone/)** - See enterprise governance patterns in action

Then progress to more complex examples as you become comfortable with the framework.

## What Gets Generated

When you run the workflow commands, the framework automatically generates:

- **principles.md** - Your project's governance rules and decision-making framework
- **spec.md** - Technology-agnostic infrastructure requirements
- **plan.md** - Cloud-specific implementation plan and architecture
- **tasks.md** - Detailed task breakdown for implementation
- **Terraform files** - Actual infrastructure as code (when you run `/iac.implement`)

You just provide simple prompts to the slash commands—the framework does the heavy lifting.
