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
<!-- Format: [Action] for [Outcome] - e.g., "Design for Simplicity", "Optimize for Cost", "Plan for Failure" -->
[ARCHITECTURE_PRINCIPLE_1_DESCRIPTION]
<!-- Format: [WHY this matters] + [HOW it applies with Baseline/Enhanced patterns]. Create your own based on your infrastructure needs. -->

### [ARCHITECTURE_PRINCIPLE_2_NAME]
<!-- Format: [Action] for [Outcome] - e.g., "Design for Security", "Build for Resilience", "Prepare for Recovery" -->
[ARCHITECTURE_PRINCIPLE_2_DESCRIPTION]
<!-- Format: [WHY this matters] + [HOW it applies with Baseline/Enhanced patterns]. Create your own based on your infrastructure needs. -->

### [ARCHITECTURE_PRINCIPLE_3_NAME]
<!-- Format: [Action] for [Outcome] - e.g., "Instrument for Observability", "Design for Debuggability", "Optimize for Performance" -->
[ARCHITECTURE_PRINCIPLE_3_DESCRIPTION]
<!-- Format: [WHY this matters] + [HOW it applies with Baseline/Enhanced patterns]. Create your own based on your infrastructure needs. -->

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

     NOTE: Unlike Architecture Principles (which are cloud-agnostic), IaC Code Principles
     CAN include tech-specific examples (module registries, validation tools) to reinforce
     key concepts like "use modules over direct resources". However, adapt these examples
     to YOUR chosen cloud provider and IaC tool - don't copy generic lists verbatim.

     FORMAT: Action-oriented title → WHY it matters → Progressive application -->

### [CODE_PRINCIPLE_1_NAME]
<!-- Format: [Action] [Object/Modifier] - e.g., "Leverage Verified Modules", "Prefer Official Packages", "Reuse Before Building" -->
[CODE_PRINCIPLE_1_DESCRIPTION]
<!-- Format: [WHY this matters] + [HOW to apply]. Create your own based on your IaC tool and cloud provider. -->

### [CODE_PRINCIPLE_2_NAME]
<!-- Format: [Action] [Object/Modifier] - e.g., "Validate During Generation", "Test Before Commit", "Enforce Code Quality" -->
[CODE_PRINCIPLE_2_DESCRIPTION]
<!-- Format: [WHY this matters] + [HOW to apply]. Adapt validation tools to YOUR chosen IaC tool. -->

### [CODE_PRINCIPLE_3_NAME]
<!-- Format: [Action] [Object/Modifier] - e.g., "Write Secure Code", "Protect Sensitive Data", "Structure for Clarity" -->
[CODE_PRINCIPLE_3_DESCRIPTION]
<!-- Format: [WHY this matters] + [HOW to apply]. Create your own based on your IaC tool and cloud provider. -->

<!-- Add more code principles below as needed for your specific requirements.
     Common additional principles to consider (expressed as charter-style tenets):

     Structure Code for Clarity and Reusability: Infrastructure code must follow consistent organizational patterns that enhance readability, maintainability, and reuse. Well-structured code reduces cognitive load and accelerates team productivity.

     Document Intent and Architecture Decisions: Infrastructure code must explain its purpose, usage, and key decisions. Documentation serves current and future team members, reducing knowledge silos and onboarding time.

     Enforce Quality Through Standards: Code quality must be measurable and enforceable through automated checks. Quality gates catch issues before they reach deployment, maintaining codebase health over time.

     Define Clear Module Contracts: Modules must have explicit, well-documented interfaces with validation. Clear contracts enable safe reuse and prevent misuse.

     Lock Dependencies for Reproducibility: Infrastructure code must produce consistent results by locking tool and module versions. Provider versions are captured in .terraform.lock.hcl, but module versions are NOT lock-file protected - use exact version pinning (= X.Y.Z) for modules in production. Version control prevents unexpected changes and simplifies troubleshooting.

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
<!-- Format: [Descriptor] [Focus] - e.g., "Progressive Complexity", "Environment-First Design", "Incremental Maturity" -->
[APPROACH_1_DESCRIPTION]
<!-- Format: [Decision framework] + [When to apply]. Create YOUR OWN progression specific to YOUR infrastructure. -->

### [APPROACH_2_NAME]
<!-- Format: [Descriptor] [Focus] - e.g., "Environment-Appropriate Complexity", "Risk-Based Controls", "Cost-Optimized Scaling" -->
[APPROACH_2_DESCRIPTION]
<!-- Format: [Decision framework] + [When to apply]. Create YOUR OWN environment descriptions specific to YOUR project. -->

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

     Compliance and Accountability: All infrastructure specifications, implementation plans, and generated code must demonstrate alignment with these principles. Code reviews and automated checks verify ongoing compliance.

     Justification for Complexity: Architectural decisions that extend beyond Baseline patterns require documented justification explaining the business or technical need. This ensures complexity serves purpose rather than emerging by default. Development environments should remain simple; production environments justify added complexity with business or technical requirements.

     Deviation and Exception Process: Deviations from these principles require explicit acknowledgment, documented rationale, and appropriate approval. Exceptions are tracked and periodically reviewed for patterns suggesting principle amendments.

     Amendment and Evolution: These principles evolve as organizational needs, technology capabilities, and regulatory requirements change. Amendments follow semantic versioning (MAJOR for breaking changes, MINOR for new principles, PATCH for clarifications), require stakeholder review, and include migration guidance when impacting existing infrastructure.

     Relationship to Operational Guidance: These principles establish WHAT and WHY; operational guidance in [GUIDANCE_FILE] addresses day-to-day HOW. Principles remain stable; operational guidance adapts more frequently to tooling and process changes. -->

**Version**: [PRINCIPLES_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 1.0.0 | Ratified: 2025-11-10 | Last Amended: 2025-11-10 -->
