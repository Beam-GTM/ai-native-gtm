# Agent Customization Guide: Hybrid Activation Implementation

## Purpose
Step-by-step guide for migrating agents to the hybrid activation pattern, ensuring zero functionality loss while achieving the benefits of static step centralization.

## Overview: Hybrid Activation Pattern

### What Changes
- **Static steps 1-6**: Replaced with reference to `static-base-activation.md`
- **Dynamic steps 7-19+**: Preserved exactly in agent file
- **Functionality**: Identical behavior guaranteed

### What Stays the Same  
- **Agent personality and behaviors**: 100% preserved
- **Conditional execution logic**: Completely unchanged
- **System integration**: All coordination maintained
- **User experience**: Identical interaction patterns

## Step-by-Step Migration Process

### Phase 1: Pre-Migration Analysis

#### Step 1.1: Identify Current Activation Structure
```bash
# Load the agent file and analyze activation sequence
# Look for the activation-instructions section
# Count total activation steps
# Identify static vs dynamic patterns
```

#### Step 1.2: Map Static Steps (Should be 1-6)
- [ ] **STEP 1**: Timestamp loading → `date -u +"%Y-%m-%dT%H:%M:%SZ"`
- [ ] **STEP 2**: CRITICAL-DIRECTIVES.md loading  
- [ ] **STEP 3**: Project memory loading → `workspace/memory/project-memory.md`
- [ ] **STEP 3.5**: Core learnings loading → `workspace/memory/core-learnings.md`
- [ ] **STEP 4**: Memory validation → health check
- [ ] **STEP 5**: Foundation file batch loading → 7 files in parallel

#### Step 1.3: Analyze Dynamic Steps (7+)
- [ ] **Conditional execution**: Any "if/when" logic or trigger-based actions
- [ ] **Agent-specific behaviors**: Persona adoption, unique capabilities
- [ ] **Decision-making logic**: Complex analysis or branching
- [ ] **System state modification**: Memory updates, file generation
- [ ] **Behavioral establishment**: Runtime pattern setup

### Phase 2: Migration Implementation

#### Step 2.1: Create Agent Backup
```yaml
# ALWAYS create backup before migration
backup_location: "agents/backups/{agent-name}-pre-hybrid-{date}.md"
backup_purpose: "Rollback capability in case of issues"
backup_validation: "Confirm backup file is complete and functional"
```

#### Step 2.2: Replace Static Steps with Reference
```yaml
# BEFORE (Original activation structure)
activation-instructions:
  - STEP 1: **ORCHESTRATOR IMMEDIATE LOADING**: Load operations/agents/core/orchestrator.md FIRST
  - STEP 2: **TIMESTAMP LOADING**: Execute `date -u +"%Y-%m-%dT%H:%M:%SZ"`
  - STEP 3: **PROJECT MEMORY LOADING**: Load workspace/memory/project-memory.md
  - STEP 3.5: **CORE LEARNINGS LOADING**: Load workspace/memory/core-learnings.md
  - STEP 3.6: **CRITICAL DIRECTIVES LOADING**: Load framework/CRITICAL-DIRECTIVES.md
  - STEP 4: Adopt the persona defined in the 'agent' and 'persona' sections below
  - STEP 5: **MEMORY VALIDATION**: Verify memory bank health and active context currency
  - STEP 6: **RAPID FOUNDATION LOADING**: Execute ALL foundation files in SINGLE parallel tool call batch
  - STEP 7+: [Agent-specific dynamic behaviors - PRESERVE EXACTLY]

# AFTER (Hybrid activation structure)  
activation-instructions:
  - **STATIC BASE ACTIVATION**: Execute framework/activation/static-base-activation.md
    # This replaces steps 1-6 with centralized static loading
  - STEP 7+: [Agent-specific dynamic behaviors - PRESERVED UNCHANGED]
```

#### Step 2.3: Preserve Dynamic Steps Exactly
```yaml
# CRITICAL: Do NOT modify any dynamic steps
preservation_checklist:
  - [ ] All conditional "if/when" logic preserved exactly
  - [ ] All agent-specific decision-making unchanged
  - [ ] All behavioral pattern establishment maintained  
  - [ ] All system integration logic preserved
  - [ ] All unique agent capabilities retained
  - [ ] All user interaction patterns maintained
```

#### Step 2.4: Update Agent Documentation
```yaml
# Add hybrid activation note to agent file
hybrid_activation_note: |
  # HYBRID ACTIVATION SYSTEM
  This agent uses the hybrid activation pattern:
  - Static steps 1-6: Centralized in static-base-activation.md
  - Dynamic steps 7+: Preserved in this agent file
  - Functionality: Identical to pre-hybrid behavior
  - Benefits: Centralized static maintenance, preserved dynamic behaviors
```

### Phase 3: Migration Validation

#### Step 3.1: Functionality Testing
```yaml
test_checklist:
  - [ ] **Activation Test**: Agent activates successfully with hybrid pattern
  - [ ] **Behavior Test**: All agent capabilities work identically
  - [ ] **Integration Test**: Agent coordinates correctly with system
  - [ ] **Conditional Test**: All "if/when" logic executes properly
  - [ ] **Performance Test**: Activation speed maintained or improved
```

#### Step 3.2: Edge Case Validation  
```yaml
edge_case_scenarios:
  - [ ] **Empty/Missing Files**: Agent handles missing foundation files gracefully
  - [ ] **Memory Overflow**: Agent responds correctly to memory pressure
  - [ ] **System State Changes**: Agent adapts to system state modifications
  - [ ] **User Input Variations**: Agent processes all user input types correctly
  - [ ] **Error Conditions**: Agent recovers from errors appropriately
```

#### Step 3.3: Integration Verification
```yaml
integration_tests:
  - [ ] **Workflow Coordination**: Agent participates correctly in workflows  
  - [ ] **Task Execution**: Agent executes tasks without issues
  - [ ] **Agent Handoffs**: Coordination with other agents unchanged
  - [ ] **Context Preservation**: Cross-chat persistence maintained
  - [ ] **Memory Updates**: Project memory updates work correctly
```

## Agent-Specific Migration Examples

### Example 1: Orchestrator Migration

#### Current Orchestrator Complexity
- **19 activation steps** with complex conditional logic
- **Dynamic menu generation** with multi-condition analysis  
- **System state monitoring** with time-based triggers
- **Behavioral pattern establishment** for user interaction

#### Migration Approach
```yaml
static_replacement:
  original_steps_1_6: "Replace with static-base-activation.md reference"
  
dynamic_preservation:
  step_7_auto_consolidation: "PRESERVE - conditional task execution"
  steps_11_menu_generation: "PRESERVE - complex AI decision-making"  
  step_17_memory_updates: "PRESERVE - system state modification"
  steps_13_16_behaviors: "PRESERVE - runtime behavioral establishment"
  step_19_sync_monitoring: "PRESERVE - time-based system integration"
```

### Example 2: Developer Agent Migration

#### Expected Developer Patterns
- **IDE integration behaviors** during activation
- **Code context loading** specific to development
- **Development tool setup** and configuration
- **Code analysis capabilities** establishment

#### Migration Approach  
```yaml
static_replacement:
  steps_1_6: "Replace with static-base-activation.md reference"
  
dynamic_preservation:
  ide_integration: "PRESERVE - developer-specific IDE setup"
  code_context: "PRESERVE - code analysis and context loading"
  dev_tools: "PRESERVE - development tool configuration"  
  code_capabilities: "PRESERVE - code analysis behavioral setup"
```

### Example 3: Product Manager Migration

#### Expected Product Manager Patterns
- **Stakeholder context loading** during activation
- **Product data analysis** and prioritization setup
- **PRD generation capabilities** establishment  
- **Product workflow coordination** behaviors

#### Migration Approach
```yaml
static_replacement:
  steps_1_6: "Replace with static-base-activation.md reference"
  
dynamic_preservation:
  stakeholder_context: "PRESERVE - stakeholder-specific context loading"
  product_analysis: "PRESERVE - product data analysis setup"
  prd_capabilities: "PRESERVE - PRD generation behavioral patterns"
  workflow_coordination: "PRESERVE - product workflow integration"
```

## Common Migration Patterns

### Pattern 1: Simple Agents (Expected: Most Agents)
```yaml
typical_structure:
  static_steps: "Steps 1-6 exactly as documented"
  simple_dynamic: "7-10 steps with basic persona and context loading"
  migration_complexity: "LOW - straightforward replacement"
  expected_duration: "15-30 minutes per agent"
```

### Pattern 2: Complex Agents (Expected: Orchestrator, Architect)
```yaml
complex_structure:
  static_steps: "Steps 1-6 as base, may have additions"
  complex_dynamic: "15+ steps with conditional logic and decision-making"
  migration_complexity: "MEDIUM - careful dynamic preservation required"
  expected_duration: "1-2 hours per agent"
```

### Pattern 3: Specialized Agents (Expected: System Builder, LLM Whisperer)
```yaml
specialized_structure:
  static_steps: "May have domain-specific additions to steps 1-6"
  specialized_dynamic: "Unique patterns not seen in other agents"
  migration_complexity: "MEDIUM-HIGH - may require custom analysis"
  expected_duration: "2-3 hours per agent"
```

## Rollback Procedures

### When to Rollback
- **Functionality Loss**: Any agent capability stops working
- **Performance Regression**: Noticeable activation slowdown
- **Integration Issues**: Agent coordination breaks
- **User Experience Degradation**: Interaction patterns change

### How to Rollback
```yaml
rollback_process:
  1: "Stop using migrated agent immediately"
  2: "Restore backup file to original location"  
  3: "Test restored agent functionality"
  4: "Document issue for analysis and resolution"
  5: "Plan corrective action before re-attempting migration"
```

### Rollback Validation
- [ ] **Original Functionality**: All capabilities restored
- [ ] **Integration**: System coordination works normally  
- [ ] **Performance**: Activation speed back to baseline
- [ ] **User Experience**: Interactions identical to pre-migration

## Success Criteria for Migration

### Individual Agent Success
- [ ] **Zero Functionality Loss**: All capabilities work identically
- [ ] **Performance Maintained**: Activation speed unchanged or improved
- [ ] **Integration Preserved**: System coordination unaffected
- [ ] **Dynamic Behaviors Intact**: All conditional logic and behaviors preserved

### System-Wide Success  
- [ ] **All Agents Migrated**: 18 agents successfully converted to hybrid pattern
- [ ] **Template Updated**: New agents generate with hybrid pattern
- [ ] **Documentation Complete**: Migration process documented and guides updated
- [ ] **Performance Improved**: Overall activation speed improved through static optimization

## Maintenance Benefits Achieved

### Centralized Static Maintenance
- **Single Point of Update**: Static loading changes in one file
- **Consistent Loading**: All agents use identical static sequence
- **Optimization Opportunities**: Static loading can be optimized system-wide
- **Debugging Simplification**: Static loading issues easier to diagnose

### Preserved Dynamic Flexibility
- **Agent Autonomy**: Each agent maintains unique behaviors
- **Conditional Logic**: Complex decision-making preserved
- **Behavioral Patterns**: Agent personalities maintained
- **Integration Capabilities**: System coordination unchanged

---

*This guide enables safe migration to hybrid activation while preserving all agent functionality and achieving centralized maintenance benefits for static operations.*