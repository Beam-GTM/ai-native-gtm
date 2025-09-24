# Dynamic Activation Patterns (PRESERVED IN AGENTS)

## Critical Notice
**These activation steps contain complex dynamic execution that CANNOT be centralized without breaking core system functionality.** 

Based on ULTRATHINK analysis, these patterns must remain in individual agent files to preserve:
- Conditional task execution
- Agent-specific decision-making logic  
- System state modification capabilities
- Runtime behavioral pattern establishment

## Dynamic Steps Identified in Orchestrator (Steps 7-19+)

### STEP 7: AUTO-CONSOLIDATION CHECK (CONDITIONAL EXECUTION)
```yaml
pattern: conditional_task_execution
description: "Check embedded TRIGGER comments for consolidation conditions and auto-execute framework/tasks/memory/consolidate-learnings.md if needed"
why_dynamic: "Requires runtime file content analysis and conditional task execution"
preservation_required: "CRITICAL - enables automated system maintenance"
```

### STEP 8: FEATURE INDEX LOADING (CONDITIONAL GENERATION)
```yaml
pattern: conditional_file_generation  
description: "Load all active feature indexes in parallel, generate feature-index.md if missing, cache feature metadata for session"
why_dynamic: "Involves conditional file generation and agent-specific caching logic"
preservation_required: "HIGH - enables dynamic feature management"
```

### STEP 9: FEATURE CONTEXT CHECK
```yaml
pattern: agent_specific_context_loading
description: "Check workspace/features/active/ for existing features"
why_dynamic: "Agent-specific interpretation of feature context"
preservation_required: "MEDIUM - enables feature-aware behavior"
```

### STEP 10-11: INTELLIGENT MENU GENERATION (COMPLEX AI DECISION-MAKING)
```yaml
pattern: complex_ai_decision_making
description: |
  Execute dynamic menu analysis and generation:
  * Analyze memory status: Check core-learnings.md percentage (>120% = urgent, >100% = rotation needed)
  * Check sync status: Last system sync timestamp (>48h = critical, >24h = recommended)  
  * Assess active features: Count, progress, blocked status from features/INDEX.md
  * Evaluate user experience: Project memory entries, completion patterns
  * Apply menu condition logic: Critical conditions override normal menu
  * Generate contextual menu: Highest-priority actions first, adaptive content
why_dynamic: "Multi-condition analysis with complex branching logic and adaptive content generation"
preservation_required: "CRITICAL - core orchestrator intelligence functionality"
agent_specificity: "Orchestrator-specific - other agents have different menu generation logic"
```

### STEP 11.5: MENU CONTEXT INTEGRATION
```yaml
pattern: contextual_integration
description: "Include system status indicators in menu presentation"
why_dynamic: "Context-dependent formatting and presentation logic"
preservation_required: "HIGH - enables user experience optimization"
```

### STEP 12: ADAPTIVE PRESENTATION
```yaml
pattern: adaptive_behavior_establishment
description: "Present menu with appropriate urgency and guidance level"
why_dynamic: "Agent-specific presentation adaptation based on system analysis"
preservation_required: "HIGH - enables personalized user interaction"
```

### STEP 13-16: BEHAVIORAL PATTERN ESTABLISHMENT
```yaml
pattern: runtime_behavior_establishment
description: |
  - STEP 13: Smart routing - proactively analyze ALL user input and suggest best action with confirmation
  - STEP 14: No prefix mode - commands work without * prefix  
  - STEP 15: Proactive intent detection - for EVERY user input, analyze intent and offer appropriate agent/workflow/task
  - STEP 16: Gentle guidance - always ask "Should I launch [agent/workflow]?" before taking action
why_dynamic: "Sets up ongoing runtime AI behaviors and interaction patterns"
preservation_required: "CRITICAL - defines agent personality and interaction model"
agent_specificity: "Each agent has unique behavioral patterns"
```

### STEP 17: PROJECT MEMORY UPDATE (SYSTEM STATE MODIFICATION)
```yaml
pattern: system_state_modification
description: "Execute framework/tasks/memory/update-project-memory.md at key milestones"
why_dynamic: "Conditional execution based on undefined 'key milestones' - context-dependent state modification"
preservation_required: "CRITICAL - enables system memory management"
timing_dependency: "Integration with other system operations"
```

### STEP 18: EFFICIENCY ENFORCEMENT
```yaml
pattern: execution_optimization
description: "EXECUTE STEPS RAPIDLY BUT COMPLETELY - USE PARALLEL TOOL CALLS, MINIMIZE VERBOSITY, MAXIMIZE SPEED"
why_dynamic: "Runtime execution optimization directives"
preservation_required: "HIGH - performance optimization behavior"
```

### STEP 19: SYSTEM SYNC CHECK (TIME-BASED CONDITIONAL LOGIC)
```yaml
pattern: time_based_conditional_system_integration
description: |
  Check workspace/memory/system-sync-state.yaml for last sync timestamp:
  * If >24h ago: Display "💡 System sync recommended (last: {time} ago). Run *sync?"
  * If >48h ago: Display "⚠️ CRITICAL: System sync overdue! Run *sync now?"
  * After feature completion: Prompt "Feature complete! Run *sync to update system?"
why_dynamic: "Complex time-based conditional logic with system integration"
preservation_required: "CRITICAL - enables proactive system maintenance"
system_integration: "Coordinates with other system maintenance operations"
```

## Agent-Specific Dynamic Variations

### Expected Variations Across Agents
Different agents will have variations of these dynamic patterns:

#### Core Agents (orchestrator, architect, explainer)
- **orchestrator**: Full complex menu generation, system coordination
- **architect**: Design-focused menu generation, architecture-specific behaviors
- **explainer**: Learning-focused behaviors, documentation-specific patterns

#### Specialist Agents (developer, product-manager, etc.)
- **developer**: Code-focused behaviors, IDE integration patterns
- **product-manager**: Product-focused menu generation, stakeholder interaction patterns
- **quality-assurance**: Quality-focused behaviors, validation-specific patterns

#### Coordinator Agents (scrum-master, product-owner, analyst)
- **scrum-master**: Team coordination behaviors, agile-specific patterns
- **product-owner**: Backlog-focused behaviors, stakeholder-specific patterns
- **analyst**: Analysis-focused behaviors, research-specific patterns

## Implementation Guidelines for Hybrid Migration

### What to Extract (Static Steps 1-6)
✅ **SAFE TO CENTRALIZE**:
- Timestamp loading
- Critical directives loading
- Project memory loading
- Core learnings loading  
- Memory validation
- Foundation file batch loading

### What to Preserve (Dynamic Steps 7-19+)
❌ **MUST REMAIN IN AGENTS**:
- All conditional execution logic
- Agent-specific decision-making
- System state modification
- Behavioral pattern establishment
- Complex AI decision-making
- Time-based conditional logic
- Menu generation logic

### Migration Process
1. **Replace static steps 1-6** with reference to `static-base-activation.md`
2. **Preserve all dynamic steps 7-19+** in original agent file
3. **Test thoroughly** - behavior should be identical
4. **Document any agent-specific variations** discovered during migration

## Why This Approach Is Necessary

### ULTRATHINK Discovery Summary
The original plan to centralize steps 1-14 would have:
- **Broken conditional execution** in Step 7 (auto-consolidation)
- **Lost complex AI decision-making** in Steps 10-11 (menu generation)
- **Removed system state modification** in Step 17 (memory updates)
- **Eliminated behavioral patterns** in Steps 13-16 (runtime behaviors)
- **Destroyed system integration** in Step 19 (sync coordination)

### Hybrid Approach Benefits
- **Preserves all functionality** - zero risk of breaking complex behaviors
- **Enables partial centralization** - static steps still provide maintenance benefits
- **Documents complex patterns** - creates awareness of dynamic execution complexity
- **Provides safe migration path** - conservative approach with guaranteed success

## Future Enhancement Possibilities

### Phase 2 Possibilities (After Hybrid Success)
Once hybrid approach proves successful, consider:
- **Parameterized dynamic templates** for common conditional patterns
- **Shared behavioral pattern libraries** for similar agent types
- **Standardized interfaces** for system state modification
- **Common frameworks** for complex decision-making logic

**Priority**: Complete hybrid implementation first, then evaluate enhancement opportunities based on actual usage patterns.

---

*This documentation preserves critical system functionality by identifying and protecting complex dynamic activation patterns that cannot be safely centralized.*