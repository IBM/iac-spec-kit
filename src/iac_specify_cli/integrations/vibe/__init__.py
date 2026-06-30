"""Mistral Vibe integration."""
from __future__ import annotations
from ..base import IntegrationBase


class VibeIntegration(IntegrationBase):
    key = "vibe"
    config = {
        "name": "Mistral Vibe",
        "folder": ".vibe/",
        "commands_subdir": "skills",
        "install_url": "https://github.com/mistralai/mistral-vibe",
        "requires_cli": True,
    }
