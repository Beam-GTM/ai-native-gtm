# Feature Planning Workflow

## Critical Execution Notice

This workflow handles the planning and design phase of feature creation, including interactive elicitation, requirements gathering, and artifact generation. It produces structured planning artifacts that can be used by the implement-feature workflow or standalone for planning-only needs.

---

## Workflow Definition

```yaml
workflow:
  id: plan-feature
  name: Feature Planning & Design
  description: >-
    Interactive workflow for feature planning, elicitation, and design that produces
    structured artifacts for implementation. Focuses on discovery, requirements gathering,
    technical planning, and comprehensive system integration analysis.
  type: planning
  project_types:
    - feature-planning
    - requirements-gathering
    - system-design
    - elicitation-discovery
  complexity: medium
  target_system: planning

context:
  situation: 'User needs to plan a feature with comprehensive requirements and system integration discovery'
  assumptions:
    - 'User has basic idea of what they want to build'
    - 'Elicitation methods available for deeper discovery'
    - 'Planning artifacts will drive implementation'
    - 'System integration points need discovery'
  success_criteria:
    - 'Complete planning artifacts generated'
    - 'System integration points discovered through elicitation'
    - 'Technical approach clearly defined'
    - 'Resource requirements estimated'
    - 'Risks and mitigations identified'
    - 'Quality gates defined for implementation'
  
  required_tasks:
    - framework/tasks/memory/update-project-memory.md
    - framework/tasks/memory/update-project-memory.md

# DEPENDENCIES DECLARATION
dependencies:
  engineering_rules:
    primary:
      - framework/engineeringrules/core-foundation/documentation-standards.md
      - framework/engineeringrules/core-foundation/system-design-principles.md
      - framework/engineeringrules/product-management/prd-writing.md
    
    contextual:
      - framework/engineeringrules/core-foundation/memory-system.md
      - framework/engineeringrules/development/coding-standards.md
  
  agents:
    - operations/agents/core/orchestrator.md
    - operations/agents/specialists/product-manager.md
    - operations/agents/core/architect.md
  
  checklists:
    - operations/checklists/quality-gate.md

# WORKFLOW SEQUENCE
sequence:
  - step: feature_definition
    agent: orchestrator
    action: 'Interactive feature definition with user input collection'
    creates: artifacts/feature-definition.yaml
    requires: []
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Interactive user prompts for feature definition:
      - Feature Name: Collect kebab-case name, validate uniqueness
      - Problem Statement: What problem does this solve? (min 20 chars)
      - Success Criteria: 2-3 measurable outcomes
      - Feature Type: frontend/backend/fullstack/integration/framework
      - Priority: critical/high/medium/low
      - Validate all inputs before proceeding
      - Apply documentation standards for quality
      
      SAVE OUTPUT: Store as structured YAML artifact

  - step: interactive_elicitation_session
    agent: product-manager
    action: 'Interactive elicitation using proven discovery techniques'
    creates: artifacts/elicitation-insights.yaml
    requires:
      - artifacts/feature-definition.yaml
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      
      INTERACTIVE ELICITATION TOOLKIT:
      
      **Core Reflective Methods** (Start here):
      1. **Expand or Contract**: "Should we go deeper on [topic] or simplify for clarity?"
      2. **Explain Reasoning**: "Walk me through your thinking on [decision]"
      3. **Critique and Refine**: "What's wrong with this approach? How would you improve it?"
      
      **Structural Analysis Methods**:
      4. **Analyze Dependencies**: "What happens if [component] fails? What breaks?"
      5. **Assess Alignment**: "How does this serve our real goal? What's misaligned?"
      
      **Multi-Persona Collaboration**:
      6. **Agile Team Perspectives**: Rotate through Product Owner → Developer → QA → Scrum Master views
      7. **Stakeholder Round Table**: Business → Technical → Operations → Security perspectives
      
      **Risk and Challenge Methods**:
      8. **Identify Risks**: "What could go wrong? What are we not seeing?"
      9. **Devil's Advocate**: "Let me argue against this... [challenge from critical perspective]"
      
      **Creative Exploration**:
      10. **Tree of Thoughts**: Break into discrete steps, explore multiple paths
      11. **Hindsight 20/20**: "Imagine this failed. What would we say 'if only we had...'?"
      
      **Interactive Brainstorming** (When stuck):
      - **What If Scenarios**: "What if we had unlimited budget? Zero budget?"
      - **Reversal/Inversion**: "What if we did the opposite of our plan?"
      - **Five Whys**: Keep asking "why" to reach root needs
      - **Red Team vs Blue Team**: Attack the plan, then defend it
      
      **Process**: Use 3-5 techniques per session. Let conversation flow naturally.
      
      SAVE OUTPUT: Discovered insights, risks, dependencies, and system integration points

  - step: technical_planning
    agent: architect
    action: 'Guide technical architecture and component planning'
    creates: artifacts/technical-design.yaml
    requires:
      - artifacts/feature-definition.yaml
      - artifacts/elicitation-insights.yaml
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Technical planning with elicitation insights:
      - Technical Approach: Architecture patterns and design
      - Key Components: 3-5 main components with purposes
      - Integration Points: APIs, databases, services (from elicitation)
      - Dependencies: Technical requirements discovered
      - Implementation Phases: Logical breakdown
      - Performance Considerations: Load, scaling, resources
      
      Apply system design principles throughout
      
      SAVE OUTPUT: Complete technical design artifact

  - step: resource_planning
    agent: product-manager
    action: 'Resource estimation and risk assessment'
    creates: artifacts/resource-plan.yaml
    requires:
      - artifacts/technical-design.yaml
      - artifacts/elicitation-insights.yaml
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Resource planning with complexity assessment:
      - Skills Required: Technical expertise needed
      - Time Estimate: Effort based on discovered complexity
      - Risks & Mitigations: Include elicitation discoveries
      - Quality Gates: Validation checkpoints
      - Testing Strategy: Unit, integration, system tests
      - Dependencies: External requirements
      
      Factor in hidden complexities from elicitation
      
      SAVE OUTPUT: Comprehensive resource plan

  - step: ultrathink_validation_consolidation
    agent: orchestrator
    action: 'ULTRATHINK validation and artifact consolidation'
    creates: artifacts/planning-complete.yaml
    requires:
      - artifacts/feature-definition.yaml
      - artifacts/elicitation-insights.yaml
      - artifacts/technical-design.yaml
      - artifacts/resource-plan.yaml
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      
      **ULTRATHINK VALIDATION CHECKPOINT**:
      
      1. **Surface Analysis**: Review apparent completeness and obvious gaps
      2. **Deep Pattern Analysis**: What hidden dependencies or complexities did we miss?
      3. **Adversarial Thinking**: Play devil's advocate - what could go wrong?
      4. **Self-Consistency Check**: Do our artifacts contradict each other?
      5. **Hindsight Preview**: "Imagine this feature failed. What would we say we missed?"
      
      **Quick Validation Questions**:
      - "What's the one thing that could kill this feature?"
      - "What assumption are we making that might be wrong?"
      - "What would a critic say about this plan?"
      - "Is this actually solving the right problem?"
      
      **Consolidation Tasks**:
      - Verify all artifacts are complete
      - Check cross-artifact consistency  
      - Address ULTRATHINK-discovered gaps
      - Ensure implementation readiness
      - Create summary for handoff
      - Update project memory with planning milestone
      
      SAVE OUTPUT: ULTRATHINK-validated planning package

# QUALITY GATES
quality_gates:
  - gate: feature_definition_complete
    trigger: 'after feature_definition'
    criteria:
      - 'Feature name is valid and unique'
      - 'Problem statement is clear (>20 chars)'
      - 'Success criteria are measurable'
      - 'Feature type is appropriate'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'artifacts/feature-definition.yaml'

  - gate: elicitation_complete
    trigger: 'after elicitation_session'
    criteria:
      - 'System dependencies discovered'
      - 'Integration points identified'
      - 'Hidden complexities uncovered'
      - 'Risk factors documented'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'artifacts/elicitation-insights.yaml'

  - gate: technical_design_complete
    trigger: 'after technical_planning'
    criteria:
      - 'Architecture approach defined'
      - 'Components identified with purposes'
      - 'Integration points documented'
      - 'Dependencies listed'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'artifacts/technical-design.yaml'

  - gate: resource_plan_complete
    trigger: 'after resource_planning'
    criteria:
      - 'Skills and expertise identified'
      - 'Time estimates realistic'
      - 'Risks assessed with mitigations'
      - 'Testing strategy defined'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'artifacts/resource-plan.yaml'

  - gate: planning_artifacts_complete
    trigger: 'after artifact_consolidation'
    criteria:
      - 'All artifacts generated'
      - 'Cross-artifact consistency verified'
      - 'Implementation readiness confirmed'
      - 'Handoff package complete'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'artifacts/planning-complete.yaml'

# OUTPUT ARTIFACTS
output_artifacts:
  feature_definition:
    location: 'workspace/features/active/{feature-name}/artifacts/feature-definition.yaml'
    schema:
      feature_name: string
      problem_statement: string
      success_criteria: array
      feature_type: enum
      priority: enum
      created_date: timestamp
  
  elicitation_insights:
    location: 'workspace/features/active/{feature-name}/artifacts/elicitation-insights.yaml'
    schema:
      system_dependencies: array
      integration_points: array
      hidden_complexities: array
      risk_factors: array
      coordination_needs: array
  
  technical_design:
    location: 'workspace/features/active/{feature-name}/artifacts/technical-design.yaml'
    schema:
      architecture_approach: string
      key_components: array
      integration_points: array
      dependencies: array
      implementation_phases: array
      performance_considerations: object
  
  resource_plan:
    location: 'workspace/features/active/{feature-name}/artifacts/resource-plan.yaml'
    schema:
      skills_required: array
      time_estimate: object
      risks_mitigations: array
      quality_gates: array
      testing_strategy: object
      external_dependencies: array
  
  planning_complete:
    location: 'workspace/features/active/{feature-name}/artifacts/planning-complete.yaml'
    schema:
      summary: string
      artifacts: array
      ready_for_implementation: boolean
      handoff_notes: string

# HANDOFF PROTOCOL
handoff_protocol:
  to_implementation:
    trigger: 'planning_artifacts_complete gate PASSED'
    artifacts_provided:
      - feature-definition.yaml
      - elicitation-insights.yaml
      - technical-design.yaml
      - resource-plan.yaml
      - planning-complete.yaml
    
    handoff_message: |
      Planning Complete - Ready for Implementation
      
      Feature: {feature-name}
      Planning Duration: {duration}
      Artifacts Generated: 5
      
      Key Discoveries:
      - System Dependencies: {count}
      - Integration Points: {count}
      - Risk Factors: {count}
      
      Implementation can proceed with:
      - Complete requirements in feature-definition.yaml
      - System insights in elicitation-insights.yaml
      - Architecture in technical-design.yaml
      - Resources in resource-plan.yaml
      
      Next: Run implement-feature workflow or proceed manually

# ADAPTIVE BEHAVIOR
adaptive_behavior:
  complexity_adjustment:
    simple_features:
      - Skip detailed elicitation if low integration
      - Streamline technical planning
      - Quick resource estimation
    
    complex_features:
      - Deep elicitation with multiple methods
      - Detailed architecture exploration
      - Comprehensive risk analysis
  
  elicitation_selection:
    based_on_feature_type:
      frontend: 'Focus on UX perspectives and user journey'
      backend: 'Focus on data flow and service dependencies'
      fullstack: 'Balance all perspectives equally'
      integration: 'Deep dive on system boundaries'
      framework: 'Focus on extensibility and patterns'

# ERROR HANDLING
error_handling:
  validation_failures:
    action: 'Re-prompt with specific guidance'
    max_retries: 3
  
  missing_dependencies:
    action: 'Document and continue with warnings'
    fallback: 'Manual intervention required'
  
  artifact_generation_failure:
    action: 'Retry with simplified schema'
    fallback: 'Generate text documentation'

# SUCCESS COMPLETION
completion_message: |
  🎯 Feature Planning Complete!
  
  Feature: {feature-name}
  Planning Artifacts: 5 files generated
  
  ✅ Requirements defined and validated
  ✅ System integration points discovered
  ✅ Technical approach designed
  ✅ Resources and timeline estimated
  ✅ Ready for implementation
  
  Artifacts saved to:
  workspace/features/active/{feature-name}/artifacts/
  
  Next Steps:
  1. Review planning artifacts
  2. Run 'implement-feature' workflow
  3. Or proceed with manual implementation
  
  Planning insights captured and ready for use!
```