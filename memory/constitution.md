# [PROJECT_NAME] Constitution
<!-- Example: Infrastructure as Code Constitution, ACME Platform IaC Constitution, etc. -->

## Core Principles

### [PRINCIPLE_1_NAME]
<!-- Example: I. Infrastructure as Code Principle -->
[PRINCIPLE_1_DESCRIPTION]
<!-- Example: All infrastructure MUST be defined as declarative code (Terraform/CloudFormation/Pulumi); Manual changes prohibited except emergency breakfix (backport within 24 hours); Infrastructure state traceable to version-controlled code; Drift detection runs hourly with automated remediation -->

### [PRINCIPLE_2_NAME]
<!-- Example: II. Security-First Gate (NON-NEGOTIABLE) -->
[PRINCIPLE_2_DESCRIPTION]
<!-- Example: Encryption: AES-256 at rest, TLS 1.2+ in transit, KMS key management; Access Control: Least privilege IAM, no long-lived credentials, RBAC, MFA for privileged access; Network Security: Private subnets for workloads, no 0.0.0.0/0 ingress except load balancers, network segmentation; Audit Logging: All API calls logged, encrypted logs, 1-year retention minimum; Enforcement: Automated scanning (Checkov, tfsec, Snyk) with hard-fail on HIGH/CRITICAL findings -->

### [PRINCIPLE_3_NAME]
<!-- Example: III. Test-Before-Deploy Mandate -->
[PRINCIPLE_3_DESCRIPTION]
<!-- Example: Required testing phases: 1) Static analysis (terraform fmt, validate, tflint) 2) Security scanning (Checkov, tfsec, secrets detection) 3) Dry-run validation (terraform plan, cost estimation) 4) Integration testing (deploy to ephemeral environment, functional validation) 5) Approval gates (peer review required, manual approval for production) -->

### [PRINCIPLE_4_NAME]
<!-- Example: IV. State Management Standards -->
[PRINCIPLE_4_DESCRIPTION]
<!-- Example: Remote state storage (IBM Cloud Object Storage/Terraform Cloud) with encryption; State locking enabled to prevent concurrent modifications; Separate state per environment and major component (minimize blast radius); State versioning enabled for rollback capability; Never commit state to version control -->

### [PRINCIPLE_5_NAME]
<!-- Example: V. Compliance and Audit Requirements -->
[PRINCIPLE_5_DESCRIPTION]
<!-- Example: Tag all resources: Environment, Owner, CostCenter, ComplianceScope; Data residency requirements respected (specify approved regions); Compliance validation automated in CI/CD; Architecture diagrams generated from deployed state; Change logs maintained with business justification -->

### [PRINCIPLE_6_NAME]
<!-- Example: VI. Cost Governance -->
[PRINCIPLE_6_DESCRIPTION]
<!-- Example: Budget defined per project/environment with alerts at 75%, 90%, 100%; Approved instance types/SKUs for each workload category; Pre-deployment cost estimation (Infracost) within ±10% of budget; Mandatory cost allocation tags for chargeback/showback -->

### [PRINCIPLE_7_NAME]
<!-- Example: VII. Module Design Principles -->
[PRINCIPLE_7_DESCRIPTION]
<!-- Example: Single responsibility per module; Standard structure (HashiCorp/Pulumi patterns); Semantic versioning (pin exact versions, no ranges); Comprehensive testing (unit + integration); Auto-generated documentation -->

## [SECTION_2_NAME]
<!-- Example: Technology Stack and Platform Standards -->

### [TECH_PRINCIPLE_1_NAME]
<!-- Example: Cloud Platform Strategy -->
[TECH_PRINCIPLE_1_DESCRIPTION]
<!-- Example: Primary Cloud: IBM Cloud (us-south, us-east, eu-de); Secondary Cloud: AWS (us-east-1, us-west-2) for DR only; Prohibited: On-premises deployments without approval; Multi-cloud: Allowed only for DR and data sovereignty requirements; Region Strategy: Primary region us-south, DR region us-east, data residency per compliance -->

### [TECH_PRINCIPLE_2_NAME]
<!-- Example: Infrastructure as Code Technology -->
[TECH_PRINCIPLE_2_DESCRIPTION]
<!-- Example: Primary IaC: Terraform 1.6+ (required for all new infrastructure); Legacy Support: IBM Schematics (existing templates only, migrate by Q4); State Management: IBM Cloud Object Storage with locking, or Terraform Cloud with SSO; Provider Versions: IBM Provider ~> 1.60, Kubernetes Provider ~> 2.23, pin all versions; Module Sources: Private registry only, no public modules without security review -->

### [TECH_PRINCIPLE_3_NAME]
<!-- Example: CI/CD and Automation Platform -->
[TECH_PRINCIPLE_3_DESCRIPTION]
<!-- Example: CI/CD Platform: GitHub Actions with OIDC (no long-lived credentials); Deployment Automation: Terraform Cloud runs or GitHub Actions workflows; Secret Management: IBM Secrets Manager or HashiCorp Vault only; Approval Workflow: PR reviews required, protected branches for main; Pipeline Requirements: Must include security scanning, cost estimation, policy checks -->

### [TECH_PRINCIPLE_4_NAME]
<!-- Example: Security and Compliance Toolchain -->
[TECH_PRINCIPLE_4_DESCRIPTION]
<!-- Example: Security Scanning: Checkov 3.0+, tfsec latest, mandatory pre-commit hooks; Policy Framework: Open Policy Agent (OPA) for policy-as-code; Compliance Scanning: IBM Cloud Security and Compliance Center, Cloud Custodian for multi-cloud; Secret Detection: git-secrets, truffleHog in CI pipeline; Vulnerability Management: Snyk for dependency scanning, Trivy for containers -->

### [TECH_PRINCIPLE_5_NAME]
<!-- Example: Testing and Validation Tools -->
[TECH_PRINCIPLE_5_DESCRIPTION]
<!-- Example: Testing Framework: Terratest (Go) for integration tests, required for all modules; Local Testing: IBM Cloud local development tools, container-based testing environments; Static Analysis: tflint with company ruleset, terraform validate; Cost Estimation: Infracost with 10% tolerance threshold; Performance Testing: k6 for load testing, resilience testing in non-prod environments -->

## [SECTION_3_NAME]
<!-- Example: Governance and Enforcement, Amendment Procedures, Exception Process, etc. -->

[SECTION_3_CONTENT]
<!-- Example: Constitutional amendments require RFC document and platform team approval; Quarterly compliance audits with automated weekly drift reports; All changes must pass validation gates or trigger automatic rollback; Exceptions require business justification, risk assessment, and time-bound waiver (max 90 days) -->

## Governance
<!-- Example: Constitution supersedes all other practices; Amendments require documentation, approval, migration plan -->

[GOVERNANCE_RULES]
<!-- Example: All infrastructure changes must verify constitutional compliance; Violations trigger automatic rollback; Use terraform.tfvars for runtime configuration; Infrastructure state reviewed weekly; Drift remediated within 24 hours -->

**Version**: [CONSTITUTION_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 1.0.0 | Ratified: 2025-01-15 | Last Amended: 2025-01-15 -->