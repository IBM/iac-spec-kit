# Contributing to IaC Spec Kit

Thank you for your interest in contributing to IaC Spec Kit! This project explores how Specification-Driven Development can improve infrastructure as code workflows with AI assistance. As this is an experimental field, contributions help shape what's possible with AI-assisted infrastructure provisioning.

## Ways to contribute

Contributions are welcome in any area. See [ideas for future work](IDEAS.md) for inspiration. Here are some specific ways you can help:

### Improve templates and patterns
- Refine existing specification, plan, and task templates based on real usage
- Add constraints or examples that reduce AI hallucinations
- Create template variants for different complexity levels
- Document template design patterns that work well

### Add cloud provider support
- Submit examples for additional cloud providers (Oracle Cloud, Alibaba Cloud, etc.)
- Document what works and what doesn't for specific providers
- Create cloud-specific workflow guides

### Test with different AI agents
- Try the toolkit with various AI coding agents
- Report compatibility issues or improvements
- Share agent-specific tips or configurations

### Submit example workflows
- Contribute example specs for different scenarios (HIPAA compliance, FinServ, microservices, etc.)
- Share real-world infrastructure patterns
- Document lessons learned from production use

### Enhance validation and quality gates
- Improve validation checkpoints in templates
- Add pre-commit hooks or automation scripts
- Contribute to IaC quality checks

### Documentation improvements
- Fix typos or clarify instructions
- Add missing documentation
- Improve guides or examples

## Development setup

### Prerequisites

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11+ | CLI tool runtime |
| uv | Latest | Package management |
| Git | Any | Version control |
| Terraform | 1.0+ | Testing generated IaC (optional) |
| AI coding agent | Any | Testing templates ([supported agents](README.md#supported-ai-agents)) |

### Local development installation

```bash
# Clone the repository
git clone https://github.com/ibm/iac-spec-kit.git
cd iac-spec-kit

# Install in development mode with uv
uv pip install -e .

# Verify installation
iac-specify --help
```

### Template structure

The key templates that guide AI agents are located in:
- `.specify/templates/spec-template.md` - Infrastructure specification template
- `.specify/templates/plan-template.md` - Technical implementation plan template
- `.specify/templates/tasks-template.md` - Task breakdown template
- `.specify/memory/principles.md` - Project principles template

### Testing workflow

1. Make changes to templates or scripts
2. Test with at least one AI coding agent:
   ```bash
   # Initialize a test project
   iac-specify init test-project --ai <your-agent>

   # Test the workflow
   cd test-project
   <launch-your-ai-agent>
   ```
3. Run through the complete SDD workflow:
   - `/iac.principles` - Create principles
   - `/iac.specify` - Create specification
   - `/iac.plan` - Generate plan
   - `/iac.tasks` - Create task list
   - `/iac.implement` - Execute implementation
4. Verify generated outputs and IaC quality

## Contribution workflow

### Fork and clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/iac-spec-kit.git
cd iac-spec-kit
git remote add upstream https://github.com/ibm/iac-spec-kit.git
```

### Branch naming

Use descriptive branch names:
- `feat/add-oracle-cloud-example` - New features
- `fix/template-typo` - Bug fixes
- `docs/improve-readme` - Documentation
- `test/pulumi-compatibility` - Testing

### Making changes

1. Create a feature branch:
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. Make your changes to templates, scripts, or documentation

3. Test thoroughly with at least one AI agent

4. Commit with clear messages:
   ```bash
   git commit -m "feat: add Oracle Cloud workflow example"
   ```

### PR submission guidelines

When submitting a pull request:

1. **Provide context**: Explain what problem you're solving or what you're improving
2. **Include testing notes**: Describe which AI agent(s) you tested with and what you verified
3. **Show examples**: If you modified templates, include example outputs
4. **Keep scope focused**: One logical change per PR
5. **Follow existing style**: Match the tone and format of existing documentation

Example PR description:
```
## Summary
Adds workflow examples for Oracle Cloud Infrastructure (OCI).

## Changes
- Created OCI workflow guide in examples/01-simple-vpc/cloud-workflows/oci.md
- Added OCI-specific MCP server recommendations to README.md

## Testing
Tested with Claude Code using:
- /iac.specify for basic VPC requirements
- /iac.plan targeting OCI in us-phoenix-1
- Verified generated Terraform uses OCI provider correctly

## Notes
OCI uses different terminology (VCN vs VPC) - updated templates to handle this
```

## Template design best practices

When modifying templates, keep these principles in mind:

### Writing effective prompts
- Be explicit about what AI agents should and shouldn't do at each phase
- Use examples to clarify expectations
- Include validation checkpoints to catch errors early

### Cloud-agnostic language
- Specification and principles should use generic infrastructure terms
- Plans and implementation can reference specific cloud services
- This separation enables multi-cloud deployment from a single spec

### Validation checkpoints
- Each phase should include review criteria
- Templates should prompt AI to validate outputs
- Quality gates should be explicit and actionable

### Example structure
- Provide concrete examples within templates
- Show both good and bad patterns
- Link to real-world examples in the repository

## Code style

### Markdown formatting
- Use sentence case for headings (capitalize only first word and proper nouns)
- Include tables for structured data
- Use code blocks with language identifiers
- Add expandable `<details>` sections for lengthy content

### Shell script conventions
- Use `#!/usr/bin/env bash` shebang
- Include error handling (`set -e`)
- Add comments for non-obvious logic
- Test on Linux, macOS, and Windows (Git Bash/PowerShell)

### Python code style
- Follow PEP 8
- Use type hints
- Include docstrings for public functions
- Test with Python 3.11+

## Getting help

- **Questions**: Open a [GitHub issue](https://github.com/ibm/iac-spec-kit/issues/new) with the question label
- **Bug reports**: Include AI agent, OS, Python version, and reproduction steps
- **Feature ideas**: Check [IDEAS.md](IDEAS.md) for inspiration or propose new directions
- **Discussions**: Use GitHub Discussions for broader topics

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
