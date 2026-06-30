from __future__ import annotations

import os
import subprocess
import shutil
import json
from pathlib import Path
from typing import Optional, Tuple

from ._console import console, StepTracker

CLAUDE_LOCAL_PATH = Path.home() / ".claude" / "local" / "claude"


def run_command(cmd: list[str], check_return: bool = True, capture: bool = False, shell: bool = False) -> Optional[str]:
    """Run a shell command and optionally capture output."""
    if shell:
        raise ValueError("run_command() does not support shell=True; pass argv as a list")
    try:
        if capture:
            result = subprocess.run(cmd, check=check_return, capture_output=True, text=True, shell=shell)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, check=check_return, shell=shell)
            return None
    except subprocess.CalledProcessError as e:
        if check_return:
            console.print(f"[red]Error running command:[/red] {' '.join(cmd)}")
            console.print(f"[red]Exit code:[/red] {e.returncode}")
            if hasattr(e, 'stderr') and e.stderr:
                console.print(f"[red]Error output:[/red] {e.stderr}")
            raise
        return None


def check_tool(tool: str, tracker: StepTracker = None) -> bool:
    """Check if a tool is installed. Optionally update tracker.
    
    Args:
        tool: Name of the tool to check
        tracker: Optional StepTracker to update with results
        
    Returns:
        True if tool is found, False otherwise
    """
    # Special handling for Claude CLI after `claude migrate-installer`
    # The migrate-installer command REMOVES the original executable from PATH
    # and creates an alias at ~/.claude/local/claude instead
    # This path should be prioritized over other claude executables in PATH
    if tool == "claude":
        if CLAUDE_LOCAL_PATH.exists() and CLAUDE_LOCAL_PATH.is_file():
            if tracker:
                tracker.complete(tool, "available")
            return True

    if tool == "kiro-cli":
        found = shutil.which("kiro-cli") is not None or shutil.which("kiro") is not None
    elif tool == "rovodev":
        found = shutil.which("acli") is not None
    else:
        found = shutil.which(tool) is not None

    if tracker:
        if found:
            tracker.complete(tool, "available")
        else:
            tracker.error(tool, "not found")

    return found


def is_git_repo(path: Path = None) -> bool:
    """Check if the specified path is inside a git repository."""
    if path is None:
        path = Path.cwd()
    
    if not path.is_dir():
        return False

    try:
        # Use git command to check if inside a work tree
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            cwd=path,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def init_git_repo(project_path: Path, quiet: bool = False) -> Tuple[bool, Optional[str]]:
    """Initialize a git repository in the specified path.
    
    Args:
        project_path: Path to initialize git repository in
        quiet: if True suppress console output (tracker handles status)
    
    Returns:
        Tuple of (success: bool, error_message: Optional[str])
    """
    try:
        original_cwd = Path.cwd()
        os.chdir(project_path)
        if not quiet:
            console.print("[cyan]Initializing git repository...[/cyan]")
        subprocess.run(["git", "init"], check=True, capture_output=True, text=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
        subprocess.run(["git", "commit", "-m", "Initial commit from Specify template"], check=True, capture_output=True, text=True)
        if not quiet:
            console.print("[green]✓[/green] Git repository initialized")
        return True, None

    except subprocess.CalledProcessError as e:
        error_msg = f"Command: {' '.join(e.cmd)}\nExit code: {e.returncode}"
        if e.stderr:
            error_msg += f"\nError: {e.stderr.strip()}"
        elif e.stdout:
            error_msg += f"\nOutput: {e.stdout.strip()}"
        
        if not quiet:
            console.print(f"[red]Error initializing git repository:[/red] {e}")
        return False, error_msg
    finally:
        os.chdir(original_cwd)


def handle_vscode_settings(sub_item, dest_file, rel_path, verbose=False, tracker=None) -> None:
    """Handle merging or copying of .vscode/settings.json files."""
    def log(message, color="green"):
        if verbose and not tracker:
            console.print(f"[{color}]{message}[/] {rel_path}")

    try:
        with open(sub_item, 'r', encoding='utf-8') as f:
            new_settings = json.load(f)

        if dest_file.exists():
            merged = merge_json_files(dest_file, new_settings, verbose=verbose and not tracker)
            with open(dest_file, 'w', encoding='utf-8') as f:
                json.dump(merged, f, indent=4)
                f.write('\n')
            log("Merged:", "green")
        else:
            shutil.copy2(sub_item, dest_file)
            log("Copied (no existing settings.json):", "blue")

    except Exception as e:
        log(f"Warning: Could not merge, copying instead: {e}", "yellow")
        shutil.copy2(sub_item, dest_file)


def merge_json_files(existing_path: Path, new_content: dict, verbose: bool = False) -> dict:
    """Merge new JSON content into existing JSON file.

    Performs a deep merge where:
    - New keys are added
    - Existing keys are preserved unless overwritten by new content
    - Nested dictionaries are merged recursively
    - Lists and other values are replaced (not merged)

    Args:
        existing_path: Path to existing JSON file
        new_content: New JSON content to merge in
        verbose: Whether to print merge details

    Returns:
        Merged JSON content as dict
    """
    try:
        with open(existing_path, 'r', encoding='utf-8') as f:
            existing_content = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is invalid, just use new content
        return new_content

    def deep_merge(base: dict, update: dict) -> dict:
        """Recursively merge update dict into base dict."""
        result = base.copy()
        for key, value in update.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                # Recursively merge nested dictionaries
                result[key] = deep_merge(result[key], value)
            else:
                # Add new key or replace existing value
                result[key] = value
        return result

    merged = deep_merge(existing_content, new_content)

    if verbose:
        console.print(f"[cyan]Merged JSON file:[/cyan] {existing_path.name}")

    return merged
