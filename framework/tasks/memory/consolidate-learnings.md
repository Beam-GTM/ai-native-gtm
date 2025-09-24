<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.831366Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.267950Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Consolidate Learnings Task
**Task ID**: consolidate-learnings  
**Priority**: HIGH - Execute regularly for system intelligence  
**Location**: framework/tasks/memory/consolidate-learnings.md  
**Pattern**: Follows update-project-memory.md automation approach  

## 🎯 PURPOSE
Automatically consolidate new learning artifacts into core-learnings.md, maintaining the compressed, always-loaded learning system. This task ensures orchestrator always has access to the latest consolidated knowledge.

## ⚡ QUICK EXECUTION (Copy & Execute)
```yaml
EXECUTE_NOW:
  1_READ: workspace/memory/core-learnings.md (check learning count)
  2_SCAN: Find new learning artifacts since last consolidation
  3_ANALYZE:
    - Learning_Count: Check if rotation needed (>35)
    - New_Patterns: Check for 3+ occurrence patterns
    - New_Features: Check for completed features with learnings
  4_CONSOLIDATE:
    - Extract_New: Compress new learnings using 1:5 ratio
    - Update_Core: Add to core-learnings.md
    - Rotate: If >35 learnings, archive oldest
  5_VALIDATE: Ensure orchestrator compatibility (<10KB)
```

## 📋 DETAILED STEPS

### Step 1: Load Current Learning State
```yaml
action: READ
files:
  - workspace/memory/core-learnings.md
  - workspace/features/INDEX.md (for completion status)
  - workspace/memory/project-memory.md (for patterns)
extract:
  - current_learning_count
  - last_consolidation_timestamp  
  - completed_features_since_last
  - new_pattern_candidates
validation:
  - Check rotation needed (>35 learnings)
  - Check file size (<10KB for orchestrator)
```

### Step 2: Discover New Learning Artifacts
```yaml
action: SCAN
locations:
  feature_completions:
    path: "workspace/features/completed/"
    files: "*/FEATURE-COMPLETE.md"
    check: "completion_date > last_consolidation"
    
  pattern_files:
    path: "workspace/memory/core-primitives/patterns/"
    files: "*.md"
    check: "modified > last_consolidation"
    
  session_logs:
    path: "workspace/memory/core-primitives/chat-sessions/"
    files: "*.md" 
    check: "created > last_consolidation"
    
  memory_insights:
    path: "workspace/memory/"
    files: "*/pattern-insights.md"
    check: "modified > last_consolidation"
```

### Step 3: Extract and Compress New Learnings
```yaml
action: EXTRACT
compression_algorithm:
  ratio: "1:5 (detailed:compressed)"
  
  feature_completion_extraction:
    input: "FEATURE-COMPLETE.md files"
    extract:
      - key_achievements: "What worked well"
      - radical_insights: "Unexpected discoveries"
      - success_patterns: "Repeatable approaches"
      - system_improvements: "Architecture insights"
    compress: "Max 1-2 lines per major insight"
    
  pattern_file_extraction:
    input: "Pattern .md files"
    extract:
      - frequency_data: "Occurrence count"
      - mitigation_strategies: "How to handle"
      - detection_signals: "Early warning signs"
    compress: "Essential mitigation only"
    
  session_insight_extraction:
    input: "Session log files"
    extract:
      - behavioral_patterns: "User behavior insights"
      - system_usage: "Tool usage patterns"
      - error_patterns: "Common failure modes"
    compress: "Key insights only, no session details"
```

### Step 4: Update Core-Learnings.md
```yaml
action: UPDATE
file: workspace/memory/core-learnings.md
process:
  header_update:
    - Update learning count: "{{new_total}} learnings"
    - Update source count: "{{source_count}} sources consolidated"
    - Update timestamp: "{{current_utc}}"
    - Update memory percentage: "{{capacity_percentage}}% full"
    
  critical_patterns_update:
    - Check for new HIGH severity patterns
    - Update frequency counts for existing patterns
    - Add new patterns with ≥3 occurrences
    
  learning_list_expansion:
    - Add new compressed learnings to TOP 15+ list
    - Organize by priority (system vs feature vs behavioral)
    - Maintain numbering sequence
    
  consolidated_summary_update:
    - Add new feature success patterns
    - Update system architecture insights  
    - Enhance pattern recognition results
    - Update system intelligence dashboard
    
validation:
  - File size <10KB (orchestrator compatibility)
  - All sections preserved
  - New learnings integrated
  - Pattern frequencies updated
```

### Step 5: Check Triggers and Rotation
```yaml
action: ANALYZE
triggers:
  learning_rotation:
    condition: "learning_count >= 35"
    action: "Archive oldest 10 learnings to core-learnings-archive.md"
    preserve: "Critical patterns and recent insights"
    
  pattern_promotion:
    condition: "pattern_occurrences >= 3"
    action: "Promote to CRITICAL PATTERNS section"
    severity: "Assign HIGH/MEDIUM/LOW based on impact"
    
  consolidation_scheduling:
    condition: "new_artifacts_found"
    action: "Update consolidation timestamp"
    next_check: "Set next consolidation trigger"
    
  orchestrator_validation:
    condition: "file_size > 10KB"
    action: "Trigger compression optimization"
    fallback: "Move detailed content to repository"
```

### Step 6: Generate Consolidation Report
```yaml
action: REPORT
output: workspace/memory/consolidation-reports/consolidation-{{timestamp}}.md
content:
  summary:
    - learnings_added: "{{count}} new learnings"
    - patterns_updated: "{{count}} pattern updates"  
    - features_processed: "{{list}} of completed features"
    - file_size: "{{size}} (orchestrator compatible)"
    
  source_breakdown:
    - feature_completions: "{{count}} processed"
    - pattern_files: "{{count}} updated"
    - session_insights: "{{count}} extracted"
    - memory_artifacts: "{{count}} integrated"
    
  validation_results:
    - orchestrator_compatibility: "PASS/FAIL"
    - compression_ratio: "{{ratio}} achieved"
    - pattern_accuracy: "{{percentage}} validated"
    - performance_impact: "{{milliseconds}} load time"
```

## 🔄 AUTOMATION TRIGGERS

### Automatic Execution Points
1. **Feature Completion**: When feature moved to completed/
2. **Weekly Schedule**: Every Sunday for routine consolidation  
3. **Memory Rotation**: When project-memory.md rotates (30 entries)
4. **Pattern Threshold**: When pattern reaches 3+ occurrences
5. **Manual Trigger**: Via *consolidate-learnings command

### Trigger Conditions
```yaml
feature_completion_trigger:
  condition: "New FEATURE-COMPLETE.md detected"
  frequency: "Immediate (within 1 hour)"
  priority: "HIGH"
  
scheduled_consolidation:
  condition: "Weekly interval reached"
  frequency: "Every Sunday 00:00 UTC"
  priority: "MEDIUM"
  
memory_rotation_trigger:
  condition: "project-memory.md rotation executed"
  frequency: "Every ~15-20 memory entries"  
  priority: "MEDIUM"
  
pattern_threshold_trigger:
  condition: "Pattern reaches 3+ occurrences"
  frequency: "As detected"
  priority: "HIGH"
```

## 📊 INTEGRATION POINTS

### Orchestrator Integration
```yaml
location: operations/agents/core/orchestrator.md
updates_needed:
  activation_sequence:
    - "core-learnings.md always loaded (no change needed)"
    - "Consolidation status visible in system intelligence dashboard"
    
  commands_addition:
    - "consolidate-learnings: Manual consolidation trigger"
    - "learning-status: Show consolidation status"
    
  memory_system_integration:
    - "Link to project-memory.md rotation triggers"
    - "Pattern extraction coordination"
```

### Feature Completion Integration  
```yaml
location: All feature completion workflows
integration:
  on_feature_complete:
    trigger: "consolidate-learnings"
    extract: "FEATURE-COMPLETE.md insights"
    compress: "Key learnings only"
    update: "core-learnings.md"
```

### Memory System Integration
```yaml
location: framework/tasks/memory/update-project-memory.md
coordination:
  pattern_sharing:
    - "Share extracted patterns with learning consolidation"
    - "Coordinate rotation timing"
    - "Avoid duplicate pattern processing"
```

## ⚠️ CRITICAL RULES

1. **ORCHESTRATOR COMPATIBILITY**: Always maintain core-learnings.md <10KB
2. **COMPRESSION RATIO**: 1:5 detailed to compressed ratio
3. **PATTERN THRESHOLD**: 3+ occurrences for pattern promotion
4. **PRESERVATION**: Never lose critical patterns or insights
5. **VALIDATION**: Test orchestrator loading after each update

## 🎯 CONSOLIDATION TYPES

### Feature Completion Consolidation
```yaml
frequency: "Immediate when feature completed"
sources: "FEATURE-COMPLETE.md files"
extract:
  - success_patterns: "What worked"  
  - architectural_insights: "System learnings"
  - process_improvements: "Workflow insights"
compress: "1-2 lines per major insight"
```

### Pattern File Consolidation  
```yaml
frequency: "Weekly or when pattern updated"
sources: "core-primitives/patterns/*.md"
extract:
  - frequency_updates: "Occurrence counts"
  - mitigation_refinements: "Updated strategies"
  - detection_improvements: "Better warning signs"
compress: "Essential mitigation strategies only"
```

### Session Insight Consolidation
```yaml
frequency: "Weekly batch processing" 
sources: "chat-sessions/*.md, memory insights"
extract:
  - behavioral_observations: "User patterns"
  - system_usage_patterns: "Tool preferences"  
  - recurring_issues: "Common problems"
compress: "High-level insights only"
```

## 📝 CONSOLIDATION REPORT TEMPLATE

```markdown
# Learning Consolidation Report
**Timestamp**: {{consolidation_timestamp}}
**Trigger**: {{trigger_type}}
**Duration**: {{processing_time}}

## Summary
- **Learnings Added**: {{new_learning_count}}
- **Patterns Updated**: {{pattern_update_count}}
- **Features Processed**: {{feature_list}}
- **Core-Learnings Size**: {{file_size}} ({{orchestrator_status}})

## Sources Processed
- **Feature Completions**: {{feature_count}} new completions
- **Pattern Files**: {{pattern_count}} updated patterns  
- **Session Insights**: {{session_count}} session logs
- **Memory Artifacts**: {{memory_count}} memory updates

## Validation Results
- **Orchestrator Compatibility**: {{compatibility_status}}
- **Compression Ratio**: {{compression_ratio}} achieved
- **Pattern Accuracy**: {{pattern_validation}}% validated
- **Performance Impact**: {{load_time}}ms load time

## Next Consolidation
- **Scheduled**: {{next_scheduled}}
- **Trigger Conditions**: {{active_triggers}}
- **Expected Sources**: {{pending_sources}}
```

## 🔗 RELATED COMPONENTS

- **Core Target**: workspace/memory/core-learnings.md (always-loaded)
- **Pattern Files**: workspace/memory/core-primitives/patterns/
- **Feature Completions**: workspace/features/completed/*/FEATURE-COMPLETE.md
- **Memory System**: workspace/memory/project-memory.md
- **Reports**: workspace/memory/consolidation-reports/

## 🚀 ORCHESTRATOR COMMAND

### Manual Trigger Command
```yaml
command: "*consolidate-learnings"
aliases: ["*consolidate", "*learning-update"]
description: "Manually trigger learning consolidation"
process:
  1: "Scan for new learning artifacts"
  2: "Extract and compress using 1:5 ratio"
  3: "Update core-learnings.md"
  4: "Validate orchestrator compatibility"
  5: "Generate consolidation report"
```

---
**REMEMBER**: This task maintains the critical core-learnings.md file that orchestrator loads on every activation. Always validate orchestrator compatibility after updates!