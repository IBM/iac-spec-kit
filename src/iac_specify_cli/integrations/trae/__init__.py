"""Trae integration."""
from __future__ import annotations
from ..base import IntegrationBase


class TraeIntegration(IntegrationBase):
    key = "trae"
    config = {
        "name": "Trae",
        "folder": ".trae/",
        "commands_subdir": "skills",
        "install_url": None,
        "requires_cli": False,
    }
