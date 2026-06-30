#!/usr/bin/env bash

set -e

# Parse command line arguments
JSON_MODE=false

for arg in "$@"; do
    case "$arg" in
        --json) JSON_MODE=true ;;
        --help|-h)
            echo "Usage: $0 [--json]"
            echo "  --json    Output results in JSON format"
            echo "  --help    Show this help message"
            exit 0
            ;;
        *) echo "ERROR: Unknown option '$arg'" >&2; exit 1 ;;
    esac
done

# Source common functions
SCRIPT_DIR="$(CDPATH="" cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# --- Stubs for functions not present in common.sh ---

# Format the iac.* command name for error messages
format_iac_command() {
    local cmd="$1"
    echo "/iac.$cmd"
}

# Check whether jq is available
has_jq() {
    command -v jq >/dev/null 2>&1
}

# Escape a string for JSON (minimal: backslash and double-quote)
json_escape() {
    local s="$1"
    s="${s//\\/\\\\}"
    s="${s//\"/\\\"}"
    echo "$s"
}

# Resolve the tasks template from the .specify/templates directory
resolve_template() {
    local template_name="$1"
    local repo_root="$2"
    local template_path="$repo_root/.specify/templates/${template_name}.md"
    if [[ -f "$template_path" ]]; then
        echo "$template_path"
    fi
}

# --- End stubs ---

# Get feature paths
eval $(get_feature_paths)

# Validate required files
if [[ ! -f "$IMPL_PLAN" ]]; then
    echo "ERROR: plan.md not found in $FEATURE_DIR" >&2
    echo "Run $(format_iac_command plan) first to create the implementation plan." >&2
    exit 1
fi

if [[ ! -f "$FEATURE_SPEC" ]]; then
    echo "ERROR: spec.md not found in $FEATURE_DIR" >&2
    echo "Run $(format_iac_command specify) first to create the feature structure." >&2
    exit 1
fi

# Build available docs list (uses variable names from this project's common.sh)
docs=()
[[ -f "$RESEARCH" ]]      && docs+=("research.md")
[[ -f "$MODULES" ]]       && docs+=("modules.md")
[[ -f "$ARCHITECTURE" ]]  && docs+=("architecture.md")
[[ -f "$QUICKSTART" ]]    && docs+=("quickstart.md")

# Resolve tasks template
TASKS_TEMPLATE=$(resolve_template "tasks-template" "$REPO_ROOT") || true
if [[ -z "$TASKS_TEMPLATE" ]] || [[ ! -f "$TASKS_TEMPLATE" ]]; then
    echo "ERROR: Could not resolve required tasks-template for $REPO_ROOT" >&2
    echo "Template 'tasks-template' was not found. Add an override at .specify/templates/overrides/tasks-template.md, or restore the core .specify/templates/tasks-template.md template." >&2
    exit 1
fi

# Output results
if $JSON_MODE; then
    if has_jq; then
        if [[ ${#docs[@]} -eq 0 ]]; then
            json_docs="[]"
        else
            json_docs=$(printf '%s\n' "${docs[@]}" | jq -R . | jq -s .)
        fi
        jq -cn \
            --arg feature_dir "$FEATURE_DIR" \
            --argjson docs "$json_docs" \
            --arg tasks_template "${TASKS_TEMPLATE:-}" \
            '{FEATURE_DIR:$feature_dir,AVAILABLE_DOCS:$docs,TASKS_TEMPLATE:$tasks_template}'
    else
        if [[ ${#docs[@]} -eq 0 ]]; then
            json_docs="[]"
        else
            json_docs=$(for d in "${docs[@]}"; do printf '"%s",' "$(json_escape "$d")"; done)
            json_docs="[${json_docs%,}]"
        fi
        printf '{"FEATURE_DIR":"%s","AVAILABLE_DOCS":%s,"TASKS_TEMPLATE":"%s"}\n' \
            "$(json_escape "$FEATURE_DIR")" "$json_docs" "$(json_escape "${TASKS_TEMPLATE:-}")"
    fi
else
    echo "FEATURE_DIR: $FEATURE_DIR"
    echo "TASKS_TEMPLATE: ${TASKS_TEMPLATE:-not found}"
    echo "AVAILABLE_DOCS:"
    check_file "$RESEARCH"      "research.md"
    check_file "$MODULES"       "modules.md"
    check_file "$ARCHITECTURE"  "architecture.md"
    check_file "$QUICKSTART"    "quickstart.md"
fi
