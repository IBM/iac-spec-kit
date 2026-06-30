"""Roo Code integration."""
from __future__ import annotations
from ..base import IntegrationBase


class RooIntegration(IntegrationBase):
    key = "roo"
    config = {
        "name": "Roo Code",
        "folder": ".roo/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
