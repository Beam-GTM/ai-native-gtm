# Conditional Framework Guidelines

## Purpose
Guidelines for maintaining consistency in agent-specific dynamic activation behaviors while preserving the conditional execution and decision-making patterns that make each agent unique.

## Core Principle: Preserve, Don't Centralize

### What This Framework Does
- **Documents best practices** for dynamic activation patterns
- **Provides consistency guidelines** for similar behaviors across agents
- **Maintains agent autonomy** for unique conditional logic
- **Prevents fragmentation** of dynamic behavior patterns

### What This Framework Does NOT Do
- **Centralize conditional logic** (this would break functionality)
- **Standardize unique behaviors** (this would eliminate agent personalities)
- **Replace agent-specific patterns** (this would cause system regression)

## Dynamic Pattern Categories

### 1. Conditional Task Execution Patterns

#### Pattern: Auto-Task Triggers
```yaml
description: "Execute tasks automatically based on file content or system state analysis"
example: "Step 3.7: Auto-consolidation check with conditional task execution"
implementation_guideline: |
  - Analyze trigger conditions specific to agent's domain
  - Execute relevant tasks when conditions are met  
  - Preserve agent-specific trigger logic and thresholds
  - Document trigger conditions for maintainability
consistency_approach: "Similar structure, different conditions per agent"
```

#### Pattern: Conditional File Generation  
```yaml
description: "Generate files conditionally based on system state"
example: "Generate feature-index.md if missing during activation"
implementation_guideline: |
  - Check for required files specific to agent's needs
  - Generate missing files using agent-appropriate templates
  - Cache generated content for session efficiency
  - Handle generation failures gracefully
consistency_approach: "Common generation pattern, agent-specific file types"
```

### 2. Complex Decision-Making Patterns

#### Pattern: Multi-Condition Analysis
```yaml
description: "Analyze multiple system conditions to make activation decisions"
example: "Orchestrator menu generation with memory/sync/feature analysis"  
implementation_guideline: |
  - Define condition hierarchies relevant to agent domain
  - Implement systematic condition checking
  - Apply agent-specific decision trees
  - Generate appropriate responses based on analysis
consistency_approach: "Similar analysis framework, different conditions and responses per agent"
```

#### Pattern: Adaptive Content Generation
```yaml
description: "Generate content based on current system state and user context"
example: "Dynamic menu generation with urgency levels and contextual options"
implementation_guideline: |
  - Assess current system state from agent perspective
  - Generate content appropriate to agent's capabilities
  - Adapt presentation based on urgency and context
  - Provide clear user guidance and options
consistency_approach: "Common adaptation principles, unique content per agent"
```

### 3. Behavioral Pattern Establishment

#### Pattern: Runtime Behavior Setup
```yaml
description: "Establish ongoing AI behaviors and interaction patterns during activation"
example: "Smart routing, intent detection, proactive guidance patterns"
implementation_guideline: |
  - Define agent-specific interaction patterns
  - Set up runtime behavioral triggers
  - Establish user communication style
  - Configure agent personality expression
consistency_approach: "Similar behavior establishment process, unique personalities"
```

#### Pattern: System Integration Behaviors
```yaml
description: "Set up coordination with other system components"
example: "Agent coordination, workflow handoffs, system monitoring"
implementation_guideline: |
  - Define agent's role in system ecosystem
  - Establish communication patterns with other agents
  - Set up monitoring for relevant system changes
  - Configure coordination protocols
consistency_approach: "Common integration framework, specialized roles"
```

### 4. System State Modification Patterns

#### Pattern: Context-Dependent State Changes
```yaml
description: "Modify system state based on agent-specific conditions"
example: "Project memory updates at agent-defined 'key milestones'"
implementation_guideline: |
  - Define what constitutes agent-specific milestones
  - Implement state modification procedures
  - Ensure state changes don't conflict with other agents
  - Document state modification triggers and effects
consistency_approach: "Common state management interfaces, agent-specific triggers"
```

## Implementation Best Practices

### Maintaining Consistency Without Centralization

#### 1. Common Structure, Unique Content
```yaml
pattern_approach: |
  Use similar code structure for related functionality:
  
  # GOOD: Similar structure, different content
  agent_a_menu: "Generate menu based on architecture patterns"  
  agent_b_menu: "Generate menu based on development context"
  
  # AVOID: Identical logic (should be centralized)  
  agent_a_loading: "Load project-brief.md"
  agent_b_loading: "Load project-brief.md"  # This should be centralized
```

#### 2. Documented Variation Points
```yaml
documentation_approach: |
  For each dynamic pattern, document:
  - Common framework elements
  - Agent-specific variation points  
  - Reasons for variation
  - Integration considerations
  
  Example:
  menu_generation:
    common_framework: "Analyze system state → Generate options → Present to user"
    orchestrator_variation: "Complex multi-condition analysis with urgency levels"
    architect_variation: "Architecture-focused options with design context"
    developer_variation: "Code-focused options with development context"
```

#### 3. Interface Standardization
```yaml
interface_approach: |
  Standardize interfaces between agents while preserving internal logic:
  
  # GOOD: Standard interface, unique implementation
  all_agents_support: "respond_to_user_intent(intent, context)"
  orchestrator_impl: "Routes to appropriate agent with confirmation"
  developer_impl: "Provides code assistance based on intent"
  
  # PRESERVE: Agent-specific internal decision-making
  orchestrator_internal: "Complex routing analysis with agent coordination"  
  developer_internal: "Code analysis and IDE integration patterns"
```

## Migration Guidelines for Dynamic Patterns

### Before Migrating an Agent

#### 1. Analyze Dynamic Complexity
- [ ] **Identify conditional execution** - any "if/when" logic in activation
- [ ] **Map decision-making processes** - complex analysis or branching
- [ ] **Document state modifications** - any system changes during activation
- [ ] **Note behavioral establishment** - runtime pattern setup

#### 2. Categorize Activation Steps
- [ ] **Static (1-6)**: Simple file loading → Safe to reference centralized file
- [ ] **Dynamic (7-19+)**: Complex logic → Must preserve in agent
- [ ] **Hybrid**: Simple agent-specific loading → Consider case-by-case

#### 3. Plan Preservation Strategy
- [ ] **Document unique behaviors** specific to this agent
- [ ] **Identify integration points** with other system components
- [ ] **Plan testing approach** to validate identical functionality
- [ ] **Design rollback procedure** in case of issues

### During Migration

#### 1. Conservative Replacement
```yaml
# BEFORE
activation-instructions:
  - STEP 1: Timestamp loading                    # → Replace with static reference
  - STEP 2: Critical directives loading          # → Replace with static reference  
  - STEP 3: Project memory loading               # → Replace with static reference
  - STEP 4: Memory validation                    # → Replace with static reference
  - STEP 5: Foundation loading                   # → Replace with static reference
  - STEP 6: Validation checkpoint                # → Replace with static reference
  - STEP 7: Agent-specific conditional logic     # → PRESERVE EXACTLY
  - STEP 8+: Dynamic behaviors                   # → PRESERVE EXACTLY

# AFTER  
activation-instructions:
  - EXECUTE: framework/activation/static-base-activation.md  # Steps 1-6
  - STEP 7: Agent-specific conditional logic     # → PRESERVED UNCHANGED
  - STEP 8+: Dynamic behaviors                   # → PRESERVED UNCHANGED
```

#### 2. Validation Testing
- [ ] **Functionality Test**: Agent behaves identically after migration
- [ ] **Integration Test**: Agent coordinates correctly with system
- [ ] **Performance Test**: Activation speed maintained or improved
- [ ] **Edge Case Test**: Conditional logic works in all scenarios

### After Migration

#### 1. Documentation Updates
- [ ] **Update agent documentation** with hybrid activation pattern
- [ ] **Document any discovered variations** from expected patterns
- [ ] **Update integration documentation** if coordination changes
- [ ] **Record lessons learned** for future migrations

#### 2. Pattern Analysis
- [ ] **Identify reusable patterns** discovered during migration
- [ ] **Document agent-specific uniqueness** for future reference
- [ ] **Update conditional framework** with new pattern insights
- [ ] **Share learnings** with other migration efforts

## Common Pitfalls and Prevention

### Pitfall 1: Over-Centralization
**Problem**: Attempting to centralize conditional logic  
**Prevention**: Always preserve dynamic behaviors in agents  
**Detection**: If migration breaks functionality, likely over-centralized  

### Pitfall 2: Under-Documentation
**Problem**: Not documenting preserved dynamic patterns  
**Prevention**: Document all dynamic behaviors and their purposes  
**Detection**: Future maintainers confused about agent-specific logic  

### Pitfall 3: Inconsistent Interfaces  
**Problem**: Agent interactions break after migration  
**Prevention**: Test all agent coordination after migration  
**Detection**: Workflow or task execution issues between agents  

### Pitfall 4: Performance Regression
**Problem**: Migration accidentally slows down activation  
**Prevention**: Measure performance before and after migration  
**Detection**: Noticeable activation slowdown or user complaints  

## Future Evolution

### Pattern Libraries (Phase 2+)
Once hybrid migration is complete and successful:
- **Common pattern templates** for similar conditional logic
- **Shared utility functions** for common system interactions  
- **Standardized interfaces** for agent coordination
- **Reusable behavioral components** for similar agent types

### Dynamic Framework Enhancement
- **Parameterized conditional templates** for common patterns
- **Shared decision-making utilities** with agent-specific configuration
- **Common system integration patterns** with role-specific implementation
- **Behavioral pattern inheritance** for agent families

---

*These guidelines enable consistent implementation of dynamic activation patterns while preserving the unique behaviors that make each agent effective in their specialized domain.*