"""Devin for Terminal integration."""
from __future__ import annotations
from ..base import IntegrationBase


class DevinIntegration(IntegrationBase):
    key = "devin"
    config = {
        "name": "Devin for Terminal",
        "folder": ".devin/",
        "commands_subdir": "skills",
        "install_url": "https://cli.devin.ai/docs",
        "requires_cli": True,
    }
