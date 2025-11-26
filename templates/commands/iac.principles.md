---
description: Create or update the infrastructure project principles from interactive or provided inputs, ensuring all dependent templates stay in sync
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project principles at `.specify/memory/principles.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[CODE_PRINCIPLE_1_NAME]`, ...). Your job is to (a) collect and/or derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing principles template at `.specify/memory/principles.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior principles versions if embedded).
   - If the user inputs and the repo context do not provide sufficient details, you MUST ask clarifying questions before proceeding. Ask about: the specific infrastructure being built, key constraints or requirements, what "simplicity" or "security" means for THIS project, environment type (dev/staging/production), which cloud provider, and overall development approach. Do not skip this step.
   - **DO NOT ask** "which of the X principles from the template do you want." Instead derive principle selection from environment type and brief user interview.
   - **IMPORTANT**: Create charter-style principles (high-level tenets like AWS Well-Architected Framework), NOT technical implementation checklists. Focus on WHAT outcomes and WHY they matter.
   - **CRITICAL**: Do NOT copy the example text from the template comments verbatim. The examples show STRUCTURE and FORMAT only. Your principles must reflect the specific infrastructure project. Adapt examples to the user's chosen cloud provider and IaC tool.
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown choose current date), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `PRINCIPLES_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated principles content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle follows charter-style format: action-oriented title (e.g., "Design for Simplicity"), rationale explaining WHY it matters FOR THIS SPECIFIC PROJECT, and how Baseline/Enhanced scale the philosophy. Examples must be specific to the infrastructure being built - never copy generic examples from the template.
   - **Architecture Principles**: Keep cloud-agnostic - focus on outcomes and philosophy, avoid specific service names.
   - **IaC Code Principles**: CAN include tech-specific examples (module registries, validation tools) to reinforce concepts like "use modules over resources" - but adapt to the user's chosen cloud/tool, don't copy generic lists.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Principles Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if the principles add/remove mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file matching `iac.*.md` pattern (including this one) to verify no outdated references remain when generic guidance is required. Known command files include:
     - `iac.analyze.md` - Infrastructure analysis and assessment
     - `iac.checklist.md` - Checklist generation and validation
     - `iac.clarify.md` - Requirements clarification
     - `iac.implement.md` - Implementation guidance
     - `iac.plan.md` - Planning and architecture
     - `iac.principles.md` - This file (principles management)
     - `iac.specify.md` - Specification creation
     - `iac.tasks.md` - Task breakdown and management
   - If additional `iac.*.md` files exist, search for them using the pattern `iac.*.md` to ensure complete coverage.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the principles file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).
   - Architecture Principles follow charter-style: high-level tenets, cloud-agnostic outcomes.
   - IaC Code Principles may include tech-specific examples adapted to the user's chosen cloud/tool.

7. Write the completed principles back to `.specify/memory/principles.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: update principles to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/principles.md` file.
