# Example: Static Website

**Complexity**: Low
**Estimated Time**: 20-30 minutes
**Best For**: Marketing teams, content creators, simple web projects

## Overview

This example shows how to deploy a static website using cloud object storage and a content delivery network (CDN). Perfect for marketing sites, documentation, portfolios, or any content that doesn't require server-side processing.

## What You'll Build

A complete static website hosting solution including:

- Object storage bucket for website files (HTML, CSS, JavaScript, images)
- Static website hosting configuration
- Content Delivery Network (CDN) for global performance
- Custom domain name support
- SSL/TLS certificate for HTTPS
- Basic security configurations

## Use Case

**Scenario**: Your marketing team needs to launch a product landing page. It's pure HTML/CSS/JavaScript with no backend requirements. You want it to load quickly worldwide, support a custom domain (www.example.com), and use HTTPS for security.

## Learning Objectives

This example teaches you:

1. **Object storage for web hosting**: How to describe storage requirements in cloud-agnostic terms
2. **Content delivery and performance**: Specifying global distribution without naming specific CDN services
3. **Domain and SSL requirements**: Expressing custom domain needs generically
4. **Non-technical friendly workflow**: Shows how marketing teams can describe "I need a website" and get proper infrastructure

## Prerequisites

- Cloud account (choose one: AWS, Azure, GCP, or IBM Cloud)
- IaC Spec Kit installed (`iac-specify check`)
- Terraform installed
- AI coding assistant running in your project directory
- (Optional) Domain name for custom domain configuration

## Get Started

Choose your cloud provider and follow the corresponding workflow guide:

- **[AWS Workflow](./cloud-workflows/aws.md)** - S3, CloudFront, Route 53, ACM
- **[Azure Workflow](./cloud-workflows/azure.md)** - Blob Storage, Azure CDN, DNS, App Service Certificate
- **[GCP Workflow](./cloud-workflows/gcp.md)** - Cloud Storage, Cloud CDN, Cloud DNS, SSL Certificates
- **[IBM Cloud Workflow](./cloud-workflows/ibm-cloud.md)** - Cloud Object Storage, CDN, DNS Services

## What Makes This Example Simple

- **No compute resources**: Just storage and CDN, no servers to manage
- **Static content only**: No application logic, databases, or dynamic content
- **Low operational overhead**: Highly managed services handle everything
- **Cost-effective**: Often falls within free tiers or costs just a few dollars per month

## Example Use Cases

This pattern works for:

- Marketing landing pages
- Product documentation sites
- Company blogs (using static site generators like Hugo, Jekyll, Gatsby)
- Portfolio websites
- Event microsites
- API documentation

## Next Steps

After completing this example:

1. Try **[03-wordpress](../03-wordpress/)** to add dynamic content and databases
2. Explore **[05-three-tier-webapp](../05-three-tier-webapp/)** for full web applications
3. Learn **[06-data-pipeline](../06-data-pipeline/)** for data-driven sites
