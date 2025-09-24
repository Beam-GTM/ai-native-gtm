<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.214628Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.304567Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Update All Indices and Context Files
**Task ID**: update-all-indices  
**Category**: system-maintenance  
**Priority**: HIGH  
**Execution**: Parallel batch processing  

## Purpose
Comprehensive system-wide update of ALL index, context, and registry files to ensure navigation accuracy, context currency, and system coherence.

## When to Use
- After major structural changes
- During system maintenance windows
- Before release preparations
- When indices become stale
- After feature completions/archival
- Weekly maintenance schedule

## Prerequisites
- System backup completed
- No active file operations
- Write permissions verified

## Task Execution Steps

### Step 1: Discovery Phase
Execute parallel discovery of all index and context files:

```bash
# Find all INDEX files
find . -name "INDEX.md" -o -name "INDEX.yaml"

# Find all CONTEXT files  
find . -name "CONTEXT.md" -o -name "active-context.md"

# Find all registry files
find . -name "MANIFEST.md" -o -name "FEATURES.md" -o -name "SYSTEM-STRUCTURE.md"
```

### Step 2: Backup Phase
Create timestamped backups of all files to be updated:

```bash
# Create backup directory
mkdir -p workspace/backups/indices-$(date +%Y%m%d-%H%M%S)

# Backup all index/context files
cp --parents */INDEX.md workspace/backups/indices-*/
cp --parents */CONTEXT.md workspace/backups/indices-*/
```

### Step 2.5: Extract Dependencies (NEW - CRITICAL)
Extract and validate dependency blocks from all files:

```yaml
action: EXTRACT_DEPENDENCIES
priority: CRITICAL
process:
  for each .md file:
    - Check for <!-- dependencies --> block
    - If missing, create from content analysis
    - Extract upstream/downstream references
    - Validate bidirectional integrity
    - Update blocks with current state
    
example_extraction:
  from_agent_file:
    - Find: "tasks: [...]" → Add to upstream
    - Find: "workflows: [...]" → Add to upstream  
    - Find references to this agent → Add to downstream
    
  from_workflow_file:
    - Find: "agents: [...]" → Add to upstream
    - Find: "tasks: [...]" → Add to upstream
    - Find references to this workflow → Add to downstream
```

### Step 3: Update Operations

#### 3.1 Update Agent INDEX.md
**File**: operations/agents/INDEX.md
**Updates**:
- Count agents in each category (core, specialists, coordinators, experimental)
- Update total agent count
- Refresh category listings
- Update timestamps

```yaml
update_logic:
  - Count files in agents/core/*.md (exclude CONTEXT.md)
  - Count files in agents/specialists/*.md
  - Count files in agents/coordinators/*.md  
  - Count files in agents/experimental/*.md
  - Update totals and listings
```

#### 3.2 Update Workflow INDEX.md
**File**: operations/workflows/INDEX.md  
**Updates**:
- Count workflow files
- List all workflows with descriptions
- Update registry entries
- Check cascade dependencies

```yaml
update_logic:
  - Scan operations/workflows/*.md
  - Scan framework/workflows/*.md
  - Extract workflow metadata
  - Update counts and listings
```

#### 3.3 Update Task INDEX.md
**File**: operations/tasks/INDEX.md
**Updates**:
- Count tasks by category
- Update growth metrics
- List all available tasks
- Track usage patterns

```yaml
update_logic:
  - Scan operations/tasks/*/*.md
  - Group by category directories
  - Extract task metadata
  - Update statistics
```

#### 3.4 Update Engineering Rules INDEX.md
**File**: framework/engineeringrules/INDEX.md
**Updates**:
- Count rules by category (37 total)
- Verify all rule files exist
- Update category totals
- Refresh quick reference

```yaml
categories_to_check:
  - core-foundation (9 rules)
  - development (10 rules)
  - product-management (9 rules)
  - system-operations (9 rules)
```

#### 3.5 Update Feature Registries
**Files**: 
- workspace/features/INDEX.md (primary feature registry)
- workspace/features/FEATURES.md (optional secondary registry)

**Updates**:
- Scan active/* for current features
- Update progress from progress.md files
- Move completed features if marked done
- Archive stale features (30+ days inactive)
- Update statistics in YAML block within INDEX.md

```yaml
feature_states:
  - active: Currently being worked on
  - completed: Finished, awaiting archival
  - archived: Historical reference
  - patterns: Extracted reusable patterns
```

#### 3.6 Update Context Files
**Files**: All CONTEXT.md files
**Updates**:
- Update file counts in directory
- Refresh purpose statements
- Update navigation paths
- Verify cross-references

```yaml
context_locations:
  - operations/agents/core/CONTEXT.md
  - operations/agents/specialists/CONTEXT.md
  - operations/agents/coordinators/CONTEXT.md
  - operations/agents/experimental/CONTEXT.md
```

#### 3.7 Update Active Context Files
**Files**: All active-context.md files
**Updates**:
- Update timestamps to current UTC
- Refresh file access lists
- Update system state
- Increment loop counters

```yaml
active_contexts:
  - workspace/memory/active-context.md (project-level)
  - workspace/features/active/*/active-context.md (feature-level)
```

#### 3.8 Update System Structure
**File**: SYSTEM-STRUCTURE.md
**Updates**:
- Refresh directory tree
- Update file counts
- Update statistics section
- Verify all paths exist

#### 3.9 Update Operations Manifest
**File**: operations/MANIFEST.md
**Updates**:
- Update resource counts
- Refresh loading sequences
- Update dependencies
- Verify component availability

#### 3.10 Update Operations INDEX
**File**: operations/INDEX.md
**Updates**:
- Update resource counts
- Refresh growth triggers
- Update total counts

#### 3.11 Update Dependency Blocks (NEW - CRITICAL)
**Files**: All .md files with dependencies
**Updates**:
- Add/update dependency blocks
- Validate bidirectional references
- Update validated timestamps
- Calculate health scores

```yaml
dependency_updates:
  process:
    - Read existing block or create new
    - Update upstream/downstream lists
    - Verify bidirectional integrity
    - Add validated timestamp
    - Calculate health percentage
    
  format: |
    <!-- dependencies
    upstream:
      - path/to/dependency.md
    downstream:
      - path/to/consumer.md
    validated: {{timestamp}}
    health: {{percentage}}%
    -->
```

### Step 4: Validation Phase

#### 4.0 Bidirectional Dependency Validation (NEW - MANDATORY)
```yaml
bidirectional_validation:
  description: "Verify all dependencies are bidirectional"
  integration: framework/tasks/validation/validate-bidirectional-dependencies.md
  checks:
    - All files have dependency blocks
    - Upstream references are valid
    - Downstream backlinks exist
    - No circular dependencies
    - Health score >= 90%
    
  on_failure: 
    - Generate violation report
    - Auto-fix if authorized
    - Block if critical issues
```

#### 4.1 Filesystem Verification (CRITICAL - Trust but Verify)
```yaml
filesystem_audit:
  description: "Verify INDEX claims match actual filesystem"
  checks:
    - agents: ls operations/agents/*/*.md | Count vs INDEX
    - workflows: ls operations/workflows/*.md + framework/workflows/*.md | Count vs INDEX  
    - tasks: ls framework/tasks/*/*.md | Count vs INDEX
    - features_active: ls workspace/features/active/ | Count vs INDEX
    - features_completed: ls workspace/features/completed/ | Count vs INDEX
  
  validation_rule: "INDEX counts MUST match filesystem EXACTLY"
  on_mismatch: "Correct INDEX immediately, log discrepancy"
```

#### 4.2 Cross-Reference Validation
- Verify all referenced files exist
- Check for orphaned references
- Validate path integrity
- Ensure bidirectional links

#### 4.2 Format Validation
- Check markdown formatting
- Validate YAML syntax
- Ensure consistent structure
- Verify required fields

#### 4.3 Consistency Validation
- Compare counts across files
- Verify category groupings
- Check timestamp formats
- Validate statistics

### Step 5: Reporting Phase

Generate comprehensive update report:
**Output Location**: workspace/data-output/index-updates/index-update-report-{timestamp}.md

```markdown
# Index Update Report
**Execution Time**: [timestamp]
**Duration**: [seconds]

## Files Updated
- Total files scanned: [count]
- Files updated: [count]
- Files skipped: [count]
- Errors encountered: [count]

## Changes Made
[List of specific updates]

## Dependency Health (NEW)
- Files with blocks: [count]/[total]
- Bidirectional valid: [percentage]%
- Issues fixed: [count]
- Manual review needed: [count]

## Validation Results
- Cross-references: PASS/FAIL
- Format checks: PASS/FAIL
- Consistency: PASS/FAIL

## Recommendations
[Any issues found or improvements suggested]
```

## Parallel Execution Strategy

Execute updates in parallel batches for performance:

```yaml
batch_1: # Independent files
  - operations/agents/INDEX.md
  - operations/workflows/INDEX.md
  - operations/tasks/INDEX.md
  - framework/engineeringrules/INDEX.md

batch_2: # Dependent on batch_1
  - operations/INDEX.md
  - operations/MANIFEST.md
  
batch_3: # Feature-related
  - workspace/features/INDEX.md
  - workspace/features/FEATURES.md
  
batch_4: # Context files
  - All CONTEXT.md files
  - All active-context.md files
  - All dependency blocks (NEW)
  
batch_5: # System-wide
  - SYSTEM-STRUCTURE.md
```

## Error Handling

### Rollback Procedure
1. If any critical error occurs:
   - Stop all update operations
   - Restore from backup directory
   - Generate error report
   - Alert user

### Error Recovery
- File not found: Skip and log
- Permission denied: Skip and alert
- Malformed content: Backup and attempt repair
- Network issues: Retry with exponential backoff

## Performance Targets
- Discovery: <5 seconds
- Backup: <10 seconds  
- Updates: <15 seconds
- Validation: <5 seconds
- **Total**: <35 seconds

## Usage Examples

### Manual Execution
```bash
# Dry run to see what would be updated
*task update-all-indices --dry-run

# Full update with backup
*task update-all-indices --backup

# Update specific category only
*task update-all-indices --category=agents

# Force update even if recent
*task update-all-indices --force
```

### Scheduled Execution
```yaml
schedule:
  daily: 03:00 UTC  # Low activity time
  weekly: Sunday 02:00 UTC  # Full validation
  on_demand: Via orchestrator command
```

## Success Criteria
- [ ] All index files current
- [ ] All context files updated
- [ ] No broken references
- [ ] Validation passes
- [ ] Performance within targets
- [ ] Backup successful
- [ ] Report generated in workspace/data-output/index-updates/

## Dependencies
- File system read/write access
- Pattern matching tools (Glob)
- Text processing (Read/Write/Edit)
- Parallel execution capability
- Timestamp generation

## Notes
- Always backup before updates
- Run validation after updates
- Monitor for circular dependencies
- Track execution metrics for optimization
- Consider system load before execution

## Related Tasks
- framework/tasks/memory/update-project-memory.md
- framework/tasks/validation/validate-dependencies.md
- framework/tasks/validation/validate-bidirectional-dependencies.md (NEW - CRITICAL)
- framework/tasks/system/update-indices-with-content.md (Enhanced version)

## Maintenance
This task should be reviewed monthly for:
- New file types to include
- Performance optimization opportunities
- Additional validation rules
- Error handling improvements