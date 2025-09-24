<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.743416Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.259803Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Update Project Milestone

**Category**: memory-management
**Complexity**: simple
**Prerequisites**: Feature milestone reached, project memory system available

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

### **THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **MANDATORY ENGINEERING RULES LOADING** - Load all required engineering rules before execution
2. **HIERARCHY RESPECT** - Apply top-level rules, then repository-specific overrides  
3. **COMPLIANCE VALIDATION** - All outputs must comply with loaded engineering rules
4. **SEQUENTIAL EXECUTION** - Follow step-by-step workflow with user validation
5. **QUALITY GATE INTEGRATION** - Engineering rules compliance checked at each gate

**VIOLATION INDICATOR:** If you skip rule loading or bypass compliance validation, you have violated this workflow.

## Engineering Rules Integration

### Required Engineering Rules
```yaml
engineering_rules_required:
  # ALWAYS REQUIRED (loaded for every execution)
  primary_rules:
    - framework/engineeringrules/core-foundation/memory-system.md         # Memory management standards
    - framework/engineeringrules/core-foundation/documentation-standards.md # Documentation requirements
    
  # CONDITIONALLY REQUIRED (loaded based on task context)
  contextual_rules:
    - condition: "Pattern extraction triggered (5+ entries)"
      rule: framework/engineeringrules/system-operations/system-generation.md
      reason: "Pattern extraction and generation rules"
    - condition: "Memory rotation needed (30+ entries)"
      rule: framework/engineeringrules/core-foundation/file-management.md
      reason: "Archive and rotation procedures"
    
  # REPOSITORY-SPECIFIC (loaded based on implementation target)
  repository_specific:
    - repository: nexus-base
      rules: [framework/engineeringrules/core-foundation/memory-system.md]
      override_behavior: "memory_specific_enhancements"

rule_application_context:
  load_timing: "During task prerequisite validation phase"
  scope: "Apply throughout memory update process"
  inheritance: "Top-level rules + repository-specific overrides"
  validation: "Memory entry format and pattern detection"
  conflict_resolution: "Repository-specific overrides top-level"
```

### Rule Loading Strategy
```yaml
loading_strategy:
  phase_1_always_load:
    - framework/engineeringrules/core-foundation/memory-system.md: "Memory entry standards"
    - framework/engineeringrules/core-foundation/documentation-standards.md: "Entry documentation"
    
  phase_2_context_based:
    - if: "entry_count >= 5 AND entry_count % 5 == 0"
      load: framework/engineeringrules/system-operations/system-generation.md
      apply: "Pattern extraction triggers"
    - if: "entry_count >= 30"
      load: framework/engineeringrules/core-foundation/file-management.md
      apply: "Memory rotation procedures"
      
  phase_3_repository_specific:
    detection_method: "workspace/memory/project-memory.md location"
    loading_pattern: "load + enhance"
    conflict_resolution: "preserve_memory_integrity"
```

## Prerequisites

**BEFORE STARTING THIS TASK:**

### Context Loading and Validation

**Context Loading Sequence:**
```yaml
context_loading_sequence:
  step_1_memory_context:
    location: "workspace/memory/"
    files: ["project-memory.md"]
    validation: "Project memory file exists and is writeable"
  
  step_2_feature_context:
    location: "workspace/features/active/{feature-name}/"
    files: ["active-context.md", "progress.md"]
    validation: "Feature context available for milestone extraction"
  
  step_3_pattern_context:
    condition: "if entry_count >= 5"
    location: "workspace/memory/patterns/"
    files: ["extracted/", "suggestions/active.md"]
    validation: "Pattern directories exist for extraction"
  
  step_4_context_consistency:
    validation_points:
      - "Entry count is accurate"
      - "Timestamp format is consistent"
      - "Pattern detection triggers are valid"
      - "Memory format is preserved"
```

**Context Update Triggers:**
```yaml
context_update_triggers:
  during_task_execution:
    - trigger: "milestone_identified"
      update: "workspace/features/active/{feature-name}/active-context.md"
      content: "Milestone captured for memory update"
    
    - trigger: "pattern_detected"
      update: "workspace/memory/patterns/extracted/{pattern-name}.md"
      content: "New pattern extracted from entries"
    
    - trigger: "memory_updated"
      update: "workspace/memory/project-memory.md"
      content: "New milestone entry added"
  
  post_task_completion:
    - update: "workspace/memory/project-memory.md"
      content: "Updated with new milestone entry"
    - update: "workspace/memory/suggestions/active.md"
      content: "Pattern suggestions if threshold reached"
```

### Validation Requirements

**Pre-Execution Validation:**
- [ ] Verify workspace/memory/project-memory.md exists
- [ ] Check current entry count (must be < 30)
- [ ] Validate milestone context is available

**Quality Gates During Execution:**
- [ ] Entry format validation
- [ ] Pattern detection check
- [ ] Memory integrity verification

**Post-Execution Validation:**
- [ ] Verify entry was added correctly
- [ ] Check pattern extraction if triggered
- [ ] Validate memory file structure intact

### Engineering Rules Loading (MANDATORY)
- [ ] Load memory-system.md for standards
- [ ] Load documentation-standards.md for format
- [ ] Check for pattern extraction rules if needed
- [ ] Confirm rule application approach

### Required Inputs
- [ ] Milestone action description
- [ ] Context details for the milestone
- [ ] Milestone type (feature_milestone, system_milestone, etc.)
- [ ] Pattern category if applicable

### Required Agent State
- [ ] Agent has memory system rules loaded
- [ ] Agent can detect patterns
- [ ] Agent can update memory safely
- [ ] Agent understands rotation triggers

### Environmental Requirements
- [ ] Write access to workspace/memory/
- [ ] User available for milestone details
- [ ] Pattern directories exist if needed

**CRITICAL:** If memory file is corrupted or missing, STOP and request recovery.

## Task Execution Workflow

### Step 1: Engineering Rules Loading & Validation

**Rule Loading Sequence:**

1. **Load Primary Rules** (Always Required)
   ```bash
   - Read framework/engineeringrules/core-foundation/memory-system.md
   - Parse memory entry format requirements
   - Read framework/engineeringrules/core-foundation/documentation-standards.md
   - Parse documentation formatting rules
   ```

2. **Context-Based Rule Loading**
   ```yaml
   rule_loading_logic:
     pattern_extraction:
       condition: "entry_count >= 5 AND entry_count % 5 == 0"
       load: [system-generation.md]
       apply_to: "Pattern extraction procedures"
     memory_rotation:
       condition: "entry_count >= 30"
       load: [file-management.md]
       apply_to: "Archive and rotation procedures"
   ```

**Engineering Rules Validation** 🔴

Present loaded rules summary to user:

**Loaded Engineering Rules:**
- ✅ **Memory System**: Entry format and pattern detection
- ✅ **Documentation Standards**: Consistent formatting
- ✅ **Pattern Extraction**: (if applicable)
- ✅ **File Management**: (if rotation needed)

**Rule Application Confirmation:**

1. **Apply all rules** - Full compliance mode
2. **Quick update** - Minimal validation
3. **Pattern focus** - Emphasize pattern detection
4. **Custom format** - User-defined entry format

**WAIT FOR USER RESPONSE** - Ensure approach confirmed.

### Step 2: Gather Milestone Information

**Collect Milestone Details from User:**

**Current Project State:**
- **Entry Count**: {current_count}/30
- **Last Entry**: {timestamp and action}
- **Pattern Check**: Next at {next_threshold} entries
- **Active Feature**: {feature-name if applicable}

**Milestone Information Needed:**

1. **Action** - What was accomplished? (e.g., "Completed feature X", "Enhanced workflow Y")
2. **Context** - Additional details about the milestone
3. **Type** - Milestone category:
   - `feature_milestone` - Feature-related progress
   - `system_milestone` - System-level changes
   - `workflow_milestone` - Workflow improvements
   - `architecture_milestone` - Architecture decisions
   - `quality_milestone` - Quality improvements
4. **Pattern** - Recurring pattern observed? (optional)

**MANDATORY:** Collect all milestone details before proceeding.

### Step 3: Read and Validate Current Memory

**Load Current Memory State:**

```bash
# Read current project-memory.md
Read workspace/memory/project-memory.md
```

**Validate Memory Structure:**
- Entry count matches header declaration
- Timestamps are in correct format (ISO 8601)
- Entry structure is consistent
- Pattern triggers are correctly set
- No corruption or formatting issues

**Extract Key Information:**
- Current entry count
- Next pattern check threshold
- Available suggestions count
- Latest entry timestamp

### Step 4: Create New Memory Entry

**Format New Entry According to Standards:**

```markdown
## Entry {next_number} | {current_timestamp}
- ACTION: {milestone_action}
- CONTEXT: {milestone_context}
- MILESTONE: {milestone_type}
- PATTERN: {observed_pattern or "N/A"}
```

**Entry Validation:**
- ACTION is concise and clear (< 100 chars)
- CONTEXT provides sufficient detail
- MILESTONE uses valid type
- PATTERN identifies recurring theme if applicable

### Step 5: Update Project Memory File

**Insert New Entry and Update Headers:**

```markdown
# PROJECT MEMORY | Updated: {current_timestamp} | Entries: {new_count}/30

**PATTERN CHECK**: {status} (next at {threshold} entries)
**SUGGESTIONS**: {count} available ({confidence}% confidence)
**SUPERSEDES**: workspace/memory/active-context.md

## Entry {new_number} | {timestamp}
- ACTION: {action}
- CONTEXT: {context}
- MILESTONE: {milestone_type}
- PATTERN: {pattern}

[Previous entries follow...]
```

**Maintain Entry Order:**
- New entry goes after "Latest Entry" or as "Entry {n}"
- Previous "Latest Entry" becomes "Entry {n-1}"
- Preserve all existing entries

### Step 6: Pattern Detection (If Triggered)

**Check Pattern Detection Triggers:**

```yaml
pattern_detection:
  trigger_check:
    - condition: "entry_count % 5 == 0"
      action: "Analyze last 5 entries for patterns"
    - condition: "entry_count == 10, 15, 20, 25"
      action: "Comprehensive pattern analysis"
      
  pattern_analysis:
    categories:
      - workflow_patterns: "Repeated workflow usage"
      - feature_patterns: "Common feature types"
      - quality_patterns: "Recurring quality improvements"
      - architecture_patterns: "System design decisions"
```

**If Patterns Detected:**

1. **Extract Pattern** to workspace/memory/patterns/extracted/{pattern-name}.md
2. **Generate Suggestion** to workspace/memory/suggestions/active.md
3. **Update Memory Header** with pattern detection results

### Step 7: Memory Rotation (If Needed)

**Check Rotation Trigger:**

```yaml
rotation_check:
  trigger: "entry_count >= 30"
  action:
    - Archive entries 1-15 to workspace/memory/archive/
    - Keep entries 16-30 as new 1-15
    - Reset counter to 15
    - Update pattern check thresholds
```

**If Rotation Required:**
1. Create archive file with timestamp
2. Move oldest entries to archive
3. Renumber remaining entries
4. Update header counters
5. Preserve pattern history

### Quality Gate: Memory Update Validation

**Compliance Assessment Framework:**

```yaml
compliance_assessment:
  memory_integrity:
    rules_source: framework/engineeringrules/core-foundation/memory-system.md
    criteria: "Memory structure preserved and valid"
    evidence_required: "Before/after comparison"
    assessment_method: "Structure validation"
    pass_threshold: "100% structure integrity"
    
  entry_format:
    rules_source: framework/engineeringrules/core-foundation/documentation-standards.md
    criteria: "Entry follows standard format"
    evidence_required: "Entry format check"
    assessment_method: "Format validation"
    pass_threshold: "All required fields present"
```

**Detailed Compliance Check:**

#### Memory System Compliance
**Criteria from memory-system.md:**
- Memory file structure intact
- Entry format consistent
- Pattern triggers accurate
- Rotation handled properly

**Evidence Collection:**
- [x] Entry added successfully
- [x] Count updated correctly
- [x] Timestamps valid

**Assessment**: {PASS/CONCERNS/FAIL/WAIVED}

**Engineering Rules Quality Decision** 🔴

Based on compliance assessment:

1. **FULL COMPLIANCE** - Memory updated successfully
2. **MINOR ISSUES** - Update successful with notes
3. **NEEDS CORRECTION** - Fix issues before saving
4. **ROLLBACK REQUIRED** - Restore previous state

**Context Update After Quality Gate:**
```yaml
post_quality_gate_context_update:
  location: "workspace/features/active/{feature-name}/active-context.md"
  content: |
    ## Milestone Recorded - {timestamp}
    **Entry Number**: {entry_number}
    **Milestone Type**: {milestone_type}
    **Pattern Detection**: {yes/no}
    **Memory Status**: Updated successfully
```

## Task Outputs with Engineering Rules Compliance

### Primary Deliverable
**Document Type**: Updated Project Memory
**Location**: workspace/memory/project-memory.md
**Format**: Structured memory entries
**Engineering Rules Compliance**: Full compliance with memory standards

**Required Sections (Rule-Driven):**
```yaml
document_structure:
  sections:
    - header:
        required: true
        rule_source: framework/engineeringrules/core-foundation/memory-system.md
        content: "Timestamp, entry count, pattern status"
        
    - entries:
        required: true
        rule_source: framework/engineeringrules/core-foundation/memory-system.md
        content: "ACTION, CONTEXT, MILESTONE, PATTERN fields"
        
    - triggers:
        required: true
        rule_source: framework/engineeringrules/core-foundation/memory-system.md
        content: "Pattern and rotation trigger comments"
```

### Engineering Rules Compliance Documentation
**Compliance Report**:
- **Rules Applied**: Memory system and documentation standards
- **Compliance Level**: 100% required for memory integrity
- **Entry Format**: Validated against standards
- **Pattern Detection**: Executed if triggered

### Secondary Deliverables
- **Pattern Extraction**: (if triggered) New pattern file
- **Suggestions Update**: (if triggered) Active suggestions
- **Archive File**: (if rotation) Historical entries

### Validation Checklist
- [ ] Memory file updated with new entry
- [ ] Entry count accurate in header
- [ ] Timestamp updated to current
- [ ] Pattern detection executed if triggered
- [ ] Rotation handled if at 30 entries
- [ ] File structure remains valid
- [ ] Context files updated

### Context Handoff Preparation
**Task Completion Context Updates:**
```yaml
task_completion_context_handoff:
  primary_context_update:
    location: "workspace/memory/project-memory.md"
    content: "New milestone entry added"
  
  feature_context_update:
    location: "workspace/features/active/{feature-name}/active-context.md"
    content: |
      ## Milestone Recorded - {timestamp}
      **Task**: update-project-milestone - COMPLETED
      **Entry Added**: Entry {number}
      **Pattern Status**: {detected/not detected}
      **Next Pattern Check**: At {threshold} entries
```

### Context Validation Checklist (Enhanced)
- [ ] Project memory updated successfully
- [ ] Entry format validated
- [ ] Pattern detection completed if triggered
- [ ] Context files reflect milestone
- [ ] Memory integrity maintained