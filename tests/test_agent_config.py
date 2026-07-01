"""Tests for the agent configuration registry."""
from __future__ import annotations

import pytest
from iac_specify_cli._agent_config import AGENT_CONFIG, SCRIPT_TYPE_CHOICES
from iac_specify_cli.integrations import INTEGRATION_REGISTRY


# ---------------------------------------------------------------------------
# AGENT_CONFIG structure
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = {"name", "folder", "install_url", "requires_cli"}


class TestAgentConfigStructure:
    def test_non_empty(self):
        assert len(AGENT_CONFIG) > 0, "AGENT_CONFIG must contain at least one agent"

    def test_required_fields_present(self):
        for key, cfg in AGENT_CONFIG.items():
            missing = REQUIRED_FIELDS - set(cfg)
            assert not missing, f"Agent '{key}' is missing fields: {missing}"

    def test_name_is_non_empty_string(self):
        for key, cfg in AGENT_CONFIG.items():
            assert isinstance(cfg["name"], str) and cfg["name"].strip(), (
                f"Agent '{key}' must have a non-empty name"
            )

    def test_requires_cli_is_bool(self):
        for key, cfg in AGENT_CONFIG.items():
            assert isinstance(cfg["requires_cli"], bool), (
                f"Agent '{key}'.requires_cli must be a bool"
            )

    def test_install_url_present_for_cli_agents(self):
        missing = []
        for key, cfg in AGENT_CONFIG.items():
            if cfg["requires_cli"] and not cfg["install_url"]:
                missing.append(key)
        assert not missing, (
            f"CLI agents missing install_url: {missing}\n"
            "Add the install URL or set requires_cli=False."
        )

    def test_known_agents_present(self):
        expected = {"claude", "copilot", "gemini", "bob", "opencode", "windsurf"}
        for agent in expected:
            assert agent in AGENT_CONFIG, f"Expected agent '{agent}' not found in AGENT_CONFIG"

    def test_generic_agent_present(self):
        assert "generic" in AGENT_CONFIG

    def test_generic_agent_not_requires_cli(self):
        assert AGENT_CONFIG["generic"]["requires_cli"] is False

    def test_bob_not_requires_cli(self):
        """IBM Bob is IDE-based and should not require a CLI tool."""
        assert AGENT_CONFIG["bob"]["requires_cli"] is False

    def test_bob_folder(self):
        assert AGENT_CONFIG["bob"]["folder"] == ".bob/"

    def test_claude_requires_cli(self):
        assert AGENT_CONFIG["claude"]["requires_cli"] is True

    def test_no_duplicate_keys(self):
        """The AGENT_CONFIG dict itself prevents duplicates, but verify via registry too."""
        assert len(AGENT_CONFIG) == len(set(AGENT_CONFIG.keys()))


# ---------------------------------------------------------------------------
# SCRIPT_TYPE_CHOICES
# ---------------------------------------------------------------------------

class TestScriptTypeChoices:
    def test_sh_present(self):
        assert "sh" in SCRIPT_TYPE_CHOICES

    def test_ps_present(self):
        assert "ps" in SCRIPT_TYPE_CHOICES

    def test_values_non_empty(self):
        for k, v in SCRIPT_TYPE_CHOICES.items():
            assert v, f"Script type '{k}' has empty description"


# ---------------------------------------------------------------------------
# Integration registry consistency
# ---------------------------------------------------------------------------

class TestIntegrationRegistry:
    def test_registry_matches_agent_config(self):
        """Every key in AGENT_CONFIG must come from INTEGRATION_REGISTRY."""
        for key in AGENT_CONFIG:
            assert key in INTEGRATION_REGISTRY, (
                f"AGENT_CONFIG key '{key}' not found in INTEGRATION_REGISTRY"
            )

    def test_registry_keys_are_non_empty(self):
        for key in INTEGRATION_REGISTRY:
            assert key, "INTEGRATION_REGISTRY must not contain empty keys"

    def test_no_duplicate_registration(self):
        """Registering the same key twice raises KeyError."""
        from iac_specify_cli.integrations import _register, INTEGRATION_REGISTRY
        from iac_specify_cli.integrations.base import IntegrationBase

        class _DummyDuplicate(IntegrationBase):
            key = "claude"  # already registered

        with pytest.raises(KeyError):
            _register(_DummyDuplicate())
