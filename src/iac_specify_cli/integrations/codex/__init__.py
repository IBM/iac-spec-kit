"""Codex CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class CodexIntegration(IntegrationBase):
    key = "codex"
    config = {
        "name": "Codex CLI",
        "folder": ".codex/",
        "commands_subdir": "prompts",
        "install_url": "https://github.com/openai/codex",
        "requires_cli": True,
    }
