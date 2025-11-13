# Example: Microservices Platform

**Complexity**: High
**Estimated Time**: 3-4 hours
**Best For**: Cloud-native applications, DevOps teams, distributed systems engineers

## Overview

This example demonstrates a complete microservices platform with container orchestration, service mesh, API gateway, and comprehensive observability. This architecture enables teams to build, deploy, and operate distributed applications with independent service lifecycles, polyglot programming, and resilient communication patterns.

## What You'll Build

A production-grade microservices platform:

- **Container Orchestration**: Kubernetes or managed container service
- **Service Mesh**: Service-to-service communication, traffic management, security
- **API Gateway**: External traffic routing, authentication, rate limiting
- **Service Discovery**: Dynamic service registration and discovery
- **Distributed Tracing**: Request tracing across services
- **Centralized Logging**: Aggregated logs from all services
- **Metrics and Monitoring**: Service health, SLIs, SLOs
- **CI/CD Integration**: Automated deployment pipelines
- **Database per Service**: Independent data stores
- **Message Queue**: Asynchronous inter-service communication

## Use Case

**Scenario**: Your organization is building a modern application with multiple teams working on different features (user management, payments, notifications, inventory, etc.). Each team needs to deploy independently, use their preferred tech stack, scale their service independently, and maintain high availability without affecting other services.

## Learning Objectives

This example teaches you:

1. **Distributed systems patterns**: How to describe service mesh, circuit breakers, retry logic
2. **Container orchestration**: Specifying cluster requirements without naming Kubernetes/ECS/etc directly
3. **Observability**: Expressing comprehensive monitoring, logging, and tracing needs
4. **API gateway patterns**: External vs internal traffic management
5. **Polyglot persistence**: Multiple database types for different services
6. **Resilience requirements**: Fault isolation, graceful degradation, chaos engineering

## Prerequisites

- Cloud account (AWS, Azure, GCP, or IBM Cloud)
- IaC Spec Kit installed (`iac-specify check`)
- Terraform installed
- AI coding assistant running
- Container registry access
- Understanding of microservices patterns

## Get Started

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS Workflow](./cloud-workflows/aws.md)** - EKS, App Mesh, API Gateway, CloudWatch, X-Ray
- **[Azure Workflow](./cloud-workflows/azure.md)** - AKS, Service Mesh, API Management, Monitor, App Insights
- **[GCP Workflow](./cloud-workflows/gcp.md)** - GKE, Anthos Service Mesh, Apigee, Operations Suite
- **[IBM Cloud Workflow](./cloud-workflows/ibm-cloud.md)** - IKS, Istio, API Connect, Monitoring, Log Analysis

## Platform Architecture

```
Internet → API Gateway → Service Mesh → Microservices
                              ↓              ↓
                        Service Discovery   Databases
                              ↓              ↓
                        Observability    Message Queue
```

**Traffic flow**: External requests → API Gateway (auth, rate limit) → Service Mesh (routing, security) → Individual microservices → Internal calls via service mesh → Data stores and message queues → All telemetry to observability platform

## What Makes This Example Complex

- **Many components**: Orchestration, mesh, gateway, databases, messaging, monitoring
- **Inter-service dependencies**: Services call each other, requiring service discovery and resilience
- **Multiple databases**: Different services use different data stores (SQL, NoSQL, cache)
- **Comprehensive observability**: Metrics, logs, traces from all services correlated
- **Network complexity**: Ingress, egress, service-to-service, external dependencies
- **Security layers**: Network policies, mutual TLS, RBAC, secrets management

## Microservices Patterns Demonstrated

- **API Gateway**: Single entry point for external traffic
- **Service Mesh**: Service-to-service communication with mutual TLS
- **Circuit Breaker**: Prevent cascading failures
- **Database per Service**: Independent data stores
- **Event-Driven**: Asynchronous communication via message queue
- **Centralized Configuration**: Config management for all services
- **Health Checks**: Liveness and readiness probes
- **Distributed Tracing**: Request correlation across services

## Next Steps

After completing this example:

1. Implement **GitOps** for declarative deployments
2. Add **service versioning** and canary deployments
3. Integrate **[06-data-pipeline](../06-data-pipeline/)** for event streaming from microservices
4. Set up **chaos engineering** to test resilience
