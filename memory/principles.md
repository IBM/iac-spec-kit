# [PROJECT_NAME] Principles
<!-- Example: MyApp Infrastructure Principles, Platform IaC Principles, etc. -->

## Cloud Architecture Principles
<!-- High-level tenets expressing WHAT outcomes infrastructure achieves.
     These are universal philosophies, NOT technical implementation checklists.

     IMPORTANT: Principle selection depends heavily on environment type:

     DEV ENVIRONMENTS typically need:
     - Simplicity (keep it minimal)
     - Security (Baseline only - basic controls)
     - Skip: Observability managed services, HA/DR, Compliance (unless required)

     STAGING ENVIRONMENTS typically need:
     - Simplicity (production-like but not over-engineered)
     - Security (Enhanced - mirrors production)
     - Observability (production-like monitoring/logging)
     - Maybe: Reliability (test HA patterns), Identity (cost tracking)

     PRODUCTION ENVIRONMENTS typically need:
     - Security (Enhanced - comprehensive controls)
     - Observability (comprehensive monitoring/alerting)
     - Reliability (HA/DR based on business needs)
     - Identity (full accountability and cost attribution)
     - Compliance (only if regulatory requirements exist)
     - Simplicity (avoid over-engineering but meet requirements)

     Start with 2-3 principles appropriate for YOUR environment type.
     Use Baseline/Enhanced pattern to express progressive philosophy.

     FORMAT: Action-oriented title → WHY it matters → HOW it applies across environments -->

### [ARCHITECTURE_PRINCIPLE_1_NAME]
<!-- Example: I. Design for Simplicity (NON-NEGOTIABLE) -->
[ARCHITECTURE_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Infrastructure should be as simple as necessary for the use case, avoiding over-engineering and unnecessary complexity. Simple infrastructure is easier to understand, maintain, secure, and troubleshoot. Complexity should serve clear requirements, not emerge by default. Dev environments prioritize minimal viable infrastructure; staging mirrors production architecture at appropriate scale; production adds capabilities only when workload requirements justify the added complexity. -->

### [ARCHITECTURE_PRINCIPLE_2_NAME]
<!-- Example: II. Design for Security (NON-NEGOTIABLE) -->
[ARCHITECTURE_PRINCIPLE_2_DESCRIPTION]
<!-- Example: Security must be built into infrastructure from inception, not added as an afterthought. Every resource implements appropriate security controls that scale with the criticality and sensitivity of the workload. Dev environments use Baseline security (basic controls, no sensitive data); staging environments mirror production security posture; production environments implement Enhanced security including defense-in-depth, comprehensive access controls, encryption, and network isolation appropriate to data sensitivity and risk profile. -->

### [ARCHITECTURE_PRINCIPLE_3_NAME]
<!-- Example: III. Build in Observability (SITUATIONAL - Staging/Production) -->
[ARCHITECTURE_PRINCIPLE_3_DESCRIPTION]
<!-- Example: Infrastructure must provide insight into its health, performance, and behavior to enable operational awareness and issue resolution. Dev environments typically rely on local logs and basic troubleshooting without managed observability services; staging environments implement production-like monitoring to validate observability patterns; production environments require comprehensive telemetry, centralized logging, alerting, and dashboards appropriate to operational complexity and business criticality. -->

<!-- Add more architecture principles below ONLY if your use case truly requires them.

     SITUATIONAL PRINCIPLES - Consider based on environment and requirements:

     Design for Reliability and Resilience (PRODUCTION/STAGING): Infrastructure resilience must match business criticality. This principle groups high availability, disaster recovery, and fault tolerance concerns. Dev environments typically use single-zone, basic availability; staging validates HA patterns; production implements comprehensive availability, failover, and recovery capabilities for mission-critical workloads. (Skip for dev, consider for staging, often required for production)

     Embed Compliance into Architecture (ONLY WHEN REGULATORY REQUIREMENTS EXIST): Regulatory and governance requirements must be addressed architecturally when they exist. This principle groups audit logging, data residency, immutable storage, and regulatory controls. Dev environments may skip compliance controls unless testing compliance features; staging mirrors production compliance posture; production implements comprehensive compliance controls. (Add only when compliance requirements exist)

     Establish Resource Identity and Accountability (MORE IMPORTANT FOR PRODUCTION): Every resource must be identifiable and traceable to its purpose and owner. This principle groups resource naming, tagging, cost attribution, and governance. Dev environments need basic identification; staging uses production-like tagging; production requires comprehensive governance, cost attribution, and automated policy enforcement. (Basic for dev, comprehensive for production)

     Remember: Only add principles that are truly non-negotiable for YOUR environment type.
     A development environment might only need: Simplicity + Security (Baseline)
     A staging environment might need: Simplicity + Security (Enhanced) + Observability
     A production environment might need: Security + Observability + Reliability + Identity
     A regulated production environment might add: Compliance -->

## IaC Code Principles
<!-- High-level tenets expressing HOW infrastructure code is written.
     These focus on code quality, maintainability, security, and validation.
     Code principles typically apply across all environments (dev, staging, production).
     Start with 2-3 critical principles.

     FORMAT: Action-oriented title → WHY it matters → Progressive application -->

### [CODE_PRINCIPLE_1_NAME]
<!-- Example: I. Leverage Proven, Maintained Modules (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Infrastructure code must build on validated, well-maintained modules rather than proliferating custom implementations. Curated modules reduce risk, improve consistency, and accelerate delivery. Use direct provider resources only when modules don't exist or requirements are truly unique. Baseline uses stable community modules; Enhanced requires formally verified or enterprise-supported modules. -->

### [CODE_PRINCIPLE_2_NAME]
<!-- Example: II. Validate Before Deploying (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_2_DESCRIPTION]
<!-- Example: Infrastructure code must be validated before deployment to prevent failures and security vulnerabilities. Testing catches errors early, reduces deployment risk, and builds confidence in changes. Baseline ensures syntax validation and linting; Enhanced implements comprehensive testing including mocked deployments, security scanning, and policy validation. -->

### [CODE_PRINCIPLE_3_NAME]
<!-- Example: III. Write Secure Code by Default (NON-NEGOTIABLE) -->
[CODE_PRINCIPLE_3_DESCRIPTION]
<!-- Example: Security must be inherent in infrastructure code, not retrofitted afterward. Secure coding practices prevent vulnerabilities before resources are deployed. Code never contains hardcoded credentials, implements least-privilege access patterns, and defaults to secure configurations. This principle applies universally regardless of environment or complexity level. -->

<!-- Add more code principles below as needed for your specific requirements.
     Common additional principles to consider (expressed as charter-style tenets):

     Structure Code for Clarity and Reusability: Infrastructure code must follow consistent organizational patterns that enhance readability, maintainability, and reuse. Well-structured code reduces cognitive load and accelerates team productivity.

     Document Intent and Architecture Decisions: Infrastructure code must explain its purpose, usage, and key decisions. Documentation serves current and future team members, reducing knowledge silos and onboarding time.

     Enforce Quality Through Standards: Code quality must be measurable and enforceable through automated checks. Quality gates catch issues before they reach deployment, maintaining codebase health over time.

     Define Clear Module Contracts: Modules must have explicit, well-documented interfaces with validation. Clear contracts enable safe reuse and prevent misuse.

     Lock Dependencies for Reproducibility: Infrastructure code must produce consistent results by locking tool and module versions. Version control prevents unexpected changes and simplifies troubleshooting.

     Manage State with Care and Isolation: Infrastructure state must be managed remotely with appropriate access controls and isolation. Proper state management prevents conflicts, data loss, and unauthorized access.

     Only add principles that are truly required for your use case. -->

## Implementation Approaches
<!-- Cloud Architecture Principles = WHAT outcomes infrastructure achieves
     IaC Code Principles = HOW infrastructure code is written
     Implementation Approaches = WHEN to apply different patterns and complexity levels

     These guide decision-making about complexity trade-offs across different use cases.
     Start with 1-2 key approaches that match your context.

     FORMAT: Approach name → Decision framework → When to apply -->

### [APPROACH_1_NAME]
<!-- Example: Progressive Complexity (Recommended for most use cases) -->
[APPROACH_1_DESCRIPTION]
<!-- Example: Infrastructure should start simple and add complexity only as requirements emerge. This approach minimizes initial investment while maintaining a clear path to enhanced capabilities. Begin with Baseline controls and patterns appropriate for dev/testing; introduce Enhanced controls as environments progress toward staging and production or when workload maturity, sensitivity, or compliance requirements demand them. Modular design enables incremental capability additions without disruptive refactoring. -->

### [APPROACH_2_NAME]
<!-- Example: Environment-Appropriate Complexity -->
[APPROACH_2_DESCRIPTION]
<!-- Example: Infrastructure complexity should match the operational characteristics and risk profile of each environment. Development environments benefit from Baseline simplicity (minimal services, basic security, local troubleshooting); staging environments mirror production architecture with Enhanced controls to validate operational patterns; production environments implement comprehensive Enhanced controls from inception (HA, centralized observability, full security). This approach balances cost efficiency in lower environments with robustness in critical environments while maintaining architectural consistency through shared modules and progressive enhancement. -->

<!-- Add more implementation approaches below as needed for your specific requirements.

     Common additional approaches to consider (expressed as decision frameworks):

     Development and Learning Environments: Short-lived or ongoing development with non-production data prioritizes simplicity and speed. Baseline security ensures basic safety; minimal architecture reduces friction and cost; avoid managed observability services and HA patterns unless specifically testing those features. Use this approach for learning, development, and testing.

     Staging and Pre-Production Environments: Production validation requires high fidelity to production architecture. Enhanced controls mirror production risk posture; observability and reliability patterns match production to validate operational procedures; architecture tests production patterns at scale. Use this approach as final validation before production deployment.

     Production Environments: Live workloads with customer data and business impact demand appropriate controls. Security, reliability, and observability capabilities match risk profile and business requirements. Architecture prioritizes availability, operational excellence, and appropriate complexity. Use this approach for business-critical workloads.

     Disaster Recovery Environments: Standby capability for production failover balances recovery objectives with cost. Minimal active resources reduce cost; automated provisioning enables rapid activation; data replication maintains currency. Use this approach when RTO/RPO requirements justify the investment.

     Only add approaches that are truly required for your use case. -->

## Governance
<!-- How these principles govern project development and evolution -->

[GOVERNANCE_RULES]
<!-- Example governance rules (add/remove/modify as needed):

     Authority and Precedence: These principles represent the foundational governance for all infrastructure development. They supersede individual preferences, tactical decisions, and conflicting guidance. When in doubt, these principles guide the decision.

     Compliance and Accountability: All infrastructure specifications, implementation plans, and deployed resources must demonstrate alignment with these principles. Code reviews, automated checks, and operational reviews verify ongoing compliance.

     Justification for Complexity: Architectural decisions that extend beyond Baseline patterns require documented justification explaining the business or technical need. This ensures complexity serves purpose rather than emerging by default. Development environments should remain simple; production environments justify added complexity with business or technical requirements.

     Deviation and Exception Process: Deviations from these principles require explicit acknowledgment, documented rationale, and appropriate approval. Exceptions are tracked and periodically reviewed for patterns suggesting principle amendments.

     Amendment and Evolution: These principles evolve as organizational needs, technology capabilities, and regulatory requirements change. Amendments follow semantic versioning (MAJOR for breaking changes, MINOR for new principles, PATCH for clarifications), require stakeholder review, and include migration guidance when impacting existing infrastructure.

     Relationship to Operational Guidance: These principles establish WHAT and WHY; operational guidance in [GUIDANCE_FILE] addresses day-to-day HOW. Principles remain stable; operational guidance adapts more frequently to tooling and process changes. -->

**Version**: [PRINCIPLES_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 1.0.0 | Ratified: 2025-11-10 | Last Amended: 2025-11-10 -->
