"""Auggie CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class AuggieIntegration(IntegrationBase):
    key = "auggie"
    config = {
        "name": "Auggie CLI",
        "folder": ".augment/",
        "commands_subdir": "commands",
        "install_url": "https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli",
        "requires_cli": True,
    }
