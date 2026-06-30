"""iFlow integration."""
from __future__ import annotations
from ..base import IntegrationBase


class IflowIntegration(IntegrationBase):
    key = "iflow"
    config = {
        "name": "iFlow",
        "folder": ".iflow/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
