# GCP Workflow for Microservices Platform

## Commands

### Step 1: Establish Project Principles

```
/iac.principles This is a production microservices platform. Comprehensive observability and high availability are critical. Focus on operational excellence. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need infrastructure for a microservices platform. Container orchestration for 10-50 services, service mesh for secure service-to-service communication, API gateway for external traffic, service discovery, distributed tracing, centralized logging, metrics monitoring, message queue for async communication. Services will use different databases. Expected: 100K-1M requests/day. Need 99.95% uptime.
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
/iac.plan Use GKE with Anthos Service Mesh (Istio), Apigee or Cloud Endpoints for API gateway, Cloud Operations (Logging, Monitoring, Trace), Cloud SQL PostgreSQL, Firestore, Memorystore Redis, Pub/Sub.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example: GKE cluster with Autopilot or Standard mode, Anthos Service Mesh, Apigee, Cloud Operations suite, Cloud SQL, Firestore, Memorystore, Pub/Sub, Secret Manager, VPC

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

**Generates**: Terraform for VPC, GKE, Anthos Service Mesh, Apigee, Cloud SQL, Firestore, Memorystore, Pub/Sub, Cloud Operations, Secret Manager

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | GCP-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
