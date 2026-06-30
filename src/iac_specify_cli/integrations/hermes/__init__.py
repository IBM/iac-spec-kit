"""Hermes integration."""
from __future__ import annotations
from ..base import IntegrationBase


class HermesIntegration(IntegrationBase):
    key = "hermes"
    config = {
        "name": "Hermes",
        "folder": ".hermes/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": True,
    }
