"""Regression tests for the git branch-name command injection (CWE-78).

Background:
    Git allows branch names such as ``001-x';id>PWNED;x='``. The bash helper
    scripts in ``scripts/bash`` used to place the branch name into shell text
    and run it through ``eval``, so that name executed ``id`` as the developer.
    ``PWNED`` is only a marker file: if it exists afterwards, the injected
    command ran.

What is covered:
    Negative (must be blocked)
        - the original payload, against all four helper scripts
        - other injection forms ($(...), backticks, ; | & ")
        - a malicious SPECIFY_FEATURE environment variable
    Positive (must keep working)
        - a valid branch, against all four helper scripts
        - valid name variants (dot, underscore, slash, capitals)
        - a valid SPECIFY_FEATURE value
        - a non-feature branch still gets the normal error
        - a folder without git still works
    Static
        - no script uses ``eval`` as a command

The scripts are bash, so they are run with ``subprocess`` inside a temporary
git project. The real repository is never modified.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
BASH_DIR = REPO / "scripts" / "bash"

pytestmark = pytest.mark.skipif(
    shutil.which("bash") is None or shutil.which("git") is None,
    reason="bash and git are required",
)

# Original payload: closes the quote, runs `id` into PWNED, reopens the quote.
PAYLOAD = "001-x';id>PWNED;x='"

# Other injection forms that git accepts as branch names.
# (Git forbids spaces and ~ ^ : ? * [ \ in names, so those cannot be tested.)
EXTRA_PAYLOADS = [
    "001-x$(id>PWNED)",
    "001-x`id>PWNED`",
    "001-x;id>PWNED",
    "001-x|id>PWNED",
    "001-x&id>PWNED",
    '001-x";id>PWNED;"',
]

# Valid branch names that must be accepted.
VALID_NAMES = ["001-x.1", "001-x_y", "001-Feature-X", "001-feat/sub"]

# Every script that used `eval $(get_feature_paths)`.
SCRIPTS = [
    ("check-prerequisites.sh", "--json", "--require-tasks", "--include-tasks"),
    ("setup-plan.sh", "--json"),
    ("setup-tasks.sh", "--json"),
    ("update-agent-context.sh", "claude"),
]
SCRIPT_IDS = [s[0] for s in SCRIPTS]
CHECK_SCRIPT = SCRIPTS[0]

REJECTION_MESSAGE = "Unsafe branch name rejected"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _git(cwd: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=False
    )


def _run(project: Path, script: tuple[str, ...], env_extra: dict | None = None):
    """Run a helper script from the project; return the CompletedProcess."""
    env = {k: v for k, v in os.environ.items() if k != "SPECIFY_FEATURE"}
    env.update(env_extra or {})
    return subprocess.run(
        ["bash", f".specify/scripts/bash/{script[0]}", *script[1:]],
        cwd=project,
        capture_output=True,
        text=True,
        env=env,
        timeout=60,
        check=False,
    )


def _use_branch(project: Path, name: str) -> None:
    """Check out a fresh branch of the given name from the initial commit."""
    (project / "PWNED").unlink(missing_ok=True)
    _git(project, "checkout", "-q", "-f", "base")  # leave any previous branch
    result = _git(project, "checkout", "-q", "-B", name)
    if result.returncode != 0:
        pytest.skip(f"git refused the branch name {name!r}")


def _assert_rejected(project: Path, result: subprocess.CompletedProcess) -> None:
    output = result.stdout + result.stderr
    assert result.returncode != 0, f"script did not fail:\n{output}"
    assert REJECTION_MESSAGE in output, f"missing rejection message:\n{output}"
    assert not (project / "PWNED").exists(), "injected command EXECUTED"


def _assert_works(result: subprocess.CompletedProcess) -> None:
    output = result.stdout + result.stderr
    assert result.returncode == 0, f"script failed:\n{output}"
    assert '"FEATURE_DIR"' in result.stdout, f"unexpected output:\n{output}"


# ---------------------------------------------------------------------------
# Fixture: a throwaway git project that contains the scripts under test
# ---------------------------------------------------------------------------
@pytest.fixture
def project(tmp_path: Path) -> Path:
    proj = tmp_path / "project"
    (proj / ".specify" / "templates").mkdir(parents=True)
    (proj / "specs" / "001-x").mkdir(parents=True)

    shutil.copytree(REPO / "scripts", proj / ".specify" / "scripts")
    for template in (REPO / "templates").glob("*.md"):
        shutil.copy(template, proj / ".specify" / "templates" / template.name)
    for name in ("plan", "spec", "tasks"):
        (proj / "specs" / "001-x" / f"{name}.md").write_text(f"# {name}\n")

    _git(proj, "init", "-q", ".")
    _git(proj, "config", "user.email", "test@example.invalid")
    _git(proj, "config", "user.name", "test")
    _git(proj, "add", "-A")
    _git(proj, "commit", "-qm", "init")
    # Start every test from a known base branch so `checkout -` works.
    _git(proj, "checkout", "-q", "-B", "base")
    return proj


# ---------------------------------------------------------------------------
# Negative tests: attacks must be blocked
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("script", SCRIPTS, ids=SCRIPT_IDS)
def test_original_payload_is_rejected(project: Path, script: tuple[str, ...]):
    _use_branch(project, PAYLOAD)
    _assert_rejected(project, _run(project, script))


@pytest.mark.parametrize("branch", EXTRA_PAYLOADS)
def test_other_injection_forms_are_rejected(project: Path, branch: str):
    _use_branch(project, branch)
    _assert_rejected(project, _run(project, CHECK_SCRIPT))


def test_malicious_specify_feature_is_rejected(project: Path):
    _use_branch(project, "001-x")
    result = _run(project, CHECK_SCRIPT, {"SPECIFY_FEATURE": PAYLOAD})
    _assert_rejected(project, result)


# ---------------------------------------------------------------------------
# Positive tests: legitimate use must keep working
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("script", SCRIPTS, ids=SCRIPT_IDS)
def test_valid_branch_works_with_all_scripts(project: Path, script: tuple[str, ...]):
    _use_branch(project, "001-x")
    result = _run(project, script)
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.mark.parametrize("branch", VALID_NAMES)
def test_valid_name_variants_are_accepted(project: Path, branch: str):
    _use_branch(project, branch)
    _assert_works(_run(project, CHECK_SCRIPT))


def test_valid_specify_feature_is_accepted(project: Path):
    _use_branch(project, "001-x")
    _assert_works(_run(project, CHECK_SCRIPT, {"SPECIFY_FEATURE": "001-x"}))


def test_non_feature_branch_keeps_normal_error(project: Path):
    _use_branch(project, "develop")
    result = _run(project, CHECK_SCRIPT)
    output = result.stdout + result.stderr
    assert result.returncode != 0
    assert "Not on a feature branch" in output
    assert "Unsafe" not in output


def test_folder_without_git_still_works(project: Path, tmp_path: Path):
    nogit = tmp_path / "nogit"
    nogit.mkdir()
    shutil.copytree(project / ".specify", nogit / ".specify")
    shutil.copytree(project / "specs", nogit / "specs")
    _assert_works(_run(nogit, CHECK_SCRIPT))


# ---------------------------------------------------------------------------
# Static test
# ---------------------------------------------------------------------------
def test_no_eval_in_bash_scripts():
    """`eval` used as a command (line start or after ; | & ( ) is forbidden.

    Mentions of the word inside comments are ignored.
    """
    eval_re = re.compile(r"(^|[;|&(])\s*eval\s")
    hits = [
        f"{path.name}:{number}: {line.strip()}"
        for path in sorted(BASH_DIR.glob("*.sh"))
        for number, line in enumerate(path.read_text().splitlines(), start=1)
        if eval_re.search(line)
    ]
    assert not hits, "eval found:\n" + "\n".join(hits)
