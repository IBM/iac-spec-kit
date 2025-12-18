---
description: Create an architecture plan from an infrastructure specification. Outputs plan.md with lightweight research inline.
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
agent_scripts:
  sh: scripts/bash/update-agent-context.sh __AGENT__
  ps: scripts/powershell/update-agent-context.ps1 -AgentType __AGENT__
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `{SCRIPT}` from repo root and parse JSON for INFRA_SPEC, ARCH_PLAN, SPECS_DIR, BRANCH.

2. **Load context**: Read INFRA_SPEC and load ARCH_PLAN template (already copied by script).

3. **Check principles**:
   - Read `memory/principles.md`
   - If file contains `[ARCHITECTURE_PRINCIPLE_` or `[PROJECT_NAME]` placeholders → principles NOT configured, skip Principles Check section
   - If placeholders are filled → apply principles to plan, fill Principles Check section

4. **Lightweight research**: Quick research to inform technology decisions:
   - Current stable versions for chosen IaC tool and cloud provider
   - Basic curated module recommendations (names only, not deep analysis)
   - Common patterns for the infrastructure type

5. **Fill plan.md**: Complete ALL sections in ARCH_PLAN template:
   - Summary (from spec)
   - Technical Context (cloud provider, IaC tool, versions from research)
   - Principles Check (if principles configured, else note "Principles not configured - run /iac.principles first")
   - Infrastructure Architecture (all subsections: Compute, Storage, Networking, Security, Environment, Complexity, State)
   - Project Structure (select appropriate option, remove unused)

6. **Update agent context**: Run `{AGENT_SCRIPT}` to update agent-specific context file.

7. **Report**: Output branch, plan.md path. Note that `/iac.enrichplan` is available for deep research, modules, and quickstart.

## Workflow

### Step 1: Analyze Specification

Read INFRA_SPEC and extract:
- Primary capability and purpose
- Infrastructure requirements (compute, storage, networking)
- Security and compliance needs
- Environment strategy (dev/staging/prod)
- Any technology preferences or constraints

### Step 2: Lightweight Research

Perform quick research to inform decisions (NOT deep analysis):

**Version Research** (required):
- Current stable Terraform version (or chosen IaC tool)
- Current stable provider version for chosen cloud
- Recommended provider version constraints (e.g., `>= 5.0, < 6.0`)

**Module Discovery** (brief):
- Identify relevant curated modules for main components:
  - AWS: terraform-aws-modules
  - Azure: Azure Verified Modules  
  - IBM Cloud: terraform-ibm-modules
  - GCP: terraform-google-modules
- Note module names only (e.g., "terraform-aws-modules/vpc/aws")
- Skip deep configuration analysis (that's for `/iac.enrichplan`)

**Pattern Check** (quick):
- Standard patterns for this infrastructure type (e.g., 3-tier web app, data pipeline)
- Common pitfalls to avoid

This research informs the Technical Context section - no separate research.md file.

### Step 3: Make Technology Decisions

Based on spec requirements and lightweight research, decide:
- **Cloud Provider**: AWS, Azure, GCP, IBM Cloud, or multi-cloud
- **IaC Tool**: Terraform, Pulumi, CloudFormation (recommend Terraform as default)
- **Provider Versions**: Pin to stable versions from research
- **Curated Modules**: List recommended modules (names and versions)
- **State Backend**: Local (POC), S3+DynamoDB (AWS), COS (IBM), etc.
- **Environment Strategy**: Workspaces, separate state files, or directory-based

### Step 4: Design Infrastructure Architecture

For each section in plan.md, provide concrete details:

**Compute Resources**: Document instance types, scaling policies, container specs
**Data Storage**: Databases, object storage, caching with capacity and backup strategies  
**Networking**: VPC/subnets with CIDR ranges, routing, DNS, load balancing
**Security**: IAM policies, security groups, encryption, secrets management
**Environment Configuration**: Variable differences between dev/staging/prod
**Complexity Level**: Baseline (POC/dev) vs Enhanced (staging/prod) with rationale
**State Management**: Backend configuration, locking, backup strategy

### Step 5: Select Project Structure

Choose ONE structure option from the template:
- **Option 1**: Simple Terraform (single main.tf) - for POC/demo
- **Option 2**: Terraform Infrastructure (organized files) - DEFAULT for IaC
- **Option 3**: Pulumi Infrastructure
- **Option 4**: CloudFormation Infrastructure

Remove unused options. Document the selection rationale.

## Output

**Single artifact**: `plan.md` - Complete architecture plan with technology decisions informed by lightweight research.

**Next steps for user**:
- Run `/iac.tasks` to break plan into implementation tasks
- OR run `/iac.enrichplan` first if you need:
  - Deep research (Well-Architected Framework analysis, detailed module configurations)
  - Module specifications (modules.md) with input/output details
  - Provisioning quickstart guide (quickstart.md)

## Key Rules

- Use absolute paths
- Research is lightweight and inline - no separate research.md file
- Complete ALL sections in plan.md (make decisions, don't defer)
- If principles not configured, note it but proceed with planning
