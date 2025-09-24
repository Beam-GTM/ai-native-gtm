<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.911700Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.273979Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Structured Folder Cleanup Task
**Version**: 1.0.0
**Type**: organization-task
**Severity**: MEDIUM
**Trigger**: Manual execution or automatic via reorganization indicators

## Purpose
Intelligently analyze folder structures and reorganize when complexity thresholds are exceeded. This task provides both analysis and cleanup capabilities with smart reorganization suggestions based on folder depth, item count, and organizational patterns.

## Reorganization Indicators

### Threshold Definitions
```yaml
reorganization_thresholds:
  critical:
    items_per_folder: 20      # More than 20 items in a single folder
    folder_depth: 5            # Folders nested deeper than 5 levels
    total_items: 100           # More than 100 items in a directory tree
    indicator: "🔴 CRITICAL"
    message: "Immediate reorganization needed - structure is becoming unmanageable"
    
  warning:
    items_per_folder: 15      # 15-20 items in a folder
    folder_depth: 4            # 4-5 levels deep
    total_items: 75           # 75-100 items total
    indicator: "🟡 WARNING"
    message: "Consider reorganization - approaching complexity limits"
    
  healthy:
    items_per_folder: 10      # Less than 10 items per folder
    folder_depth: 3            # 3 levels or less
    total_items: 50           # Less than 50 items total
    indicator: "🟢 HEALTHY"
    message: "Structure is well-organized"

calculation_formula: |
  complexity_score = (items_per_folder / 10) * 0.4 + 
                    (folder_depth / 3) * 0.3 + 
                    (total_items / 50) * 0.3
  
  # Score interpretation:
  # > 2.0: Critical reorganization needed
  # 1.5-2.0: Warning - consider reorganization
  # < 1.5: Healthy structure
```

## Inline Activation Trigger

### For INDEX.md Files
```yaml
# REORGANIZATION-TRIGGER: AUTO-CHECK ON LOAD
# When any INDEX.md is loaded, this trigger activates:
# 1. Counts items in current directory
# 2. Calculates folder depth
# 3. Computes complexity score
# 4. Displays indicator if threshold exceeded
# 
# ACTIVATION: Check thresholds and display:
# <!-- REORGANIZATION-CHECK
#   Status: {indicator}
#   Items: {count}/{threshold}
#   Depth: {current}/{max}
#   Action: {message}
# -->
```

## Task Execution Steps

### Phase 1: Analysis
```yaml
analysis_steps:
  1_scan_structure:
    command: "ls -la && find . -type d -maxdepth 5 | head -50"
    purpose: "Get current structure overview"
    
  2_count_items:
    command: "find . -maxdepth 1 -type f | wc -l"
    purpose: "Count files in current directory"
    
  3_measure_depth:
    command: "find . -type d | awk -F/ '{print NF}' | sort -n | tail -1"
    purpose: "Find maximum folder depth"
    
  4_calculate_complexity:
    action: "Apply complexity formula"
    output: "Complexity score and recommendation"
```

### Phase 2: Categorization
```yaml
categorization_patterns:
  by_type:
    pattern: "Group files by extension"
    example: "*.md → docs/, *.yaml → configs/"
    
  by_purpose:
    pattern: "Group by functional area"
    example: "tasks/, workflows/, agents/"
    
  by_date:
    pattern: "Archive old items"
    example: "archive/2024/, archive/2025/"
    
  by_status:
    pattern: "Organize by completion state"
    example: "active/, completed/, archived/"
```

### Phase 3: Reorganization Actions
```yaml
reorganization_actions:
  1_create_structure:
    action: "Create new folder hierarchy"
    commands:
      - "mkdir -p {category}/{subcategory}"
      - "mkdir -p archive/{year}/{month}"
      
  2_move_files:
    action: "Relocate files to appropriate folders"
    safety: "Always create backup first"
    commands:
      - "cp -r . ../backup-{timestamp}/"
      - "mv *.md docs/"
      - "mv *.yaml configs/"
      
  3_update_references:
    action: "Update all file references"
    scope: "Check all INDEX.md and dependency files"
    
  4_validate_structure:
    action: "Ensure no broken references"
    command: "grep -r 'old_path' . | wc -l"
```

## Smart Reorganization Patterns

### Pattern 1: Feature Organization
```
features/
├── active/           # Currently working (max 5)
│   └── {feature}/    # Each with standard structure
├── completed/        # Done features (archive after 30 days)
└── patterns/         # Extracted reusable patterns
```

### Pattern 2: Document Hierarchy
```
documentation/
├── guides/           # How-to guides
├── reference/        # API/technical reference  
├── tutorials/        # Step-by-step tutorials
└── concepts/         # Conceptual explanations
```

### Pattern 3: Task Grouping
```
tasks/
├── system/          # System maintenance tasks
├── memory/          # Memory management tasks
├── validation/      # Quality validation tasks
└── organization/    # Structure organization tasks
```

## Implementation Example

### Step 1: Add Trigger to INDEX.md
```markdown
# Operations Index
<!-- REORGANIZATION-TRIGGER: AUTO-CHECK
     Thresholds: 20 items/folder, 5 depth, 100 total
     Current: Checking... -->

<!-- REORGANIZATION-CHECK
  Status: 🟡 WARNING
  Items: 18/20 (90% of threshold)
  Depth: 4/5 levels
  Score: 1.7 (Warning range)
  Action: Consider splitting workflows/ into subcategories
  Suggested structure:
  - workflows/core/ (main workflows)
  - workflows/feature/ (feature-specific)
  - workflows/utility/ (helper workflows)
-->
```

### Step 2: Execute Cleanup
```bash
# Run the cleanup task
framework/tasks/organization/structured-folder-cleanup.md

# Follow prompts for:
1. Analyze current structure
2. Review reorganization suggestions
3. Approve/modify reorganization plan
4. Execute with backup
5. Validate references
```

## Quality Gates

### Gate 1: Pre-Cleanup Validation
- [ ] Current structure analyzed
- [ ] Complexity score calculated
- [ ] Backup location confirmed
- [ ] User approval obtained

### Gate 2: Reorganization Safety
- [ ] Full backup created
- [ ] Reference map generated
- [ ] Dependency check completed
- [ ] No active processes using files

### Gate 3: Post-Cleanup Verification
- [ ] All files accounted for
- [ ] No broken references
- [ ] INDEX files updated
- [ ] Structure meets thresholds

## Automation Integration

### Close-Chat Integration
Add to close-chat workflow for automatic structure health check:
```yaml
structure_health_check:
  trigger: "On session close"
  action: "Check all active feature folders"
  threshold: "Alert if any exceed limits"
```

### System-Sync Integration
Include in system-sync for periodic cleanup:
```yaml
periodic_cleanup:
  frequency: "Weekly"
  scope: "All workspace directories"
  action: "Reorganize if complexity > 2.0"
```

## Error Handling

### Rollback Procedures
```yaml
rollback:
  trigger: "Any error during reorganization"
  steps:
    1: "Stop all operations"
    2: "Restore from backup"
    3: "Log error details"
    4: "Notify user"
```

### Common Issues
- **Circular references**: Detect and break before moving
- **Permission errors**: Check write access before starting
- **Space constraints**: Ensure sufficient disk space
- **Active file locks**: Wait for processes to complete

## Metrics and Reporting

### Success Metrics
- Complexity score reduction
- Average items per folder
- Maximum folder depth
- Reference integrity maintained

### Report Format
```markdown
## Folder Cleanup Report
**Date**: {timestamp}
**Duration**: {time}

### Before
- Complexity: {score}
- Items/folder: {count}
- Max depth: {levels}

### After  
- Complexity: {score} ↓
- Items/folder: {count} ↓
- Max depth: {levels} ↓

### Actions Taken
- Moved {n} files
- Created {n} folders
- Updated {n} references

### Health Status: 🟢 HEALTHY
```

---
*Task created: 2025-08-27*
*Trigger: Manual or automatic via reorganization indicators*