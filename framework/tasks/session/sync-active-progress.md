<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.982931Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.279924Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Sync Active Progress Task

## Purpose
Synchronizes progress percentages from individual feature progress.md files to the central workspace/features/INDEX.md registry, preventing progress drift between local feature tracking and system-wide status.

## Context
**Problem**: Features update their local progress.md files during development, but these updates don't automatically sync to the central INDEX.md registry, causing system-wide progress reporting to become stale.

**Solution**: During close-chat workflow, scan all active feature progress files and update the INDEX.md with current progress values, then recalculate averages.

## Dependencies
- workspace/features/active/*/progress.md (source files)
- workspace/features/INDEX.md (target file)

## Input Requirements
- At least one active feature with progress.md file
- Write access to workspace/features/INDEX.md

## Output
- Updated progress values in INDEX.md
- Recalculated average_progress statistic
- Log of progress changes

## Execution Steps

### Step 1: Scan Active Features
```
Action: Scan workspace/features/active/ for progress.md files
Pattern: workspace/features/active/*/progress.md
Extract: Feature directory names for matching
```

### Step 2: Extract Progress Values
```
For each progress.md file found:
  Action: Extract current progress percentage
  Pattern: "Overall Progress: (\d+)%" or "## Overall Progress: (\d+)%"
  Fallback: Look for "progress: (\d+)%" in YAML frontmatter
  Store: feature_name → progress_percentage mapping
```

### Step 3: Load INDEX.md
```
Action: Read current workspace/features/INDEX.md
Parse: YAML structure for feature_registry.active entries
Prepare: For selective updates
```

### Step 4: Update Progress Values
```
For each feature with extracted progress:
  Action: Find matching entry in INDEX.md by feature name/path
  Match: feature directory name to feature registry entry
  Update: progress field with new value
  Update: description if needed to reflect current phase
  Log: Old progress → New progress for reporting
```

### Step 5: Recalculate Statistics
```
Action: Recalculate quick_stats.average_progress
Formula: Sum(all active feature progress) / Count(active features)
Update: quick_stats.average_progress field
Verify: Total counts still accurate
```

### Step 6: Write Updated INDEX.md
```
Action: Write updated INDEX.md with new progress values
Preserve: All other YAML structure and metadata
Maintain: File formatting and comments
Backup: Create .bak file before overwriting (optional)
```

### Step 7: Generate Progress Report
```
Action: Create summary of progress changes
Format:
  "Progress Sync Report:
   - Features Updated: X
   - Progress Changes:
     * feature-1: 30% → 45%
     * feature-2: 60% → 75%
   - New Average: X%"
Output: Console and/or log file
```

### Step 8: Validation
```
Action: Verify updates were successful
Check: INDEX.md contains new progress values
Check: YAML structure remains valid
Check: Average calculation is correct
Report: Success/failure status
```

## Error Handling

### Missing Progress Files
- Skip features without progress.md
- Log warning but continue processing
- Don't fail entire task

### Parse Errors
- Try multiple progress extraction patterns
- Default to 0% if no progress found
- Log parse failures for debugging

### INDEX.md Write Errors
- Create backup before modifications
- Restore from backup on failure
- Report specific error details

### Validation Failures
- Report which validations failed
- Allow partial success if some features updated
- Provide manual correction guidance

## Quality Gates

### Input Validation
- ✅ At least one active feature directory exists
- ✅ INDEX.md is readable and valid YAML
- ✅ Write permissions available

### Processing Validation
- ✅ At least one progress value extracted successfully
- ✅ Feature name matching works correctly
- ✅ Progress values are realistic (0-100%)

### Output Validation
- ✅ INDEX.md remains valid YAML after updates
- ✅ All expected features still present in registry
- ✅ Average calculation is mathematically correct
- ✅ No data corruption in INDEX.md

## Success Criteria
- All active features' progress synchronized between local files and INDEX.md
- Average progress statistic accurately reflects current state
- No data loss or corruption in INDEX.md
- Clear report of what was updated

## Integration Points
- **Close-Chat Workflow**: Called from ENGINE 4 (feature_lifecycle)
- **Feature Progress Files**: Reads from workspace/features/active/*/progress.md
- **System INDEX**: Updates workspace/features/INDEX.md
- **Reporting**: Contributes to session closure reports

## Performance Notes
- Lightweight operation: reads ~4 files, writes 1 file
- Parallel-safe: only reads feature files, writes single INDEX
- Fast execution: typically <5 seconds
- Memory efficient: processes features one at a time

## Usage Examples

### Manual Execution
```
*task sync-active-progress
```

### From Close-Chat Workflow
```
Automatically executed during ENGINE 4: feature_lifecycle
Priority: medium (after critical archival tasks)
```

### Expected Output
```
✅ Progress Sync Complete
- learning-analysis-pipeline: 10% → 45%
- agent-template-orchestrator-enhancement: 40% → 40% (no change)
- memory-learnings-consolidation: 90% → 90% (no change)
- nexus-template: 40% → 40% (no change)
Average Progress: 54% (updated from 45%)
```

## Notes
- This task addresses Learning #28: Progress Update Dissociation Pattern
- Prevents the common issue of stale progress in system-wide reporting
- Maintains single source of truth for progress tracking
- Essential for accurate system health monitoring and user experience

---
*Task created to resolve progress drift between feature files and system INDEX*