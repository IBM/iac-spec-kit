"""Base class for AI-assistant integrations."""
from __future__ import annotations
from typing import Any


class IntegrationBase:
    """Thin base class every integration must implement.

    Subclasses set:
    - key: unique agent identifier (matches CLI tool name for CLI agents)
    - config: dict matching the AGENT_CONFIG entry shape
    """
    key: str = ""
    config: dict[str, Any] | None = None
