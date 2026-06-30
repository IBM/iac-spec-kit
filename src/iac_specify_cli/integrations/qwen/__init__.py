"""Qwen Code integration."""
from __future__ import annotations
from ..base import IntegrationBase


class QwenIntegration(IntegrationBase):
    key = "qwen"
    config = {
        "name": "Qwen Code",
        "folder": ".qwen/",
        "commands_subdir": "commands",
        "install_url": "https://github.com/QwenLM/qwen-code",
        "requires_cli": True,
    }
