#!/usr/bin/env bash
set -euo pipefail

# Simple wrapper to call create-release-packages.sh with homebrew coreutils on Mac
# Usage: ./build-package-mac.sh [version]
#   version defaults to extracting from pyproject.toml
#
# Requires GNU coreutils on macOS (for cp --parents support):
#   brew install coreutils

# Homebrew coreutils path (adjust if installed elsewhere)
COREUTILS_PATH="/opt/homebrew/opt/coreutils/libexec/gnubin"

VERSION="${1:-}"

# Extract version from pyproject.toml if not provided
if [[ -z "$VERSION" ]]; then
  if [[ -f "pyproject.toml" ]]; then
    VERSION=$(grep '^version = ' pyproject.toml | sed -E 's/^version = "(.+)"$/v\1/')
    echo "Using version from pyproject.toml: $VERSION"
  else
    echo "Error: No version provided and pyproject.toml not found" >&2
    exit 1
  fi
fi

# Use environment variables if set, otherwise use defaults
: "${AGENTS:=bob}"
: "${SCRIPTS:=sh}"

PATH="$COREUTILS_PATH:$PATH" \
  AGENTS="$AGENTS" \
  SCRIPTS="$SCRIPTS" \
  .github/workflows/scripts/create-release-packages.sh "$VERSION"