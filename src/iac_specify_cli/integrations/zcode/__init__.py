"""ZCode integration."""
from __future__ import annotations
from ..base import IntegrationBase


class ZcodeIntegration(IntegrationBase):
    key = "zcode"
    config = {
        "name": "ZCode",
        "folder": ".zcode/",
        "commands_subdir": "skills",
        "install_url": "https://zcode.z.ai/",
        "requires_cli": True,
    }
