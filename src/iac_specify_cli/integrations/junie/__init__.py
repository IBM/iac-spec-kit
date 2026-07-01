"""Junie integration."""
from __future__ import annotations
from ..base import IntegrationBase


class JunieIntegration(IntegrationBase):
    key = "junie"
    config = {
        "name": "Junie",
        "folder": ".junie/",
        "commands_subdir": "commands",
        "install_url": "https://junie.jetbrains.com/",
        "requires_cli": True,
    }
