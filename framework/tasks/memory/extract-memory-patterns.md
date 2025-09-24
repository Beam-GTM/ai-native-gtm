<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.843831Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.268991Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Extract Memory Patterns
**Type**: Pattern Recognition  
**Category**: Intelligence Layer  
**Priority**: MEDIUM  
**Created**: 2025-08-26T01:10:00Z  

## Purpose
Analyze project-memory.md entries to extract recurring patterns, behaviors, and learnings for system intelligence improvement.

## Trigger Conditions
- Every 5 entries (20, 25, 30, etc.)
- Manual pattern extraction request
- Before rotation (to preserve patterns)

## Pattern Extraction Process

### 1. Pattern Categories to Detect
```yaml
pattern_types:
  action_patterns:
    - Repeated workflows or tasks
    - Common problem-solving approaches
    - Frequent command sequences
    
  learning_patterns:
    - Recurring mistakes
    - Consistent improvements
    - Knowledge gaps
    
  project_patterns:
    - Feature development cycles
    - Common milestones
    - Typical completion times
    
  behavior_patterns:
    - User preferences
    - Decision-making tendencies
    - Communication styles
```

### 2. Analysis Process
```yaml
analysis_steps:
  1_collect:
    - Read last 5 entries (or all since last extraction)
    - Group by PROJECT, TASK, WORKFLOW fields
    - Identify commonalities
    
  2_analyze:
    - Count frequency of actions
    - Identify sequences (A→B→C patterns)
    - Find correlation between project types and outcomes
    
  3_extract:
    - Patterns appearing 3+ times
    - Learnings mentioned 2+ times  
    - Consistent project approaches
```

### 3. Pattern Output Format
```yaml
# patterns/extracted/pattern-YYYY-MM-DD.yaml
pattern_id: "pat-001"
name: "Feature Development Workflow"
confidence: "high"  # Based on frequency
occurrences: 5
entries: [15, 17, 19, 20, 22]

description: |
  User consistently follows plan-feature → implement-feature workflow
  for all feature creation, with quality gates

components:
  - Create PRD
  - Set up workspace
  - Implement progressively
  - Run quality gates
  
recommendations:
  - Pre-load workflow for feature tasks
  - Suggest quality checks proactively
  
extracted_from:
  start_entry: 15
  end_entry: 22
  extraction_date: "2025-08-26T01:10:00Z"
```

### 4. Suggestion Generation
```yaml
suggestion_criteria:
  confidence_threshold: 70%  # Minimum confidence
  occurrence_minimum: 3      # Times pattern seen
  
suggestion_format:
  - pattern_detected: What was observed
  - suggestion: What to do about it
  - confidence: How sure we are
  - benefit: Why this helps
```

### 5. Integration with Project Memory
```yaml
feedback_loop:
  - Add PATTERN field to new entries
  - Reference extracted patterns in decisions
  - Track if suggestions were followed
  - Measure suggestion success rate
```

## Real Examples from Current Memory

### Example Pattern 1: Overengineering Recognition
```yaml
pattern: "Overengineering Recognition"
seen_in: [Entry 17, 19, 20]
behavior: "User questions complexity → LLM recognizes overengineering → Simplification"
suggestion: "When proposing complex solutions, pause and ask 'Is this overengineering?'"
```

### Example Pattern 2: Trust But Verify
```yaml
pattern: "Trust But Verify"
seen_in: [Entry 18, Learning #12]
behavior: "Claims made without verification → User prompts check → Discrepancy found"
suggestion: "Always verify filesystem/reality before documenting counts or status"
```

## Pattern Storage
```
workspace/memory/patterns/
├── extracted/
│   ├── pattern-2025-08-26.yaml
│   ├── overengineering-pattern.yaml
│   └── trust-verify-pattern.yaml
└── active-patterns.md  # Currently applicable patterns
```

## Success Metrics
- Extract 1+ pattern per 5 entries
- 70%+ suggestion acceptance rate
- Patterns lead to measurable improvements
- Reduced repeat mistakes

## Error Handling
- **No patterns found**: Normal for diverse work, continue monitoring
- **Low confidence**: Don't generate suggestions below 70%
- **Conflicting patterns**: Present both, let user decide

---
**Status**: READY  
**Auto-trigger**: EVERY 5 ENTRIES