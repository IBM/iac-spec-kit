"""Amp integration."""
from __future__ import annotations
from ..base import IntegrationBase


class AmpIntegration(IntegrationBase):
    key = "amp"
    config = {
        "name": "Amp",
        "folder": ".agents/",
        "commands_subdir": "commands",
        "install_url": "https://ampcode.com/manual#install",
        "requires_cli": True,
    }
