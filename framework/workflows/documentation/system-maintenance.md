# System Maintenance Workflow
**Workflow ID**: system-maintenance  
**Type**: Interactive & Automated  
**Priority**: CRITICAL  
**Category**: System Operations

<!-- dependencies
upstream:
  # AUTO-DETECTED Tasks Orchestrated (from workflow content analysis):
  - ../framework/tasks/system/system-sync.md  # Pattern: 'execute_task(system-sync)'
  - ../framework/tasks/system/update-system-structure.md  # Pattern: 'execute_task(update-system-structure)'
  - ../framework/tasks/system/update-all-indices.md  # Pattern: 'execute_task(update-all-indices)'
  - ../framework/tasks/validation/validate-dependencies.md  # Pattern: 'execute_task(validate-dependencies)'
  - ../framework/tasks/memory/update-project-memory.md  # Pattern: 'parallel_execute'
  
  # AUTO-DETECTED Engineering Rules Applied:
  - ../framework/engineeringrules/system-operations/workflow-orchestration.md  # Applied: workflow-execution
  - ../framework/engineeringrules/core-foundation/quality-assurance.md  # Applied: PASS/CONCERNS/FAIL/WAIVED framework
  
downstream:
  # AUTO-DETECTED Dependencies (entities that use system-maintenance):
  - agents/core/orchestrator.md  # Uses: operations/workflows/system-maintenance.md for maintenance commands
  - ../framework/tasks/system/system-sync.md  # References: maintenance workflow in orchestration
  
validated: 2025-08-27T16:30:00Z
health: 95%  # 95% - critical workflow with complete upstream/downstream mapping
generator: framework/templates/workflow.yaml
-->

## Workflow Definition

```yaml
workflow:
  id: system-maintenance
  name: System Maintenance & Synchronization
  description: >-
    Interactive workflow for comprehensive system maintenance including
    structure updates, index synchronization, dependency validation,
    and memory system updates. Provides both interactive menu and
    automated execution modes.
  type: operational
  complexity: high
  target_system: meta
  
context:
  situation: System requires regular maintenance to prevent drift
  assumptions:
    - User has system admin privileges
    - Backup storage available
    - All maintenance tasks accessible
  success_criteria:
    - System fully synchronized
    - All indices current
    - Dependencies valid
    - Documentation accurate
    - Memory systems updated
```

## Workflow Orchestration

### Interactive Mode
```yaml
interactive_menu:
  title: "🔧 System Maintenance Menu"
  options:
    1:
      name: "Full System Sync (Recommended)"
      description: "Complete system synchronization"
      action: execute_task('system-sync')
      estimated_time: "60 seconds"
      
    2:
      name: "Update Structure Map"
      description: "Update SYSTEM-STRUCTURE.md only"
      action: execute_task('update-system-structure')
      estimated_time: "10 seconds"
      
    3:
      name: "Update All Indices"
      description: "Synchronize all INDEX.md files"
      action: execute_task('update-all-indices')
      estimated_time: "15 seconds"
      
    4:
      name: "Validate Dependencies"
      description: "Check all system dependencies"
      action: execute_task('validate-dependencies')
      estimated_time: "20 seconds"
      
    5:
      name: "Update Memory Systems"
      description: "Sync active context and project memory"
      action: parallel_execute(['update-active-context', 'update-project-memory'])
      estimated_time: "5 seconds"
      
    6:
      name: "Generate Feature Roadmap (NEW)"
      description: "Update feature roadmap with current data"
      action: execute_task('generate-roadmap')
      estimated_time: "10 seconds"
      
    7:
      name: "Dry Run (Preview)"
      description: "See what would change without modifying"
      action: dry_run_mode()
      estimated_time: "30 seconds"
      
    7:
      name: "View Last Sync Report"
      description: "Display previous sync results"
      action: display_report()
      estimated_time: "Instant"
      
    8:
      name: "Schedule Maintenance"
      description: "Set up automated sync schedule"
      action: configure_schedule()
      estimated_time: "2 minutes"
      
    9:
      name: "Emergency Sync (Force)"
      description: "Force sync ignoring timestamps"
      action: execute_task('system-sync --force')
      estimated_time: "60 seconds"
      
    0:
      name: "Exit"
      description: "Return to orchestrator"
      action: exit_workflow()
```

## Execution Steps

### Step 1: Workflow Initialization
```yaml
initialization:
  - Load current system state
  - Check last sync timestamp
  - Verify task availability
  - Create session ID
  - Initialize logging
  
  display_status:
    last_sync: {timestamp}
    time_since_sync: {hours}
    system_health: {green | yellow | red}
    pending_changes: {count}
```

### Step 2: Health Check
```yaml
health_assessment:
  checks:
    - Last sync age (<24h: green, 24-48h: yellow, >48h: red)
    - File count drift (compare with last known)
    - Index currency (check modification times)
    - Dependency issues (quick scan)
    - Memory system status
    
  recommendations:
    red: "⚠️ CRITICAL: Full sync strongly recommended"
    yellow: "⚡ Sync recommended for optimal performance"
    green: "✅ System healthy, sync optional"
```

### Step 3: User Interaction
```yaml
menu_interaction:
  display:
    - Show menu with numbered options
    - Highlight recommended action
    - Display time estimates
    - Show health status indicator
    
  input_handling:
    - Accept number selection (0-9)
    - Accept command shortcuts (sync, check, etc.)
    - Validate input
    - Confirm destructive operations
```

### Step 4: Task Execution
```yaml
task_execution_modes:
  full_sync:
    tasks:
      - system-sync
    confirmation: required
    backup: automatic
    
  selective_sync:
    user_selects: [task_list]
    order: dependency_resolved
    backup: optional
    
  dry_run:
    simulation: true
    changes_preview: true
    no_modifications: true
    
  emergency:
    force_flags: true
    skip_checks: true
    priority: maximum
```

### Step 5: Progress Monitoring
```yaml
progress_display:
  format: |
    === System Maintenance in Progress ===
    Current Phase: {phase_name}
    Progress: [████████░░░░░░] {percentage}%
    Current Task: {task_name}
    Elapsed Time: {seconds}s
    Estimated Remaining: {seconds}s
    
  updates:
    frequency: real_time
    show_subtasks: true
    display_warnings: immediate
    error_handling: pause_and_prompt
```

### Step 6: Result Reporting
```yaml
completion_report:
  summary:
    - Total duration
    - Tasks completed
    - Files updated
    - Issues found
    - Quality gate status
    
  details:
    - Per-task results
    - File change list
    - Error log
    - Recommendations
    
  storage:
    location: workspace/data-output/maintenance-reports/
    format: maintenance-{timestamp}.md
```

## Automated Mode

### Scheduled Execution
```yaml
scheduled_maintenance:
  daily:
    time: "03:00 UTC"
    tasks: ['update-all-indices', 'update-active-context']
    
  weekly:
    time: "Sunday 02:00 UTC"
    tasks: ['system-sync']
    
  on_event:
    feature_complete: ['system-sync']
    milestone_reached: ['system-sync', 'generate-reports']
```

### Command Line Mode
```bash
# Full maintenance
*workflow system-maintenance --auto

# Specific maintenance
*workflow system-maintenance --tasks=structure,indices

# Scheduled mode
*workflow system-maintenance --schedule=daily

# Check only
*workflow system-maintenance --check
```

## Quality Gates

### Pre-Maintenance Gate
```yaml
pre_checks:
  required:
    - Sufficient disk space
    - Write permissions
    - No active locks
    - Backup location available
  
  decision: PROCEED | WARN | ABORT
```

### Post-Maintenance Gate
```yaml
post_validation:
  criteria:
    - All tasks completed
    - No critical errors
    - Files consistent
    - Dependencies valid
  
  decision: PASS | CONCERNS | FAIL
```

## Error Handling

### Recovery Strategies
| Error Type | Strategy | User Action |
|------------|----------|-------------|
| Task Failure | Retry with backoff | Prompted to retry |
| Permission Denied | Skip and document | Manual intervention |
| Disk Space | Abort safely | Clear space |
| Network Issues | Offline mode | Local only |
| Corruption Detected | Restore backup | Confirm restore |

### Rollback Procedure
```yaml
rollback:
  trigger:
    - Critical task failure
    - User abort
    - Corruption detected
    
  process:
    1. Stop all tasks
    2. Restore from backup
    3. Generate incident report
    4. Alert user
    5. Log for analysis
```

## Integration Points

### Orchestrator Integration
```yaml
orchestrator_commands:
  - maintenance: Launch interactive menu
  - sync: Direct full sync
  - sync-check: Health check only
  - maintenance-report: Last report
  - maintenance-schedule: Configure automation
```

### Task Dependencies
```yaml
required_tasks:
  - framework/tasks/system/system-sync.md
  - framework/tasks/system/update-system-structure.md
  - framework/tasks/system/update-all-indices.md
  - framework/tasks/validation/validate-dependencies.md
  - framework/tasks/memory/update-project-memory.md
  - framework/tasks/memory/update-project-memory.md
```

## Performance Optimization

### Caching Strategy
```yaml
cache:
  file_metadata: 5_minutes
  structure_tree: until_changed
  index_contents: per_session
  validation_results: 10_minutes
```

### Parallel Execution
```yaml
parallelizable:
  - Memory system updates
  - Non-dependent index updates
  - Report generation
  
sequential_required:
  - Structure before indices
  - Indices before validation
  - Backup before changes
```

## User Experience

### Feedback Messages
```yaml
messages:
  start: "🔧 Starting system maintenance..."
  progress: "📊 {task} in progress... {percent}%"
  success: "✅ Maintenance complete! All systems synchronized."
  warning: "⚠️ Maintenance completed with warnings. Review report."
  error: "❌ Maintenance failed. System restored from backup."
  
prompts:
  confirm: "This will update {count} files. Continue? (y/n)"
  rollback: "Error detected. Restore from backup? (y/n)"
  schedule: "Enter schedule (daily/weekly/custom):"
```

### Help System
```yaml
help_topics:
  - What does sync do?
  - When should I run maintenance?
  - What's a dry run?
  - How to schedule automation?
  - Troubleshooting guide
```

## Success Metrics
- Execution time <60 seconds for full sync
- Zero data loss incidents
- 100% dependency validation accuracy
- User satisfaction >90%
- Automation adoption >50%

## Future Enhancements
- Web-based maintenance dashboard
- Mobile notifications
- Predictive maintenance AI
- Multi-system federation
- Incremental sync optimization
- Visual diff previews

---
**Remember**: Regular maintenance prevents system drift. Run at least weekly or after major changes!