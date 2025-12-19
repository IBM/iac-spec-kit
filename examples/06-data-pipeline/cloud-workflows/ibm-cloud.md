# IBM Cloud Workflow for Data Processing Pipeline

## Commands

### Step 1: Establish Project Principles

```
/iac.principles This is a production data pipeline. Prefer serverless and event-driven patterns. Keep it scalable and cost-effective. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need a data pipeline to process application events and logs. Ingest from multiple sources, queue for buffering, serverless processing, store raw and processed data in data lake, load into data warehouse for analytics. Expected: 1M events/day growing to 10M. Need data partitioned by date. Budget: under $1000/month.
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
/iac.plan Use Cloud Object Storage for data lake, Cloud Functions for processing, Event Streams (Kafka), Data Engine (Presto), Db2 Warehouse.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example: Event Streams for messaging, Cloud Functions for processing, COS buckets with lifecycle, Data Engine for SQL queries on data lake, Db2 Warehouse for analytics, monitoring with Activity Tracker and Log Analysis

---

### Step 5: Generate Task Breakdown

```
/iac.tasks
```

**Generates**: `tasks.md` with phased implementation

---

### Step 6: Implement Infrastructure Code

```
/iac.implement
```

**Generates**: Terraform for COS buckets, Event Streams, Cloud Functions, Data Engine, Db2 Warehouse, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | IBM Cloud-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
