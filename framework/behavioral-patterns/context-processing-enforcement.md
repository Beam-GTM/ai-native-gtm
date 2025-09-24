# Context Processing Enforcement Pattern

## 🎯 Purpose
Ensure the system ALWAYS processes user context and cleans up folders automatically, without user intervention or memory dependence.

## 🔄 Automatic Trigger Pattern

### Trigger Condition
```yaml
trigger_when:
  location: "briefing/context_input/"
  condition: "folder contains user files (not just README.md)"
  frequency: "every session startup"
  precedence: "BEFORE any other operations"
```

### Enforcement Logic
```yaml
enforcement:
  detection: "Scan briefing/context_input/ during dynamic context resolution"
  
  if_context_found:
    priority: "HIGHEST - Override all other workflows"
    action: "Execute process-user-context.md task immediately"
    block: "All other operations until context processed"
    message: "🔄 Processing your project context..."
    
  after_processing:
    verify: "Files moved to processed_context/ archive"
    confirm: "Input folder cleaned (only README remains)"
    continue: "With personalized system setup"
    
  if_processing_skipped:
    flag: "CRITICAL ERROR - Context processing bypassed"
    force: "Re-trigger context processing"
    prevent: "System from proceeding without processing"
```

## 📋 Mandatory Processing Steps

### Phase 1: Context Detection (Always Executed)
```yaml
detection_checklist:
  - scan_input_folder: "briefing/context_input/"
  - count_user_files: "exclude README.md and .gitkeep"
  - log_findings: "document what context is available"
  - set_processing_flag: "if any user files found"
```

### Phase 2: Automatic Processing (If Context Found)
```yaml
processing_checklist:
  - execute_task: "framework/tasks/system/process-user-context.md"
  - analyze_content: "extract project information"
  - generate_brief: "create personalized project-brief.md"
  - configure_system: "personalize agents and workflows"
  - archive_files: "move to processed_context/ with timestamp"
  - clean_input: "remove processed files, keep README"
  - validate_cleanup: "verify folder is clean"
  - update_system_state: "mark as personalized"
```

### Phase 3: Verification (Always Executed)
```yaml
verification_checklist:
  - confirm_archive_created: "processed_context/ folder exists"
  - confirm_files_moved: "original files preserved in archive"
  - confirm_input_clean: "only README.md remains in context_input/"
  - confirm_brief_updated: "project-brief.md is personalized"
  - confirm_system_ready: "template indicators removed"
```

## 🚨 Failure Prevention

### Memory Independence
```yaml
memory_independence:
  principle: "Never depend on session memory to trigger processing"
  method: "Check folder state every session startup"
  validation: "File system is the source of truth"
  enforcement: "Built into activation sequence"
```

### Error Recovery
```yaml
error_recovery:
  if_processing_fails:
    preserve: "Original files in context_input/"
    log: "Processing failure details"
    retry: "Attempt processing again next session"
    fallback: "Continue with template setup"
    
  if_partial_processing:
    complete: "Finish archival and cleanup"
    verify: "All files properly handled"
    continue: "With available personalization"
```

### Processing Validation
```yaml
validation_checks:
  before_processing:
    - context_input_has_files: true
    - processed_context_folder_available: true
    - system_has_write_permissions: true
    
  during_processing:
    - files_being_analyzed: true
    - brief_being_generated: true
    - archive_being_created: true
    
  after_processing:
    - all_files_archived: true
    - input_folder_clean: true
    - system_personalized: true
    - template_state_removed: true
```

## 🎯 Integration Points

### Activation Sequence Integration
```yaml
activation_integration:
  position: "Step 2 in dynamic-context-resolver.md"
  precedence: "BEFORE all other operations"
  blocking: "Prevents other workflows until complete"
  mandatory: "Cannot be skipped or postponed"
```

### Orchestrator Commands
```yaml
orchestrator_commands:
  automatic: "Triggered by context detection"
  manual: "@process-context" (if user wants to reprocess)
  status: "@context-status" (check processing state)
  archive: "@view-context-archive" (see processed context)
```

### Behavioral Pattern Registry
```yaml
pattern_registration:
  category: "system-enforcement"
  priority: "critical"
  frequency: "every-session"
  dependencies: ["dynamic-context-resolver", "process-user-context"]
  validates: "context processing never forgotten"
```

## 🔄 Lifecycle Management

### Fresh Template State
```yaml
fresh_template:
  detect: "TEMPLATE-INDICATORS.md exists"
  expect: "User to add context to context_input/"
  trigger: "Process context when files detected"
  result: "Personalized system with clean folders"
```

### Operational State
```yaml
operational_state:
  detect: "No TEMPLATE-INDICATORS.md"
  expect: "Context already processed or none provided"
  verify: "context_input/ folder is clean"
  maintain: "Archive integrity in processed_context/"
```

### Context Updates
```yaml
context_updates:
  detect: "New files added to context_input/"
  trigger: "Incremental context processing"
  merge: "New context with existing personalization"
  archive: "Additional context in dated subfolder"
```

## 💡 User Communication

### Processing Messages
```yaml
user_messages:
  detecting: "🔍 Checking for project context..."
  processing: "🔄 Processing your project context..."
  archiving: "📁 Archiving context files..."
  cleaning: "🧹 Cleaning up input folder..."
  complete: "✅ Context processed and folders organized!"
```

### Status Updates
```yaml
status_updates:
  found_context: "Found {count} context files"
  analyzing: "Analyzing project requirements..."
  personalizing: "Customizing system for your project..."
  archiving: "Moving files to processed_context/{timestamp}/"
  ready: "System personalized and ready to use!"
```

## 📊 Success Metrics

### Processing Success
```yaml
success_criteria:
  context_analyzed: "Project information extracted"
  system_personalized: "Agents configured for domain"
  files_archived: "Original context preserved"
  folders_clean: "Input folder ready for reuse"
  user_notified: "Clear confirmation of completion"
```

### Quality Validation
```yaml
quality_checks:
  no_files_lost: "All original files preserved"
  personalization_applied: "System reflects user's project"
  clean_state_achieved: "Template ready for next user"
  archive_accessible: "Processed context viewable"
```

---

**This pattern ensures context processing is NEVER forgotten and ALWAYS results in clean, organized folders with preserved original context.**