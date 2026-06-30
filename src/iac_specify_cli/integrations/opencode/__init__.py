"""opencode integration."""
from __future__ import annotations
from ..base import IntegrationBase


class OpencodeIntegration(IntegrationBase):
    key = "opencode"
    config = {
        "name": "opencode",
        "folder": ".opencode/",
        "commands_subdir": "command",
        "install_url": "https://opencode.ai",
        "requires_cli": True,
    }
