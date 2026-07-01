"""Tests for version utilities."""
from __future__ import annotations

import pytest
from iac_specify_cli._version import _normalize_tag, _is_newer, GITHUB_API_LATEST


class TestNormalizeTag:
    def test_strips_lowercase_v(self):
        assert _normalize_tag("v1.2.3") == "1.2.3"

    def test_strips_uppercase_v(self):
        assert _normalize_tag("V2.0.0") == "2.0.0"

    def test_no_prefix_unchanged(self):
        assert _normalize_tag("1.0.0") == "1.0.0"

    def test_empty_string_unchanged(self):
        assert _normalize_tag("") == ""


class TestIsNewer:
    def test_newer_version_returns_true(self):
        assert _is_newer("v2.0.0", "v1.0.0") is True

    def test_same_version_returns_false(self):
        assert _is_newer("v1.0.0", "v1.0.0") is False

    def test_older_version_returns_false(self):
        assert _is_newer("v0.9.0", "v1.0.0") is False

    def test_patch_bump_returns_true(self):
        assert _is_newer("1.0.1", "1.0.0") is True

    def test_invalid_version_returns_false(self):
        assert _is_newer("not-a-version", "1.0.0") is False

    def test_both_invalid_returns_false(self):
        assert _is_newer("bad", "also-bad") is False


class TestGitHubApiLatest:
    def test_is_correct_repo(self):
        assert "ibm/iac-spec-kit" in GITHUB_API_LATEST

    def test_is_https(self):
        assert GITHUB_API_LATEST.startswith("https://")
