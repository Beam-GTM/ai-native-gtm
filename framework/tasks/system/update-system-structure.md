<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.245858Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.307941Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Update System Structure Map
**Task ID**: update-system-structure  
**Category**: system-maintenance  
**Priority**: CRITICAL  
**Execution**: Automated with validation  
**Dependencies**: File system access, SYSTEM-STRUCTURE.md

## Purpose
Maintain accurate and current system structure documentation by automatically updating SYSTEM-STRUCTURE.md with real-time file counts, directory trees, and statistics. Critical for system navigation and orchestrator awareness.

## When to Use
- After structural changes to the system
- During system synchronization
- Before releases or milestones
- When indices show discrepancies
- Part of system-sync super task
- Weekly maintenance schedule

## Prerequisites
- Read/write access to SYSTEM-STRUCTURE.md
- File system traversal permissions
- Backup of current structure map

## Task Execution Steps

### Step 1: Backup Current Structure
```bash
# Create timestamped backup
cp SYSTEM-STRUCTURE.md "workspace/backups/SYSTEM-STRUCTURE-$(date +%Y%m%d-%H%M%S).md"
```

### Step 2: Collect System Metrics
```yaml
metrics_to_collect:
  file_counts:
    - total_files: find . -type f | wc -l
    - markdown_files: find . -name "*.md" | wc -l
    - yaml_files: find . -name "*.yaml" | wc -l
    - other_files: calculated from total - (md + yaml)
    
  directory_counts:
    - total_directories: find . -type d | wc -l
    - depth_levels: find . -type d | awk -F/ '{print NF}' | sort -n | tail -1
    
  category_counts:
    - agents: count files in operations/agents/**/*.md
    - workflows: count files in operations/workflows/*.md + framework/workflows/*.md
    - tasks: count files in framework/tasks/*/*.md
    - engineering_rules: count files in framework/engineeringrules/**/*.md
    - features_active: count directories in workspace/features/active/
    - features_completed: count directories in workspace/features/completed/
    - knowledge_files: count files in workspace/knowledge/**/*
```

### Step 3: Generate Directory Tree
```yaml
tree_generation:
  root: 
  
  include_patterns:
    - "*.md"
    - "*.yaml"
    - "INDEX.*"
    - "CONTEXT.*"
    - "README.*"
    
  annotation_rules:
    - directories: show file count in comment
    - key_files: add description comment
    - empty_dirs: mark as (empty)
    
  depth_control:
    - full_depth: [briefing, framework, operations]
    - limited_depth_2: [workspace/features]
    - limited_depth_1: [workspace/knowledge]
```

### Step 4: Update File Statistics Section
```markdown
## File Statistics (Accurate Count)
- **Total Directories**: {count}
- **Total Files**: {total} ({md_count} .md + {yaml_count} .yaml + {other} other)
- **Markdown Files**: {md_count}
- **YAML Templates**: {yaml_count}
- **Engineering Rules**: {rule_count} active rules across 4 categories
- **Agents**: {agent_count} configured ({orchestrator} + {specialists})
- **Workflows**: {workflow_count} active ({ops} operations + {fw} framework)
- **Tasks**: {task_count} framework tasks
- **Active Features**: {active_count} (list names)
- **Completed Features**: {completed_count}
- **Archived Features**: {archived_count}
- **Knowledge Base**: {kb_count} files in workspace/knowledge/
```

### Step 5: Validate Key Navigation Points
```yaml
navigation_validation:
  entry_points:
    - orchestrator.md
    - operations/MANIFEST.md
    - SYSTEM-STRUCTURE.md
    - README.md
    
  index_files:
    - operations/INDEX.md
    - operations/agents/INDEX.md
    - operations/workflows/INDEX.md
    - framework/INDEX.md
    - framework/engineeringrules/INDEX.md
    - workspace/features/INDEX.md
    - workspace/memory/INDEX.md
    
  context_files:
    - operations/agents/core/CONTEXT.md
    - operations/agents/specialists/CONTEXT.md
    - operations/agents/coordinators/CONTEXT.md
    - operations/agents/experimental/CONTEXT.md
    - framework/CONTEXT.md
```

### Step 6: Update Engineering Rules Categories
```yaml
rule_categories:
  core-foundation:
    path: framework/engineeringrules/core-foundation/
    expected: 10 files
    
  development:
    path: framework/engineeringrules/development/
    expected: 10 files
    
  product-management:
    path: framework/engineeringrules/product-management/
    expected: 9 files
    
  system-operations:
    path: framework/engineeringrules/system-operations/
    expected: 9 files
    
  legacy:
    path: framework/engineeringrules/versions/
    check: v1-legacy/ and v2/ directories
```

### Step 7: Update Growth Monitoring
```yaml
growth_metrics:
  current:
    agents: "{count}/∞ (grows at >3 uses/week)"
    workflows: "{count}/∞ (grows at >2 uses/week)"
    tasks: "{count}/∞ (grows at >5 uses/week)"
    patterns: "{count}/∞ (extracted from 3+ features)"
    
  expansion_zones:
    - operations/agents/ - New agent categories
    - operations/workflows/ - New workflow types
    - operations/tasks/ - Task categories
    - workspace/features/patterns/ - Extracted patterns
    - workspace/memory/patterns/ - Pattern recognition
```

### Step 8: Generate Change Report
```markdown
# System Structure Update Report
**Timestamp**: {iso_timestamp}
**Previous Update**: {last_update_from_file}

## Changes Detected
### File Changes
- Files Added: {added_count}
  {list of new files}
- Files Removed: {removed_count}
  {list of removed files}
- Files Modified: {modified_count}

### Directory Changes
- Directories Added: {new_dirs}
- Directories Removed: {removed_dirs}

### Statistics Updates
- Previous Total Files: {old_total}
- Current Total Files: {new_total}
- Change: {delta} ({percentage}%)

### Key Observations
{automated observations about significant changes}
```

### Step 9: Update SYSTEM-STRUCTURE.md
```yaml
update_process:
  1. Update version number (increment patch)
  2. Update timestamp to current UTC
  3. Replace directory tree section
  4. Update file statistics section
  5. Update navigation points if changed
  6. Update growth monitoring metrics
  7. Preserve all other sections unchanged
  8. Add change summary comment at end of file
```

### Step 10: Validation
```yaml
post_update_validation:
  structure_checks:
    - All listed paths exist
    - No unlisted significant files
    - Statistics match actual counts
    - Version incremented correctly
    
  format_checks:
    - Markdown formatting valid
    - Tree structure properly indented
    - Links functional
    - No duplicate entries
    
  consistency_checks:
    - Counts match across sections
    - Categories properly grouped
    - Timestamps updated
    - Change report generated
```

## Error Handling

### Recovery Procedures
- **File Not Found**: Log and continue, note in report
- **Permission Denied**: Alert user, skip that section
- **Malformed Content**: Backup and attempt repair
- **Write Failure**: Restore from backup, alert user

### Rollback Process
```bash
# If any critical error occurs
if [ $ERROR_CRITICAL ]; then
  cp "workspace/backups/SYSTEM-STRUCTURE-{backup_timestamp}.md" SYSTEM-STRUCTURE.md
  echo "ERROR: Update failed, restored from backup"
  exit 1
fi
```

## Performance Targets
- Discovery: <3 seconds
- Tree Generation: <5 seconds
- Statistics Calculation: <2 seconds
- File Update: <1 second
- **Total**: <11 seconds

## Success Criteria
- [ ] All files and directories accurately counted
- [ ] Directory tree matches actual structure
- [ ] Statistics 100% accurate
- [ ] Navigation points verified
- [ ] Version number incremented
- [ ] Timestamp updated
- [ ] Change report generated
- [ ] Backup created successfully
- [ ] No errors during execution

## Output Locations
- **Updated File**: SYSTEM-STRUCTURE.md
- **Backup**: workspace/backups/SYSTEM-STRUCTURE-{timestamp}.md
- **Change Report**: workspace/data-output/system-reports/structure-update-{timestamp}.md

## Integration Points
- Called by: system-sync.md (super task)
- Calls: None (leaf task)
- Triggers: operations/INDEX.md update recommended after

## Usage Examples
```bash
# Direct execution
*task update-system-structure

# Dry run mode
*task update-system-structure --dry-run

# With detailed logging
*task update-system-structure --verbose

# As part of system sync
*task system-sync  # Includes this task
```

## Maintenance Notes
- Review monthly for new file types to track
- Update expected counts when system grows
- Consider caching for large systems
- Monitor execution time for optimization needs

## Related Tasks
- framework/tasks/system/update-all-indices.md
- framework/tasks/system/system-sync.md
- framework/tasks/validation/validate-dependencies.md

---
**Remember**: System structure accuracy is critical for navigation and awareness. Always backup before updates!