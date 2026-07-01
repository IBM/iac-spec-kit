"""CodeBuddy integration."""
from __future__ import annotations
from ..base import IntegrationBase


class CodebuddyIntegration(IntegrationBase):
    key = "codebuddy"
    config = {
        "name": "CodeBuddy",
        "folder": ".codebuddy/",
        "commands_subdir": "commands",
        "install_url": "https://www.codebuddy.ai/cli",
        "requires_cli": True,
    }
