<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.954014Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.278217Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Feature Archival Task

## Automatically move completed features to completed directory

---

## Task Definition

```yaml
task:
  id: feature-archival
  name: Archive Completed Features
  description: >-
    Identifies and moves completed features from active/ to completed/ directory,
    updates all references, and maintains system integrity during the move.
  type: maintenance
  category: feature-management
  priority: high

execution:
  trigger: 'Session closure or manual request'
  frequency: 'As needed'
  timeout: 30s
  
dependencies:
  reads:
    - workspace/features/active/*/progress.md
    - workspace/features/active/*/quality-gates.md
    - workspace/features/INDEX.md
  
  writes:
    - workspace/features/completed/
    - workspace/features/INDEX.md
    - workspace/memory/project-memory.md

# TASK SEQUENCE
sequence:
  - step: scan_active_features
    action: 'Identify completed features'
    scan:
      path: 'workspace/features/active/*'
      criteria:
        - progress: '100%'
        - quality_gates: 'Gate 5: Production Ready PASSED'
      exclude:
        - '[planned]*'
        - '*-draft'
        - '*-wip'
    
  - step: validate_completion
    action: 'Verify feature is truly complete'
    checks:
      - progress_file: 'Shows 100% completion'
      - quality_gates: 'All 5 gates passed'
      - prd_status: 'Not in draft or planning'
      - no_blockers: 'No unresolved issues'
      - documentation: 'Complete and current'
    
  - step: user_confirmation
    action: 'Confirm archival with user'
    prompt: |
      📦 Feature Archival
      
      Found {count} completed features:
      {feature_list}
      
      Move to completed/? (Y/n/select)
    options:
      - all: 'Archive all completed features'
      - select: 'Choose specific features'
      - skip: 'Do not archive now'
    
  - step: backup_features
    action: 'Create backup before move'
    backup:
      source: 'workspace/features/active/{feature}/'
      target: '/tmp/feature-backup-{timestamp}/'
      include_all: true
    
  - step: prepare_target
    action: 'Ensure target directory exists'
    create:
      path: 'workspace/features/completed/{feature}/'
      permissions: 'maintain'
    
  - step: move_feature
    action: 'Move feature to completed'
    operation:
      type: 'move'  # Not copy
      source: 'workspace/features/active/{feature}/'
      target: 'workspace/features/completed/{feature}/'
      preserve:
        - timestamps
        - permissions
        - structure
    
  - step: update_references
    action: 'Update all references to moved feature'
    update:
      - file: 'workspace/features/INDEX.md'
        from: 'active/{feature}'
        to: 'completed/{feature}'
        set_status: 'completed'
        set_completion_date: '{timestamp}'
      
      - file: 'operations/agents/*/README.md'
        update_paths: true
        optional: true
      
      - file: 'SYSTEM-STRUCTURE.md'
        update_counts: true
    
  - step: validate_move
    action: 'Verify successful archival'
    checks:
      - source_removed: 'Active directory no longer exists'
      - target_exists: 'Completed directory has all files'
      - file_count: 'Same number of files'
      - file_integrity: 'No corruption during move'
      - references_updated: 'All paths corrected'
    
  - step: update_statistics
    action: 'Update feature statistics'
    update:
      file: 'workspace/features/INDEX.md'
      statistics:
        - total_active: 'decrease by {count}'
        - total_completed: 'increase by {count}'
        - completion_rate: 'recalculate'
        - by_status: 'update counts'
    
  - step: record_milestone
    action: 'Add to project memory'
    entry:
      action: 'Feature archival'
      features: '{feature_list}'
      milestone: 'feature_archived'
      pattern: 'Systematic feature lifecycle management'
    
  - step: cleanup
    action: 'Remove temporary files'
    cleanup:
      - backup_if_success: 'Remove after validation'
      - empty_directories: 'Remove if empty'
      - broken_links: 'Fix or remove'

# ERROR HANDLING
error_handling:
  move_failure:
    action: 'Restore from backup'
    severity: high
    recovery:
      - restore_backup
      - update_references_back
      - report_issue
    
  partial_move:
    action: 'Complete or rollback'
    decision: 'Based on completion percentage'
    threshold: 50%
    
  reference_update_failure:
    action: 'Log inconsistency for manual fix'
    severity: medium
    continue: true
    
  validation_failure:
    action: 'Restore and abort'
    severity: critical
    notify: true

# ROLLBACK PROCEDURE
rollback:
  trigger:
    - move_failure
    - validation_failure
    - user_cancellation
  
  steps:
    1: 'Stop current operation'
    2: 'Restore from backup to active/'
    3: 'Revert INDEX changes'
    4: 'Update references back'
    5: 'Remove partial completed/ directory'
    6: 'Verify system consistency'
    7: 'Report rollback complete'

# SUCCESS CRITERIA
success_criteria:
  - features_moved: 'All selected features archived'
  - no_data_loss: 'All files preserved'
  - references_valid: 'No broken links'
  - statistics_accurate: 'Counts match reality'
  - system_consistent: 'No integrity issues'

# PERFORMANCE
performance:
  optimization:
    - batch_operations: 'Move multiple features together'
    - parallel_updates: 'Update references concurrently'
    - cached_validation: 'Reuse validation results'
  
  targets:
    - single_feature: '<5 seconds'
    - multiple_features: '<20 seconds'
    - reference_updates: '<10 seconds'
```

---

## Usage Examples

### Automatic Execution
Called automatically by close-chat workflow during session closure.

### Manual Execution
```bash
# Archive all completed features
*task feature-archival

# Archive specific feature
*task feature-archival --feature close-chat-workflow

# Dry run to see what would be moved
*task feature-archival --dry-run
```

### Integration Points
- **close-chat workflow**: Calls during feature lifecycle engine
- **orchestrator**: Can trigger manually
- **feature INDEX**: Primary registry updated
- **project-memory**: Records archival milestone

---

## Archival Criteria

### Required for Archival
1. **Progress**: Must show 100% completion
2. **Quality Gates**: Gate 5 (Production Ready) must be PASSED
3. **Documentation**: PRD and progress tracking complete
4. **No Blockers**: No unresolved issues in active-context

### Excluded from Archival
- Features with `[planned]` prefix
- Draft features (`*-draft`)
- Work in progress (`*-wip`)
- Features with failed quality gates
- Features with open blockers

---

## Example Execution

```
📦 Feature Archival Process

Scanning active features...
Found 3 completed features:

1. ✅ close-chat-workflow (100%, all gates passed)
2. ✅ memory-system-upgrade (100%, all gates passed)
3. ❌ template-analysis (100%, gate 4 pending)

Move 2 completed features to completed/? (Y/n)
> Y

✅ Backing up features...
✅ Moving close-chat-workflow → completed/
✅ Moving memory-system-upgrade → completed/
✅ Updating INDEX references...
✅ Updating statistics...
✅ Recording milestone...

Archival Complete:
- Features Archived: 2
- References Updated: 5
- Statistics Updated: ✅
- System Integrity: ✅
```

This task ensures completed features are properly organized.