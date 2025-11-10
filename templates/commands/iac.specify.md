---
description: Create or update the infrastructure specification from a natural language infrastructure description.
scripts:
  sh: scripts/bash/create-new-feature.sh --json "{ARGS}"
  ps: scripts/powershell/create-new-feature.ps1 -Json "{ARGS}"
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/speckit.iac.specify` in the triggering message **is** the feature description. Assume you always have it available in this conversation even if `{ARGS}` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that feature description, do this:

1. **Generate a concise short name** (2-4 words) for the branch:
   - Analyze the infrastructure description and extract the most meaningful keywords
   - Create a 2-4 word short name that captures the essence of the infrastructure
   - Use action-noun format when possible (e.g., "deploy-vpc", "configure-database")
   - Preserve technical terms and acronyms (VPC, RDS, K8s, etc.)
   - Keep it concise but descriptive enough to understand the infrastructure at a glance
   - Examples:
     - "Deploy production VPC with public and private subnets" → "production-vpc"
     - "Set up auto-scaling compute cluster with load balancing" → "autoscaling-compute"
     - "Configure managed database with automated backups" → "managed-database"
     - "Implement multi-region disaster recovery" → "multi-region-dr"

2. **Check for existing branches before creating new one**:
   
   a. First, fetch all remote branches to ensure we have the latest information:
      ```bash
      git fetch --all --prune
      ```
   
   b. Find the highest feature number across all sources for the short-name:
      - Remote branches: `git ls-remote --heads origin | grep -E 'refs/heads/[0-9]+-<short-name>$'`
      - Local branches: `git branch | grep -E '^[* ]*[0-9]+-<short-name>$'`
      - Specs directories: Check for directories matching `specs/[0-9]+-<short-name>`
   
   c. Determine the next available number:
      - Extract all numbers from all three sources
      - Find the highest number N
      - Use N+1 for the new branch number
   
   d. Run the script `{SCRIPT}` with the calculated number and short-name:
      - Pass `--number N+1` and `--short-name "your-short-name"` along with the infrastructure description
      - Bash example: `{SCRIPT} --json --number 5 --short-name "production-vpc" "Deploy production VPC with public and private subnets"`
      - PowerShell example: `{SCRIPT} -Json -Number 5 -ShortName "production-vpc" "Deploy production VPC with public and private subnets"`
   
   **IMPORTANT**:
   - Check all three sources (remote branches, local branches, specs directories) to find the highest number
   - Only match branches/directories with the exact short-name pattern
   - If no existing branches/directories found with this short-name, start with number 1
   - You must only ever run this script once per feature
   - The JSON is provided in the terminal as output - always refer to it to get the actual content you're looking for
   - The JSON output will contain BRANCH_NAME and SPEC_FILE paths
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot")

3. Load `templates/spec-template.md` to understand required sections.

4. Follow this execution flow:

    1. Parse user description from Input
       If empty: ERROR "No infrastructure description provided"
    2. Extract key concepts from description
       Identify: infrastructure components, capabilities, requirements, constraints
    3. For unclear aspects:
       - Make informed guesses based on context and industry standards
       - Only mark with [NEEDS CLARIFICATION: specific question] if:
         - The choice significantly impacts infrastructure scope or requirements
         - Multiple reasonable interpretations exist with different implications
         - No reasonable default exists
       - **LIMIT: Maximum 3 [NEEDS CLARIFICATION] markers total**
       - Prioritize clarifications by impact: scope > security/compliance > cost > technical details
    4. Fill Infrastructure Requirements section
       If no clear infrastructure capabilities: ERROR "Cannot determine infrastructure requirements"
    5. Generate Functional Requirements
       Each requirement must be testable
       Use reasonable defaults for unspecified details (document assumptions in Assumptions section)
    6. Define Success Criteria
       Create measurable, technology-agnostic outcomes
       Include both quantitative metrics (SLOs, cost, capacity) and qualitative measures (compliance, operational readiness)
       Each criterion must be verifiable without implementation details
    7. Document Cost Constraints and Compliance Requirements (if applicable)
    8. Return: SUCCESS (spec ready for planning)

5. Write the specification to SPEC_FILE using the template structure, replacing placeholders with concrete details derived from the infrastructure description (arguments) while preserving section order and headings.

6. **Specification Quality Validation**: After writing the initial spec, validate it against quality criteria:

   a. **Create Spec Quality Checklist**: Generate a checklist file at `INFRA_DIR/checklists/requirements.md` using the checklist template structure with these validation items:

      ```markdown
      # Specification Quality Checklist: [INFRASTRUCTURE NAME]

      **Purpose**: Validate specification completeness and quality before proceeding to planning
      **Created**: [DATE]
      **Infrastructure**: [Link to spec.md]
      
      ## Content Quality

      - [ ] No implementation details (cloud providers, specific tools)
      - [ ] Focused on infrastructure capabilities and business needs
      - [ ] Written for both technical and non-technical stakeholders
      - [ ] All mandatory sections completed

      ## Requirement Completeness

      - [ ] No [NEEDS CLARIFICATION] markers remain
      - [ ] Requirements are testable and unambiguous
      - [ ] Success criteria are measurable
      - [ ] Success criteria are technology-agnostic (no cloud provider names)
      - [ ] SLOs are clearly defined with measurement methods
      - [ ] Cost constraints are documented
      - [ ] Compliance requirements identified (if applicable)
      - [ ] Scope is clearly bounded
      - [ ] Dependencies and assumptions identified

      ## Infrastructure Readiness

      - [ ] All functional requirements have clear success criteria
      - [ ] Non-functional requirements (performance, availability, security, scalability) defined
      - [ ] Infrastructure meets measurable outcomes defined in Success Criteria
      - [ ] No implementation details leak into specification

      ## Notes

      - Items marked incomplete require spec updates before `/iac.plan`
      ```

   b. **Run Validation Check**: Review the spec against each checklist item:
      - For each item, determine if it passes or fails
      - Document specific issues found (quote relevant spec sections)

   c. **Handle Validation Results**:

      - **If all items pass**: Mark checklist complete and proceed to step 6

      - **If items fail (excluding [NEEDS CLARIFICATION])**:
        1. List the failing items and specific issues
        2. Update the spec to address each issue
        3. Re-run validation until all items pass (max 3 iterations)
        4. If still failing after 3 iterations, document remaining issues in checklist notes and warn user

      - **If [NEEDS CLARIFICATION] markers remain**:
        1. Extract all [NEEDS CLARIFICATION: ...] markers from the spec
        2. **LIMIT CHECK**: If more than 3 markers exist, keep only the 3 most critical (by scope/security/UX impact) and make informed guesses for the rest
        3. For each clarification needed (max 3), present options to user in this format:

           ```markdown
           ## Question [N]: [Topic]
           
           **Context**: [Quote relevant spec section]
           
           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]
           
           **Suggested Answers**:
           
           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |
           
           **Your choice**: _[Wait for user response]_
           ```

        4. **CRITICAL - Table Formatting**: Ensure markdown tables are properly formatted:
           - Use consistent spacing with pipes aligned
           - Each cell should have spaces around content: `| Content |` not `|Content|`
           - Header separator must have at least 3 dashes: `|--------|`
           - Test that the table renders correctly in markdown preview
        5. Number questions sequentially (Q1, Q2, Q3 - max 3 total)
        6. Present all questions together before waiting for responses
        7. Wait for user to respond with their choices for all questions (e.g., "Q1: A, Q2: Custom - [details], Q3: B")
        8. Update the spec by replacing each [NEEDS CLARIFICATION] marker with the user's selected or provided answer
        9. Re-run validation after all clarifications are resolved

   d. **Update Checklist**: After each validation iteration, update the checklist file with current pass/fail status

7. Report completion with branch name, spec file path, checklist results, and readiness for the next phase (`/iac.plan`).

**NOTE:** The script creates and checks out the new branch and initializes the spec file before writing.

## General Guidelines

## Quick Guidelines

- Focus on **WHAT** infrastructure is needed and **WHY**.
- Avoid HOW to implement (no cloud providers, specific tools, IaC syntax).
- Written for both infrastructure and business stakeholders.
- DO NOT create any checklists that are embedded in the spec. That will be a separate command.

### Section Requirements

- **Mandatory sections**: Must be completed for every infrastructure specification
- **Optional sections**: Include only when relevant to the infrastructure
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation

When creating this spec from a user prompt:

1. **Make informed guesses**: Use context, industry standards, and common cloud patterns to fill gaps
2. **Document assumptions**: Record reasonable defaults in the Assumptions section
3. **Limit clarifications**: Maximum 3 [NEEDS CLARIFICATION] markers - use only for critical decisions that:
   - Significantly impact infrastructure scope or requirements
   - Have multiple reasonable interpretations with different implications
   - Lack any reasonable default
4. **Prioritize clarifications**: scope > security/compliance > cost > technical details
5. **Think like an infrastructure engineer**: Every vague requirement should fail the "testable and unambiguous" checklist item
6. **Common areas needing clarification** (only if no reasonable default exists):
   - Infrastructure scope and boundaries (include/exclude specific components)
   - Security and compliance requirements (when legally/financially significant)
   - Cost constraints and budget limits (when significantly impacting design)

**Examples of reasonable defaults** (don't ask about these):

- Environment type: Infer from context (dev, staging, prod) and adjust requirements accordingly
- Availability targets: Match to environment purpose (dev: lower SLOs acceptable, prod: higher requirements)
- Backup frequency: Align with data criticality and environment (dev: daily, prod: hourly/continuous)
- Multi-region: Only assume if explicitly mentioned or clearly needed for compliance/DR
- Scaling approach: Start with simple fixed capacity unless high traffic mentioned

### Success Criteria Guidelines

Success criteria must be:

1. **Measurable**: Include specific metrics (time, percentage, count, rate)
2. **Technology-agnostic**: No mention of frameworks, languages, databases, or tools
3. **User-focused**: Describe outcomes from user/business perspective, not system internals
4. **Verifiable**: Can be tested/validated without knowing implementation details

**Good examples**:

- "Infrastructure deploys in under 15 minutes"
- "System scales to handle 10,000 requests per second"
- "99.9% uptime SLO for production workloads"
- "Database failover completes in under 5 minutes"

**Bad examples** (implementation-focused):

- "Terraform files are under 500 lines" (implementation detail, use outcome-based metric)
- "Uses dedicated-cores database instances" (technology-specific, too prescriptive)
- "IBM Cloud provider version 1.60" (version-specific, let plan phase decide)
- "VPC has 3 subnets across zones" (architecture detail, belongs in plan phase)
