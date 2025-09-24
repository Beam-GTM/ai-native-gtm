<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.966733Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.279135Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Session Summary Task

## Generate comprehensive session summary for chat sessions

---

## Task Definition

```yaml
task:
  id: session-summary
  name: Generate Session Summary
  description: >-
    Creates a comprehensive summary of the current chat session including
    work completed, decisions made, learnings captured, and next steps.
  type: documentation
  category: memory
  priority: high

execution:
  trigger: 'Session closure or manual request'
  frequency: 'End of each session'
  timeout: 15s
  
dependencies:
  reads:
    - workspace/memory/project-memory.md
    - workspace/memory/active-context.md (if exists)
    - workspace/features/active/*/active-context.md
  
  writes:
    - workspace/memory/core-primitives/chat-sessions/session-{date}.md

# TASK SEQUENCE
sequence:
  - step: gather_session_data
    action: 'Collect session information'
    collect:
      - session_id: 'Current date/time stamp'
      - duration: 'Session length if available'
      - agent_transformations: 'Agents used during session'
      - workflows_executed: 'Workflows run'
      - features_worked: 'Features modified or created'
    
  - step: extract_accomplishments
    action: 'Identify work completed'
    scan:
      - project_memory: 'Recent entries for this session'
      - active_contexts: 'Progress updates'
      - feature_progress: 'Milestone achievements'
    output:
      - tasks_completed
      - milestones_reached
      - files_created_modified
    
  - step: capture_decisions
    action: 'Document key decisions made'
    identify:
      - architectural_choices
      - design_decisions
      - risk_assessments
      - quality_gates_passed
    
  - step: collect_learnings
    action: 'Gather session learnings'
    sources:
      - captured_primitives: 'New behavioral patterns'
      - discovered_issues: 'Problems encountered'
      - solutions_found: 'How issues were resolved'
      - patterns_recognized: 'Recurring themes'
    
  - step: identify_blockers
    action: 'Document unresolved issues'
    categories:
      - technical_blockers
      - missing_dependencies
      - incomplete_tasks
      - deferred_decisions
    
  - step: prepare_next_session
    action: 'Define next steps'
    include:
      - priority_tasks: 'What to tackle first'
      - context_needed: 'Files to load'
      - decisions_pending: 'Choices to make'
      - resources_required: 'Dependencies to prepare'
    
  - step: generate_summary
    action: 'Create summary document'
    template: |
      # Session Summary - {date}
      
      **Session ID**: {session_id}
      **Duration**: {duration}
      **Agents Used**: {agents}
      **Workflows**: {workflows}
      
      ## 🎯 Accomplishments
      {accomplishments_list}
      
      ## 📊 Features Worked
      {features_with_progress}
      
      ## 🧠 Key Decisions
      {decisions_list}
      
      ## 📚 Learnings Captured
      {learnings_list}
      
      ## 🚧 Blockers & Issues
      {blockers_list}
      
      ## ⏭️ Next Session Focus
      {next_steps}
      
      ## 📈 Metrics
      - Files Created: {file_count}
      - Tasks Completed: {task_count}
      - Quality Gates: {gates_passed}/{gates_total}
      - System Health: {health_status}
      
      ---
      *Generated: {timestamp}*
    
  - step: save_summary
    action: 'Write to chat-sessions directory'
    path: 'workspace/memory/core-primitives/chat-sessions/'
    filename: 'session-{YYYY-MM-DD-HH-MM}.md'
    
  - step: update_index
    action: 'Add to sessions index if exists'
    update: 'workspace/memory/core-primitives/chat-sessions/INDEX.md'
    optional: true

# ERROR HANDLING
error_handling:
  missing_data:
    action: 'Use available data, note gaps'
    continue: true
    
  write_failure:
    action: 'Output to console as fallback'
    retry: 1
    
  timeout:
    action: 'Generate partial summary'
    priority: 'Accomplishments and next steps'

# SUCCESS CRITERIA
success_criteria:
  - summary_generated: 'Document created successfully'
  - key_sections_complete: 'All major sections populated'
  - file_saved: 'Written to correct location'
  - readable_format: 'Clear and organized'

# PERFORMANCE
performance:
  optimization:
    - cache_reads: 'Read files once'
    - parallel_scan: 'Check multiple contexts simultaneously'
    - template_based: 'Fast generation from template'
  
  targets:
    - execution_time: '<10 seconds'
    - file_size: '<10KB'
    - completeness: '>80% sections filled'
```

---

## Usage Examples

### Automatic Execution
Called automatically by close-chat workflow during session closure.

### Manual Execution
```bash
# Generate session summary
*task session-summary

# With custom timestamp
*task session-summary --date 2025-08-26-14-30
```

### Integration Points
- **close-chat workflow**: Primary consumer
- **orchestrator**: Can trigger manually
- **project-memory**: Source of session data
- **chat-sessions directory**: Output location

---

## Output Example

```markdown
# Session Summary - 2025-08-26

**Session ID**: chat-2025-08-26-afternoon
**Duration**: 2 hours 15 minutes
**Agents Used**: orchestrator, architect, developer
**Workflows**: plan-feature, implement-feature, close-chat

## 🎯 Accomplishments
- ✅ Implemented close-chat-workflow feature workspace
- ✅ Created 5-engine orchestrated workflow architecture
- ✅ Generated comprehensive PRD from planning artifacts
- ✅ Established quality gates and validation framework

## 📊 Features Worked
- **close-chat-workflow**: 15% complete (planning ✅, implementation started)
- **memory-learnings-consolidation**: 0% (planned)

## 🧠 Key Decisions
- Architecture: 5-engine orchestrated pattern based on system-sync
- Performance: Three execution modes (standard/quick/force)
- Error Handling: Phase independence with rollback capability

## 📚 Learnings Captured
- Pattern: Orchestrated workflow delegation enables rapid workspace creation
- Learning: Implement-feature workflow works seamlessly with planning artifacts

## 🚧 Blockers & Issues
- None identified this session

## ⏭️ Next Session Focus
1. Complete close-chat workflow implementation
2. Create supporting tasks (feature-archival, closure-report)
3. Integrate with orchestrator command routing
4. Test end-to-end execution

## 📈 Metrics
- Files Created: 7
- Tasks Completed: 5
- Quality Gates: 1/5 passed
- System Health: GREEN

---
*Generated: 2025-08-26T14:30:00Z*
```

This task ensures every session is properly documented for continuity.