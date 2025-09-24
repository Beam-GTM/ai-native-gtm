# Update System Status Task

## Purpose
Update the SYSTEM STATUS header in project-memory.md with real-time feature progress and critical priorities.

## When to Execute
- After completing any feature work
- When discovering progress discrepancies  
- After major breakthroughs or blockers
- At start of each session (via orchestrator)
- When features are completed/archived

## Status Update Protocol

### 1. Update Timestamp
```markdown
Updated: 2025-08-28T[current-time]Z
```

### 2. Assess System Health
- 🟢 HEALTHY: <8 active features, low complexity
- 🟡 HIGH ACTIVITY: 8-12 active features, moderate complexity
- 🔴 CRITICAL: >12 active features OR critical blockers

### 3. Update Critical Priorities (Top 2)
List most urgent items that could block system function:
- Path reference breaks
- Progress tracking failures
- Feature conflicts
- Safety protocol violations

### 4. Update Recent Breakthroughs (Today's achievements)
- New features created
- Major implementations completed
- Paradigm shifts discovered
- Critical insights gained

### 5. Update Portfolio Reality Check
- Actual feature count vs claimed
- Stale file identification
- Implementation vs planning ratios
- Empty/abandoned features

### 6. Update Ready for Implementation List
Features with:
- Complete planning
- Clear next steps
- No blockers
- Evidence-based readiness

### 7. Update Key Insights
Current system-wide learnings and solutions

## Integration Points & Triggers

### **Automatic Triggers (Must call this task)**
1. **orchestrator.md activation** - Update status on every session start
2. **close-chat workflow** - Update status before session closure
3. **feature completion** - Update when features moved to completed/
4. **workflow completion** - Update after major workflow execution
5. **critical issue detection** - Update when blockers identified
6. **breakthrough discovery** - Update when paradigm shifts happen
7. **progress discrepancy detection** - Update when inflation found

### **Manual Triggers (Should call this task)**
- After significant feature work
- When updating progress.md files
- During system maintenance
- After architectural changes
- When roadmap changes

### **Required Integration Points**
```yaml
must_update_status:
  - close-chat.md: "STEP 3: Update system status before memory rotation"
  - feature-completion-workflow.md: "STEP 5: Update status after moving to completed/"
  - orchestrator.md: "STEP 2: Load and update system status"
  - progress-update-tasks: "STEP FINAL: Update centralized status"
```

## Success Criteria
- Status reflects current reality
- Critical items clearly highlighted
- Ready-to-work list accurate
- Timestamp current
- Health status appropriate

---

This task ensures the SYSTEM STATUS header remains the authoritative source of truth, solving the stale progress.md problem.