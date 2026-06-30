"""Integration registry for AI coding assistants."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import IntegrationBase

INTEGRATION_REGISTRY: dict[str, "IntegrationBase"] = {}


def _register(integration: "IntegrationBase") -> None:
    """Register an integration in the global registry."""
    key = integration.key
    if not key:
        raise ValueError("Cannot register integration with an empty key.")
    if key in INTEGRATION_REGISTRY:
        raise KeyError(f"Integration with key {key!r} is already registered.")
    INTEGRATION_REGISTRY[key] = integration


def _register_builtins() -> None:
    """Register all built-in integrations."""
    from .copilot import CopilotIntegration
    from .claude import ClaudeIntegration
    from .gemini import GeminiIntegration
    from .cursor_agent import CursorAgentIntegration
    from .qwen import QwenIntegration
    from .opencode import OpencodeIntegration
    from .codex import CodexIntegration
    from .windsurf import WindsurfIntegration
    from .kilocode import KilocodeIntegration
    from .auggie import AuggieIntegration
    from .codebuddy import CodebuddyIntegration
    from .qodercli import QodercliIntegration
    from .roo import RooIntegration
    from .q import QIntegration
    from .amp import AmpIntegration
    from .shai import ShaiIntegration
    from .agy import AgyIntegration
    from .bob import BobIntegration
    from .generic import GenericIntegration

    _register(CopilotIntegration())
    _register(ClaudeIntegration())
    _register(GeminiIntegration())
    _register(CursorAgentIntegration())
    _register(QwenIntegration())
    _register(OpencodeIntegration())
    _register(CodexIntegration())
    _register(WindsurfIntegration())
    _register(KilocodeIntegration())
    _register(AuggieIntegration())
    _register(CodebuddyIntegration())
    _register(QodercliIntegration())
    _register(RooIntegration())
    _register(QIntegration())
    _register(AmpIntegration())
    _register(ShaiIntegration())
    _register(AgyIntegration())
    _register(BobIntegration())
    _register(GenericIntegration())


_register_builtins()
