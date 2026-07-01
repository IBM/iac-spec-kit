"""Tests for the install_ai_skills function and related helpers."""
from __future__ import annotations

from pathlib import Path
import yaml

import pytest

from iac_specify_cli import install_ai_skills, _get_skills_dir, AGENT_SKILLS_DIR_OVERRIDES


@pytest.fixture
def project_with_bob_commands(tmp_path: Path) -> Path:
    """Scaffold a minimal project with Bob command templates."""
    bob_cmds = tmp_path / ".bob" / "commands"
    bob_cmds.mkdir(parents=True)

    for name in ("iac.specify.md", "iac.plan.md", "iac.tasks.md"):
        (bob_cmds / name).write_text(
            f"---\ndescription: Test {name}\n---\nBody content for {name}.\n"
        )
    return tmp_path


@pytest.fixture
def project_with_no_commands(tmp_path: Path) -> Path:
    """Minimal project with no command templates."""
    (tmp_path / ".specify").mkdir()
    return tmp_path


class TestGetSkillsDir:
    def test_bob_uses_bob_skills_dir(self, tmp_path):
        result = _get_skills_dir(tmp_path, "bob")
        assert result == tmp_path / ".bob" / "skills"

    def test_claude_uses_claude_skills_dir(self, tmp_path):
        result = _get_skills_dir(tmp_path, "claude")
        assert result == tmp_path / ".claude" / "skills"

    def test_codex_uses_override(self, tmp_path):
        result = _get_skills_dir(tmp_path, "codex")
        assert result == tmp_path / AGENT_SKILLS_DIR_OVERRIDES["codex"]

    def test_unknown_agent_uses_default(self, tmp_path):
        result = _get_skills_dir(tmp_path, "unknown_agent_xyz")
        assert result == tmp_path / ".agents" / "skills"


class TestInstallAiSkills:
    def test_installs_skills_for_bob(self, project_with_bob_commands):
        project = project_with_bob_commands
        success = install_ai_skills(project, "bob")
        assert success is True

    def test_skill_files_created(self, project_with_bob_commands):
        project = project_with_bob_commands
        install_ai_skills(project, "bob")
        skills_dir = project / ".bob" / "skills"
        assert skills_dir.is_dir()
        skill_dirs = list(skills_dir.iterdir())
        assert len(skill_dirs) == 3

    def test_skill_file_named_skill_md(self, project_with_bob_commands):
        project = project_with_bob_commands
        install_ai_skills(project, "bob")
        skills_dir = project / ".bob" / "skills"
        for skill_dir in skills_dir.iterdir():
            assert (skill_dir / "SKILL.md").exists()

    def test_skill_frontmatter_is_valid_yaml(self, project_with_bob_commands):
        project = project_with_bob_commands
        install_ai_skills(project, "bob")
        skills_dir = project / ".bob" / "skills"
        for skill_dir in skills_dir.iterdir():
            content = (skill_dir / "SKILL.md").read_text()
            assert content.startswith("---"), "SKILL.md must start with YAML frontmatter"
            parts = content.split("---", 2)
            assert len(parts) >= 3, "SKILL.md must have valid frontmatter delimiter"
            parsed = yaml.safe_load(parts[1])
            assert isinstance(parsed, dict)

    def test_skill_names_start_with_iac(self, project_with_bob_commands):
        project = project_with_bob_commands
        install_ai_skills(project, "bob")
        skills_dir = project / ".bob" / "skills"
        for skill_dir in skills_dir.iterdir():
            assert skill_dir.name.startswith("iac-"), (
                f"Skill directory name '{skill_dir.name}' must start with 'iac-'"
            )

    def test_idempotent_second_install(self, project_with_bob_commands):
        project = project_with_bob_commands
        install_ai_skills(project, "bob")
        result = install_ai_skills(project, "bob")
        # Second call returns True (all already present)
        assert result is True

    def test_returns_false_when_no_templates(self, project_with_no_commands, tmp_path):
        """When no command templates exist anywhere, install_ai_skills returns False.

        The function has a fallback that looks for templates/commands/ relative to
        __file__. We redirect __file__ to an isolated directory that has no templates.
        """
        import iac_specify_cli as mod

        # Create a fake module location whose parent.parent.parent has no templates/
        fake_root = tmp_path / "fake_pkg" / "sub" / "mod.py"
        fake_root.parent.mkdir(parents=True)

        original_file = mod.__file__
        mod.__file__ = str(fake_root)
        try:
            result = install_ai_skills(project_with_no_commands, "bob")
        finally:
            mod.__file__ = original_file

        assert result is False

    def test_tracker_updated(self, project_with_bob_commands):
        from iac_specify_cli._console import StepTracker
        tracker = StepTracker("test")
        tracker.add("ai-skills", "Install skills")
        project = project_with_bob_commands
        install_ai_skills(project, "bob", tracker=tracker)
        step = next(s for s in tracker.steps if s["key"] == "ai-skills")
        assert step["status"] == "done"
