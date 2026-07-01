"""Gemini CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class GeminiIntegration(IntegrationBase):
    key = "gemini"
    config = {
        "name": "Gemini CLI",
        "folder": ".gemini/",
        "commands_subdir": "commands",
        "install_url": "https://github.com/google-gemini/gemini-cli",
        "requires_cli": True,
    }
