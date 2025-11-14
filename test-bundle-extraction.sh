#!/usr/bin/env bash
set -euo pipefail

# Script to build bundle and extract to timestamped test directories
# Usage: ./test-bundle-extraction.sh

echo "Step 1: Building bundle with local-build-mac.sh..."
./local-build-mac.sh

# Get the version from pyproject.toml
VERSION=$(grep '^version = ' pyproject.toml | sed -E 's/^version = "(.+)"$/v\1/')
echo "Bundle built for version: $VERSION"

# Generate timestamp prefix (DDMM format)
TIMESTAMP=$(date +"%d%m")
echo ""
echo "Using timestamp prefix: $TIMESTAMP"

# Create base temp directory
BASE_DIR="/tmp/${TIMESTAMP}-speckit-test"
mkdir -p "$BASE_DIR"
echo "Created base directory: $BASE_DIR"

# Find the generated zip file
ZIP_FILE=".genreleases/iac-spec-kit-template-bob-sh-${VERSION}.zip"

if [[ ! -f "$ZIP_FILE" ]]; then
    echo "Error: Expected zip file not found: $ZIP_FILE"
    echo "Available files in .genreleases/:"
    ls -la .genreleases/ || echo "Directory doesn't exist"
    exit 1
fi

echo ""
echo "Found bundle: $ZIP_FILE"

# Create test directories and extract
TEST_DIRS=("test1" "test2" "test3")

echo ""
echo "Step 2 & 3: Creating directories and extracting bundle..."
for dir in "${TEST_DIRS[@]}"; do
    TARGET_DIR="${BASE_DIR}/${dir}"
    mkdir -p "$TARGET_DIR"
    echo "  Created: $TARGET_DIR"
    
    # Extract zip to the directory
    unzip -q "$ZIP_FILE" -d "$TARGET_DIR"
    echo "  Extracted bundle to: $TARGET_DIR"
done

echo ""
echo "All done! Test directories created at:"
echo "   $BASE_DIR"
echo ""
echo "Directory structure:"
tree -L 2 "$BASE_DIR" 2>/dev/null || ls -la "$BASE_DIR"

echo ""
echo "To clean up later, run:"
echo "   rm -rf $BASE_DIR"