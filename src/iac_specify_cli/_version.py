from __future__ import annotations

import re
from pathlib import Path
from packaging.version import Version, InvalidVersion


def get_speckit_version() -> str:
    """Get current iac-spec-kit version."""
    import importlib.metadata
    try:
        return importlib.metadata.version("iac-specify-cli")
    except Exception:
        # Fallback: try reading from pyproject.toml
        try:
            import tomllib
            pyproject_path = Path(__file__).parent.parent.parent / "pyproject.toml"
            if pyproject_path.exists():
                with open(pyproject_path, "rb") as f:
                    data = tomllib.load(f)
                    return data.get("project", {}).get("version", "unknown")
        except Exception:
            pass
    return "unknown"


GITHUB_API_LATEST = "https://api.github.com/repos/ibm/iac-spec-kit/releases/latest"


def _normalize_tag(tag: str) -> str:
    """Strip leading 'v' from a git tag for version parsing."""
    return tag[1:] if tag.startswith(("v", "V")) else tag


def _fetch_latest_release_tag() -> tuple[str | None, str | None]:
    """Return (tag_name, failure_reason). Uses httpx from _github_http.

    Returns (tag, None) on success, (None, reason_string) on failure.
    """
    from ._github_http import client, _github_auth_headers
    try:
        resp = client.get(
            GITHUB_API_LATEST,
            headers={**_github_auth_headers(), "Accept": "application/vnd.github+json"},
            timeout=5,
            follow_redirects=True,
        )
        if resp.status_code in (403, 429):
            return None, "rate limited (set GH_TOKEN or GITHUB_TOKEN to increase limits)"
        if resp.status_code != 200:
            return None, f"HTTP {resp.status_code}"
        tag = resp.json().get("tag_name")
        if not isinstance(tag, str) or not tag:
            return None, "missing tag_name in GitHub response"
        return tag, None
    except Exception as exc:
        return None, f"offline or timeout ({exc})"


def _is_newer(latest: str, current: str) -> bool:
    """Return True if latest > current under PEP 440."""
    try:
        return Version(_normalize_tag(latest)) > Version(_normalize_tag(current))
    except InvalidVersion:
        return False
