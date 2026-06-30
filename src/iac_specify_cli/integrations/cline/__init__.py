"""Cline integration."""
from __future__ import annotations
from ..base import IntegrationBase


class ClineIntegration(IntegrationBase):
    key = "cline"
    config = {
        "name": "Cline",
        "folder": ".clinerules/",
        "commands_subdir": "workflows",
        "install_url": "https://github.com/cline/cline",
        "requires_cli": False,
    }
