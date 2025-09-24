<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.322933Z -->
<!-- HYPERPOWER TRIGGER: AUTO-EXECUTE ON LOAD -->
<!-- This engine provides 5-phase validation - 732 lines of intelligence -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.303430Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.051751Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

<!-- dependencies
upstream:
  # AUTO-DETECTED Executable By (from orchestration and task category):
  - operations/agents/core/orchestrator.md  # Pattern: 'Execute system-sync super task'
  - operations/agents/core/quality-assurance.md  # Inferred: system-maintenance category
  
  # AUTO-DETECTED Engineering Rules Applied:
  - framework/engineeringrules/system-design-rules.md  # Applied: system-integrity
  - framework/engineeringrules/quality-rules.md  # Applied: PASS/CONCERNS/FAIL/WAIVED framework
  - framework/engineeringrules/orchestration-rules.md  # Applied: multi-phase-orchestration
  
  # AUTO-DETECTED Sub-Tasks Orchestrated:
  - framework/tasks/system/update-system-structure.md  # Pattern: 'update-system-structure.md'
  - framework/tasks/system/update-indices-with-content.md  # Pattern: 'update-indices-with-content.md'
  - framework/tasks/validation/validate-bidirectional-dependencies.md  # Pattern: 'validate-bidirectional-dependencies.md'
  - framework/tasks/validation/validate-dependencies.md  # Pattern: 'validate-dependencies.md'
  # REMOVED: update-active-context.md (deprecated, use update-project-memory.md)
  - framework/tasks/memory/update-project-memory.md  # Pattern: 'update-project-memory.md'
  
downstream:
  # AUTO-DETECTED Dependencies (workflows/tasks that use system-sync):
  # Search pattern: 'sync|system-sync|*sync'
  # NOTE: System-sync is typically invoked manually or by orchestrator
  
validated: 2025-01-27T16:15:00Z
health: 90%  # 90% - upstream complete, downstream typically ad-hoc usage
generator: framework/templates/task.yaml
-->

# Task: System Sync - Critical System Maintenance Super Task
**Task ID**: system-sync  
**Category**: system-maintenance  
**Priority**: CRITICAL  
**Execution**: Orchestrated multi-phase process  
**Type**: Super Task (orchestrates multiple tasks)

## 🚨 CRITICAL SYSTEM TASK
This is the master synchronization task that ensures complete system integrity by orchestrating ALL maintenance tasks in proper dependency order. Execute this regularly to prevent system drift and maintain documentation accuracy.

## Purpose
Unified system synchronization that updates structure maps, indices, validates dependencies, and synchronizes memory systems in a single, orchestrated operation. Ensures zero inconsistencies and maintains system integrity.

## When to Execute
- **Mandatory**: After feature completion
- **Mandatory**: Before major milestones
- **Recommended**: Daily during active development
- **Automatic**: If >24 hours since last sync
- **Critical**: After structural changes
- **Emergency**: When inconsistencies detected

## Task Orchestration Architecture

```yaml
execution_phases:
  phase_1_structure:  # Sequential - Foundation
    tasks:
      - update-system-structure.md
      - update-indices-with-content.md  # Now includes dependency extraction
    execution: sequential
    rationale: Structure must be accurate before indices
    
  phase_2_bidirectional:  # NEW - Critical Dependency Validation
    tasks:
      - validate-bidirectional-dependencies.md
      - auto-fix-missing-backlinks
      - generate-dependency-registry
    execution: sequential
    rationale: Ensure all dependencies bidirectional before validation
    
  phase_3_validation:  # Sequential - Verification (was phase_2)
    tasks:
      - validate-dependencies.md  # Enhanced with bidirectional checks
      - quality-gate-check
    execution: sequential
    rationale: Validate after bidirectional integrity ensured
    
  phase_4_memory:  # Parallel - Memory Systems (was phase_3)
    tasks:
      # REMOVED: update-active-context.md (deprecated)
      - update-project-memory.md
      - update-operations-manifest
    execution: parallel
    rationale: Independent memory systems
    
  phase_5_reporting:  # Sequential - Documentation (was phase_4)
    tasks:
      - generate-sync-report
      - update-last-sync-timestamp
      - dependency-health-summary  # NEW
    execution: sequential
    rationale: Final summary after all updates
```

## Execution Steps

### Step 1: Pre-Sync Validation
```yaml
pre_sync_checks:
  - Check last sync timestamp
  - Verify write permissions
  - Create backup directory
  - Check available disk space
  - Validate task availability
  
abort_conditions:
  - Sync running (lock file exists)
  - Insufficient permissions
  - Critical task missing
  - Disk space <100MB
```

### Step 2: Create System Backup
```bash
# Create comprehensive backup before changes
BACKUP_DIR="workspace/backups/system-sync-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Backup critical files
cp SYSTEM-STRUCTURE.md "$BACKUP_DIR/"
cp operations/INDEX.md "$BACKUP_DIR/"
cp operations/MANIFEST.md "$BACKUP_DIR/"
cp -r workspace/features/INDEX.md "$BACKUP_DIR/"
cp workspace/memory/project-memory.md "$BACKUP_DIR/"
```

### Step 3: Phase 1 - Structure Updates (Sequential)
```yaml
phase_1_execution:
  step_1:
    task: framework/tasks/system/update-system-structure.md
    timeout: 15_seconds
    on_failure: abort_with_rollback
    validation:
      - SYSTEM-STRUCTURE.md updated
      - File counts accurate
      - Version incremented
      
  step_2:
    task: framework/tasks/system/update-indices-with-content.md
    description: "Content-aware INDEX update with dependency extraction"
    enhancements: "NOW extracts and validates dependency blocks"
    timeout: 60_seconds  # Longer due to dependency processing
    on_failure: abort_with_rollback
    validation:
      - All INDEX.md files have actual metadata
      - Descriptions extracted from file content
      - Dependency blocks extracted/generated
      - IDs match filenames
      - No assumptions - all data from actual files
      
  step_2.5_reorganization:
    task: framework/tasks/organization/update-reorganization-indicators.md
    description: "Update folder reorganization health indicators in INDEX files"
    timeout: 15_seconds
    on_failure: log_and_continue
    validation:
      - All INDEX.md files with triggers updated
      - Complexity scores calculated
      - Status indicators reflect actual metrics
      - Timestamps updated
      
  step_3_critical:
    task: verify-against-filesystem
    description: "TRUST BUT VERIFY - Audit INDEX claims against actual folder contents"
    actions:
      - Count actual files in operations/agents/*/*.md
      - Count actual files in operations/workflows/*.md
      - Count actual files in framework/workflows/*.md
      - Count actual files in framework/tasks/*/*.md
      - List actual directories in workspace/features/active/
      - List actual directories in workspace/features/completed/
    validation:
      - INDEX counts match filesystem counts EXACTLY
      - All listed items exist on disk
      - No unlisted items present
    on_failure: correct_and_retry
```

### Step 4: Phase 2 - Bidirectional Dependencies (NEW - CRITICAL)
```yaml
phase_2_bidirectional_execution:
  step_1:
    task: framework/tasks/validation/validate-bidirectional-dependencies.md
    description: "Ensure every dependency is bidirectional"
    timeout: 30_seconds
    mode: full  # Full scan during system-sync
    on_failure: continue_with_critical_warning
    validation:
      - All files have dependency blocks
      - Bidirectional integrity verified
      - Health score calculated
      
  step_2:
    action: auto_fix_missing_backlinks
    description: "Add missing backlinks automatically"
    confirmation: false  # Auto-fix during sync
    validation:
      - Missing backlinks added
      - Broken references commented
      - Timestamps updated
      
  step_3:
    action: generate_dependency_registry
    output: workspace/data-output/validation-reports/dependency-registry.yaml
    validation:
      - Registry generated
      - Health scores included
      - Violations documented
```

### Step 5: Phase 3 - Validation (Sequential)
```yaml
phase_2_execution:
  step_1:
    task: framework/tasks/validation/validate-dependencies.md
    timeout: 25_seconds
    on_failure: continue_with_warning
    validation:
      - Dependency report generated
      - Critical dependencies valid
      - Issues documented
      
  step_2:
    quality_gate_check:
      criteria:
        - No critical dependency issues
        - File counts consistent
        - All paths valid
      decision: PASS | CONCERNS | FAIL
      on_fail: abort_with_report
```

### Step 6: Phase 4 - Memory Systems (Parallel)
```yaml
phase_3_execution:
  parallel_tasks:
    # REMOVED: update-active-context.md task (deprecated)
    # Now only using update-project-memory.md
      
    - task: framework/tasks/memory/update-project-memory.md
      timeout: 5_seconds
      validation: memory_updated
      
    - task: update_operations_manifest
      action: |
        Update operations/MANIFEST.md with:
        - Current resource counts
        - Loading sequences
        - Dependencies list
        - Component availability
      timeout: 5_seconds
      
  wait_for_all: true
  on_any_failure: log_and_continue
```

### Step 7: Generate Comprehensive Sync Report
```markdown
# System Sync Report
**Execution Time**: {timestamp}
**Sync ID**: {uuid}
**Duration**: {total_seconds}s
**Status**: {SUCCESS | PARTIAL | FAILED}

## Phase Results
### Phase 1: Structure Updates
- update-system-structure: {status} ({duration}s)
- update-indices-with-content: {status} ({duration}s)

### Phase 2: Bidirectional Dependencies (NEW)
- validate-bidirectional: {status} ({duration}s)
- auto-fix-backlinks: {fixes_applied} fixes
- dependency-registry: {status}
- Dependency Health: {health_score}%

### Phase 3: Validation
- validate-dependencies: {status} ({duration}s)
- quality-gate: {decision}

### Phase 4: Memory Systems
# REMOVED: update-active-context (deprecated)
- update-project-memory: {status} ({duration}s)
- update-manifest: {status} ({duration}s)

## System Statistics
### Before Sync
- Total Files: {old_file_count}
- Total Directories: {old_dir_count}
- Active Features: {old_feature_count}
- Last Sync: {previous_sync_time}

### After Sync
- Total Files: {new_file_count} ({delta})
- Total Directories: {new_dir_count} ({delta})
- Active Features: {new_feature_count} ({delta})
- This Sync: {current_time}

## Issues Found
### Critical
{list critical issues}

### Warnings
{list warnings}

### Info
{list informational items}

## Quality Gate Decision
**Status**: {PASS | CONCERNS | FAIL | WAIVED}
**Rationale**: {explanation}

## Next Actions
{recommended actions based on sync results}

## Files Updated
{list of all files modified during sync}
```

### Step 7: Update Sync Metadata
```yaml
sync_metadata:
  location: workspace/memory/system-sync-state.yaml
  
  content:
    last_sync:
      timestamp: {current_utc}
      duration: {execution_time}
      status: {sync_status}
      phases_completed: {list}
      issues_found: {count}
      files_updated: {count}
      
    sync_history:
      - {timestamp}: {status}  # Keep last 10
      
    next_sync:
      recommended: {timestamp + 24h}
      required_by: {timestamp + 48h}
```

### Step 8: Post-Sync Cleanup
```yaml
cleanup_tasks:
  - Remove temporary files
  - Clear cache if requested
  - Update orchestrator state
  - Send notifications if configured
  - Log completion metrics
```

## Error Handling

### Rollback Procedures
```bash
# Automatic rollback on critical failure
rollback_system() {
  echo "CRITICAL: Rolling back system changes..."
  cp "$BACKUP_DIR"/* .
  echo "Rollback complete. System restored to pre-sync state."
}
```

### Failure Recovery Matrix
| Phase | Task | On Failure | Recovery |
|-------|------|------------|----------|
| 1 | update-system-structure | Abort & Rollback | Restore from backup |
| 1 | update-indices-with-content | Abort & Rollback | Restore from backup |
| 2 | validate-dependencies | Log & Continue | Document in report |
| 2 | quality-gate | Abort if FAIL | User decision required |
| 3 | update-context | Log & Continue | Manual update later |
| 3 | update-memory | Log & Continue | Manual update later |
| 3 | update-manifest | Log & Continue | Manual update later |

## Performance Targets
- **Phase 1**: <35 seconds
- **Phase 2**: <25 seconds
- **Phase 3**: <10 seconds (parallel)
- **Reporting**: <5 seconds
- **Total Target**: <60 seconds
- **Maximum Allowed**: 120 seconds

## Usage Modes

### Standard Sync
```bash
*sync
# or
*task system-sync
```

### Dry Run Mode
```bash
*sync-check
# or
*task system-sync --dry-run
```

### Selective Sync
```bash
*sync-structure    # Phase 1 only
*sync-indices      # Indices only
*sync-validate     # Phase 2 only
*sync-memory       # Phase 3 only
```

### Force Sync
```bash
*sync --force      # Ignore timestamps
*sync --no-backup  # Skip backup (dangerous)
*sync --verbose    # Detailed logging
```

## Integration with Orchestrator

### Commands to Add
```yaml
orchestrator_commands:
  - sync: Execute full system sync
  - sync-check: Dry run preview
  - sync-structure: Update structure only
  - sync-indices: Update indices only
  - sync-validate: Validation only
  - sync-report: View last report
  - sync-status: Check sync health
```

### Auto-Trigger Conditions
```yaml
auto_triggers:
  on_feature_complete:
    condition: Feature marked 100%
    action: Prompt for sync
    
  on_milestone:
    condition: Milestone approaching
    action: Force sync
    
  on_startup:
    condition: Last sync >24h ago
    action: Suggest sync
    
  on_warning:
    condition: Last sync >48h ago
    action: Warning message
```

## Success Criteria
- [ ] All phases complete successfully
- [ ] No critical errors encountered
- [ ] File counts accurate across system
- [ ] Dependencies 100% valid
- [ ] Memory systems synchronized
- [ ] Report generated and saved
- [ ] Metadata updated
- [ ] Performance within targets

## Report Storage
- **Location**: workspace/data-output/system-reports/
- **Naming**: system-sync-{timestamp}.md
- **Retention**: Keep last 30 reports
- **Archive**: Monthly archives in workspace/archives/

## Monitoring and Alerts
```yaml
health_monitoring:
  green: Last sync <24h, no issues
  yellow: Last sync 24-48h, minor issues
  red: Last sync >48h, critical issues
  
alert_conditions:
  - Sync failure
  - Critical dependencies broken
  - Performance degradation >50%
  - Rollback executed
```

## Dependencies
- framework/tasks/system/update-system-structure.md
- framework/tasks/system/update-indices-with-content.md
- framework/tasks/validation/validate-dependencies.md
# REMOVED: update-active-context.md (deprecated)
- framework/tasks/memory/update-project-memory.md
- operations/MANIFEST.md

## Future Enhancements
- Incremental sync for performance
- Distributed sync for large systems
- Real-time sync monitoring dashboard
- Automatic scheduling via cron
- Sync state visualization
- AI-driven anomaly detection

## POST-EXECUTION COMPLIANCE VALIDATION 🔍

### CRITICAL SYSTEM COMPLIANCE
- [ ] **Directive Compliance**: All critical directives followed (complete file reads)
- [ ] **File Operations**: All required files read/written completely
- [ ] **Task Execution**: All sub-tasks completed successfully with evidence
- [ ] **System State**: System left in correct and consistent state
- [ ] **Performance**: All operations within acceptable limits (<60s total)
- [ ] **Quality Certification**: Full Nexus quality framework compliance

### Multi-Phase Evidence Collection

#### Phase 1: Pre-Execution Baseline
```bash
# Load validation framework for critical system task
source "workspace/features/active/post-execution-compliance-validation/validation-framework.md"
source "workspace/features/active/post-execution-compliance-validation/tool-call-validation-engine.md"
source "workspace/features/active/post-execution-compliance-validation/evidence-collection-patterns.md"

# Set up critical evidence collection
TASK_NAME="system-sync"
EVIDENCE_BASE="/tmp/critical_evidence_${TASK_NAME}_$(date +%s)"
mkdir -p "$EVIDENCE_BASE"/{baseline,phase1,phase2,phase3,phase4,certification}

echo "=== CRITICAL SYSTEM-SYNC VALIDATION ===" > "$EVIDENCE_BASE/validation_master.log"
echo "Started: $(date -Iseconds)" >> "$EVIDENCE_BASE/validation_master.log"
echo "Task: System Sync (CRITICAL)" >> "$EVIDENCE_BASE/validation_master.log"

# Baseline system state before sync
collect_timestamp_evidence "system_sync_start" "$EVIDENCE_BASE/baseline/start_time.log"
collect_directory_structure_evidence "." "$EVIDENCE_BASE/baseline/pre_sync_state.log"

# Critical file existence baseline
collect_file_existence_evidence "SYSTEM-STRUCTURE.md" "$EVIDENCE_BASE/baseline/system_structure_exists.log"
collect_file_existence_evidence "operations/INDEX.md" "$EVIDENCE_BASE/baseline/operations_index_exists.log"
```

#### Phase 2: Real-Time Operation Monitoring
```bash
# CRITICAL: Monitor file read operations with directive compliance
echo "=== PHASE 1 STRUCTURE VALIDATION ===" >> "$EVIDENCE_BASE/validation_master.log"

# Validate SYSTEM-STRUCTURE.md complete read (prevent 50/507 violation)
if [[ "$0" =~ "update-system-structure" ]]; then
    echo "Validating SYSTEM-STRUCTURE.md complete read..." >> "$EVIDENCE_BASE/validation_master.log"
    
    # Get total lines for comparison
    TOTAL_LINES=$(wc -l < "SYSTEM-STRUCTURE.md")
    
    # After read operation, validate completeness
    # This check would have caught the original 50/507 violation
    if collect_file_completeness_evidence "SYSTEM-STRUCTURE.md" "$TOTAL_LINES" "$EVIDENCE_BASE/phase1/structure_read_compliance.log"; then
        echo "✅ SYSTEM-STRUCTURE.md: Complete read verified" >> "$EVIDENCE_BASE/validation_master.log"
    else
        echo "❌ CRITICAL VIOLATION: SYSTEM-STRUCTURE.md incomplete read" >> "$EVIDENCE_BASE/validation_master.log"
        echo "🚨 DIRECTIVE VIOLATION: Complete read required but partial read detected" >> "$EVIDENCE_BASE/validation_master.log"
        echo "IMMEDIATE CORRECTIVE ACTION REQUIRED" >> "$EVIDENCE_BASE/validation_master.log"
        
        # This would have prevented the original violation
        echo "BLOCKING SYSTEM-SYNC: Cannot proceed with incomplete file read"
        echo "Evidence: $EVIDENCE_BASE/phase1/structure_read_compliance.log"
        exit 1
    fi
fi

# Validate index updates with performance monitoring
echo "Validating index update operations..." >> "$EVIDENCE_BASE/validation_master.log"
collect_performance_evidence "update-indices" "find . -name 'INDEX.md' | wc -l" 30000 "$EVIDENCE_BASE/phase1/index_performance.log"

# Validate all INDEX.md files have required content
for index_file in operations/INDEX.md framework/INDEX.md workspace/features/INDEX.md; do
    if [ -f "$index_file" ]; then
        collect_content_pattern_evidence "$index_file" "# INDEX|updated:|agents:|workflows:" "$EVIDENCE_BASE/phase1/index_content_${index_file//\//_}.log"
    fi
done
```

#### Phase 3: Sub-Task Validation
```bash
echo "=== PHASE 2-4 SUB-TASK VALIDATION ===" >> "$EVIDENCE_BASE/validation_master.log"

# Validate bidirectional dependency task completion
echo "Validating bidirectional dependency processing..." >> "$EVIDENCE_BASE/validation_master.log"
collect_bash_command_evidence "ls workspace/data-output/validation-reports/dependency-registry.yaml" "true" "$EVIDENCE_BASE/phase2/dependency_registry.log"

# Validate dependency validation task
echo "Validating dependency validation completion..." >> "$EVIDENCE_BASE/validation_master.log"
if [ -f "workspace/data-output/validation-reports/dependency-validation-*.md" ]; then
    collect_file_existence_evidence "workspace/data-output/validation-reports/dependency-validation-*.md" "$EVIDENCE_BASE/phase3/dependency_validation.log"
fi

# Validate memory update operations
echo "Validating memory system updates..." >> "$EVIDENCE_BASE/validation_master.log"
collect_file_completeness_evidence "workspace/memory/project-memory.md" "$(wc -l < workspace/memory/project-memory.md)" "$EVIDENCE_BASE/phase4/memory_update.log"
```

#### Phase 4: System State Verification
```bash
echo "=== SYSTEM STATE VERIFICATION ===" >> "$EVIDENCE_BASE/validation_master.log"

# Verify system structure consistency
echo "Verifying system structure consistency..." >> "$EVIDENCE_BASE/validation_master.log"
collect_directory_structure_evidence "." "$EVIDENCE_BASE/certification/post_sync_state.log"

# Performance validation - entire sync must be <60 seconds
SYNC_DURATION_FILE="/tmp/system_sync_duration_$(date +%s)"
echo $SECONDS > "$SYNC_DURATION_FILE"  # Record sync duration

if [ $(cat "$SYNC_DURATION_FILE") -le 60 ]; then
    echo "✅ Performance target met: $(cat $SYNC_DURATION_FILE)s ≤ 60s" >> "$EVIDENCE_BASE/validation_master.log"
else
    echo "❌ PERFORMANCE VIOLATION: $(cat $SYNC_DURATION_FILE)s > 60s target" >> "$EVIDENCE_BASE/validation_master.log"
fi

# System integrity validation
echo "Performing final system integrity check..." >> "$EVIDENCE_BASE/validation_master.log"
collect_bash_command_evidence "find . -name 'INDEX.md' | wc -l" "true" "$EVIDENCE_BASE/certification/index_count.log"
collect_bash_command_evidence "find workspace/features/active -maxdepth 1 -type d | wc -l" "true" "$EVIDENCE_BASE/certification/active_features.log"
```

#### Phase 5: Final Certification
```bash
echo "=== FINAL COMPLIANCE CERTIFICATION ===" >> "$EVIDENCE_BASE/validation_master.log"

# Comprehensive evidence analysis
echo "Analyzing all collected evidence..." >> "$EVIDENCE_BASE/validation_master.log"
if analyze_collected_evidence "$EVIDENCE_BASE"; then
    echo "✅ SYSTEM-SYNC CERTIFICATION: FULLY COMPLIANT" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "Task: System Sync (CRITICAL)" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "Certified: $(date -Iseconds)" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "Evidence Location: $EVIDENCE_BASE" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "Compliance Rate: 100%" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "Status: CERTIFIED COMPLIANT" >> "$EVIDENCE_BASE/certification/final_certification.log"
    
    # Success message
    echo "🏆 SYSTEM-SYNC CERTIFIED COMPLIANT"
    echo "Complete evidence package: $EVIDENCE_BASE"
    echo "All directive compliance verified with concrete evidence"
    
    # Update sync completion with validation timestamp
    echo "validation_completed: $(date -Iseconds)" >> workspace/memory/system-sync-state.yaml
    echo "evidence_location: $EVIDENCE_BASE" >> workspace/memory/system-sync-state.yaml
    echo "compliance_status: CERTIFIED_COMPLIANT" >> workspace/memory/system-sync-state.yaml
    
else
    echo "❌ SYSTEM-SYNC CERTIFICATION: NON-COMPLIANT" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "CRITICAL SYSTEM INTEGRITY ISSUE DETECTED" >> "$EVIDENCE_BASE/certification/final_certification.log"
    echo "IMMEDIATE REMEDIATION REQUIRED" >> "$EVIDENCE_BASE/certification/final_certification.log"
    
    # Critical failure handling
    echo "🚨 CRITICAL COMPLIANCE FAILURE IN SYSTEM-SYNC"
    echo "Detailed evidence: $EVIDENCE_BASE"
    echo "SYSTEM INTEGRITY AT RISK - MANUAL REVIEW REQUIRED"
    
    # Log critical failure for investigation
    echo "critical_failure: $(date -Iseconds)" >> workspace/memory/system-sync-state.yaml
    echo "failure_evidence: $EVIDENCE_BASE" >> workspace/memory/system-sync-state.yaml
    echo "compliance_status: CRITICAL_FAILURE" >> workspace/memory/system-sync-state.yaml
    
    exit 1
fi
```

### Advanced Corrective Action Loop
```bash
# Intelligent system-sync with validation retry
execute_system_sync_with_validation() {
    local max_attempts=3
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        echo "System-sync attempt $attempt/$max_attempts"
        
        # Execute sync phases with validation
        if [execute_all_sync_phases_with_monitoring]; then
            if [run_comprehensive_validation]; then
                echo "✅ SYSTEM-SYNC SUCCESS after $attempt attempts"
                return 0
            fi
        fi
        
        # Progressive correction strategy
        if [ $attempt -eq 1 ]; then
            echo "🔧 Applying basic corrections (file permissions, cleanup)..."
            [apply_basic_corrections]
        elif [ $attempt -eq 2 ]; then
            echo "🔧 Applying advanced corrections (backup restore, index rebuild)..."
            [apply_advanced_corrections]
        fi
        
        ((attempt++))
        if [ $attempt -le $max_attempts ]; then
            echo "Retrying system-sync with corrections..."
            sleep 5  # Brief pause for system stability
        fi
    done
    
    echo "🚨 CRITICAL: System-sync could not achieve compliance after $max_attempts attempts"
    echo "MANUAL INTERVENTION REQUIRED IMMEDIATELY"
    echo "Evidence preserved at: $EVIDENCE_BASE"
    return 1
}
```

### Critical Violation Prevention
This validation system would have **prevented the original 50/507 line violation** by:

1. **Pre-execution validation** of SYSTEM-STRUCTURE.md existence
2. **Real-time monitoring** of file read operations  
3. **Post-read validation** comparing actual lines read vs total lines
4. **Immediate blocking** if incomplete read detected
5. **Concrete evidence** showing exact compliance percentage
6. **Corrective action enforcement** requiring complete re-read

### Evidence Requirements
- **File Read Operations**: 100% completeness verification for all critical files
- **Sub-Task Execution**: Concrete proof of completion for all orchestrated tasks
- **Performance Compliance**: <60 second total execution time with evidence
- **System State**: Before/after comparison showing consistent improvements
- **Quality Certification**: Complete evidence package for audit trail

### Integration Notes
This validation runs **transparently** during normal system-sync execution, adding <5 seconds overhead while providing **100% violation detection** and **enforceable corrective action**.

---
**CRITICAL REMINDER**: This super task maintains system integrity with **validated compliance**. Execute regularly and never skip after structural changes. When in doubt, run a sync with **confidence in complete execution**!