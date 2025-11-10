# Infrastructure Specification: [INFRASTRUCTURE_NAME]
<!-- Example: Production Web Platform, Data Analytics Infrastructure, Multi-Region DR Setup -->

**Spec ID**: `[###-infrastructure-name]`
**Created**: [DATE]
**Status**: Draft
**Input**: User description: "$ARGUMENTS"

## Executive Summary *(mandatory)*

<!--
  ACTION REQUIRED: Provide a concise overview of what infrastructure this spec defines and its primary purpose.
-->

[Brief description of the infrastructure and its purpose, e.g., "This specification defines the infrastructure requirements for a highly available e-commerce platform supporting 100K daily active users. The infrastructure will enable 99.99% uptime, sub-second response times, and automatic scaling to handle peak shopping periods."]

## Problem Statement *(mandatory)*

### Current State

<!--
  ACTION REQUIRED: Describe the existing infrastructure situation or lack thereof.
-->

[Description of current infrastructure state, e.g., "Applications currently run on aging on-premises servers with frequent outages, no disaster recovery, and manual scaling requiring 2-3 hours response time."]

### Desired State

<!--
  ACTION REQUIRED: Describe the target infrastructure capabilities and characteristics.
-->

[Description of target infrastructure state, e.g., "Cloud-native infrastructure with auto-scaling, multi-region failover, and zero-downtime deployments managed through Infrastructure as Code."]

### Business Impact

<!--
  ACTION REQUIRED: Explain the business value and risks.
-->

[Business value and risk analysis, e.g., "Benefits: 50% reduction in downtime, 3x faster feature deployment, 40% cost optimization. Risks if not implemented: continued revenue loss from outages, inability to handle growth, security vulnerabilities."]

## Infrastructure Requirements *(mandatory)*

<!--
  Define WHAT infrastructure capabilities are needed, not HOW to implement.
  Keep technology-agnostic - no cloud provider names (AWS/IBM Cloud/Oracle/Azure/GCP).

  Example Infrastructure Requirements:
  - Virtual private network with public and private subnets
  - Compute instances with auto-scaling groups
  - Load balancer for traffic distribution
  - Managed relational database with automated backups
  - Object storage for static files and backups
  - Container orchestration platform with auto-scaling
  - Security groups and network access control lists
  - Identity and access management policies
  - Content delivery network for static assets
  - Message queue for asynchronous processing
  - Monitoring and logging infrastructure
  - Secrets management service
  - DNS and domain management
  - VPN or private connectivity to on-premises
-->

### Functional Requirements

<!--
  ACTION REQUIRED: List specific infrastructure capabilities that MUST be provided.
  Mark unclear requirements with NEEDS CLARIFICATION.
-->

- **FR-001**: Infrastructure MUST [specific capability, e.g., "provide a virtual private network with network segmentation"]
- **FR-002**: Infrastructure MUST [specific capability, e.g., "provide managed database with automatic failover"]
- **FR-003**: Infrastructure MUST [specific capability, e.g., "implement auto-scaling based on load metrics"]
- **FR-004**: Infrastructure MUST [specific capability]
- **FR-005**: Infrastructure MUST [specific capability]

[Add more as needed]

*Example of marking unclear requirements:*

- **FR-006**: Infrastructure MUST [NEEDS CLARIFICATION: e.g., "provide compute resources - serverless, containers, or VMs?"]

### Non-Functional Requirements

#### Performance

<!--
  ACTION REQUIRED: Define performance requirements.
-->

- [Performance requirement, e.g., "API response latency p95 < 100ms, p99 < 200ms"]
- [Performance requirement, e.g., "Support 10,000 requests per second"]
- [Performance requirement, e.g., "Handle 50,000 concurrent connections"]

#### Availability

<!--
  ACTION REQUIRED: Define availability requirements.
-->

- [Availability requirement, e.g., "99.95% uptime SLO (4.38 hours downtime/year)"]
- [Availability requirement, e.g., "Active-active across 3 availability zones"]
- [Availability requirement, e.g., "RTO < 1 hour, RPO < 15 minutes"]

#### Security

<!--
  ACTION REQUIRED: Define security requirements.
-->

- [Security requirement, e.g., "AES-256 encryption for data at rest"]
- [Security requirement, e.g., "TLS 1.2+ for all communications"]
- [Security requirement, e.g., "Private subnets for compute, public only for load balancers"]
- [Security requirement, e.g., "Role-based access with MFA for administrative operations"]

#### Scalability

<!--
  ACTION REQUIRED: Define scalability requirements.
-->

- [Scalability requirement, e.g., "Scale from 2 to 100 instances based on demand"]
- [Scalability requirement, e.g., "Auto-scale triggers: CPU > 70%, Memory > 80%"]
- [Scalability requirement, e.g., "New instances operational within 90 seconds"]

## Service Level Objectives (SLOs) *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable, technology-independent success criteria.
  Must be verifiable without knowing implementation details.
-->

- [SLO with measurement criteria, e.g., "Availability: 99.95% uptime measured over 30-day rolling window"]
- [SLO with measurement criteria, e.g., "Latency: 95th percentile response time < 100ms"]
- [SLO with measurement criteria, e.g., "Error Rate: Less than 0.1% failed requests"]
- [SLO with measurement criteria, e.g., "Recovery: Full restoration within 1 hour of outage"]

## Cost Constraints *(mandatory)*

### Budget

<!--
  ACTION REQUIRED: Define budget constraints and targets.
-->

[Budget constraints and targets, e.g., "Initial setup: $10,000 one-time; Monthly operating: $5,000 ± 10%; Annual: $60,000 including reserved capacity"]

### Cost Optimization

<!--
  ACTION REQUIRED: Define cost optimization strategies.
-->

[Cost optimization strategies, e.g., "Use reserved instances for baseline capacity; Scale down during off-peak hours; Archive logs after 30 days"]

## Compliance Requirements *(include if applicable)*

### Regulatory Frameworks

<!--
  ACTION REQUIRED: List applicable compliance frameworks.
-->

[Applicable compliance frameworks, e.g., "SOC 2 Type II, HIPAA, PCI-DSS Level 1, GDPR"]

### Data Requirements

<!--
  ACTION REQUIRED: Define data handling and retention requirements.
-->

[Data handling and retention requirements, e.g., "Data residency in US regions only; 7-year retention for audit logs; Encryption required for PII"]

## Success Criteria *(mandatory)*

<!--
  ACTION REQUIRED: Define measurable and verifiable criteria for successful deployment.
  Infrastructure is considered successfully deployed when these criteria are met.
-->

### Deployment Validation

- [ ] [Deployment validation criterion, e.g., "All resources deployed in correct regions"]
- [ ] [Deployment validation criterion, e.g., "Zero drift from IaC definitions"]
- [ ] [Deployment validation criterion, e.g., "Required tags applied to all resources"]

### Security Validation

- [ ] [Security validation criterion, e.g., "No HIGH/CRITICAL findings in security scans"]
- [ ] [Security validation criterion, e.g., "Encryption enabled for all data stores"]
- [ ] [Security validation criterion, e.g., "IAM policies follow least privilege"]

### Performance Validation

- [ ] [Performance validation criterion, e.g., "Load testing meets throughput requirements"]
- [ ] [Performance validation criterion, e.g., "Auto-scaling tested and working"]
- [ ] [Performance validation criterion, e.g., "Latency targets achieved under load"]

### Operational Validation

- [ ] [Operational validation criterion, e.g., "Monitoring dashboards configured"]
- [ ] [Operational validation criterion, e.g., "Alerts routing correctly"]
- [ ] [Operational validation criterion, e.g., "Backup/restore validated"]

## Assumptions *(include if making assumptions)*

<!--
  ACTION REQUIRED: Document any assumptions made when creating this specification.
-->

- [Assumption, e.g., "Assume 20% monthly traffic growth"]
- [Assumption, e.g., "Assume read-heavy workload (80% reads, 20% writes)"]
- [Assumption, e.g., "Assume business hours 6 AM - 10 PM EST"]

## Out of Scope *(include if explicitly excluding items)*

<!--
  ACTION REQUIRED: Clearly state what this infrastructure will NOT include.
-->

- [Out of scope item, e.g., "Application code deployment (handled separately)"]
- [Out of scope item, e.g., "Email service (using existing corporate email)"]
- [Out of scope item, e.g., "Legacy system migration (phase 2 project)"]

## Dependencies *(include if external dependencies exist)*

<!--
  ACTION REQUIRED: List external systems or services this infrastructure depends on.
-->

- [External dependency, e.g., "Corporate Active Directory for authentication"]
- [External dependency, e.g., "Existing VPN connection to datacenter"]
- [External dependency, e.g., "Third-party monitoring service (Datadog)"]

## Notes

- [Additional note or context]
- [Additional note or context]

---

**Specification Quality Checklist**:
- [ ] No implementation details (cloud providers, specific tools)
- [ ] All requirements are testable and unambiguous
- [ ] Success criteria are measurable
- [ ] Cost constraints clearly defined
- [ ] Compliance requirements specified (if applicable)