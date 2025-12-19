# IBM Cloud Workflow for Enterprise Landing Zone

This guide shows the commands and prompts to deploy an enterprise landing zone on IBM Cloud using IaC Spec Kit.

## Prerequisites

- IBM Cloud Enterprise account
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
/iac.specify I need an enterprise landing zone for our organization. Requirements: separate account groups for production, staging, development, and shared services. Centralized networking with hub-and-spoke topology. All logs aggregated to security account. Policy-based guardrails to enforce compliance. Cost tracking by environment. We need to comply with SOC 2 and Financial Services Cloud requirements.
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
/iac.plan We'll use IBM Cloud Enterprise account groups. Transit Gateway for networking. Security and Compliance Center for compliance. Activity Tracker and Log Analysis for centralized logging.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example architecture:
- Enterprise with account groups (Production, Development, Shared Services)
- Transit Gateway with VPCs per environment
- IAM policies and access groups
- Activity Tracker event routing, Log Analysis
- Security and Compliance Center with Financial Services profile

---

### Step 5: Generate Task Breakdown

```
/iac.tasks
```

**Generates**: `tasks.md` with phased implementation

---

### Step 6: Implement Infrastructure Code

```
/iac.implement
```

**Generates**: Terraform files for enterprise structure, account groups, networking, security, compliance

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Enterprise governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | IBM Cloud-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
