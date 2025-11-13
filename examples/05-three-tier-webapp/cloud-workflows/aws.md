# AWS Workflow for Three-Tier Web Application

This guide shows the commands to deploy a three-tier web application on AWS using IaC Spec Kit.

## Prerequisites

- AWS account with IAM permissions
- IaC Spec Kit installed
- Terraform installed
- AI coding assistant running

## Commands

### Step 1: Establish Project Principles

```
/iac.principles This is a production web application. High availability and auto-scaling are important. Balance reliability with cost efficiency. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need infrastructure for a three-tier web application. Load balancer to distribute traffic, auto-scaling application servers (containers or VMs), managed PostgreSQL database with automated backups and read replicas, Redis cache for session storage and performance. Expected traffic: 10,000-100,000 requests/day with peaks during business hours. Need 99.9% uptime.
```

**Generates**: `spec.md`, `checklists/requirements.md`

Spec includes cloud-agnostic requirements for load balancing, auto-scaling compute, managed database, caching, monitoring.

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Deploy in us-east-1. Use Application Load Balancer, ECS Fargate for containers, RDS PostgreSQL Multi-AZ, ElastiCache Redis.
```

**plan.md** example:
- Load Balancing: ALB with SSL termination, health checks
- Compute: ECS Fargate with auto-scaling (CPU/memory targets)
- Database: RDS PostgreSQL Multi-AZ, automated backups, read replica
- Cache: ElastiCache Redis cluster
- Networking: VPC with public (ALB) and private (ECS, RDS, Redis) subnets
- Monitoring: CloudWatch metrics, logs, alarms

---

### Steps 5-6: Tasks and Implementation

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
| `/iac.principles` | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, checklists | Requirements |
| `/iac.plan` | `plan.md`, etc. | AWS architecture |
| `/iac.tasks` | `tasks.md` | Tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
