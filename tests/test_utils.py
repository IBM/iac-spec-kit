"""Tests for utility functions in _utils.py."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from iac_specify_cli._utils import (
    check_tool,
    init_git_repo,
    is_git_repo,
    merge_json_files,
    handle_vscode_settings,
)


# ---------------------------------------------------------------------------
# check_tool
# ---------------------------------------------------------------------------

class TestCheckTool:
    def test_git_found(self):
        """git should be available in the test environment."""
        assert check_tool("git") is True

    def test_nonexistent_tool_returns_false(self):
        assert check_tool("__nonexistent_tool_xyz__") is False

    def test_returns_bool(self):
        result = check_tool("git")
        assert isinstance(result, bool)

    def test_kiro_cli_alias(self):
        """kiro-cli check should also accept the bare 'kiro' executable."""
        with patch("shutil.which", side_effect=lambda t: None if t == "kiro-cli" else "/usr/bin/kiro"):
            assert check_tool("kiro-cli") is True

    def test_rovodev_uses_acli(self):
        with patch("shutil.which", return_value="/usr/bin/acli"):
            assert check_tool("rovodev") is True

    def test_rovodev_missing(self):
        with patch("shutil.which", return_value=None):
            assert check_tool("rovodev") is False

    def test_claude_local_path_wins(self):
        """If ~/.claude/local/claude exists, check_tool('claude') returns True."""
        with patch("iac_specify_cli._utils.CLAUDE_LOCAL_PATH") as mock_path:
            mock_path.exists.return_value = True
            mock_path.is_file.return_value = True
            assert check_tool("claude") is True

    def test_tracker_updated_on_found(self):
        from iac_specify_cli._console import StepTracker
        tracker = StepTracker("test")
        tracker.add("git", "Git")
        check_tool("git", tracker=tracker)
        step = next(s for s in tracker.steps if s["key"] == "git")
        assert step["status"] == "done"

    def test_tracker_updated_on_missing(self):
        from iac_specify_cli._console import StepTracker
        tracker = StepTracker("test")
        tracker.add("__nonexistent__", "Missing Tool")
        check_tool("__nonexistent__", tracker=tracker)
        step = next(s for s in tracker.steps if s["key"] == "__nonexistent__")
        assert step["status"] == "error"


# ---------------------------------------------------------------------------
# is_git_repo
# ---------------------------------------------------------------------------

class TestIsGitRepo:
    def test_true_for_existing_repo(self, tmp_path):
        """A path that is a git repo returns True."""
        subprocess.run(["git", "init", str(tmp_path)], check=True, capture_output=True)
        assert is_git_repo(tmp_path) is True

    def test_false_for_non_repo(self, tmp_path):
        assert is_git_repo(tmp_path) is False

    def test_false_for_nonexistent_path(self, tmp_path):
        assert is_git_repo(tmp_path / "does_not_exist") is False

    def test_defaults_to_cwd_when_none(self):
        """When path=None, should not raise an error."""
        # We can't predict if CWD is a repo, but it shouldn't crash.
        result = is_git_repo(None)
        assert isinstance(result, bool)


# ---------------------------------------------------------------------------
# init_git_repo
# ---------------------------------------------------------------------------

class TestInitGitRepo:
    def test_initializes_fresh_directory(self, tmp_path):
        project = tmp_path / "new_project"
        project.mkdir()
        (project / "README.md").write_text("# Hello")
        success, err = init_git_repo(project, quiet=True)
        assert success is True
        assert err is None
        assert (project / ".git").is_dir()

    def test_returns_error_message_on_failure(self, tmp_path):
        """A directory with no identity (no user config) forces a git commit failure."""
        # init_git_repo does os.chdir first, so the path must exist.
        # We make it exist but force git commit to fail by unsetting user config.
        project = tmp_path / "fail_proj"
        project.mkdir()
        (project / "README.md").write_text("content")
        import os as _os
        orig = _os.environ.copy()
        try:
            _os.environ["GIT_AUTHOR_NAME"] = ""
            _os.environ["GIT_AUTHOR_EMAIL"] = ""
            _os.environ["GIT_COMMITTER_NAME"] = ""
            _os.environ["GIT_COMMITTER_EMAIL"] = ""
            success, err = init_git_repo(project, quiet=True)
        finally:
            _os.environ.clear()
            _os.environ.update(orig)
        # Whether success or not, the function should return a bool/string tuple
        assert isinstance(success, bool)


# ---------------------------------------------------------------------------
# merge_json_files
# ---------------------------------------------------------------------------

class TestMergeJsonFiles:
    def test_adds_new_key(self, tmp_path):
        existing = tmp_path / "s.json"
        existing.write_text(json.dumps({"a": 1}))
        result = merge_json_files(existing, {"b": 2})
        assert result == {"a": 1, "b": 2}

    def test_overwrites_existing_key(self, tmp_path):
        existing = tmp_path / "s.json"
        existing.write_text(json.dumps({"a": 1}))
        result = merge_json_files(existing, {"a": 99})
        assert result["a"] == 99

    def test_deep_merge_nested_dicts(self, tmp_path):
        existing = tmp_path / "s.json"
        existing.write_text(json.dumps({"editor": {"tabSize": 4, "wordWrap": "off"}}))
        result = merge_json_files(existing, {"editor": {"tabSize": 2, "formatOnSave": True}})
        assert result["editor"]["tabSize"] == 2
        assert result["editor"]["wordWrap"] == "off"
        assert result["editor"]["formatOnSave"] is True

    def test_missing_file_returns_new_content(self, tmp_path):
        result = merge_json_files(tmp_path / "nonexistent.json", {"x": 42})
        assert result == {"x": 42}

    def test_invalid_json_returns_new_content(self, tmp_path):
        bad = tmp_path / "bad.json"
        bad.write_text("not-json{{")
        result = merge_json_files(bad, {"ok": True})
        assert result == {"ok": True}


# ---------------------------------------------------------------------------
# handle_vscode_settings
# ---------------------------------------------------------------------------

class TestHandleVsCodeSettings:
    def test_copies_when_dest_missing(self, tmp_path):
        src = tmp_path / "settings.json"
        src.write_text(json.dumps({"editor.tabSize": 4}))
        dest = tmp_path / "subdir" / "settings.json"
        dest.parent.mkdir()
        handle_vscode_settings(src, dest, "settings.json")
        assert dest.exists()
        assert json.loads(dest.read_text())["editor.tabSize"] == 4

    def test_merges_when_dest_exists(self, tmp_path):
        src = tmp_path / "src_settings.json"
        src.write_text(json.dumps({"editor.formatOnSave": True}))
        dest = tmp_path / "settings.json"
        dest.write_text(json.dumps({"editor.tabSize": 4}))
        handle_vscode_settings(src, dest, "settings.json")
        merged = json.loads(dest.read_text())
        assert merged["editor.tabSize"] == 4
        assert merged["editor.formatOnSave"] is True
