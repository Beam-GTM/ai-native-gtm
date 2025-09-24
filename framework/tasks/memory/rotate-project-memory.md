<!-- last_modified: 2025-08-28T02:17:11.270680Z -->
<!-- migration_path: auto-generated -->

# Task: Rotate Project Memory
**Type**: Memory Management  
**Category**: Automatic Maintenance  
**Priority**: HIGH  
**Created**: 2025-08-26T01:10:00Z  

## Purpose
Automatically rotate project-memory.md entries when limit reached (30 entries), preserving patterns and insights while maintaining manageable file size.

## Activation Triggers

```yaml
activation_triggers:
  version: "1.0.0"
  priority: "high"
  confidence_threshold: 95
  
  threshold_triggers:
    - name: "memory_approaching_capacity"
      condition: "project-memory.md > 25/30 entries"
      description: "Memory utilization exceeding 83%"
      check_method: "entry_count_analysis"
      auto_suggest: true
      
    - name: "memory_at_capacity"  
      condition: "project-memory.md >= 30/30 entries"
      description: "Memory at maximum capacity"
      check_method: "entry_count_analysis"
      auto_suggest: true
      severity: "critical"
      
  pattern_triggers:
    - name: "high_activity_session"
      condition: "3+ entries added in single session"
      description: "Unusually high development velocity"
      check_method: "session_activity_analysis"
      auto_suggest: false
      user_confirm: true
      
  orchestrator_integration:
    menu_priority: 10  # Highest priority
    context_aware: true
    confirmation_required: false  # High confidence triggers
    
  execution_controls:
    max_auto_triggers: 1
    cooldown_period: "4 hours"
    dependency_checks: false  # Memory rotation is always safe
```

## Legacy Trigger Conditions
- Entry count reaches 30
- Manual rotation request
- Monthly rotation (if not triggered by count)

## Rotation Process

### 1. Check Rotation Need
```yaml
rotation_check:
  - Count entries in project-memory.md
  - If count >= 30: ROTATE
  - If last rotation > 30 days: ROTATE
  - Otherwise: SKIP
```

### 2. Archive Old Entries
```yaml
archive_process:
  - Create archive file: workspace/memory/archives/project-memory-YYYY-MM-DD.md
  - Move entries 16-30 to archive (keep recent 15)
  - Preserve all metadata and structure
  - Update entry count in header
```

### 3. Extract Patterns Before Rotation
```yaml
pattern_preservation:
  - Scan entries 16-30 for patterns
  - Extract recurring themes
  - Update patterns/extracted/ if new patterns found
  - Preserve learnings in separate file
```

### 4. Update Rotated File
```yaml
post_rotation:
  header_update:
    - Reset entry count to 15
    - Update rotation timestamp
    - Note archive file location
    
  entry_renumbering:
    - Renumber remaining entries 1-15
    - Update trigger counts
    - Preserve all metadata
```

### 5. Validation
```yaml
rotation_validation:
  - Verify archive file created
  - Confirm entry count correct
  - Check no data loss
  - Validate patterns preserved
```

## Archive Format
```markdown
# PROJECT MEMORY ARCHIVE | Archived: YYYY-MM-DD | Entries: 16-30
<!-- ARCHIVE: From project-memory.md rotation -->
<!-- PATTERNS: Extracted to patterns/extracted/ -->

## Entry 16 | [timestamp]
[Original entry content preserved exactly]

## Entry 17 | [timestamp]
[Original entry content preserved exactly]

[etc...]
```

## Implementation Example
```bash
# When entry 31 would be added:
1. Check count (30) >= 30 ✓
2. Create archive: workspace/memory/archives/project-memory-2025-08-26.md
3. Move entries 16-30 to archive
4. Keep entries 1-15, renumber as 1-15
5. Add new entry as Entry 16
6. Update header: Entries: 16/30
```

## Pattern Extraction Integration
When rotating, also check for patterns:
- If 3+ similar actions → Extract action pattern
- If 3+ similar learnings → Extract learning pattern
- If 3+ similar projects → Extract project pattern

## Error Handling
- **Archive fails**: Keep all entries, alert user
- **Pattern extraction fails**: Continue rotation, log error
- **Disk full**: Compress old archives, retry
- **Permission denied**: Alert user, skip rotation

## Success Metrics
- Zero data loss during rotation
- Archives searchable and intact
- Patterns successfully extracted
- File size remains <100KB

---
**Status**: READY  
**Auto-trigger**: AT 30 ENTRIES