"""Claude Code integration."""
from __future__ import annotations
from ..base import IntegrationBase


class ClaudeIntegration(IntegrationBase):
    key = "claude"
    config = {
        "name": "Claude Code",
        "folder": ".claude/",
        "commands_subdir": "commands",
        "install_url": "https://docs.anthropic.com/en/docs/claude-code/setup",
        "requires_cli": True,
    }
