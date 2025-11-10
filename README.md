<div align="center">
    <img src="./media/logo_small.webp" alt="Spec Kit Logo"/>
    <h1>🌱 IAC Spec Kit</h1>
    <h3><em>Build high-quality infrastructure faster with Terraform and cloud resources.</em></h3>
</div>

> **Note**: This is a domain-specific implementation of the [spec-kit pattern](https://github.com/github/spec-kit) optimized for Infrastructure as Code workflows. While the original spec kit focuses on software development, IAC Spec Kit provides infrastructure-specific templates, constitutional principles, cloud resource specifications, and Terraform patterns.

## What makes IAC Spec Kit different

This is not a fork but rather a specialized implementation of the spec-driven development pattern for infrastructure:

- **Infrastructure-focused commands**: All slash commands use `.iac` namespace (`/speckit.iac.specify`, `/speckit.iac.plan`, `/speckit.iac.tasks`, etc.)
- **Terraform-centric templates**: Documentation and templates use Terraform modules, cloud resources, and infrastructure scenarios
- **Cloud provider coverage**: Examples span AWS, Azure, GCP, and IBM Cloud
- **Infrastructure constitutional principles**: Governance frameworks specific to cloud infrastructure, security, compliance, and cost management
- **Cloud resource specifications**: Templates designed for networking, compute, storage, and security infrastructure

---

<p align="center">
    <strong>An open source toolkit that allows you to focus on infrastructure scenarios and predictable cloud deployments instead of manually crafting every Terraform module from scratch.</strong>
</p>

<p align="center">
    <a href="https://github.com/github/spec-kit/actions/workflows/release.yml"><img src="https://github.com/github/spec-kit/actions/workflows/release.yml/badge.svg" alt="Release"/></a>
    <a href="https://github.com/github/spec-kit/stargazers"><img src="https://img.shields.io/github/stars/github/spec-kit?style=social" alt="GitHub stars"/></a>
    <a href="https://github.com/github/spec-kit/blob/main/LICENSE"><img src="https://img.shields.io/github/license/github/spec-kit" alt="License"/></a>
    <a href="https://github.github.io/spec-kit/"><img src="https://img.shields.io/badge/docs-GitHub_Pages-blue" alt="Documentation"/></a>
</p>

---

## Table of Contents

- [🤔 What is Spec-Driven Development?](#-what-is-spec-driven-development)
- [⚡ Get Started](#-get-started)
- [📽️ Video Overview](#️-video-overview)
- [🤖 Supported AI Agents](#-supported-ai-agents)
- [🔧 Specify CLI Reference](#-specify-cli-reference)
  - [Contributing to Spec Kit Templates](#contributing-to-spec-kit-templates)
  - [Infrastructure-as-Code Projects](#infrastructure-as-code-projects)
- [📚 Core Philosophy](#-core-philosophy)
- [🌟 Development Phases](#-development-phases)
- [🎯 Experimental Goals](#-experimental-goals)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Learn More](#-learn-more)
- [📋 Detailed Process](#-detailed-process)
- [🔍 Troubleshooting](#-troubleshooting)
- [👥 Maintainers](#-maintainers)
- [💬 Support](#-support)
- [🙏 Acknowledgements](#-acknowledgements)
- [📄 License](#-license)

## 🤔 What is Spec-Driven Development?

Spec-Driven Development **flips the script** on traditional infrastructure provisioning. For decades, infrastructure code has been written directly — specifications were just documentation we created after the fact. Spec-Driven Development changes this: **specifications become executable**, directly generating working Terraform configurations rather than just guiding them.

**Specialized for Infrastructure as Code**: Use a structured workflow for Terraform infrastructure projects. Document cloud resources, networking, and security in specifications, then let AI agents generate production-ready infrastructure code.

## ⚡ Get Started

### 1. Install Specify CLI

Choose your preferred installation method:

#### Option 1: Persistent Installation (Recommended)

Install once and use everywhere:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

Then use the tool directly:

```bash
specify init <PROJECT_NAME>
specify check
```

To upgrade specify run:

```bash
uv tool install specify-cli --force --from git+https://github.com/github/spec-kit.git
```

#### Option 2: One-time Usage

Run directly without installing:

```bash
uvx --from git+https://github.com/github/spec-kit.git specify init <PROJECT_NAME>
```

**Benefits of persistent installation:**

- Tool stays installed and available in PATH
- No need to create shell aliases
- Better tool management with `uv tool list`, `uv tool upgrade`, `uv tool uninstall`
- Cleaner shell configuration

### 2. Establish project principles

Launch your AI assistant in the project directory. The `/speckit.iac.*` commands are available in the assistant.

Use the **`/speckit.iac.constitution`** command to create your project's governing principles and development guidelines that will guide all subsequent development.

```bash
/speckit.iac.constitution Create principles focused on infrastructure security, compliance standards, cost governance, and operational excellence requirements
```

### 3. Create the spec

Use the **`/speckit.iac.specify`** command to describe what you want to build. Focus on the **what** and **why**, not the tech stack.

```bash
/speckit.iac.specify Provision a multi-region AWS VPC infrastructure with public and private subnets across three availability zones. Include NAT gateways for private subnet internet access, VPC peering between regions for cross-region communication, and security groups configured for web tier, app tier, and database tier traffic isolation.
```

### 4. Create a technical implementation plan

Use the **`/speckit.iac.plan`** command to provide your tech stack and architecture choices.

```bash
/speckit.iac.plan Use Terraform 1.5+ with AWS provider. Store state in S3 with DynamoDB locking. Structure modules for networking (VPC, subnets, gateways), security (security groups, NACLs), and peering. Use Terraform workspaces for environment separation (dev, staging, prod). Output VPC IDs, subnet IDs, and security group IDs for downstream consumption.
```

### 5. Break down into tasks

Use **`/speckit.iac.tasks`** to create an actionable task list from your implementation plan.

```bash
/speckit.iac.tasks
```

### 6. Execute implementation

Use **`/speckit.implement`** to execute all tasks and build your feature according to the plan.

```bash
/speckit.implement
```

For detailed step-by-step instructions, see our [comprehensive guide](./spec-driven.md).

## 📽️ Video Overview

Want to see Spec Kit in action? Watch our [video overview](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)!

[![Spec Kit video header](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🤖 Supported AI Agents

| Agent                                                     | Support | Notes                                             |
|-----------------------------------------------------------|---------|---------------------------------------------------|
| [Claude Code](https://www.anthropic.com/claude-code)      | ✅ |                                                   |
| [GitHub Copilot](https://code.visualstudio.com/)          | ✅ |                                                   |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ✅ |                                                   |
| [Cursor](https://cursor.sh/)                              | ✅ |                                                   |
| [Qwen Code](https://github.com/QwenLM/qwen-code)          | ✅ |                                                   |
| [opencode](https://opencode.ai/)                          | ✅ |                                                   |
| [Windsurf](https://windsurf.com/)                         | ✅ |                                                   |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)         | ✅ |                                                   |
| [Auggie CLI](https://docs.augmentcode.com/cli/overview)   | ✅ |                                                   |
| [CodeBuddy CLI](https://www.codebuddy.ai/cli)             | ✅ |                                                   |
| [Roo Code](https://roocode.com/)                          | ✅ |                                                   |
| [Codex CLI](https://github.com/openai/codex)              | ✅ |                                                   |
| [Amazon Q Developer CLI](https://aws.amazon.com/developer/learning/q-developer-cli/) | ⚠️ | Amazon Q Developer CLI [does not support](https://github.com/aws/amazon-q-developer-cli/issues/3064) custom arguments for slash commands. |
| [Amp](https://ampcode.com/) | ✅ | |

## 🔧 Specify CLI Reference

The `specify` command supports the following options:

### Commands

| Command     | Description                                                    |
|-------------|----------------------------------------------------------------|
| `init`      | Initialize a new Specify project from the latest template      |
| `check`     | Check for installed tools (`git`, `claude`, `gemini`, `code`/`code-insiders`, `cursor-agent`, `windsurf`, `qwen`, `opencode`, `codex`) |

### `specify init` Arguments & Options

| Argument/Option        | Type     | Description                                                                  |
|------------------------|----------|------------------------------------------------------------------------------|
| `<project-name>`       | Argument | Name for your new project directory (optional if using `--here`, or use `.` for current directory) |
| `--ai`                 | Option   | AI assistant to use: `claude`, `gemini`, `copilot`, `cursor-agent`, `qwen`, `opencode`, `codex`, `windsurf`, `kilocode`, `auggie`, `roo`, `codebuddy`, `amp`, or `q` |
| `--script`             | Option   | Script variant to use: `sh` (bash/zsh) or `ps` (PowerShell)                 |
| `--ignore-agent-tools` | Flag     | Skip checks for AI agent tools like Claude Code                             |
| `--no-git`             | Flag     | Skip git repository initialization                                          |
| `--here`               | Flag     | Initialize project in the current directory instead of creating a new one   |
| `--force`              | Flag     | Force merge/overwrite when initializing in current directory (skip confirmation) |
| `--skip-tls`           | Flag     | Skip SSL/TLS verification (not recommended)                                 |
| `--debug`              | Flag     | Enable detailed debug output for troubleshooting                            |
| `--github-token`       | Option   | GitHub token for API requests (or set GH_TOKEN/GITHUB_TOKEN env variable)  |

### Examples

```bash
# Basic project initialization
specify init my-infrastructure

# Initialize with specific AI assistant
specify init my-infrastructure --ai claude

# Initialize with Cursor support
specify init my-infrastructure --ai cursor-agent

# Initialize with Windsurf support
specify init my-infrastructure --ai windsurf

# Initialize with Amp support
specify init my-infrastructure --ai amp

# Initialize with PowerShell scripts (Windows/cross-platform)
specify init my-infrastructure --ai copilot --script ps

# Initialize in current directory
specify init . --ai copilot
# or use the --here flag
specify init --here --ai copilot

# Force merge into current (non-empty) directory without confirmation
specify init . --force --ai copilot
# or
specify init --here --force --ai copilot

# Skip git initialization
specify init my-infrastructure --ai gemini --no-git

# Enable debug output for troubleshooting
specify init my-infrastructure --ai claude --debug

# Use GitHub token for API requests (helpful for corporate environments)
specify init my-infrastructure --ai claude --github-token ghp_your_token_here

# Check system requirements
specify check
```

### Available Slash Commands

After running `specify init`, your AI coding agent will have access to these slash commands for structured development:

#### Core Commands

Essential commands for the Spec-Driven Development workflow:

| Command                  | Description                                                           |
|--------------------------|-----------------------------------------------------------------------|
| `/speckit.iac.constitution`  | Create or update project governing principles and development guidelines |
| `/speckit.iac.specify`       | Define what you want to build (requirements and user stories)        |
| `/speckit.iac.plan`          | Create technical implementation plans with your chosen tech stack     |
| `/speckit.iac.tasks`         | Generate actionable task lists for implementation                     |
| `/speckit.implement`     | Execute all tasks to build the feature according to the plan         |

#### Optional Commands

Additional commands for enhanced quality and validation:

| Command              | Description                                                           |
|----------------------|-----------------------------------------------------------------------|
| `/speckit.iac.clarify`   | Clarify underspecified areas (recommended before `/speckit.iac.plan`; formerly `/quizme`) |
| `/speckit.iac.analyze`   | Cross-artifact consistency & coverage analysis (run after `/speckit.iac.tasks`, before `/speckit.iac.implement`) |
| `/speckit.iac.checklist` | Generate custom quality checklists that validate requirements completeness, clarity, and consistency (like "unit tests for English") |

### Infrastructure-as-Code Projects

IAC Spec Kit specializes in infrastructure projects using Terraform with the same structured workflow as application development.

#### Key Differences for Infrastructure Projects

| Aspect | Application Project | Infrastructure Project |
|--------|-------------------|----------------------|
| **Specification** | User stories for features | User stories for infrastructure needs (technology-agnostic) |
| **Planning** | Tech stack & architecture | Cloud provider selection + **Infrastructure Architecture section** |
| **Implementation** | AI generates application code | AI generates Terraform configuration files (.tf) |
| **Validation** | Run tests | Run `terraform validate`, `terraform fmt`, `tflint` |

#### Infrastructure Architecture Section

When using `/speckit.iac.plan` for infrastructure projects, your `plan.md` will include an **Infrastructure Architecture** section with:

- **Cloud Provider Selection**: Which provider and why (AWS, Azure, GCP, etc.)
- **Compute Resources**: VMs, containers, serverless, load balancers
- **Data Storage**: Databases, object storage, caching layers
- **Networking**: VPCs, subnets, security groups, routing
- **Security**: IAM roles, encryption, secrets management
- **Environment Configuration**: Development, staging, production settings
- **State Management**: Terraform backend configuration, workspace strategy

#### Quick Example

```bash
# 1. Create infrastructure specification (technology-agnostic)
/speckit.iac.specify Build production web app infrastructure with database, caching, and auto-scaling

# 2. Create technical plan (specify AWS, document Infrastructure Architecture)
/speckit.iac.plan We'll use AWS with ECS Fargate, RDS PostgreSQL, ElastiCache Redis, and Application Load Balancer

# 3. Generate tasks (includes terraform validation checkpoints)
/speckit.iac.tasks

# 4. Implement (AI generates Terraform .tf files)
/speckit.implement
```

**Important**: IAC Spec Kit generates and validates Terraform code. Actual provisioning (`terraform apply`) is a manual step you control.

### Environment Variables

| Variable         | Description                                                                                    |
|------------------|------------------------------------------------------------------------------------------------|
| `SPECIFY_FEATURE` | Override feature detection for non-Git repositories. Set to the feature directory name (e.g., `001-vpc-infrastructure`) to work on a specific feature when not using Git branches.<br/>**Must be set in the context of the agent you're working with prior to using `/speckit.iac.plan` or follow-up commands. |

## 📚 Core Philosophy

Spec-Driven Development is a structured process that emphasizes:

- **Intent-driven development** where specifications define the "*what*" before the "*how*"
- **Rich specification creation** using guardrails and organizational principles
- **Multi-step refinement** rather than one-shot code generation from prompts
- **Heavy reliance** on advanced AI model capabilities for specification interpretation

## 🌟 Development Phases

| Phase | Focus | Key Activities |
|-------|-------|----------------|
| **0-to-1 Development** ("Greenfield") | Generate from scratch | <ul><li>Start with high-level requirements</li><li>Generate specifications</li><li>Plan implementation steps</li><li>Build production-ready infrastructure</li></ul> |
| **Creative Exploration** | Parallel implementations | <ul><li>Explore diverse solutions</li><li>Support multiple cloud providers & architectures</li><li>Experiment with infrastructure patterns</li></ul> |
| **Iterative Enhancement** ("Brownfield") | Brownfield modernization | <ul><li>Add infrastructure iteratively</li><li>Modernize legacy infrastructure</li><li>Adapt processes</li></ul> |
| **Infrastructure-as-Code** | Infrastructure provisioning | <ul><li>Specify cloud resources technology-agnostically</li><li>Document Infrastructure Architecture</li><li>Generate Terraform configurations</li><li>Validate with terraform validate/fmt/tflint</li></ul> |

## 🎯 Experimental Goals

Our research and experimentation focus on:

### Technology independence

- Create infrastructure using diverse cloud providers
- Validate the hypothesis that Spec-Driven Development is a process not tied to specific cloud platforms, IaC tools, or frameworks
- Support multi-cloud and hybrid cloud scenarios

### Enterprise constraints

- Demonstrate mission-critical infrastructure development
- Incorporate organizational constraints (cloud providers, compliance requirements, engineering practices)
- Support enterprise security standards and compliance requirements

### Infrastructure-centric development

- Build infrastructure for different workload types and requirements
- Support various development approaches (from manual provisioning to fully automated IaC)

### Creative & iterative processes

- Validate the concept of parallel implementation exploration
- Provide robust iterative infrastructure development workflows
- Extend processes to handle upgrades and modernization tasks

## 🔧 Prerequisites

- **Linux/macOS/Windows**
- [Supported](#-supported-ai-agents) AI coding agent.
- [uv](https://docs.astral.sh/uv/) for package management
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

If you encounter issues with an agent, please open an issue so we can refine the integration.

## 📖 Learn More

- **[Complete Spec-Driven Development Methodology](./spec-driven.md)** - Deep dive into the full process
- **[Detailed Walkthrough](#-detailed-process)** - Step-by-step implementation guide

---

## 📋 Detailed Process

<details>
<summary>Click to expand the detailed step-by-step walkthrough</summary>

You can use the Specify CLI to bootstrap your project, which will bring in the required artifacts in your environment. Run:

```bash
specify init <project_name>
```

Or initialize in the current directory:

```bash
specify init .
# or use the --here flag
specify init --here
# Skip confirmation when the directory already has files
specify init . --force
# or
specify init --here --force
```

![Specify CLI bootstrapping a new project in the terminal](./media/specify_cli.gif)

You will be prompted to select the AI agent you are using. You can also proactively specify it directly in the terminal:

```bash
specify init <project_name> --ai claude
specify init <project_name> --ai gemini
specify init <project_name> --ai copilot

# Or in current directory:
specify init . --ai claude
specify init . --ai codex

# or use --here flag
specify init --here --ai claude
specify init --here --ai codex

# Force merge into a non-empty current directory
specify init . --force --ai claude

# or
specify init --here --force --ai claude
```

The CLI will check if you have Claude Code, Gemini CLI, Cursor CLI, Qwen CLI, opencode, Codex CLI, or Amazon Q Developer CLI installed. If you do not, or you prefer to get the templates without checking for the right tools, use `--ignore-agent-tools` with your command:

```bash
specify init <project_name> --ai claude --ignore-agent-tools
```

### **STEP 1:** Establish project principles

Go to the project folder and run your AI agent. In our example, we're using `claude`.

![Bootstrapping Claude Code environment](./media/bootstrap-claude-code.gif)

You will know that things are configured correctly if you see the `/speckit.iac.constitution`, `/speckit.iac.specify`, `/speckit.iac.plan`, `/speckit.iac.tasks`, and `/speckit.implement` commands available.

The first step should be establishing your project's governing principles using the `/speckit.iac.constitution` command. This helps ensure consistent decision-making throughout all subsequent development phases:

```text
/speckit.iac.constitution Create principles focused on infrastructure security, compliance standards, cost governance, and operational excellence. Include governance for how these principles should guide technical decisions and implementation choices.
```

This step creates or updates the `.specify/memory/constitution.md` file with your project's foundational guidelines that the AI agent will reference during specification, planning, and implementation phases.

### **STEP 2:** Create project specifications

With your project principles established, you can now create the functional specifications. Use the `/speckit.iac.specify` command and then provide the concrete requirements for the infrastructure you want to develop.

>[!IMPORTANT]
>Be as explicit as possible about *what* you are trying to build and *why*. **Do not focus on the tech stack at this point**.

An example prompt:

```text
Provision a production-grade Kubernetes cluster infrastructure with high availability and disaster recovery capabilities. The infrastructure should support a microservices architecture with separate environments for development, staging, and production. Include managed database services with automated backups, object storage for application assets, a content delivery network for static content, and comprehensive monitoring and logging. The infrastructure must meet SOC 2 compliance requirements and support auto-scaling based on demand. Initial capacity should handle 10,000 concurrent users with the ability to scale to 100,000 users.
```

After this prompt is entered, you should see your AI agent kick off the planning and spec drafting process. The agent will also trigger some of the built-in scripts to set up the repository.

Once this step is completed, you should have a new branch created (e.g., `001-k8s-infrastructure`), as well as a new specification in the `specs/001-k8s-infrastructure` directory.

The produced specification should contain a set of infrastructure requirements and functional requirements, as defined in the template.

At this stage, your project folder contents should resemble the following:

```text
└── .specify
    ├── memory
    │  └── constitution.md
    ├── scripts
    │  ├── check-prerequisites.sh
    │  ├── common.sh
    │  ├── create-new-feature.sh
    │  ├── setup-plan.sh
    │  └── update-agent-context.sh
    ├── specs
    │  └── 001-k8s-infrastructure
    │      └── spec.md
    └── templates
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **STEP 3:** Functional specification clarification (required before planning)

With the baseline specification created, you can go ahead and clarify any of the requirements that were not captured properly within the first shot attempt.

You should run the structured clarification workflow **before** creating a technical plan to reduce rework downstream.

Preferred order:

1. Use `/speckit.iac.clarify` (structured) – sequential, coverage-based questioning that records answers in a Clarifications section.
2. Optionally follow up with ad-hoc free-form refinement if something still feels vague.

If you intentionally want to skip clarification (e.g., spike or exploratory prototype), explicitly state that so the agent doesn't block on missing clarifications.

Example free-form refinement prompt (after `/speckit.iac.clarify` if still needed):

```text
For the database services, we need PostgreSQL 14+ with point-in-time recovery enabled. Backup retention should be 30 days for production and 7 days for non-production environments. The database should be deployed in a private subnet with no direct internet access.
```

You should also ask your AI agent to validate the **Review & Acceptance Checklist**, checking off the things that are validated/pass the requirements, and leave the ones that are not unchecked. The following prompt can be used:

```text
Read the review and acceptance checklist, and check off each item in the checklist if the infrastructure spec meets the criteria. Leave it empty if it does not.
```

It's important to use the interaction with your AI agent as an opportunity to clarify and ask questions around the specification - **do not treat its first attempt as final**.

### **STEP 4:** Generate a plan

You can now be specific about the tech stack and other technical requirements. You can use the `/speckit.iac.plan` command that is built into the project template with a prompt like this:

```text
We will use AWS as the cloud provider. For the Kubernetes cluster, use Amazon EKS with managed node groups. Database services will use Amazon RDS for PostgreSQL with Multi-AZ deployment. Object storage will use Amazon S3 with versioning enabled. Use CloudFront for the CDN. Implement infrastructure using Terraform 1.5+ with remote state stored in S3 with DynamoDB locking. Structure the code into reusable modules for networking, compute, database, and monitoring. Use AWS Systems Manager Parameter Store for secrets management.
```

The output of this step will include a number of implementation detail documents, with your directory tree resembling this:

```text
.
├── memory
│  └── constitution.md
├── scripts
│  ├── check-prerequisites.sh
│  ├── common.sh
│  ├── create-new-feature.sh
│  ├── setup-plan.sh
│  └── update-agent-context.sh
├── specs
│  └── 001-k8s-infrastructure
│      ├── contracts
│      │  └── terraform-outputs.md
│      ├── data-model.md
│      ├── plan.md
│      ├── quickstart.md
│      ├── research.md
│      └── spec.md
└── templates
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

Check the `research.md` document to ensure that the right tech stack is used, based on your instructions. You can ask your AI agent to refine it if any of the components stand out, or even have it check the locally-installed version of Terraform or cloud provider CLI tools.

Additionally, you might want to ask your AI agent to research details about the chosen tech stack if it's something that is rapidly changing (e.g., Kubernetes versions, Terraform provider versions), with a prompt like this:

```text
I want you to go through the implementation plan and implementation details, looking for areas that could benefit from additional research as AWS EKS and Terraform providers are rapidly changing. For those areas that you identify that require further research, I want you to update the research document with additional details about the specific versions that we are going to be using in this infrastructure and spawn parallel research tasks to clarify any details using research from the web.
```

During this process, you might find that your AI agent gets stuck researching the wrong thing - you can help nudge it in the right direction with a prompt like this:

```text
I think we need to break this down into a series of steps. First, identify a list of tasks that you would need to do during implementation that you're not sure of or would benefit from further research. Write down a list of those tasks. And then for each one of these tasks, I want you to spin up a separate research task so that the net result is we are researching all of those very specific tasks in parallel. What I saw you doing was it looks like you were researching AWS EKS in general and I don't think that's gonna do much for us in this case. That's way too untargeted research. The research needs to help you solve a specific targeted question.
```

>[!NOTE]
>Your AI agent might be over-eager and add components that you did not ask for. Ask it to clarify the rationale and the source of the change.

### **STEP 5:** Have your AI agent validate the plan

With the plan in place, you should have your AI agent run through it to make sure that there are no missing pieces. You can use a prompt like this:

```text
Now I want you to go and audit the implementation plan and the implementation detail files. Read through it with an eye on determining whether or not there is a sequence of tasks that you need to be doing that are obvious from reading this. Because I don't know if there's enough here. For example, when I look at the core implementation, it would be useful to reference the appropriate places in the implementation details where it can find the information as it walks through each step in the core implementation or in the refinement.
```

This helps refine the implementation plan and helps you avoid potential blind spots that your AI agent missed in its planning cycle. Once the initial refinement pass is complete, ask your AI agent to go through the checklist once more before you can get to the implementation.

You can also ask your AI agent (if you have the [GitHub CLI](https://docs.github.com/en/github-cli/github-cli) installed) to go ahead and create a pull request from your current branch to `main` with a detailed description, to make sure that the effort is properly tracked.

>[!NOTE]
>Before you have the agent implement it, it's also worth prompting your AI agent to cross-check the details to see if there are any over-engineered pieces (remember - it can be over-eager). If over-engineered components or decisions exist, you can ask your AI agent to resolve them. Ensure that your AI agent follows the [constitution](memory/constitution.md) as the foundational piece that it must adhere to when establishing the plan.

### **STEP 6:** Generate task breakdown with /speckit.iac.tasks

With the implementation plan validated, you can now break down the plan into specific, actionable tasks that can be executed in the correct order. Use the `/speckit.iac.tasks` command to automatically generate a detailed task breakdown from your implementation plan:

```text
/speckit.iac.tasks
```

This step creates a `tasks.md` file in your feature specification directory that contains:

- **Task breakdown organized by infrastructure component** - Each component becomes a separate implementation phase with its own set of tasks
- **Dependency management** - Tasks are ordered to respect dependencies between components (e.g., networking before compute, compute before databases)
- **Parallel execution markers** - Tasks that can run in parallel are marked with `[P]` to optimize development workflow
- **File path specifications** - Each task includes the exact file paths where Terraform configuration should be created
- **Validation checkpoints** - Each component phase includes checkpoints to validate with `terraform validate`, `terraform fmt`, and `tflint`
- **Checkpoint validation** - Each infrastructure component phase includes checkpoints to validate independent functionality

The generated tasks.md provides a clear roadmap for the `/speckit.implement` command, ensuring systematic implementation that maintains infrastructure quality and allows for incremental delivery of infrastructure components.

### **STEP 7:** Implementation

Once ready, use the `/speckit.implement` command to execute your implementation plan:

```text
/speckit.implement
```

The `/speckit.implement` command will:

- Validate that all prerequisites are in place (constitution, spec, plan, and tasks)
- Parse the task breakdown from `tasks.md`
- Execute tasks in the correct order, respecting dependencies and parallel execution markers
- Generate Terraform configuration files (.tf)
- Provide progress updates and handle errors appropriately

>[!IMPORTANT]
>The AI agent will execute local CLI commands (such as `terraform`, `aws`, etc.) - make sure you have the required tools installed on your machine.

Once the implementation is complete, review the generated Terraform code and run validation commands:

```bash
terraform init
terraform validate
terraform fmt -check
tflint
```

Resolve any validation errors by providing feedback to your AI agent. Remember that `terraform apply` is a manual step you control - review the plan carefully before applying changes to your infrastructure.

</details>

---

## 🔍 Troubleshooting

### Git Credential Manager on Linux

If you're having issues with Git authentication on Linux, you can install Git Credential Manager:

```bash
#!/usr/bin/env bash
set -e
echo "Downloading Git Credential Manager v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "Installing Git Credential Manager..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "Configuring Git to use GCM..."
git config --global credential.helper manager
echo "Cleaning up..."
rm gcm-linux_amd64.2.6.1.deb
```

## 👥 Maintainers

- Den Delimarsky ([@localden](https://github.com/localden))
- John Lam ([@jflam](https://github.com/jflam))

## 💬 Support

For support, please open a [GitHub issue](https://github.com/github/spec-kit/issues/new). We welcome bug reports, feature requests, and questions about using Spec-Driven Development for Infrastructure as Code.

## 🙏 Acknowledgements

This project is heavily influenced by and based on the work and research of [John Lam](https://github.com/jflam) and the [GitHub Spec Kit](https://github.com/github/spec-kit) project.

## 📄 License

This project is licensed under the terms of the MIT open source license. Please refer to the [LICENSE](./LICENSE) file for the full terms.
