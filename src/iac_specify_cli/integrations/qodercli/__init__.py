"""Qoder CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class QodercliIntegration(IntegrationBase):
    key = "qodercli"
    config = {
        "name": "Qoder CLI",
        "folder": ".qoder/",
        "commands_subdir": "commands",
        "install_url": "https://qoder.com/cli",
        "requires_cli": True,
    }
