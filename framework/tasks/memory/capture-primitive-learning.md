<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.816592Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.266815Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Capture Primitive Learning

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: Never use limit parameter when reading files during this task -->
<!-- This directive OVERRIDES token conservation - read files completely -->
<!-- VIOLATION = Missing critical content in learning analysis -->

**Type**: Learning Capture  
**Category**: Memory & Intelligence  
**Priority**: HIGH  
**Created**: 2025-08-26T12:45:00Z  

## 🔴 PRE-EXECUTION DIRECTIVE CHECK
**MANDATORY**: Before executing this task, verify:
- [ ] All Read tool calls will use complete files (no limit parameter)
- [ ] Any file reads required for context will be comprehensive 
- [ ] Learning analysis requires full file content to be accurate

## Purpose
Quick capture of LLM behavioral patterns, limitations, and learning opportunities as they occur during any session. Documents honest assessments of what LLMs actually can and cannot do.

## Trigger Conditions
- User says: "capture learning", "primitive", "I noticed", "pattern detected"
- LLM recognizes overengineering or unrealistic capability claims
- Quality gate failures or concerns
- Error recovery or fallback activation
- Session closure or context switching
- Anytime a behavioral pattern is observed

## Capture Process

### 1. Quick Capture Format
When triggered, immediately capture to workspace/memory/core-primitives/learnings.md:

```markdown
## Learning #[next_number]: [Pattern Name]
**Date**: YYYY-MM-DD
**Context**: [What feature/task exposed this]
**Pattern**: [What behavior was observed]
**Reality**: [What actually is possible]
**Lesson**: [What to remember for future]
```

### 2. Pattern Categories
Classify the learning into one of these categories:
- **Capability Limitations**: What LLMs actually can't do
- **Overengineering Patterns**: Where complexity exceeded capability
- **Context Management**: Context window and memory limitations
- **Consistency Issues**: Cross-session inconsistencies
- **False Confidence**: Where LLMs claimed abilities they don't have
- **Process Violations**: Not following own workflows/systems
- **Validation Failures**: Marking things complete without testing

### 3. Validation Questions
Before capturing, ask:
- Is this a genuine limitation or just poor implementation?
- Has this pattern been observed before?
- What's the honest assessment of capability?
- How can future sessions avoid this?

## Implementation

### Interactive Capture
```yaml
capture_flow:
  1_trigger: "User invokes capture or pattern detected"
  2_gather: "Collect context about what happened"
  3_classify: "Determine pattern category"
  4_document: "Write to learnings.md with next number"
  5_confirm: "Show captured learning to user"
```

### Automated Capture Points
```yaml
automatic_triggers:
  quality_gates:
    on: [FAIL, CONCERNS]
    action: "Prompt for learning about why it failed"
    
  error_handling:
    on: "Fallback activation"
    action: "Document what caused the error"
    
  workflow_completion:
    on: "Workflow complete"
    action: "Any learnings from this workflow?"
    
  session_closure:
    on: "Chat ending"
    action: "Capture session learnings before close"
```

## File Locations
```
workspace/memory/core-primitives/
├── learnings.md                  # Main learning log (18+ entries)
├── patterns/                     # Identified patterns
│   ├── trust-but-verify.md       # Index drift pattern
│   ├── overengineering.md        # Complexity pattern
│   └── partial-file-reading.md   # Incomplete loading
└── chat-sessions/                # Session-specific learnings
    └── session-YYYY-MM-DD.md    # Individual session insights
```

## Usage Examples

### Example 1: Overengineering Detection
```
User: "This seems too complex"
System: "Capturing learning about overengineering..."
*Writes Learning #019 about unnecessary complexity*
```

### Example 2: Validation Failure
```
System: "Quality gate FAILED"
System: "What learning should we capture about this failure?"
*Documents why the validation failed*
```

### Example 3: Session Closure
```
User: "bye"
System: "Before closing, any learnings to capture from this session?"
System: "Consider: What couldn't be done? What was overengineered?"
```

## Integration Points

### With Orchestrator
- Available via: `*capture-learning` or `*primitive`
- Natural language triggers in routing_patterns
- Integrated in help menu as learning command

### With Workflows
- Add to workflow completion steps
- Trigger on quality gate issues
- Include in error handling paths

### With Quality Gates
- Automatic prompt on FAIL or CONCERNS
- Document why gates didn't pass
- Learn from validation failures

## Success Metrics
- Capture rate: 1+ learning per session
- Pattern identification: 3+ similar learnings = pattern
- Honesty level: No sugar-coating limitations
- Usage frequency: Used when patterns observed

## Important Notes
1. **Be Honest**: Document real limitations, not aspirational capabilities
2. **Be Specific**: Include concrete examples and context
3. **Be Constructive**: Focus on what TO do, not just what failed
4. **Be Consistent**: Use the standard format for all captures
5. **Be Proactive**: Capture as soon as pattern observed, don't wait

## POST-EXECUTION COMPLIANCE VALIDATION 🔍

### MEMORY TASK COMPLIANCE
- [ ] **Learning Capture**: Actual learning pattern extracted and documented
- [ ] **File Operations**: Learning appended to correct file with evidence
- [ ] **Pattern Classification**: Learning properly categorized with reasoning
- [ ] **Format Compliance**: Standard learning format followed exactly
- [ ] **Content Validation**: Learning includes concrete examples and context

### Evidence Collection for Memory Operations
```bash
# Load validation framework for memory operations
source "workspace/features/active/post-execution-compliance-validation/validation-framework.md"
source "workspace/features/active/post-execution-compliance-validation/evidence-collection-patterns.md"

# Set up evidence collection for learning capture
TASK_NAME="capture-primitive-learning"
EVIDENCE_DIR="/tmp/memory_evidence_${TASK_NAME}_$(date +%s)"
mkdir -p "$EVIDENCE_DIR"/{baseline,capture,validation}

echo "=== MEMORY TASK VALIDATION ===" > "$EVIDENCE_DIR/memory_validation.log"
echo "Task: Capture Primitive Learning" >> "$EVIDENCE_DIR/memory_validation.log"
echo "Started: $(date -Iseconds)" >> "$EVIDENCE_DIR/memory_validation.log"

# Baseline: Count existing learnings before capture
if [ -f "workspace/memory/core-primitives/learnings.md" ]; then
    BASELINE_COUNT=$(grep -c "^## Learning #" "workspace/memory/core-primitives/learnings.md" 2>/dev/null || echo "0")
    echo "Baseline learning count: $BASELINE_COUNT" >> "$EVIDENCE_DIR/memory_validation.log"
    
    collect_file_existence_evidence "workspace/memory/core-primitives/learnings.md" "$EVIDENCE_DIR/baseline/learnings_exists.log"
    collect_file_completeness_evidence "workspace/memory/core-primitives/learnings.md" "$(wc -l < workspace/memory/core-primitives/learnings.md)" "$EVIDENCE_DIR/baseline/learnings_baseline.log"
else
    BASELINE_COUNT=0
    echo "No existing learnings file - will be created" >> "$EVIDENCE_DIR/memory_validation.log"
fi

# Execute learning capture process here...
# [Learning capture implementation would go here]

# Post-capture validation
if [ -f "workspace/memory/core-primitives/learnings.md" ]; then
    POST_COUNT=$(grep -c "^## Learning #" "workspace/memory/core-primitives/learnings.md" 2>/dev/null || echo "0")
    echo "Post-capture learning count: $POST_COUNT" >> "$EVIDENCE_DIR/memory_validation.log"
    
    # Validate learning was actually added
    if [ "$POST_COUNT" -gt "$BASELINE_COUNT" ]; then
        echo "✅ Learning capture verified: +$((POST_COUNT - BASELINE_COUNT)) new learnings" >> "$EVIDENCE_DIR/memory_validation.log"
        
        # Validate learning format compliance
        LATEST_LEARNING=$(grep "^## Learning #" "workspace/memory/core-primitives/learnings.md" | tail -1)
        echo "Latest learning: $LATEST_LEARNING" >> "$EVIDENCE_DIR/capture/latest_learning.log"
        
        # Check for required format components
        collect_content_pattern_evidence "workspace/memory/core-primitives/learnings.md" "## Learning #[0-9]*:|\\*\\*Date\\*\\*:|\\*\\*Context\\*\\*:|\\*\\*Pattern\\*\\*:|\\*\\*Reality\\*\\*:|\\*\\*Lesson\\*\\*:" "$EVIDENCE_DIR/capture/format_validation.log"
        
    else
        echo "❌ VIOLATION: Learning count unchanged - no learning was captured" >> "$EVIDENCE_DIR/memory_validation.log"
        echo "Expected: $((BASELINE_COUNT + 1)), Actual: $POST_COUNT" >> "$EVIDENCE_DIR/memory_validation.log"
    fi
else
    echo "❌ CRITICAL VIOLATION: Learning file not created" >> "$EVIDENCE_DIR/memory_validation.log"
fi

# Performance validation - memory operations should be fast
TASK_END_TIME=$(date +%s%N)
TASK_DURATION=$(((TASK_END_TIME - TASK_START_TIME) / 1000000)) # Convert to ms
echo "Task duration: ${TASK_DURATION}ms" >> "$EVIDENCE_DIR/memory_validation.log"

if [ "$TASK_DURATION" -le 5000 ]; then
    echo "✅ Performance target met: ${TASK_DURATION}ms ≤ 5000ms" >> "$EVIDENCE_DIR/memory_validation.log"
else
    echo "❌ PERFORMANCE VIOLATION: ${TASK_DURATION}ms > 5000ms target" >> "$EVIDENCE_DIR/memory_validation.log"
fi

# Final validation
MEMORY_VIOLATIONS=0

# Check for format violations
if grep -q "MISSING REQUIRED PATTERNS" "$EVIDENCE_DIR/capture/format_validation.log" 2>/dev/null; then
    ((MEMORY_VIOLATIONS++))
    echo "❌ Format violations detected" >> "$EVIDENCE_DIR/memory_validation.log"
fi

# Check for capture violations
if grep -q "VIOLATION" "$EVIDENCE_DIR/memory_validation.log"; then
    ((MEMORY_VIOLATIONS++))
fi

if [ $MEMORY_VIOLATIONS -eq 0 ]; then
    echo "✅ MEMORY TASK CERTIFICATION: FULLY COMPLIANT" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Task: Capture Primitive Learning" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Learning captured with evidence" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Format compliance verified" >> "$EVIDENCE_DIR/validation/final_result.log"
    
    echo "🏆 LEARNING CAPTURE CERTIFIED COMPLIANT"
    echo "Evidence: $EVIDENCE_DIR"
else
    echo "❌ MEMORY TASK CERTIFICATION: NON-COMPLIANT" >> "$EVIDENCE_DIR/validation/final_result.log"
    echo "Violations: $MEMORY_VIOLATIONS found" >> "$EVIDENCE_DIR/validation/final_result.log"
    
    echo "🚨 LEARNING CAPTURE COMPLIANCE FAILURE"
    echo "Evidence: $EVIDENCE_DIR"
    exit 1
fi
```

### Memory Operations Evidence Requirements
- **Learning Extraction**: Concrete proof that learning pattern was identified and extracted
- **File Modification**: Evidence showing learning was appended to learnings.md
- **Format Compliance**: Validation that standard learning format was followed
- **Content Quality**: Verification that learning includes context, pattern, reality, and lesson
- **Performance**: Memory operations completed within 5-second target

### Corrective Actions
**If violations detected:**
1. **Missing Learning**: Re-execute pattern extraction with concrete examples
2. **Format Violations**: Apply standard learning format template
3. **File Operations**: Ensure proper file creation/modification with evidence
4. **Content Issues**: Add missing context, pattern details, or lessons learned

### Integration Notes
This validation ensures memory capture tasks actually extract and document learning patterns rather than just claiming completion. Critical for preventing Learning #8/#9 substitution patterns.

---
**Status**: READY **WITH VALIDATION**  
**Command**: `*capture-learning` or `*primitive`  
**Auto-triggers**: Quality gates, errors, workflow completion, session closure  
**Validation**: Memory operations compliance with evidence collection