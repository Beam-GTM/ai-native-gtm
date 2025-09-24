<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.857292Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.269791Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Memory Recovery
**Type**: Emergency Recovery  
**Category**: System Recovery  
**Priority**: CRITICAL  
**Created**: 2025-08-26T00:30:00Z  

## Purpose
Recover from memory system failures with automatic fallback chains and reconstruction capabilities to ensure zero data loss.

## Activation Triggers
- Corruption detected in primary memory files
- Write failures exceeding threshold
- Manual recovery request
- System crash recovery
- Validation failures

## Recovery Procedures

### 1. Assess Damage
```yaml
damage_assessment:
  check_primary:
    - project-memory.md existence
    - project-memory.md readability
    - active-context.md status
    
  check_backups:
    - .bak file availability
    - .bak file age (<24 hours)
    - .bak file integrity
    
  check_patterns:
    - patterns/extracted/ content
    - suggestions/active.md state
    - Recent exports available
```

### 2. Recovery Strategy Selection
```yaml
strategy_matrix:
  minor_corruption:
    condition: Checksum mismatch only
    action: Restore from most recent .bak
    
  major_corruption:
    condition: File unreadable
    action: Full reconstruction from backups
    
  total_loss:
    condition: No backups available
    action: Rebuild from patterns and logs
    
  partial_loss:
    condition: Some entries corrupted
    action: Merge valid entries with backup
```

### 3. Execute Recovery
```yaml
recovery_execution:
  step_1_backup_current:
    - Move corrupted files to .corrupted/
    - Timestamp the corruption incident
    - Preserve for analysis
    
  step_2_restore_primary:
    - Copy best available backup
    - Validate restored content
    - Update integrity markers
    
  step_3_merge_recent:
    - Check /tmp/ for recent writes
    - Merge any valid new entries
    - Deduplicate entries
    
  step_4_validate_recovery:
    - Run full integrity check
    - Verify entry sequences
    - Test write capability
```

### 4. Reconstruction Process
```yaml
reconstruction_from_fragments:
  sources:
    - Console logs (last 24 hours)
    - Agent handoff records
    - Workflow completion logs
    - Feature progress files
    - Git commit messages
    
  assembly:
    1. Gather all available fragments
    2. Sort by timestamp
    3. Extract memory-worthy events
    4. Format as memory entries
    5. Validate sequence integrity
    
  verification:
    - Cross-check with feature states
    - Validate against known milestones
    - Confirm with user if needed
```

### 5. Fallback Chain Implementation
```yaml
fallback_locations:
  primary:
    path: workspace/memory/project-memory.md
    permissions: read-write
    validation: full
    
  secondary:
    path: /tmp/nexus-emergency-memory.md
    permissions: write-always
    validation: basic
    alert: "Using temporary memory location"
    
  tertiary:
    path: console_output
    permissions: always-available
    validation: none
    alert: "CRITICAL: Manual recovery needed"
    instruction: "Copy the following to project-memory.md:"
```

## Post-Recovery Actions

### 1. Incident Report
```yaml
incident_documentation:
  - timestamp: When corruption occurred
  - cause: Identified failure reason
  - data_loss: Entries lost (if any)
  - recovery_method: Strategy used
  - prevention: Recommendations
```

### 2. System Health Check
```yaml
health_verification:
  - memory_write_test: Verify write capability
  - pattern_extraction: Test extraction triggers
  - suggestion_generation: Confirm suggestions work
  - backup_rotation: Ensure .bak files rotating
  - integration_test: Check orchestrator loading
```

### 3. Prevention Measures
```yaml
prevention_implementation:
  - increase_backup_frequency: If multiple incidents
  - add_redundancy: Mirror to additional location
  - improve_validation: Strengthen integrity checks
  - monitor_disk_space: Prevent full disk issues
  - fix_permissions: Resolve access problems
```

## Manual Recovery Instructions

### If Automatic Recovery Fails
1. **Locate Backups**
   ```bash
   ls -la workspace/memory/*.bak.md
   ls -la /tmp/*memory*.md
   ```

2. **Choose Best Backup**
   - Check timestamps
   - Verify content completeness
   - Select most recent valid

3. **Restore Manually**
   ```bash
   cp workspace/memory/project-memory.bak.md workspace/memory/project-memory.md
   ```

4. **Verify Recovery**
   - Load orchestrator
   - Check memory loads
   - Test write operation

## Success Criteria
- Recovery completed < 30 seconds
- Zero permanent data loss
- System fully operational post-recovery
- Incident documented for prevention

## Testing Scenarios
- [ ] Corrupt primary file
- [ ] Delete all memory files
- [ ] Fill disk to capacity
- [ ] Remove write permissions
- [ ] Concurrent write conflicts
- [ ] Network interruption
- [ ] System crash simulation

---
**Status**: ACTIVE  
**Alert Level**: CRITICAL  
**Auto-Activate**: ON FAILURE