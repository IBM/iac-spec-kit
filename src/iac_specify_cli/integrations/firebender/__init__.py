"""Firebender integration."""
from __future__ import annotations
from ..base import IntegrationBase


class FirebenderIntegration(IntegrationBase):
    key = "firebender"
    config = {
        "name": "Firebender",
        "folder": ".firebender/",
        "commands_subdir": "commands",
        "install_url": "https://firebender.dev",
        "requires_cli": False,
    }
