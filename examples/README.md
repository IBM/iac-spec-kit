# IaC Spec Kit Examples

This directory contains real-world examples demonstrating how to use the IaC Spec Kit for various infrastructure use cases, ranging from simple to complex scenarios.

**See a complete generated example:** [wordpress-ibm-cloud](https://github.com/vburckhardt/wordpress-ibm-cloud) - A full WordPress deployment on IBM Cloud generated using this workflow.

## Multi-Cloud Support

All examples in this directory are designed to work with any cloud provider. Each example shows the commands and prompts to use with:

- AWS
- Azure
- Google Cloud Platform (GCP)
- IBM Cloud

The workflow commands (`/iac.principles`, `/iac.specify`, `/iac.plan`, etc.) remain the same across clouds—only the prompts and cloud selections differ.

## Available Examples

| Example | Complexity | What You'll Learn |
|---------|------------|-------------------|
| [01-simple-vpc](./01-simple-vpc/) | Low | Basic IaC Spec Kit workflow using a simple VPC example. Learn the six core commands and how to describe networking requirements generically. |
| [02-static-website](./02-static-website/) | Low | How to specify storage and CDN requirements without cloud-specific terms. Practice translating "I need a website" into proper infrastructure specs. |
| [03-wordpress](./03-wordpress/) | Medium | Handling non-technical requirements and the Baseline vs Enhanced complexity pattern. See how the same spec deploys to different clouds. |
| [04-landing-zone](./04-landing-zone/) | Medium-High | Enterprise governance patterns, multi-account strategies, and compliance requirements. Learn to express regulatory needs generically. |
| [05-three-tier-webapp](./05-three-tier-webapp/) | Medium | Multi-tier architecture specifications, auto-scaling requirements, and security layers. Practice describing layered applications. |
| [06-data-pipeline](./06-data-pipeline/) | High | Event-driven architecture patterns, serverless compute specs, and data governance. Learn to specify complex data flows generically. |
| [07-microservices](./07-microservices/) | High | Distributed systems patterns, service mesh concepts, and comprehensive observability. Practice specifying container orchestration needs. |

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

- **Simple Command-Based Workflow**: Run slash commands with prompts to have the framework generate specs, plans, and tasks
- **Generic Infrastructure Principles**: Governance rules (security, testing, progressive complexity) apply regardless of cloud provider
- **Generic Infrastructure Terms**: Specifications use generic terms ("managed database", "object storage", "encryption key management") instead of cloud-specific service names ("RDS", "S3", "Key Protect")
- **Cloud-Specific Implementation**: The `/iac.plan` step is where you specify your cloud and services, translating generic terms into specific services (e.g., "object storage" → S3, Cloud Storage, or COS)
- **Progressive Complexity**: Examples show the Baseline vs Enhanced pattern for scaling infrastructure based on environment needs (Baseline = minimal production-ready controls, Enhanced = additional enterprise-grade controls for security, HA, DR)

## Getting Started

If you're new to IaC Spec Kit, we recommend starting with:

1. **[01-simple-vpc](./01-simple-vpc/)** - Learn the basic workflow and commands
2. **[03-wordpress](./03-wordpress/)** - Understand how to handle real-world application requirements
3. **[04-landing-zone](./04-landing-zone/)** - See enterprise governance patterns in action

Then progress to more complex examples as you become comfortable with the framework.

## What Gets Generated

When you run the workflow commands, the framework generates:

- **principles.md** - Your project's governance rules and decision-making framework
- **spec.md** - Infrastructure requirements using generic terms (no cloud-specific service names)
- **plan.md** - Cloud-specific implementation plan translating generic terms to actual services
- **tasks.md** - Detailed task breakdown for implementation
- **Terraform files** - Actual infrastructure as code (when you run `/iac.implement`)

You provide prompts to the slash commands and the framework generates the structured artifacts.
