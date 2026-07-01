"""Generic (bring your own agent) integration."""
from __future__ import annotations
from ..base import IntegrationBase


class GenericIntegration(IntegrationBase):
    key = "generic"
    config = {
        "name": "Generic (bring your own agent)",
        "folder": None,
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
