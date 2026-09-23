"""Tests for ensure_executable_scripts and ensure_principles_from_template."""
from __future__ import annotations

import os
import stat
from pathlib import Path

import pytest

from iac_specify_cli import ensure_executable_scripts, ensure_principles_from_template
from iac_specify_cli._console import StepTracker


# ---------------------------------------------------------------------------
# ensure_executable_scripts
# ---------------------------------------------------------------------------

class TestEnsureExecutableScripts:
    @pytest.mark.skipif(os.name == "nt", reason="POSIX executable bits are not supported on Windows")
    def test_makes_sh_scripts_executable(self, tmp_path):
        scripts_dir = tmp_path / ".specify" / "scripts"
        scripts_dir.mkdir(parents=True)
        script = scripts_dir / "deploy.sh"
        script.write_bytes(b"#!/bin/bash\necho hello\n")
        # Remove exec bits
        script.chmod(0o644)

        ensure_executable_scripts(tmp_path)

        mode = script.stat().st_mode
        assert mode & stat.S_IXUSR, "Owner exec bit should be set"

    @pytest.mark.skipif(os.name == "nt", reason="POSIX executable bits are not supported on Windows")
    def test_makes_sh_scripts_in_speckit_executable(self, tmp_path):
        scripts_dir = tmp_path / ".speckit" / "scripts"
        scripts_dir.mkdir(parents=True)
        script = scripts_dir / "setup.sh"
        script.write_bytes(b"#!/bin/bash\necho hello\n")
        script.chmod(0o644)

        ensure_executable_scripts(tmp_path)

        mode = script.stat().st_mode
        assert mode & stat.S_IXUSR, "Owner exec bit should be set on .speckit script"

    @pytest.mark.skipif(os.name == "nt", reason="POSIX executable bits are not supported on Windows")
    def test_skips_non_shebang_sh_files(self, tmp_path):
        scripts_dir = tmp_path / ".specify" / "scripts"
        scripts_dir.mkdir(parents=True)
        script = scripts_dir / "data.sh"
        script.write_bytes(b"# Just a comment\n")
        script.chmod(0o644)

        ensure_executable_scripts(tmp_path)

        mode = script.stat().st_mode
        assert not (mode & stat.S_IXUSR), "Non-shebang file should NOT get exec bit"

    def test_no_scripts_dir_is_noop(self, tmp_path):
        # Should not raise even when .specify/scripts does not exist
        ensure_executable_scripts(tmp_path)

    def test_tracker_reports_updated_count(self, tmp_path):
        scripts_dir = tmp_path / ".specify" / "scripts"
        scripts_dir.mkdir(parents=True)
        for i in range(3):
            s = scripts_dir / f"script{i}.sh"
            s.write_bytes(b"#!/bin/bash\necho hi\n")
            s.chmod(0o644)

        tracker = StepTracker("test")
        # Note: ensure_executable_scripts adds "chmod" step to tracker
        ensure_executable_scripts(tmp_path, tracker=tracker)
        step = next((s for s in tracker.steps if s["key"] == "chmod"), None)
        assert step is not None
        if os.name == "nt":
            assert step["status"] == "skipped"
            assert "Windows" in step["detail"]
        else:
            assert step["status"] == "done"
            assert "3 updated" in step["detail"]


# ---------------------------------------------------------------------------
# ensure_principles_from_template
# ---------------------------------------------------------------------------

class TestEnsurePrinciplesFromTemplate:
    def test_copies_template_to_memory(self, tmp_path):
        memory_dir = tmp_path / ".specify" / "memory"
        templates_dir = tmp_path / ".specify" / "templates"
        memory_dir.mkdir(parents=True)
        templates_dir.mkdir(parents=True)
        (templates_dir / "principles-template.md").write_text("# Principles\n")

        ensure_principles_from_template(tmp_path)

        assert (memory_dir / "principles.md").exists()
        assert "# Principles" in (memory_dir / "principles.md").read_text()

    def test_preserves_existing_principles(self, tmp_path):
        memory_dir = tmp_path / ".specify" / "memory"
        templates_dir = tmp_path / ".specify" / "templates"
        memory_dir.mkdir(parents=True)
        templates_dir.mkdir(parents=True)
        existing = memory_dir / "principles.md"
        existing.write_text("# My Custom Principles\n")
        (templates_dir / "principles-template.md").write_text("# Template\n")

        ensure_principles_from_template(tmp_path)

        assert existing.read_text() == "# My Custom Principles\n"

    def test_no_template_does_not_raise(self, tmp_path):
        memory_dir = tmp_path / ".specify" / "memory"
        memory_dir.mkdir(parents=True)
        # No templates dir
        ensure_principles_from_template(tmp_path)

    def test_tracker_skipped_if_existing(self, tmp_path):
        memory_dir = tmp_path / ".specify" / "memory"
        memory_dir.mkdir(parents=True)
        (memory_dir / "principles.md").write_text("# Existing\n")

        tracker = StepTracker("test")
        ensure_principles_from_template(tmp_path, tracker=tracker)
        step = next((s for s in tracker.steps if s["key"] == "principles"), None)
        assert step is not None
        assert step["status"] == "skipped"

    def test_tracker_complete_when_copied(self, tmp_path):
        memory_dir = tmp_path / ".specify" / "memory"
        templates_dir = tmp_path / ".specify" / "templates"
        memory_dir.mkdir(parents=True)
        templates_dir.mkdir(parents=True)
        (templates_dir / "principles-template.md").write_text("# Template\n")

        tracker = StepTracker("test")
        ensure_principles_from_template(tmp_path, tracker=tracker)
        step = next((s for s in tracker.steps if s["key"] == "principles"), None)
        assert step is not None
        assert step["status"] == "done"
