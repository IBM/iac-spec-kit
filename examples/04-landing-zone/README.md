# Example: Enterprise Landing Zone

**Complexity**: Medium-High
**Estimated Time**: 1-2 hours
**Best For**: Enterprise teams, cloud platform teams, governance-focused organizations

## Overview

This example demonstrates how to establish an enterprise-grade cloud landing zone—the foundational infrastructure that organizations need before deploying applications. A landing zone provides security, governance, networking, and identity management for multi-account/subscription cloud environments.

## What You'll Build

A comprehensive landing zone foundation including:

- Multi-account/subscription structure (production, staging, development, shared services)
- Centralized identity and access management
- Hub-and-spoke network topology with transit gateway/peering
- Security baseline (logging, monitoring, compliance controls)
- Centralized logging and audit trail
- Policy enforcement and guardrails
- Cost management and billing alerts
- Automated compliance scanning

## Use Case

**Scenario**: Your organization is moving to the cloud and needs a secure, compliant foundation before deploying applications. You need separation between environments (prod/dev), centralized security monitoring, network connectivity between accounts, and compliance with industry frameworks (SOC2, PCI-DSS, HIPAA, etc.).

## Learning Objectives

This example teaches you:

1. **Enterprise governance patterns**: Multi-account strategies, policy enforcement, compliance controls
2. **Complex infrastructure specifications**: How to describe enterprise requirements in cloud-agnostic terms
3. **Hub-and-spoke networking**: Central connectivity hub with spoke networks for workloads
4. **Security and compliance**: Expressing regulatory requirements without cloud-specific services
5. **Separation of concerns**: Organizing infrastructure by function (networking, security, identity, logging)

## Prerequisites

- Cloud account with organization/management group permissions
- IaC Spec Kit installed (`iac-specify check`)
- Terraform installed
- AI coding assistant running in your project directory
- Understanding of your organization's compliance requirements

## Get Started

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS Workflow](./cloud-workflows/aws.md)** - AWS Organizations, Control Tower, Transit Gateway, Security Hub
- **[Azure Workflow](./cloud-workflows/azure.md)** - Management Groups, Landing Zones, Virtual WAN, Azure Policy
- **[GCP Workflow](./cloud-workflows/gcp.md)** - Organization, Folders, Shared VPC, Security Command Center
- **[IBM Cloud Workflow](./cloud-workflows/ibm-cloud.md)** - Enterprise Account Groups, Transit Gateway, Security and Compliance Center

## What Makes This Example Complex

- **Multi-account/subscription architecture**: Requires organization-level permissions and understanding
- **Multiple infrastructure tiers**: Networking, security, identity, logging all interrelated
- **Compliance requirements**: Must map to regulatory frameworks
- **Operational complexity**: Sets foundation for all future applications

## Common Compliance Frameworks

This landing zone pattern helps with:

- SOC 2 Type II (System and Organization Controls)
- PCI-DSS (Payment Card Industry Data Security Standard)
- HIPAA (Health Insurance Portability and Accountability Act)
- ISO 27001 (Information Security Management)
- FedRAMP (Federal Risk and Authorization Management Program)
- GDPR (General Data Protection Regulation)

## Next Steps

After completing this example:

1. Deploy **[05-three-tier-webapp](../05-three-tier-webapp/)** into your landing zone
2. Add **[07-microservices](../07-microservices/)** platform on top of the foundation
3. Implement **[06-data-pipeline](../06-data-pipeline/)** in the shared services account
