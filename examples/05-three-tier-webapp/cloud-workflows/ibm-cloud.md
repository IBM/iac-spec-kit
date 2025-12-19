# IBM Cloud Workflow for Three-Tier Web Application

## Commands

### Optional: Establish Project Principles

```
/iac.principles This is a production web application. High availability and auto-scaling are important. Balance reliability with cost efficiency. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 1: Describe What You Want

```
/iac.specify I need infrastructure for a three-tier web application. Load balancer to distribute traffic, auto-scaling application servers, managed PostgreSQL database with automated backups and read replicas, Redis cache for session storage. Expected traffic: 10,000-100,000 requests/day. Need 99.9% uptime.
```

**Generates**: `spec.md`, `checklists/requirements.md`

---

### Step 2: Clarify Requirements (Optional)

```
/iac.clarify
```

---

### Step 3: Create Implementation Plan

```
/iac.plan Deploy in us-south. Use VPC Load Balancer, instance groups or Code Engine, Databases for PostgreSQL, Databases for Redis.
```

**Generates**: `plan.md` with inline research

**Optional enrichment**: For quality-critical or complex projects, run `/iac.enrichplan` after `/iac.plan`.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example: VPC Load Balancer, instance groups with auto-scaling or Code Engine, Databases for PostgreSQL with HA, Databases for Redis, VPC with subnets

---

### Step 4: Generate Task Breakdown

```
/iac.tasks
```

**Generates**: `tasks.md`

---

### Step 5: Implement Infrastructure Code

```
/iac.implement
```

**Generates**: Terraform for VPC, load balancer, instance groups/Code Engine, Databases for PostgreSQL and Redis, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` (optional) | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | IBM Cloud-specific architecture with inline research |
| `/iac.enrichplan` (optional) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
