# IaC Spec Kit

*Define infrastructure requirements, generate production-ready Terraform.*

**IaC Spec Kit is an Infrastructure as Code framework that uses the [Specification-Driven Development methodology](https://github.com/github/spec-kit) created by GitHub. Write cloud-agnostic infrastructure requirements and let AI agents generate Terraform configurations for AWS, Azure, GCP, and IBM Cloud.**

## Getting Started

- [Installation Guide](installation.md)
- [Quick Start Guide](quickstart.md)
- [Local Development](local-development.md)

## What is IaC Spec Kit?

IaC Spec Kit transforms how teams provision cloud infrastructure. Instead of writing Terraform code directly, you:

1. **Write infrastructure requirements** in plain language (technology-agnostic)
2. **Specify your cloud provider** and architectural preferences
3. **Generate Terraform code** automatically using AI agents
4. **Validate and provision** infrastructure with confidence

The framework uses the specification-driven development methodology (created by GitHub) applied specifically to Infrastructure as Code workflows. This approach separates *what* you need (requirements, SLOs, compliance) from *how* to build it (cloud provider, Terraform modules).

### Who is this for?

**Infrastructure specialists** who need:
- Faster Terraform development with AI assistance
- Reusable infrastructure patterns across cloud providers
- Governance frameworks for infrastructure decisions
- Structured workflows for complex multi-cloud architectures

**Application developers** who need:
- Simple infrastructure provisioning without deep cloud expertise
- Production-ready infrastructure for their applications
- Cost-effective cloud deployments with best practices built-in
- Less time managing infrastructure, more time building features

## Key Features

### Infrastructure-Focused Templates

All templates are designed for cloud infrastructure:
- **Specification templates**: Infrastructure requirements, SLOs, compliance needs, cost constraints
- **Planning templates**: Cloud provider selection, network architecture, security design, state management
- **Task templates**: Dependency-ordered implementation with Terraform validation checkpoints

### Multi-Cloud Support

Generate infrastructure for multiple cloud providers:
- **AWS**: VPC, EC2, ECS, EKS, RDS, S3, CloudFront, and more
- **Azure**: Virtual Networks, VMs, AKS, Azure SQL, Storage, CDN
- **GCP**: VPC, Compute Engine, GKE, Cloud SQL, Cloud Storage, Cloud CDN
- **IBM Cloud**: VPC, VSIs, Code Engine, Kubernetes Service, Object Storage, Databases

### Infrastructure Commands

All commands use the `.iac` namespace for infrastructure workflows:
- `/iac.principles` - Define infrastructure governance principles
- `/iac.specify` - Create cloud-agnostic infrastructure specifications
- `/iac.plan` - Generate architecture plans with cloud provider selection
- `/iac.tasks` - Break down into dependency-ordered Terraform tasks
- `/iac.implement` - Execute tasks and generate Terraform code
- `/iac.clarify` - Clarify underspecified requirements
- `/iac.analyze` - Validate consistency across specification artifacts
- `/iac.checklist` - Generate quality validation checklists

### Terraform Integration

Built-in support for Terraform workflows:
- Automatic validation with `terraform validate`, `terraform fmt`, `tflint`
- State management patterns (S3 + DynamoDB, Azure Blob, Terraform Cloud)
- Module structure for reusability across environments
- Multi-environment support (dev, staging, production)

### Infrastructure Governance

Foundational principles for infrastructure:
- **Security standards**: Encryption requirements, IAM policies, network isolation
- **Compliance frameworks**: SOC 2, HIPAA, PCI-DSS, GDPR requirements
- **Cost governance**: Budget alerts, approved instance types, cost estimation
- **Operational standards**: Monitoring requirements, backup policies, disaster recovery
- **Technology decisions**: Approved cloud providers, IaC tools, CI/CD platforms

## Infrastructure Workflow Phases

### Greenfield Infrastructure
Start from scratch with cloud-agnostic requirements:
- Define infrastructure needs without choosing a cloud provider
- AI analyzes requirements and recommends optimal cloud services
- Generate complete Terraform configurations
- Deploy production-ready infrastructure

### Multi-Cloud Exploration
Compare infrastructure approaches across cloud providers:
- Write requirements once, explore multiple cloud implementations
- Compare costs, capabilities, and operational complexity
- Make informed decisions based on actual infrastructure code
- Maintain cloud provider flexibility

### Brownfield Migration
Modernize existing infrastructure with IaC:
- Document current infrastructure as specifications
- Generate Terraform code for existing resources
- Incrementally migrate to infrastructure as code
- Modernize to newer cloud services

## Core Principles for Infrastructure

**Requirements-first thinking**: Define what infrastructure needs to accomplish (availability, performance, security, compliance) before choosing cloud services.

**Cloud provider independence**: Infrastructure requirements shouldn't assume a specific cloud provider unless there's a compelling reason.

**Governance through principles**: Encode organizational infrastructure principles (security, compliance, cost management) that guide all infrastructure decisions.

**Iterative refinement**: Infrastructure specifications go through clarification, planning, task breakdown, and consistency analysis before code generation.

**AI-powered implementation**: Advanced AI models interpret infrastructure requirements and generate production-ready Terraform code with proper module structure, security configurations, and validation.

## Why Use IaC Spec Kit?

### Speed up infrastructure development
- Generate Terraform code 5-10x faster than manual coding
- Reuse infrastructure patterns across projects
- Focus on requirements, not Terraform syntax

### Improve infrastructure quality
- Built-in security best practices and compliance frameworks
- Consistent infrastructure patterns across teams
- Validation gates before provisioning

### Enable team collaboration
- Infrastructure specialists and application developers use the same workflow
- Clear separation between requirements and implementation
- Living documentation of infrastructure decisions

### Support organizational governance
- Foundational principles encode infrastructure standards
- Compliance requirements built into specifications
- Audit trail of infrastructure decisions

## Attribution

IaC Spec Kit builds upon the [Specification-Driven Development methodology](https://github.com/github/spec-kit) created by GitHub. The core methodology, workflow patterns, and foundational principles were developed by the GitHub Spec Kit team. We are grateful for their foundational work.

For the complete Spec-Driven Development methodology, please refer to the [original GitHub Spec Kit documentation](https://github.com/github/spec-kit).

### IaC-Specific Contributions

This implementation adds substantial infrastructure-focused capabilities:
- Infrastructure command namespace (`.iac` prefix for all commands)
- Terraform-centric templates for cloud resources, networking, security, and compliance
- Cloud provider integration patterns for AWS, Azure, GCP, and IBM Cloud
- Infrastructure foundational principles for governance, security standards, and cost management
- Terraform validation workflows with `terraform validate`, `terraform fmt`, and `tflint`
- Cloud-agnostic specification patterns that work across providers
- Infrastructure-specific quality gates and analysis tools

## Contributing

We welcome contributions to IaC Spec Kit! Please open an issue or pull request on the [IaC Spec Kit GitHub repository](https://github.com/ibm/iac-spec-kit) to contribute.

## Support

For support, please open an issue on the [IaC Spec Kit GitHub repository](https://github.com/ibm/iac-spec-kit/issues).
