# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to the IaC Spec Kit (IaC Specify CLI and infrastructure templates) are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## About IaC Spec Kit

**IaC Spec Kit** is a domain-specific implementation of the spec-driven development pattern optimized for Infrastructure as Code workflows. This project is forked from the original [GitHub Spec Kit](https://github.com/github/spec-kit) which focuses on general software development.

**For the complete changelog history prior to the IaC fork, please refer to the [original GitHub Spec Kit changelog](https://github.com/github/spec-kit/blob/main/CHANGELOG.md).**

IaC Spec Kit provides infrastructure-specific templates, foundational principles, cloud resource specifications, and Terraform patterns. All infrastructure commands use the `.iac` namespace (e.g., `/iac.specify`, `/iac.plan`, `/iac.tasks`).

---

## [0.0.3] - 2025-11-21

### Fixed

- Resolved ambiguity in [`iac.principles.md`](templates/commands/iac.principles.md) command
- Corrected file paths in principles template
- Relaxed baseline single-zone template requirements

### Infrastructure

- Added Renovate configuration for automated dependency updates

### Documentation

- Added visual walkthrough video (2 minutes) to main README showing end-to-end workflow
- Updated examples table to remove "Time" column
- Removed "Estimated Time" field from all individual example README files
- Added link to generated WordPress example repository
- Improved MCP server recommendations and documentation
- Enhanced user documentation wording and flow
- Fixed badge display and improved README structure

---

## [0.0.1] - 2025-11-14

### Added

- Initial release of IaC Spec Kit
- Infrastructure-specific templates for cloud resources, networking, security, and compliance
- Multi-cloud support (AWS, Azure, GCP, IBM Cloud)
- IaC-centric command namespace (`.iac` prefix)
- Support for multiple AI coding assistants (Claude Code, GitHub Copilot, Gemini CLI, Cursor, Qwen Code, opencode, Windsurf, Kilo Code, Auggie CLI, CodeBuddy CLI, Roo Code, Codex CLI, Amazon Q Developer CLI, Amp, IBM Bob)
- `iac-specify` CLI tool for project initialization
- Infrastructure principles and governance frameworks
- Cloud-agnostic specification templates
- Terraform-focused implementation patterns
- Example workflows for common infrastructure patterns

### Documentation

- Comprehensive README with multi-cloud examples
- Cloud provider workflow guides (AWS, Azure, GCP, IBM Cloud)
- Infrastructure architecture documentation
- Agent integration guide
- Writing tech-agnostic specifications guide

### Infrastructure

- GitHub Actions workflow for releases
- Python package configuration with `pyproject.toml`
- Development scripts for local testing
