# Quick Start Guide

This guide will help you get started with IaC Spec Kit.

> NEW: All automation scripts now provide both Bash (`.sh`) and PowerShell (`.ps1`) variants. The `iac-specify` CLI auto-selects based on OS unless you pass `--script sh|ps`.

## Cloud-Agnostic Framework

**IaC Spec Kit is cloud-agnostic.** You write infrastructure requirements without specifying a cloud provider, then choose your preferred cloud (AWS, Azure, GCP, IBM Cloud) during the planning phase. The same specification can generate infrastructure for different cloud providers.

This guide provides complete workflow examples for common cloud providers. Choose the cloud provider that matches your needs and follow the complete workflow from requirements to implementation.

## The 4-Step Process

### 1. Install Specify

Initialize your project depending on the coding agent you're using:

```bash
uvx --from git+https://github.com/ibm/iac-spec-kit.git iac-specify init <PROJECT_NAME>
```

Pick script type explicitly (optional):

```bash
uvx --from git+https://github.com/ibm/iac-spec-kit.git iac-specify init <PROJECT_NAME> --script ps  # Force PowerShell
uvx --from git+https://github.com/ibm/iac-spec-kit.git iac-specify init <PROJECT_NAME> --script sh  # Force POSIX shell
```

### 2. Create the Spec

Use the `/iac.specify` command to describe what infrastructure you want to build. Focus on the **what** and **why**, not the specific cloud provider or tools.

**Application-focused example:**
```bash
/iac.specify Deploy the IBM AI Agent for Loan Risk application (https://github.com/IBM/ai-agent-for-loan-risk) on IBM Cloud. The app needs to be production-ready with high availability, secure, and cost-effective.
```

**Infrastructure-focused example:**
```bash
/iac.specify Create a 3-tier web application infrastructure with load balancing, auto-scaling, managed database with automatic backups, and CDN for static assets. Must support 10,000 concurrent users with 99.9% uptime SLA.
```

### 3. Create a Technical Implementation Plan

Use the `/iac.plan` command to specify your cloud provider and technical preferences.

**For IBM Cloud:**
```bash
/iac.plan Use IBM Cloud with VPC infrastructure. Deploy the application using IBM Cloud Code Engine for containerized workloads. Use IBM Cloud Object Storage for file storage and IBM Cloudant for the database. Include IBM Cloud Monitoring and logging.
```

**For multi-cloud or comparative analysis:**
```bash
/iac.plan Compare implementation approaches for AWS, Azure, and GCP. Recommend the best option based on cost, ease of deployment, and managed service availability.
```

### 4. Break Down and Implement

Use `/iac.tasks` to create an actionable task list with proper dependencies, then ask your agent to implement.

```bash
/iac.tasks

# After reviewing the tasks:
implement .specify/specs/001-feature-name/plan.md
```

## Complete Workflow Examples by Cloud Provider

Choose your cloud provider and follow the complete workflow from requirements to implementation.

---

### IBM Cloud: Deploy AI Agent Application

Complete workflow for deploying the IBM AI Agent for Loan Risk application with production-ready infrastructure.

**Step 1: Establish Project Principles**

```text
/iac.principles Create infrastructure principles focused on:
- Security: TLS 1.3, encryption at rest (AES-256), least-privilege IAM
- Cost governance: Monthly budget alerts, approved instance types
- Operational excellence: Automated backups, monitoring, disaster recovery
- Compliance: Data residency in approved regions, audit logging
```

**Step 2: Define Requirements (Cloud-Agnostic)**

```text
/iac.specify Deploy the IBM AI Agent for Loan Risk application from https://github.com/IBM/ai-agent-for-loan-risk

Requirements:
- Python-based AI application with web interface
- HTTPS-accessible web interface and API endpoints
- Document database for loan applications and risk scores
- Object storage for uploaded loan documents
- Application monitoring and centralized logging
- High availability with automatic failover
- Auto-scaling based on traffic demand
- Suitable for startup workload (budget: $500/month)

Non-functional requirements:
- 99.9% uptime SLA
- Support 1,000 concurrent users initially
- Response time < 500ms for API calls
- Automated daily backups with 30-day retention
```

**Step 3: Optional Clarification**

```text
/iac.clarify
```

The AI will ask targeted questions about deployment specifics, scaling requirements, and security preferences.

**Step 4: Create Technical Plan (Cloud-Specific)**

```text
/iac.plan Use IBM Cloud with the following architecture:

Compute:
- IBM Cloud Code Engine for containerized application (auto-scaling 1-10 instances)
- Container registry for application images

Data:
- IBM Cloudant (managed CouchDB) for document database
- IBM Cloud Object Storage (Standard tier) for document storage

Networking:
- IBM Cloud VPC for network isolation
- Public gateway for internet access
- Security groups for application and database tiers

Operations:
- IBM Cloud Monitoring for metrics and alerting
- IBM Cloud Log Analysis for centralized logging
- IBM Cloud Secrets Manager for API keys and credentials

Terraform:
- Remote state in IBM Cloud Object Storage
- Terraform 1.5+ with IBM Cloud provider
- Modular structure: networking, compute, data, security
```

**Step 5: Generate Task Breakdown**

```text
/iac.tasks
```

Generates dependency-ordered tasks:
1. Foundation: VPC, subnets, security groups
2. Data layer: Object Storage bucket, Cloudant instance
3. Compute: Code Engine project, container registry
4. Application: Deploy container, configure environment variables
5. Operations: Set up monitoring, logging, alerts
6. Validation: `terraform validate`, `terraform fmt`, `tflint`

**Step 6: Optional Consistency Analysis**

```text
/iac.analyze
```

Validates alignment between spec, plan, and tasks before implementation.

**Step 7: Execute Implementation**

```text
implement .specify/specs/001-deploy-loan-risk-app/plan.md
```

AI generates Terraform modules and validates configurations. Review and apply:

```bash
cd .specify/specs/001-deploy-loan-risk-app/terraform
terraform init
terraform plan
terraform apply
```

---

### AWS: 3-Tier Web Application

Complete workflow for production-grade 3-tier architecture on AWS.

**Step 1: Establish Project Principles**

```text
/iac.principles Create infrastructure principles for enterprise web applications:
- Security: WAF rules, encrypted databases, private subnets for app/data tiers
- High availability: Multi-AZ deployment, auto-scaling, automated failover
- Cost optimization: Reserved instances for baseline, spot instances for bursting
- Disaster recovery: RPO 1 hour, RTO 4 hours, cross-region backups
```

**Step 2: Define Requirements (Cloud-Agnostic)**

```text
/iac.specify Create a 3-tier web application infrastructure:

Architecture:
- Load-balanced web tier with SSL/TLS termination
- Application tier with auto-scaling capabilities
- Database tier with managed relational database
- Caching layer for improved performance
- CDN for static assets

Requirements:
- Support 10,000 concurrent users with ability to scale to 50,000
- 99.99% uptime SLA
- Automated database backups with point-in-time recovery
- Multi-availability-zone deployment for fault tolerance
- Zero-downtime deployments
- Comprehensive monitoring and alerting

Security:
- Web tier in public subnets, app and database in private subnets
- Database not accessible from internet
- Bastion host for administrative access
- WAF protection for web tier
- All data encrypted at rest and in transit
```

**Step 3: Optional Clarification**

```text
/iac.clarify
```

**Step 4: Create Technical Plan (AWS-Specific)**

```text
/iac.plan Use AWS with the following architecture:

Network:
- VPC spanning 3 availability zones
- Public subnets (10.0.1.0/24, 10.0.2.0/24, 10.0.3.0/24) for load balancers
- Private app subnets (10.0.11.0/24, 10.0.12.0/24, 10.0.13.0/24)
- Private database subnets (10.0.21.0/24, 10.0.22.0/24, 10.0.23.0/24)
- NAT gateways in each AZ for outbound internet access

Compute:
- Application Load Balancer with HTTPS listeners
- ECS Fargate for containerized application tier (auto-scaling 3-15 tasks)
- Bastion host in public subnet with security group restrictions

Data:
- RDS PostgreSQL Multi-AZ with automated backups
- ElastiCache Redis cluster for session/cache management
- S3 bucket for static assets with versioning enabled

CDN & DNS:
- CloudFront distribution for S3 static assets
- Route 53 for DNS management and health checks

Security:
- WAF with OWASP rules on ALB
- Security groups for each tier with least-privilege access
- Secrets Manager for database credentials and API keys
- KMS for encryption keys

Monitoring:
- CloudWatch for metrics, logs, and alarms
- CloudWatch Application Insights for application monitoring

Terraform:
- S3 backend with DynamoDB locking
- Terraform 1.5+ with AWS provider
- Module structure: networking, compute, data, security, monitoring
```

**Step 5: Generate Task Breakdown**

```text
/iac.tasks
```

**Step 6: Optional Consistency Analysis**

```text
/iac.analyze
```

**Step 7: Execute Implementation**

```text
implement .specify/specs/002-aws-web-app/plan.md
```

---

### Azure: Kubernetes Microservices Platform

Complete workflow for AKS cluster with supporting infrastructure.

**Step 1: Establish Project Principles**

```text
/iac.principles Create principles for cloud-native microservices:
- Security: Azure AD integration, network policies, container scanning
- Scalability: Horizontal pod autoscaling, cluster autoscaling
- Observability: Centralized logging, distributed tracing, metrics collection
- Cost efficiency: Right-sized node pools, automatic scale-down during off-hours
```

**Step 2: Define Requirements (Cloud-Agnostic)**

```text
/iac.specify Create a Kubernetes cluster infrastructure for microservices:

Cluster Requirements:
- Kubernetes cluster with 3-5 worker nodes (auto-scaling)
- Support for 20 containerized microservices
- Private container registry for application images
- Ingress controller with SSL/TLS termination
- Network policies for microservice isolation

Data Requirements:
- Managed PostgreSQL database (shared by multiple services)
- Redis cache for session state and caching
- Object storage for file uploads and backups

Operations:
- Centralized logging for all microservices
- Metrics collection and visualization
- Distributed tracing for request flows
- Automated certificate management
- GitOps-based deployments

Environments:
- Development, staging, and production namespaces
- Environment-specific configurations and secrets
```

**Step 3: Optional Clarification**

```text
/iac.clarify
```

**Step 4: Create Technical Plan (Azure-Specific)**

```text
/iac.plan Deploy on Azure in East US region:

Kubernetes:
- AKS cluster with Azure CNI networking
- System node pool (2 nodes, Standard_D2s_v3)
- User node pool (3-5 nodes, Standard_D4s_v3, auto-scaling)
- Azure AD integration for RBAC
- Kubernetes version 1.28+

Container Management:
- Azure Container Registry (Premium tier, geo-replication)
- Automated vulnerability scanning
- Image retention policies

Data Services:
- Azure Database for PostgreSQL Flexible Server (zone-redundant, 2 vCores)
- Azure Cache for Redis (Premium tier, 1GB)
- Azure Storage Account (Standard tier) for backups

Networking:
- Virtual Network with subnets for AKS, data services
- Azure Application Gateway v2 with WAF for ingress
- Private endpoints for data services
- Azure Firewall for egress traffic

Security:
- Azure Key Vault for secrets and certificates
- Managed identities for AKS to access Azure resources
- Network security groups for subnet isolation

Observability:
- Azure Monitor Container Insights
- Log Analytics workspace
- Application Insights for distributed tracing

Terraform:
- Azure Storage backend for state
- Terraform 1.5+ with AzureRM provider
- Modules: networking, aks, data, security, monitoring
```

**Step 5: Generate Task Breakdown**

```text
/iac.tasks
```

**Step 6: Optional Consistency Analysis**

```text
/iac.analyze
```

**Step 7: Execute Implementation**

```text
implement .specify/specs/003-azure-aks-platform/plan.md
```

---

### GCP: Cloud Run Serverless Platform

Complete workflow for serverless microservices on Google Cloud.

**Step 1: Establish Project Principles**

```text
/iac.principles Create principles for serverless architecture:
- Cost efficiency: Pay only for actual usage, automatic scale-to-zero
- Developer experience: Minimal infrastructure management, fast deployments
- Security: Service accounts with minimal permissions, VPC service controls
- Observability: Structured logging, error reporting, trace collection
```

**Step 2: Define Requirements (Cloud-Agnostic)**

```text
/iac.specify Create a serverless platform for REST API microservices:

Application Requirements:
- 5-10 containerized microservices (HTTP-based APIs)
- Automatic scaling from 0 to 1000 concurrent requests
- API gateway for unified endpoint and authentication
- Service-to-service authentication

Data Requirements:
- Managed SQL database for transactional data
- NoSQL database for user sessions and real-time data
- Object storage for file uploads and exports
- In-memory cache for frequently accessed data

Operations:
- CI/CD pipeline from GitHub
- Automated container builds on git push
- Blue-green deployments with traffic splitting
- Centralized logging and error tracking
- API monitoring and alerting

Security:
- Service-to-service authentication using cloud-native mechanisms
- API authentication using OAuth 2.0 / JWT
- Secrets management for database credentials and API keys
- DDoS protection and rate limiting
```

**Step 3: Optional Clarification**

```text
/iac.clarify
```

**Step 4: Create Technical Plan (GCP-Specific)**

```text
/iac.plan Use Google Cloud Platform:

Compute:
- Cloud Run services for each microservice (auto-scaling, min 0, max 100 instances)
- Cloud Build for automated container builds from GitHub
- Artifact Registry for container images

API Gateway:
- API Gateway for unified endpoint
- Cloud Endpoints for API management and authentication

Data Services:
- Cloud SQL for PostgreSQL (db-f1-micro, automated backups)
- Cloud Firestore for NoSQL data
- Cloud Storage bucket (Standard storage class) for files
- Cloud Memorystore for Redis (1GB Basic tier)

Networking:
- Serverless VPC Connector for Cloud Run to VPC resources
- Private IP for Cloud SQL
- Cloud NAT for outbound internet access from Cloud Run

Security:
- Service accounts with minimal IAM roles per service
- Secret Manager for database credentials and API keys
- Cloud Armor for DDoS protection

CI/CD:
- Cloud Build triggers on GitHub commits
- Container Registry for images
- Cloud Deploy for deployment management

Observability:
- Cloud Logging for centralized logs
- Cloud Monitoring for metrics and dashboards
- Error Reporting for exception tracking
- Cloud Trace for distributed tracing

Terraform:
- Cloud Storage backend for state
- Terraform 1.5+ with Google provider
- Modules: networking, compute, data, security, cicd
```

**Step 5: Generate Task Breakdown**

```text
/iac.tasks
```

**Step 6: Optional Consistency Analysis**

```text
/iac.analyze
```

**Step 7: Execute Implementation**

```text
implement .specify/specs/004-gcp-serverless/plan.md
```

## Key Principles

- **Be explicit** about your infrastructure requirements, SLOs, and constraints
- **Don't focus on cloud provider** during specification phase (unless you have a specific requirement)
- **Iterate and refine** your specifications before implementation using `/iac.clarify`
- **Validate** the plan before infrastructure provisioning using `/iac.analyze`
- **Let the AI agent handle** the Terraform code generation and cloud architecture decisions
- **Use principles** (`/iac.principles`) to encode organizational infrastructure principles
- **Validate infrastructure** with `terraform validate`, `terraform fmt`, and `tflint` before applying

## Workflow Summary

```
1. /iac.principles  → Define organizational principles (one-time setup)
2. /iac.specify       → Create infrastructure specification (technology-agnostic)
3. /iac.clarify       → Optional: Clarify underspecified areas
4. /iac.plan          → Generate architecture plan with cloud provider choice
5. /iac.tasks         → Break down into dependency-ordered tasks
6. /iac.analyze       → Optional: Validate consistency across artifacts
7. implement          → Execute tasks and generate Terraform code
8. terraform apply    → Provision infrastructure
```

## Next Steps

- Review the [Installation Guide](installation.md) for setup instructions
- Check the main [README](https://github.com/ibm/iac-spec-kit) for comprehensive documentation
- Read about infrastructure principles in the project documentation
- Explore the [iac-spec-driven.md](https://github.com/ibm/iac-spec-kit/blob/main/iac-spec-driven.md) methodology guide
