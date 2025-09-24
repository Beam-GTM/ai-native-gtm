# Feature Implementation Workflow

## Critical Execution Notice

This workflow handles the implementation phase of feature creation, taking planning artifacts as input and creating a complete feature workspace with all necessary files, tracking, and validation. It can be used after plan-feature workflow or with manually created planning artifacts.

---

## Workflow Definition

```yaml
workflow:
  id: implement-feature
  name: Feature Implementation & Workspace Creation
  description: >-
    Workflow for creating organized feature workspaces from planning artifacts.
    Generates PRD, progress tracking, quality gates, and validation checklists
    using framework templates and ensures all dependencies are properly configured.
  type: implementation
  project_types:
    - workspace-creation
    - feature-implementation
    - template-generation
    - validation-setup
  complexity: medium
  target_system: implementation

context:
  situation: 'User has planning artifacts and needs to create implementation workspace'
  assumptions:
    - 'Planning artifacts exist (from plan-feature or manual creation)'
    - 'Framework templates available for file generation'
    - 'Workspace structure supports organized development'
    - 'Quality gates and validation needed'
  success_criteria:
    - 'Complete workspace created with all files'
    - 'PRD generated from planning artifacts'
    - 'Progress tracking configured'
    - 'Quality gates established'
    - 'Feature checklist created'
    - 'Dependencies validated'
    - 'Milestone recorded in project memory'
  
  required_tasks:
    - framework/tasks/feature/create-feature-checklist.md
    - framework/tasks/feature/update-project-milestone.md
    - framework/tasks/validation/validate-dependencies.md
    - framework/tasks/memory/update-project-memory.md

# DEPENDENCIES DECLARATION
dependencies:
  engineering_rules:
    primary:
      - framework/engineeringrules/core-foundation/file-management.md
      - framework/engineeringrules/system-operations/template-management.md
      - framework/engineeringrules/core-foundation/quality-assurance.md
    
    contextual:
      - framework/engineeringrules/core-foundation/placement-standards.md
      - framework/engineeringrules/core-foundation/memory-system.md
  
  agents:
    - operations/agents/core/orchestrator.md
    - operations/agents/specialists/quality-assurance.md
  
  checklists:
    - operations/checklists/quality-gate.md
  
  templates:
    - framework/templates/features/prd.yaml
    - framework/templates/features/active-context.yaml
    - framework/templates/features/progress.yaml
    - framework/templates/features/quality-gates.yaml

# INPUT ARTIFACTS
input_artifacts:
  required:
    feature_definition:
      location: 'workspace/features/active/{feature-name}/artifacts/feature-definition.yaml'
      fallback: 'Prompt user for feature details'
    
    technical_design:
      location: 'workspace/features/active/{feature-name}/artifacts/technical-design.yaml'
      fallback: 'Use simplified technical approach'
    
    resource_plan:
      location: 'workspace/features/active/{feature-name}/artifacts/resource-plan.yaml'
      fallback: 'Use default resource estimates'
    
    elicitation_insights:
      location: 'workspace/features/active/{feature-name}/artifacts/elicitation-insights.yaml'
      fallback: 'Proceed without integration insights'
  
  optional:
    planning_complete:
      location: 'workspace/features/active/{feature-name}/artifacts/planning-complete.yaml'
      purpose: 'Additional context and notes'

# WORKFLOW SEQUENCE
sequence:
  - step: validate_inputs
    agent: orchestrator
    action: 'Validate planning artifacts exist and are valid'
    validates:
      - artifacts/feature-definition.yaml
      - artifacts/technical-design.yaml
      - artifacts/resource-plan.yaml
      - artifacts/elicitation-insights.yaml
    requires: []
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Input validation:
      - Check if artifacts directory exists
      - Validate YAML structure of each artifact
      - Ensure required fields are present
      - Handle missing artifacts with fallbacks
      - Report validation status
      
      If artifacts missing:
      - Offer to run plan-feature workflow first
      - Or collect minimal information interactively

  - step: workspace_creation
    agent: orchestrator
    action: 'Create organized feature workspace structure'
    creates: workspace/features/active/{feature-name}/
    requires:
      - validated input artifacts
    notes: |
      Workspace structure creation:
      - Create workspace/features/active/{feature-name}/ directory
      - Create subdirectories if needed (artifacts/, docs/, tests/)
      - Set up proper permissions
      - Initialize with .gitkeep if needed
      
      Apply file management standards

  - step: prd_generation
    agent: orchestrator
    action: 'Generate comprehensive PRD from planning artifacts'
    creates: workspace/features/active/{feature-name}/prd.md
    requires:
      - artifacts/feature-definition.yaml
      - artifacts/technical-design.yaml
      - artifacts/resource-plan.yaml
      - artifacts/elicitation-insights.yaml
    uses: framework/templates/features/prd.yaml
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      PRD generation from artifacts:
      - Load and parse all planning artifacts
      - Merge data into PRD template structure
      - Include problem statement from feature-definition
      - Add technical architecture from technical-design
      - Include resource requirements from resource-plan
      - Integrate discovered dependencies from elicitation
      - Add quality gates and success criteria
      
      Apply PRD writing standards

  - step: progress_tracking_setup
    agent: orchestrator
    action: 'Create progress tracking with task breakdown'
    creates: workspace/features/active/{feature-name}/progress.md
    requires:
      - artifacts/technical-design.yaml
      - artifacts/resource-plan.yaml
    uses: framework/templates/features/progress.yaml
    notes: |
      Progress tracking setup:
      - Break down implementation phases from technical design
      - Create task list from components
      - Set up sprint planning structure
      - Include time estimates from resource plan
      - Add milestone tracking
      - Configure progress percentages
      
      Structure for easy updates

  - step: quality_gates_configuration
    agent: quality-assurance
    action: 'Configure quality gates and validation criteria'
    creates: workspace/features/active/{feature-name}/quality-gates.md
    requires:
      - artifacts/resource-plan.yaml
      - workspace/features/active/{feature-name}/prd.md
    uses: framework/templates/features/quality-gates.yaml
    notes: |
      Quality gates configuration:
      - Set up 5 standard gates (Design, Code, Test, Docs, Deploy)
      - Configure PASS/CONCERNS/FAIL/WAIVED framework
      - Add specific criteria from resource plan
      - Include testing requirements
      - Add validation checklists
      - Set approval requirements
      
      Apply quality assurance standards

  - step: active_context_initialization
    agent: orchestrator
    action: 'Initialize active context for work tracking'
    creates: workspace/features/active/{feature-name}/active-context.md
    requires:
      - workspace/features/active/{feature-name}/prd.md
    uses: framework/templates/features/active-context.yaml
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Active context initialization:
      - Set up current work tracking
      - Initialize with feature overview
      - Add implementation start timestamp
      - Include key decisions from planning
      - Set up session tracking
      - Configure for context persistence
      
      Enable cross-chat continuity

  - step: checklist_generation
    agent: orchestrator
    action: 'Generate comprehensive feature validation checklist'
    creates: workspace/features/active/{feature-name}/feature-checklist.md
    requires:
      - workspace/features/active/{feature-name}/prd.md
      - workspace/features/active/{feature-name}/quality-gates.md
    uses: framework/tasks/feature/create-feature-checklist.md
    notes: |
      Checklist generation:
      - Execute create-feature-checklist task
      - Analyze feature type and requirements
      - Generate validation categories
      - Include functional checks
      - Add technical validations
      - Include integration tests
      - Add quality checkpoints
      
      Comprehensive validation coverage

  - step: dependency_validation
    agent: orchestrator
    action: 'Validate all dependencies are properly configured'
    creates: workspace/features/active/{feature-name}/dependency-validation.md
    requires:
      - All workspace files created
    uses: framework/tasks/validation/validate-dependencies.md
    notes: |
      Dependency validation:
      - Execute validate-dependencies task
      - Check all 8 dependency categories
      - Validate file references
      - Check engineering rule links
      - Verify template usage
      - Validate task references
      - Generate health report
      
      Ensure everything is connected

  - step: milestone_recording
    agent: orchestrator
    action: 'Record feature creation milestone in project memory'
    updates: workspace/memory/project-memory.md
    requires:
      - workspace/features/active/{feature-name}/feature-checklist.md
    uses: framework/tasks/feature/update-project-milestone.md
    notes: |
      Milestone recording:
      - Execute update-project-milestone task
      - Record feature workspace creation
      - Update with implementation start
      - Check pattern extraction triggers
      - Maintain memory integrity
      
      Track project progress

# QUALITY GATES
quality_gates:
  - gate: inputs_validated
    trigger: 'after validate_inputs'
    criteria:
      - 'Planning artifacts exist or fallbacks available'
      - 'YAML structure valid'
      - 'Required fields present'
      - 'Data consistency verified'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'Validation report'

  - gate: workspace_created
    trigger: 'after workspace_creation'
    criteria:
      - 'Directory structure complete'
      - 'Permissions set correctly'
      - 'Path follows standards'
      - 'No conflicts with existing features'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'workspace/features/active/{feature-name}/'

  - gate: files_generated
    trigger: 'after active_context_initialization'
    criteria:
      - 'PRD generated successfully'
      - 'Progress tracking configured'
      - 'Quality gates established'
      - 'Active context initialized'
      - 'All templates populated correctly'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'All workspace files'

  - gate: validation_complete
    trigger: 'after dependency_validation'
    criteria:
      - 'Feature checklist created'
      - 'Dependencies validated'
      - 'No critical issues found'
      - 'Health score acceptable'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'feature-checklist.md'
      - 'dependency-validation.md'

  - gate: implementation_ready
    trigger: 'after milestone_recording'
    criteria:
      - 'All files generated'
      - 'Validation passed'
      - 'Milestone recorded'
      - 'Ready for development'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'Complete workspace'
      - 'Updated project memory'

# OUTPUT STRUCTURE
output_structure:
  workspace_location: 'workspace/features/active/{feature-name}/'
  
  generated_files:
    - prd.md                    # Comprehensive PRD from artifacts
    - active-context.md         # Work tracking and context
    - progress.md              # Task breakdown and tracking
    - quality-gates.md         # Validation framework
    - feature-checklist.md     # Comprehensive checklist
    - dependency-validation.md # Validation report
  
  preserved_artifacts:
    - artifacts/               # Planning artifacts preserved
  
  ready_for:
    - Development work
    - Testing implementation
    - Documentation
    - Quality validation

# ERROR HANDLING
error_handling:
  missing_artifacts:
    action: 'Offer to run plan-feature workflow'
    fallback: 'Collect minimal information interactively'
  
  template_generation_failure:
    action: 'Retry with default values'
    fallback: 'Create basic file structure'
  
  validation_failure:
    action: 'Document issues and continue'
    warning: 'Feature may have integration issues'
  
  workspace_conflict:
    action: 'Prompt for new feature name'
    fallback: 'Add timestamp suffix'

# INTEGRATION POINTS
integration:
  from_plan_feature:
    seamless: true
    artifacts_location: 'workspace/features/active/{feature-name}/artifacts/'
    validation: 'Automatic artifact discovery'
  
  from_manual_planning:
    supported: true
    requirements: 'Artifacts in correct YAML format'
    validation: 'Schema checking with fallbacks'
  
  to_development:
    handoff: 'Complete workspace ready'
    documentation: 'All context preserved'
    tracking: 'Progress system initialized'

# SUCCESS COMPLETION
completion_message: |
  🚀 Feature Implementation Workspace Created!
  
  Feature: {feature-name}
  Workspace: workspace/features/active/{feature-name}/
  Files Generated: 6
  
  ✅ PRD created from planning artifacts
  ✅ Progress tracking configured
  ✅ Quality gates established
  ✅ Active context initialized
  ✅ Feature checklist generated
  ✅ Dependencies validated
  ✅ Milestone recorded
  
  Workspace Contents:
  📋 prd.md - Complete requirements and design
  📊 progress.md - Task breakdown and tracking
  🛡️ quality-gates.md - Validation framework
  ⚡ active-context.md - Work tracking
  ✅ feature-checklist.md - Validation checklist
  🔍 dependency-validation.md - Health report
  
  Next Steps:
  1. Review generated PRD
  2. Check progress tracking tasks
  3. Begin implementation
  4. Update progress as you work
  5. Use quality gates for validation
  
  Feature workspace ready for development!
```