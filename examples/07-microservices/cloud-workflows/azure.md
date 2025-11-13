# Azure Workflow for Microservices Platform

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a cloud-native microservices platform on Azure. Need container orchestration, service mesh, comprehensive observability, and high availability. Use Terraform.
/iac.specify I need infrastructure for a microservices platform. Container orchestration for 10-50 services, service mesh for secure service-to-service communication, API gateway for external traffic, service discovery, distributed tracing, centralized logging, metrics monitoring, message queue for async communication. Services will use different databases. Expected: 100K-1M requests/day. Need 99.95% uptime.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use AKS for Kubernetes, Open Service Mesh or Istio, API Management, Azure Monitor, Application Insights, Azure Database for PostgreSQL, Cosmos DB, Azure Cache for Redis, Service Bus.
```

**plan.md** example: AKS cluster with system/user node pools, service mesh (OSM/Istio), API Management, Azure Monitor + Application Insights, Azure Database for PostgreSQL, Cosmos DB, Service Bus, Key Vault, Virtual Network

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VNet, AKS, service mesh, API Management, databases, messaging, monitoring, Key Vault

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | Azure microservices platform infrastructure |
