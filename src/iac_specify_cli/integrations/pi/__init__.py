"""Pi Coding Agent integration."""
from __future__ import annotations
from ..base import IntegrationBase


class PiIntegration(IntegrationBase):
    key = "pi"
    config = {
        "name": "Pi Coding Agent",
        "folder": ".pi/",
        "commands_subdir": "commands",
        "install_url": "https://www.earendil.works/pi",
        "requires_cli": True,
    }
