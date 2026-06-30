"""Antigravity integration."""
from __future__ import annotations
from ..base import IntegrationBase


class AgyIntegration(IntegrationBase):
    key = "agy"
    config = {
        "name": "Antigravity",
        "folder": ".agent/",
        "commands_subdir": "workflows",
        "install_url": None,
        "requires_cli": False,
    }
