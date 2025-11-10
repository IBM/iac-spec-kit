# [PROJECT NAME] Development Guidelines

Auto-generated from all feature plans. Last updated: [DATE]

## Active Technologies

[EXTRACTED FROM ALL PLAN.MD FILES]

## Project Structure

```text
[ACTUAL STRUCTURE FROM PLANS]

# FOR INFRASTRUCTURE PROJECTS:
# Place Terraform files (.tf) in iac/ directory at repository root:
#   iac/*.tf - Main infrastructure definitions
#   iac/terraform.tfvars.* - Environment-specific variables
#   iac/modules/ - Optional reusable modules
```

## Commands

[ONLY COMMANDS FOR ACTIVE TECHNOLOGIES]

# Terraform commands:
# - terraform init: Initialize backend and download providers
# - terraform validate: Check syntax and configuration validity
# - terraform fmt: Format code to canonical style
# - terraform plan -var-file=terraform.tfvars.dev: Preview changes for dev environment
# - terraform apply -var-file=terraform.tfvars.dev: Apply changes to dev environment
# - tflint: Lint Terraform code for best practices and errors

## Code Style

[LANGUAGE-SPECIFIC, ONLY FOR LANGUAGES IN USE]

## Recent Changes

[LAST 3 FEATURES AND WHAT THEY ADDED]

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
