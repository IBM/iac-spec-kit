"""Integration tests for the iac-specify CLI commands.

These tests use Typer's CliRunner so they run entirely in-process.
Where operations would make network calls or touch the filesystem beyond
what is needed, they are patched.
"""
from __future__ import annotations

import json
import zipfile
from io import BytesIO
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from iac_specify_cli import app
from iac_specify_cli._agent_config import AGENT_CONFIG


@pytest.fixture
def runner():
    return CliRunner()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_zip(files: dict[str, bytes]) -> bytes:
    """Build an in-memory ZIP archive from a dict of {name: content}."""
    buf = BytesIO()
    with zipfile.ZipFile(buf, "w") as zf:
        for name, content in files.items():
            zf.writestr(name, content)
    return buf.getvalue()


def _mock_download_and_extract(project_path: Path, ai_assistant, script_type,
                                is_current_dir=False, **kwargs):
    """Simulate template extraction by writing stub files to project_path."""
    if not is_current_dir:
        project_path.mkdir(parents=True, exist_ok=True)
    (project_path / ".specify").mkdir(parents=True, exist_ok=True)
    (project_path / ".specify" / "memory").mkdir(parents=True, exist_ok=True)
    (project_path / ".specify" / "templates").mkdir(parents=True, exist_ok=True)
    (project_path / ".specify" / "templates" / "principles-template.md").write_text("# Principles\n")
    (project_path / ".specify" / "scripts").mkdir(parents=True, exist_ok=True)

    tracker = kwargs.get("tracker")
    if tracker:
        for key in ("fetch", "download", "extract", "zip-list", "extracted-summary"):
            tracker.add(key, key)
            tracker.complete(key, "mocked")
    return project_path


# ---------------------------------------------------------------------------
# --help / --version
# ---------------------------------------------------------------------------

class TestHelpCommand:
    def test_help_exits_zero(self, runner):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0

    def test_help_mentions_commands(self, runner):
        result = runner.invoke(app, ["--help"])
        for cmd in ("init", "check", "version"):
            assert cmd in result.output


class TestVersionCommand:
    def test_version_exits_zero(self, runner):
        # version calls GitHub API; patch the http client to avoid real calls
        with patch("iac_specify_cli.client") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "tag_name": "v0.0.8",
                "published_at": "2025-01-01T00:00:00Z",
            }
            mock_client.get.return_value = mock_response
            result = runner.invoke(app, ["version"])
        assert result.exit_code == 0

    def test_version_shows_cli_version(self, runner):
        with patch("iac_specify_cli.client") as mock_client:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"tag_name": "v1.0.0", "published_at": "2025-01-01T00:00:00Z"}
            mock_client.get.return_value = mock_response
            result = runner.invoke(app, ["version"])
        assert "CLI Version" in result.output


# ---------------------------------------------------------------------------
# check command
# ---------------------------------------------------------------------------

class TestCheckCommand:
    def test_check_exits_zero(self, runner):
        result = runner.invoke(app, ["check"])
        assert result.exit_code == 0

    def test_check_mentions_git(self, runner):
        result = runner.invoke(app, ["check"])
        assert "git" in result.output.lower() or "Git" in result.output


# ---------------------------------------------------------------------------
# init command – argument validation (no network required)
# ---------------------------------------------------------------------------

class TestInitValidation:
    def test_no_args_fails(self, runner):
        result = runner.invoke(app, ["init"])
        assert result.exit_code != 0

    def test_both_project_name_and_here_fails(self, runner, tmp_path):
        result = runner.invoke(app, ["init", "myproject", "--here"], catch_exceptions=False)
        assert result.exit_code != 0
        assert "Cannot specify both" in result.output

    def test_invalid_ai_fails(self, runner, tmp_path):
        result = runner.invoke(
            app,
            ["init", str(tmp_path / "proj"), "--ai", "nonexistent_agent_xyz", "--ignore-agent-tools", "--no-git"],
        )
        assert result.exit_code != 0
        assert "Invalid AI assistant" in result.output

    def test_ai_flag_value_starting_with_dashes_rejected(self, runner):
        result = runner.invoke(app, ["init", "--ai", "--here"])
        assert result.exit_code != 0
        assert "Invalid value for --ai" in result.output

    def test_ai_skills_without_ai_fails(self, runner, tmp_path):
        result = runner.invoke(
            app,
            ["init", str(tmp_path / "proj"), "--ai-skills", "--ignore-agent-tools", "--no-git"],
        )
        assert result.exit_code != 0
        assert "--ai-skills requires --ai" in result.output

    def test_ai_commands_dir_without_generic_fails(self, runner, tmp_path):
        result = runner.invoke(
            app,
            [
                "init", str(tmp_path / "proj"),
                "--ai", "bob",
                "--ai-commands-dir", ".myagent/commands/",
                "--ignore-agent-tools", "--no-git",
            ],
        )
        assert result.exit_code != 0
        assert "--ai-commands-dir can only be used with --ai generic" in result.output

    def test_generic_without_commands_dir_fails(self, runner, tmp_path):
        result = runner.invoke(
            app,
            ["init", str(tmp_path / "proj"), "--ai", "generic", "--no-git"],
        )
        assert result.exit_code != 0

    def test_existing_directory_fails(self, runner, tmp_path):
        existing = tmp_path / "existing_project"
        existing.mkdir()
        result = runner.invoke(
            app,
            ["init", str(existing), "--ai", "bob", "--ignore-agent-tools", "--no-git"],
        )
        assert result.exit_code != 0
        assert "already exists" in result.output.lower() or "Directory Conflict" in result.output

    def test_invalid_script_type_fails(self, runner, tmp_path):
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract):
            result = runner.invoke(
                app,
                [
                    "init", str(tmp_path / "proj"),
                    "--ai", "bob",
                    "--script", "bat",
                    "--ignore-agent-tools", "--no-git",
                ],
            )
        assert result.exit_code != 0
        assert "Invalid script type" in result.output

    def test_dot_sets_here_flag(self, runner, tmp_path):
        """Passing '.' as project_name is equivalent to --here."""
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract), \
             patch("iac_specify_cli.Path.cwd", return_value=tmp_path):
            result = runner.invoke(
                app,
                ["init", ".", "--ai", "bob", "--ignore-agent-tools", "--no-git", "--force"],
            )
        # Should not error on "Cannot specify both project name and --here"
        assert "Cannot specify both" not in result.output


# ---------------------------------------------------------------------------
# init command – successful extraction (patched network)
# ---------------------------------------------------------------------------

class TestInitSuccess:
    def test_init_bob_no_git(self, runner, tmp_path):
        project_dir = tmp_path / "testproj"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract):
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
        assert "Project ready" in result.output

    def test_init_copilot_no_git(self, runner, tmp_path):
        project_dir = tmp_path / "copilot_proj"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract):
            result = runner.invoke(
                app,
                [
                    "init", str(project_dir),
                    "--ai", "copilot",
                    "--script", "sh",
                    "--ignore-agent-tools",
                    "--no-git",
                ],
            )
        assert result.exit_code == 0, result.output

    def test_init_here_no_git(self, runner, tmp_path):
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract), \
             patch("iac_specify_cli.Path.cwd", return_value=tmp_path):
            result = runner.invoke(
                app,
                [
                    "init", "--here",
                    "--ai", "bob",
                    "--script", "sh",
                    "--ignore-agent-tools",
                    "--no-git",
                    "--force",
                ],
            )
        assert result.exit_code == 0, result.output
        assert "Project ready" in result.output

    def test_init_generic_with_commands_dir(self, runner, tmp_path):
        project_dir = tmp_path / "generic_proj"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract):
            result = runner.invoke(
                app,
                [
                    "init", str(project_dir),
                    "--ai", "generic",
                    "--ai-commands-dir", ".myagent/commands/",
                    "--script", "sh",
                    "--ignore-agent-tools",
                    "--no-git",
                ],
            )
        assert result.exit_code == 0, result.output

    def test_init_shows_next_steps(self, runner, tmp_path):
        project_dir = tmp_path / "steps_proj"
        with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract):
            result = runner.invoke(
                app,
                [
                    "init", str(project_dir),
                    "--ai", "claude",
                    "--script", "sh",
                    "--ignore-agent-tools",
                    "--no-git",
                ],
            )
        assert result.exit_code == 0, result.output
        assert "/iac.specify" in result.output or "Next Steps" in result.output

    def test_init_all_agents_validated(self, runner, tmp_path):
        """Every agent key in AGENT_CONFIG must be accepted by the init command."""
        skip_agents = {"generic"}  # generic requires --ai-commands-dir
        for agent_key in AGENT_CONFIG:
            if agent_key in skip_agents:
                continue
            project_dir = tmp_path / f"proj_{agent_key}"
            with patch("iac_specify_cli.download_and_extract_template", side_effect=_mock_download_and_extract):
                result = runner.invoke(
                    app,
                    [
                        "init", str(project_dir),
                        "--ai", agent_key,
                        "--script", "sh",
                        "--ignore-agent-tools",
                        "--no-git",
                    ],
                )
            assert result.exit_code == 0, (
                f"init --ai {agent_key} failed with exit {result.exit_code}:\n{result.output}"
            )
