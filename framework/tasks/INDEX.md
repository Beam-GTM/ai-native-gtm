<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.653634Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.250559Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Framework Tasks Index

**Total Tasks**: 22  
**Categories**: System, Memory, Validation, Feature, Session, Analysis

## Memory Tasks (8)
- `memory/aggregate-core-learnings.md` - Consolidate patterns into always-loaded file
- `memory/capture-primitive-learning.md` - On-demand capture of LLM behavioral patterns
- `memory/consolidate-learnings.md` - Consolidate learning artifacts
- `memory/extract-memory-patterns.md` - Extract patterns from project memory
- `memory/memory-recovery.md` - Recover memory system from failures
- `memory/rotate-project-memory.md` - Archive old memory entries
- `memory/update-project-memory.md` - Update project memory with milestones
- `memory/validate-memory-integrity.md` - Check memory system health

## System Tasks (5)
- `system/generate-template.md` - Create clean distributable template from system
- `system/system-sync.md` - Full system synchronization super task
- `system/update-all-indices.md` - Update all INDEX files across system
- `system/update-indices-with-content.md` - Update indices with content extraction
- `system/update-system-structure.md` - Update SYSTEM-STRUCTURE.md map

## Validation Tasks (3)
- `validation/validate-dependencies.md` - Check unidirectional dependencies
- `validation/validate-bidirectional-dependencies.md` - Check bidirectional dependencies
- `validation/validate-agent-compliance.md` - Validate agents against template standards

## Feature Tasks (2)
- `feature/create-feature-checklist.md` - Generate feature validation checklist
- `feature/update-project-milestone.md` - Record feature milestones

## Session Tasks (3)
- `session/session-summary.md` - Generate comprehensive session summary
- `session/feature-archival.md` - Archive completed features to completed/
- `session/closure-report.md` - Generate session closure report

## Analysis Tasks (1)
- `analysis/analyze-learnings-to-features.md` - Transform learnings into feature proposals

## Task Metadata
```yaml
tasks:
  memory:
    - id: aggregate-core-learnings
      aliases: ['aggregate-learnings', 'consolidate-patterns']
      type: memory
      complexity: medium
      auto_trigger: true
      
    - id: capture-primitive-learning
      aliases: ['capture-learning', 'primitive']
      type: memory
      complexity: simple
      
    - id: extract-memory-patterns
      type: memory
      complexity: medium
      
    - id: memory-recovery
      type: memory
      complexity: high
      
    - id: rotate-project-memory
      type: memory
      complexity: simple
      
    - id: update-project-memory
      type: memory
      complexity: simple
      
    - id: validate-memory-integrity
      type: memory
      complexity: medium
      
  system:
    - id: system-sync
      type: system
      complexity: high
      super_task: true
      
    - id: update-all-indices
      type: system
      complexity: medium
      
    - id: update-indices-with-content
      type: system
      complexity: high
      
    - id: update-system-structure
      type: system
      complexity: medium
      
  validation:
    - id: validate-dependencies
      type: validation
      complexity: medium
      
    - id: validate-bidirectional-dependencies
      type: validation
      complexity: high
      
    - id: validate-agent-compliance
      type: validation
      complexity: medium
      aliases: ['validate-agent', 'check-agent']
      
    - id: ultrathink-validation
      type: validation
      complexity: critical
      priority: CRITICAL
      auto_trigger: true
      
  feature:
    - id: create-feature-checklist
      type: feature
      complexity: simple
      
    - id: update-project-milestone
      type: feature
      complexity: simple
      
  session:
    - id: session-summary
      type: session
      complexity: simple
      auto_trigger: true
      
    - id: feature-archival
      type: session
      complexity: medium
      
    - id: closure-report
      type: session
      complexity: simple
      auto_trigger: true
      
  analysis:
    - id: analyze-learnings-to-features
      type: analysis
      complexity: high
      aliases: ['analyze-learnings', 'learning-analysis']
      priority: high
```

## Quick Access Commands
- `*capture-learning` - Capture primitive learning on-demand
- `*system-sync` - Run full system synchronization
- `*validate-deps` - Check all dependencies
- `*update-indices` - Refresh all INDEX files

---
*Tasks provide automated and semi-automated operations for the Nexus system*