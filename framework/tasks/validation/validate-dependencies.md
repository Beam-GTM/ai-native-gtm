<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.337615Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.348114Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.064879Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Validate Dependencies Task
**Task ID**: validate-dependencies  
**Priority**: HIGH - Execute at feature completion and milestones  
**Location**: framework/tasks/validation/validate-dependencies.md  
**Category**: validation  
**Complexity**: complex  

## 🎯 PURPOSE
Systematically validate all dependencies across the system are current, correct, and properly linked when completing features or milestones. This ensures system integrity and prevents broken references.

## ⚠️ CRITICAL EXECUTION NOTICE

### **THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **MANDATORY RULE LOADING** - Load all validation rules before execution
2. **SYSTEMATIC SCANNING** - Check every dependency type in order
3. **EVIDENCE COLLECTION** - Document all issues found
4. **QUALITY GATE INTEGRATION** - Block completion if critical issues exist
5. **REPORT GENERATION** - Create validation report for review

**VIOLATION INDICATOR:** Skipping dependency checks or marking features complete with broken dependencies violates quality standards.

## 📋 PREREQUISITE CHECKS
```yaml
prerequisites:
  - Feature at 90%+ completion OR milestone deadline approaching
  - Active context is current (<5 min old)
  - All recent changes committed to workspace
  - Quality gates defined for feature/milestone
```

## 🆕 BIDIRECTIONAL DEPENDENCY VALIDATION

### Execute Bidirectional Check (NEW - MANDATORY)
```yaml
action: VALIDATE_BIDIRECTIONAL
priority: CRITICAL
integration: framework/tasks/validation/validate-bidirectional-dependencies.md
process:
  - Execute bidirectional validation task
  - Check all dependency blocks exist
  - Verify upstream/downstream integrity
  - Auto-fix missing backlinks
  - Generate dependency registry
  
failure_handling:
  - Block feature completion if critical issues
  - Create fix queue for manual review
  - Generate violation report
```

## 🔍 DEPENDENCY CATEGORIES TO VALIDATE

### 1. Configuration Dependencies
```yaml
type: system_configuration
priority: CRITICAL
locations:
  - SYSTEM-STRUCTURE.md
  - system.manifest.md  
  - CLAUDE.md
  - structure/**/*.yaml
  - **/INDEX.md

validation_checks:
  - All referenced paths exist
  - Version numbers consistent
  - Index files match actual contents
  - Registry counts accurate
  - No orphaned references
```

### 2. Agent Dependencies
```yaml
type: agent_references
priority: HIGH
locations:
  - operations/agents/INDEX.md
  - operations/agents/**/*.md
  - framework/templates/agent.yaml

validation_checks:
  - Dependencies list in metadata accurate
  - Cross-agent references valid
  - Workflow references exist
  - Task references valid
  - Resource paths correct
  - Available agents in orchestrator current
```

### 3. Workflow Dependencies  
```yaml
type: workflow_references
priority: HIGH
locations:
  - operations/workflows/INDEX.md
  - operations/workflows/**/*.md
  - framework/templates/workflow.yaml

validation_checks:
  - Agent references valid
  - Task dependencies exist
  - Quality gate references correct
  - Step sequences valid
  - Template uses correct
  - Engineering rules referenced exist
```

### 4. Feature Dependencies
```yaml
type: feature_references
priority: MEDIUM
locations:
  - workspace/features/INDEX.yaml
  - workspace/features/active/*/index.yaml
  - workspace/features/active/*/*.md

validation_checks:
  - Registry entries match directories
  - Cross-feature dependencies documented
  - States current (active/completed/archived)
  - Progress percentages accurate
  - Quality gates satisfied
  - Required files present (prd, active-context, progress, quality-gates)
```

### 5. Engineering Rules Dependencies
```yaml
type: engineering_rules
priority: HIGH
locations:
  - framework/engineeringrules/INDEX.md
  - framework/engineeringrules/**/*.md

validation_checks:
  - Rules referenced in components exist
  - Category paths correct
  - Version-specific rules valid
  - Compliance requirements documented
  - No circular dependencies
```

### 6. Template Dependencies
```yaml
type: templates
priority: MEDIUM
locations:
  - framework/templates/*.yaml
  - framework/templates/features/*.yaml

validation_checks:
  - Template variables defined
  - Template paths in workflows valid
  - Required fields match implementation
  - Inheritance chains complete
  - Dependencies list accurate
```

### 7. Memory System Dependencies
```yaml
type: memory_system
priority: CRITICAL
locations:
  - workspace/memory/active-context.md
  - workspace/memory/project-foundation/*.md
  - workspace/memory/patterns/*.md

validation_checks:
  - Active context current (<5 min)
  - Memory paths in agents correct
  - Pattern extractions linked
  - Session handover complete
  - Update task references valid
```

### 8. Cross-File Link Dependencies
```yaml
type: internal_links
priority: MEDIUM
locations:
  - **/*.md

validation_checks:
  - Markdown links [text](path) valid
  - File references in comments correct
  - Relative paths accurate
  - No broken links
  - Anchors exist for internal links
```

## 🔄 EXECUTION STEPS

### Step 1: Initialize Validation
```yaml
action: INITIALIZE
tasks:
  - Load current active context
  - Identify feature/milestone scope
  - Prepare validation report template
  - Set up issue tracking
```

### Step 2: Load Validation Rules
```yaml
action: LOAD_RULES
engineering_rules:
  - framework/engineeringrules/core-foundation/file-management.md
  - framework/engineeringrules/core-foundation/memory-system.md
  - framework/engineeringrules/core-foundation/quality-assurance.md
  - framework/engineeringrules/core-foundation/compliance-enforcement.md
  
validation_tasks:
  - framework/tasks/validation/validate-bidirectional-dependencies.md  # NEW
```

### Step 2.5: Run Bidirectional Validation (NEW)
```yaml
action: BIDIRECTIONAL_CHECK
priority: CRITICAL
process:
  - Execute: *task validate-bidirectional-dependencies --quick
  - Check dependency blocks in all files
  - Verify upstream/downstream integrity
  - Generate violations list
  - Auto-fix if authorized
  
integration:
  - Results feed into main validation report
  - Critical issues block completion
  - Registry updated for reference
```

### Step 3: Scan Configuration Dependencies
```yaml
action: VALIDATE_CONFIG
process:
  - Read SYSTEM-STRUCTURE.md
  - Verify all paths exist
  - Check version consistency
  - Validate index accuracy
  - Document issues found
```

### Step 4: Validate Agent Dependencies
```yaml
action: VALIDATE_AGENTS
process:
  - Read operations/agents/INDEX.md
  - Check each agent's dependencies
  - Verify cross-references
  - Validate resource paths
  - Document issues found
```

### Step 5: Check Workflow Dependencies
```yaml
action: VALIDATE_WORKFLOWS
process:
  - Read operations/workflows/INDEX.md
  - Verify agent references
  - Check task dependencies
  - Validate quality gates
  - Document issues found
```

### Step 6: Verify Feature Dependencies
```yaml
action: VALIDATE_FEATURES
process:
  - Read workspace/features/INDEX.yaml
  - Check feature directories
  - Verify required files
  - Validate cross-references
  - Document issues found
```

### Step 7: Audit Engineering Rules
```yaml
action: VALIDATE_RULES
process:
  - Read framework/engineeringrules/INDEX.md
  - Check referenced rules exist
  - Verify category structure
  - Validate rule applications
  - Document issues found
```

### Step 8: Check Template Dependencies
```yaml
action: VALIDATE_TEMPLATES
process:
  - Scan framework/templates/
  - Verify variable definitions
  - Check template references
  - Validate inheritance
  - Document issues found
```

### Step 9: Validate Memory System
```yaml
action: VALIDATE_MEMORY
process:
  - Check active context currency
  - Verify memory paths
  - Validate pattern links
  - Check update task
  - Document issues found
```

### Step 10: Scan Cross-File Links
```yaml
action: VALIDATE_LINKS
process:
  - Scan all markdown files
  - Check internal links
  - Verify file references
  - Validate relative paths
  - Document issues found
```

### Step 11: Generate Report
```yaml
action: GENERATE_REPORT
output_location: workspace/data-output/validation-reports/validation-report-{timestamp}.md
template: |
  # Dependency Validation Report
  **Date**: {{timestamp}}
  **Feature/Milestone**: {{name}}
  **Validator**: {{agent}}
  
  ## Summary
  - Total Dependencies Checked: {{total}}
  - Valid Dependencies: {{valid}}
  - Issues Found: {{issues}}
  - Critical Issues: {{critical}}
  - Bidirectional Health: {{bidirectional_score}}%  # NEW
  
  ## Bidirectional Validation (NEW)
  - Files with dependency blocks: {{blocks_count}}/{{total_files}}
  - Bidirectional valid: {{bidirectional_valid}}
  - Missing backlinks: {{missing_backlinks}}
  - Broken references: {{broken_refs}}
  
  ## Issues by Category
  {{#each categories}}
  ### {{name}}
  - Checked: {{checked}}
  - Valid: {{valid}}
  - Issues: {{issues}}
  {{#if issues}}
  #### Details:
  {{#each issue_list}}
  - {{severity}}: {{description}} at {{location}}
  {{/each}}
  {{/if}}
  {{/each}}
  
  ## Critical Issues Requiring Resolution
  {{#each critical_issues}}
  1. {{description}}
     - Location: {{location}}
     - Impact: {{impact}}
     - Resolution: {{suggested_fix}}
  {{/each}}
  
  ## Quality Gate Decision
  **Status**: {{status}} # PASS | CONCERNS | FAIL | WAIVED
  **Rationale**: {{rationale}}
  
  ## Sign-off
  - [ ] All critical dependencies validated
  - [ ] Non-critical issues documented
  - [ ] Feature/Milestone ready for {{action}}
```

### Step 12: Apply Quality Gate
```yaml
action: QUALITY_GATE
decision_framework:
  PASS:
    - All dependencies valid
    - No broken references
    - All files present
    
  CONCERNS:
    - Minor issues found
    - Non-critical references missing
    - Documentation gaps
    
  FAIL:
    - Critical dependencies broken
    - Required files missing
    - Circular dependencies detected
    
  WAIVED:
    - Issues documented
    - Mitigation plan in place
    - User explicitly accepts
```

## 📊 METRICS AND THRESHOLDS

### Dependency Health Score
```yaml
scoring:
  100%: All dependencies valid and current
  90-99%: Minor issues, non-blocking
  80-89%: Some issues, needs attention
  <80%: Critical issues, blocks completion

calculation:
  score = (valid_dependencies / total_dependencies) * 100
  
severity_weights:
  CRITICAL: -10% per issue
  HIGH: -5% per issue
  MEDIUM: -2% per issue
  LOW: -1% per issue
```

### Common Issues Patterns
```yaml
patterns:
  missing_dependency_block:  # NEW
    description: File lacks dependency block
    detection: No <!-- dependencies --> block found
    resolution: Add block with extracted dependencies
    
  unidirectional_reference:  # NEW
    description: A references B but B doesn't reference A
    detection: Missing backlink in downstream file
    resolution: Add backlink to maintain bidirectional integrity
    
  stale_references:
    description: Files moved but references not updated
    detection: Path exists check fails
    resolution: Update all references to new path
    
  version_mismatch:
    description: Different versions referenced
    detection: Version comparison fails
    resolution: Standardize to latest version
    
  missing_dependencies:
    description: Required files not present
    detection: File existence check fails
    resolution: Create missing files or update requirements
    
  circular_dependencies:
    description: A depends on B, B depends on A
    detection: Dependency graph has cycles
    resolution: Refactor to break circular reference
    
  orphaned_dependencies:
    description: Referenced but never used
    detection: No incoming references found
    resolution: Remove or document purpose
```

## 🔗 INTEGRATION POINTS

### Trigger Points
```yaml
triggers:
  - Feature reaches 90% completion
  - Milestone deadline approaching
  - Before marking feature complete
  - After major refactoring
  - Before system migration
  - During quality gate validation
  - Before archiving features
```

### Integration with Other Tasks
```yaml
related_tasks:
  - validate-bidirectional-dependencies.md: Bidirectional validation (CRITICAL)
  - update-active-context.md: Updates before validation
  - quality-gate.md: Uses validation results
  - feature-completion.md: Requires validation pass
  - milestone-review.md: Includes validation report
  - update-all-indices.md: Updates dependency blocks
  - update-indices-with-content.md: Content-aware dependency extraction
```

## 🛠️ AUTOMATION OPPORTUNITIES

### Scriptable Checks
```yaml
automatable:
  - File existence validation
  - Link checking in markdown
  - Version consistency checks
  - Registry synchronization
  - Dependency graph generation
  - Cross-reference validation
  - Path verification
  - Template variable checking
```

### Manual Review Required
```yaml
manual_only:
  - Semantic correctness
  - Business logic validation
  - Architectural decisions
  - Quality judgments
  - Risk assessment
  - Waiver decisions
```

## ⚡ QUICK EXECUTION COMMAND

```bash
# Quick validation for current feature
FEATURE=$(pwd | grep -oP 'features/active/\K[^/]+')
echo "Validating dependencies for: $FEATURE"

# Run validation checks
for category in config agents workflows features rules templates memory links; do
  echo "Checking $category dependencies..."
  # Validation logic here
done

# Generate report
echo "Generating validation report..."
```

## 📝 CHECKLIST FOR MANUAL EXECUTION

When manually executing this task:

- [ ] Load this task file completely
- [ ] Read current active context
- [ ] Identify validation scope
- [ ] Load engineering rules
- [ ] Check each dependency category
- [ ] Document all issues found
- [ ] Calculate health score
- [ ] Generate validation report
- [ ] Apply quality gate decision
- [ ] Update feature/milestone status
- [ ] Save report to workspace/data-output/validation-reports/
- [ ] Update active context

## 🚨 CRITICAL REMINDERS

1. **NEVER SKIP** validation for features marked complete
2. **ALWAYS DOCUMENT** issues found, even if waived
3. **BLOCK COMPLETION** if critical dependencies broken
4. **UPDATE IMMEDIATELY** when dependencies change
5. **PRESERVE EVIDENCE** for quality audits

---
**REMEMBER**: Dependency validation ensures system integrity. Never compromise on critical dependencies!