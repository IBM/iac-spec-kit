"""Tests for StepTracker and console utilities."""
from __future__ import annotations

import pytest
from iac_specify_cli._console import StepTracker


class TestStepTracker:
    def test_add_step(self):
        t = StepTracker("test")
        t.add("step1", "Step One")
        assert len(t.steps) == 1
        assert t.steps[0]["key"] == "step1"
        assert t.steps[0]["status"] == "pending"

    def test_add_duplicate_key_is_noop(self):
        t = StepTracker("test")
        t.add("step1", "Step One")
        t.add("step1", "Step One Again")
        assert len(t.steps) == 1

    def test_start_sets_running(self):
        t = StepTracker("test")
        t.add("step1", "Step One")
        t.start("step1", "in progress")
        assert t.steps[0]["status"] == "running"
        assert t.steps[0]["detail"] == "in progress"

    def test_complete_sets_done(self):
        t = StepTracker("test")
        t.add("step1", "Step One")
        t.complete("step1", "all good")
        assert t.steps[0]["status"] == "done"

    def test_error_sets_error(self):
        t = StepTracker("test")
        t.add("step1", "Step One")
        t.error("step1", "failed!")
        assert t.steps[0]["status"] == "error"
        assert t.steps[0]["detail"] == "failed!"

    def test_skip_sets_skipped(self):
        t = StepTracker("test")
        t.add("step1", "Step One")
        t.skip("step1", "not needed")
        assert t.steps[0]["status"] == "skipped"

    def test_update_unknown_key_appends(self):
        """Updating a key not added via add() appends a new entry."""
        t = StepTracker("test")
        t.complete("ghost", "surprise step")
        assert any(s["key"] == "ghost" for s in t.steps)

    def test_render_returns_renderable(self):
        """render() must return a Rich renderable (Tree)."""
        from rich.tree import Tree
        t = StepTracker("test")
        t.add("a", "A")
        t.complete("a", "ok")
        result = t.render()
        assert isinstance(result, Tree)

    def test_refresh_callback_is_called(self):
        calls = []
        t = StepTracker("test")
        t.attach_refresh(lambda: calls.append(1))
        t.add("s", "Step")
        assert len(calls) == 1

    def test_refresh_callback_exception_is_swallowed(self):
        """Errors in the refresh callback must not propagate."""
        def bad_callback():
            raise RuntimeError("boom")

        t = StepTracker("test")
        t.attach_refresh(bad_callback)
        # Should not raise
        t.add("s", "Step")

    def test_multiple_steps_ordering(self):
        t = StepTracker("test")
        for i in range(5):
            t.add(f"step{i}", f"Step {i}")
        for i, step in enumerate(t.steps):
            assert step["key"] == f"step{i}"

    def test_detail_empty_by_default(self):
        t = StepTracker("test")
        t.add("s", "S")
        assert t.steps[0]["detail"] == ""

    def test_complete_without_detail(self):
        t = StepTracker("test")
        t.add("s", "S")
        t.complete("s")
        assert t.steps[0]["status"] == "done"
        assert t.steps[0]["detail"] == ""
