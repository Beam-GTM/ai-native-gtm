<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.998363Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.281039Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Generate Template Task
**Purpose**: Create clean Nexus template from current system  
**Type**: System Task  
**Usage**: Template distribution and sharing  
**Script**: generate-template.ps1

## Task Overview
Generate a clean, distributable template from the current Nexus system by:
- Copying entire system structure
- Removing active features (except learn-platform)
- Cleaning memory and workspace
- Creating fresh project state
- Preparing for new user onboarding

## Usage

### Basic Template Generation
```bash
powershell -ExecutionPolicy Bypass -File "framework/tasks/system/generate-template.ps1"
```

### Custom Paths
```bash
powershell -ExecutionPolicy Bypass -File "framework/tasks/system/generate-template.ps1" -SourcePath "C:\path\to\source" -TargetPath "C:\path\to\template"
```

### Skip Backup (Faster)
```bash
powershell -ExecutionPolicy Bypass -File "framework/tasks/system/generate-template.ps1" -SkipBackup
```

## What Gets Cleaned
- **Active Features**: All except learn-platform removed
- **Completed Features**: All moved out 
- **Memory System**: Reset to fresh template state
- **Workspace**: Cleaned of project-specific content
- **Git History**: Not included (fresh repo needed)

## Output
Clean template ready for:
- Git repository creation
- Distribution to users
- GitHub publication
- Template customization

## Template Features Included
- Complete framework (tasks, workflows, templates)
- 11 specialized agents ready for extraction
- Learn platform for user onboarding
- Fresh workspace and memory system
- Project brief template ready for personalization

## Usage Patterns
- **Template Distribution**: Generate for sharing system
- **Clean Starts**: Create fresh environment
- **Backup Creation**: Safe system duplication
- **Version Release**: Prepare distribution packages

## Integration
- Used by nexus-template feature for GitHub publication
- Referenced in system-setup task for template detection
- Part of distribution workflow for Nexus sharing

---

**Generated templates are production-ready and tested for user onboarding.**