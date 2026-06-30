"""Lingma integration."""
from __future__ import annotations
from ..base import IntegrationBase


class LingmaIntegration(IntegrationBase):
    key = "lingma"
    config = {
        "name": "Lingma",
        "folder": ".lingma/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
