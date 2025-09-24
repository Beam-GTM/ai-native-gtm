<!-- version: nav-guide-20250825 -->
<!-- last-updated: 2025-08-25T13:45:00Z -->
<!-- document-type: ai-navigation-guide -->

# AI Navigation Guide for Engineering Rules

## 🎯 **NAVIGATION STRATEGY FOR AI AGENTS**

### **Primary Access Pattern: Task-Based Loading**

When an AI agent needs engineering rules, follow this decision tree:

```yaml
NAVIGATION_DECISION_TREE:
  1_identify_task:
    question: "What task am I performing?"
    examples:
      - "Writing a PRD" → Load product-management/prd-writing.md
      - "Reviewing code" → Load development/code-review.md
      - "Organizing files" → Load core-foundation/file-management.md
      - "Running tests" → Load development/testing-standards.md
      - "Updating system" → Load system-operations/system-update-protocol.md

  2_check_index:
    action: "If unsure, load INDEX.md first"
    benefit: "Quick overview of all available rules"
    path: "engineeringrules/INDEX.md"

  3_lazy_loading:
    principle: "Load only what you need, when you need it"
    not: "Don't load all 37 files at once"
    instead: "Load specific sections for specific tasks"
```

## 📋 **COMMON AI SCENARIOS & NAVIGATION**

### **Scenario 1: Agent Activation**
```yaml
when: "AI agent is activating/initializing"
load:
  - core-foundation/placement-standards.md  # For file organization rules
  - core-foundation/memory-system.md        # For memory requirements
why: "These define core operational standards"
```

### **Scenario 2: Development Task**
```yaml
when: "AI is writing or reviewing code"
load_sequence:
  1: development/coding-standards.md        # General standards
  2: development/python-standards.md        # If Python project
  3: development/testing-standards.md       # If writing tests
  4: development/llm-development.md         # If LLM features
optional:
  - development/code-review.md              # For PR reviews
  - development/linting-formatting.md       # For code cleanup
```

### **Scenario 3: Product Management**
```yaml
when: "AI is doing product work"
for_prd_creation:
  - product-management/prd-writing.md       # PRD format & structure
for_sprint_planning:
  - product-management/agile-sprint.md      # Sprint standards
  - product-management/backlog-management.md # Backlog organization
for_releases:
  - product-management/release-management.md # Release process
```

### **Scenario 4: System Operations**
```yaml
when: "AI is managing system operations"
for_generation:
  - system-operations/system-generation.md  # Generation standards
  - system-operations/template-management.md # Template rules
for_maintenance:
  - system-operations/file-operations.md    # File management
  - system-operations/system-update-protocol.md # Update procedures
for_emergency:
  - system-operations/emergency-procedures.md # Recovery protocols
```

## 🔍 **SEARCH STRATEGIES**

### **Strategy 1: Grep Across Shards**
```bash
# Search for a specific concept across all shards
grep -r "validation" engineeringrules/*/

# Search within a specific domain
grep -r "test" engineeringrules/development/

# Find specific standards
grep -r "CRITICAL_RULE" engineeringrules/
```

### **Strategy 2: Smart Context Loading**
```yaml
intelligent_loading:
  step_1: "Identify the domain first"
    - Is it development? → development/
    - Is it product? → product-management/
    - Is it operations? → system-operations/
    - Is it foundational? → core-foundation/
  
  step_2: "Load domain index pattern"
    example: "Load all development/*.md for coding session"
  
  step_3: "Cache for session"
    principle: "Keep loaded rules in context for session duration"
```

## 🚀 **OPTIMIZED LOADING PATTERNS**

### **Pattern 1: Progressive Loading**
```yaml
progressive_pattern:
  initial: Load INDEX.md for overview
  focused: Load specific shard for task
  expanded: Load related shards if needed
  complete: Load full domain only if comprehensive work

example_flow:
  1: AI needs to write tests
  2: Load INDEX.md, see testing-standards.md exists
  3: Load development/testing-standards.md
  4: Task requires Python specifics
  5: Also load development/python-standards.md
  6: Don't load unrelated shards
```

### **Pattern 2: Domain Bundle Loading**
```yaml
domain_bundles:
  development_bundle:
    core: [coding-standards.md, python-standards.md]
    testing: [testing-standards.md, quality-metrics.md]
    review: [code-review.md, linting-formatting.md]
  
  product_bundle:
    planning: [prd-writing.md, agile-sprint.md]
    execution: [backlog-management.md, metrics-reporting.md]
    delivery: [release-management.md, product-quality.md]
  
  operations_bundle:
    generation: [system-generation.md, template-management.md]
    maintenance: [file-operations.md, system-update-protocol.md]
    health: [architecture-operations.md, performance-optimization.md]
```

## 📊 **CONTEXT MANAGEMENT FOR AI**

### **Working Memory Strategy**
```yaml
context_limits:
  problem: "AI has limited context window"
  solution: "Strategic loading and unloading"

management_approach:
  1_task_start:
    - Load relevant shards for immediate task
    - Keep in context during task execution
  
  2_task_switch:
    - Summarize key rules from previous task
    - Unload detailed rules
    - Load new task-specific rules
  
  3_reference_needed:
    - Temporarily load specific shard
    - Extract needed information
    - Unload after use
```

### **Caching Strategy**
```yaml
cache_hierarchy:
  session_cache:
    - INDEX.md (always available)
    - Current domain shards
    - Recently accessed rules
  
  task_cache:
    - Active task rules
    - Related standards
    - Quality gates
  
  reference_cache:
    - Quick reference snippets
    - Common patterns
    - Critical rules only
```

## 🎯 **QUICK REFERENCE MAPPING**

### **Task → Rule Mapping**
```yaml
quick_map:
  "need to organize files": core-foundation/file-management.md
  "writing documentation": core-foundation/documentation-standards.md
  "designing system": core-foundation/system-design-principles.md
  "managing memory": core-foundation/memory-system.md
  
  "writing Python code": development/python-standards.md
  "creating tests": development/testing-standards.md
  "reviewing PR": development/code-review.md
  "building LLM feature": development/llm-development.md
  
  "creating PRD": product-management/prd-writing.md
  "planning sprint": product-management/agile-sprint.md
  "managing backlog": product-management/backlog-management.md
  "preparing release": product-management/release-management.md
  
  "generating system": system-operations/system-generation.md
  "managing templates": system-operations/template-management.md
  "updating system": system-operations/system-update-protocol.md
  "handling emergency": system-operations/emergency-procedures.md
```

## 💡 **BEST PRACTICES FOR AI NAVIGATION**

### **DO's**
```yaml
best_practices:
  - DO use INDEX.md as starting point when unsure
  - DO load specific shards for specific tasks
  - DO cache frequently used rules for session
  - DO unload rules when switching contexts
  - DO use search to find specific concepts
  - DO load related shards together (e.g., testing + python)
```

### **DON'Ts**
```yaml
avoid:
  - DON'T load all 37 shards at once
  - DON'T keep unrelated rules in context
  - DON'T reload unchanged rules repeatedly
  - DON'T ignore the INDEX.md navigation
  - DON'T load consolidated files when shards exist
```

## 🔄 **INTEGRATION WITH AI WORKFLOWS**

### **Orchestrator Integration**
```yaml
orchestrator_commands:
  "*rules [domain]": Load all rules for domain
  "*rule [specific]": Load specific rule shard
  "*rules-index": Load INDEX.md for navigation
  "*rules-search [term]": Search across all shards

examples:
  "*rules development": Loads all development/*.md
  "*rule prd-writing": Loads product-management/prd-writing.md
  "*rules-search validation": Searches for validation rules
```

### **Agent Activation Pattern**
```yaml
agent_activation:
  1_on_activation:
    - Agent reads its own definition
    - Agent checks INDEX.md for relevant rules
    - Agent loads domain-specific shards
  
  2_during_operation:
    - Agent loads task-specific rules on demand
    - Agent caches rules for session duration
    - Agent unloads when switching tasks
  
  3_on_handoff:
    - Agent summarizes applicable rules
    - Agent indicates which shards next agent needs
    - Agent clears task-specific rule cache
```

## 📚 **FALLBACK STRATEGIES**

### **When Unsure Which Shard**
```yaml
fallback_sequence:
  1: Load INDEX.md
  2: Search for keywords in index
  3: Load 2-3 most likely shards
  4: Search within loaded shards
  5: Expand search if not found
```

### **When Need Comprehensive View**
```yaml
comprehensive_loading:
  option_1: "Load all shards in domain"
    example: "Load all development/*.md for code audit"
  
  option_2: "Load original consolidated file"
    example: "Load development-standards.md for full picture"
  
  option_3: "Load INDEX.md + specific sections"
    example: "Use index to navigate + load key sections"
```

---

**AI NAVIGATION PROMISE**: This guide ensures AI agents can efficiently navigate the sharded engineering rules, loading only what they need when they need it, while maintaining full access to all engineering standards and guidelines.