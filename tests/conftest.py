"""Shared fixtures for iac-specify-cli tests."""
from __future__ import annotations

import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from iac_specify_cli import app
from iac_specify_cli._agent_config import AGENT_CONFIG


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def tmp_project(tmp_path: Path):
    """Return a fresh temporary directory outside the current repo."""
    return tmp_path


@pytest.fixture
def tmp_project_dir(tmp_path: Path):
    """Create a non-existent subdirectory path (not yet created)."""
    return tmp_path / "my-test-project"
