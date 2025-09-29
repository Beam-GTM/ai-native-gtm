# Pattern Extraction Engine
**Component**: extraction-engine  
**Location**: workspace/memory/patterns/extraction-engine.md  
**Purpose**: Analyze project memory for repeated behaviors and extract patterns  

## 🎯 OVERVIEW
The extraction engine analyzes project memory entries to identify repeated user behaviors, preferences, and workflows. It runs automatically when triggered by entry thresholds and generates pattern files for the suggestion engine.

## ⚡ TRIGGER CONDITIONS
```yaml
automatic_triggers:
  entry_threshold:
    condition: "(entry_count % 5) == 0"
    action: "Run full pattern analysis"
    
  manual_triggers:
    - Quality gate decisions
    - Workflow completions
    - Feature milestones
    - User request
```

## 📋 EXTRACTION PROCESS

### Step 1: Load Memory Window
```yaml
action: ANALYZE
source: workspace/memory/project-memory.md
window:
  size: 15  # Last 15 entries
  focus: 
    - ACTION field
    - MILESTONE field
    - PATTERN field
reason: "Recent behavior most relevant"
```

### Step 2: Identify Sequences
```yaml
action: DETECT
patterns_to_find:
  workflow_sequences:
    - "feature planning → elicitation → technical planning"
    - "agent switch → task execution → agent return"
    - "error encounter → debug → resolution"
    
  preference_patterns:
    - "always uses agent X for task Y"
    - "prefers workflow A over B"
    - "consistently chooses option C"
    
  behavior_patterns:
    - "creates features in specific order"
    - "follows same testing approach"
    - "uses similar naming conventions"
```

### Step 3: Calculate Confidence
```yaml
action: SCORE
algorithm:
  occurrences: count_similar_sequences
  confidence: occurrences / window_size
  threshold: 0.3  # 3+ occurrences in 15 entries
  
confidence_levels:
  HIGH: ">= 0.7"  # 10+ occurrences
  MEDIUM: "0.4 - 0.69"  # 6-9 occurrences
  LOW: "0.3 - 0.39"  # 3-5 occurrences
```

### Step 4: Abstract Pattern
```yaml
action: ABSTRACT
process:
  1_generalize:
    - Remove specific names/IDs
    - Extract action types
    - Identify intent
    
  2_categorize:
    type:
      - workflow_preference
      - agent_preference
      - coding_style
      - problem_solving
      - feature_creation
      
  3_generate_insight:
    format: "User [behavior] when [condition]"
    example: "User prefers elicitation when planning complex features"
```

### Step 5: Store Pattern
```yaml
action: STORE
location: workspace/memory/patterns/extracted/{pattern_id}.yaml
format:
  pattern_id: "{type}_{timestamp}"
  metadata:
    detected: "{timestamp}"
    confidence: "{score}"
    occurrences: "{count}"
    window_size: 15
    
  pattern:
    type: "{category}"
    sequence: 
      - "{action_1}"
      - "{action_2}"
      - "{action_3}"
    
  insight:
    observation: "{what_user_does}"
    condition: "{when_they_do_it}"
    suggestion: "{what_to_offer}"
```

## 🎯 PATTERN TYPES

### Workflow Preferences
```yaml
type: workflow_preference
examples:
  - "Always uses design-new-feature for planning"
  - "Prefers advanced elicitation for complex features"
  - "Consistently follows quality gates"
suggestions:
  - "Auto-suggest preferred workflow"
  - "Pre-configure workflow options"
  - "Skip confirmation for trusted patterns"
```

### Agent Preferences
```yaml
type: agent_preference
examples:
  - "Uses developer for all coding tasks"
  - "Switches to architect for design questions"
  - "Calls explainer for understanding"
suggestions:
  - "Quick-switch to preferred agents"
  - "Create custom agent combinations"
  - "Suggest agent for detected task type"
```

### Coding Style
```yaml
type: coding_style
examples:
  - "Always adds comprehensive documentation"
  - "Prefers functional programming patterns"
  - "Consistently uses specific naming conventions"
suggestions:
  - "Apply style automatically"
  - "Generate templates with preferences"
  - "Suggest style improvements"
```

### Problem Solving
```yaml
type: problem_solving
examples:
  - "Debugs by reading error → searching → testing"
  - "Resolves issues through incremental changes"
  - "Always validates after fixes"
suggestions:
  - "Provide debugging workflow"
  - "Suggest validation steps"
  - "Offer problem-specific agents"
```

## 📊 OUTPUT FORMAT

### Pattern File Example
```yaml
# Pattern: feature-planning-elicitation
pattern_id: "workflow_preference_2025-08-25T00:30:00Z"
metadata:
  detected: "2025-08-25T00:30:00Z"
  confidence: 0.85
  occurrences: 5
  window_size: 15
  last_seen: "2025-08-25T00:15:00Z"

pattern:
  type: "workflow_preference"
  name: "Feature Planning with Elicitation"
  sequence:
    - action: "request feature planning"
    - action: "choose advanced elicitation"
    - action: "complete technical planning"
    - action: "create workspace"
  
  triggers:
    - "user says 'plan feature'"
    - "user says 'build feature'"
    - "complex requirement detected"

insight:
  observation: "User consistently uses advanced elicitation for feature planning"
  condition: "When creating new features or complex components"
  frequency: "5 times in last 15 actions"
  suggestion: "Auto-offer advanced elicitation for feature planning"

recommendation:
  agent: "orchestrator"
  action: "When user mentions feature planning, immediately offer: 'Would you like to use advanced elicitation for comprehensive planning? (Y/n)'"
  confidence: "HIGH"
```

## ⚙️ CONFIGURATION

### Thresholds
```yaml
thresholds:
  min_occurrences: 3  # Minimum to create pattern
  confidence_threshold: 0.3  # 30% minimum
  window_size: 15  # Entries to analyze
  pattern_expiry: 30  # Days before re-validation
```

### Performance
```yaml
performance:
  max_execution_time: "500ms"
  max_patterns_per_run: 10
  cache_extracted: true
  parallel_analysis: true
```

## 🔗 INTEGRATION

### With Project Memory
- Triggered by entry count thresholds
- Reads last 15 entries
- Updates PATTERN field hints

### With Suggestion Engine
- Provides patterns for analysis
- Confidence scores guide suggestions
- Patterns feed recommendation generation

### With Orchestrator
- Patterns influence agent routing
- Suggestions appear in menus
- Auto-routing based on high-confidence patterns

## 📈 METRExample-Company

### Success Metrics
- Pattern accuracy: >70%
- Suggestion relevance: >80%
- User acceptance: >60%
- Performance impact: <5%

### Monitoring
- Track pattern hit rate
- Measure suggestion acceptance
- Monitor extraction time
- Validate pattern expiry

---
**REMEMBER**: The extraction engine learns from user behavior to make the system more intelligent over time!