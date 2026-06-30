"""Tabnine CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class TabnineIntegration(IntegrationBase):
    key = "tabnine"
    config = {
        "name": "Tabnine CLI",
        "folder": ".tabnine/agent/",
        "commands_subdir": "commands",
        "install_url": "https://docs.tabnine.com/main/getting-started/tabnine-cli",
        "requires_cli": True,
    }
