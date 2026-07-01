"""IBM Bob integration."""
from __future__ import annotations
from ..base import IntegrationBase


class BobIntegration(IntegrationBase):
    key = "bob"
    config = {
        "name": "IBM Bob",
        "folder": ".bob/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
