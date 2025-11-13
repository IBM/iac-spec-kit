# AWS Workflow for Data Processing Pipeline

This guide shows the commands to deploy a data pipeline on AWS using IaC Spec Kit.

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a scalable data pipeline on AWS. Serverless-first, event-driven, cost-effective. Use Terraform.
/iac.specify I need a data pipeline to process application events and logs. Ingest from multiple sources, queue for buffering, serverless processing for transformation, store raw and processed data in data lake, load processed data into data warehouse for analytics. Expected: 1M events/day growing to 10M. Need data partitioned by date. Must track data lineage and quality. Budget: under $1000/month.
```

**Generates**: `spec.md` with requirements for event ingestion, message queuing, serverless compute, data lake, data warehouse, orchestration, monitoring

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use S3 for data lake, Lambda for processing, Kinesis Data Streams for ingestion, Glue for ETL and catalog, Athena for queries, Step Functions for orchestration.
```

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

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for S3 buckets, Lambda functions, Kinesis streams, SQS queues, Glue catalog/crawlers, Step Functions, IAM roles, CloudWatch

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | AWS data pipeline infrastructure |
