# Suggestion Engine
**Component**: suggestion-engine  
**Location**: workspace/memory/patterns/suggestion-engine.md  
**Purpose**: Generate intelligent recommendations based on extracted patterns  

## 🎯 OVERVIEW
The suggestion engine analyzes extracted patterns to generate contextual recommendations for agents, workflows, and optimizations. It runs after pattern extraction and maintains an active suggestions list that influences system behavior.

## ⚠️ CRITICAL: DATA PRESERVATION
**NEVER OVERWRITE EXISTING SUGGESTIONS OR USER DATA**
- This engine operates in APPEND-ONLY mode
- Existing suggestions must be preserved
- New suggestions are added to the list
- Only update header metadata (counts, timestamps)
- User-created content is sacred - never delete or overwrite

## ⚡ TRIGGER CONDITIONS
```yaml
automatic_triggers:
  pattern_extraction:
    condition: "New patterns extracted"
    action: "Generate suggestions from patterns"
    
  entry_threshold:
    condition: "Every 5 new memory entries"
    action: "Refresh suggestions based on context"
    
  confidence_threshold:
    condition: "Pattern confidence > 70%"
    action: "Create high-priority suggestion"
```

## 📋 SUGGESTION GENERATION PROCESS

### Step 1: Load Patterns
```yaml
action: LOAD
source: workspace/memory/patterns/extracted/*.yaml
filters:
  confidence: ">= 0.7"  # Only high confidence
  age: "< 30 days"  # Recent patterns only
  relevance: "matches_current_context"
sort: "confidence DESC, occurrences DESC"
```

### Step 2: Analyze Context
```yaml
action: CONTEXTUALIZE
inputs:
  current_memory: workspace/memory/project-memory.md
  active_features: workspace/features/active/*/
  recent_actions: "last 5 entries"
  
determine:
  - current_task_type
  - user_intent
  - workflow_stage
  - likely_next_action
```

### Step 3: Generate Suggestions
```yaml
action: GENERATE
types:
  agent_suggestions:
    format: "Consider using {agent} for {task}"
    example: "Consider using developer agent for implementation"
    
  workflow_suggestions:
    format: "Run {workflow} to {benefit}"
    example: "Run design-new-feature to plan your component"
    
  optimization_suggestions:
    format: "Automate {pattern} with {solution}"
    example: "Automate testing with quality-gate workflow"
    
  new_capability_suggestions:
    format: "Create {type} for {repeated_action}"
    example: "Create custom agent for database operations"
```

### Step 4: Score & Prioritize
```yaml
action: PRIORITIZE
scoring:
  relevance: 
    weight: 0.4
    factors: ["context_match", "timing", "user_state"]
    
  confidence:
    weight: 0.3
    factors: ["pattern_confidence", "occurrence_count"]
    
  impact:
    weight: 0.3
    factors: ["time_saved", "error_reduction", "quality_improvement"]
    
priority_levels:
  CRITICAL: ">= 0.9"  # Show immediately
  HIGH: "0.7 - 0.89"  # Show in menu
  MEDIUM: "0.5 - 0.69"  # Show on request
  LOW: "< 0.5"  # Store for analysis
```

### Step 5: Store Suggestions
```yaml
action: APPEND
location: workspace/memory/suggestions/active.md
strategy: "PRESERVE_EXISTING"
format:
  header:
    updated: "{timestamp}"
    count: "{total_suggestions}"
    triggered: "{trigger_condition}"
    
  new_suggestions:
    - id: "{suggestion_id}"
      type: "{category}"
      priority: "{level}"
      text: "{suggestion_text}"
      action: "{recommended_action}"
      confidence: "{score}"
      pattern_ref: "{pattern_id}"
      
  preservation_rules:
    - "NEVER overwrite existing suggestions"
    - "ADD new suggestions to existing list"
    - "UPDATE header counts only"
    - "MAINTAIN suggestion history"
    - "EXPIRE old suggestions after 7 days"
```

## 🎯 SUGGESTION TYPES

### Agent Recommendations
```yaml
type: agent_recommendation
triggers:
  - "Repeated task type detected"
  - "Current task matches agent specialty"
  - "Error pattern suggests different agent"
  
examples:
  - text: "You frequently debug Python code. Launch developer agent?"
    action: "*agent developer"
    confidence: 0.85
    
  - text: "Complex architecture decision ahead. Use architect agent?"
    action: "*agent architect"
    confidence: 0.92
```

### Workflow Automation
```yaml
type: workflow_automation
triggers:
  - "Repeated sequence detected"
  - "Manual steps could be automated"
  - "Pattern matches existing workflow"
  
examples:
  - text: "You follow this 5-step process often. Create a workflow?"
    action: "Create custom workflow from pattern"
    confidence: 0.78
    
  - text: "Feature planning pattern detected. Use design-new-feature?"
    action: "*workflow design-new-feature"
    confidence: 0.88
```

### New Agent Creation
```yaml
type: new_agent_suggestion
triggers:
  - "Specialized task repeated >5 times"
  - "No existing agent matches pattern"
  - "Custom behavior consistently needed"
  
examples:
  - text: "You often work with databases. Create a database specialist agent?"
    action: "Generate database-specialist agent template"
    confidence: 0.75
    
  - text: "API testing pattern detected. Create API testing agent?"
    action: "Generate api-tester agent template"
    confidence: 0.82
```

### Optimization Opportunities
```yaml
type: optimization
triggers:
  - "Inefficient pattern detected"
  - "Repeated error-fix cycles"
  - "Manual process could be automated"
  
examples:
  - text: "You manually update 5 files each time. Automate with task?"
    action: "Create batch-update task"
    confidence: 0.90
    
  - text: "Testing after every change. Enable auto-test mode?"
    action: "Configure auto-test workflow"
    confidence: 0.77
```

## 📊 OUTPUT FORMAT

### Active Suggestions File
```markdown
# Active Suggestions | Updated: 2025-08-25T00:45:00Z | Count: 3
**Generated From**: 5 high-confidence patterns
**Trigger**: Entry threshold reached (5 new entries)

## 🔴 CRITICAL SUGGESTIONS

### 1. Feature Planning Workflow Detected
**Confidence**: 95%
**Pattern**: You've planned 3 features using similar steps
**Suggestion**: "Launch design-new-feature workflow for structured planning?"
**Quick Action**: Type 'workflow design' or '1' to start
**Based On**: Pattern workflow_preference_2025-08-25

## 🟡 HIGH PRIORITY SUGGESTIONS

### 2. Developer Agent Preference
**Confidence**: 82%
**Pattern**: You use developer agent for all code tasks
**Suggestion**: "Set developer as default for coding tasks?"
**Quick Action**: Type 'set default' or '2' to configure
**Based On**: Pattern agent_preference_2025-08-25

## 🟢 MEDIUM PRIORITY SUGGESTIONS

### 3. Create Database Agent
**Confidence**: 68%
**Pattern**: Database operations appearing frequently
**Suggestion**: "Create specialized database agent?"
**Quick Action**: Type 'create agent' or '3' to generate
**Based On**: Pattern specialization_need_2025-08-25

## 📈 PATTERN INSIGHTS
- You prefer comprehensive planning (5/5 features)
- You validate after major changes (8/10 times)
- You use similar naming conventions (project-*)

## 🎯 QUICK ACTIONS
Type the number (1-3) to accept a suggestion, or 'dismiss' to clear
```

## ⚙️ CONFIGURATION

### Thresholds
```yaml
thresholds:
  min_confidence: 0.7  # Minimum to generate suggestion
  max_suggestions: 10  # Maximum active suggestions
  refresh_interval: 5  # Entries between refreshes
  suggestion_expiry: 7  # Days before re-evaluation
  
preservation_policy:
  mode: "APPEND_ONLY"  # Never overwrite, only append
  merge_duplicates: true  # Merge if same pattern detected
  update_confidence: true  # Update confidence if pattern stronger
  preserve_user_data: true  # Never delete user-created content
```

### Display Rules
```yaml
display:
  critical_always_show: true
  high_in_menu: true
  medium_on_request: true
  low_hidden: true
  max_display: 3  # Max shown at once
```

## 🔗 INTEGRATION

### With Orchestrator
```yaml
orchestrator_integration:
  menu_display:
    - Show top 3 suggestions in help menu
    - Add suggestion numbers for quick access
    
  auto_routing:
    - Apply CRITICAL suggestions automatically
    - Ask confirmation for HIGH suggestions
    
  context_awareness:
    - Load suggestions on activation
    - Update based on user actions
```

### With Patterns
```yaml
pattern_integration:
  source: workspace/memory/patterns/extracted/
  refresh: "On new pattern detection"
  validation: "Check pattern still valid"
  feedback: "Track suggestion acceptance"
```

### With Project Memory
```yaml
memory_integration:
  triggers:
    - Entry count thresholds
    - Milestone completions
    
  updates:
    - Mark accepted suggestions (preserve existing)
    - Track rejection reasons (append to list)
    - Update pattern confidence (modify metadata only)
    
  preservation_guarantee:
    - "READ existing suggestions first"
    - "APPEND new suggestions to existing"
    - "NEVER replace entire file"
    - "PRESERVE user modifications"
```

## 📈 METRICS

### Success Metrics
- Suggestion acceptance: >60%
- Relevance score: >80%
- Time saved: >30%
- User satisfaction: >4/5

### Tracking
```yaml
tracking:
  accepted_suggestions: []
  rejected_suggestions: []
  auto_applied: []
  user_feedback: []
  time_saved_estimate: "0 hours"
```

## 🎮 USER INTERACTION

### Accepting Suggestions
```yaml
accept_flow:
  1_display: "Show numbered suggestions"
  2_select: "User types number or action"
  3_execute: "Run suggested command"
  4_track: "Update pattern confidence"
  5_update: "Refresh suggestions"
```

### Dismissing Suggestions
```yaml
dismiss_flow:
  1_dismiss: "User types 'dismiss' or 'ignore'"
  2_reason: "Optional: Ask why"
  3_adjust: "Lower pattern confidence"
  4_hide: "Don't show for 7 days"
```

---
**REMEMBER**: The suggestion engine makes the system feel intelligent by learning and adapting to user behavior!