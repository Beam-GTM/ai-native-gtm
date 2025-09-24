<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.802716Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.265891Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Aggregate Core Learnings
**Type**: Pattern Consolidation  
**Category**: Memory & Intelligence  
**Priority**: HIGH  
**Created**: 2025-08-26T16:00:00Z  

## Purpose
Aggregate all core primitive patterns and learnings into a consolidated file that's always loaded by the orchestrator, providing immediate access to all documented LLM behavioral patterns and limitations.

## Trigger Conditions
- **Automatic**: When learnings.md reaches 20+ entries (memory full)
- **Automatic**: When new pattern file added to patterns/ directory
- **Manual**: Command `*aggregate-learnings` or `*consolidate-patterns`
- **Scheduled**: After every 5 new learnings added
- **Critical**: Before memory rotation to preserve insights

## Aggregation Process

### 1. Source Locations
```yaml
source_files:
  primary:
    - workspace/memory/core-primitives/learnings.md
    - workspace/memory/core-primitives/patterns/*.md
  
  secondary:
    - workspace/memory/core-primitives/chat-sessions/*.md
    - workspace/features/completed/core-primitives-learning/*.md

  output:
    - workspace/memory/core-learnings.md  # Always loaded by orchestrator
```

### 2. Aggregation Steps

#### Step 1: Collect All Patterns
```yaml
pattern_collection:
  - Read all .md files from patterns/ directory
  - Extract pattern name, severity, category
  - Count occurrences across learnings.md
  - Identify relationships between patterns
```

#### Step 2: Analyze Learnings
```yaml
learning_analysis:
  - Group learnings by category
  - Identify top 10 most critical learnings
  - Extract actionable lessons
  - Find patterns mentioned 3+ times
```

#### Step 3: Generate Core Learnings
```yaml
core_learnings_structure:
  header:
    - Total learnings count
    - Total patterns identified
    - Last update timestamp
    - Memory status (% full)
  
  critical_patterns:
    - Pattern name
    - Frequency
    - Severity
    - Mitigation strategy
    
  top_learnings:
    - Learning number
    - Key lesson
    - Applicable contexts
    
  action_items:
    - What to ALWAYS do
    - What to NEVER do
    - What to VERIFY first
```

### 3. Output Format
```markdown
# CORE LEARNINGS | Updated: YYYY-MM-DDTHH:MM:SSZ
**Status**: {learnings_count} learnings | {patterns_count} patterns | Memory {percentage}% full

## 🚨 CRITICAL PATTERNS (Always Active)

### 1. {Pattern Name} - Severity: {HIGH/MEDIUM/LOW}
**Frequency**: Observed {N} times
**Mitigation**: {One-line strategy}
**Remember**: {Key lesson}

### 2. {Next Pattern}...

## 📚 TOP 10 LEARNINGS (Must Remember)

1. **{Learning Name}**: {Key lesson in one sentence}
2. **{Next Learning}**: {Key lesson}
...

## ✅ ALWAYS DO
- {Action based on patterns}
- {Verification step}
- {Best practice}

## ❌ NEVER DO  
- {Common mistake to avoid}
- {Overengineering pattern}
- {False capability claim}

## 🔍 VERIFY FIRST
- {What to check before claiming}
- {Reality check needed}
- {Validation required}

## 📊 PATTERN STATISTICS
- **Most Common**: {pattern} ({N} occurrences)
- **Most Severe**: {pattern} (impacts {area})
- **Latest**: {pattern} (discovered {date})

## 🎯 QUICK REFERENCE
When you encounter:
- **Complexity** → Check for overengineering (Learning #1)
- **Counts/Status** → Trust but verify (Pattern: trust-but-verify)
- **Validation** → Execute don't just read (Learning #15)
- **Features** → Load context first (Learning #17)
```

### 4. Integration Rules

#### Memory Management
```yaml
memory_thresholds:
  warning: 15 learnings  # Start monitoring
  full: 20 learnings     # Trigger aggregation
  critical: 25 learnings # Force rotation
  
rotation_preservation:
  - Aggregate before rotation
  - Preserve patterns in core-learnings.md
  - Archive raw learnings
  - Reset counter but keep patterns
```

#### Orchestrator Integration
```yaml
orchestrator_loading:
  when: "Step 3 of activation sequence"
  file: "workspace/memory/core-learnings.md"
  priority: "HIGH - load immediately"
  cache: "Session persistent"
  
usage:
  - Reference during decision making
  - Check before complex operations
  - Validate against known patterns
  - Prevent repeat mistakes
```

### 5. Pattern Relationship Mapping
```yaml
relationship_detection:
  - Identify pattern chains (A leads to B)
  - Group related patterns
  - Find root causes
  - Map mitigation strategies
  
example:
  chain: "overengineering → validation-failure → post-hoc-rationalization"
  root_cause: "Not acknowledging LLM limitations"
  mitigation: "Start simple, test early, be honest"
```

## Auto-Trigger Implementation

### Memory Full Detection
```yaml
memory_check:
  trigger_points:
    - After capture-primitive-learning execution
    - During update-project-memory task
    - On session closure
    
  check_logic:
    if: learnings.md line_count > 20
    then: 
      - Execute aggregate-core-learnings
      - Update core-learnings.md
      - Alert user about memory status
      - Suggest rotation if > 25
```

### Pattern Addition Detection
```yaml
pattern_watch:
  monitor: workspace/memory/core-primitives/patterns/
  on_new_file:
    - Trigger aggregation
    - Update pattern statistics
    - Recalculate relationships
```

## Success Metrics
- Core learnings file always current (< 5 learnings behind)
- Orchestrator loads successfully on every activation
- Pattern recognition improves over time
- Reduced repeat mistakes by 50%+
- Memory never exceeds 25 learnings without rotation

## Error Handling
- **File not found**: Create core-learnings.md with template
- **Pattern conflict**: Show both patterns with context
- **Memory overflow**: Force rotation with preservation
- **Load failure**: Fall back to reading learnings.md directly

## Task Metadata
```yaml
task:
  id: aggregate-core-learnings
  aliases: ['aggregate-learnings', 'consolidate-patterns', 'core-learnings']
  type: memory-consolidation
  priority: high
  auto_trigger: true
  interrupts_workflow: false
  estimated_time: 10s
  output: workspace/memory/core-learnings.md
```

---
**Status**: READY  
**Auto-triggers**: Memory full (20+ learnings) | New pattern added  
**Command**: `*aggregate-learnings` or automatic  
**Output**: Always-loaded core-learnings.md for orchestrator