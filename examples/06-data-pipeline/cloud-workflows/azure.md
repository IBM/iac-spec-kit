# Azure Workflow for Data Processing Pipeline

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles This is a production data pipeline. Prefer serverless and event-driven patterns. Keep it scalable and cost-effective. Use Terraform.
/iac.specify I need a data pipeline to process application events and logs. Ingest from multiple sources, queue for buffering, serverless processing, store raw and processed data in data lake, load into data warehouse for analytics. Expected: 1M events/day growing to 10M. Need data partitioned by date. Budget: under $1000/month.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use Azure Data Lake Storage Gen2, Azure Functions, Event Hub, Data Factory, Synapse Analytics.
```

**plan.md** example: Event Hub for ingestion, Functions for processing, Data Lake Storage with hierarchical namespace, Data Factory for orchestration, Synapse for analytics, Application Insights for monitoring

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for storage accounts, Event Hub namespaces, Function Apps, Data Factory, Synapse workspace, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | Azure-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
