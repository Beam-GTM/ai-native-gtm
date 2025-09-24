<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.938809Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.276852Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Closure Report Task

## Generate comprehensive session closure report

---

## Task Definition

```yaml
task:
  id: closure-report
  name: Generate Closure Report
  description: >-
    Creates a comprehensive closure report showing all actions taken during
    session closure, including validation results, issues found/fixed, and
    system health status.
  type: reporting
  category: system-integrity
  priority: medium

execution:
  trigger: 'End of close-chat workflow'
  frequency: 'Each session closure'
  timeout: 10s
  
dependencies:
  reads:
    - Engine execution logs
    - Validation results
    - Memory operation results
    - Feature archival results
  
  writes:
    - workspace/data-output/closure-reports/closure-{timestamp}.md
    - Console output (summary)

# TASK SEQUENCE
sequence:
  - step: collect_engine_results
    action: 'Gather results from all 5 engines'
    engines:
      session_capture:
        - learnings_captured: count
        - summary_generated: path
        - memory_updated: status
      
      system_validation:
        - indices_verified: pass/fail
        - dependencies_valid: count
        - drift_detected: issues
        - fixes_applied: count
      
      memory_management:
        - rotation_performed: yes/no
        - aggregation_performed: yes/no
        - patterns_extracted: count
        - memory_health: status
      
      feature_lifecycle:
        - features_archived: list
        - registry_updated: status
        - gates_validated: count
      
      system_synchronization:
        - sync_executed: yes/no
        - phases_completed: list
        - issues_found: count
        - time_taken: duration
    
  - step: calculate_metrics
    action: 'Compute closure metrics'
    metrics:
      - total_execution_time: sum
      - engines_successful: count
      - issues_found: total
      - issues_fixed: total
      - data_protected: percentage
      - system_integrity: score
    
  - step: assess_health
    action: 'Determine system health status'
    criteria:
      green:
        - no_drift: true
        - memory_healthy: true
        - features_organized: true
        - no_critical_issues: true
      
      yellow:
        - minor_drift: '<5 issues'
        - memory_near_limit: '>80%'
        - non_critical_issues: '<10'
      
      red:
        - critical_drift: '>5 issues'
        - memory_full: '>95%'
        - critical_issues: 'any'
        - data_loss: 'any'
    
  - step: identify_actions_needed
    action: 'List required follow-up actions'
    categories:
      immediate:
        - critical_fixes
        - data_recovery
        - memory_issues
      
      next_session:
        - deferred_archival
        - manual_validations
        - performance_tuning
      
      monitoring:
        - watch_items
        - trend_analysis
        - pattern_alerts
    
  - step: generate_report
    action: 'Create closure report document'
    template: |
      # Session Closure Report
      **Timestamp**: {timestamp}
      **Execution Mode**: {mode}
      **Total Duration**: {duration}
      **System Health**: {health_badge}
      
      ## 🔄 Engine Execution Summary
      
      ### Session Capture Engine ✅
      - Learnings Captured: {learning_count}
      - Summary Generated: {summary_path}
      - Memory Updated: {memory_status}
      - Duration: {engine_time}
      
      ### System Validation Engine {validation_badge}
      - INDEX Verification: {index_status}
      - Dependencies Valid: {dep_count} checked
      - Drift Detected: {drift_issues}
      - Fixes Applied: {fix_count}
      - Duration: {engine_time}
      
      ### Memory Management Engine {memory_badge}
      - Rotation: {rotation_status}
      - Aggregation: {aggregation_status}
      - Patterns Extracted: {pattern_count}
      - Memory Health: {memory_health}
      - Duration: {engine_time}
      
      ### Feature Lifecycle Engine {feature_badge}
      - Features Archived: {archived_list}
      - Registry Updated: {registry_status}
      - Quality Gates: {gates_checked}
      - Duration: {engine_time}
      
      ### System Synchronization Engine {sync_badge}
      - Sync Executed: {sync_status}
      - Phases: {phases_completed}
      - Issues Found: {sync_issues}
      - Duration: {engine_time}
      
      ## 📊 Metrics Dashboard
      
      | Metric | Value | Status |
      |--------|-------|--------|
      | Total Execution | {total_time} | {time_status} |
      | Engines Success | {engine_success}/{engine_total} | {success_status} |
      | Issues Found | {issues_found} | {issue_status} |
      | Issues Fixed | {issues_fixed} | {fix_status} |
      | Data Protected | {data_protection}% | ✅ |
      | System Integrity | {integrity_score}/10 | {integrity_status} |
      
      ## 🚨 Issues & Resolutions
      
      ### Issues Found
      {issues_list}
      
      ### Issues Fixed
      {fixes_list}
      
      ### Pending Issues
      {pending_list}
      
      ## 📋 Actions Required
      
      ### Immediate Actions
      {immediate_actions}
      
      ### Next Session
      {next_session_actions}
      
      ### Monitoring
      {monitoring_items}
      
      ## 🎯 System State
      
      ### Before Closure
      - Active Features: {before_active}
      - Memory Entries: {before_memory}
      - System Drift: {before_drift}
      
      ### After Closure
      - Active Features: {after_active}
      - Memory Entries: {after_memory}
      - System Drift: {after_drift}
      
      ## ✅ Validation Summary
      
      - **Zero Drift**: {drift_status}
      - **Data Protection**: {protection_status}
      - **Memory Health**: {memory_status}
      - **Feature Organization**: {feature_status}
      - **System Integrity**: {integrity_status}
      
      ## 📝 Notes
      {additional_notes}
      
      ---
      *Report Generated: {timestamp}*
      *Next Sync Recommended: {next_sync}*
    
  - step: save_report
    action: 'Write report to file system'
    location: 'workspace/data-output/closure-reports/'
    filename: 'closure-{YYYY-MM-DD-HH-MM}.md'
    
  - step: display_summary
    action: 'Show summary to user'
    console_output: |
      ✅ Session Closure Complete!
      
      Summary:
      - Duration: {duration}
      - Health: {health_badge}
      - Issues Fixed: {issues_fixed}/{issues_found}
      - Features Archived: {archive_count}
      - Memory Status: {memory_health}
      
      Full Report: {report_path}

# ERROR HANDLING
error_handling:
  missing_data:
    action: 'Note as "unavailable" in report'
    continue: true
    
  calculation_error:
    action: 'Use defaults or skip metric'
    log: true
    
  write_failure:
    action: 'Output to console only'
    warn: true

# SUCCESS CRITERIA
success_criteria:
  - report_generated: 'Document created'
  - metrics_calculated: 'All key metrics computed'
  - health_assessed: 'System status determined'
  - actions_identified: 'Follow-up items listed'
  - user_informed: 'Summary displayed'

# PERFORMANCE
performance:
  optimization:
    - aggregate_data: 'Collect all data in one pass'
    - template_rendering: 'Fast markdown generation'
    - async_write: 'Non-blocking file write'
  
  targets:
    - execution_time: '<5 seconds'
    - report_size: '<20KB'
    - completeness: '100% sections'
```

---

## Usage Examples

### Automatic Execution
Called automatically at the end of close-chat workflow.

### Manual Execution
```bash
# Generate closure report
*task closure-report

# With specific timestamp
*task closure-report --timestamp 2025-08-26-14-30

# Console output only
*task closure-report --console-only
```

### Integration Points
- **close-chat workflow**: Final step after all engines
- **orchestrator**: Can display summary
- **data-output directory**: Report storage
- **monitoring systems**: Health tracking

---

## Report Sections

### Critical Information
- System health status (GREEN/YELLOW/RED)
- Issues found and fixed
- Data protection confirmation
- Actions required

### Detailed Metrics
- Engine-by-engine execution results
- Performance timing
- Success rates
- System state changes

### Follow-up Items
- Immediate actions needed
- Next session priorities
- Monitoring recommendations

---

## Health Status Badges

- 🟢 **GREEN**: System healthy, no issues
- 🟡 **YELLOW**: Minor issues, monitoring needed
- 🔴 **RED**: Critical issues, immediate action required
- ✅ **SUCCESS**: Operation completed successfully
- ⚠️ **WARNING**: Operation completed with concerns
- ❌ **FAILURE**: Operation failed

This task ensures complete visibility into session closure operations.