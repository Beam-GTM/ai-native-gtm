<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.300704Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.314307Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

<!-- dependencies
upstream:
  # AUTO-DETECTED Executable By (from task category and session integration):
  - operations/agents/core/orchestrator.md  # Pattern: 'Execute validate-bidirectional-dependencies'
  - operations/agents/core/quality-assurance.md  # Inferred: validation category
  
  # AUTO-DETECTED Called By (from content analysis):
  - framework/tasks/system/system-sync.md  # Pattern: 'validate-bidirectional-dependencies.md'
  
  # AUTO-DETECTED Engineering Rules Applied:
  - framework/engineeringrules/quality-rules.md  # Applied: validation-standards
  - framework/engineeringrules/system-design-rules.md  # Applied: dependency-integrity
  
downstream:
  # AUTO-DETECTED Dependencies (tasks/workflows that depend on this validation):
  # Search pattern: 'validate-bidirectional|bidirectional-validation|dependency-validation'
  # NOTE: All system processes depend on dependency integrity
  
validated: 2025-01-27T16:20:00Z
health: 95%  # 95% - critical validation task with clear dependencies
generator: framework/templates/task.yaml
-->

# Validate Bidirectional Dependencies Task
**Task ID**: validate-bidirectional-dependencies  
**Priority**: CRITICAL - Execute in EVERY session  
**Location**: framework/tasks/validation/validate-bidirectional-dependencies.md  
**Category**: validation  
**Complexity**: complex  
**Integration**: MANDATORY for all sessions

## 🎯 PURPOSE
Ensure EVERY dependency relationship is bidirectional and validated. If A depends on B, then B MUST know that A depends on it. This prevents silent failures from broken references and maintains system integrity.

## ⚠️ CRITICAL SESSION INTEGRATION

### **EXECUTE THIS TASK IN EVERY SESSION**

```yaml
session_integration:
  when_to_run:
    - At session start (after loading context)
    - Before any feature work
    - After file modifications
    - Before session closure
    - During system-sync
    
  quick_check_command: |
    # Add to EVERY session startup
    *task validate-bidirectional-dependencies --quick
```

## 📋 DUAL VALIDATION APPROACH

### Approach 1: Distributed Dependencies (In Each File)
```yaml
# Every .md file MUST have this block
<!-- dependencies
upstream:
  - framework/workflows/implement-feature.md  # Files I depend on
  - operations/workflows/development.md
downstream:
  - operations/agents/developer.md         # Files that depend on me
  - framework/tasks/system/system-sync.md
validated: 2025-08-26T12:00:00Z
validator: validate-bidirectional-dependencies
-->
```

### Approach 2: Central Registry (Generated for Verification)
```yaml
# Auto-generated: workspace/data-output/dependency-registry.yaml
dependency_registry:
  operations/agents/developer.md:
    upstream: [...]
    downstream: [...]
    last_validated: timestamp
    issues: []
```

## 🔍 DEPENDENCY BLOCK FORMAT

### Standard Block Template
```markdown
<!-- dependencies
upstream:
  # Files/resources this file depends on
  - path/to/dependency1.md
  - path/to/dependency2.yaml
  
downstream:
  # Files that depend on this file
  - path/to/consumer1.md
  - path/to/consumer2.md
  
cross_references:
  # Related but not dependent
  - path/to/related.md
  
validated: 2025-08-26T12:00:00Z
health: 100%
-->
```

### Entity-Specific Templates

#### For Agents
```markdown
<!-- dependencies
upstream:
  tasks_used:
    - framework/workflows/implement-feature.md
    - framework/tasks/validation/validate-dependencies.md
  workflows_integrated:
    - framework/workflows/development.md
  templates_required:
    - framework/templates/agent.yaml
    
downstream:
  workflows_using_me:
    - operations/workflows/development.md
  tasks_calling_me:
    - framework/tasks/system/system-sync.md
    
validated: timestamp
-->
```

#### For Workflows
```markdown
<!-- dependencies
upstream:
  agents_required:
    - operations/agents/developer.md
    - operations/agents/quality-assurance.md
  tasks_executed:
    - framework/tasks/validation/validate-dependencies.md
  templates_used:
    - framework/templates/workflow.yaml
    
downstream:
  orchestrator_references:
    - operations/agents/core/orchestrator.md
  features_using:
    - workspace/features/active/*/prd.md
    
validated: timestamp
-->
```

#### For Tasks
```markdown
<!-- dependencies
upstream:
  agents_executable_by:
    - operations/agents/orchestrator.md
  workflows_calling:
    - framework/workflows/development.md
  engineering_rules:
    - framework/engineeringrules/core-foundation/file-management.md
    
downstream:
  workflows_using:
    - operations/workflows/system-maintenance.md
  agents_implementing:
    - operations/agents/developer.md
    
validated: timestamp
-->
```

## 🔄 EXECUTION STEPS

### Step 1: Quick Session Check (EVERY SESSION)
```yaml
action: QUICK_CHECK
priority: CRITICAL
when: Session startup
process:
  - Check if dependency blocks exist in recently modified files
  - Verify bidirectional integrity for active feature files
  - Report any broken references
  - Generate quick health score
time_limit: 10 seconds
```

### Step 2: Extract Dependencies from Files
```yaml
action: EXTRACT_DEPENDENCIES
process:
  for each md_file:
    - Extract dependency block (between <!-- dependencies and -->)
    - Parse YAML content
    - Extract upstream/downstream lists
    - Store in memory map
    
patterns:
  dependency_block: "<!-- dependencies\\n(.*?)-->"
  yaml_content: Parse as YAML
  fallback: Extract from content patterns if no block exists
```

### Step 3: Validate Bidirectional Integrity
```yaml
action: VALIDATE_BIDIRECTIONAL
rules:
  bidirectional_check:
    for each file A:
      for each upstream dependency B:
        - Verify A exists in B's downstream list
        - If missing, add to violations
        
      for each downstream reference C:
        - Verify A exists in C's upstream list
        - If missing, add to violations
        
severity:
  missing_backlink: ERROR
  broken_reference: CRITICAL
  stale_timestamp: WARNING
```

### Step 4: Auto-Fix Missing Dependencies
```yaml
action: AUTO_FIX
strategy:
  missing_dependency_block:
    - Create block from detected references
    - Add at top of file after header
    
  missing_backlink:
    - Add reference to target file's downstream
    - Update validated timestamp
    
  broken_reference:
    - Comment out with /* BROKEN */
    - Add to fix queue
    
confirmation_required: true
backup_before_fix: true
```

### Step 5: Generate Central Registry
```yaml
action: GENERATE_REGISTRY
output: workspace/data-output/validation-reports/dependency-registry.yaml
format:
  registry:
    metadata:
      generated: timestamp
      total_files: count
      health_score: percentage
      
    dependencies:
      {file_path}:
        upstream: [list]
        downstream: [list]
        issues: [list]
        validated: timestamp
        
    violations:
      missing_blocks: [files without dependency blocks]
      broken_references: [non-existent files]
      missing_backlinks: [unidirectional references]
      circular_dependencies: [A->B->C->A chains]
```

### Step 6: Update Dependency Blocks
```yaml
action: UPDATE_BLOCKS
process:
  for each file with issues:
    - Read current block
    - Fix identified issues
    - Update validated timestamp
    - Write updated block
    
format:
  - Preserve existing structure
  - Add missing entries
  - Update timestamp
  - Recalculate health score
```

## 📊 VALIDATION RULES

### Critical Rules (Block Completion)
```yaml
critical_validations:
  dependency_block_exists:
    rule: "Every .md file MUST have a dependency block"
    exception: "README.md files"
    auto_fix: "Create block from content analysis"
    
  bidirectional_integrity:
    rule: "If A references B, B must reference A"
    severity: ERROR
    auto_fix: "Add missing backlink"
    
  reference_exists:
    rule: "Every referenced file must exist"
    severity: CRITICAL
    auto_fix: "Remove or fix broken reference"
```

### Health Score Calculation
```yaml
health_scoring:
  perfect: 100%
  calculation:
    - Start at 100%
    - Missing block: -20%
    - Each broken reference: -10%
    - Each missing backlink: -5%
    - Stale validation (>7 days): -5%
    - Circular dependency: -15%
    
  thresholds:
    healthy: ">= 90%"
    concerning: "70-89%"
    critical: "< 70%"
```

## 🚀 SESSION INTEGRATION COMMANDS

### Add to Session Startup
```bash
# Quick validation at session start
echo "=== Validating Bidirectional Dependencies ==="
*task validate-bidirectional-dependencies --quick --active-only

# If issues found
if [ $? -ne 0 ]; then
  echo "⚠️ Dependency issues detected. Run full validation?"
  *task validate-bidirectional-dependencies --full --auto-fix
fi
```

### Add to Feature Work
```bash
# Before starting feature work
*task validate-bidirectional-dependencies --feature {feature-name}

# After modifying files
*task validate-bidirectional-dependencies --changed-files

# Before marking complete
*task validate-bidirectional-dependencies --comprehensive
```

### Add to System Maintenance
```bash
# Weekly full scan
*task validate-bidirectional-dependencies --full --generate-report

# After structural changes
*task validate-bidirectional-dependencies --rebuild-registry

# During system-sync
*task validate-bidirectional-dependencies --integrate-sync
```

## 📈 PERFORMANCE OPTIMIZATION

### Incremental Validation
```yaml
incremental_mode:
  track_changes:
    - Monitor file modifications
    - Validate only changed files and their connections
    - Update registry incrementally
    
  cache_strategy:
    - Cache dependency map in memory
    - Persist between operations
    - Invalidate on file changes
    
  time_targets:
    quick_check: "< 5 seconds"
    incremental: "< 10 seconds"
    full_scan: "< 30 seconds"
```

## 🔧 INTEGRATION WITH EXISTING TASKS

### Update validate-dependencies.md
```yaml
enhancement:
  add_step: "Step 2.5: Check Bidirectional Dependencies"
  integration: |
    - Call validate-bidirectional-dependencies --quick
    - Include results in validation report
    - Block on critical bidirectional issues
```

### Update update-all-indices.md
```yaml
enhancement:
  add_step: "Step 3.11: Extract and Update Dependencies"
  integration: |
    - Extract dependency blocks while reading files
    - Update blocks with current information
    - Generate dependency registry
    - Report bidirectional violations
```

### Update system-sync.md
```yaml
enhancement:
  add_phase: "Phase 4: Bidirectional Validation"
  integration: |
    - Run full bidirectional validation
    - Auto-fix missing backlinks
    - Update all dependency blocks
    - Generate health report
```

## 📝 REPORTING

### Session Report (Quick)
```markdown
=== Bidirectional Dependency Check ===
Time: 2025-08-26T12:00:00Z
Mode: Quick Check
Files Checked: 15
Health Score: 85%

Issues Found: 3
- Missing backlink: task/implement.md -> agent/developer.md
- Broken reference: workflow/old.md (file not found)
- Missing block: features/active/new/prd.md

Run full validation? *task validate-bidirectional-dependencies --full
```

### Comprehensive Report
```markdown
# Bidirectional Dependency Validation Report
Generated: timestamp
Files Analyzed: 127
Registry Updated: Yes

## Health Score: 92%

## Summary
- Files with blocks: 120/127 (94%)
- Bidirectional valid: 115/120 (96%)
- Broken references: 5
- Missing backlinks: 12
- Circular dependencies: 0

## Critical Issues
[Detailed issue list with fixes]

## Auto-Fixed
[List of automatic corrections]

## Manual Review Required
[Issues needing human decision]
```

## ⚡ QUICK REFERENCE

### Essential Commands
```bash
# Session start (ALWAYS RUN)
*task validate-bidirectional-dependencies --quick

# After changes
*task validate-bidirectional-dependencies --changed

# Full validation
*task validate-bidirectional-dependencies --full

# Auto-fix issues
*task validate-bidirectional-dependencies --auto-fix

# Generate registry
*task validate-bidirectional-dependencies --generate-registry
```

## 🚨 CRITICAL REMINDERS

1. **EVERY SESSION** must run quick validation at startup
2. **EVERY FILE** must have a dependency block
3. **EVERY REFERENCE** must be bidirectional
4. **NEVER SKIP** validation before marking features complete
5. **ALWAYS BACKUP** before auto-fixing

---
**REMEMBER**: Bidirectional dependencies prevent silent failures. This is NOT optional!