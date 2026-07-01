"""Goose integration."""
from __future__ import annotations
from ..base import IntegrationBase


class GooseIntegration(IntegrationBase):
    key = "goose"
    config = {
        "name": "Goose",
        "folder": ".goose/",
        "commands_subdir": "recipes",
        "install_url": "https://goose-docs.ai",
        "requires_cli": True,
    }
