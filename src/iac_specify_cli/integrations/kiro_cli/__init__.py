"""Kiro CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class KiroCliIntegration(IntegrationBase):
    key = "kiro-cli"
    config = {
        "name": "Kiro CLI",
        "folder": ".kiro/",
        "commands_subdir": "prompts",
        "install_url": "https://kiro.dev/docs/cli/",
        "requires_cli": True,
    }
