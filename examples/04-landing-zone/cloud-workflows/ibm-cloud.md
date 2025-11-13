# IBM Cloud Workflow for Enterprise Landing Zone

This guide shows the commands and prompts to deploy an enterprise landing zone on IBM Cloud using IaC Spec Kit.

## Prerequisites

- IBM Cloud Enterprise account
- IBM Cloud CLI configured
- IaC Spec Kit installed
- Terraform installed

## Commands

### Step 1: Establish Project Principles

```
/iac.principles I'm building an enterprise cloud landing zone on IBM Cloud for a regulated industry. Security and compliance are critical. Multiple environments need isolation. Use Terraform with terraform-ibm-modules.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need an enterprise landing zone for our organization. Requirements: separate account groups for production, staging, development, and shared services. Centralized networking with hub-and-spoke topology. All logs aggregated to security account. Policy-based guardrails to enforce compliance. Cost tracking by environment. We need to comply with SOC 2 and Financial Services Cloud requirements.
```

**Generates**: `spec.md`, `checklists/requirements.md`

---

### Step 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan We'll use IBM Cloud Enterprise account groups. Transit Gateway for networking. Security and Compliance Center for compliance. Activity Tracker and Log Analysis for centralized logging.
```

**plan.md** example architecture:
- Enterprise with account groups (Production, Development, Shared Services)
- Transit Gateway with VPCs per environment
- IAM policies and access groups
- Activity Tracker event routing, Log Analysis
- Security and Compliance Center with Financial Services profile

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform files for enterprise structure, account groups, networking, security, compliance

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Enterprise governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.plan` | `plan.md`, etc. | IBM Cloud-specific architecture |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
