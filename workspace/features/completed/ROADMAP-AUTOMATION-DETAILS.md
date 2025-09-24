# Roadmap Automation: How It Really Works

## 🎯 The Truth About "Automatic"

### What Automatic Means Here
- **Automatic Detection**: System knows when updates needed
- **Automatic Execution**: When orchestrator runs, it checks and updates
- **NOT Automatic**: Doesn't run in background without orchestrator

## 🔄 The Actual Update Flow

### 1. Every Time You Interact (Most Common)
```mermaid
graph TD
    A[User: "hi"] --> B[Orchestrator Activates]
    B --> C[Step 8: Load INDEX.md]
    C --> D{Check ROADMAP-UPDATE-TRIGGER}
    D -->|Conditions Met| E[Execute generate-roadmap]
    D -->|No Update Needed| F[Use Cached Roadmap]
    E --> G[Update ROADMAP.md]
    G --> H[Cache New Summary]
    H --> I[Show Menu with Fresh Data]
    F --> I
```

**Trigger Conditions Checked:**
```yaml
roadmap_needs_update_if:
  - INDEX.md modified > roadmap last generated
  - Any feature.progress changed > 25%
  - New feature added to active/
  - Feature moved to completed/
  - Current day = Monday AND last update < this week
```

### 2. Through Feature Operations
```yaml
When you work on features:
  
  "complete template simplification task":
    1. Updates progress.md → 40%
    2. Updates INDEX.md statistics
    3. INDEX.md trigger detected on next "hi"
    4. Roadmap regenerates automatically
    
  "move feature to completed":
    1. Move files to completed/
    2. INDEX.md updated
    3. Trigger activated
    4. Next orchestrator load → roadmap updates
```

### 3. Embedded Trigger Mechanism

**In INDEX.md:**
```html
<!-- ROADMAP-UPDATE-TRIGGER: AUTO-CHECK ON LOAD
     Last Generated: 2025-08-27T17:30:00Z
     Conditions: [listed above]
     Execute: framework/tasks/features/generate-roadmap.md
     Status: ACTIVE -->
```

**How It Executes:**
1. Orchestrator loads INDEX.md (Step 8)
2. Sees `AUTO-CHECK ON LOAD` directive
3. Evaluates conditions against current state
4. If ANY condition true → Runs generate-roadmap
5. Updates "Last Generated" timestamp

### 4. Manual Triggers (Always Available)
```bash
# Force immediate update
roadmap update

# Through system maintenance
*workflow system-maintenance
> Choose option 6

# Direct task execution
*task generate-roadmap
```

## 📊 Real-World Examples

### Example 1: Feature Progress Update
```markdown
Monday Morning:
1. You: "hi"
2. System: Checks trigger → "It's Monday!" → Updates roadmap
3. Menu: Shows fresh weekly priorities

Later that day:
1. You: Work on feature, update progress 15% → 40%
2. You: "hi" (or any command)
3. System: Checks trigger → ">25% change!" → Updates roadmap
4. Menu: Risk status changed from HIGH to MEDIUM
```

### Example 2: Feature Completion
```markdown
1. You: Complete evidence-tracking feature
2. You: Move to completed/
3. You: Update INDEX.md
4. You: "hi" (next interaction)
5. System: Trigger fires → Roadmap updates
6. Menu: "🎉 Evidence-tracking completed! Velocity: 1.9/week ↑"
```

### Example 3: New Feature Added
```markdown
1. You: Create new feature in active/
2. You: Add to INDEX.md
3. You: Continue working...
4. Next "hi": Trigger detects new feature
5. Roadmap: Adds to timeline, adjusts priorities
```

## 🚦 Automation Status Indicators

The system shows when updates happen:

```markdown
When trigger fires:
"📊 Roadmap outdated (last: 3 days ago). Updating..."
[1-2 seconds]
"✅ Roadmap updated! 2 features at risk, velocity 1.8/week"

When current:
[No message - uses cached version silently]

When forced:
"🔄 Regenerating roadmap..."
"✅ Roadmap current. No changes detected."
```

## 🎯 Why This Approach?

### Pros:
- **No background processes** eating resources
- **Updates when you need them** (on interaction)
- **Predictable behavior** (only during orchestrator runs)
- **Can force update** anytime with commands
- **Efficient** (caches when no changes)

### Cons:
- **Not real-time** (waits for next interaction)
- **Requires orchestrator** (no standalone updates)
- **Manual trigger possible** (user might skip)

## 🚀 Making It More Automatic

### Option 1: Aggressive Triggering
Add more trigger points:
- After EVERY task completion
- On EVERY file save in features/
- Every N minutes during active session

### Option 2: Background Task (Future)
Create a background monitor:
```yaml
background_monitor:
  check_every: 5_minutes
  update_if_changed: true
  notify_user: true
```

### Option 3: Git Hooks (For Git Users)
```bash
# .git/hooks/post-commit
if [[ $changed_files == *"features/"* ]]; then
  nexus task generate-roadmap
fi
```

## 📋 Current Implementation Summary

**What IS Automated:**
- ✅ Detection of when updates needed
- ✅ Execution during orchestrator runs
- ✅ Trigger conditions evaluation
- ✅ Cache management
- ✅ Timestamp tracking

**What ISN'T Automated:**
- ❌ Background updates without user interaction
- ❌ Real-time updates as changes happen
- ❌ Push notifications of changes
- ❌ Updates without orchestrator activation

**Bottom Line**: The roadmap updates automatically *when you interact with the system*, not continuously in the background. This is by design to maintain predictability and resource efficiency.

---

*The automation is "interactive-automatic" - it happens automatically during your normal workflow, not independently of it.*