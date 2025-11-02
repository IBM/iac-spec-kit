# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: [e.g., Python 3.11, Swift 5.9, Rust 1.75 or NEEDS CLARIFICATION]  
**Primary Dependencies**: [e.g., FastAPI, UIKit, LLVM or NEEDS CLARIFICATION]  
**Storage**: [if applicable, e.g., PostgreSQL, CoreData, files or N/A]  
**Testing**: [e.g., pytest, XCTest, cargo test or NEEDS CLARIFICATION]  
**Target Platform**: [e.g., Linux server, iOS 15+, WASM or NEEDS CLARIFICATION]
**Project Type**: [single/web/mobile - determines source structure]  
**Performance Goals**: [domain-specific, e.g., 1000 req/s, 10k lines/sec, 60 fps or NEEDS CLARIFICATION]  
**Constraints**: [domain-specific, e.g., <200ms p95, <100MB memory, offline-capable or NEEDS CLARIFICATION]  
**Scale/Scope**: [domain-specific, e.g., 10k users, 1M LOC, 50 screens or NEEDS CLARIFICATION]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

[Gates determined based on constitution file]

## Infrastructure Architecture *(infrastructure projects)*

<!--
  This section is for INFRASTRUCTURE PROJECTS ONLY (e.g., Terraform, Pulumi, CloudFormation).
  Application projects can skip this section entirely.

  Use this section to document cloud infrastructure requirements in a provider-specific way.
  The spec.md should remain technology-agnostic; provider-specific details belong here.

  During /speckit.implement, AI agents will read this section to generate infrastructure-as-code files.
-->

### Compute Resources

<!--
  Document compute infrastructure: VMs, containers, serverless functions, load balancers.
  Be specific about instance types, scaling policies, and resource requirements.

  INFRASTRUCTURE PATTERN EXAMPLES:

  Web Application Infrastructure:
  - Load Balancer: Application Load Balancer (ALB) with SSL/TLS termination, health checks
  - Application Tier: ECS Fargate containers (2-10 tasks, auto-scaling based on CPU >70%)
  - Scaling Policy: Target tracking on CPU utilization, scale out at 70%, scale in at 30%

  API Service Infrastructure:
  - API Gateway: REST API with request validation, throttling (10k req/s), API keys
  - Compute: Lambda functions (Node.js 18, 512MB memory, 30s timeout) or ECS Fargate
  - Concurrency: Reserved concurrency per function, burst capacity configuration

  Data Processing Pipeline:
  - Batch Processing: ECS tasks on EC2 (c5.xlarge spot instances), scheduled via EventBridge
  - Orchestration: Step Functions for multi-stage workflows with error handling
  - Auto-scaling: Scale based on SQS queue depth for parallel processing

  Static Website Hosting:
  - CDN: CloudFront distribution with custom domain, SSL certificate, edge caching
  - Origin: S3 bucket with static website hosting enabled
  - No compute resources needed (fully serverless)
-->

[Document compute resources here]

### Data Storage

<!--
  Document data storage infrastructure: databases, object storage, caches, file systems.
  Include capacity, backup strategies, replication, and access patterns.

  INFRASTRUCTURE PATTERN EXAMPLES:

  Web Application Infrastructure:
  - Primary Database: RDS PostgreSQL 15.x (db.t3.medium, Multi-AZ, 100GB gp3 storage)
  - Backups: Automated daily backups, 7-day retention, point-in-time recovery enabled
  - Cache: ElastiCache Redis 7.x (cache.t3.micro for dev, cache.r6g.large cluster for prod)
  - Object Storage: S3 bucket for user uploads, versioning enabled, lifecycle to Glacier after 90 days

  API Service Infrastructure:
  - Database: DynamoDB with on-demand billing, point-in-time recovery, global tables
  - Throughput: Provisioned capacity for predictable workloads, on-demand for variable loads
  - Backup: Continuous backups with 35-day retention, cross-region replication for DR

  Data Processing Pipeline:
  - Raw Data: S3 bucket with intelligent tiering, event notifications for new objects
  - Processed Data: S3 bucket with partitioned structure (year/month/day) for efficient querying
  - Data Warehouse: Redshift cluster (dc2.large, 2 nodes) or Athena for serverless queries
  - Metadata: DynamoDB table tracking processing status and lineage

  Static Website Hosting:
  - Storage: S3 bucket with website hosting enabled, bucket policy for CloudFront access
  - Versioning: Enabled for rollback capability
  - Logging: Access logs to separate S3 bucket for analytics
-->

[Document data storage resources here]

### Networking

<!--
  Document network topology: VPCs, subnets, routing, DNS, load balancing, CDN.
  Include IP ranges, subnet configurations, and network security boundaries.

  Examples:
  - VPC: 10.0.0.0/16 in primary region
  - Public Subnets: 10.0.1.0/24 (AZ-a), 10.0.2.0/24 (AZ-b) - for load balancers
  - Private Subnets: 10.0.10.0/24 (AZ-a), 10.0.11.0/24 (AZ-b) - for application tier
  - NAT Gateway: One per availability zone for private subnet internet access
  - DNS: Route53 hosted zone for custom domain with health checks
  - CDN: CloudFront distribution for static assets and API caching
-->

[Document networking configuration here]

### Security

<!--
  Document security controls: IAM policies, security groups/firewalls, encryption, secrets management.
  Include principle of least privilege, access boundaries, and compliance requirements.

  Examples:
  - Security Groups:
    - ALB SG: Inbound 443 from 0.0.0.0/0, outbound to ECS SG
    - ECS SG: Inbound from ALB SG, outbound to RDS SG and internet
    - RDS SG: Inbound 5432 from ECS SG only
  - IAM Roles:
    - ECS Task Execution Role: Pull images, write logs to CloudWatch
    - ECS Task Role: Access S3 buckets, read secrets from Secrets Manager
  - Encryption:
    - RDS: Encryption at rest with KMS, TLS in transit
    - S3: AES-256 server-side encryption
  - Secrets: AWS Secrets Manager for database credentials, API keys
-->

[Document security configuration here]

### Environment Configuration

<!--
  Document environment-specific parameters: dev/staging/prod differences.
  Include variable files, workspace strategies, and environment isolation approaches.

  CLOUD PROVIDER SELECTION GUIDANCE:
  When choosing a cloud provider, document your rationale here:
  - AWS: Mature ecosystem, widest service selection, strong enterprise support
  - Azure: Best for Microsoft stack integration, hybrid cloud scenarios
  - GCP: Competitive pricing, strong data/ML services, Kubernetes-native
  - Multi-cloud: Only if required by compliance or risk management needs

  Choose ONE provider for this project to minimize complexity.

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
  - Backend: S3 bucket (my-project-terraform-state) in us-east-1 with versioning enabled
  - State Locking: DynamoDB table (terraform-state-lock) to prevent concurrent modifications
  - Encryption: AES-256 server-side encryption (SSE-S3) or KMS for additional security
  - Backup Strategy: S3 versioning + lifecycle policy (retain 30 days of versions, archive to Glacier after 90 days)
  - Access Control: IAM policies restrict state bucket access to CI/CD role and authorized users only
  - Workspace Usage: One state file per workspace (terraform workspace select dev/staging/prod)
  - State File Naming: terraform.tfstate for default workspace, terraform.tfstate.d/<workspace>/ for named workspaces
-->

[Document state management strategy here]

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.

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
-->

```text
# [REMOVE IF UNUSED] Option 1: Single project (DEFAULT)
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [REMOVE IF UNUSED] Option 2: Web application (when "frontend" + "backend" detected)
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]

# [REMOVE IF UNUSED] Option 4: Infrastructure project (Terraform, IaC)
iac/
├── backend.tf              # State backend (S3, Azure Storage, GCS)
├── provider.tf             # Provider configuration (AWS, Azure, GCP)
├── vpc.tf                  # Network infrastructure
├── security-groups.tf      # Security policies and firewall rules
├── compute.tf              # Compute resources
├── data.tf                 # Data storage resources
├── variables.tf            # Variable declarations
├── outputs.tf              # Output declarations
├── terraform.tfvars.dev    # Dev environment variables
├── terraform.tfvars.staging # Staging environment variables
├── terraform.tfvars.prod   # Production environment variables
└── README.md               # Provisioning and usage instructions
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
