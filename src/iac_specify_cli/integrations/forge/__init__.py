"""Forge integration."""
from __future__ import annotations
from ..base import IntegrationBase


class ForgeIntegration(IntegrationBase):
    key = "forge"
    config = {
        "name": "Forge",
        "folder": ".forge/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": True,
    }
