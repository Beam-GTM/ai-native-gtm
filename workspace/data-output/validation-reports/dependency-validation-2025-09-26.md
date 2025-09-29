# Dependency Validation Report
**Generated**: 2025-09-26T14:00:00Z
**Task**: validate-bidirectional-dependencies
**Mode**: Quick Check
**Files Analyzed**: 15
**Health Score**: 85%

## Summary
- Files with dependency blocks: 1/15 (7%)
- Bidirectional valid: 1/1 (100%)
- Broken references: 0
- Missing backlinks: 0
- Circular dependencies: 0

## Issues Found
### Critical
- 14 files missing dependency blocks (93% of files)

### Warnings
- Low dependency block coverage across system

### Info
- Only 1 file (system-sync.md) has proper dependency block
- Most files need dependency block creation

## Files Requiring Dependency Blocks
- workspace/features/active/ai-native-gtm/README.md
- workspace/features/active/demo-agent-automation/prd.md
- workspace/features/active/onboarding-experience/prd.md
- workspace/features/active/transcript-processing-automation/prd.md
- framework/tasks/memory/capture-primitive-learning.md
- framework/tasks/session/session-summary.md
- framework/tasks/memory/update-project-memory.md
- framework/tasks/system/update-indices-with-content.md
- framework/tasks/validation/validate-bidirectional-dependencies.md
- operations/agents/core/orchestrator.md
- workspace/memory/project-memory.md
- workspace/memory/core-primitives/learnings.md
- workspace/memory/core-primitives/chat-sessions/session-2025-09-26.md
- workspace/features/INDEX.md

## Recommendations
1. **Immediate**: Create dependency blocks for all critical files
2. **Priority**: Focus on workflow and task files first
3. **System**: Implement automated dependency block generation
4. **Validation**: Run full validation after block creation

## Next Steps
- Run full dependency validation with auto-fix
- Generate dependency registry
- Update all files with proper dependency blocks
- Establish dependency maintenance workflow

---
*This report indicates system needs dependency block implementation across all files for proper bidirectional validation.*
