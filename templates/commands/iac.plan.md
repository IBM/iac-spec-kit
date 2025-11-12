---
description: Execute the architecture planning workflow using the plan template to generate infrastructure design artifacts.
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

1. **Setup**: Run `{SCRIPT}` from repo root and parse JSON for INFRA_SPEC, ARCH_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read INFRA_SPEC and `./specify/memory/principles.md`. Load ARCH_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in ARCH_PLAN template to:
   - Fill Technical Context (cloud provider, IaC tool, versions - mark unknowns as "NEEDS CLARIFICATION")
   - Fill Principles Check section from principles (technology stack validation)
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve cloud/tool selection, best practices)
   - Phase 1: Design Infrastructure Architecture (compute, storage, networking, security, state management)
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Principles Check post-design

4. **Stop and report**: Command ends after Phase 1 planning. Report branch, ARCH_PLAN path, and generated artifacts.

## Phases

### Phase 0: Technology Selection & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - Cloud provider selection (if not specified in principles)
   - IaC tool and version (if not specified in principles)
   - State management strategy
   - Multi-environment approach
   - Infrastructure patterns and best practices

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {infrastructure context}"
   For IaC tool (if not specified):
     Task: "Best practices for {Terraform/Pulumi/CloudFormation} for {use case} on {cloud provider}"
   For well-architected framework (MANDATORY REFERENCE):
     Task: "Study {cloud provider} Well-Architected Framework and document applicable pillars/principles:
       - AWS: 6 pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability)
       - Azure: 5 pillars (Cost Optimization, Operational Excellence, Performance Efficiency, Reliability, Security)
       - GCP: 5 principles (Operational Excellence, Security Privacy & Compliance, Reliability, Cost Optimization, Performance & Scalability)
       - IBM Cloud: Framework for Financial Services & IBM Cloud best practices
     Map framework recommendations to infrastructure requirements.
     Identify which pillar applies to each component and document specific best practices to follow."
   For curated modules (PREFERRED APPROACH):
     Task: "Identify and recommend curated modules as the PRIMARY implementation approach:
       - AWS: terraform-aws-modules (Terraform Registry verified)
       - Azure: Azure Verified Modules (Microsoft official)
       - IBM Cloud: terraform-ibm-modules (IBM official)
       - GCP: terraform-google-modules (Google Cloud official)
       - Pulumi: Official Pulumi packages for each cloud provider
     Document specific modules for each infrastructure component (VPC, compute, database, etc.).
     Only recommend direct provider resources when: custom requirements not supported by modules, very simple single resources, or modules add unnecessary complexity.
     Provide rationale for any direct resource usage."
   For patterns:
     Task: "Research {multi-region/DR/state-management/scaling} patterns on {cloud provider}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen - cloud provider, IaC tool, versions]
   - Rationale: [why chosen - cost, features, team expertise, ecosystem]
   - Alternatives considered: [what else evaluated and why rejected]
   - Well-Architected Framework (MANDATORY): [applicable pillars/principles mapped to infrastructure components with specific best practices]
   - Curated Modules (PRIMARY APPROACH): [specific modules/packages identified for each component with versions, rationale for any direct resource usage]
   - Best practices: [key patterns to follow]
   - References: [documentation links, examples, module registries]

**Output**: `research.md` with all NEEDS CLARIFICATION resolved

### Phase 1: Infrastructure Architecture Design

**Prerequisites:** `research.md` complete with all technology decisions made

1. **Design infrastructure architecture** → `architecture.md`:
   - Compute Resources: instances, containers, serverless, auto-scaling
   - Data Storage: databases, object storage, caching, backups
   - Networking: VPC/VNet, subnets, routing, DNS, load balancing
   - Security: IAM/RBAC, security groups, encryption, secrets
   - Environment Configuration: dev/staging/prod differences
   - State Management: backend, locking, backup strategy

2. **Define module specifications** (if using modules) → `modules.md`:
   - Module name and purpose
   - Input variables with validation
   - Output values
   - Dependencies between modules
   - Testing strategy

3. **Create deployment guide** → `quickstart.md`:
   - Prerequisites (tools, accounts, credentials)
   - State backend setup
   - Variable configuration per environment
   - Deployment commands (init, plan, apply)
   - Validation steps
   - Rollback procedures

4. **Agent context update**:
   - Run `{AGENT_SCRIPT}`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add cloud provider and IaC tool to technology stack
   - Preserve manual additions between markers

**Output**: `architecture.md`, `modules.md`, `quickstart.md`, agent-specific file updated

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications
