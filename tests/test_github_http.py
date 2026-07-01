"""Tests for GitHub HTTP helpers."""
from __future__ import annotations

import pytest
from unittest.mock import MagicMock

from iac_specify_cli._github_http import (
    _github_token,
    _github_auth_headers,
    _parse_rate_limit_headers,
    _format_rate_limit_error,
)


class TestGithubToken:
    def test_cli_arg_takes_precedence(self, monkeypatch):
        monkeypatch.setenv("GH_TOKEN", "env_token")
        assert _github_token("cli_token") == "cli_token"

    def test_env_gh_token_used(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        monkeypatch.setenv("GH_TOKEN", "from_env")
        assert _github_token() == "from_env"

    def test_github_token_env_used(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        monkeypatch.setenv("GITHUB_TOKEN", "from_github_token")
        assert _github_token() == "from_github_token"

    def test_none_when_no_token(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        assert _github_token() is None

    def test_empty_string_treated_as_none(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        assert _github_token("") is None

    def test_whitespace_only_treated_as_none(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        assert _github_token("   ") is None


class TestGithubAuthHeaders:
    def test_returns_bearer_when_token_present(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        headers = _github_auth_headers("mytoken")
        assert "Authorization" in headers
        assert headers["Authorization"] == "Bearer mytoken"

    def test_returns_empty_when_no_token(self, monkeypatch):
        monkeypatch.delenv("GH_TOKEN", raising=False)
        monkeypatch.delenv("GITHUB_TOKEN", raising=False)
        headers = _github_auth_headers(None)
        assert headers == {}


class TestParseRateLimitHeaders:
    def _make_headers(self, data: dict):
        mock = MagicMock()
        mock.__contains__ = lambda self, key: key in data
        mock.get = lambda key, default=None: data.get(key, default)
        return mock

    def test_extracts_limit_and_remaining(self):
        headers = self._make_headers({
            "X-RateLimit-Limit": "60",
            "X-RateLimit-Remaining": "42",
        })
        result = _parse_rate_limit_headers(headers)
        assert result["limit"] == "60"
        assert result["remaining"] == "42"

    def test_parses_reset_epoch(self):
        import time
        future = int(time.time()) + 3600
        headers = self._make_headers({
            "X-RateLimit-Reset": str(future),
        })
        result = _parse_rate_limit_headers(headers)
        assert "reset_epoch" in result
        assert "reset_time" in result

    def test_empty_headers_returns_empty_dict(self):
        headers = self._make_headers({})
        result = _parse_rate_limit_headers(headers)
        assert result == {}


class TestFormatRateLimitError:
    def _make_headers(self, data: dict):
        mock = MagicMock()
        mock.__contains__ = lambda self, key: key in data
        mock.get = lambda key, default=None: data.get(key, default)
        return mock

    def test_includes_status_code(self):
        headers = self._make_headers({})
        msg = _format_rate_limit_error(403, headers, "https://api.github.com/test")
        assert "403" in msg

    def test_includes_url(self):
        headers = self._make_headers({})
        msg = _format_rate_limit_error(200, headers, "https://example.com/api")
        assert "example.com" in msg

    def test_includes_troubleshooting_tips(self):
        headers = self._make_headers({})
        msg = _format_rate_limit_error(429, headers, "https://api.github.com")
        assert "Troubleshooting" in msg
