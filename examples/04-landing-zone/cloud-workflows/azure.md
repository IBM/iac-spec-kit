# Azure Workflow for Enterprise Landing Zone

This guide shows the commands and prompts to deploy an enterprise landing zone on Azure using IaC Spec Kit.

## Prerequisites

- Azure subscription with Management Group permissions
- IaC Spec Kit installed
- Terraform installed
- AI coding assistant running

## Commands

### Step 1: Establish Project Principles

```
/iac.principles I'm building an enterprise cloud landing zone on Azure for a regulated industry. Security and compliance are critical. Multiple environments need isolation. Use Terraform with Azure Verified Modules.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need an enterprise landing zone for our organization. Requirements: separate subscriptions for production, staging, development, and shared services. Centralized networking with hub-and-spoke topology. All logs aggregated to security subscription. Policy-based guardrails to enforce compliance. Cost tracking by environment. We need to comply with SOC 2 and must implement least-privilege access controls.
```

**Generates**: `spec.md`, `checklists/requirements.md`

---

### Step 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan We'll use Azure Landing Zones framework. Virtual WAN or hub-spoke VNet peering. Azure Policy for compliance. Log Analytics for centralized logging. Microsoft Defender for Cloud for security.
```

**plan.md** example architecture:
- Management Groups with subscription organization
- Hub VNet with Azure Firewall, spoke VNets per environment
- Azure Policy assignments, Azure Blueprints
- Log Analytics workspace, Microsoft Sentinel
- Azure AD with Privileged Identity Management

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform files for management groups, networking, security, policy enforcement

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Enterprise governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.plan` | `plan.md`, etc. | Azure-specific architecture |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
