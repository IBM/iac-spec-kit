"""Live integration test: run `iac-specify init --ai bob --no-git --ignore-agent-tools`
against a real temporary directory (no network: we patch the download).
Verifies the project scaffold is created correctly end-to-end.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from iac_specify_cli import app


@pytest.fixture
def runner():
    return CliRunner()


def _make_minimal_project(project_path: Path, ai_assistant=None, script_type=None,
                           is_current_dir: bool = False, **kwargs):
    """Simulate extraction of a minimal project scaffold."""
    if not is_current_dir:
        project_path.mkdir(parents=True, exist_ok=True)

    specify = project_path / ".specify"
    (specify / "memory").mkdir(parents=True, exist_ok=True)
    (specify / "templates").mkdir(parents=True, exist_ok=True)
    (specify / "scripts").mkdir(parents=True, exist_ok=True)
    (specify / "templates" / "principles-template.md").write_text("# Principles Template\n")

    bob_dir = project_path / ".bob" / "commands"
    bob_dir.mkdir(parents=True, exist_ok=True)
    (bob_dir / "iac.specify.md").write_text("---\ndescription: specify\n---\nSpecify body\n")
    (bob_dir / "iac.plan.md").write_text("---\ndescription: plan\n---\nPlan body\n")

    tracker = kwargs.get("tracker")
    if tracker:
        for key in ("fetch", "download", "extract", "zip-list", "extracted-summary"):
            tracker.add(key, key)
            tracker.complete(key, "mocked")
    return project_path


class TestInitBobLive:
    def test_project_directory_created(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            result = runner.invoke(
                app,
                [
                    "init", str(project_dir),
                    "--ai", "bob",
                    "--script", "sh",
                    "--ignore-agent-tools",
                    "--no-git",
                ],
            )
        assert result.exit_code == 0, result.output
        assert project_dir.exists()

    def test_specify_directory_created(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            runner.invoke(
                app,
                ["init", str(project_dir), "--ai", "bob", "--script", "sh",
                 "--ignore-agent-tools", "--no-git"],
            )
        assert (project_dir / ".specify").is_dir()

    def test_principles_copied_from_template(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            runner.invoke(
                app,
                ["init", str(project_dir), "--ai", "bob", "--script", "sh",
                 "--ignore-agent-tools", "--no-git"],
            )
        assert (project_dir / ".specify" / "memory" / "principles.md").exists()

    def test_output_contains_project_ready(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            result = runner.invoke(
                app,
                ["init", str(project_dir), "--ai", "bob", "--script", "sh",
                 "--ignore-agent-tools", "--no-git"],
            )
        assert "Project ready" in result.output

    def test_security_notice_shown(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            result = runner.invoke(
                app,
                ["init", str(project_dir), "--ai", "bob", "--script", "sh",
                 "--ignore-agent-tools", "--no-git"],
            )
        # IBM Bob is IDE-based; security notice includes agent folder .bob/
        assert ".bob/" in result.output

    def test_next_steps_shown(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            result = runner.invoke(
                app,
                ["init", str(project_dir), "--ai", "bob", "--script", "sh",
                 "--ignore-agent-tools", "--no-git"],
            )
        assert "Next Steps" in result.output
        assert "/iac.specify" in result.output

    def test_no_git_repo_initialized_with_no_git_flag(self, runner, tmp_path):
        project_dir = tmp_path / "iac-bob-test"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_make_minimal_project):
            runner.invoke(
                app,
                ["init", str(project_dir), "--ai", "bob", "--script", "sh",
                 "--ignore-agent-tools", "--no-git"],
            )
        assert not (project_dir / ".git").is_dir()
