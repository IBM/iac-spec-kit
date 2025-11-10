---
description: Generate an actionable, dependency-ordered tasks.md for the infrastructure based on available design artifacts.
scripts:
  sh: scripts/bash/check-prerequisites.sh --json
  ps: scripts/powershell/check-prerequisites.ps1 -Json
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `{SCRIPT}` from repo root and parse INFRA_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from INFRA_DIR:
   - **Required**: plan.md (cloud provider, IaC tool, structure), spec.md (infrastructure requirements)
   - **Optional**: architecture.md (detailed design), modules.md (module specs), research.md (technology decisions), quickstart.md (deployment guide)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract cloud provider, IaC tool, state backend, project structure
   - Load spec.md and extract infrastructure requirements with priorities (Must Have, Should Have)
   - If architecture.md exists: Extract resource specifications and dependencies
   - If modules.md exists: Map modules to infrastructure requirements
   - If research.md exists: Extract technology decisions for setup tasks
   - Generate tasks organized by infrastructure layer and dependencies (see Task Generation Rules below)
   - Generate dependency graph showing infrastructure provisioning order
   - Create parallel execution examples for independent resources
   - Validate task completeness (proper dependency ordering, validation checkpoints)

4. **Generate tasks.md**: Use `.specify/templates/tasks-template.md` as structure, fill with:
   - Correct infrastructure name from plan.md
   - Phase 1: Setup tasks (IaC project initialization, backend configuration)
   - Phase 2: Foundation tier (state backend, provider configuration)
   - Phase 3: Network tier (VPC, subnets, security groups, routing)
   - Phase 4: Compute & Data tier (instances, databases, storage, load balancers)
   - Phase 5: Application tier (DNS, monitoring, application configuration)
   - Final Phase: Validation & documentation
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task (iac/vpc.tf, iac/compute.tf, etc.)
   - Dependencies section showing infrastructure provisioning order
   - Parallel execution examples for independent resources
   - Validation checkpoints after each tier

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per infrastructure tier
   - Parallel opportunities identified
   - Validation checkpoints defined
   - Deployment order (dev → staging → prod)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: {ARGS}

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by infrastructure tier following dependency hierarchy (Foundation → Network → Compute/Data → Application).

**Validation checkpoints are REQUIRED**: Include `terraform validate` or equivalent after each major tier completion.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **Description**: Clear action with exact file path and infrastructure component

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create iac/ directory structure per plan.md`
- ✅ CORRECT: `- [ ] T002 [P] Configure Terraform backend in iac/backend.tf`
- ✅ CORRECT: `- [ ] T007 [P] Create VPC and subnets in iac/vpc.tf`
- ✅ CORRECT: `- [ ] T010 Create security groups in iac/security-groups.tf`
- ❌ WRONG: `- [ ] Create VPC` (missing ID and file path)
- ❌ WRONG: `T001 Create VPC` (missing checkbox)
- ❌ WRONG: `- [ ] Create VPC in iac/vpc.tf` (missing Task ID)
- ❌ WRONG: `- [ ] T001 Create VPC` (missing file path)

### Task Organization

1. **From Infrastructure Requirements (spec.md)** - PRIMARY ORGANIZATION:
   - Extract all Must Have and Should Have requirements
   - Map requirements to infrastructure resources (compute, storage, networking, security)
   - Organize resources by tier based on dependencies

2. **From Architecture Design (architecture.md)**:
   - Extract compute resources → Compute & Data tier
   - Extract storage resources → Compute & Data tier
   - Extract network resources → Network tier
   - Extract security configurations → Network tier (security groups) and throughout

3. **From Modules (modules.md)**:
   - If using modules: Create module directory structure in Setup phase
   - Module implementation → appropriate tier based on module purpose
   - Module dependencies → ensure parent resources exist first

4. **Infrastructure Tier Organization**:
   - **Setup (Phase 1)**: IaC project initialization, directory structure
   - **Foundation (Phase 2)**: State backend, provider configuration, version constraints
   - **Network (Phase 3)**: VPC, subnets, routing, security groups, NAT gateways, IAM roles
   - **Compute & Data (Phase 4)**: Instances, databases, storage buckets, load balancers, caching
   - **Application (Phase 5)**: DNS, CDN, monitoring, alerting, application-specific config
   - **Validation (Final)**: Documentation, formatting, linting, final validation

### Phase Structure

- **Phase 1**: Setup (IaC project initialization, directory structure)
- **Phase 2**: Foundation (state backend, provider configuration - MUST complete before infrastructure)
- **Phase 3**: Network Tier (VPC, subnets, security groups, routing - BLOCKS compute resources)
- **Phase 4**: Compute & Data Tier (instances, databases, storage, load balancers - depends on Network)
- **Phase 5**: Application Tier (DNS, monitoring, application configuration - depends on Compute & Data)
- **Final Phase**: Validation & Documentation (formatting, linting, validation, documentation)
