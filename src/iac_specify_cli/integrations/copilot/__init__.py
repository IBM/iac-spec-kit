"""GitHub Copilot integration."""
from __future__ import annotations
from ..base import IntegrationBase


class CopilotIntegration(IntegrationBase):
    key = "copilot"
    config = {
        "name": "GitHub Copilot",
        "folder": ".github/",
        "commands_subdir": "agents",
        "install_url": None,
        "requires_cli": False,
    }
