"""Tests for the integration modules."""
from __future__ import annotations

import pytest
from iac_specify_cli.integrations import INTEGRATION_REGISTRY
from iac_specify_cli.integrations.base import IntegrationBase


REQUIRED_CONFIG_FIELDS = {"name", "folder", "install_url", "requires_cli"}


class TestIntegrationBase:
    def test_base_has_empty_key(self):
        base = IntegrationBase()
        assert base.key == ""

    def test_base_has_none_config(self):
        base = IntegrationBase()
        assert base.config is None


class TestAllIntegrations:
    @pytest.fixture(params=list(INTEGRATION_REGISTRY.keys()))
    def integration(self, request):
        return INTEGRATION_REGISTRY[request.param]

    def test_key_non_empty(self, integration):
        assert integration.key, f"{type(integration).__name__} must have a non-empty key"

    def test_config_not_none(self, integration):
        assert integration.config is not None, (
            f"{type(integration).__name__} config must not be None"
        )

    def test_config_has_required_fields(self, integration):
        missing = REQUIRED_CONFIG_FIELDS - set(integration.config)
        assert not missing, (
            f"{type(integration).__name__} config missing: {missing}"
        )

    def test_name_is_non_empty_string(self, integration):
        assert isinstance(integration.config["name"], str)
        assert integration.config["name"].strip()

    def test_requires_cli_is_bool(self, integration):
        assert isinstance(integration.config["requires_cli"], bool)


class TestSpecificIntegrations:
    def test_claude_key(self):
        from iac_specify_cli.integrations.claude import ClaudeIntegration
        assert ClaudeIntegration.key == "claude"

    def test_claude_requires_cli(self):
        from iac_specify_cli.integrations.claude import ClaudeIntegration
        assert ClaudeIntegration.config["requires_cli"] is True

    def test_claude_folder(self):
        from iac_specify_cli.integrations.claude import ClaudeIntegration
        assert ClaudeIntegration.config["folder"] == ".claude/"

    def test_bob_key(self):
        from iac_specify_cli.integrations.bob import BobIntegration
        assert BobIntegration.key == "bob"

    def test_bob_ide_based(self):
        from iac_specify_cli.integrations.bob import BobIntegration
        assert BobIntegration.config["requires_cli"] is False
        assert BobIntegration.config["install_url"] is None

    def test_bob_folder(self):
        from iac_specify_cli.integrations.bob import BobIntegration
        assert BobIntegration.config["folder"] == ".bob/"

    def test_gemini_requires_cli(self):
        from iac_specify_cli.integrations.gemini import GeminiIntegration
        assert GeminiIntegration.config["requires_cli"] is True

    def test_generic_no_folder(self):
        from iac_specify_cli.integrations.generic import GenericIntegration
        assert GenericIntegration.config["folder"] is None

    def test_generic_not_requires_cli(self):
        from iac_specify_cli.integrations.generic import GenericIntegration
        assert GenericIntegration.config["requires_cli"] is False

    def test_copilot_ide_based(self):
        from iac_specify_cli.integrations.copilot import CopilotIntegration
        assert CopilotIntegration.config["requires_cli"] is False

    def test_goose_custom_commands_subdir(self):
        from iac_specify_cli.integrations.goose import GooseIntegration
        assert GooseIntegration.config["commands_subdir"] == "recipes"
