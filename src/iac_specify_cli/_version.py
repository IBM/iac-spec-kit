from __future__ import annotations

from pathlib import Path


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
