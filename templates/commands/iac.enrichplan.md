---
description: Enrich an existing plan with deep research, architecture details, module specifications, and quickstart guide. Updates plan.md with research findings.
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

## Prerequisites

- `plan.md` must exist (run `/iac.plan` first)
- This command enriches an existing plan - it does not create one

## Pre-Execution Checks

**Check for extension hooks (before enrichment)**:

- Check if `.specify/extensions.yml` exists in the project root.
- If it exists, read it and look for entries under the `hooks.before_iac_enrichplan` key
- If the YAML cannot be parsed or is invalid, skip hook checking silently and continue normally
- Filter out hooks where `enabled` is explicitly `false`. Treat hooks without an `enabled` field as enabled by default.
- For each remaining hook, do **not** attempt to interpret or evaluate hook `condition` expressions:
  - If the hook has no `condition` field, or it is null/empty, treat the hook as executable
  - If the hook defines a non-empty `condition`, skip the hook and leave condition evaluation to the HookExecutor implementation
- For each executable hook, output the following based on its `optional` flag:
  - **Optional hook** (`optional: true`):

    ```text
    ## Extension Hooks

    **Optional Pre-Hook**: {extension}
    Command: `/{command}`
    Description: {description}

    Prompt: {prompt}
    To execute: `/{command}`
    ```

  - **Mandatory hook** (`optional: false`):

    ```text
    ## Extension Hooks

    **Automatic Pre-Hook**: {extension}
    Executing: `/{command}`
    EXECUTE_COMMAND: {command}

    Wait for the result of the hook command before proceeding to the Outline.
    ```
    After emitting the block above you MUST actually invoke the hook and wait for it to finish before continuing. Run it the same way you would run the command yourself in this agent/session (the invocation may differ from the literal `{command}` id shown above, e.g. a skills-mode agent runs it as `/skill:speckit-...` or `$speckit-...`). Emitting the block alone does not run the hook.

- If no hooks are registered or `.specify/extensions.yml` does not exist, skip silently

## Outline

1. **Setup**: Run `{SCRIPT}` from repo root and parse JSON for ARCH_PLAN, SPECS_DIR, BRANCH.

2. **Validate**: Confirm ARCH_PLAN (plan.md) exists. If not, instruct user to run `/iac.plan` first.

3. **Load context**: Read plan.md and `memory/principles.md` to understand:
   - Cloud provider and IaC tool decisions (already made in plan)
   - Infrastructure architecture requirements
   - Complexity level (Baseline vs Enhanced)

4. **Execute enrichment workflow**:
   - Phase 0: Deep research → `research.md`
   - Phase 1: Architecture details → `architecture.md`, `modules.md`, `quickstart.md`
   - Update plan.md with research findings
   - Re-evaluate Principles Check post-design

5. **Update agent context**: Run `{AGENT_SCRIPT}`.

6. **Report**: List generated artifacts and next steps.

## Phases

### Phase 0: Technology Selection & Research

1. **Extract from plan.md**:
   - Cloud provider and IaC tool (already decided)
   - Infrastructure components to research
   - State management strategy
   - Multi-environment approach

2. **Generate and dispatch research agents**:

   ```text
   For well-architected framework (MANDATORY REFERENCE):
     Task: "Study {cloud provider} Well-Architected Framework / Best practices and document applicable pillars/principles:
       - AWS: 6 pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability)
       - Azure: 5 pillars (Cost Optimization, Operational Excellence, Performance Efficiency, Reliability, Security)
       - GCP: 5 principles (Operational Excellence, Security Privacy & Compliance, Reliability, Cost Optimization, Performance & Scalability)
       - IBM Cloud: Use the Framework for Financial Services and IBM Cloud best practices
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
     For production stability: Recommend exact version pinning (= X.Y.Z) for modules since they are NOT captured in .terraform.lock.hcl.
     For development: ~> X.Y allows flexibility for testing minor updates.
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

**Output**: `research.md` with comprehensive research. This single file consolidates ALL research findings - do not create separate files for module research, provider analysis, or other research topics.

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

3. **Create provisioning guide** → `quickstart.md`:
   - Prerequisites (tools, accounts, credentials)
   - State backend setup if any (no state backend setup if using local, or managed iac service such as HashiCorp Terraform Cloud or IBM Cloud Schematics)
   - Provisioning commands (init, plan, apply)
   - Manual validation steps
   - Rollback procedures
   **IMPORTANT**: ❌ Do NOT include IaC code, e.g: terraform code in this file. The IaC code will be generated in next phase by /iac.implement command.

4. **Update plan.md**:
   - Update Technical Context with any refined versions from research
   - Update Module Versions with specific versions from research
   - Re-evaluate Principles Check post-design

5. **Agent context update**:
   - Run `{AGENT_SCRIPT}`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add cloud provider and IaC tool to technology stack
   - Preserve manual additions between markers

**Output**: `architecture.md`, `modules.md`, `quickstart.md`, updated `plan.md`, agent-specific file updated.

## Key Rules

- Requires existing plan.md - do not proceed without it
- Use absolute paths
- research.md consolidates ALL research - no separate files
- No IaC code in quickstart.md
- Update plan.md with research findings at the end
