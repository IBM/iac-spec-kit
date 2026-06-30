"""Kilo Code integration."""
from __future__ import annotations
from ..base import IntegrationBase


class KilocodeIntegration(IntegrationBase):
    key = "kilocode"
    config = {
        "name": "Kilo Code",
        "folder": ".kilocode/",
        "commands_subdir": "workflows",
        "install_url": None,
        "requires_cli": False,
    }
