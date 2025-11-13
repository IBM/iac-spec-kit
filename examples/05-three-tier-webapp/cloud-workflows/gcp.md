# GCP Workflow for Three-Tier Web Application

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a production web application on GCP. Need high availability, auto-scaling, and cost optimization. Use Terraform.
/iac.specify I need infrastructure for a three-tier web application. Load balancer to distribute traffic, auto-scaling application servers, managed PostgreSQL database with automated backups and read replicas, Redis cache for session storage. Expected traffic: 10,000-100,000 requests/day. Need 99.9% uptime.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Deploy in us-central1. Use Cloud Load Balancing, Cloud Run or GKE, Cloud SQL PostgreSQL with HA, Memorystore for Redis.
```

**plan.md** example: HTTPS Load Balancer, Cloud Run with auto-scaling or GKE with node pools, Cloud SQL with HA and read replicas, Memorystore Redis, VPC with Cloud NAT

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VPC, load balancer, Cloud Run/GKE, Cloud SQL, Memorystore, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | GCP-specific three-tier architecture |
