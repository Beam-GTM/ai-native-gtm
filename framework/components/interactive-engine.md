---
name: interactive-engine
description: Clean implementation engine for state detection, content population, and user interaction
type: component
version: 1.0
---

# Interactive Engine Component

## Purpose
Provides the actual implementation logic for menu state detection, dynamic content population, and user interaction handling.

## Core Implementation

### 1. State Detection Implementation

```yaml
state_detector:
  execute: |
    # State Detection Algorithm (runs in sequence, first match wins)
    
    1_TEMPLATE_CHECK:
      conditions:
        - check_file_size: "workspace/memory/project-memory.md"
          if: "size < 500 bytes"
          then: "template_state = true"
        - check_content: "framework/CRITICAL-DIRECTIVES.md"
          if: "contains 'TEMPLATE STATE ACTIVE'"
          then: "template_state = true"
        - check_exists: "workspace/features/active/*"
          if: "count = 0"
          then: "template_state = true"
      result: 
        if_true: "LOAD: framework/components/menus/template-menu.md"
        stop: true
    
    2_CRITICAL_CHECK:
      conditions:
        - check_memory: "workspace/memory/core-learnings.md"
          if: "size > 50000 bytes OR line_count > 1000"
          then: "memory_critical = true"
        - check_timestamp: "workspace/memory/system-sync-state.yaml"
          if: "last_sync > 48 hours ago"
          then: "sync_critical = true"
        - check_logs: "workspace/data-output/errors.log"
          if: "contains 'CRITICAL' OR 'ERROR'"
          then: "errors_critical = true"
      result:
        if_any_true: "LOAD: framework/components/menus/critical-menu.md"
        stop: true
    
    3_HIGH_ACTIVITY_CHECK:
      conditions:
        - count_features: "workspace/features/active/*"
          if: "count >= 3"
          then: "high_activity = true"
        - check_recent: "workspace/memory/project-memory.md"
          if: "last_entry < 2 hours ago"
          then: "recent_activity = true"
        - calculate_progress: "workspace/features/active/*/progress.md"
          if: "average_progress > 70%"
          then: "high_momentum = true"
      result:
        if_any_true: "LOAD: framework/components/menus/active-menu.md"
        stop: true
    
    4_CLEAN_CHECK:
      conditions:
        - count_features: "workspace/features/active/*"
          if: "count <= 1"
          then: "minimal_activity = true"
        - check_health: "SYSTEM-STRUCTURE.md"
          if: "health >= 95%"
          then: "system_healthy = true"
        - check_warnings: "workspace/data-output/*"
          if: "no warnings or alerts"
          then: "clean_status = true"
      result:
        if_all_true: "LOAD: framework/components/menus/clean-menu.md"
        stop: true
    
    5_DEFAULT:
      result: "LOAD: framework/components/menus/standard-menu.md"
```

### 2. Dynamic Content Population

```yaml
content_populator:
  gather_data: |
    # Collect system metrics for menu placeholders
    
    ACTIVE_FEATURES:
      source: "workspace/features/active/*"
      format: "{count} active features"
      fallback: "No active features"
    
    SYNC_STATUS:
      source: "workspace/memory/system-sync-state.yaml"
      calculate: "time_since_last_sync"
      format:
        < 1h: "Recently synced"
        < 24h: "Synced {hours}h ago"
        < 48h: "Sync recommended"
        >= 48h: "SYNC OVERDUE"
      fallback: "Never synced"
    
    SYSTEM_HEALTH:
      sources:
        - memory_usage: "workspace/memory/core-learnings.md size"
        - error_count: "workspace/data-output/errors.log count"
        - warning_count: "workspace/data-output/warnings.log count"
      calculate:
        if: "no errors AND no warnings AND memory < 80%"
        then: "System healthy ✅"
        elif: "warnings > 0 OR memory > 80%"
        then: "Needs attention ⚠️"
        else: "Critical state 🚨"
      fallback: "Status unknown"
    
    CURRENT_FEATURE:
      source: "workspace/features/active/*"
      sort_by: "last_modified DESC"
      extract: "feature_name from first result"
      fallback: "new-feature"
    
    FEATURE_DESCRIPTION:
      source: "workspace/features/active/{CURRENT_FEATURE}/prd.md"
      extract: "first line after 'description:'"
      max_length: 50
      fallback: "Continue development"
    
    SUGGESTED_ACTION:
      logic: |
        IF template_state:
          "Complete 60-second quick setup"
        ELIF critical_state:
          "Fix {CRITICAL_ISSUE} immediately"
        ELIF high_activity AND near_complete_feature:
          "Complete {FEATURE} - {REMAINING}% left"
        ELIF high_activity:
          "Continue {CURRENT_FEATURE} development"
        ELIF clean_state:
          "Start building something awesome"
        ELSE:
          "Review active work and prioritize"
    
    GO_ACTION_TIP:
      derive_from: SUGGESTED_ACTION
      format: "action_verb from suggestion"
      examples:
        "Complete 60-second..." → "start setup"
        "Fix {ISSUE}..." → "resolve critical issue"
        "Continue {FEATURE}..." → "keep momentum"
        "Start building..." → "create new feature"
```

### 3. User Input Processing

```yaml
input_processor:
  natural_language_routing:
    # Process any user input and route to appropriate action
    
    EXACT_MATCHES:
      "go": execute(SUGGESTED_ACTION)
      "1": execute(menu_option_1)
      "2": execute(menu_option_2)
      "3": execute(menu_option_3)
      "4": execute(menu_option_4)
      "5": execute(menu_option_5)
      "6": execute(menu_option_6)
      "help": reload_menu()
      "status": show_detailed_status()
      "exit": execute(close_chat_workflow)
    
    INTENT_PATTERNS:
      build_patterns:
        triggers: ["build", "create", "make", "start", "new"]
        detect: "extract object after trigger word"
        confirm: "Build {object}? I'll guide you through the workflow. (Y/n)"
        action: "load plan-feature workflow"
      
      continue_patterns:
        triggers: ["continue", "work on", "resume", "finish"]
        detect: "identify most relevant active feature"
        confirm: "Continue {feature}? You're at {progress}%. (Y/n)"
        action: "load feature workspace"
      
      fix_patterns:
        triggers: ["fix", "repair", "resolve", "debug"]
        detect: "identify issue or error"
        confirm: "Fix {issue}? I'll help diagnose and resolve. (Y/n)"
        action: "route to appropriate specialist"
      
      help_patterns:
        triggers: ["explain", "help", "how", "what", "why"]
        detect: "extract topic after trigger"
        confirm: "Get help with {topic}? (Y/n)"
        action: "load explainer agent"
      
      specialist_patterns:
        triggers: ["developer", "architect", "product", "ux", "quality"]
        detect: "agent name from trigger"
        confirm: "Switch to {agent} agent? (Y/n)"
        action: "load specified agent"
    
    FUZZY_MATCHING:
      threshold: 85%
      strategy: |
        1. Check for partial command matches
        2. Check for common typos/abbreviations
        3. Check for workflow name fragments
        4. If multiple matches: show numbered list
        5. If no matches: suggest closest alternatives
```

### 4. Elicitation Flow

```yaml
elicitation_engine:
  context_gathering:
    # Progressively gather context for better suggestions
    
    INITIAL_UNKNOWN:
      prompt: "I'd like to help! What are you trying to accomplish?"
      follow_up:
        if_vague: "Could you tell me more about your goal?"
        if_technical: "Are you building, fixing, or exploring?"
        if_feature: "Is this a new feature or existing work?"
    
    CLARIFICATION:
      ambiguous_feature:
        prompt: "I found multiple features matching '{input}':"
        format: "1. {feature1} ({progress1}%)\n2. {feature2} ({progress2}%)"
        follow: "Which one? (enter number)"
      
      unclear_intent:
        prompt: "I can help in several ways:"
        options:
          - "Build something new"
          - "Continue existing work"
          - "Fix an issue"
          - "Learn about the system"
        follow: "What sounds right? (1-4)"
    
    CONFIRMATION:
      template: |
        ✅ Got it! You want to {interpreted_intent}.
        
        I'll {planned_action}. This will:
        • {benefit_1}
        • {benefit_2}
        • {benefit_3}
        
        Ready to proceed? (Y/n)
```

### 5. Implementation Orchestration

```yaml
orchestration_flow:
  activation_step_10:
    # Modified Step 10 for interactive engine
    execute_sequence:
      1: "Load framework/components/menu-index.md"
      2: "Load framework/components/interactive-engine.md"
      3: "Execute state_detector algorithm"
      4: "Load selected menu file"
      5: "Execute content_populator"
      6: "Display populated menu"
      7: "Wait for user input"
      8: "Execute input_processor"
      9: "Route to appropriate action"
      10: "Handle response or loop back"
  
  runtime_behavior:
    state_caching:
      duration: "session"
      invalidate_on: ["feature changes", "sync operations", "error states"]
    
    content_refresh:
      frequency: "on each menu display"
      optimize: "cache static content, refresh dynamic only"
    
    error_handling:
      missing_files: "use fallback values"
      detection_failure: "default to standard menu"
      population_error: "show placeholder with warning"
      routing_failure: "ask for clarification"
```

## Integration Points

### With Orchestrator
```yaml
orchestrator_integration:
  activation:
    step_10: "Load interactive-engine.md"
    step_11: "Execute state detection"
    step_12: "Display contextual menu"
  
  command_handling:
    all_inputs: "Route through input_processor"
    confirmations: "Use elicitation_engine"
    menu_refresh: "Re-execute full flow"
```

### With Menu System
```yaml
menu_integration:
  menu_index: "Provides detection rules"
  menu_files: "Provides display templates"
  interactive_engine: "Provides execution logic"
  result: "Complete interactive system"
```

## Performance Optimizations

```yaml
optimizations:
  lazy_evaluation:
    - "Only check conditions until first match"
    - "Stop processing on state determination"
    
  smart_caching:
    - "Cache file counts for session"
    - "Cache feature lists until changes"
    - "Refresh only dynamic metrics"
    
  parallel_checks:
    - "Run independent conditions simultaneously"
    - "Gather all metrics in single pass"
    
  minimal_reads:
    - "Read only headers for metadata"
    - "Use file stats before content reads"
    - "Batch file operations"
```

This interactive engine provides:
- **Clean implementation** of state detection
- **Efficient content population** with fallbacks
- **Smart input processing** with intent recognition
- **Progressive elicitation** for unclear requests
- **Optimized performance** through caching and lazy evaluation