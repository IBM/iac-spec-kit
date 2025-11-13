# GCP Workflow for Microservices Platform

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a cloud-native microservices platform on GCP. Need container orchestration, service mesh, comprehensive observability, and high availability. Use Terraform.
/iac.specify I need infrastructure for a microservices platform. Container orchestration for 10-50 services, service mesh for secure service-to-service communication, API gateway for external traffic, service discovery, distributed tracing, centralized logging, metrics monitoring, message queue for async communication. Services will use different databases. Expected: 100K-1M requests/day. Need 99.95% uptime.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use GKE with Anthos Service Mesh (Istio), Apigee or Cloud Endpoints for API gateway, Cloud Operations (Logging, Monitoring, Trace), Cloud SQL PostgreSQL, Firestore, Memorystore Redis, Pub/Sub.
```

**plan.md** example: GKE cluster with Autopilot or Standard mode, Anthos Service Mesh, Apigee, Cloud Operations suite, Cloud SQL, Firestore, Memorystore, Pub/Sub, Secret Manager, VPC

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for VPC, GKE, Anthos Service Mesh, Apigee, Cloud SQL, Firestore, Memorystore, Pub/Sub, Cloud Operations, Secret Manager

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | GCP microservices platform infrastructure |
