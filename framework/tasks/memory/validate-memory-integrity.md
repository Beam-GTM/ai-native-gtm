<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.898001Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.273109Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Validate Memory Integrity
**Type**: System Validation  
**Category**: Memory Management  
**Priority**: CRITICAL  
**Created**: 2025-08-26T00:30:00Z  

## Purpose
Validate project-memory.md integrity with comprehensive pre-save and post-save checks to ensure zero data loss and maintain system reliability. (Note: active-context.md has been REMOVED - project-memory.md is the sole memory system)

## Execution Steps

### 1. Pre-Save Validation Gates
```yaml
pre_save_checks:
  - entry_format_validation:
      check: Entry follows "## Entry N | timestamp" format
      action: Reject malformed entries
      
  - duplicate_detection:
      check: Entry number not already present
      action: Alert and merge if duplicate
      
  - timestamp_sequence:
      check: Timestamp newer than previous entry
      action: Warn if out of sequence
      
  - pattern_threshold:
      check: Pattern extraction triggers correct
      action: Execute extraction if threshold met
```

### 2. Simple Integrity Check
```yaml
integrity_check:
  - method: Basic validation markers
  - validation: Entry count and format verification
  - storage: Simple status in header
  - update: Quick check on every write
  - note: SHA256 WAIVED - overengineering for local text files
```

### 3. Post-Save Verification
```yaml
post_save_checks:
  - existence_verification:
      check: File exists at expected path
      action: Fallback to secondary location
      
  - content_readability:
      check: File can be read back successfully
      action: Attempt recovery from .bak
      
  - entry_count_validation:
      check: Entry count matches header declaration
      action: Reconcile count discrepancies
      
  - trigger_preservation:
      check: Pattern/rotation triggers intact
      action: Restore triggers from backup
```

### 4. Corruption Detection (Simplified)
```yaml
corruption_detection:
  - entry_count_mismatch: Header count vs actual entries
  - truncated_file: Check for incomplete final entry
  - format_violations: Missing "## Entry" markers
  - duplicate_entries: Same entry number twice
  
  on_corruption_detected:
    1. Alert with specific error details
    2. Load most recent .bak file
    3. Attempt reconstruction from fragments
    4. Log incident to error journal
```

### 5. Recovery Procedures
```yaml
recovery_chain:
  level_1:
    location: workspace/memory/project-memory.md
    action: Standard write with validation
    
  level_2:
    location: /tmp/emergency-memory.md
    action: Write to temp with alert
    
  level_3:
    location: Console output
    action: Echo for manual recovery
    
  level_4:
    location: .bak files (last 3)
    action: Reconstruct from backups
    
  level_5:
    location: patterns/extracted/
    action: Fresh start preserving patterns
```

## Integration Points

### With Orchestrator
- Load validation on activation
- Check integrity before handoffs
- Validate after agent switches

### With Workflows
- Pre-milestone validation
- Post-completion verification
- Error recovery automation

### With Tasks
- Memory update validation
- Pattern extraction checks
- Rotation verification

## Error Handling

### Common Errors
1. **Permission Denied**
   - Try secondary location
   - Alert user for manual intervention
   
2. **Disk Full**
   - Clear old .bak files
   - Compress archived entries
   
3. **Concurrent Access**
   - Implement file locking
   - Queue writes with retry
   
4. **Network Issues**
   - Cache locally first
   - Sync when connection restored

## Success Metrics
- Zero data loss incidents
- <1 second validation time
- 100% recovery success rate
- <1% write failure rate

## Testing Checklist
- [ ] Corrupt file recovery
- [ ] Concurrent write handling
- [ ] Disk full scenario
- [ ] Permission denied handling
- [ ] Checksum validation
- [ ] Trigger preservation
- [ ] Entry deduplication
- [ ] Timestamp sequencing

## Usage Example
```yaml
# Called automatically by memory update tasks
validate_memory_integrity:
  pre_save: true
  calculate_checksum: true
  post_save_verify: true
  
  on_failure:
    attempt_recovery: true
    alert_user: true
    log_incident: true
```

## Dependencies
- project-memory.md write access
- /tmp/ directory available
- .bak file rotation active
- Console output capability

---
**Status**: ACTIVE  
**Next Review**: After 10 validations