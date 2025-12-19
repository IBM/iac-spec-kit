# GCP Workflow for Enterprise Landing Zone

This guide shows the commands and prompts to deploy an enterprise landing zone on Google Cloud Platform using IaC Spec Kit.

## Prerequisites

- GCP Organization with admin permissions
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
/iac.specify I need an enterprise landing zone for our organization. Requirements: separate GCP projects for production, staging, development, and shared services. Centralized networking with hub-and-spoke topology. All logs aggregated to security project. Policy-based guardrails to enforce compliance. Cost tracking by environment. We need to comply with SOC 2 and must implement least-privilege access controls.
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
/iac.plan We'll use GCP Organization hierarchy with folders. Shared VPC for hub-spoke networking. Organization Policy constraints. Cloud Logging and Cloud Audit Logs. Security Command Center.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example architecture:
- Organization with folders (Production, Non-Production, Shared)
- Shared VPC in host project, service projects per environment
- Organization Policy constraints, IAM policies
- Log sink to centralized logging project
- Security Command Center, Cloud Asset Inventory

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

**Generates**: Terraform files for organization, folders, projects, networking, security, logging

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Enterprise governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | GCP-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
