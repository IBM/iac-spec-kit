"""Cursor integration."""
from __future__ import annotations
from ..base import IntegrationBase


class CursorAgentIntegration(IntegrationBase):
    key = "cursor-agent"
    config = {
        "name": "Cursor",
        "folder": ".cursor/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
