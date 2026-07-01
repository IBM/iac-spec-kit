"""Zed integration."""
from __future__ import annotations
from ..base import IntegrationBase


class ZedIntegration(IntegrationBase):
    key = "zed"
    config = {
        "name": "Zed",
        "folder": ".agents/",
        "commands_subdir": "skills",
        "install_url": None,
        "requires_cli": False,
    }
