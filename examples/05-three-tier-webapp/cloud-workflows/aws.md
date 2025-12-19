# AWS Workflow for Three-Tier Web Application

This guide shows the commands to deploy a three-tier web application on AWS using IaC Spec Kit.

## Prerequisites

- AWS account with IAM permissions
- IaC Spec Kit installed
- Terraform installed
- AI coding assistant running

## Commands

### Optional: Establish Project Principles

```
/iac.principles This is a production web application. High availability and auto-scaling are important. Balance reliability with cost efficiency. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 1: Describe What You Want

```
/iac.specify I need infrastructure for a three-tier web application. Load balancer to distribute traffic, auto-scaling application servers (containers or VMs), managed PostgreSQL database with automated backups and read replicas, Redis cache for session storage and performance. Expected traffic: 10,000-100,000 requests/day with peaks during business hours. Need 99.9% uptime.
```

**Generates**: `spec.md`, `checklists/requirements.md`

Spec includes cloud-agnostic requirements for load balancing, auto-scaling compute, managed database, caching, monitoring.

---

### Step 2: Clarify Requirements (Optional)

```
/iac.clarify
```

---

### Step 3: Create Implementation Plan

```
/iac.plan Deploy in us-east-1. Use Application Load Balancer, ECS Fargate for containers, RDS PostgreSQL Multi-AZ, ElastiCache Redis.
```

**Generates**: `plan.md` with inline research

**Optional enrichment**: For quality-critical or complex projects, run `/iac.enrichplan` after `/iac.plan`.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example:
- Load Balancing: ALB with SSL termination, health checks
- Compute: ECS Fargate with auto-scaling (CPU/memory targets)
- Database: RDS PostgreSQL Multi-AZ, automated backups, read replica
- Cache: ElastiCache Redis cluster
- Networking: VPC with public (ALB) and private (ECS, RDS, Redis) subnets
- Monitoring: CloudWatch metrics, logs, alarms

---

### Step 4: Generate Task Breakdown

```
/iac.tasks
```

**Generates**: `tasks.md`

---

### Step 5: Implement Infrastructure Code

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform files for VPC, ALB, ECS cluster/services, RDS, ElastiCache, security groups, CloudWatch

---

## Deployment

After `terraform apply`, deploy application container to ECR, update ECS task definition with image URI.

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` (optional) | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | AWS-specific architecture with inline research |
| `/iac.enrichplan` (optional) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
