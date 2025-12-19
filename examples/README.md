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

| Example | Complexity | Recommended Flow | What You'll Learn |
|---------|------------|------------------|-------------------|
| [01-simple-vpc](./01-simple-vpc/) | Low | Minimal (4 steps) | Basic workflow, networking requirements. Optional: Add principles for team projects. |
| [02-static-website](./02-static-website/) | Low | Minimal (4 steps) | Storage and CDN specs. Optional: Add principles for multi-site projects. |
| [03-wordpress](./03-wordpress/) | Medium | Minimal or Enriched | Non-technical requirements, Baseline vs Enhanced. Use enrichplan for production. |
| [04-landing-zone](./04-landing-zone/) | Medium-High | Enriched (with principles) | Enterprise governance, compliance. Principles essential for consistency. Enrichplan recommended. |
| [05-three-tier-webapp](./05-three-tier-webapp/) | Medium | Minimal or Enriched | Multi-tier architecture, security layers. Use enrichplan for production-grade implementations. |
| [06-data-pipeline](./06-data-pipeline/) | High | Enriched (with principles) | Event-driven patterns, data governance. Enrichplan recommended for complex data flows. |
| [07-microservices](./07-microservices/) | High | Enriched (with principles) | Distributed systems, service mesh. Principles essential. Enrichplan critical for quality. |

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

Minimal workflow (4 steps):
- **spec.md** (`/iac.specify`) - Infrastructure requirements using generic terms
- **plan.md** (`/iac.plan`) - Cloud-specific implementation plan with inline research
- **tasks.md** (`/iac.tasks`) - Detailed task breakdown
- **Terraform files** (`/iac.implement`) - Actual infrastructure as code

Optional enhancements:
- **principles.md** (`/iac.principles`) - Project governance rules (cross-capability memory for multi-feature projects)
- **research.md, architecture.md, modules.md, quickstart.md** (`/iac.enrichplan`) - Deep research and comprehensive documentation (improves quality for complex/production projects)
