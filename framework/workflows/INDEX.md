# Framework Workflows Index

**Total Workflows**: 9  
**Organization**: Purpose-based subcategories (following task pattern)
**Structure**: Organized by workflow purpose for intuitive navigation

## Feature Workflows (2)
Located in `feature/`
- `plan-feature.md` - Interactive feature planning with elicitation and design
- `implement-feature.md` - Feature implementation and workspace creation from planning artifacts

## System Workflows (1)  
Located in `system/`
- `close-chat.md` - Session closure with system integrity checks, memory management, and feature archival

## Analysis Workflows (2)
Located in `analysis/`
- `consolidate-learning-knowledge.md` - Consolidate learning artifacts into structured knowledge
- `ultrathink-learning-analysis.md` - Deep analysis of learnings using ULTRATHINK methodology

## Documentation Workflows (4)
Located in `documentation/`
- `full-documentation-update.md` - Comprehensive documentation generation and updates
- `development.md` - Development workflow documentation processes  
- `system-maintenance.md` - System maintenance documentation workflows
- `diagrams.md` - Diagram generation and maintenance workflows

## Workflow Metadata
```yaml
workflows:
  feature_management:
    - id: plan-feature
      type: planning
      complexity: high
      outputs: [feature-definition, technical-design, resource-plan]
      purpose: Interactive feature planning and design
      
    - id: implement-feature
      type: implementation
      complexity: medium
      requires: planning_artifacts
      purpose: Create feature workspace from artifacts
      
  session_management:
    - id: close-chat
      type: maintenance
      priority: critical
      complexity: high
      engines: 5
      purpose: Automated session closure with system integrity
```

## Quick Access Commands
- `*workflow plan-feature` - Plan a new feature interactively
- `*workflow implement-feature` - Create workspace from planning artifacts  
- `*workflow close-chat` - Execute session closure with integrity checks
- `bye` / `exit` / `quit` / `close` - Trigger close-chat workflow

## Workflow Relationships
```
plan-feature (planning phase)
├── feature-definition.yaml
├── technical-design.yaml
├── resource-plan.yaml
├── elicitation-insights.yaml
└── planning-complete.yaml
    ↓ (sequential user-controlled execution)
implement-feature (implementation phase)
├── prd.md
├── progress.md
├── quality-gates.md
├── active-context.md
└── feature-checklist.md

close-chat (maintenance)
├── Session Capture Engine
├── System Validation Engine  
├── Memory Management Engine
├── Feature Lifecycle Engine
└── System Synchronization Engine
```

---
*Workflows provide coordinated multi-step processes for the Nexus system*