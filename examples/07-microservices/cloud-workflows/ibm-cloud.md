# IBM Cloud Workflow for Microservices Platform

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a cloud-native microservices platform on IBM Cloud. Need container orchestration, service mesh, comprehensive observability, and high availability. Use Terraform.
/iac.specify I need infrastructure for a microservices platform. Container orchestration for 10-50 services, service mesh for secure service-to-service communication, API gateway for external traffic, service discovery, distributed tracing, centralized logging, metrics monitoring, message queue for async communication. Services will use different databases. Expected: 100K-1M requests/day. Need 99.95% uptime.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use IBM Kubernetes Service (IKS) with managed Istio, API Connect, IBM Log Analysis and Monitoring, Databases for PostgreSQL and MongoDB, Databases for Redis, Event Streams.
```

**plan.md** example: IKS cluster with worker pools, managed Istio service mesh, API Connect, IBM Cloud Monitoring with Prometheus, Log Analysis with LogDNA, Databases for PostgreSQL and MongoDB, Databases for Redis, Event Streams (Kafka), Secrets Manager, VPC

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VPC, IKS cluster, Istio, API Connect, databases, Event Streams, monitoring, logging, Secrets Manager

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | IBM Cloud microservices platform infrastructure |
