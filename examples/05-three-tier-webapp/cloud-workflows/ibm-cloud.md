# IBM Cloud Workflow for Three-Tier Web Application

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a production web application on IBM Cloud. Need high availability, auto-scaling, and cost optimization. Use Terraform.
/iac.specify I need infrastructure for a three-tier web application. Load balancer to distribute traffic, auto-scaling application servers, managed PostgreSQL database with automated backups and read replicas, Redis cache for session storage. Expected traffic: 10,000-100,000 requests/day. Need 99.9% uptime.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Deploy in us-south. Use VPC Load Balancer, instance groups or Code Engine, Databases for PostgreSQL, Databases for Redis.
```

**plan.md** example: VPC Load Balancer, instance groups with auto-scaling or Code Engine, Databases for PostgreSQL with HA, Databases for Redis, VPC with subnets

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VPC, load balancer, instance groups/Code Engine, Databases for PostgreSQL and Redis, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | IBM Cloud-specific three-tier architecture |
