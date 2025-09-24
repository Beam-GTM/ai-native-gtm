# STATIC FOUNDATION LOADER
**Version**: 1.0.0  
**Purpose**: Universal foundation loading for ALL agents (orchestrator, developer, architect, future agents)  
**Execution**: Mandatory first step in every agent activation  
**Status**: CENTRALIZED LOADING SYSTEM

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: Never use limit parameter when reading files -->
<!-- This directive OVERRIDES token conservation - read files completely -->
<!-- VIOLATION = Missing critical system foundations -->

## 🚀 UNIVERSAL FOUNDATION LOADING PROTOCOL

**EXECUTION PATTERN**: This file is executed by ALL agents as their first step
- Called by: Every agent template via static_activation.execution
- Timing: BEFORE any agent-specific behavior
- Validation: Must complete successfully before dynamic activation

## STEP 1: 🔴 CRITICAL SYSTEM FOUNDATIONS + CORE WORKFLOWS (MAXIMUM PRIORITY)

Load these files in PARALLEL - **CORE WORKFLOWS ARE SYSTEM-CRITICAL**:

```yaml
critical_system_foundations:
  - framework/CRITICAL-DIRECTIVES.md  # Mandatory enforcement directives
  - SYSTEM-STRUCTURE.md              # System navigation map
  - workspace/memory/project-memory.md # Current system state
  - workspace/memory/core-learnings.md # LLM behavioral patterns
  - framework/workflows/INDEX.md     # 🔴 CORE WORKFLOWS: plan-feature, implement-feature + close-chat
```

**🚨 CORE WORKFLOW PRIORITY**: The 3 core workflows are AS IMPORTANT as CRITICAL-DIRECTIVES
**LOADING INSTRUCTION**: Execute parallel Read operations - CORE WORKFLOWS ARE NON-NEGOTIABLE

## STEP 2: BEHAVIORAL CORRECTION MODELS

Load behavioral pattern correction models in PARALLEL:

```yaml
behavioral_models:
  - framework/tasks/behavioral-correction/execution-documentation-paradox-model.md
  - framework/tasks/behavioral-correction/false-completion-syndrome-model.md  
  - framework/tasks/behavioral-correction/basic-operations-failure-model.md
```

**PURPOSE**: Prevent 75% of documented AI failure patterns through active correction

## STEP 3: SYSTEM REGISTRIES (Core workflows already loaded in Step 1)

Load discovery registries for additional system awareness:

```yaml
system_registries:
  - operations/INDEX.md           # Resource discovery registry
  - workspace/features/INDEX.md   # Current work context
```

**PURPOSE**: Enable dynamic discovery of agents, features, and additional resources
**NOTE**: Core workflows already loaded as CRITICAL SYSTEM FOUNDATIONS in Step 1

## VALIDATION GATE ✅

**COMPLETION CHECKPOINT**: Before proceeding to dynamic activation, verify:
- [ ] All 10 foundation files loaded successfully (including CORE WORKFLOWS)
- [ ] 🔴 CORE WORKFLOWS KNOWLEDGE CONFIRMED: plan-feature, implement-feature, close-chat
- [ ] CRITICAL-DIRECTIVES.md enforcement active
- [ ] Behavioral correction models operational  
- [ ] System registries accessible
- [ ] No loading errors or partial reads

**🚨 CRITICAL**: If core workflows INDEX failed to load, ABORT activation and report error

**RETURN STATUS**: 
- ✅ "FOUNDATION_READY" - All files loaded, proceed to dynamic activation
- ⚠️ "FOUNDATION_INCOMPLETE: [missing_files]" - Show missing files, continue with available context

## SUCCESS METRICS

**Performance Target**: <3 seconds total loading time  
**Reliability Target**: >95% success rate  
**Token Efficiency**: ~15KB total vs previous ~50KB scattered loading  
**Agent Coverage**: 100% of agents use this system (orchestrator, specialists, coordinators, experimental)

## INTEGRATION NOTES

This file is:
- **Universal**: Works for ANY agent (current: 12 agents, future: unlimited)
- **Template-Integrated**: Automatically used by agent.yaml template system
- **Bootstrap-Safe**: Handles its own file resolution and loading
- **Error-Tolerant**: Continues with available context if some files missing
- **Performance-Optimized**: Parallel loading with validation gates

**Next Step**: After FOUNDATION_READY, agents proceed to dynamic-context-resolver.md for contextual loading