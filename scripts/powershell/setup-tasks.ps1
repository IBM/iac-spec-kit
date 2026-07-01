#!/usr/bin/env pwsh

[CmdletBinding()]
param(
    [switch]$Json,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

if ($Help) {
    Write-Output "Usage: setup-tasks.ps1 [-Json] [-Help]"
    exit 0
}

# Source common functions
. "$PSScriptRoot/common.ps1"

# --- Stubs for functions not present in common.ps1 ---

function Format-IacCommand {
    param([string]$CommandName)
    return "/iac.$CommandName"
}

function Resolve-IacTemplate {
    param([string]$TemplateName, [string]$RepoRoot)
    $templatePath = Join-Path $RepoRoot ".specify/templates/$TemplateName.md"
    if (Test-Path -LiteralPath $templatePath -PathType Leaf) {
        return $templatePath
    }
    return $null
}

# --- End stubs ---

# Get feature paths
$paths = Get-FeaturePathsEnv

if (-not (Test-Path $paths.IMPL_PLAN -PathType Leaf)) {
    [Console]::Error.WriteLine("ERROR: plan.md not found in $($paths.FEATURE_DIR)")
    $planCommand = Format-IacCommand -CommandName 'plan'
    [Console]::Error.WriteLine("Run $planCommand first to create the implementation plan.")
    exit 1
}

if (-not (Test-Path $paths.FEATURE_SPEC -PathType Leaf)) {
    [Console]::Error.WriteLine("ERROR: spec.md not found in $($paths.FEATURE_DIR)")
    $specifyCommand = Format-IacCommand -CommandName 'specify'
    [Console]::Error.WriteLine("Run $specifyCommand first to create the feature structure.")
    exit 1
}

# Build available docs list (uses path fields from this project's Get-FeaturePathsEnv)
$docs = @()
if (Test-Path $paths.RESEARCH)     { $docs += 'research.md' }
if (Test-Path $paths.MODULES)      { $docs += 'modules.md' }
if (Test-Path $paths.ARCHITECTURE) { $docs += 'architecture.md' }
if (Test-Path $paths.QUICKSTART)   { $docs += 'quickstart.md' }

# Resolve tasks template
$tasksTemplate = Resolve-IacTemplate -TemplateName 'tasks-template' -RepoRoot $paths.REPO_ROOT
if (-not $tasksTemplate -or -not (Test-Path -LiteralPath $tasksTemplate -PathType Leaf)) {
    $expectedCoreTemplate = Join-Path $paths.REPO_ROOT '.specify/templates/tasks-template.md'
    [Console]::Error.WriteLine("ERROR: Tasks template not found for repository root: $($paths.REPO_ROOT)")
    [Console]::Error.WriteLine("Expected template location: $expectedCoreTemplate")
    [Console]::Error.WriteLine("Add an override at .specify/templates/overrides/tasks-template.md, or restore .specify/templates/tasks-template.md.")
    exit 1
}
$tasksTemplate = (Resolve-Path -LiteralPath $tasksTemplate).Path

# Output results
if ($Json) {
    [PSCustomObject]@{
        FEATURE_DIR    = $paths.FEATURE_DIR
        AVAILABLE_DOCS = $docs
        TASKS_TEMPLATE = $tasksTemplate
    } | ConvertTo-Json -Compress
} else {
    Write-Output "FEATURE_DIR: $($paths.FEATURE_DIR)"
    Write-Output "TASKS_TEMPLATE: $(if ($tasksTemplate) { $tasksTemplate } else { 'not found' })"
    Write-Output "AVAILABLE_DOCS:"
    Test-FileExists -Path $paths.RESEARCH     -Description 'research.md'     | Out-Null
    Test-FileExists -Path $paths.MODULES      -Description 'modules.md'      | Out-Null
    Test-FileExists -Path $paths.ARCHITECTURE -Description 'architecture.md' | Out-Null
    Test-FileExists -Path $paths.QUICKSTART   -Description 'quickstart.md'   | Out-Null
}
