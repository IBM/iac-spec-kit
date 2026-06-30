"""RovoDev ACLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class RovodevIntegration(IntegrationBase):
    key = "rovodev"
    config = {
        "name": "RovoDev ACLI",
        "folder": ".rovodev/",
        "commands_subdir": "skills",
        "install_url": "https://www.atlassian.com/software/rovo-dev",
        "requires_cli": True,
    }
