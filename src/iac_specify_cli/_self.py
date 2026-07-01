"""Self-management commands for iac-specify-cli: check and upgrade."""
from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys

import typer

from ._console import console

self_app = typer.Typer(
    name="self",
    help="Manage the iac-specify CLI itself: check for updates and upgrade in place.",
    add_completion=False,
)

# PyPI package name
_PKG_NAME = "iac-specify-cli"
# Source repo for git-based installs
_GIT_SOURCE = "git+https://github.com/IBM/iac-spec-kit.git"


def _render_argv(argv: list[str]) -> str:
    return subprocess.list2cmdline(argv) if os.name == "nt" else shlex.join(argv)


def _detect_install_method() -> str:
    """Return 'uv-tool', 'pipx', 'uvx-ephemeral', 'source', or 'unknown'."""
    argv0 = sys.argv[0]

    # Check uv tool path patterns
    uv_patterns = [
        os.path.expanduser("~/.local/share/uv/tools/iac-specify-cli/"),
        os.path.expandvars("%LOCALAPPDATA%\\uv\\tools\\iac-specify-cli\\"),
    ]
    for pattern in uv_patterns:
        if pattern and argv0.startswith(pattern):
            return "uv-tool"

    # Check pipx
    pipx_patterns = [
        os.path.expanduser("~/.local/pipx/venvs/iac-specify-cli/"),
        os.path.expandvars("%LOCALAPPDATA%\\pipx\\venvs\\iac-specify-cli\\"),
    ]
    for pattern in pipx_patterns:
        if pattern and argv0.startswith(pattern):
            return "pipx"

    # uvx ephemeral
    if ".cache/uv/archive" in argv0 or "archive-v0" in argv0:
        return "uvx-ephemeral"

    # Try registry lookup as fallback
    if shutil.which("uv"):
        try:
            result = subprocess.run(
                ["uv", "tool", "list"], capture_output=True, text=True, timeout=5, check=False
            )
            if result.returncode == 0 and "iac-specify-cli" in result.stdout:
                return "uv-tool"
        except Exception:
            pass

    if shutil.which("pipx"):
        try:
            result = subprocess.run(
                ["pipx", "list", "--json"], capture_output=True, text=True, timeout=5, check=False
            )
            if result.returncode == 0 and "iac-specify-cli" in result.stdout:
                return "pipx"
        except Exception:
            pass

    return "unknown"


def _build_upgrade_argv(method: str) -> list[str] | None:
    """Build the installer argv for an upgradable method."""
    if method == "uv-tool":
        uv = shutil.which("uv")
        if uv:
            return [uv, "tool", "install", _PKG_NAME, "--force"]
    if method == "pipx":
        pipx = shutil.which("pipx")
        if pipx:
            return [pipx, "install", "--force", _PKG_NAME]
    return None


@self_app.command("check")
def self_check() -> None:
    """Check whether a newer iac-specify-cli release is available. Read-only."""
    from ._version import get_speckit_version, _fetch_latest_release_tag, _is_newer

    installed = get_speckit_version()
    tag, failure = _fetch_latest_release_tag()

    if failure:
        console.print(f"Installed: {installed}")
        console.print(f"[yellow]Could not check latest release:[/yellow] {failure}")
        return

    latest_display = tag.lstrip("vV")
    if _is_newer(tag, installed):
        console.print(f"[green]Update available:[/green] {installed} → {latest_display}")
        console.print("\nTo upgrade:")
        console.print("  iac-specify self upgrade")
        console.print("\nManual fallback:")
        console.print(f"  uv tool install {_PKG_NAME} --force")
        console.print(f"  pipx install --force {_PKG_NAME}")
    else:
        console.print(f"[green]Up to date:[/green] {installed}")


@self_app.command("upgrade")
def self_upgrade(
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Print what would be run without executing it.",
    ),
) -> None:
    """Upgrade iac-specify-cli to the latest release.

    Supports uv tool and pipx installs. For uvx (ephemeral) or source checkouts,
    prints guidance instead.

    Exit codes: 0 success, 1 failure, 3 installer not found.
    """
    from ._version import get_speckit_version, _fetch_latest_release_tag, _is_newer

    installed = get_speckit_version()
    method = _detect_install_method()

    if method in ("uvx-ephemeral",):
        console.print(
            "Running via uvx (ephemeral) — next uvx invocation already resolves to latest."
        )
        return

    if method == "unknown":
        console.print("Could not identify install method. Run one of:")
        console.print(f"  uv tool install {_PKG_NAME} --force")
        console.print(f"  pipx install --force {_PKG_NAME}")
        return

    # Fetch latest
    tag, failure = _fetch_latest_release_tag()
    if failure:
        console.print(f"[red]Could not resolve latest release:[/red] {failure}")
        raise typer.Exit(1)

    latest_display = tag.lstrip("vV")

    if not _is_newer(tag, installed) and not dry_run:
        console.print(f"[green]Already on latest release:[/green] {installed}")
        return

    argv = _build_upgrade_argv(method)
    if argv is None:
        installer_name = "uv" if method == "uv-tool" else "pipx"
        console.print(
            f"[red]Installer '{installer_name}' not found on PATH.[/red] "
            "Reinstall it and retry."
        )
        raise typer.Exit(3)

    if dry_run:
        if not _is_newer(tag, installed):
            console.print(f"[green]Already on latest release:[/green] {installed}")
            console.print(f"Dry run — would execute: {_render_argv(argv)}")
            console.print(f"  (No upgrade needed — latest release is {latest_display})")
            return
        console.print(f"Dry run — would execute: {_render_argv(argv)}")
        console.print(f"  Current: {installed}")
        console.print(f"  Target:  {latest_display}")
        return

    console.print(f"Upgrading iac-specify-cli {installed} → {latest_display} via {method}")
    console.print(f"Running: {_render_argv(argv)}")

    try:
        result = subprocess.run(argv, shell=False, check=False)
        if result.returncode != 0:
            console.print(f"[red]Upgrade failed (exit {result.returncode}).[/red]")
            raise typer.Exit(result.returncode)
    except FileNotFoundError:
        console.print(f"[red]Installer not found:[/red] {argv[0]}")
        raise typer.Exit(3)

    console.print("[green]✓[/green] Upgrade complete.")
