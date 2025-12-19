# AWS Workflow for Microservices Platform

This guide shows the commands to deploy a microservices platform on AWS using IaC Spec Kit.

## Commands

### Step 1: Establish Project Principles

```
/iac.principles This is a production microservices platform. Comprehensive observability and high availability are critical. Focus on operational excellence. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need infrastructure for a microservices platform. Container orchestration for 10-50 services, service mesh for secure service-to-service communication, API gateway for external traffic, service discovery, distributed tracing, centralized logging, metrics monitoring, message queue for async communication. Services will use different databases (PostgreSQL, MongoDB, Redis). Expected: 100K-1M requests/day. Need 99.95% uptime with fault isolation.
```

**Generates**: `spec.md`, `checklists/requirements.md`

---

### Step 3: Clarify Requirements (Optional)

```
/iac.clarify
```

---

### Step 4: Create Implementation Plan

```
/iac.plan Use EKS for Kubernetes, AWS App Mesh for service mesh, API Gateway for external traffic, CloudWatch for logs and metrics, X-Ray for tracing, RDS PostgreSQL and DocumentDB for databases, ElastiCache Redis, SQS/SNS for messaging.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example:
- Orchestration: EKS cluster with managed node groups, auto-scaling
- Service Mesh: AWS App Mesh with Envoy sidecars
- API Gateway: API Gateway or ALB with Ingress Controller
- Discovery: Kubernetes service discovery, Cloud Map
- Databases: RDS (PostgreSQL), DocumentDB (MongoDB-compatible), ElastiCache (Redis)
- Messaging: SQS for queues, SNS for pub/sub
- Observability: CloudWatch Logs/Metrics, Container Insights, X-Ray, Prometheus/Grafana on EKS
- Networking: VPC with private subnets for EKS, public subnets for load balancers
- Security: IAM roles for service accounts, Secrets Manager, VPC security groups

---

### Step 5: Generate Task Breakdown

```
/iac.tasks
```

**Generates**: `tasks.md` with phased implementation

---

### Step 6: Implement Infrastructure Code

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VPC, EKS cluster, App Mesh, API Gateway, RDS, DocumentDB, ElastiCache, SQS, SNS, CloudWatch, X-Ray, IAM roles, security groups

---

## Post-Deployment

After infrastructure is deployed:
1. Install service mesh data plane (Envoy sidecars)
2. Deploy sample microservices with mesh annotations
3. Configure API Gateway routes
4. Set up dashboards in CloudWatch/Grafana

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | AWS-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
