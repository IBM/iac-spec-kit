"""SHAI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class ShaiIntegration(IntegrationBase):
    key = "shai"
    config = {
        "name": "SHAI",
        "folder": ".shai/",
        "commands_subdir": "commands",
        "install_url": "https://github.com/ovh/shai",
        "requires_cli": True,
    }
