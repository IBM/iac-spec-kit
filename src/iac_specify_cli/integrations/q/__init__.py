"""Amazon Q Developer CLI integration."""
from __future__ import annotations
from ..base import IntegrationBase


class QIntegration(IntegrationBase):
    key = "q"
    config = {
        "name": "Amazon Q Developer CLI",
        "folder": ".amazonq/",
        "commands_subdir": "prompts",
        "install_url": "https://aws.amazon.com/developer/learning/q-developer-cli/",
        "requires_cli": True,
    }
