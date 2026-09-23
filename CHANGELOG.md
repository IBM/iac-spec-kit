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

## [0.0.10] - 2026-07-07

### Fixed (IaC-specific)

- **Executable bash scripts out of the box OOTB (#11)**:
  - Updated git repository index permissions for `scripts/bash/*.sh` to `100755`.
  - Added explicit `chmod +x` step in `.github/workflows/scripts/create-release-packages.sh` before zipping release archives.
  - Improved `ensure_executable_scripts` in CLI core to check `.specify` and `.speckit` directories recursively and properly complete progress tracker step on Windows.

## [0.0.9] - 2026-06-30

> Syncs with [GitHub Spec Kit](https://github.com/github/spec-kit) [v0.12.0](https://github.com/github/spec-kit/releases/tag/v0.12.0) (upstream, 2026-06-29), plus IaC-specific additions and corrections.
> Note: v0.0.8 was an unintended early release from `main` containing only dependency updates; this release supersedes it with the full upstream sync.

### Added (IaC-specific)

- **New `/iac.converge` command**: Assesses the Terraform codebase against spec/plan/tasks and appends remaining unbuilt work as new tasks to `tasks.md`

### Changed (IaC-specific corrections)

- **`spec-template.md`**: Added `## Assumptions` section with infra-scope examples; replaced app-tier NFR performance examples (API latency, RPS) with infra-tier equivalents (subnet throughput, storage IOPS, scale-out time)
- **`iac.analyze.md`**: Replaced User Stories load step and user-story inventory with NFR + SC-### acceptance criteria inventory
- **`iac.clarify.md`**: Replaced software-app taxonomy (personas, data model, rate limiting, UX behavior) with IaC equivalents (consumer teams/service accounts, resource & config model, provisioning failure, quota breaches)
- **`iac.converge.md`**: Replaced User Stories / `US1/AC2` references with acceptance criteria checkboxes and `SC-###` style keys
- **`iac.specify.md`**: Clarification priority uses `operational impact` instead of `UX impact`

### Added (from upstream — [v0.1.6 → v0.12.0](https://github.com/github/spec-kit/blob/main/CHANGELOG.md))

- **19 new agent integrations**: Cline, Devin for Terminal, Firebender, Forge, Goose, Hermes, iFlow, Junie, Kimi Code, Kiro CLI, Lingma, OMP, Pi Coding Agent, RovoDev ACLI, Tabnine CLI, Trae, Mistral Vibe, ZCode, Zed — bringing total supported agents to 38
- **`setup-tasks.sh` / `setup-tasks.ps1`**: Script pair for task prerequisite validation
- **`SPECIFY_INIT_DIR` monorepo support**: Set this env var to target a member project from the repo root in bash/PowerShell scripts
- **`find_specify_root()` in scripts**: Scripts now find the project root via `.specify/` directory marker instead of `.git`, enabling non-git repo support
- **`iac-specify self check`**: Check whether a newer release is available (ported from upstream `specify self check`)
- **`iac-specify self upgrade`**: Upgrade the CLI in-place via `uv`, `pipx`, or source (ported from upstream `specify self upgrade`)
- **Extension hook blocks** in all command templates (`before_*` / `after_*` hooks via `.specify/extensions.yml`)
- **`handoffs` frontmatter** in `iac.specify.md` and `iac.clarify.md` for agent-to-agent chaining
- **New `.devcontainer/`**: Devcontainer configuration with Junie CLI, Pi Coding Agent, Kiro CLI, and Kimi Code CLI pre-installed (adapted from upstream; excludes Amazon Q)

### Changed (from upstream)

- **`update-agent-context.sh` / `.ps1`**: Plan path now derived from `.specify/feature.json` with fallback to `SPECIFY_FEATURE` env var
- CLI refactored into sub-modules (`_console.py`, `_github_http.py`, `_utils.py`, `_version.py`, `integrations/`) — no behaviour change for users

### Fixed (from upstream)

- `run_command()` now rejects `shell=True` with a clear error (security hardening)
- Windows: force UTF-8 stdout/stderr to prevent `UnicodeEncodeError` on non-UTF-8 code pages

---

## [0.0.7] - 2026-03-02

> This release syncs the installer with [GitHub Spec Kit](https://github.com/github/spec-kit) [v0.1.6](https://github.com/github/spec-kit/releases/tag/v0.1.6) (upstream, 2026-02-23). There is no change to the IaC templates.

### Added (from upstream)

- **Extension system**: New `iac-specify extension` command group for managing modular extension packages (`list`, `add`, `remove`, `search`, `info`, `update`, `enable`, `disable`) — ported from upstream `specify extension`
- **Version command**: `iac-specify version` shows CLI version, latest template version, and system info — ported from upstream `specify version`
- **New agents**: Added support for SHAI/OVHcloud (`shai`), Antigravity (`agy`), Qoder CLI (`qodercli`), and Generic/bring-your-own-agent (`generic`) — from upstream agent additions
- **Generic agent support**: `--ai-commands-dir` option allows specifying a custom commands directory for any AI agent — from upstream
- **AI skills installation**: New `--ai-skills` option in `init` command to install AI agent skills alongside project setup — from upstream
- **Principles setup**: Projects now get a `.specify/memory/principles.md` from the principles template during initialization — adapted from upstream constitution setup
- **Rate-limit error handling**: Improved error messages when GitHub API rate limits are hit, with guidance on authentication — from upstream
- New `extensions.py` module providing `ExtensionManifest`, `ExtensionRegistry`, `ExtensionManager`, `CommandRegistrar`, `ExtensionCatalog`, `ConfigManager`, and `HookExecutor` classes — ported from upstream `specify_cli/extensions.py`

### Changed (from upstream)

- Updated all agent configurations with `commands_subdir` field for more flexible directory structures
- Copilot agent now uses `.github/agents` directory (was `.github/prompts`)
- Added `pyyaml>=6.0`, `packaging>=23.0`, `click>=8.1` to dependencies

### Changed (IaC-specific)

- Updated release packaging to include all 19 agent variants (was 15)
- Release workflow now triggers on `src/**` path changes
- Updated bash and PowerShell agent context scripts with new agent support

### Infrastructure

- Updated `create-release-packages.sh` with new agent build variants and `rewrite_paths` dedup fix
- Updated `create-github-release.sh` with new agent ZIP entries

---

## [0.0.6] - 2025-12-19

### Changed

- Streamlined workflow with faster, more focused commands:
  - `/iac.plan` now uses lightweight research by default for quicker iteration
  - Added optional `/iac.enrichplan` command for deep research and architecture exploration when needed
  - `/iac.principles` is now optional, recognizing that IaC repositories typically focus on single infrastructure specifications rather than multiple application components requiring governance

### Fixed

- Issue where plan.md file was overridden during workflow execution
- Removed unused references to data-model and contracts md files

### Documentation

- Updated documentation to reflect streamlined workflow with optional commands
- Added list of ideas for future work and contribution guide

### Infrastructure

- Added issue templates for GitHub

---

## [0.0.5] - 2025-12-02

### Fixed

- Issue where some paths had double .specify/.specify in generated release bundles

---

## [0.0.4] - 2025-11-27

### Fixed

- Abstracted principle name examples in templates to prevent verbatim copying by AI agents
- Updated principles template with improved version guidance and clearer instructions
- Trimmed verbose boilerplate comments from specification template for better readability
- Replaced deployment terminology with provision/environment terminology in commands for consistency

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
