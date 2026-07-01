"""Windsurf integration."""
from __future__ import annotations
from ..base import IntegrationBase


class WindsurfIntegration(IntegrationBase):
    key = "windsurf"
    config = {
        "name": "Windsurf",
        "folder": ".windsurf/",
        "commands_subdir": "workflows",
        "install_url": None,
        "requires_cli": False,
    }
