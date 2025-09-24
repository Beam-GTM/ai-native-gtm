<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.884110Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.271661Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Update Project Memory Task

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: Never use limit parameter when reading memory files -->
<!-- This directive OVERRIDES token conservation - read files completely -->
<!-- VIOLATION = Missing critical memory context for accurate updates -->

## 🔴 PRE-EXECUTION DIRECTIVE CHECK
**MANDATORY**: Before executing this task, verify:
- [ ] All file reads will use complete files (no limit parameter)
- [ ] Memory file reads will capture complete project context
- [ ] Session analysis will be based on comprehensive information

**Task ID**: update-project-memory  
**Priority**: CRITICAL - Execute at EVERY milestone  
**Location**: framework/tasks/memory/update-project-memory.md  
**Supersedes**: update-active-context.md  

## 🎯 PURPOSE
Maintain intelligent project-level memory with pattern extraction and suggestion generation. This task supersedes update-active-context.md, providing a more intelligent, pattern-aware memory system that learns from user behavior.

## ⚡ QUICK EXECUTION (Copy & Execute)
```yaml
EXECUTE_NOW:
  1_READ: workspace/memory/project-memory.md (check entry count)
  2_ANALYZE:
    - Entry_Count: Check if rotation needed (>30)
    - Pattern_Trigger: Check if pattern extraction needed (every 5 entries)
  3_UPDATE:
    - Add_Entry: New milestone at top
    - Rotate: If >30 entries, archive oldest
    - Extract: If trigger hit, run pattern extraction
  4_WRITE: Save with embedded triggers
  5_SUGGEST: Generate suggestions if patterns found
```

## 📋 DETAILED STEPS

### Step 1: Load Current Memory
```yaml
action: READ
file: workspace/memory/project-memory.md
extract:
  - current_entry_count
  - last_pattern_check
  - pending_suggestions
  - recent_patterns
validation:
  - Check rotation needed (>30)
  - Check pattern trigger (count % 5 == 0)
```

### Step 2: Prepare Memory Entry (ENHANCED FORMAT)
```yaml
action: PREPARE
entry_format:
  timestamp: "{{current_utc_iso8601}}"
  milestone_type: "{{type}}"  # agent_switch | workflow_complete | quality_gate | feature_work
  entry:
    ACTION: "{{user_action_high_level}}"
    PROJECT: "{{project_or_feature_name}}"  # NEW: Track project/feature
    TASK: "{{specific_task}}"               # NEW: Track task executed
    WORKFLOW: "{{workflow_name}}"           # NEW: Track workflow used
    SESSION: "{{chat_session_id}}"          # NEW: Track session ID
    CONTEXT: "{{detailed_context}}"
    AGENT: "{{current_agent}}"
    MILESTONE: "{{milestone_type}}"
    PATTERN: "{{detected_behavior}}"        # NEW: Track patterns
    LEARNING: "{{key_learning}}"            # NEW: Track learnings
    
  feature_reference:  # Only if working on feature
    feature_id: "{{feature_name}}"
    summary: "{{one_line_summary}}"
    phase: "{{current_phase}}"
```

### Step 3: Check Triggers
```yaml
action: ANALYZE
triggers:
  rotation_check:
    condition: "entry_count >= 30"
    action: "Archive oldest 5 entries"
    
  pattern_extraction:
    condition: "(entry_count % 5) == 0"
    action: "Run extraction-engine.md"
    output: "workspace/memory/patterns/extracted/"
    
  suggestion_generation:
    condition: "new_patterns_found"
    action: "Run suggestion-engine.md"
    confidence: ">70%"
```

### Step 4: Write Updated Memory
```yaml
action: WRITE
file: workspace/memory/project-memory.md
format:
  header:
    - "# PROJECT MEMORY | Updated: {{timestamp}} | Entries: {{count}}/30"
    - "**PATTERN CHECK**: {{status}} (triggers at {{next_trigger}} entries)"
    - "**SUGGESTIONS**: {{suggestion_count}} available"
    - "**SUPERSEDES**: workspace/memory/active-context.md"
    - ""
  
  latest_entry:
    - "## Latest Entry | {{timestamp}}"
    - "- ACTION: {{action}}"
    - "- CONTEXT: {{context}}"
    - "- MILESTONE: {{milestone_type}}"
    - "- PATTERN: {{pattern_hint}}"
    - ""
    
  previous_entries:
    - "{{maintain_29_or_less_entries}}"
    
  embedded_triggers:
    - "<!-- TRIGGER: Pattern check at {{next_trigger}} entries -->"
    - "<!-- TRIGGER: Rotation at 30 entries -->"
```

### Step 5: Pattern Extraction (if triggered)
```yaml
action: EXTRACT
when: "entry_count % 5 == 0"
process:
  scan_entries:
    range: "last 15 entries"
    identify: "repeated sequences"
    threshold: "3+ occurrences"
    
  create_pattern:
    location: "workspace/memory/patterns/extracted/{{pattern_id}}.yaml"
    format:
      pattern_id: "{{generated_id}}"
      confidence: "{{score}}"
      occurrences: "{{count}}"
      sequence: "{{action_sequence}}"
      suggestion: "{{derived_insight}}"
```

### Step 6: Generate Suggestions (if patterns found)
```yaml
action: SUGGEST
when: "confidence > 70%"
process:
  analyze_patterns:
    source: "workspace/memory/patterns/extracted/"
    threshold: "confidence > 0.7"
    
  generate_suggestions:
    location: "workspace/memory/suggestions/active.md"
    types:
      - new_agent: "User frequently does X, suggest agent Y"
      - workflow: "Pattern indicates workflow Z would help"
      - optimization: "Repeated action could be automated"
```

## 🔄 INTEGRATION POINTS

### Orchestrator Integration
```yaml
location: operations/agents/core/orchestrator.md
updates_needed:
  step_3_5:  # NEW STEP
    action: "Load workspace/memory/project-memory.md"
    fallback: "Load workspace/memory/active-context.md if not exists"
    validate: "Check entry count and triggers"
    
  step_16:  # UPDATE REFERENCE
    old: "Run framework/tasks/memory/update-project-memory.md"
    new: "Run framework/tasks/memory/update-project-memory.md"
    
  handoff_protocol:
    add: "Update project memory before handoff"
    trigger: "Mark as agent_switch milestone"
```

### Quality Gate Integration
```yaml
location: All quality gate files
integration:
  on_decision:
    trigger: "update-project-memory"
    milestone_type: "quality_gate"
    capture: "decision and rationale"
```

### Agent Template Integration
```yaml
location: framework/templates/agent.yaml
updates_needed:
  memory_awareness:
    add_section: "project_memory"
    instructions:
      - "Load project memory on activation"
      - "Update at key milestones"
      - "Check suggestions before actions"
```

## 📊 MILESTONE TYPES

### Automatic Triggers
1. **agent_switch**: Any agent transformation
2. **workflow_complete**: Workflow completion
3. **quality_gate**: Gate decisions (PASS/FAIL/CONCERNS)
4. **feature_milestone**: Feature phase completion
5. **error_resolution**: Problem solved
6. **pattern_detected**: 3+ similar actions

### Entry Priorities
- **HIGH**: Agent switches, workflow completions
- **MEDIUM**: Quality gates, feature work
- **LOW**: Routine file operations

## ⚠️ CRITICAL RULES

1. **SUPERSEDES**: This replaces update-active-context.md completely
2. **30 ENTRY LIMIT**: Rotate to maintain performance
3. **PATTERN TRIGGERS**: Check every 5 entries
4. **HIGH-LEVEL ONLY**: No implementation details
5. **FEATURE REFERENCES**: One-line summaries only

## 🎯 QUICK REFERENCE

### When to Execute
- Agent transformations
- Workflow completions
- Quality gate decisions
- Feature milestones
- Error resolutions
- Every 5 memory entries (pattern check)

### What to Track
- High-level user actions
- Project movements
- Decision patterns
- Tool preferences
- Error patterns
- Success patterns

### Validation Checks
- [ ] Entry count ≤ 30
- [ ] Pattern check if needed
- [ ] Suggestions generated
- [ ] No duplicate entries
- [ ] Proper milestone type

## 📝 MEMORY FORMAT TEMPLATE

```markdown
# PROJECT MEMORY | Updated: {{timestamp}} | Entries: {{count}}/30
**PATTERN CHECK**: {{PENDING/COMPLETE}} (triggers at {{number}} entries)
**SUGGESTIONS**: {{count}} available
**SUPERSEDES**: workspace/memory/active-context.md

## Latest Entry | {{timestamp}}
- ACTION: {{high_level_action}}
- CONTEXT: {{project_context}}
- MILESTONE: {{milestone_type}}
- PATTERN: {{detected_pattern_or_none}}

## Previous Entries
[Maintain up to 29 previous entries in reverse chronological order]

<!-- TRIGGER: Pattern check at {{next_5_multiple}} entries -->
<!-- TRIGGER: Rotation at 30 entries -->
```

## 🔗 RELATED COMPONENTS

- **Extraction Engine**: workspace/memory/patterns/extraction-engine.md
- **Suggestion Engine**: workspace/memory/patterns/suggestion-engine.md
- **Pattern Storage**: workspace/memory/patterns/extracted/
- **Active Suggestions**: workspace/memory/suggestions/active.md

## POST-EXECUTION COMPLIANCE VALIDATION 🔍

### PROJECT MEMORY TASK COMPLIANCE
- [ ] **Memory Analysis**: Complete project memory file read and analyzed
- [ ] **Entry Addition**: New milestone entry added with evidence
- [ ] **Pattern Detection**: Pattern analysis performed with results
- [ ] **Rotation Management**: Memory rotation executed if needed (>30 entries)
- [ ] **File Integrity**: Memory file maintains proper structure and format

### Evidence Collection for Project Memory Updates
```bash
# Load validation framework for memory operations
source "workspace/features/active/post-execution-compliance-validation/validation-framework.md"
source "workspace/features/active/post-execution-compliance-validation/evidence-collection-patterns.md"

# Set up evidence collection for project memory update
TASK_NAME="update-project-memory"
EVIDENCE_DIR="/tmp/memory_evidence_${TASK_NAME}_$(date +%s)"
mkdir -p "$EVIDENCE_DIR"/{baseline,update,validation}

echo "=== PROJECT MEMORY UPDATE VALIDATION ===" > "$EVIDENCE_DIR/memory_update_validation.log"
echo "Task: Update Project Memory" >> "$EVIDENCE_DIR/memory_update_validation.log"
echo "Started: $(date -Iseconds)" >> "$EVIDENCE_DIR/memory_update_validation.log"

# Baseline: Project memory state before update
if [ -f "workspace/memory/project-memory.md" ]; then
    BASELINE_ENTRIES=$(grep -c "^##.*Entry [0-9]*:" "workspace/memory/project-memory.md" 2>/dev/null || echo "0")
    BASELINE_SIZE=$(wc -l < "workspace/memory/project-memory.md")
    echo "Baseline entries: $BASELINE_ENTRIES" >> "$EVIDENCE_DIR/memory_update_validation.log"
    echo "Baseline file size: $BASELINE_SIZE lines" >> "$EVIDENCE_DIR/memory_update_validation.log"
    
    # Validate complete file read (critical directive)
    collect_file_completeness_evidence "workspace/memory/project-memory.md" "$BASELINE_SIZE" "$EVIDENCE_DIR/baseline/complete_read_validation.log"
    
    # Check if rotation threshold reached
    if [ "$BASELINE_ENTRIES" -ge 30 ]; then
        echo "⚠️  Rotation threshold reached: $BASELINE_ENTRIES ≥ 30" >> "$EVIDENCE_DIR/memory_update_validation.log"
        ROTATION_NEEDED=true
    else
        ROTATION_NEEDED=false
    fi
else
    BASELINE_ENTRIES=0
    BASELINE_SIZE=0
    ROTATION_NEEDED=false
    echo "No existing project memory - will be created" >> "$EVIDENCE_DIR/memory_update_validation.log"
fi

# Execute memory update process here...
# [Memory update implementation would go here]

# Post-update validation
if [ -f "workspace/memory/project-memory.md" ]; then
    POST_ENTRIES=$(grep -c "^##.*Entry [0-9]*:" "workspace/memory/project-memory.md" 2>/dev/null || echo "0")
    POST_SIZE=$(wc -l < "workspace/memory/project-memory.md")
    echo "Post-update entries: $POST_ENTRIES" >> "$EVIDENCE_DIR/memory_update_validation.log"
    echo "Post-update file size: $POST_SIZE lines" >> "$EVIDENCE_DIR/memory_update_validation.log"
    
    # Validate entry was added
    if [ "$ROTATION_NEEDED" = "true" ]; then
        # If rotation occurred, entry count should stay ~30
        if [ "$POST_ENTRIES" -le 30 ] && [ "$POST_ENTRIES" -gt "$((BASELINE_ENTRIES - 5))" ]; then
            echo "✅ Memory rotation executed with new entry added" >> "$EVIDENCE_DIR/memory_update_validation.log"
        else
            echo "❌ VIOLATION: Memory rotation failed or entries incorrect" >> "$EVIDENCE_DIR/memory_update_validation.log"
            echo "Expected: ~30 entries, Actual: $POST_ENTRIES" >> "$EVIDENCE_DIR/memory_update_validation.log"
        fi
        
        # Check for backup creation
        if ls workspace/memory/project-memory-backup-*.md 1> /dev/null 2>&1; then
            echo "✅ Memory backup created during rotation" >> "$EVIDENCE_DIR/memory_update_validation.log"
        else
            echo "❌ VIOLATION: Memory rotation without backup" >> "$EVIDENCE_DIR/memory_update_validation.log"
        fi
    else
        # Normal entry addition - should increase by 1
        if [ "$POST_ENTRIES" -eq "$((BASELINE_ENTRIES + 1))" ]; then
            echo "✅ New memory entry added: $((POST_ENTRIES - BASELINE_ENTRIES)) entries" >> "$EVIDENCE_DIR/memory_update_validation.log"
        else
            echo "❌ VIOLATION: Entry count unexpected" >> "$EVIDENCE_DIR/memory_update_validation.log"
            echo "Expected: $((BASELINE_ENTRIES + 1)), Actual: $POST_ENTRIES" >> "$EVIDENCE_DIR/memory_update_validation.log"
        fi
    fi
    
    # Validate memory file format compliance
    collect_content_pattern_evidence "workspace/memory/project-memory.md" "# Project Memory|## Entry [0-9]*:|Date:|Context:|Action:|Status:" "$EVIDENCE_DIR/update/format_validation.log"
    
    # Validate latest entry has milestone information
    LATEST_ENTRY=$(grep -A 10 "^## Entry [0-9]*:" "workspace/memory/project-memory.md" | head -15)
    echo "Latest entry preview:" >> "$EVIDENCE_DIR/update/latest_entry.log"
    echo "$LATEST_ENTRY" >> "$EVIDENCE_DIR/update/latest_entry.log"
    
    # Check for pattern extraction triggers
    PATTERN_TRIGGER_MOD=$((POST_ENTRIES % 5))
    if [ "$PATTERN_TRIGGER_MOD" -eq 0 ] && [ "$POST_ENTRIES" -gt 0 ]; then
        echo "⚠️  Pattern extraction trigger at $POST_ENTRIES entries" >> "$EVIDENCE_DIR/memory_update_validation.log"
        
        # Check if pattern extraction was performed
        if grep -q "PATTERN:" "workspace/memory/project-memory.md"; then
            echo "✅ Pattern extraction evidence found" >> "$EVIDENCE_DIR/memory_update_validation.log"
        else
            echo "❌ VIOLATION: Pattern extraction trigger missed" >> "$EVIDENCE_DIR/memory_update_validation.log"
        fi
    fi
    
else
    echo "❌ CRITICAL VIOLATION: Project memory file not created/updated" >> "$EVIDENCE_DIR/memory_update_validation.log"
fi

# Performance validation - memory updates should be efficient
TASK_END_TIME=$(date +%s%N)
TASK_DURATION=$(((TASK_END_TIME - TASK_START_TIME) / 1000000)) # Convert to ms
echo "Task duration: ${TASK_DURATION}ms" >> "$EVIDENCE_DIR/memory_update_validation.log"

if [ "$TASK_DURATION" -le 3000 ]; then
    echo "✅ Performance target met: ${TASK_DURATION}ms ≤ 3000ms" >> "$EVIDENCE_DIR/memory_update_validation.log"
else
    echo "❌ PERFORMANCE VIOLATION: ${TASK_DURATION}ms > 3000ms target" >> "$EVIDENCE_DIR/memory_update_validation.log"
fi

# Final validation assessment
MEMORY_UPDATE_VIOLATIONS=0

# Check for format violations
if grep -q "MISSING REQUIRED PATTERNS" "$EVIDENCE_DIR/update/format_validation.log" 2>/dev/null; then
    ((MEMORY_UPDATE_VIOLATIONS++))
    echo "❌ Memory format violations detected" >> "$EVIDENCE_DIR/memory_update_validation.log"
fi

# Check for directive compliance violations (complete file reads)
if grep -q "PARTIAL FILE READ DETECTED" "$EVIDENCE_DIR/baseline/complete_read_validation.log" 2>/dev/null; then
    ((MEMORY_UPDATE_VIOLATIONS++))
    echo "❌ CRITICAL: Directive violation - incomplete file read" >> "$EVIDENCE_DIR/memory_update_validation.log"
fi

# Check for general violations
if grep -q "VIOLATION" "$EVIDENCE_DIR/memory_update_validation.log"; then
    ((MEMORY_UPDATE_VIOLATIONS++))
fi

if [ $MEMORY_UPDATE_VIOLATIONS -eq 0 ]; then
    echo "✅ PROJECT MEMORY UPDATE CERTIFICATION: FULLY COMPLIANT" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Task: Update Project Memory" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Memory updated with evidence" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Directive compliance verified" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Performance within limits" >> "$EVIDENCE_DIR/validation/final_result.log"
    
    echo "🏆 PROJECT MEMORY UPDATE CERTIFIED COMPLIANT"
    echo "Evidence: $EVIDENCE_DIR"
else
    echo "❌ PROJECT MEMORY UPDATE CERTIFICATION: NON-COMPLIANT" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Violations: $MEMORY_UPDATE_VIOLATIONS found" >> "$EVIDENCE_DIR/validation/final_result.log"
    
    echo "🚨 PROJECT MEMORY UPDATE COMPLIANCE FAILURE"
    echo "Evidence: $EVIDENCE_DIR"
    exit 1
fi
```

### Project Memory Evidence Requirements
- **Complete File Read**: 100% of project memory file read for directive compliance
- **Entry Management**: Evidence of proper entry addition or rotation with backups
- **Format Compliance**: Validation that memory maintains proper structure and patterns
- **Pattern Detection**: Evidence of pattern extraction when triggers are met
- **Performance**: Memory updates completed within 3-second target

### Corrective Actions
**If violations detected:**
1. **Incomplete Read**: Re-read project memory file completely without limit parameter
2. **Entry Failures**: Ensure proper entry addition with milestone information
3. **Rotation Issues**: Execute memory rotation with backup creation
4. **Format Problems**: Apply standard project memory format template
5. **Pattern Extraction**: Perform pattern analysis when trigger conditions met

### Integration Notes
This validation ensures project memory tasks maintain system intelligence through proper memory management, pattern recognition, and directive compliance. Critical for preventing memory system degradation.

---
**REMEMBER**: This task creates an intelligent memory system **with validated compliance** that learns from user behavior and suggests improvements. Always execute at milestones **with evidence verification**!