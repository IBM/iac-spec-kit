# Writing Tech-Agnostic Infrastructure Specifications

This guide helps you write effective infrastructure specifications using generic terms rather than cloud-specific service names.

## The Challenge

Infrastructure specifications face a unique challenge compared to application development:

- **Application specs** can often be completely tech-agnostic: "Users need to see their data in real-time" doesn't assume React, Vue, or any specific framework
- **Infrastructure specs** need some technical context: decisions like "managed vs self-managed database" or "serverless vs VMs" affect costs, operations, and feasibility

The key principle: **Use generic infrastructure terms in specifications, translate to cloud-specific services in plans.**

You might already know your cloud provider (e.g., IBM Cloud or AWS), but your spec should describe requirements using generic terms like "managed database" or "object storage" instead of cloud-specific service names like "RDS", "S3", or "Cloud SQL".

The question is: **How much technical detail belongs in the specification vs the plan?**

## The Abstraction Balance

IaC Spec Kit uses a balanced approach:

### ✅ Include in Specifications (High-Level Technical Decisions)

Include architectural patterns and service categories that significantly impact your requirements:

**Compute Models:**
- "Serverless functions" vs "Virtual machines" vs "Containerized workloads"
- "Auto-scaling compute" vs "Fixed capacity"

**Data Storage:**
- "Managed database service" vs "Self-managed database on VMs"
- "Relational database" vs "NoSQL database" vs "Time-series database"
- "Object storage" vs "Block storage" vs "File storage"

**Networking:**
- "Content delivery network for static assets"
- "Load balancer for traffic distribution"
- "Private network isolation"

**Operations:**
- "Automated backups with point-in-time recovery"
- "Multi-zone deployment for high availability"
- "Monitoring and alerting infrastructure"

**Why include these?** They affect cost, operational complexity, and feasibility. A team comfortable with VMs might struggle with serverless, affecting timeline and risk.

### ❌ Avoid in Specifications (Cloud-Specific Implementation)

Do not include cloud provider-specific services or implementation details:

**Don't specify:**
- Cloud providers: "AWS", "Azure", "GCP", "IBM Cloud"
- Specific services: "RDS", "Lambda", "S3", "EKS", "Cloud Run", "Azure Blob Storage"
- Service tiers: "db.t3.micro", "F1 instance", "Standard_B2s"
- Provider features: "AWS WAF rules", "Azure Front Door", "GCP Cloud Armor"
- IaC tools: "Terraform modules", "CloudFormation templates", "Pulumi programs"

**Why avoid these?** They belong in the implementation plan, where you've researched the specific cloud provider and can make informed technical decisions based on available services, pricing, and features.

## Good vs Bad Examples

### Example 1: Database Requirements

**❌ Too Cloud-Specific:**
> "Use AWS RDS PostgreSQL with db.r5.large instance type in Multi-AZ configuration with 500GB GP3 storage"

**✅ Tech-Agnostic with Appropriate Detail:**
> "Managed relational database service (PostgreSQL-compatible) with automated backups, point-in-time recovery, and multi-zone deployment for high availability. Estimated capacity: 4 vCPU, 16GB RAM, 500GB storage."

**Why it works:** Specifies requirements (managed service, HA, backup capabilities) and sizing without locking into AWS RDS.

---

### Example 2: Compute Requirements

**❌ Too Vague:**
> "Needs to be scalable"

**❌ Too Cloud-Specific:**
> "Deploy on AWS Lambda with 512MB memory and 30-second timeout"

**✅ Tech-Agnostic with Appropriate Detail:**
> "Serverless compute for event-driven processing. Each invocation processes 1-100 records, requires 512MB memory, completes within 30 seconds. Must auto-scale to handle 0-10,000 requests/minute."

**Why it works:** Specifies the compute model (serverless), performance requirements, and scale without choosing Lambda, Cloud Functions, or Azure Functions.

---

### Example 3: Storage Requirements

**❌ Too Cloud-Specific:**
> "Use S3 Standard storage class with lifecycle policies to move to Glacier after 90 days"

**✅ Tech-Agnostic with Appropriate Detail:**
> "Object storage for media files with automatic tiering to archive storage after 90 days. Hot storage: <100ms access latency. Archive storage: retrieval within 12 hours acceptable. Estimated 1TB initially, growing 100GB/month."

**Why it works:** Describes storage characteristics (object storage, tiering, latency) without specifying S3/Glacier.

---

### Example 4: Networking Requirements

**❌ Too Cloud-Specific:**
> "Use AWS VPC with 10.0.0.0/16 CIDR, public subnets in us-east-1a and us-east-1b, NAT Gateway for private subnet egress"

**✅ Tech-Agnostic with Appropriate Detail:**
> "Isolated virtual network with public and private subnets across multiple availability zones. Public subnets host load balancers, private subnets host application and database resources. Private resources require outbound internet access for updates."

**Why it works:** Specifies network topology and isolation requirements without dictating VPC or specific subnet configurations.

## Common Patterns for IaC Specifications

### Pattern 1: Service Category + Characteristics

Instead of naming services, describe the category and required characteristics:

| Instead of... | Use... |
|---------------|--------|
| "AWS ECS Fargate" | "Managed container orchestration service (serverless model preferred)" |
| "Azure Application Gateway" | "Load balancer with SSL termination and path-based routing" |
| "Google Cloud Storage" | "Object storage with 99.99% availability SLA" |
| "IBM Databases for MySQL" | "Managed relational database (MySQL-compatible) with automated backups" |

### Pattern 2: Capability + Performance Requirements

Describe what you need and how it should perform:

| Instead of... | Use... |
|---------------|--------|
| "Use CDN" | "Content delivery network to serve static assets with <50ms latency globally" |
| "Enable auto-scaling" | "Compute resources must scale from 2 to 20 instances based on CPU utilization (target: 70%)" |
| "Configure monitoring" | "Monitoring infrastructure to track response times, error rates, and resource utilization with 1-minute granularity" |

### Pattern 3: Outcomes Over Implementation

Focus on the desired outcome rather than how to achieve it:

| Instead of... | Use... |
|---------------|--------|
| "Set up CloudWatch alarms" | "Alert operations team when response time p95 exceeds 500ms or error rate exceeds 1%" |
| "Configure RDS automated backups" | "Database backups taken daily with 30-day retention and point-in-time recovery capability" |
| "Implement IAM roles" | "Service components must use temporary credentials with least-privilege access following the principle of separation of duties" |

## When to Include Technical Specifics

Sometimes you have legitimate technical requirements. Here's when it's appropriate:

### Compliance or Regulatory Requirements

**Acceptable:**
> "Database must support encryption at rest using FIPS 140-2 validated cryptographic modules"

**Why:** Compliance requirement that affects provider selection.

### Integration Requirements

**Acceptable:**
> "Must integrate with existing MySQL 8.0 database using native replication protocol"

**Why:** Technical constraint from existing systems.

### Team Capabilities

**Acceptable:**
> "Team has expertise in containerized deployments but not serverless architectures. Prefer container-based solutions."

**Why:** Affects risk, timeline, and operational success.

### Budget Constraints with Technical Implications

**Acceptable:**
> "Budget constraint of $500/month favors serverless or managed services over self-managed infrastructure to minimize operational overhead"

**Why:** Technical decision directly driven by business constraint.

## Writing Effective Success Criteria

Success criteria must be measurable and technology-agnostic:

**✅ Good Success Criteria:**
- "Infrastructure deploys in under 15 minutes"
- "System handles 10,000 requests/second with p95 latency under 200ms"
- "Database failover completes in under 5 minutes with zero data loss"
- "Costs remain under $500/month for projected traffic (5,000 daily users)"

**❌ Bad Success Criteria:**
- "Uses terraform-aws-modules" (implementation detail)
- "RDS instance is db.t3.small" (too specific, not outcome-focused)
- "Three availability zones" (architecture detail, not outcome)
- "VPC has /16 CIDR" (implementation detail)

## The IaC Spec Kit Workflow

Understanding where technical decisions happen:

```
1. /iac.principles
   → Project governance rules (cloud-agnostic)
   → Example: "Prefer managed services", "Progressive complexity"

2. /iac.specify
   → Requirements specification (cloud-agnostic with high-level technical decisions)
   → Example: "Managed database service", "Serverless compute"

3. /iac.clarify
   → Resolve ambiguities (still cloud-agnostic)
   → Example: Clarify "managed database" → PostgreSQL vs MySQL

4. /iac.plan
   → Cloud provider and specific services (cloud-specific)
   → Example: AWS → RDS PostgreSQL, GCP → Cloud SQL PostgreSQL

5. /iac.implement
   → Generate IaC code (provider-specific)
   → Example: Terraform with terraform-aws-modules
```

**Key insight:** Technical decisions progressively refine from general (managed database) to specific (RDS PostgreSQL db.r5.large) as you move through the workflow.

## Quick Reference

**Use generic terms:**
- ✅ "Managed database service" → ❌ "RDS"
- ✅ "Object storage" → ❌ "S3"
- ✅ "Serverless compute" → ❌ "Lambda"
- ✅ "Container orchestration" → ❌ "EKS"
- ✅ "Load balancer" → ❌ "ALB"
- ✅ "Content delivery network" → ❌ "CloudFront"

**Include high-level technical decisions:**
- ✅ "Managed vs self-managed"
- ✅ "Serverless vs VMs vs containers"
- ✅ "Relational vs NoSQL database"
- ✅ "Multi-zone deployment for HA"
- ✅ "Automated backup and recovery"

**Focus on outcomes:**
- ✅ Performance targets (latency, throughput)
- ✅ Availability goals (uptime, failover time)
- ✅ Security requirements (encryption, isolation)
- ✅ Cost constraints (budget limits)
- ✅ Operational needs (monitoring, alerting)

## Need Help?

- See [examples/](../examples/) for complete specification examples
- Review the [WordPress example](../examples/03-wordpress/) showing cloud-agnostic specs deployed to 4 clouds
- Check the [spec template](../templates/spec-template.md) for guidance and examples
