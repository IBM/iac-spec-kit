---

description: "Task list template for infrastructure implementation"
---

# Tasks: [INFRASTRUCTURE NAME]

**Input**: Design documents from `/specs/[###-infrastructure-name]/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, architecture.md, modules.md, quickstart.md

**Note**: The examples below show infrastructure implementation tasks organized by tier.

**Organization**: Tasks grouped by infrastructure tier following dependency hierarchy (Foundation → Network → Compute/Data → Application)

## Format: `[ID] [P?] Description`

- **[ID]**: Sequential task number (T001, T002, T003...)
- **[P]**: Can run in parallel (different files, no dependencies) - optional
- **Description**: Clear action with exact file path included

Tasks are organized by infrastructure tier in the phase structure below

## Path Conventions

- **IaC files**: `iac/` at repository root
- **Terraform**: `iac/*.tf`, `iac/terraform.tfvars.{env}`, `iac/modules/`
- **Pulumi**: `iac/*.ts` or `iac/*.py`, `Pulumi.{stack}.yaml`
- **CloudFormation**: `iac/*.yaml`, `iac/parameters/`

Paths shown below are examples - adjust based on structure defined in plan.md

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /iac.tasks command MUST replace these with actual tasks based on:
  - Infrastructure requirements from spec.md (Must Have, Should Have priorities)
  - Architecture design from plan.md and architecture.md
  - Resource specifications and dependencies
  - Module definitions from modules.md (if using modules)

  Tasks MUST be organized by infrastructure tier following dependency hierarchy:
  - Foundation → Network → Compute/Data → Application
  - Each tier must complete before the next can begin
  - Resources within a tier can execute in parallel where independent

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup

**Purpose**: IaC project initialization and directory structure

<!-- Terraform Example (IBM Cloud): -->
- [ ] T001 Create iac/ directory structure per plan.md
- [ ] T002 [P] Configure Terraform backend (IBM Cloud Object Storage) in iac/backend.tf
- [ ] T003 [P] Configure IBM Cloud provider in iac/provider.tf
- [ ] T004 [P] Create versions.tf with Terraform and ibm provider version constraints
- [ ] T005 Create terraform.tfvars files for each environment (dev/staging/prod)
- [ ] T006 Run `terraform init` to initialize backend and download providers
- [ ] T007 Run `terraform validate` - setup checkpoint

<!-- Pulumi Example (IBM Cloud):
- [ ] T001 Create iac/ directory structure per plan.md
- [ ] T002 Initialize Pulumi project with `pulumi new`
- [ ] T003 [P] Configure Pulumi backend (Pulumi Cloud or IBM COS)
- [ ] T004 [P] Create Pulumi.dev.yaml, Pulumi.staging.yaml, Pulumi.prod.yaml stack configs
- [ ] T005 Install required dependencies including @pulumi/ibm
- [ ] T006 Run `pulumi preview` - setup checkpoint
-->

---

## Phase 2: Network Tier

**Purpose**: Network infrastructure - prerequisite for all compute/data resources

**⚠️ CRITICAL**: Network tier MUST complete before compute resources can be provisioned

<!-- Terraform Example (IBM Cloud): -->
- [ ] T008 Create VPC with address prefixes per plan.md in iac/vpc.tf
- [ ] T009 [P] Create subnets across zones (us-south-1, us-south-2, us-south-3) in iac/vpc.tf
- [ ] T010 [P] Create Public Gateway for private subnet internet access in iac/vpc.tf
- [ ] T011 [P] Attach Public Gateway to subnets in iac/vpc.tf
- [ ] T012 [P] Create security groups (load balancer, compute, database) in iac/security-groups.tf
- [ ] T013 [P] Create network ACLs for subnet-level security in iac/network-acls.tf
- [ ] T014 [P] Create IAM access groups and policies in iac/iam.tf
- [ ] T015 [P] Create resource groups for environment organization in iac/resource-groups.tf
- [ ] T016 Run `terraform validate` - network tier checkpoint

<!-- Pulumi Example (IBM Cloud):
- [ ] T008 Create VPC with address prefixes in iac/networking.ts
- [ ] T009 [P] Create subnets across zones in iac/networking.ts
- [ ] T010 [P] Create Public Gateway and attach to subnets in iac/networking.ts
- [ ] T011 [P] Create security groups in iac/security.ts
- [ ] T012 [P] Create network ACLs in iac/security.ts
- [ ] T013 [P] Create IAM access groups in iac/iam.ts
- [ ] T014 Run `pulumi preview` - network tier checkpoint
-->

**Checkpoint**: Network tier complete - compute and data resources can now be provisioned

---

## Phase 3: Compute & Data Tier

**Purpose**: Compute resources, databases, storage, and load balancers

**Dependencies**: Requires Network Tier (Phase 2) to be complete

<!-- Terraform Example (IBM Cloud): -->
- [ ] T017 [P] Create IBM Cloud Databases for PostgreSQL in iac/database.tf
- [ ] T018 [P] Configure database auto-scaling and backups in iac/database.tf
- [ ] T019 [P] Create IBM Cloud Databases for Redis in iac/cache.tf
- [ ] T020 [P] Create Cloud Object Storage instance in iac/storage.tf
- [ ] T021 [P] Create COS buckets (static assets, application data) in iac/storage.tf
- [ ] T022 [P] Configure bucket policies and lifecycle rules in iac/storage.tf
- [ ] T023 Create VPC Load Balancer (Application Load Balancer) in iac/loadbalancer.tf
- [ ] T024 [P] Create load balancer pools and listeners in iac/loadbalancer.tf
- [ ] T025 [P] Configure health checks for load balancer in iac/loadbalancer.tf
- [ ] T026 Create Code Engine project in iac/compute.tf
- [ ] T027 [P] Create Code Engine application with auto-scaling in iac/compute.tf
- [ ] T028 [P] Configure Code Engine environment variables and secrets in iac/compute.tf
- [ ] T029 Run `terraform validate` - compute/data tier checkpoint
- [ ] T030 Run `terraform plan -var-file=terraform.tfvars.dev` to preview changes

<!-- Alternative: Kubernetes Service Example (IBM Cloud):
- [ ] T026 Create IBM Cloud Kubernetes Service (IKS) cluster in iac/compute.tf
- [ ] T027 [P] Configure IKS worker pools across zones in iac/compute.tf
- [ ] T028 [P] Create Kubernetes namespaces in iac/k8s-config.tf
- [ ] T029 [P] Deploy application workloads via Helm or kubectl in iac/k8s-workloads.tf
-->

<!-- Pulumi Example (IBM Cloud):
- [ ] T017 [P] Create IBM Cloud Databases for PostgreSQL in iac/storage.ts
- [ ] T018 [P] Create IBM Cloud Databases for Redis in iac/storage.ts
- [ ] T019 [P] Create Cloud Object Storage instance and buckets in iac/storage.ts
- [ ] T020 Create VPC Load Balancer in iac/compute.ts
- [ ] T021 [P] Configure load balancer pools and listeners in iac/compute.ts
- [ ] T022 Create Code Engine project and applications in iac/compute.ts
- [ ] T023 [P] Configure auto-scaling policies in iac/compute.ts
- [ ] T024 Run `pulumi preview` - compute/data tier checkpoint
-->

**Checkpoint**: Compute and data tier complete - application tier can now be configured

---

## Phase 4: Application Tier

**Purpose**: DNS, CDN, monitoring, alerting, and application-specific configuration

**Dependencies**: Requires Compute & Data Tier (Phase 3) to be complete

<!-- Terraform Example (IBM Cloud): -->
- [ ] T031 [P] Create Internet Services (CIS) instance for DNS and CDN in iac/dns.tf
- [ ] T032 [P] Configure DNS zones and records in iac/dns.tf
- [ ] T033 [P] Enable CDN and configure caching rules in iac/cdn.tf
- [ ] T034 [P] Configure SSL/TLS certificates in iac/certificates.tf
- [ ] T035 [P] Create IBM Cloud Monitoring instance in iac/monitoring.tf
- [ ] T036 [P] Configure monitoring dashboards and metrics in iac/monitoring.tf
- [ ] T037 [P] Create Event Notifications instance in iac/notifications.tf
- [ ] T038 [P] Configure alerting policies and notification channels in iac/alerts.tf
- [ ] T039 [P] Create Activity Tracker instance for audit logging in iac/logging.tf
- [ ] T040 [P] Configure log routing and retention policies in iac/logging.tf
- [ ] T041 [P] Create Secrets Manager instance in iac/secrets.tf
- [ ] T042 [P] Store application secrets and credentials in iac/secrets.tf
- [ ] T043 Run `terraform validate` - application tier checkpoint
- [ ] T044 Run `terraform plan -var-file=terraform.tfvars.dev` to preview changes

<!-- Pulumi Example (IBM Cloud):
- [ ] T031 [P] Create Internet Services instance in iac/dns.ts
- [ ] T032 [P] Configure DNS zones, records, and CDN in iac/dns.ts
- [ ] T033 [P] Create monitoring and alerting in iac/monitoring.ts
- [ ] T034 [P] Configure Activity Tracker in iac/logging.ts
- [ ] T035 [P] Create Secrets Manager instance in iac/secrets.ts
- [ ] T036 Run `pulumi preview` - application tier checkpoint
-->

**Checkpoint**: Application tier complete - infrastructure ready for deployment validation

---

---

[Add more infrastructure tier phases as needed based on your architecture]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Final validation, formatting, documentation, and deployment readiness

<!-- Terraform Example (IBM Cloud): -->
- [ ] TXXX Run `terraform fmt` to format all .tf files
- [ ] TXXX Run `terraform validate` across all configurations
- [ ] TXXX [P] Run security scanning (Checkov, tfsec) on IaC code
- [ ] TXXX [P] Run cost estimation (Infracost) for all environments
- [ ] TXXX [P] Add outputs for key infrastructure values in iac/outputs.tf
- [ ] TXXX [P] Add resource tags for cost tracking and management
- [ ] TXXX [P] Generate architecture diagram from Terraform code
- [ ] TXXX Document infrastructure in iac/README.md
- [ ] TXXX Create deployment runbook in docs/deployment.md
- [ ] TXXX Run `terraform plan` for dev environment
- [ ] TXXX Run quickstart.md validation

<!-- Pulumi Example (IBM Cloud):
- [ ] TXXX Run `pulumi preview` for all stacks
- [ ] TXXX [P] Run security scanning on IaC code
- [ ] TXXX [P] Run cost estimation
- [ ] TXXX [P] Add stack outputs for key infrastructure values
- [ ] TXXX Document infrastructure in iac/README.md
- [ ] TXXX Create deployment runbook
- [ ] TXXX Run quickstart.md validation
-->

---

## Dependencies & Execution Order

### Phase Dependencies

**Infrastructure Projects - General Pattern:**
- **Phase 1: Setup**: No dependencies - can start immediately
- **Phase 2: Network Tier**: Depends on Setup - BLOCKS all compute/data resources
- **Phase 3+: Resource Tiers**: Depend on Network Tier and possibly each other
  - Organize additional phases by resource dependencies
  - Number of phases varies by infrastructure complexity
- **Phase N: Polish**: Depends on all infrastructure tiers being complete

**Common Infrastructure Dependency Pattern:**
1. Setup (backend, provider, variables)
2. Network (VPC, subnets, security groups, routing)
3. Compute & Data (databases, storage, compute resources, load balancers)
4. Application (DNS, monitoring, alerting, application config)
5. Polish (validation, documentation, final checks)

Note: Your infrastructure may need more or fewer phases depending on complexity

### Infrastructure Task Sequencing Rules

**Critical Dependencies:**
- Network resources MUST complete before compute resources
- Security groups MUST be defined before resources that reference them
- IAM roles/policies MUST exist before resources that use them
- VPC/subnets MUST exist before placing resources in them
- Load balancers MUST exist before compute services register with them

**Validation Checkpoints:**
- Run `terraform validate` (or equivalent) after each tier completes
- Run `terraform plan` before marking tier complete
- Formatting checks (`terraform fmt`) in Polish phase

### Parallel Opportunities

**Within Same Tier:**
- Resources within same tier can execute in parallel when marked [P]
- Example: Multiple security groups, multiple subnets, multiple IAM policies
- Variable file creation can happen in parallel with resource definitions
- Documentation tasks can run in parallel during Polish phase

**Across Environments:**
- Different environments (dev/staging/prod) can be provisioned in parallel
- Each environment follows same tier dependencies independently

**Independent Components:**
- Separate VPCs or separate applications can execute in parallel
- Unrelated infrastructure stacks can be deployed simultaneously

### When Tasks CANNOT Be Parallel

**CRITICAL: Tasks CANNOT run in parallel when:**

1. **Same File Modification**:
   - ❌ Two tasks both modifying `iac/vpc.tf`
   - ✅ One task on `iac/vpc.tf`, another on `iac/security-groups.tf`

2. **Resource Dependencies**:
   - ❌ Creating compute instances BEFORE VPC exists
   - ❌ Attaching security groups BEFORE they're defined
   - ❌ Configuring load balancer pools BEFORE load balancer exists
   - ✅ Creating multiple independent security groups (different files, no dependencies)

3. **Cross-Tier Dependencies**:
   - ❌ Any Compute/Data tier task running before Network tier completes
   - ❌ Application tier DNS configuration before compute resources exist
   - ✅ Within Network tier: subnets, security groups, IAM roles (if in different files)

4. **Sequential Configuration**:
   - ❌ Configuring database backups BEFORE database is created
   - ❌ Attaching policies to IAM roles BEFORE roles exist
   - ❌ Registering targets with load balancer BEFORE targets exist
   - ✅ Creating multiple databases in parallel (if no dependencies between them)

5. **Validation Checkpoints**:
   - ❌ Starting next tier BEFORE validation checkpoint passes
   - ❌ Running `terraform plan` BEFORE all tier resources defined
   - ✅ Running validation commands in sequence at tier boundaries

**Infrastructure-Specific Dependency Examples:**

- **VPC → Subnets → Resources**: Must create VPC, then subnets, then place resources in subnets
- **Security Groups → Compute**: Define security groups before launching instances that reference them
- **IAM Roles → Resources**: Create IAM roles before resources that assume those roles
- **Load Balancer → Pools → Targets**: Create LB, then pools, then register targets
- **Network → Database**: Network infrastructure must exist before database placement
- **Secrets Manager → Application**: Secrets must exist before applications reference them

**Rule of Thumb**: If task B needs output/ID from task A, they CANNOT be parallel. Mark task B without [P] and ensure it comes after task A in the sequence.

---

## Implementation Strategy

### Tier-by-Tier Code Generation

1. Complete Phase 1: Setup (create backend.tf, provider.tf, variables.tf)
2. Complete Phase 2: Network Tier (create vpc.tf, security-groups.tf, etc.)
3. **VALIDATE**: Run `terraform validate` to verify configuration syntax
4. Complete Phase 3+: Additional tiers (create compute.tf, database.tf, etc.)
5. **VALIDATE**: Run `terraform validate` after each tier
6. Complete Phase N: Polish (formatting, documentation, outputs.tf)
7. Final validation with `terraform validate` and `terraform plan`

**Note**: Implementation generates IaC code files only. Actual infrastructure deployment (terraform apply) is outside the scope of this framework.

### Parallel Code Generation

When multiple team members work on IaC code:

1. Complete Setup + Network together (foundation files)
2. Once Network tier files complete, parallelize within tiers:
   - Team member A: Database resource definitions
   - Team member B: Compute resource definitions
   - Team member C: Storage resource definitions
3. Validate at tier boundaries before proceeding to next tier

---

## Notes

- [P] tasks = different files, no dependencies within same tier
- Tasks organized by infrastructure tier following dependency hierarchy
- Run `terraform validate` at tier boundaries to catch syntax errors early
- Run `terraform plan` before marking major tiers complete
- Commit after each tier or logical group of resources
- Stop at checkpoints to validate configuration
- Avoid: vague tasks, same file conflicts, violating tier dependencies
