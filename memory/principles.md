# [PROJECT_NAME] Principles
<!-- Example: MyApp Infrastructure Principles, Platform IaC Principles, etc. -->

## Cloud Architecture Principles
<!-- Principles about the infrastructure resources that will be created from generated code.
     Start with 2-3 critical principles, then add more only if truly needed.
     Use Baseline/Enhanced pattern to scale complexity with use case.

     NOTE: Keep the set of principles focused and manageable. Start with the principles that are
     truly non-negotiable for your organization. Quality over quantity. -->

### [ARCHITECTURE_PRINCIPLE_1_NAME]
<!-- Example: I. Security Defaults (NON-NEGOTIABLE) -->
[ARCHITECTURE_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Infrastructure must be secure by default; Baseline: Basic security controls; Enhanced: Additional hardening, managed encryption keys, private network placement, audit logging -->

### [ARCHITECTURE_PRINCIPLE_2_NAME]
<!-- Example: II. Resource Identification -->
[ARCHITECTURE_PRINCIPLE_2_DESCRIPTION]
<!-- Example: All resources tagged/labeled consistently; Baseline: Core tags; Enhanced: Extended tags for cost allocation and compliance; Naming convention includes resource type and environment -->

### [ARCHITECTURE_PRINCIPLE_3_NAME]
<!-- Example: III. Observability -->
[ARCHITECTURE_PRINCIPLE_3_DESCRIPTION]
<!-- Example: Monitoring resources included; Baseline: Basic monitoring; Enhanced: Custom metrics, centralized logging, alerting -->

<!-- Add more architecture principles below as needed for your specific requirements.
     Common additional principles to consider:

     Network Architecture: Network topology aligned with isolation needs; Baseline: Single network; Enhanced: Multi-tier isolated subnets, NAT gateways

     Data Storage: Storage based on sensitivity and durability; Baseline: Standard storage; Enhanced: Automated backups, versioning, private endpoints, multi-zone replication

     High Availability: HA patterns scale with criticality; Baseline: Single zone; Enhanced: Multi-zone deployment, load balancers, auto-scaling, failover configs

     Disaster Recovery: DR readiness scales with business needs; Baseline: Basic backups; Enhanced: Cross-region replication, backup vaults, DR region resources, RPO/RTO targets in comments

     Compliance Controls: Compliance based on regulatory requirements; Baseline: Basic audit logging; Enhanced: Audit logs to immutable storage, data residency controls

     Cost Optimization: Cost management appropriate to scale; Baseline: Right-sized resources; Enhanced: Reserved/spot instances, cost monitoring, resource lifecycle policies

     Only add principles that are truly required for your use case. -->

## IaC Code Principles
<!-- Principles about the infrastructure code itself: structure, testing, quality, etc.
     Start with 2-3 critical principles, then add more only if truly needed. -->

### [CODE_PRINCIPLE_1_NAME]
<!-- Example: I. Prefer Curated Modules (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Favor validated, well-maintained modules over direct provider resources; Examples: Azure Verified Modules, terraform-ibm-modules; Use direct resources only for custom requirements or very simple cases; Pin to specific versions -->

### [CODE_PRINCIPLE_2_NAME]
<!-- Example: II. Testing and Validation (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_2_DESCRIPTION]
<!-- Example: Code must be testable and validated before deployment; Baseline: Syntax validation, dry-run, linting (tflint); Enhanced: Unit tests (terraform test, mocking with override files), integration tests, security scanning -->

### [CODE_PRINCIPLE_3_NAME]
<!-- Example: III. Security in Code (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_3_DESCRIPTION]
<!-- Example: Secure coding practices enforced; Never hardcode secrets; Include key rotation policies; Least-privilege access; Default-deny network rules; Enable encryption by default -->

<!-- Add more code principles below as needed for your specific requirements.
     Common additional principles to consider:

     Module Structure: Follow tool best practices; Terraform: HashiCorp Standard Module Structure; Single responsibility, clear contracts, versioning

     Formatting and Style: Properly formatted per tool standards; Consistent naming and organization

     Documentation: In-code comments and separate README; Include purpose, usage examples, architecture decisions

     Code Quality Standards: Enforced quality gates; Type constraints on variables, lifecycle rules, dependency declarations (depends_on)

     Variable and Output Patterns: Clear contracts; Descriptions mandatory, sensitive flag for secrets, validation rules

     Version Pinning: Lock provider and module versions; Use version constraints appropriately

     State Management: Remote state with locking; State isolation per environment; Sensitive data handling in state

     Only add principles that are truly required for your use case. -->

## Implementation Approaches
<!-- Cloud Architecture Principles = WHAT infrastructure resources to create
     IaC Code Principles = HOW to write the infrastructure code
     Implementation Approaches = WHEN to use different patterns and complexity levels

     Start with 1-2 key approaches that match your use case, then add more only if needed. -->

### [APPROACH_1_NAME]
<!-- Example: Progressive Complexity (Recommended for most use cases) -->
[APPROACH_1_DESCRIPTION]
<!-- Example: Start simple, layer controls as needs grow; Use Baseline controls initially, add Enhanced controls as requirements mature; Modular design allows incremental additions -->

### [APPROACH_2_NAME]
<!-- Example: Environment-Based Complexity -->
[APPROACH_2_DESCRIPTION]
<!-- Example: Different environments have different complexity levels; Dev/Test use Baseline controls, Staging mirrors production, Production uses Enhanced controls from start; Shared modules with environment-specific configurations -->

<!-- Add more implementation approaches below as needed for your specific requirements.
     Common additional approaches to consider:

     POC / Demo / Learning: Short-lived, limited data sensitivity; Baseline security only, simplified architecture, minimal resources, auto-cleanup tags

     Development Environments: Ongoing use, shared team, non-production data; Baseline security, production-like architecture at reduced scale, cost controls

     Staging / Pre-Production: Production validation, performance testing; Enhanced security controls, architecture mirrors production, multi-zone for HA testing

     Production Environments: Live workloads, customer data, SLAs, compliance; All Enhanced security controls, HA config (multi-zone/region), comprehensive monitoring, DR resources, full backup/retention

     Disaster Recovery Environments: Passive standby for production failover; Minimal running resources, data replication, automated failover procedures, balance cost vs RTO/RPO

     Multi-Region Deployments: Global presence, data residency; Region-specific configurations, data replication strategies, traffic routing (active-active or active-passive)

     Only add approaches that are truly required for your use case. -->

## Governance
<!-- How these principles govern project development and evolution -->

[GOVERNANCE_RULES]
<!-- Example governance rules (add/remove/modify as needed):

     Principles Authority: These principles supersede all other practices and guidelines

     Compliance Enforcement: All specifications, plans, and implementations must demonstrate compliance with these principles; All PRs/reviews must verify compliance

     Complexity Justification: Architectural decisions beyond Baseline patterns require documented justification; Deviations from principles require explicit approval

     Amendment Process: Changes to these principles require documentation, approval, and migration plan; Use semantic versioning (MAJOR/MINOR/PATCH)

     Operational Guidance: Use [GUIDANCE_FILE] for detailed runtime development practices (separate from these foundational principles) -->

**Version**: [PRINCIPLES_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 1.0.0 | Ratified: 2025-11-10 | Last Amended: 2025-11-10 -->