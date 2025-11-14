# Architecture Plan: [INFRASTRUCTURE]

**Branch**: `[###-infrastructure-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Infrastructure specification from `/specs/[###-infrastructure-name]/spec.md`

**Note**: This template is filled in by the `/iac.plan` command. See `iac.plan.md` for the execution workflow.

## Summary

[Extract from infrastructure spec: primary capability + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the infrastructure project. Mark any unknowns as "NEEDS CLARIFICATION" -
  these will be resolved in Phase 0 research.
-->

**Cloud Provider**: [e.g., AWS, Azure, GCP, IBM Cloud, Multi-cloud or NEEDS CLARIFICATION]
**IaC Tool**: [e.g., Terraform 1.12+, Pulumi 3.x, CloudFormation or NEEDS CLARIFICATION]
**Provider Versions**: [e.g., AWS Provider ~> 5.0, Azure Provider ~> 3.0 or NEEDS CLARIFICATION]
**Curated Modules**: [e.g., terraform-aws-modules, Azure Verified Modules, terraform-ibm-modules, terraform-google-modules, Pulumi packages or NEEDS CLARIFICATION]
**State Backend**: [e.g., S3 + DynamoDB, Azure Blob, Terraform Cloud or NEEDS CLARIFICATION]
**Environment Strategy**: [e.g., Workspaces, Separate state files, Directory-based or NEEDS CLARIFICATION]
**Testing**: [e.g., Terratest, Kitchen-Terraform, terraform test or N/A]
**Security Scanning**: [e.g., Checkov, tfsec, Snyk or NEEDS CLARIFICATION]
**Cost Estimation**: [e.g., Infracost, Cloud provider calculators or N/A]
**Target Environments**: [e.g., dev/staging/prod, dev/prod only, single environment or NEEDS CLARIFICATION]
**Compliance**: [if applicable, e.g., SOC 2, HIPAA, PCI-DSS or N/A]

## Principles Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Gates determined based on principles file]

## Infrastructure Architecture

<!--
  **CRITICAL TRANSITION POINT**: This is where generic requirements become cloud-specific.
  
  The spec.md uses ONLY generic infrastructure terms (e.g., "managed database", "object storage").
  THIS file (plan.md) translates them to cloud-specific services (e.g., "RDS PostgreSQL", "S3").
  
  Translation Examples:
  - spec.md: "managed relational database" → plan.md: "AWS RDS PostgreSQL 15.x" or "IBM Cloud Databases for PostgreSQL 15.x"
  - spec.md: "object storage" → plan.md: "S3 bucket with versioning" or "Cloud Object Storage bucket"
  - spec.md: "serverless compute" → plan.md: "Lambda functions (Node.js 18)" or "Code Engine applications"
  - spec.md: "container orchestration" → plan.md: "EKS cluster v1.28" or "IBM Cloud Kubernetes Service"
  - spec.md: "load balancer" → plan.md: "Application Load Balancer" or "VPC Load Balancer"
  - spec.md: "virtual private network" → plan.md: "AWS VPC" or "IBM Cloud VPC"
  
  During /iac.implement, AI agents will read this section to generate IaC files.
  
  This content will be expanded into architecture.md in Phase 1.
-->

### Compute Resources

<!--
  Document compute infrastructure: VMs, containers, serverless functions, load balancers.
  Be specific about instance types, scaling policies, and resource requirements.

  INFRASTRUCTURE PATTERN EXAMPLES:

  Web Application Infrastructure:
  - Load Balancer: VPC Load Balancer (Application Load Balancer) with SSL/TLS termination, health checks
  - Application Tier: Code Engine applications (2-10 instances, auto-scaling based on CPU >70%)
  - Scaling Policy: Target tracking on CPU utilization, scale out at 70%, scale in at 30%

  API Service Infrastructure:
  - API Gateway: API Gateway with request validation, throttling (10k req/s), API keys
  - Compute: Code Engine applications or Cloud Functions (Node.js 18, 512MB memory, 60s timeout)
  - Concurrency: Reserved concurrency per function, burst capacity configuration

  Data Processing Pipeline:
  - Batch Processing: Code Engine jobs (cx2-2x4 profile), scheduled via Event Notifications
  - Orchestration: App Connect or custom workflow orchestration with error handling
  - Auto-scaling: Scale based on message queue depth for parallel processing

  Static Website Hosting:
  - CDN: Internet Services (CIS) with custom domain, SSL certificate, edge caching
  - Origin: Cloud Object Storage bucket with static website hosting enabled
  - No compute resources needed (fully serverless)
-->

[Document compute resources here]

### Data Storage

<!--
  Document data storage infrastructure: databases, object storage, caches, file systems.
  Include capacity, backup strategies, replication, and access patterns.

  INFRASTRUCTURE PATTERN EXAMPLES:

  Web Application Infrastructure:
  - Primary Database: IBM Cloud Databases for PostgreSQL 15.x (shared-cores or dedicated-cores, Multi-AZ, 20GB storage)
  - Backups: Automated daily backups, 7-day retention, point-in-time recovery enabled
  - Cache: IBM Cloud Databases for Redis 7.x (shared-cores for dev, dedicated high-memory for prod)
  - Object Storage: Cloud Object Storage bucket for user uploads, versioning enabled, lifecycle to Archive after 90 days

  API Service Infrastructure:
  - Database: IBM Cloudant with standard plan, continuous replication, global distribution
  - Throughput: Provisioned capacity for predictable workloads, standard capacity for variable loads
  - Backup: Continuous backups with 35-day retention, cross-region replication for DR

  Data Processing Pipeline:
  - Raw Data: Cloud Object Storage bucket with smart tier, event notifications for new objects
  - Processed Data: Cloud Object Storage bucket with partitioned structure (year/month/day) for efficient querying
  - Data Warehouse: Db2 Warehouse (flex-one system, 2 nodes) or SQL Query for serverless queries
  - Metadata: Cloudant database tracking processing status and lineage

  Static Website Hosting:
  - Storage: Cloud Object Storage bucket with website hosting enabled, bucket policy for CIS access
  - Versioning: Enabled for rollback capability
  - Logging: Access logs to separate COS bucket for analytics
-->

[Document data storage resources here]

### Networking

<!--
  Document network topology: VPCs, subnets, routing, DNS, load balancing, CDN.
  Include IP ranges, subnet configurations, and network security boundaries.

  Examples:
  - VPC: 10.0.0.0/16 in primary region (us-south)
  - Public Subnets: 10.0.1.0/24 (us-south-1), 10.0.2.0/24 (us-south-2) - for load balancers
  - Private Subnets: 10.0.10.0/24 (us-south-1), 10.0.11.0/24 (us-south-2) - for application tier
  - Public Gateway: One per zone for private subnet internet access
  - DNS: Internet Services (CIS) DNS zones for custom domain with health checks
  - CDN: Internet Services (CIS) with edge caching for static assets and API acceleration
-->

[Document networking configuration here]

### Security

<!--
  Document security controls: IAM policies, security groups/firewalls, encryption, secrets management.
  Include principle of least privilege, access boundaries, and compliance requirements.

  Examples:
  - Security Groups:
    - Load Balancer SG: Inbound 443 from 0.0.0.0/0, outbound to application SG
    - Application SG: Inbound from LB SG, outbound to database SG and internet
    - Database SG: Inbound 5432 from application SG only
  - IAM Access Groups:
    - Code Engine Service Role: Pull images from Container Registry, write logs to Log Analysis
    - Application Service Role: Access COS buckets, read secrets from Secrets Manager
  - Encryption:
    - Databases: Encryption at rest with Key Protect, TLS in transit
    - Cloud Object Storage: AES-256 server-side encryption with Key Protect integration
  - Secrets: IBM Secrets Manager for database credentials, API keys, certificates
-->

[Document security configuration here]

### Environment Configuration

<!--
  Document environment-specific parameters: dev/staging/prod differences.
  Include variable files, workspace strategies, and environment isolation approaches.

  MULTI-ENVIRONMENT CONFIGURATION GUIDANCE:
  Use variable files (.tfvars) to parameterize environment-specific values.
  Do not duplicate Terraform code across environments.

  Environment Strategy Options:
  1. Terraform Workspaces: Separate state per environment, same VPC/network
  2. Separate State Files: Different backends per environment, complete isolation
  3. Directory-based: environments/dev/, environments/staging/, environments/prod/

  Examples:
  - Environments: dev, staging, prod
  - Variable Files:
    - terraform.tfvars.dev: t3.micro instances, single-AZ RDS, 1-2 tasks, minimal scaling
    - terraform.tfvars.staging: t3.small instances, Multi-AZ RDS, 2-4 tasks, moderate scaling
    - terraform.tfvars.prod: t3.medium instances, Multi-AZ RDS, 4-10 tasks, aggressive scaling
  - Workspace Strategy: Terraform workspaces per environment (terraform workspace select dev)
  - Isolation: Separate VPCs per environment for network-level isolation
  - Deployment Order: dev → staging → prod (validate in each before promoting)
-->

[Document environment configuration here]

### Complexity Level

<!--
  Document the complexity level (Baseline vs Enhanced) based on use case and environment type.
  This guides which architecture principles to apply from the project principles.

  BASELINE (POC/Demo/Dev environments):
  - Purpose: Quick demos, learning, rapid iteration, short-lived experiments
  - Architecture: Simplified (single-zone, single-tier networking acceptable)
  - Resources: Minimal (smallest instance sizes, basic storage classes)
  - Security: Basic controls (no hardcoded credentials, encryption in transit, restricted network access)
  - Monitoring: Default metrics and basic health checks only
  - Cost: Highly optimized (auto-shutdown schedules, smallest viable resources)
  - HA/DR: Not required
  - Examples: Single main.tf acceptable, local state okay for solo dev

  ENHANCED (Staging/Production environments):
  - Purpose: Production validation, live customer workloads, business-critical services
  - Architecture: Production-grade (multi-zone, multi-tier networking with isolation)
  - Resources: Right-sized based on performance requirements and load testing
  - Security: Full controls (encryption at rest + transit, least-privilege IAM, private networks, audit logging, security scanning)
  - Monitoring: Comprehensive (custom metrics, alerting, dashboards, centralized logging)
  - Cost: Balanced with performance and availability requirements
  - HA/DR: Multi-zone deployment, auto-scaling, load balancing, backup/restore, disaster recovery
  - Examples: Organized file structure, remote state with locking, separate environments

  Choose complexity level based on:
  - Environment purpose (POC vs Development vs Staging vs Production)
  - Data sensitivity and compliance requirements
  - Availability and performance SLAs
  - Team size and operational maturity
-->

[Document complexity level and rationale here]

### State Management

<!--
  Document Terraform state backend configuration: local vs remote, locking, backup.
  Critical for team collaboration and preventing state corruption.

  STATE MANAGEMENT STRATEGY GUIDANCE:
  - Local State: Only for solo development, prototyping, or learning. NOT for production.
  - Remote State: Required for team collaboration and production infrastructure.

  Remote Backend Options:
  - S3 + DynamoDB (AWS): Most common, reliable, cost-effective
  - Azure Blob Storage + Storage Account Lock (Azure): Native Azure integration
  - GCS (GCP): Native GCP integration, good performance
  - Terraform Cloud: Managed service, includes remote execution, policy as code
  - Consul: For multi-cloud or hybrid scenarios

  Best Practices:
  - Enable versioning on backend storage for rollback capability
  - Use locking mechanism to prevent concurrent modifications (DynamoDB for S3, native for others)
  - Encrypt state files at rest (contains sensitive data like passwords, keys)
  - Restrict access via IAM/RBAC (state files contain credentials and topology)
  - Separate state files per environment (never share state across dev/staging/prod)
  - Regular backups with retention policy (keep 30+ days for disaster recovery)

  Examples:
  - Backend: Cloud Object Storage bucket (my-project-terraform-state) in us-south with versioning enabled
  - State Locking: COS object locking or Terraform Cloud state locking to prevent concurrent modifications
  - Encryption: AES-256 server-side encryption with Key Protect for additional security
  - Backup Strategy: COS versioning + lifecycle policy (retain 30 days of versions, archive to Archive tier after 90 days)
  - Access Control: IAM policies restrict state bucket access to CI/CD service IDs and authorized users only
  - Workspace Usage: One state file per workspace (terraform workspace select dev/staging/prod)
  - State File Naming: terraform.tfstate for default workspace, terraform.tfstate.d/<workspace>/ for named workspaces
-->

[Document state management strategy here]

## Project Structure

### Documentation (this infrastructure)

```text
specs/[###-infrastructure]/
├── spec.md              # Infrastructure specification (technology-agnostic)
├── plan.md              # This file (/iac.plan command output)
├── research.md          # Phase 0 output: technology decisions and best practices
├── architecture.md      # Phase 1 output: detailed infrastructure design
├── modules.md           # Phase 1 output: module specifications (if using modules)
├── quickstart.md        # Phase 1 output: deployment guide
└── tasks.md             # Phase 2 output (/iac.tasks command - NOT created by /iac.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this infrastructure project. Delete unused options and expand the chosen structure with
  real paths. The delivered plan must not include Option labels.

  FOR INFRASTRUCTURE PROJECTS:
  Place infrastructure code in an `iac/` (Infrastructure-as-Code) directory.
  Keep infrastructure separate from application code for clear separation of concerns.

  Infrastructure File Placement Guidance:
  - Terraform files (.tf): Place in iac/ directory at repository root
  - Variable files (.tfvars): Place alongside .tf files, one per environment
  - Modules: Optionally create iac/modules/ for reusable components
  - Documentation: Create iac/README.md with provisioning instructions

  Recommended structure for infrastructure projects:
  iac/
  ├── backend.tf              # State backend configuration
  ├── provider.tf             # Cloud provider configuration
  ├── vpc.tf                  # Networking resources
  ├── security-groups.tf      # Security policies
  ├── compute.tf              # Compute resources (VMs, containers, functions)
  ├── data.tf                 # Data storage resources (databases, buckets)
  ├── variables.tf            # Input variable declarations
  ├── outputs.tf              # Output value declarations
  ├── terraform.tfvars.dev    # Dev environment variables
  ├── terraform.tfvars.staging # Staging environment variables
  ├── terraform.tfvars.prod   # Production environment variables
  └── README.md               # Provisioning instructions

  For HYBRID PROJECTS (both application and infrastructure):
  Keep them separate - application code in src/, infrastructure in iac/

  STRUCTURE SELECTION GUIDANCE:
  Choose infrastructure code structure based on use case complexity, not arbitrary rules.

  - POCs/Demos/Learning: Use Option 1 (Simple Terraform) - single main.tf is perfectly acceptable
    * Characteristics: Short-lived, single user, demonstration or learning purpose
    * Benefits: Minimal overhead, easy to understand, quick to iterate
    * When to upgrade: When infrastructure exceeds ~100 lines or needs team collaboration

  - Development/Testing: Use Option 2 (Terraform Infrastructure) - organized by resource type
    * Characteristics: Ongoing use, shared team access, multiple resource types
    * Benefits: Clear organization, easier to navigate, supports growth
    * File separation: Logical grouping by concern (network, compute, data, security)

  - Production: Use Option 2 with modules/ directory for reusable components
    * Characteristics: Business-critical, compliance requirements, complex dependencies
    * Benefits: Reusability, testing isolation, version control of infrastructure patterns
    * Modules: Extract common patterns (e.g., standard VPC setup, standard app tier)

  - Large/Complex Systems: Consider Option 2 with workspaces or directory-based environments
    * Characteristics: Multiple teams, multiple environments, extensive infrastructure
    * Benefits: Environment isolation, parallel development, clear boundaries
    * Trade-off: More files to manage, requires discipline to avoid drift

  Do NOT over-engineer structure for simple use cases. A single main.tf for a POC is appropriate.
-->

```text
# [REMOVE IF UNUSED] Option 1: Simple Terraform (POC/Demo/Single Resource)
iac/
├── main.tf                 # All resources in one file
├── variables.tf            # Variable declarations
├── outputs.tf              # Output declarations
├── provider.tf             # Provider configuration
└── README.md               # Provisioning instructions

# [REMOVE IF UNUSED] Option 2: Terraform Infrastructure (DEFAULT for IaC)
iac/
├── backend.tf              # State backend (IBM COS, S3, Azure Storage, GCS)
├── provider.tf             # Provider configuration (IBM Cloud, AWS, Azure, GCP)
├── versions.tf             # Terraform and provider version constraints
├── vpc.tf                  # Network infrastructure
├── security-groups.tf      # Security policies and firewall rules
├── compute.tf              # Compute resources
├── data.tf                 # Data storage resources
├── loadbalancer.tf         # Load balancing resources
├── dns.tf                  # DNS and domain management
├── iam.tf                  # IAM roles and policies
├── monitoring.tf           # Monitoring and logging
├── variables.tf            # Variable declarations
├── outputs.tf              # Output declarations
├── terraform.tfvars.dev    # Dev environment variables
├── terraform.tfvars.staging # Staging environment variables
├── terraform.tfvars.prod   # Production environment variables
├── modules/                # Custom reusable modules (optional)
│   ├── web-application/
│   ├── database-cluster/
│   └── vpc-networking/
└── README.md               # Provisioning and usage instructions

# [REMOVE IF UNUSED] Option 3: Pulumi Infrastructure
iac/
├── Pulumi.yaml             # Project definition
├── Pulumi.dev.yaml         # Dev stack configuration
├── Pulumi.staging.yaml     # Staging stack configuration
├── Pulumi.prod.yaml        # Production stack configuration
├── index.ts                # Main program entry point
├── networking.ts           # VPC, subnets, security groups
├── compute.ts              # Compute resources
├── storage.ts              # Databases and object storage
├── package.json            # Node.js dependencies
└── README.md               # Deployment instructions

# [REMOVE IF UNUSED] Option 4: CloudFormation Infrastructure (AWS)
iac/
├── main-stack.yaml         # Root stack template
├── networking.yaml         # Nested stack: VPC, subnets
├── compute.yaml            # Nested stack: Compute resources
├── database.yaml           # Nested stack: Database resources
├── parameters/
│   ├── dev.json            # Dev environment parameters
│   ├── staging.json        # Staging parameters
│   └── prod.json           # Production parameters
└── README.md               # Deployment guide
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Principles Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., Multi-cloud] | [current need] | [why single cloud insufficient] |
