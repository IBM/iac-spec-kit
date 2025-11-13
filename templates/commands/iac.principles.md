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
   - If the user inputs and the repo context do not provide sufficient details, ask a few simple and scoped questions to derive values - **IMPORTANT**: Environment type (dev/staging/production) is critical for principle selection: dev environments typically need Simplicity + Security (Baseline) only, skipping observability managed services/HA/DR/compliance; staging adds Observability and mirrors production security; production adds Reliability, Identity, and potentially Compliance. Also ask: which cloud?, what overall development approach (start simple and add complexity iteratively, or complex upfront?).
   - **DO NOT ask** "which of the X principles from the template do you want." Instead derive principle selection from environment type and brief user interview.
   - **IMPORTANT**: Create charter-style principles (high-level tenets like AWS Well-Architected Framework), NOT technical implementation checklists. Focus on WHAT outcomes and WHY they matter, not tactical HOW (specific tools, commands, or managed services). Principles should be tool-agnostic and outcomes-focused.
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `PRINCIPLES_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated principles content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle follows charter-style format: action-oriented title (e.g., "Design for Simplicity"), rationale explaining WHY it matters, and how Baseline/Enhanced scale the philosophy across environments (dev/staging/production).
   - **AVOID technical implementation details** like specific tools (tflint, terraform test), service names (NAT gateways, private endpoints), or tactical commands. Keep principles at strategic level - focus on outcomes and philosophy.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `/templates/plan-template.md` and ensure any "Principles Check" or rules align with updated principles.
   - Read `/templates/spec-template.md` for scope/requirements alignment—update if the principles add/remove mandatory sections or constraints.
   - Read `/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `iac.*.md` (including this one) to verify no outdated references remain when generic guidance is required.
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
   - Principles follow charter-style: high-level tenets, not technical checklists. No specific tool names, service names, or implementation commands in principle descriptions.

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
