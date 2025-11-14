---
description: Execute the infrastructure implementation by processing and executing all tasks defined in tasks.md
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## CRITICAL: Code Generation vs Deployment

**This command generates infrastructure-as-code files ONLY. It does NOT deploy actual cloud resources.**

Understanding this distinction is essential before proceeding with implementation.

### What this command DOES:
- Generates .tf files (or equivalent IaC code) based on architecture plan
- Applies code formatting and validates syntax
- Creates documentation and deployment guides
- Ensures code follows foundational principles and best practices

### What this command does NOT do:
- Deploy/provision actual cloud resources (terraform apply, pulumi up, etc.)
- Manage Terraform state or infrastructure lifecycle
- Handle operational concerns (monitoring, incident response, day-2 operations)
- Execute actual infrastructure changes in your cloud account

### Next steps after code generation:
1. Review generated code for correctness and completeness
2. Run validation: `terraform plan` (or `pulumi preview`, `cloudformation validate-template`)
3. Review plan output to understand what will be created
4. Deploy infrastructure: `terraform apply` (or equivalent) - YOUR responsibility, outside this framework
5. Manage infrastructure lifecycle using your preferred deployment workflow

---

## Outline

1. Run `{SCRIPT}` from repo root and parse INFRA_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Check checklists status** (if INFRA_DIR/checklists/ exists):
   - Scan all checklist files in the checklists/ directory
   - For each checklist, count:
     - Total items: All lines matching `- [ ]` or `- [X]` or `- [x]`
     - Completed items: Lines matching `- [X]` or `- [x]`
     - Incomplete items: Lines matching `- [ ]`
   - Create a status table:

     ```text
     | Checklist | Total | Completed | Incomplete | Status |
     |-----------|-------|-----------|------------|--------|
     | security.md | 12  | 12        | 0          | ✓ PASS |
     | compliance.md | 8 | 5         | 3          | ✗ FAIL |
     | cost.md   | 6     | 6         | 0          | ✓ PASS |
     ```

   - Calculate overall status:
     - **PASS**: All checklists have 0 incomplete items
     - **FAIL**: One or more checklists have incomplete items

   - **If any checklist is incomplete**:
     - Display the table with incomplete item counts
     - **STOP** and ask: "Some checklists are incomplete. Do you want to proceed with implementation anyway? (yes/no)"
     - Wait for user response before continuing
     - If user says "no" or "wait" or "stop", halt execution
     - If user says "yes" or "proceed" or "continue", proceed to step 3

   - **If all checklists are complete**:
     - Display the table showing all checklists passed
     - Automatically proceed to step 3

3. Load and analyze the implementation context:
   - **REQUIRED**: Read tasks.md for the complete task list and execution plan
   - **REQUIRED**: Read plan.md for cloud provider, IaC tool, architecture, and file structure
   - **IF EXISTS**: Read architecture.md for detailed infrastructure design
   - **IF EXISTS**: Read modules.md for module specifications
   - **IF EXISTS**: Read research.md for technology decisions
   - **IF EXISTS**: Read quickstart.md for deployment procedures

4. **Project Setup Verification**:
   - **REQUIRED**: Create/verify ignore files based on actual project setup:

   **Detection & Creation Logic**:
   - Check if the following command succeeds to determine if the repository is a git repo (create/verify .gitignore if so):

     ```sh
     git rev-parse --git-dir 2>/dev/null
     ```

   - Check if Dockerfile* exists or Docker in plan.md → create/verify .dockerignore
   - Check if .eslintrc*or eslint.config.* exists → create/verify .eslintignore
   - Check if .prettierrc* exists → create/verify .prettierignore
   - Check if .npmrc or package.json exists → create/verify .npmignore (if publishing)
   - Check if terraform files (*.tf) exist → create/verify .terraformignore
   - Check if .helmignore needed (helm charts present) → create/verify .helmignore

   **If ignore file already exists**: Verify it contains essential patterns, append missing critical patterns only
   **If ignore file missing**: Create with full pattern set for detected technology

   **Common Patterns by Technology** (from plan.md tech stack):
   - **Node.js/JavaScript/TypeScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
   - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
   - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
   - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
   - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
   - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `Makefile`, `config.log`, `.idea/`, `*.log`, `.env*`
   - **Swift**: `.build/`, `DerivedData/`, `*.swiftpm/`, `Packages/`
   - **R**: `.Rproj.user/`, `.Rhistory`, `.RData`, `.Ruserdata`, `*.Rproj`, `packrat/`, `renv/`
   - **Universal**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **Tool-Specific Patterns**:
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`, `crash.log`, `override.tf`, `override.tf.json`
   - **Pulumi**: `node_modules/` (TS/JS), `__pycache__/` (Python), `bin/`, `obj/` (.NET), `Pulumi.*.yaml` (may contain secrets)
   - **CloudFormation**: `packaged-*.yaml`, `.aws-sam/`
   - **Kubernetes/k8s**: `*.secret.yaml`, `secrets/`, `.kube/`, `kubeconfig*`, `*.key`, `*.crt`

5. Parse tasks.md structure and extract:
   - **Task phases**: Organized by infrastructure tiers as defined in tasks.md
   - **Task dependencies**: Sequential vs parallel execution rules from task structure
   - **Task details**: ID, description, file paths, parallel markers [P]
   - **Execution flow**: Phase order and validation checkpoints as specified

6. Execute implementation following the task plan:
   - **Phase-by-phase execution**: Complete each phase before moving to the next
   - **Respect tier dependencies**: Follow the dependency hierarchy defined in tasks.md
   - **Run sequential tasks in order**: Tasks marked [P] can run in parallel within same phase
   - **File-based coordination**: Tasks affecting the same files must run sequentially
   - **Validation checkpoints**: Run validation commands (e.g., `terraform validate`) as specified in tasks

7. Implementation execution rules for infrastructure code generation:
   - **Generate IaC files**: Create .tf files, .yaml files, or language-specific IaC code as specified
   - **Follow tier dependencies**: Respect resource dependencies defined in architecture
   - **Apply validation**: Run syntax validation after each major phase
   - **Format code**: Apply code formatting (e.g., `terraform fmt`) as specified
   - **Generate documentation**: Create README, outputs, and deployment guides as specified
   - **Note**: This generates infrastructure code only - actual deployment (terraform apply, etc.) is outside scope

8. Progress tracking and error handling:
   - Report progress after each completed task
   - Halt execution if any non-parallel task fails
   - For parallel tasks [P], continue with successful tasks, report failed ones
   - Provide clear error messages with context for debugging
   - Suggest next steps if implementation cannot proceed
   - **IMPORTANT** For completed tasks, make sure to mark the task off as [X] in the tasks file.

9. Completion validation:
   - Verify all required tasks are completed and marked [X] in tasks.md
   - Check that generated IaC code matches the specification and architecture design
   - Validate that syntax validation passes (e.g., `terraform validate`, `pulumi preview`)
   - Verify code formatting is applied and consistent
   - Confirm the implementation follows the technical plan and principles requirements
   - Report final status with summary of completed phases and generated files

**Note**: This command assumes a complete task breakdown exists in tasks.md. If tasks are incomplete or missing, suggest running `/iac.tasks` first to regenerate the task list.

