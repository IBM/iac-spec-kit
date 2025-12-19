# AWS Workflow for Data Processing Pipeline

This guide shows the commands to deploy a data pipeline on AWS using IaC Spec Kit.

## Commands

### Step 1: Establish Project Principles

```
/iac.principles This is a production data pipeline. Prefer serverless and event-driven patterns. Keep it scalable and cost-effective. Use Terraform.
```

**Generates**: `.specify/memory/principles.md`

---

### Step 2: Describe What You Want

```
/iac.specify I need a data pipeline to process application events and logs. Ingest from multiple sources, queue for buffering, serverless processing for transformation, store raw and processed data in data lake, load processed data into data warehouse for analytics. Expected: 1M events/day growing to 10M. Need data partitioned by date. Must track data lineage and quality. Budget: under $1000/month.
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
/iac.plan Use S3 for data lake, Lambda for processing, Kinesis Data Streams for ingestion, Glue for ETL and catalog, Athena for queries, Step Functions for orchestration.
```

**Generates**: `plan.md` with inline research

**Enriched workflow** (recommended): Run `/iac.enrichplan` after `/iac.plan` for comprehensive documentation.

```
/iac.enrichplan
```

**Generates** (enriched): `research.md`, `architecture.md`, `modules.md`, `quickstart.md`

**plan.md** example:
- Ingestion: Kinesis Data Streams or API Gateway → Lambda
- Queue: SQS for decoupling
- Processing: Lambda functions with retries and DLQ
- Data Lake: S3 buckets (raw, processed) with lifecycle policies
- Catalog: Glue Data Catalog for schema, partitions
- Warehouse: Athena or Redshift Serverless
- Orchestration: Step Functions or EventBridge Scheduler
- Monitoring: CloudWatch metrics, logs, X-Ray tracing

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

**Generates**: Terraform for S3 buckets, Lambda functions, Kinesis streams, SQS queues, Glue catalog/crawlers, Step Functions, IAM roles, CloudWatch

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| `/iac.principles` | `principles.md` | Project governance |
| `/iac.specify` | `spec.md`, `checklists/requirements.md` | Requirements |
| `/iac.clarify` (optional) | Updates `spec.md` | Resolves ambiguities |
| `/iac.plan` | `plan.md` | AWS-specific architecture with inline research |
| `/iac.enrichplan` (recommended) | `research.md`, `architecture.md`, `modules.md`, `quickstart.md` | Deep research and detailed specs |
| `/iac.tasks` | `tasks.md` | Implementation tasks |
| `/iac.implement` | `*.tf` files | Terraform code |
