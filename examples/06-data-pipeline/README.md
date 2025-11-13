# Example: Data Processing Pipeline

**Complexity**: High
**Estimated Time**: 2-3 hours
**Best For**: Data engineering teams, analytics teams, data-driven organizations

## Overview

This example demonstrates a serverless data processing pipeline that ingests, transforms, and stores data at scale. This pattern is used for ETL (Extract, Transform, Load) workflows, real-time analytics, data lakes, and machine learning data preparation.

## What You'll Build

A complete data pipeline infrastructure:

- **Data Ingestion**: Event-driven ingestion from multiple sources
- **Message Queue**: Decouples ingestion from processing, provides buffering
- **Serverless Processing**: Auto-scaling compute for data transformation
- **Data Lake**: Raw and processed data storage with partitioning
- **Data Warehouse**: Structured data for analytics and reporting
- **Orchestration**: Workflow management for batch processing
- **Monitoring**: Pipeline health, data quality metrics, cost tracking
- **Multi-Region**: Data replication for disaster recovery

## Use Case

**Scenario**: Your organization collects data from multiple sources (application logs, user events, IoT sensors, third-party APIs) and needs to process it for analytics, reporting, and machine learning. Data must be transformed, validated, enriched, and loaded into both a data lake (for data scientists) and data warehouse (for business analysts).

## Learning Objectives

This example teaches you:

1. **Event-driven architecture**: Describing asynchronous, scalable data flows
2. **Serverless compute**: Specifying event-triggered processing without managing servers
3. **Storage patterns**: Data lake vs data warehouse requirements
4. **Orchestration needs**: Workflow dependencies, scheduling, error handling
5. **Data governance**: Expressing data quality, lineage, and compliance requirements

## Prerequisites

- Cloud account (AWS, Azure, GCP, or IBM Cloud)
- Cloud CLI installed and configured
- IaC Spec Kit installed (`iac-specify check`)
- Terraform installed
- AI coding assistant running
- Understanding of data pipeline concepts

## Get Started

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS Workflow](./cloud-workflows/aws.md)** - S3, Lambda, Kinesis, Glue, Athena, Step Functions
- **[Azure Workflow](./cloud-workflows/azure.md)** - Blob Storage, Functions, Event Hub, Data Factory, Synapse
- **[GCP Workflow](./cloud-workflows/gcp.md)** - Cloud Storage, Cloud Functions, Pub/Sub, Dataflow, BigQuery
- **[IBM Cloud Workflow](./cloud-workflows/ibm-cloud.md)** - COS, Functions, Event Streams, Data Engine, Db2 Warehouse

## Pipeline Architecture

```
Sources → Ingestion → Queue → Transform → Storage
                                  ↓
                            Orchestration
                                  ↓
                        Data Warehouse ← Analytics
```

**Data flow**: Sources push events → Queue buffers messages → Serverless functions process batches → Write to data lake (raw + processed) → Periodic batch jobs load warehouse → BI tools query warehouse

## What Makes This Example Complex

- **Multiple components**: Ingestion, queuing, processing, storage, orchestration
- **Event-driven patterns**: Asynchronous messaging, backpressure handling
- **Data partitioning**: Organizing data by date/type for efficient queries
- **Schema evolution**: Handling changing data formats over time
- **Error handling**: Dead letter queues, retry logic, alerting
- **Multi-region**: Data replication across regions

## Common Use Cases

This pattern works for:

- Application log processing and analytics
- User behavioral analytics and personalization
- IoT sensor data collection and analysis
- Real-time fraud detection
- Machine learning feature engineering
- Business intelligence and reporting

## Next Steps

After completing this example:

1. Add **machine learning models** that consume pipeline data
2. Implement **streaming analytics** for real-time insights
3. Deploy **[07-microservices](../07-microservices/)** that publish events to this pipeline
