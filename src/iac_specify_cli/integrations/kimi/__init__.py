"""Kimi Code integration."""
from __future__ import annotations
from ..base import IntegrationBase


class KimiIntegration(IntegrationBase):
    key = "kimi"
    config = {
        "name": "Kimi Code",
        "folder": ".kimi-code/",
        "commands_subdir": "skills",
        "install_url": "https://code.kimi.com/",
        "requires_cli": True,
    }
