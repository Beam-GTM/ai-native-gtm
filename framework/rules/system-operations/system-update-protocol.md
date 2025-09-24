<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# System Update Protocol

## 🔄 **SYSTEM UPDATE PROTOCOL**

### **Complete System Component Inventory**

#### **Core Components**
```yaml
agent_definitions:
  location: operations/agents/
  count: 16 files
  includes: [orchestrator, architect, developer, etc.]

memory_documents:
  location: workspace/memory/
  types: [project-brief, system-architecture, etc.]
  per_feature: [prd, progress, active-context]

engineering_rules:
  location: operations/engineeringrules/
  core: 7 files
  repository_specific: Variable per repository

structure_templates:
  location: operations/.structure/
  count: 6 files
  types: [agent, task, workflow, checklist]

generation_templates:
  location: operations/templates/
  types: [systems, domains, components]
```

### **Systematic Update Protocol**

#### **Phase 1: Planning & Impact Assessment**
```yaml
step_1_define_scope:
  - What specific improvement?
  - Which component types affected?
  - Are there interdependencies?
  - What is rollback plan?

step_2_create_matrix:
  - List all files requiring updates
  - Define specific changes per file
  - Identify update pattern/template
  - Set validation criteria

step_2.5_generate_checklist:
  CRITICAL: Create validation checklist before starting
  location: operations/checklists/system-update-[DATE].md
  includes:
    - Validation items per component
    - File count verification
    - Pattern consistency validation
    - Cross-reference integrity
    - Agent activation testing
```

#### **Phase 2: Update Execution**
```yaml
step_3_template_updates:
  priority_order:
    1: Structure templates
    2: Engineering rules
    3: Generation templates
    4: Agent definitions
    5: Memory documents

step_4_systematic_updates:
  for_each_file:
    1: Load current timestamp
    2: Read existing structure
    3: Apply update pattern
    4: Update version header
    5: Validate syntax
    6: Verify cross-references

step_5_update_validation:
  after_each_file:
    - Verify structure integrity
    - Check cross-references
    - Validate against rules
    - Test agent activation
```

#### **Phase 3: System Validation**
```yaml
step_6_execute_checklist:
  CRITICAL: Complete generated validation checklist
  process:
    1: Load session checklist
    2: Execute each item systematically
    3: Mark PASS/CONCERNS/FAIL/WAIVED
    4: Document issues found
    5: Require 100% PASS for critical
    6: Address all CONCERNS

step_7_comprehensive_check:
  validation:
    - All checklist items addressed
    - 100% component coverage
    - Documentation compliance
    - System functionality confirmed

step_8_final_verification:
  evidence:
    - Completed checklist with PASS
    - Updated file count verification
    - Timestamp consistency
    - Agent activation results
    - Cross-reference validation
```

### **Validation Checklist Template**
```yaml
checklist_structure:
  header:
    - Update session and timestamp
    - Improvement description
    - Scope and categories
  
  validation_items:
    component_coverage:
      - File count verification
      - Category coverage
      - Critical: PASS required
    
    pattern_consistency:
      - Update pattern applied
      - Timestamp accuracy
      - Critical: PASS required
    
    integration_validation:
      - Cross-reference integrity
      - Agent activation testing
      - Template inheritance
      - High: Should PASS
    
    quality_standards:
      - Documentation compliance
      - Cross-repository consistency
      - Medium: Address CONCERNS
```

### **Protocol Integration Requirements**
```yaml
new_protocol_integration:
  orchestrator_updates:
    - Add command to commands section
    - Add to help-display-template
    - Add to dependencies.engineering_rules
    - Add to orchestration_scenarios
  
  cross_references:
    - Primary: memory-rules.md
    - Add description and usage
    - Reference orchestrator command
  
  component_inventories:
    - Add to relevant lists
    - Update validation checklists
  
  testing:
    - Verify in *help output
    - Test accessibility
    - Validate cross-references
```

