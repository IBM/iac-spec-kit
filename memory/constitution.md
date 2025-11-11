# [PROJECT_NAME] Constitution
<!-- Example: MyApp Infrastructure Constitution, Platform IaC Constitution, etc. -->

## Cloud Architecture Principles
<!-- Principles about the infrastructure resources that will be created from generated code.
     Add or remove principles based on needs - the number is flexible.
     Use Baseline/Enhanced pattern to scale complexity with use case. -->

### [ARCHITECTURE_PRINCIPLE_1_NAME]
<!-- Example: I. Security Defaults -->
[ARCHITECTURE_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Infrastructure must be secure by default; Baseline: No hardcoded credentials, encryption in transit enabled, network access restricted to necessary sources; Enhanced: + Encryption at rest with managed keys, least-privilege access policies, private network placement, audit logging for privileged operations -->

### [ARCHITECTURE_PRINCIPLE_2_NAME]
<!-- Example: II. Resource Identification -->
[ARCHITECTURE_PRINCIPLE_2_DESCRIPTION]
<!-- Example: All resources tagged/labeled consistently; Baseline: environment, owner, purpose; Enhanced: + cost_center, compliance_scope, data_classification; Naming: [project]-[resource-type]-[environment], include region/zone for multi-region -->

### [ARCHITECTURE_PRINCIPLE_3_NAME]
<!-- Example: III. Network Architecture -->
[ARCHITECTURE_PRINCIPLE_3_DESCRIPTION]
<!-- Example: Network topology aligned with isolation needs; Baseline: Single network with security groups/firewall rules; Enhanced: Multi-tier with isolated subnets (public for load balancers, private for apps, isolated for data), NAT gateways, network ACLs + security groups -->

### [ARCHITECTURE_PRINCIPLE_4_NAME]
<!-- Example: IV. Data Storage -->
[ARCHITECTURE_PRINCIPLE_4_DESCRIPTION]
<!-- Example: Storage based on sensitivity and durability; Baseline: Standard storage, provider-managed encryption; Enhanced: + Encryption at rest, automated backups, versioning for objects, private endpoints, multi-zone replication for critical data -->

### [ARCHITECTURE_PRINCIPLE_5_NAME]
<!-- Example: V. Observability -->
[ARCHITECTURE_PRINCIPLE_5_DESCRIPTION]
<!-- Example: Monitoring resources included; Baseline: Default metrics, basic health checks; Enhanced: + Custom metrics/alarms, centralized logging, alerting channels, dashboards for KPIs -->

### [ARCHITECTURE_PRINCIPLE_6_NAME]
<!-- Example: VI. High Availability -->
[ARCHITECTURE_PRINCIPLE_6_DESCRIPTION]
<!-- Example: HA patterns scale with criticality; Baseline: Single zone with basic health checks; Enhanced: Multi-zone deployment, load balancers with health checks, auto-scaling, database replicas, cross-region backups, failover configs -->

### [ARCHITECTURE_PRINCIPLE_7_NAME]
<!-- Example: VII. Disaster Recovery -->
[ARCHITECTURE_PRINCIPLE_7_DESCRIPTION]
<!-- Example: DR readiness scales with business needs; Baseline: Basic backups with retention; Enhanced: Cross-region replication, backup vaults, DR region resources, failover routing, RPO/RTO targets in comments -->

### [ARCHITECTURE_PRINCIPLE_8_NAME]
<!-- Example: VIII. Compliance Controls -->
[ARCHITECTURE_PRINCIPLE_8_DESCRIPTION]
<!-- Example: Compliance controls based on regulatory requirements; Baseline: Basic audit logging; Enhanced: Encryption keys with rotation, audit logs to immutable storage, compliance tags, data residency controls, access logging, policy checks -->

### [ARCHITECTURE_PRINCIPLE_N_NAME]
<!-- Add more principles as needed for your use case: Cost Optimization, Container Security, Database Standards, etc. -->

## IaC Code Principles
<!-- Principles about the infrastructure code itself: structure, testing, quality, etc.
     Add or remove principles based on your needs - the number is flexible. -->

### [CODE_PRINCIPLE_1_NAME]
<!-- Example: I. Prefer Curated Modules (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Favor validated, well-maintained modules over direct provider resources; Terraform: Use terraform-aws-modules, Azure Verified Modules, terraform-ibm-modules, terraform-google-modules; Benefits: Best practices built-in, tested and maintained, consistent patterns, reduced boilerplate; When to use direct resources: Custom requirements not supported by modules, very simple single resources, modules add unnecessary complexity; Module selection: Verify module is actively maintained, check community usage and stars, review source code for security, pin to specific versions -->

### [CODE_PRINCIPLE_2_NAME]
<!-- Example: II. Module Structure and Organization -->
[CODE_PRINCIPLE_2_DESCRIPTION]
<!-- Example: Follow tool best practices; Terraform: HashiCorp Standard Module Structure; Other tools: equivalent patterns; Principles: Single responsibility per module, clear input/output contracts, versioning, comments explain intent, use locals for DRY -->

### [CODE_PRINCIPLE_3_NAME]
<!-- Example: III. Testing and Validation -->
[CODE_PRINCIPLE_3_DESCRIPTION]
<!-- Example: Code must be testable and validated; Baseline: Syntax validation (terraform validate), dry-run (terraform plan), basic linting; Enhanced: + Unit tests for modules if supported (terraform test, mocking with override files), integration tests for stacks, security scanning, cost estimation -->

### [CODE_PRINCIPLE_4_NAME]
<!-- Example: IV. Formatting and Style -->
[CODE_PRINCIPLE_4_DESCRIPTION]
<!-- Example: Properly formatted per tool standards; Consistent naming (snake_case recommended), logical grouping, consistent indentation, alphabetize arguments where helpful, meaningful names -->

### [CODE_PRINCIPLE_5_NAME]
<!-- Example: V. Documentation -->
[CODE_PRINCIPLE_5_DESCRIPTION]
<!-- Example: Documentation in and alongside code; In-code: Header comments with purpose, variable/output descriptions, complex logic explanations; Separate: README with prerequisites, usage examples, architecture decisions; Note provider-specific behaviors -->

### [CODE_PRINCIPLE_6_NAME]
<!-- Example: VI. Code Quality Standards -->
[CODE_PRINCIPLE_6_DESCRIPTION]
<!-- Example: Enforced quality gates; Include: Input validation rules, type constraints on variables, lifecycle rules where appropriate, dependency declarations (depends_on); Must pass: Syntax validation, plan execution, unit tests (if applicable), security scanning, cost estimates within expectations -->

### [CODE_PRINCIPLE_7_NAME]
<!-- Example: VII. Variable and Output Patterns -->
[CODE_PRINCIPLE_7_DESCRIPTION]
<!-- Example: Clear contracts; Variables: Type constraints, descriptions mandatory, sensitive flag for secrets, defaults for optional params, validation rules; Outputs: Resource IDs/endpoints/connection strings, mark sensitive, usage examples in descriptions -->

### [CODE_PRINCIPLE_8_NAME]
<!-- Example: VIII. Security in Code -->
[CODE_PRINCIPLE_8_DESCRIPTION]
<!-- Example: Secure coding practices; Secrets: Use variable references never hardcode; Rotation: Include key rotation policies; Access: Least-privilege IAM/RBAC; Network: Default-deny security groups; Encryption: Enable by default with KMS; TLS: Minimum version 1.2 -->

### [CODE_PRINCIPLE_N_NAME]
<!-- Add more principles as needed for your use case: Version Pinning, State Management, Provider Configuration, etc. -->

## Implementation Approaches
<!-- Cloud Architecture Principles = WHAT infrastructure resources to create
     IaC Code Principles = HOW to write the infrastructure code
     Implementation Approaches = WHEN to use different patterns and complexity levels

     Add or remove approaches/scenarios based on needs - the number is flexible.
     Include the strategies and environment types relevant to use case. -->

### [APPROACH_1_NAME]
<!-- Example: Progressive Complexity (Single Environment Evolution) -->
[APPROACH_1_DESCRIPTION]
<!-- Example: When: Single long-lived environment that matures over time; Pattern: Start simple, layer controls as needs grow; Code: Feature flags/variables to enable/disable advanced features, commented blocks for future enhancements, modular design allows incremental additions; Pros: Lower initial complexity, gradual learning; Cons: Careful change management needed -->

### [APPROACH_2_NAME]
<!-- Example: Separate Environments (Dev/Stage/Prod Isolation) -->
[APPROACH_2_DESCRIPTION]
<!-- Example: When: Need isolation between workload tiers; Pattern: Separate stacks per environment with different configs; Code: Environment-specific variable files, shared modules with env-specific settings, lower resource counts for dev/staging, full controls for prod; Pros: Clear boundaries, safer testing, production isolation; Cons: More infrastructure to manage -->

### [APPROACH_3_NAME]
<!-- Example: Hybrid Approach (Recommended) -->
[APPROACH_3_DESCRIPTION]
<!-- Example: When: Balance isolation and progressive enhancement; Pattern: Separate environments for different purposes, each can evolve independently; Code: Dev for rapid iteration (Baseline controls), Staging mirrors prod architecture, Production gets Enhanced controls from start; Recommended for most teams -->

### [APPROACH_4_NAME]
<!-- Example: POC / Demo / Learning -->
[APPROACH_4_DESCRIPTION]
<!-- Example: Characteristics: Short-lived (days-weeks), single user/small team, demonstration/learning, limited data sensitivity; Code: Baseline security only, simplified architecture (single-tier networking okay), minimal resources, cost-optimized sizes, auto-cleanup tags, single file okay for simple cases; Skip: HA, DR, extensive monitoring, backups -->

### [APPROACH_5_NAME]
<!-- Example: Development / Testing Environments -->
[APPROACH_5_DESCRIPTION]
<!-- Example: Characteristics: Ongoing use, shared team, integration testing, non-production data; Code: Baseline security, production-like architecture at reduced scale, modular structure, basic monitoring/logging, network isolation similar to prod, cost controls (auto-shutdown, smaller instances); Include: Variable-driven config, security scanning -->

### [APPROACH_6_NAME]
<!-- Example: Staging / Pre-Production -->
[APPROACH_6_DESCRIPTION]
<!-- Example: Characteristics: Production validation, performance testing, production-like data (anonymized); Code: Enhanced security controls, architecture mirrors production, full monitoring/alerting, separated modules, backup configs with shorter retention, multi-zone for HA testing; Must: All prod security controls, comprehensive tagging, logging/audit -->

### [APPROACH_7_NAME]
<!-- Example: Production Environments -->
[APPROACH_7_DESCRIPTION]
<!-- Example: Characteristics: Live workloads, customer data, SLAs, compliance; Code: All Enhanced security controls, HA config (multi-zone/region), separated modules, comprehensive monitoring/alerting/logging, auto-scaling, load balancing/health checks, DR resources, full backup/retention; Must: All security controls, compliance tags, audit logging, network isolation, encryption -->

### [APPROACH_N_NAME]
<!-- Add more approaches as needed: DR environments, Edge deployments, Multi-tenant scenarios, etc. -->

## Governance
<!-- Example: Constitution supersedes all other practices; All changes must be backward compatible, Amendments require documentation, approval, migration plan -->

[GOVERNANCE_RULES]
<!-- Example: All PRs/reviews must verify compliance; Complexity must be justified;s -->

**Version**: [CONSTITUTION_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 2.0.0 | Ratified: 2025-11-10 | Last Amended: 2025-11-10 -->