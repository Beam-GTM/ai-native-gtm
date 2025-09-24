# Pattern: Session Splitting for Complex Tasks

## Pattern Recognition Triggers

### Explicit Multi-Feature Indicators
- "I want to do X **and** Y **and** Z"
- "Let's build A, then enhance B, then create C"
- Multiple unrelated file modifications requested
- Task lists with 10+ major items
- "ULTIMATE", "COMPLETE", "EVERYTHING" in feature names

### Implicit Complexity Indicators
- Estimated time > 2 hours
- Multiple agent switches needed
- Requires 3+ different workflows
- Context approaching 50% capacity
- Dependencies between distinct features

## The Anti-Pattern to Avoid

### "Mega-Feature Syndrome"
```yaml
symptoms:
  - Feature names like "ULTIMATE-CONSOLIDATION"
  - Trying to solve all problems at once
  - Combining unrelated improvements
  - 1000+ line single implementations
  - Context overflow warnings

consequences:
  - Quality degradation
  - Incomplete implementations
  - Lost context between parts
  - Difficult to test/validate
  - Poor handoffs to next session
```

## The Correct Pattern

### Session Pipeline Architecture
```yaml
session_1:
  focus: Single coherent feature
  output: Complete, tested deliverable
  handoff: Clear documentation for next

session_2:
  input: Output from session 1
  focus: Next feature building on first
  output: Enhanced capability

session_3:
  input: Combined outputs
  focus: Integration and optimization
  output: Cohesive system improvement
```

## Suggested User Prompts

### When Complexity Detected
```
🎯 I notice this request involves multiple complex features.

Let me break this down for better execution:

Feature A: [First major component]
  - Estimated effort: [time]
  - Dependencies: [list]
  
Feature B: [Second major component]  
  - Estimated effort: [time]
  - Dependencies: [needs Feature A outputs]

Recommended Approach:
━━━━━━━━━━━━━━━━━━━━━
This Session → Focus on Feature A
Next Session → Build Feature B using A's outputs
━━━━━━━━━━━━━━━━━━━━━

This approach ensures:
✓ Better quality through focus
✓ Proper testing of each component
✓ Clear dependencies and handoffs
✓ Maintainable implementations

Proceed with Feature A only? (Y/n)
```

### When User Insists on Everything
```
⚠️ Session Capacity Warning

Attempting all requested features in one session risks:
- Context overflow (currently at X%)
- Reduced quality due to split focus
- Incomplete implementations
- Lost work if session fails

Strongly Recommended:
1. Let's excel at Feature A now
2. Schedule Feature B for next session
3. Create proper handoff documentation

Would you like to:
1) Focus on Feature A (recommended)
2) Try everything (not recommended)
3) See a detailed session plan

Your choice (1/2/3):
```

### Proactive Planning Offer
```
📋 Multi-Session Plan Available

Your request naturally splits into a 3-session pipeline:

Session 1: Foundation
- [Core feature development]
- Output: [Base implementation]

Session 2: Enhancement  
- [Build on foundation]
- Output: [Enhanced system]

Session 3: Integration
- [Connect components]
- Output: [Complete solution]

Would you like me to:
1) Create detailed session plan
2) Start with Session 1 now
3) Proceed differently

Your choice (1/2/3):
```

## Implementation Locations

### Orchestrator Enhancement
Add to activation sequence:
```yaml
step_x_scope_detection:
  - Analyze user request for complexity
  - Count distinct features requested
  - Estimate total effort required
  - Check context capacity
  - Suggest splitting if needed
```

### Close-Chat Workflow
Add to completion phase:
```yaml
session_continuation_check:
  - Were multiple features attempted?
  - Any incomplete work remaining?
  - Create continuation plan?
  - Document handoff needs
  - Suggest next session focus
```

### Plan-Feature Workflow
Add scope check:
```yaml
feature_scope_validation:
  - Is this truly one feature?
  - Could this be split?
  - Natural boundary points?
  - Session capacity sufficient?
  - Suggest decomposition if needed
```

## Success Metrics

### Good Session Indicators
- Single feature completed with evidence
- All quality gates passed
- Context usage < 70%
- Clear outputs documented
- Ready for next session

### Bad Session Indicators
- Multiple incomplete features
- Context overflow warnings
- Quality gates skipped
- Unclear handoffs
- "Will finish next time" promises

## The Philosophy

**"Sessions are transactions, not marathons"**

Each session should:
- Have clear scope
- Produce complete output
- Enable the next session
- Maintain quality standards
- Respect context limits

The constraint of session boundaries isn't a limitation - it's an architectural advantage that forces better design through modularity.

---

*Pattern documented: 2025-08-29T00:40:00Z*
*Priority: HIGH - Prevents systemic quality issues*