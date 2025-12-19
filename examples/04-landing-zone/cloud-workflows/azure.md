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
/iac.principles This is an enterprise landing zone for a regulated industry. Security and compliance are critical. Multiple environments need strong isolation. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need an enterprise landing zone for our organization. Requirements: separate subscriptions for production, staging, development, and shared services. Centralized networking with hub-and-spoke topology. All logs aggregated to security subscription. Policy-based guardrails to enforce compliance. Cost tracking by environment. We need to comply with SOC 2 and must implement least-privilege access controls.
```

**Generates**: `spec.md`, `checklists/requirements.md`

---

### Step 3: Clarify Requirements (Optional)

```
/iac.clarify
```

---

### Step 4: Create Implementation Plan

```
/iac.plan We'll use Azure Landing Zones framework. Virtual WAN or hub-spoke VNet peering. Azure Policy for compliance. Log Analytics for centralized logging. Microsoft Defender for Cloud for security.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example architecture:
- Management Groups with subscription organization
- Hub VNet with Azure Firewall, spoke VNets per environment
- Azure Policy assignments, Azure Blueprints
- Log Analytics workspace, Microsoft Sentinel
- Azure AD with Privileged Identity Management

---

### Step 5: Generate Task Breakdown

```
/iac.tasks
```

**Generates**: `tasks.md` with phased implementation

---

### Step 6: Implement Infrastructure Code

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
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | Azure-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
