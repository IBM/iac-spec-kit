<!--
Sync Impact Report:
Version: 1.0.0 → 1.1.0
Modified Principles: Added Principle VIII (Runtime Command Integrity)
Added Sections:
  - Principle VIII: Runtime Command Integrity
Added Rules:
  - Files in .claude/commands/ MUST NOT be modified during feature implementation
  - Branding/configuration changes MUST be applied to .specify/templates/ only
  - Runtime command changes require explicit constitution amendment
  - Task lists MUST NOT include modifications to .claude/commands/ files
Removed Sections: N/A
Templates Status:
  ✅ plan-template.md - No changes needed (no runtime command references)
  ✅ spec-template.md - No changes needed (specifications are technology-agnostic)
  ✅ tasks-template.md - Aligned (template already shows .specify/templates/ as modification target)
  ✅ agent-file-template.md - No changes needed (agent guidance separate from constitution)
  ✅ checklist-template.md - No changes needed (validation only)
Follow-up TODOs: None
Rationale for MINOR version bump (1.1.0):
  - Adds material guidance (new principle with multiple rules)
  - Does not break existing specifications or implementations
  - Prevents future errors in feature implementation
  - Based on real operational feedback from 002-iac-branding implementation
-->

# Spec Kit Constitution

## Core Principles

### I. Specification-First Development

Every feature begins with a complete, technology-agnostic specification that defines the "what" and "why" before the "how".

**Rules:**
- Specifications MUST be written before any implementation decisions
- Specifications MUST focus on user scenarios, requirements, and success criteria
- Specifications MUST NOT include technology choices, implementation details, or code structure
- Specifications MUST be independently reviewable and understandable by non-technical stakeholders

**Rationale:** Separating intent from implementation enables creative exploration, technology independence, and better alignment with actual user needs rather than technical convenience.

### II. User Story Independence (NON-NEGOTIABLE)

Every user story MUST be independently implementable, testable, and deliverable as a viable increment of value.

**Rules:**
- Each user story MUST be prioritized (P1, P2, P3, etc.)
- Each user story MUST be testable on its own without requiring other stories
- Each user story MUST deliver tangible value when implemented alone
- P1 stories MUST constitute a complete Minimum Viable Product (MVP)
- User stories MUST NOT have circular dependencies
- Cross-story integration MAY occur but MUST NOT break independent testability

**Rationale:** Independent user stories enable incremental delivery, parallel development, early value delivery, and reduced risk. Teams can ship P1 stories as MVP without waiting for lower-priority features.

### III. Test-First Discipline (NON-NEGOTIABLE)

When tests are requested, they MUST be written before implementation, MUST fail initially, and MUST pass after implementation.

**Rules:**
- Tests MUST be written and verified to fail before any implementation begins
- Implementation proceeds only after failing tests confirm test validity
- Red-Green-Refactor cycle MUST be followed strictly when tests are requested
- Contract tests MUST validate API specifications match contracts/
- Integration tests MUST validate complete user journeys
- Tests are OPTIONAL - only required when explicitly requested in specification

**Rationale:** Test-first development catches specification ambiguities early, validates that tests actually test something, and provides living documentation of intended behavior.

### IV. Technology Independence

Specifications and plans MUST support diverse technology stacks without bias toward any particular language, framework, or platform.

**Rules:**
- Specifications MUST be expressible in any modern technology stack
- Templates MUST use generic placeholders, not technology-specific terminology
- Research phase MUST validate chosen stack versions and compatibility
- Project structure MUST adapt to project type (single/web/mobile) automatically
- Constitution MUST NOT mandate specific languages, frameworks, or platforms

**Rationale:** Technology independence validates that Spec-Driven Development is a universal process, supports enterprise constraints, and enables creative exploration with different stacks.

### V. Complexity Justification

Every addition of complexity MUST be explicitly justified against simpler alternatives.

**Rules:**
- Default to simplest solution that meets requirements
- Follow YAGNI (You Aren't Gonna Need It) principles
- Violations of simplicity principles MUST be documented in Complexity Tracking table
- Each violation MUST explain why it's needed and why simpler alternatives were rejected
- Constitution Check gates MUST be passed or explicitly justified before proceeding
- Over-engineering MUST be identified and removed during validation phases

**Rationale:** Complexity is the enemy of maintainability, comprehension, and velocity. Every bit of complexity must earn its place by solving a real problem that simpler approaches cannot.

### VI. Structured Workflow Phases

Development MUST follow a defined multi-phase process: Constitution → Specification → Planning → Task Breakdown → Implementation.

**Rules:**
- Constitution MUST be established before specifications
- Specifications MUST be completed before technical planning
- Technical planning MUST be completed before task breakdown
- Task breakdown MUST be completed before implementation
- Each phase MUST have clear deliverables and validation checkpoints
- Phases MAY be iterated but MUST NOT be skipped
- Clarification SHOULD occur after specification and before planning

**Rationale:** Structured phases prevent premature implementation decisions, enable proper validation at each stage, and ensure foundational choices (constitution, requirements) guide downstream work rather than being retrofitted.

### VII. Observability and Transparency

All processes, decisions, and artifacts MUST be transparent, traceable, and auditable.

**Rules:**
- Every feature MUST have a numbered branch and specification directory (###-feature-name)
- All design decisions MUST be documented in plan.md with rationale
- All research findings MUST be captured in research.md
- All task dependencies MUST be explicit and traceable to user stories
- Implementation MUST reference specification sections it implements
- Version history and amendment tracking MUST be maintained for constitution

**Rationale:** Transparency enables collaboration, knowledge transfer, onboarding, and post-mortem analysis. Traceability ensures every line of code can be traced back to a requirement and business value.

### VIII. Runtime Command Integrity (NON-NEGOTIABLE)

Runtime command files MUST be protected from modification during feature implementation to preserve operational stability.

**Rules:**
- Files in `.claude/commands/` are runtime command definitions and MUST NOT be modified during feature implementation
- Branding, configuration, or workflow changes MUST be applied to template files in `.specify/templates/` and `templates/commands/` only
- Command name customization MUST be done by renaming templates in `templates/commands/` (e.g., `specify.md` → `iac.specify.md`)
- Template changes propagate to future releases; runtime commands in `.claude/commands/` execute current workflows
- Runtime command changes require explicit constitution amendment and cross-feature validation
- Task lists (tasks.md) MUST NOT include modifications to `.claude/commands/` files

**Rationale:** Runtime commands actively execute the development workflow. Modifying them during implementation can break in-flight operations, invalidate existing specifications, and create inconsistencies between template expectations and command behavior. The build system generates release command files from `templates/commands/` sources, so customization happens there, not in the active runtime directory. Separation of runtime execution from template generation preserves system stability.

## Development Workflow

### Amendment Procedure

Constitution amendments follow semantic versioning and require explicit impact analysis:

**Versioning Rules:**
- **MAJOR**: Backward-incompatible changes (principle removal, fundamental redefinition)
- **MINOR**: Additive changes (new principle, material expansion of existing guidance)
- **PATCH**: Clarifications, wording improvements, non-semantic fixes

**Amendment Process:**
1. Propose amendment with rationale and version bump justification
2. Document Sync Impact Report identifying affected templates and artifacts
3. Update constitution with new version and Last Amended date
4. Propagate changes to all dependent templates (plan, spec, tasks, commands)
5. Update runtime guidance documents (README, quickstart, agent files)
6. Verify no unexplained placeholder tokens remain
7. Commit with descriptive message referencing version

### Compliance Review

**All planning, design, and implementation work MUST:**
- Reference relevant constitution principles in decision rationale
- Document any principle violations in Complexity Tracking
- Pass Constitution Check gates before proceeding to next phase
- Be reviewable against constitution during code review and retrospectives

**Constitution Check Gates:**
- Gate 1: Before Phase 0 research - verify specification alignment
- Gate 2: After Phase 1 design - verify implementation plan alignment
- Ad-hoc: Anytime complexity or violations are suspected

### Complexity Governance

Teams MUST NOT add complexity without explicit justification:
- New projects, services, or architectural layers require Complexity Tracking entry
- Design patterns beyond direct implementation require justification
- Third-party dependencies beyond essential libraries require justification
- Over-engineered solutions identified during review MUST be simplified

## Governance

This constitution supersedes all other development practices and serves as the foundational authority for all technical decisions within Spec Kit projects.

All pull requests, code reviews, and retrospectives MUST verify compliance with constitutional principles. When conflicts arise between constitution and other guidance, constitution prevails unless formally amended.

Use `.specify/memory/constitution.md` (this file) for constitutional governance and `.specify/templates/agent-file-template.md` for runtime development guidance specific to AI agents.

**Version**: 1.1.0 | **Ratified**: 2025-11-01 | **Last Amended**: 2025-11-04
