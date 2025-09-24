# Task: Multi-Session Safe INDEX Sync

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: Never use limit parameter when reading progress.md files -->
<!-- This directive OVERRIDES token conservation - read files completely -->

**Task ID**: multi-session-index-sync  
**Category**: session-maintenance  
**Priority**: CRITICAL  
**Type**: Concurrency-safe INDEX synchronization  
**Multi-Session**: SAFE - designed for concurrent Claude sessions

## Purpose
Safely synchronize workspace/features/INDEX.md with filesystem reality while handling 3-6 concurrent Claude sessions. Uses conservative append-only approach with user validation for questionable changes.

## Multi-Session Problem Context
```yaml
challenge: "User runs 3-6 concurrent Claude sessions"
manifestation: "Features created/completed in parallel sessions"
git_behavior: "Last write wins - potential data loss"
solution: "Conservative append-only with conflict detection"
```

## Algorithm: Conservative + Smart

### Phase 1: Filesystem Discovery (DIRECTIVE #1 & #2 Compliant)
```yaml
step_1_scan:
  tool: Glob
  pattern: "workspace/features/active/*"
  purpose: "Get filesystem reality (DIRECTIVE #2: filesystem is truth)"

step_2_metadata_extraction:
  tool: Read
  files: "Each feature's progress.md" 
  limit: "NONE - DIRECTIVE #1: always read complete files"
  extract:
    - feature_name: "from directory name"
    - progress: "from 'Overall Progress: X%' pattern"
    - status: "from progress analysis"
```

### Phase 2: Safe Analysis
```yaml
step_3_comparison:
  current_index: "Read workspace/features/INDEX.md active section"
  filesystem_features: "From Phase 1 discovery"
  classification:
    SAFE_NEW: "Feature in filesystem but not INDEX - auto-append"
    QUESTIONABLE: "Feature exists but progress/status differs"
    DANGEROUS: "Feature in INDEX but missing from filesystem"

step_4_backup:
  action: "Create INDEX.md.backup.{timestamp}"
  reason: "Safety before any modifications"
```

### Phase 3: Fully Automatic Updates
```yaml
step_5_automatic_operations:
  SAFE_NEW_features:
    action: "Auto-append to INDEX.md active section"
    method: "Add to end of active list with filesystem data"
    conflicts: "IMPOSSIBLE - append-only"
    
  PROGRESS_updates:
    action: "Auto-update with latest progress from filesystem"
    method: "Take highest progress value (filesystem vs INDEX)"
    rationale: "Progress only goes forward, highest value is most current"
    
  STATUS_updates:
    action: "Auto-update status based on progress analysis"
    method: "100% = completed, <100% = active"
    benefit: "Automatic feature lifecycle management"
    
  MISSING_features:
    action: "Keep in INDEX but mark as [MISSING]"
    method: "Add status indicator without removal"
    rationale: "Conservative - may reappear in other sessions"
```

## Multi-Session Safety Features

### Concurrency Protection
```yaml
append_only_safety:
  principle: "New features appended to end"
  benefit: "Multiple sessions can append simultaneously"
  git_behavior: "Appends rarely conflict in git"
  
smart_updates:
  principle: "Auto-update with latest/highest values"
  benefit: "Always shows most current state across sessions"
  algorithm: "Highest progress wins, filesystem status trumps INDEX"
  
session_independence:
  principle: "Each session operates independently"
  benefit: "No coordination required between sessions"
  eventual_consistency: "All sessions converge over time"
```

### Automatic Experience
```yaml
transparency:
  show_changes: "✅ Added 2 new features: behavioral-directive, interactive-engine"
  show_updates: "📈 Updated 3 features with latest progress from filesystem"
  show_results: "INDEX sync complete: 2 additions, 3 updates, 0 conflicts"
  
automatic_intelligence:
  new_features: "Added automatically with current filesystem data"
  progress_updates: "Latest progress from any session applied"
  status_sync: "Completed features automatically flagged"
  missing_handling: "Missing features marked [MISSING] but preserved"
```

## Implementation Steps

### Step 1: Discovery
```bash
# Use native Claude tools for filesystem scan
*glob workspace/features/active/*
# Extract directory names as feature names

# Read each feature's progress.md (NO LIMIT PARAMETER)
*read workspace/features/active/{feature}/progress.md
# Extract "Overall Progress: X%" pattern
```

### Step 2: Analysis
```bash
# Read current INDEX.md active section
*read workspace/features/INDEX.md

# Compare filesystem vs INDEX
# Classify changes as SAFE/QUESTIONABLE/DANGEROUS
```

### Step 3: Safe Updates
```bash
# Create backup
*bash cp workspace/features/INDEX.md "INDEX.md.backup.$(date +%Y%m%d_%H%M%S)"

# Auto-append new features and update existing ones
*edit workspace/features/INDEX.md
# Use surgical edits to:
# - Append new features with filesystem data
# - Update progress with highest values (filesystem vs INDEX)
# - Update status based on progress (100% = completed)
# - Mark missing features as [MISSING] but preserve entries
```

## Error Handling
```yaml
filesystem_errors:
  missing_progress: "Default to 0% progress"
  malformed_progress: "Extract what possible, flag for review"
  
index_errors:
  corrupted_index: "Use backup, regenerate from filesystem"
  git_conflicts: "Conservative approach - preserve all data"
  
automation_errors:
  calculation_failures: "Use filesystem value as authoritative"
  merge_conflicts: "Highest progress value wins automatically"
```

## Success Criteria
- [ ] All filesystem features represented in INDEX
- [ ] No data loss from concurrent sessions
- [ ] User maintains control over questionable changes
- [ ] Execution time under 20 seconds
- [ ] Works reliably with 3-6 concurrent sessions

## Integration Points
```yaml
close_chat_workflow:
  engine: "feature_lifecycle"
  task: "multi_session_safe_index_sync"
  priority: "critical"
  
orchestrator_activation:
  step: "9.5 - Feature Context Check with Index Sync"
  mode: "lightweight - new features only"
  timeout: "10 seconds"
```

## Multi-Session Benefits
```yaml
for_user_workflow:
  session_a: "Creates new features → auto-added to INDEX"
  session_b: "Completes features → user prompted to confirm"
  session_c: "Updates progress → user decides whether to sync"
  
result: "All sessions eventually see accurate INDEX without data loss"
coordination_required: "NONE - each session operates independently"
```

---

**This task transforms INDEX maintenance from a multi-session coordination problem into a series of independent, conservative operations that eventually converge to consistency.**