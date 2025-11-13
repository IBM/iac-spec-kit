# AWS Workflow for Microservices Platform

This guide shows the commands to deploy a microservices platform on AWS using IaC Spec Kit.

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles This is a production microservices platform. Comprehensive observability and high availability are critical. Focus on operational excellence. Use Terraform.
/iac.specify I need infrastructure for a microservices platform. Container orchestration for 10-50 services, service mesh for secure service-to-service communication, API gateway for external traffic, service discovery, distributed tracing, centralized logging, metrics monitoring, message queue for async communication. Services will use different databases (PostgreSQL, MongoDB, Redis). Expected: 100K-1M requests/day. Need 99.95% uptime with fault isolation.
```

**Generates**: `spec.md` with requirements for container orchestration, service mesh, API gateway, observability, databases, messaging

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use EKS for Kubernetes, AWS App Mesh for service mesh, API Gateway for external traffic, CloudWatch for logs and metrics, X-Ray for tracing, RDS PostgreSQL and DocumentDB for databases, ElastiCache Redis, SQS/SNS for messaging.
```

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

### Steps 5-6: Tasks and Implementation

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
| All commands | Standard set | AWS microservices platform infrastructure |
