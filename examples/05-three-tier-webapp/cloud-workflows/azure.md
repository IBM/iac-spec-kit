# Azure Workflow for Three-Tier Web Application

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a production web application on Azure. Need high availability, auto-scaling, and cost optimization. Use Terraform.
/iac.specify I need infrastructure for a three-tier web application. Load balancer to distribute traffic, auto-scaling application servers, managed PostgreSQL database with automated backups and read replicas, Redis cache for session storage. Expected traffic: 10,000-100,000 requests/day. Need 99.9% uptime.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Deploy in East US. Use Application Gateway, App Service with auto-scale, Azure Database for PostgreSQL Flexible Server, Azure Cache for Redis.
```

**plan.md** example: App Gateway with WAF, App Service with scale rules, PostgreSQL with HA, Redis Premium tier, Virtual Network with subnets

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VNet, App Gateway, App Service plans/apps, Azure Database, Redis Cache, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | Azure-specific three-tier architecture |
