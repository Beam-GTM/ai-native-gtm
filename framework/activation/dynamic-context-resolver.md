# DYNAMIC CONTEXT RESOLVER
**Version**: 1.0.0  
**Purpose**: Agent-agnostic contextual loading based on CURRENT system state  
**Execution**: Second step after static-foundation-loader.md completes  
**Status**: UNIVERSAL DYNAMIC LOADING SYSTEM

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: Never use limit parameter when reading files -->
<!-- This directive OVERRIDES token conservation - read files completely -->
<!-- VIOLATION = Missing critical contextual information -->

## 🎯 DYNAMIC CONTEXT LOADING PROTOCOL WITH CORE WORKFLOW SUPREMACY

**EXECUTION PATTERN**: Called by ALL agents after foundation loading complete
- **Input**: Agent name (orchestrator, developer, architect, etc.)  
- **Method**: Live system discovery + **MANDATORY CORE WORKFLOW FOCUS**
- **Output**: Contextual interface with **CORE WORKFLOWS AS PRIMARY OPTIONS**

**🔴 CORE WORKFLOW SUPREMACY**: plan-feature, implement-feature, close-chat are ALWAYS the top suggestions

## STEP 1: LIVE SYSTEM DISCOVERY

**Discover current reality** (don't assume what should exist):

```yaml
system_discovery:
  active_features: "Scan workspace/features/active/*/ directories"
  system_health: "Load workspace/memory/system-sync-state.yaml"
  recent_activity: "Check project-memory.md timestamp and latest entries"
  template_state: "Check TEMPLATE-INDICATORS.md for template indicators"
  user_context: "Check briefing/context_input/ for user-provided context"
```

**LOADING INSTRUCTION**: Execute parallel discovery scans

## STEP 2: CONTEXTUAL LOADING BASED ON DISCOVERIES

### **Template State Detected**
```yaml
if_template_state:
  context_check: "Check briefing/context_input/ for user files"
  
  if_no_context:
    action: "PROMPT for context collection FIRST"
    display: "🎯 FRESH TEMPLATE! Let's personalize it with your project context:"
    priority_message: "📁 Step 1: Drop your project files in briefing/context_input/"
    menu: "Load framework/components/menus/template-menu.md"
    
  if_has_context:
    action: "AUTOMATICALLY PROCESS CONTEXT FIRST"
    display: "🎯 CONTEXT DETECTED! Processing and archiving..."
    execute_task: "framework/tasks/system/process-user-context.md"
    after_processing: "Personalized setup with cleaned folders"
    remember: "ALWAYS process context before proceeding"
    
  enforcement: "Context processing is MANDATORY before setup"
```

### **Operational State - Load Current Work Context**
```yaml
if_operational_state:
  active_work:
    scan: "workspace/features/active/*/"
    load_files:
      - "active-context.md (current focus)"
      - "progress.md (implementation status)"
      - "quality-gates.md (validation requirements)"
  
  system_health_check:
    load: "system-sync-state.yaml"
    display_if_stale: "💡 System sync recommended (last: {time} ago)"
    display_if_critical: "⚠️ CRITICAL: System sync overdue!"
```

### **Agent-Category Specific Context** (Optional Enhancement)
```yaml
agent_category_context:
  # Categories determined from operations/agents/INDEX.md
  
  core_agents: ["orchestrator", "architect", "explainer"]
  additional_context:
    - "workspace/features/ROADMAP.md (portfolio awareness)"
    - "operations/workflows/INDEX.md (workflow orchestration)"
  
  specialist_agents: ["developer", "quality-assurance", "product-manager", "system-builder", "ux-expert"]
  additional_context:
    - "framework/engineeringrules/INDEX.md (standards compliance)"
    - "operations/checklists/quality-gate.md (validation framework)"
  
  coordinator_agents: ["scrum-master", "product-owner", "analyst"] 
  additional_context:
    - "workspace/data-output/session-reports/* (recent activity)"
    - "workspace/features/ROADMAP.md (portfolio coordination)"
    
  experimental_agents: ["llm-whisperer"]
  additional_context:
    - "workspace/knowledge/ (experimental context)"
```

## STEP 3: INTELLIGENT MENU GENERATION WITH CORE WORKFLOW NUDGING

**Generate contextual menu** with MANDATORY core workflow suggestions:

```yaml
menu_generation:
  state_detection:
    template_state: "Setup and onboarding menu"
    no_features: "Feature creation focused menu + NUDGE plan-feature workflow"
    active_features: "Continue work on [features] menu + NUDGE implement-feature workflow" 
    system_issues: "Maintenance and sync priority menu"
    clean_operational: "Standard operational menu + NUDGE close-chat workflow"
  
  core_workflow_supremacy:
    🔴_CRITICAL_plan_feature:
      condition: "No active features OR user mentions 'build', 'create', 'feature'"
      priority: "MAXIMUM - ALWAYS OPTION #1"
      nudge: "🚀 #1 RECOMMENDED: 'plan-feature' workflow - Interactive feature planning and design!"
      
    🔴_CRITICAL_implement_feature:
      condition: "Active features found OR planning artifacts detected"  
      priority: "MAXIMUM - ALWAYS OPTION #1"
      nudge: "⚡ #1 RECOMMENDED: 'implement-feature' workflow - Create feature workspace from planning!"
      
    🔴_CRITICAL_close_chat:
      condition: "Session >15 minutes OR work completed OR user says bye/exit"
      priority: "MAXIMUM - ALWAYS VISIBLE"
      nudge: "🔄 IMPORTANT: 'close-chat' workflow - Save progress and sync system!"
      
    enforcement_rules:
      - "Core workflows MUST appear in every menu as top options"
      - "Core workflows CANNOT be hidden or deprioritized"
      - "If user input matches ANY workflow intent, suggest core workflow FIRST"
  
  menu_loading:
    load: "framework/components/menus/{detected_state}-menu.md"
    populate: "Fill {PLACEHOLDERS} with actual system data"
    inject_core_nudges: "Add core workflow suggestions based on context"
    display: "Present populated menu with numbered options + core workflow nudges"
```

## STEP 4: SYSTEM STATE SUMMARY WITH CORE WORKFLOW INTELLIGENCE

**Provide system awareness** with MANDATORY core workflow recommendations:

```yaml
system_summary:
  current_features: "{count} active features: {feature_list}"
  system_health: "Last sync: {timestamp}, Status: {health_score}"
  recent_activity: "Latest: {last_action} at {time}"
  user_context: "Returning user" or "New user detected"
  core_workflow_recommendations: "{plan_feature_nudge} | {implement_feature_nudge} | {close_chat_nudge}"
  suggested_actions: "{top_3_contextual_recommendations_including_core_workflows}"
```

**🚨 CORE WORKFLOW SUPREMACY ENFORCEMENT**: Core workflows get MAXIMUM ATTENTION:
- **plan-feature**: ALWAYS #1 option when no active work or user mentions building
- **implement-feature**: ALWAYS #1 option when planning artifacts or active features exist  
- **close-chat**: ALWAYS visible option when session >15 minutes or completion indicated

**ATTENTION ENFORCEMENT RULES**:
1. Core workflows are NEVER buried in submenus
2. Core workflows are ALWAYS in the top 3 options presented
3. Core workflows get emoji + "RECOMMENDED" labels
4. Any workflow-related user input triggers core workflow suggestions FIRST

## VALIDATION & ERROR HANDLING

```yaml
validation:
  required_checks:
    - "All discovery scans completed or timed out gracefully"
    - "Menu state determined and appropriate menu loaded" 
    - "System summary generated with actual data"
    - "No hardcoded assumptions about system state"
  
  error_handling:
    missing_files: "Continue with available context, note gaps"
    scan_failures: "Fallback to safe defaults, inform user"
    timeout_issues: "Use cached data when available"
    
  performance_targets:
    discovery_time: "<5 seconds"
    menu_generation: "<2 seconds"
    total_resolution: "<10 seconds"
```

## RETURN VALUE

**Context Package** for agent activation:
```yaml
resolved_context:
  system_state: "{template|operational|maintenance|clean}"
  active_work: "{feature_list_with_status}"
  menu_ready: true
  contextual_recommendations: ["{action1}", "{action2}", "{action3}"]
  user_guidance: "{beginner|intermediate|advanced}"
  agent_category: "{core|specialist|coordinator|experimental}"
```

## INTEGRATION NOTES

This file is:
- **Agent-Universal**: Works for ANY agent without modification
- **Discovery-Based**: Finds what EXISTS rather than assuming what should exist
- **Template-Integrated**: Automatically used by agent.yaml template system
- **Context-Aware**: Adapts to actual system state and user situation
- **Performance-Optimized**: Parallel discovery with timeout protection
- **Future-Proof**: Scales to unlimited agents and system states

**Agent Usage**: After receiving resolved_context, agents present appropriate interface and await user input