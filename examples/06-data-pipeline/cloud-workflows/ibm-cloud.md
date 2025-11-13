# IBM Cloud Workflow for Data Processing Pipeline

## Commands

### Steps 1-2: Principles and Specify

```
/iac.principles I'm building a scalable data pipeline on IBM Cloud. Serverless-first, event-driven, cost-effective. Use Terraform.
/iac.specify I need a data pipeline to process application events and logs. Ingest from multiple sources, queue for buffering, serverless processing, store raw and processed data in data lake, load into data warehouse for analytics. Expected: 1M events/day growing to 10M. Need data partitioned by date. Budget: under $1000/month.
```

---

### Steps 3-4: Clarify and Plan

```
/iac.clarify
/iac.plan Use Cloud Object Storage for data lake, Cloud Functions for processing, Event Streams (Kafka), Data Engine (Presto), Db2 Warehouse.
```

**plan.md** example: Event Streams for messaging, Cloud Functions for processing, COS buckets with lifecycle, Data Engine for SQL queries on data lake, Db2 Warehouse for analytics, monitoring with Activity Tracker and Log Analysis

---

### Steps 5-6: Tasks and Implementation

```
/iac.tasks
/iac.implement
```

**Generates**: Terraform for COS buckets, Event Streams, Cloud Functions, Data Engine, Db2 Warehouse, monitoring

---

## Files Generated Summary

| Command | Files | Purpose |
|---------|-------|---------|
| All commands | Standard set | IBM Cloud data pipeline infrastructure |
