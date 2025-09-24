# generate-template-CLEAN.ps1
# CLEAN WORKING VERSION - Simpler approach

param(
    [string]$SourcePath = "C:\Users\dsber\Code\Nexus-v2\nexus-base",
    [string]$TargetPath = "C:\Users\dsber\Code\Nexus-v2\nexus-template-clean",
    [switch]$SkipBackup
)

$ErrorActionPreference = "Stop"
$TIMESTAMP = Get-Date -Format "yyyyMMdd_HHmmss"

Write-Host "======================================================"
Write-Host "       NEXUS TEMPLATE GENERATION - CLEAN VERSION     "
Write-Host "======================================================" -ForegroundColor Cyan

# Safety check
if ($SourcePath -eq $TargetPath) {
    Write-Host "[ERROR] Source and target paths are the same!" -ForegroundColor Red
    exit 1
}

# Backup if needed
if (-not $SkipBackup -and (Test-Path $TargetPath)) {
    Write-Host "Creating safety backup..." -ForegroundColor Yellow
    $backupPath = "$TargetPath-backup-$TIMESTAMP"
    Move-Item -Path $TargetPath -Destination $backupPath -Force
    Write-Host "[OK] Backup created" -ForegroundColor Green
}

# Copy source to target
Write-Host "Copying source to target..." -ForegroundColor Yellow
Copy-Item -Path $SourcePath -Destination $TargetPath -Recurse -Force
Write-Host "[OK] Source copied" -ForegroundColor Green

# Clean features
Write-Host "Cleaning features..." -ForegroundColor Yellow
$activePath = Join-Path $TargetPath "workspace\features\active"
if (Test-Path $activePath) {
    Get-ChildItem $activePath -Directory | Where-Object {
        $_.Name -ne "learn-platform"
    } | Remove-Item -Recurse -Force
}

# Clean completed/archived
$completedPath = Join-Path $TargetPath "workspace\features\completed"
$archivedPath = Join-Path $TargetPath "workspace\features\archive"
if (Test-Path $completedPath) { 
    Get-ChildItem $completedPath | Remove-Item -Recurse -Force 
}
if (Test-Path $archivedPath) { 
    Get-ChildItem $archivedPath | Remove-Item -Recurse -Force 
}
Write-Host "[OK] Features cleaned" -ForegroundColor Green

# Clean memory
Write-Host "Cleaning memory..." -ForegroundColor Yellow
$memoryPath = Join-Path $TargetPath "workspace\memory"
if (Test-Path $memoryPath) {
    Get-ChildItem $memoryPath -Exclude "INDEX.md","project-memory.md" | Remove-Item -Recurse -Force
    
    # Create clean core-learnings.md
    $coreLearningsmPath = Join-Path $memoryPath "core-learnings.md"
    @"
# CORE LEARNINGS | TEMPLATE | 0 Patterns

**Status**: Clean Template
**Patterns**: 0 recorded

## Template State
This is a clean template. Your learnings will be captured here.
"@ | Set-Content -Path $coreLearningsmPath
}

# Clean knowledge
$knowledgePath = Join-Path $TargetPath "workspace\knowledge"
if (Test-Path $knowledgePath) {
    Get-ChildItem $knowledgePath | Remove-Item -Recurse -Force
    
    # Create consolidated-learnings.md
    $consolidatedPath = Join-Path $knowledgePath "consolidated-learnings.md"
    @"
# Consolidated Learnings | Template

**Status**: Clean Template
Your learnings will be consolidated here.
"@ | Set-Content -Path $consolidatedPath
}

# Remove nexus-base folder
$nexusBasePath = Join-Path $TargetPath "nexus-base"
if (Test-Path $nexusBasePath) {
    Remove-Item $nexusBasePath -Recurse -Force
}
Write-Host "[OK] Memory cleaned" -ForegroundColor Green

# Fix critical files
Write-Host "Fixing critical files..." -ForegroundColor Yellow

# Add template markers to CRITICAL-DIRECTIVES.md
$directivesPath = Join-Path $TargetPath "framework\CRITICAL-DIRECTIVES.md"
if (Test-Path $directivesPath) {
    $content = Get-Content -Path $directivesPath -Raw
    $templateHeader = @"
# CRITICAL DIRECTIVES | MANDATORY LOADING
**THIS FILE MUST BE LOADED BY EVERY AGENT DURING ACTIVATION**
**Version**: 1.0.0-template
**Status**: TEMPLATE_STATE_ACTIVE
**Severity**: MAXIMUM CRITICAL

<!-- TEMPLATE-STATE-ACTIVE -->
<!-- This marker indicates this is a fresh template requiring setup -->
"@
    $replacement = $templateHeader + "`n`n"
    $newContent = $content -replace "^# CRITICAL DIRECTIVES[^#]*", $replacement
    Set-Content -Path $directivesPath -Value $newContent
}

# Reset project memory
$projectMemoryPath = Join-Path $TargetPath "workspace\memory\project-memory.md"
@"
# PROJECT MEMORY | Template State | Entries: 0/30
**PATTERN CHECK**: PENDING (triggers at 5 entries)

## Template State - Ready for Your Journey

This is a clean Nexus template. Your journey starts here.
"@ | Set-Content -Path $projectMemoryPath

# Create project brief from template
$briefingPath = Join-Path $TargetPath "briefing"
$templateBriefPath = Join-Path $briefingPath "project-brief-template.md"
$projectBriefPath = Join-Path $briefingPath "project-brief.md"

if (Test-Path $templateBriefPath) {
    Copy-Item -Path $templateBriefPath -Destination $projectBriefPath -Force
}

# If no template exists, create a proper AI-oriented brief
if (-not (Test-Path $projectBriefPath)) {
    @"
# PROJECT BRIEF | NEXUS TEMPLATE

## Project Identity
**Name**: Nexus Template System
**Type**: Language-Based Operating System Template
**Status**: Clean Template - Ready for Customization

## Core Purpose
Transform natural language into automated workflows through an intelligent agent-based system.

## Key Components
- **Framework**: Core system architecture and rules
- **Operations**: Agents and workflows for execution
- **Workspace**: Active development and memory
- **Briefing**: Project context and documentation

## Template Features
- Pre-configured learn-platform feature for onboarding
- Clean memory system ready for pattern capture
- Orchestrator with intelligent menu system
- Template detection for guided setup

## Success Metrics
- User successfully personalizes template
- First feature created successfully
- System patterns begin accumulating
- Workflows execute without errors
"@ | Set-Content -Path $projectBriefPath
}

# Fix CLAUDE.md
$claudeMdPath = Join-Path $TargetPath "CLAUDE.md"
@"
ALWAYS LOAD operations\agents\core\orchestrator.md
even if I say hi or whatever I say
"@ | Set-Content -Path $claudeMdPath

# Clean .claude folder
$claudeFolderPath = Join-Path $TargetPath ".claude"
if (Test-Path $claudeFolderPath) {
    # Remove everything except settings.local.json
    Get-ChildItem $claudeFolderPath -Exclude "settings.local.json" | Remove-Item -Recurse -Force
    
    # Create a CLEAN settings.local.json (don't try to fix the existing one)
    $settingsLocalPath = Join-Path $claudeFolderPath "settings.local.json"
    $cleanSettings = @'
{
  "permissions": {
    "allow": [
      "WebFetch(domain:context7.com)",
      "Bash(mcp list:*)",
      "WebFetch(domain:github.com)",
      "Bash(for cmd in \"help\" \"agent\" \"workflow\" \"task\" \"status\" \"generate-system\" \"menu-agents\" \"menu-workflows\")",
      "Bash(do echo -n \"$cmd: \")",
      "Bash(grep:*)",
      "Bash(done)",
      "Bash(dir:*)",
      "Bash(python:*)",
      "Bash(mkdir:*)",
      "Bash(touch:*)",
      "Bash(cp:*)",
      "Bash(powershell:*)",
      "Bash(find:*)",
      "Bash(rm:*)",
      "Bash(test:*)",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(git add:*)",
      "Bash(git mv:*)",
      "Bash(date:*)",
      "Read(.claude/**)",
      "Write(.claude/**)",
      "Edit(.claude/**)"
    ],
    "deny": [],
    "ask": [],
    "additionalDirectories": []
  }
}
'@
    Set-Content -Path $settingsLocalPath -Value $cleanSettings
    
    # Add README
    @"
# Claude Code Configuration

This folder will contain your Claude Code configuration when you set it up.

## Coming Soon

The following Claude Code features will be implemented:
- **Agents**: Custom AI agents for specific tasks
- **Commands**: Slash commands for quick actions  
- **Hooks**: Event-driven automation triggers
- **Tools**: Custom tool integrations
- **Workflows**: Multi-step automation sequences

## Getting Started

1. Install Claude Code extension
2. Configure your settings
3. Start building your custom automation

Your Nexus system will integrate seamlessly with Claude Code features as you add them.
"@ | Set-Content -Path (Join-Path $claudeFolderPath "README.md")
}

# Move SYSTEM-STRUCTURE.md
$systemStructurePath = Join-Path $TargetPath "SYSTEM-STRUCTURE.md"
$frameworkPath = Join-Path $TargetPath "framework"
if ((Test-Path $systemStructurePath) -and (Test-Path $frameworkPath)) {
    Move-Item -Path $systemStructurePath -Destination (Join-Path $frameworkPath "SYSTEM-STRUCTURE.md") -Force
}

# Fix ALL nexus-base references in ALL files
Write-Host "Removing nexus-base references from all files..." -ForegroundColor Yellow
$files = Get-ChildItem -Path $TargetPath -Recurse -File -Include "*.md", "*.yaml", "*.yml", "*.json", "*.sh", "*.ps1"
foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    if ($content -match "nexus-base") {
        # Replace all variations of nexus-base
        $content = $content -replace "nexus-base/", ""
        $content = $content -replace "nexus-base\\", ""
        $content = $content -replace "nexus-base ", " "  # nexus-base followed by space
        $content = $content -replace "nexus-base\.", "."  # nexus-base followed by dot
        $content = $content -replace "\bnexus-base\b", "template"  # standalone nexus-base word
        Set-Content -Path $file.FullName -Value $content
        Write-Host "   Fixed: $($file.Name)" -ForegroundColor Gray
    }
}

# Also remove backup files that might contain references
$backupFiles = @(
    "framework\templates\agent.yaml.backup.2025-08-26",
    "workspace\backups"
)
foreach ($backup in $backupFiles) {
    $backupPath = Join-Path $TargetPath $backup
    if (Test-Path $backupPath) {
        Remove-Item -Path $backupPath -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "   Removed backup: $backup" -ForegroundColor Gray
    }
}

Write-Host "[OK] Critical files fixed" -ForegroundColor Green

# Ensure system-setup task exists (should be copied from source)
$systemSetupPath = Join-Path $TargetPath "framework\tasks\system\system-setup.md"
if (-not (Test-Path $systemSetupPath)) {
    Write-Host "   Warning: system-setup.md not found in template" -ForegroundColor Yellow
}

# Update indices
Write-Host "Updating indices..." -ForegroundColor Yellow

$featuresIndexPath = Join-Path $TargetPath "workspace\features\INDEX.md"
@"
# Workspace Features Index - CLEAN TEMPLATE

metadata:
  template_version: "4.0"
  state: "clean"

feature_registry:
  active:
    - feature_id: "learn-platform-001"
      name: "learn-platform"
      priority: "high"
      status: "active"
      progress: 0
      description: "Beginner guide to Nexus - Your starting point"
  
  completed: []
  archived: []  
  patterns: []
"@ | Set-Content -Path $featuresIndexPath

# Create context folder
$contextPath = Join-Path $TargetPath "briefing\context"
if (-not (Test-Path $contextPath)) {
    New-Item -ItemType Directory -Path $contextPath -Force | Out-Null
    @"
# Project Context Folder

Place your project-specific documentation here.
"@ | Set-Content -Path (Join-Path $contextPath "README.md")
}

Write-Host "[OK] Indices updated" -ForegroundColor Green

# Final message
Write-Host ""
Write-Host "======================================================"
Write-Host "           TEMPLATE GENERATION COMPLETE!              "
Write-Host "======================================================"
Write-Host "Template is ready at: $TargetPath" -ForegroundColor Green
Write-Host ""
Write-Host "This template will:" -ForegroundColor Cyan
Write-Host "  - Load without errors"
Write-Host "  - Show proper orchestrator menu"
Write-Host "  - Detect template state correctly"
Write-Host "  - Have project brief ready"
Write-Host "  - Include learn-platform feature"
Write-Host "  - Have clean memory system"
Write-Host ""

$completionTime = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
Write-Host "Generation complete at: $completionTime" -ForegroundColor Gray