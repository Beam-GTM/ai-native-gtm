<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.325224Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.355441Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:15:00Z -->
<!-- migration_path: auto-generated -->

# Validate Version Headers Task
**Task ID**: validate-version-headers  
**Priority**: HIGH - Execute after version deployment and during system-sync  
**Location**: framework/tasks/validation/validate-version-headers.md  
**Category**: validation  
**Complexity**: standard  

## 🎯 PURPOSE
Systematically validate all version headers across the system are present, correctly formatted, and consistent with system versioning standards. Ensures version integrity and compliance with file-level versioning requirements.

## ⚠️ CRITICAL EXECUTION NOTICE

### **THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:
1. **SYSTEMATIC SCANNING** - Check every file type for version headers
2. **FORMAT VALIDATION** - Verify header structure and required fields
3. **CONSISTENCY CHECKING** - Ensure versions align with component standards
4. **COMPLIANCE REPORTING** - Generate comprehensive validation report
5. **AUTO-CORRECTION** - Fix minor issues automatically where possible

## 📋 VERSION HEADER REQUIREMENTS

### Standard Header Format (Markdown)
```markdown
```

### Standard Header Format (YAML)
```yaml
---
version: [component_version]
system_version: [system_version]
last_modified: [ISO_timestamp]
migration_path: [migration_path]
---
```

## 🔍 VALIDATION CATEGORIES

### 1. Critical System Files
```yaml
type: critical_system
priority: CRITICAL
files:
  - operations/agents/core/orchestrator.md
  - framework/tasks/system/system-sync.md
  - framework/tasks/validation/validate-dependencies.md
  - operations/INDEX.md
  - SYSTEM-STRUCTURE.md
  - framework/CRITICAL-DIRECTIVES.md

validation_checks:
  - Version header present
  - All required fields complete
  - Version matches system version (3.2.0)
  - Timestamp format valid (ISO 8601)
  - Migration path specified
```

### 2. Agent Files
```yaml
type: agent_files
priority: HIGH
pattern: "operations/agents/**/*.md"
expected_version: "3.2.0"

validation_checks:
  - Header format correct
  - Version consistent across all agents
  - System version matches current
  - Last modified timestamp reasonable
  - No duplicate version entries
```

### 3. Task Files
```yaml
type: task_files
priority: HIGH
pattern: "framework/tasks/**/*.md"
expected_version: "2.0.0"

validation_checks:
  - Version header present
  - Task version matches tier system
  - System version alignment
  - Modification tracking accurate
```

### 4. Template Files
```yaml
type: template_files
priority: MEDIUM
pattern: "framework/templates/**/*.yaml"
expected_version: "2.1.0"

validation_checks:
  - YAML header format
  - Template version consistency
  - Archive versions documented
  - Migration paths defined
```

### 5. Workflow Files
```yaml
type: workflow_files
priority: MEDIUM
pattern: "operations/workflows/**/*.md"
expected_version: "1.5.0"

validation_checks:
  - Version header compliance
  - Workflow version alignment
  - Cross-workflow consistency
```

## 🔄 EXECUTION STEPS

### Step 1: Initialize Validation
```yaml
action: INITIALIZE
tasks:
  - Load version configuration from framework/versioning/VERSION.yaml
  - Prepare validation report template
  - Set up issue tracking
  - Define validation thresholds
```

### Step 2: Scan Critical System Files
```yaml
action: VALIDATE_CRITICAL
process:
  - Check each critical file for version header
  - Validate header format and completeness
  - Verify version consistency
  - Document any issues
priority: BLOCKING
```

### Step 3: Validate Agent Files
```yaml
action: VALIDATE_AGENTS
process:
  - Scan all agent files for headers
  - Check version consistency (3.2.0)
  - Validate timestamp formats
  - Cross-reference with agent INDEX
```

### Step 4: Check Task Files
```yaml
action: VALIDATE_TASKS
process:
  - Scan framework/tasks/ recursively
  - Verify task version alignment (2.0.0)
  - Check tier-specific versions
  - Validate migration paths
```

### Step 5: Audit Template Files
```yaml
action: VALIDATE_TEMPLATES
process:
  - Check YAML header format
  - Verify template versions (2.1.0)
  - Validate archive references
  - Cross-check with template registry
```

### Step 6: Verify Workflow Files
```yaml
action: VALIDATE_WORKFLOWS
process:
  - Scan workflow files
  - Check version alignment (1.5.0)
  - Validate cross-references
  - Document inconsistencies
```

### Step 7: Auto-Correction Pass
```yaml
action: AUTO_CORRECT
scope: minor_issues
corrections:
  - Fix malformed timestamps
  - Standardize version formats
  - Add missing migration paths
  - Update system versions
backup: true
```

### Step 8: Generate Validation Report
```yaml
action: GENERATE_REPORT
output_location: workspace/data-output/validation-reports/version-validation-{timestamp}.md
template: |
  # Version Header Validation Report
  **Date**: {{timestamp}}
  **System Version**: {{system_version}}
  **Validator**: version-validation-task
  
  ## Summary
  - Total Files Scanned: {{total_scanned}}
  - Files with Headers: {{files_with_headers}}
  - Valid Headers: {{valid_headers}}
  - Issues Found: {{total_issues}}
  - Auto-Corrections: {{corrections_made}}
  - Coverage: {{coverage_percent}}%
  
  ## Validation Results by Category
  {{#each categories}}
  ### {{name}}
  - Files Scanned: {{scanned}}
  - Valid Headers: {{valid}}
  - Missing Headers: {{missing}}
  - Format Issues: {{format_issues}}
  - Version Mismatches: {{version_mismatches}}
  {{/each}}
  
  ## Critical Issues
  {{#each critical_issues}}
  1. **{{file_path}}**
     - Issue: {{issue_type}}
     - Description: {{description}}
     - Impact: {{impact_level}}
     - Resolution: {{suggested_fix}}
  {{/each}}
  
  ## Version Consistency Check
  - Agent Files: {{agent_consistency}}%
  - Task Files: {{task_consistency}}%
  - Template Files: {{template_consistency}}%
  - Workflow Files: {{workflow_consistency}}%
  
  ## Quality Gate Decision
  **Status**: {{status}} # PASS | CONCERNS | FAIL
  **Coverage Threshold**: 95% (Current: {{coverage_percent}}%)
  **Rationale**: {{rationale}}
  
  ## Auto-Corrections Applied
  {{#each corrections}}
  - {{file_path}}: {{correction_type}} - {{description}}
  {{/each}}
  
  ## Recommended Actions
  {{#each recommendations}}
  1. {{action}} - {{priority}} - {{timeline}}
  {{/each}}
```

## 📊 VALIDATION METRICS

### Coverage Thresholds
```yaml
thresholds:
  critical_files: 100%  # Must have headers
  agent_files: 95%      # High priority
  task_files: 90%       # Important
  template_files: 85%   # Standard
  other_files: 70%      # Baseline

quality_gates:
  PASS: >=95% overall coverage, no critical issues
  CONCERNS: 85-94% coverage, minor issues present
  FAIL: <85% coverage, critical files missing headers
```

### Validation Rules
```yaml
format_validation:
  required_fields:
    - version
    - system_version
    - last_modified
    - migration_path
  
  timestamp_format: "YYYY-MM-DDTHH:MM:SSZ"
  version_format: "MAJOR.MINOR.PATCH"
  migration_path_options: ["auto-generated", "manual", "migration-script"]

consistency_checks:
  agent_version_match: all agents same version
  task_tier_alignment: versions match tier system
  template_registry_sync: versions match registry
  system_version_current: all files reference current system
```

## 🛠️ AUTO-CORRECTION CAPABILITIES

### Minor Corrections (Automatic)
```yaml
auto_corrections:
  timestamp_normalization:
    - Convert to ISO 8601 format
    - Fix timezone indicators
    - Standardize precision
  
  version_formatting:
    - Add missing patch versions (.0)
    - Standardize version strings
    - Fix semantic version format
  
  header_completion:
    - Add missing migration_path fields
    - Update system_version references
    - Complete partial headers
```

### Manual Review Required
```yaml
manual_review:
  version_conflicts:
    - Conflicting versions in same component
    - Major version mismatches
    - Custom version schemes
  
  missing_headers:
    - Critical system files
    - Files with complex formatting
    - Legacy files requiring migration
```

## 🔗 INTEGRATION WITH SYSTEM-SYNC

### System-Sync Integration
```yaml
integration_point: framework/tasks/system/system-sync.md
phase: phase_2_validation
execution_order: after_dependency_validation

trigger_conditions:
  - During regular system sync
  - After version header deployment
  - Before system version increment
  - During quality gate validation
```

### Command Integration
```yaml
orchestrator_commands:
  - validate-versions: Quick version validation
  - version-check: Full validation with report
  - fix-versions: Auto-correction mode
  - version-coverage: Coverage analysis only
```

## ⚡ QUICK EXECUTION COMMANDS

### Validation Check
```bash
# Quick validation
python framework/scripts/versioning/validate-headers.py --quick

# Full validation with report
python framework/scripts/versioning/validate-headers.py --full-report

# Auto-correction mode
python framework/scripts/versioning/validate-headers.py --auto-fix
```

### Manual Validation
```bash
# Check specific file types
grep -r "<!-- version:" operations/agents/
grep -r "version:" framework/templates/ | grep "^---"

# Count coverage
find . -name "*.md" | xargs grep -l "<!-- version:" | wc -l
find . -name "*.yaml" | xargs grep -l "^version:" | wc -l
```

## 📝 EXECUTION CHECKLIST

When manually executing this task:

- [ ] Load version configuration
- [ ] Scan all file categories
- [ ] Validate header formats
- [ ] Check version consistency
- [ ] Document all issues
- [ ] Apply auto-corrections
- [ ] Generate validation report
- [ ] Apply quality gate decision
- [ ] Update validation metadata
- [ ] Save report to data-output/

## 🚨 CRITICAL SUCCESS CRITERIA

1. **100% coverage** for critical system files
2. **95% overall coverage** across all file types
3. **Version consistency** within component categories
4. **Format compliance** with standard headers
5. **Auto-correction success** for minor issues

## 🔄 AUTOMATION INTEGRATION

### Scheduled Validation
```yaml
automation:
  daily_check: Quick validation during system sync
  weekly_audit: Full validation with detailed report
  pre_release: Comprehensive validation before version increment
  post_deployment: Validation after version header updates
```

---
**REMEMBER**: Version header validation ensures system integrity and compliance. Never skip validation after version-related changes!