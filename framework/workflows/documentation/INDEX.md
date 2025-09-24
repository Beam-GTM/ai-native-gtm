# Workflow Index - Dynamic Loading Registry
**Updated**: 2025-08-26T14:00:00Z  
**Total Workflows**: 6  
**Loading**: Use `*workflow [name]` for execution
**Growth Strategy**: Extract workflows when patterns emerge (>2x/week usage)

## Active Workflows (6)

### Core Development Workflow
```yaml
development:
  name: Development Workflow
  description: Core development process with quality gates
  type: core
  path: development.md
  phases:
    - planning
    - implementation
    - validation
    - completion
  quality_gates:
    - Design Review
    - Code Quality
    - Testing Complete
    - Documentation Complete
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

### Feature Planning Workflow
```yaml
plan-feature:
  name: Feature Planning & Design
  description: Interactive planning, elicitation, and design workflow that produces structured artifacts for implementation
  type: planning
  path: ../../framework/workflows/plan-feature.md
  phases:
    - feature-definition
    - elicitation-session
    - technical-planning
    - resource-planning
    - artifact-consolidation
  outputs:
    - feature-definition.yaml
    - elicitation-insights.yaml
    - technical-design.yaml
    - resource-plan.yaml
    - planning-complete.yaml
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

### Feature Implementation Workflow
```yaml
implement-feature:
  name: Feature Implementation & Workspace Creation
  description: Creates organized feature workspaces from planning artifacts with all tracking and validation
  type: implementation
  path: ../../framework/workflows/implement-feature.md
  phases:
    - validate-inputs
    - workspace-creation
    - prd-generation
    - progress-tracking-setup
    - quality-gates-configuration
    - checklist-generation
    - dependency-validation
    - milestone-recording
  inputs:
    - planning artifacts from plan-feature
  outputs:
    - complete feature workspace
    - PRD documentation
    - progress tracking
    - quality gates
    - validation checklist
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

### Interactive Feature Design Workflow (Orchestrator)
```yaml
design-new-feature:
  name: Design New Feature
  description: Complete feature creation workflow that orchestrates planning and implementation phases
  type: orchestrator
  path: ../../framework/workflows/design-new-feature.md
  delegates_to:
    - plan-feature
    - implement-feature
  backward_compatible: true
  phases:
    - Execute plan-feature workflow
    - Validate planning artifacts
    - Execute implement-feature workflow
    - Validate complete workspace
  outputs:
    - planning artifacts
    - complete feature workspace
    - comprehensive documentation
    - quality validation framework
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

### System Maintenance Workflow  
```yaml
system-maintenance:
  name: System Maintenance
  description: Interactive system maintenance workflow with sync operations
  type: maintenance
  path: system-maintenance.md
  phases:
    - system-analysis
    - sync-planning
    - execution
    - validation
  operations:
    - sync-check
    - sync-indices
    - sync-structure
    - sync-validate
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

### Session Closure Workflow
```yaml
close-chat:
  name: Session Closure Automation
  description: Comprehensive session closure with integrity checks, memory management, and feature archival
  type: maintenance
  priority: critical
  path: ../../framework/workflows/close-chat.md
  phases:
    - session-capture (parallel)
    - system-validation (sequential)
    - memory-management (conditional)
    - feature-lifecycle (parallel)
    - system-synchronization (orchestrated)
  engines: 5
  execution_modes:
    - standard (< 2 minutes)
    - quick (< 30 seconds)
    - force (< 10 seconds)
  triggers:
    - bye
    - exit
    - quit
    - close
  outputs:
    - session summary
    - closure report
    - archived features
    - validated system
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

### Documentation Update Workflow
```yaml
full-documentation-update:
  name: Full Documentation Update
  description: Comprehensive documentation update and maintenance workflow
  type: documentation
  path: documentation/full-documentation-update.md
  phases:
    - documentation-audit
    - content-update
    - structure-validation
    - publication
  scope:
    - system-documentation
    - api-documentation
    - user-documentation
  decision_framework: PASS | CONCERNS | FAIL | WAIVED
```

## Planned Workflows (Pattern-Based Growth)

### Emerging Patterns to Monitor
```yaml
# These will be extracted when usage patterns justify them

feature-development:
  trigger: "EXTRACTED - Now available as design-new-feature workflow"
  pattern: "definition → planning → resource-planning → quality-setup → workspace-creation"
  
system-generation:
  trigger: "When generation commands used >3x/week"
  pattern: "template → customize → validate → deploy"
  
maintenance:
  trigger: "When cleanup/update tasks repeated >2x/week"
  pattern: "analyze → plan → execute → verify"
```

## Quick Selection

### By Purpose
- **General Development**: development (handles all development tasks)
- **Feature Creation**: design-new-feature (guides systematic feature planning)
- **Session Management**: close-chat (automated session closure with integrity checks)

### By Complexity
- **Adaptive**: development (scales to project needs)

### By Duration
- **Variable**: development (adapts to task scope)

## Loading Pattern
```yaml
command: "*workflow {name}"
resolution:
  1. Check workflow in this index
  2. Resolve to workflows/{name}.md
  3. Load workflow definition
  4. Initialize workflow engine
  5. Apply quality framework
  6. Cache for execution
```

## Workflow Execution Flow
1. **Initialization**: Load workflow definition
2. **Context Setup**: Establish workflow context
3. **Phase Execution**: Execute workflow phases
4. **Quality Gates**: Validate at checkpoints (PASS/CONCERNS/FAIL/WAIVED)
5. **Completion**: Update progress and extract patterns

## Growth Triggers

### Pattern Recognition
Monitor workflow executions for:
- **Repeated Sequences**: Same phase pattern >2x/week
- **Custom Flows**: Manual workflow variations
- **Domain Patterns**: Industry-specific workflows
- **Integration Needs**: External system workflows

### Extraction Protocol
When pattern identified:
1. Document pattern in workspace/features/patterns/
2. Create workflow definition
3. Add to this INDEX.md
4. Update MANIFEST.md
5. Test workflow execution

## Dynamic Resolution
- Fuzzy matching at 85% confidence
- Partial names supported (e.g., "dev" → "development")
- Growth hints shown when no match
- Pattern suggestions based on usage

## Integration Points
- **Features**: Workflows integrate with feature lifecycle
- **Agents**: Orchestrator coordinates workflow execution
- **Quality**: All workflows use quality gate framework
- **Patterns**: Successful workflows become templates