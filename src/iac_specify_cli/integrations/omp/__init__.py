"""OMP integration."""
from __future__ import annotations
from ..base import IntegrationBase


class OmpIntegration(IntegrationBase):
    key = "omp"
    config = {
        "name": "OMP",
        "folder": ".omp/",
        "commands_subdir": "commands",
        "install_url": None,
        "requires_cli": False,
    }
