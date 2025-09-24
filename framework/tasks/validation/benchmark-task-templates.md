<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.260681Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.309918Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

<!-- dependencies
upstream:
  # AUTO-DETECTED Executable By (agents that can run this):
  - operations/agents/core/orchestrator.md  # Capability: task-coordination
  - operations/agents/specialists/quality-assurance.md  # Capability: validation-analysis
  - operations/agents/core/analyst.md  # Capability: requirements-analysis
  
  # AUTO-DETECTED Engineering Rules Applied:
  - framework/engineeringrules/core-foundation/quality-assurance.md  # Applied: PASS/CONCERNS/FAIL/WAIVED framework
  - framework/engineeringrules/core-foundation/system-design-principles.md  # Applied: validation-methodology
  
  # AUTO-DETECTED Templates/Resources Used:
  - framework/templates/task.yaml  # Purpose: benchmark-baseline
  - framework/tasks/INDEX.md  # Purpose: task-registry
  
downstream:
  # AUTO-DETECTED Dependencies (entities that use this task):
  # Pattern: 'task[s]?:\s*benchmark-task-templates|uses:\s*framework/tasks/benchmark-task-templates\.md'
  # Search: operations/workflows/**/*.md, framework/tasks/**/*.md, operations/agents/**/*.md
  # NOTE: Requires bidirectional validation scan to populate downstream dependencies
  
validated: 2025-08-26T23:30:00Z
health: 90%  # 90% - upstream complete, downstream requires scan
generator: framework/templates/task.yaml
-->

# Benchmark Task Templates

**Category**: validation
**Complexity**: standard
**Prerequisites**: Access to framework/tasks/ directory, task template file

## ⚠️ CRITICAL EXECUTION NOTICE ⚠️

### **THIS IS AN EXECUTABLE WORKFLOW - NOT REFERENCE MATERIAL**

When this task is invoked:

1. **MANDATORY ENGINEERING RULES LOADING** - Load all required engineering rules before execution
2. **HIERARCHY RESPECT** - Apply top-level rules, then repository-specific overrides  
3. **COMPLIANCE VALIDATION** - All outputs must comply with loaded engineering rules
4. **SEQUENTIAL EXECUTION** - Follow step-by-step workflow with user validation
5. **QUALITY GATE INTEGRATION** - Engineering rules compliance checked at each gate

**VIOLATION INDICATOR:** If you skip rule loading or bypass compliance validation, you have violated this workflow.

## Engineering Rules Integration

### Required Engineering Rules
```yaml
engineering_rules_required:
  # ALWAYS REQUIRED (loaded for every execution)
  primary_rules:
    - framework/engineeringrules/core-foundation/quality-assurance.md          # PASS/CONCERNS/FAIL/WAIVED framework
    - framework/engineeringrules/core-foundation/system-design-principles.md  # Validation methodology standards
  
  # CONDITIONALLY REQUIRED (loaded based on task context)
  contextual_rules:
    - condition: "template_modification_needed"
      rule: framework/engineeringrules/development/coding-rules.md
      reason: "Standards for template improvement recommendations"
    - condition: "documentation_gaps_found"
      rule: framework/engineeringrules/core-foundation/documentation-rules.md
      reason: "Documentation quality standards"
  
  # REPOSITORY-SPECIFIC (loaded based on implementation target)
  repository_specific:
    - repository: "nexus-system"
      rules: ["framework/engineeringrules/system-operations/architecture-operations.md"]
      override_behavior: "nexus_validation_patterns"

rule_application_context:
  load_timing: "During task prerequisite validation phase"
  scope: "Apply throughout task execution and quality gates"
  inheritance: "Top-level rules + repository-specific overrides"
  validation: "All task outputs must comply with loaded rules"
  conflict_resolution: "Repository-specific overrides top-level, user can waive"
```

## Prerequisites

**BEFORE STARTING THIS TASK:**

### Context Loading and Validation

**Context Loading Sequence:**
```yaml
context_loading_sequence:
  step_1_task_template_context:
    location: "framework/templates/task.yaml"
    validation: "Template file accessible and contains current structure requirements"
  
  step_2_task_repository:
    location: "framework/tasks/**/*.md"
    files: "All existing task files for comparison analysis"
    validation: "Task files accessible and properly structured"
  
  step_3_quality_context:
    location: "framework/engineeringrules/core-foundation/quality-assurance.md"
    validation: "Quality standards accessible for benchmark criteria"
    
  step_4_context_consistency:
    validation_points:
      - "Template structure aligns with current engineering rules"
      - "Recent tasks follow expected patterns"
      - "No conflicts between template and actual implementations"
      - "All task categories represented in scan"
```

### Engineering Rules Loading (MANDATORY)
- [ ] Load primary engineering rules: quality-assurance.md, system-design-principles.md
- [ ] Detect repository context and load repository-specific rules
- [ ] Parse rule requirements and quality standards
- [ ] Resolve any rule conflicts using hierarchy precedence
- [ ] Confirm rule application approach with user

### Required Inputs
- [ ] Project context loaded from framework/templates/task.yaml
- [ ] Access to framework/tasks/ directory structure
- [ ] Current task template structure definition
- [ ] Quality assessment criteria from engineering rules

### Required Agent State
- [ ] Agent has engineering rules loaded and parsed
- [ ] Agent understands current repository context
- [ ] Agent has quality standards defined from rules
- [ ] Agent can validate compliance throughout execution

**CRITICAL:** If engineering rules cannot be loaded or parsed, STOP and request resolution.

## Task Execution Workflow

### Step 1: Engineering Rules Loading & Validation

**Rule Loading Sequence:**

1. **Load Primary Rules** (Always Required)
   ```bash
   - Read framework/engineeringrules/core-foundation/quality-assurance.md
   - Parse PASS/CONCERNS/FAIL/WAIVED framework standards
   - Read framework/engineeringrules/core-foundation/system-design-principles.md  
   - Parse validation methodology requirements
   ```

2. **Context-Based Rule Loading**
   ```yaml
   rule_loading_logic:
     if_template_improvements_needed:
       condition: "benchmarking reveals template gaps"
       load: ["framework/engineeringrules/development/coding-rules.md"]
       apply_to: "template enhancement recommendations"
     if_documentation_issues_found:
       condition: "tasks missing required documentation"
       load: ["framework/engineeringrules/core-foundation/documentation-rules.md"]
       apply_to: "documentation quality assessment"
   ```

**Engineering Rules Validation** 🔴

Present loaded rules summary to user:

**Loaded Engineering Rules:**
- ✅ **Quality Assurance**: PASS/CONCERNS/FAIL/WAIVED framework for all assessments
- ✅ **System Design**: Validation methodology and benchmark criteria standards

**Rule Application Confirmation:**

1. **Apply all loaded rules** - Use all standards throughout benchmarking
2. **Focus on quality gates** - Emphasize PASS/CONCERNS/FAIL/WAIVED framework
3. **Template compliance** - Prioritize template structure validation
4. **Evidence-based assessment** - Require proof for all benchmark claims
5. **Systematic methodology** - Follow structured validation approach

**WAIT FOR USER RESPONSE** - Ensure rule application approach confirmed.

### Step 2: Task Template Analysis

**Template Baseline Establishment:**

Load and analyze the official task template:

```yaml
template_analysis:
  source_file: "framework/templates/task.yaml"
  extraction_focus:
    - Required structural elements
    - Mandatory content sections
    - Engineering rules integration patterns
    - Quality gate specifications
    - Context management requirements
    - Dependency declaration formats
```

**Template Structure Mapping:**
- [ ] **Dependency Block**: Auto-generated upstream/downstream patterns
- [ ] **Header Section**: Title, category, complexity, prerequisites
- [ ] **Critical Execution Notice**: Workflow execution guidance
- [ ] **Engineering Rules Integration**: Rule loading and application
- [ ] **Prerequisites Section**: Context loading and validation
- [ ] **Execution Workflow**: Step-by-step implementation
- [ ] **Quality Gates**: PASS/CONCERNS/FAIL/WAIVED integration
- [ ] **Output Specification**: Deliverable requirements

### Step 3: Recent Task Inventory

**Task Discovery and Categorization:**

```yaml
task_scanning:
  scan_location: "framework/tasks/**/*.md"
  categorization:
    by_creation_date: "Last 30 days = recent"
    by_category: "memory, validation, system, session, feature, analysis"
    by_complexity: "simple, standard, complex"
  focus_criteria:
    - Tasks created in last 30 days
    - Tasks modified recently  
    - Tasks with new patterns or structures
```

**Recent Task Identification:**
Scan for tasks created or significantly modified in the last 30 days based on:
- File modification timestamps
- Internal version/date metadata
- Git commit history (if available)
- Content analysis for new patterns

### Step 4: Benchmark Analysis Execution

**Structural Compliance Assessment:**

For each recent task, evaluate against template:

```yaml
structural_benchmarking:
  dependency_block_analysis:
    criteria: "Presence of <!-- dependencies --> block"
    validation: "Auto-detected patterns present"
    scoring: "PASS/CONCERNS/FAIL/WAIVED"
    
  header_compliance:
    criteria: "Category, complexity, prerequisites present"
    validation: "Format matches template specification"
    scoring: "PASS/CONCERNS/FAIL/WAIVED"
    
  critical_execution_notice:
    criteria: "Workflow execution guidance included"
    validation: "Engineering rules integration referenced"
    scoring: "PASS/CONCERNS/FAIL/WAIVED"
    
  engineering_rules_integration:
    criteria: "Required rules section present"
    validation: "Rule loading sequence defined"
    scoring: "PASS/CONCERNS/FAIL/WAIVED"
```

**Content Quality Assessment:**

```yaml
content_benchmarking:
  prerequisites_completeness:
    criteria: "Context loading sequence defined"
    validation: "Validation requirements specified"
    evidence_required: "Checklist format present"
    
  workflow_clarity:
    criteria: "Step-by-step execution defined"
    validation: "Quality gates integrated at checkpoints"
    evidence_required: "User confirmation points included"
    
  output_specification:
    criteria: "Deliverable format and validation defined"
    validation: "Engineering rules compliance documented"
    evidence_required: "Success criteria measurable"
```

### Step 5: Gap Analysis and Scoring

**Compliance Scoring System:**

```yaml
scoring_methodology:
  structural_score:
    weight: 40
    components:
      - dependency_block: 10
      - header_compliance: 10
      - execution_notice: 10
      - rules_integration: 10
      
  content_score:
    weight: 40
    components:
      - prerequisites: 15
      - workflow_clarity: 15  
      - output_spec: 10
      
  quality_score:
    weight: 20
    components:
      - engineering_compliance: 10
      - evidence_requirements: 10
```

**Gap Identification:**
- [ ] Missing structural elements
- [ ] Incomplete engineering rules integration
- [ ] Absent quality gate frameworks
- [ ] Poor context management
- [ ] Inadequate prerequisite validation

### Step 6: Benchmark Report Generation

**Report Structure:**

```markdown
# Task Template Benchmarking Report
**Analysis Date**: {timestamp}
**Tasks Analyzed**: {count}
**Template Version**: {version}

## Executive Summary
- **Overall Compliance**: {percentage}%
- **Structural Compliance**: {structural_score}%
- **Content Quality**: {content_score}%
- **Engineering Rules Integration**: {rules_score}%

## Detailed Analysis

### Recent Tasks Performance
{task_by_task_breakdown}

### Pattern Analysis
{compliance_patterns_identified}

### Gap Analysis
{critical_gaps_and_recommendations}
```

## Quality Gates

### Quality Gate: Template Compliance Assessment

**Compliance Assessment Framework:**

```yaml
compliance_assessment:
  structural_compliance:
    rules_source: framework/templates/task.yaml
    criteria: ["dependency_block", "header_format", "execution_notice", "rules_integration"]
    evidence_required: ["file_structure_analysis", "template_comparison"]
    assessment_method: "systematic_comparison"
    pass_threshold: "80% structural elements present"
    
  content_compliance:
    rules_source: framework/engineeringrules/core-foundation/quality-assurance.md
    criteria: ["prerequisites_completeness", "workflow_clarity", "output_specification"]
    evidence_required: ["content_analysis", "quality_gate_presence"]
    assessment_method: "qualitative_assessment"
    pass_threshold: "All mandatory content sections present"
```

**Engineering Rules Quality Decision** 🔴

Based on compliance assessment, select overall status:

1. **FULL COMPLIANCE** - Recent tasks meet template standards, template is effective
2. **MINOR GAPS** - Small deviations found, template guidance needs clarification  
3. **SIGNIFICANT GAPS** - Multiple tasks missing key elements, template needs enhancement
4. **MAJOR NON-COMPLIANCE** - Template not being followed, enforcement needed
5. **TEMPLATE INADEQUATE** - Template itself needs revision based on task evolution
6. **INCONSISTENT APPLICATION** - Template good but inconsistently applied
7. **EVOLUTION MISMATCH** - Tasks evolved beyond template, update needed
8. **TRAINING REQUIRED** - Template fine, education about proper usage needed

## Task Outputs

### Primary Deliverable
**Document Type**: Benchmarking Analysis Report
**Location**: workspace/data-output/validation-reports/task-template-benchmark-{date}.md
**Format**: Structured markdown with YAML metadata
**Engineering Rules Compliance**: Full compliance with quality-assurance.md standards

**Required Sections:**
- Executive summary with compliance percentages
- Task-by-task detailed analysis
- Pattern identification and trend analysis
- Gap analysis with specific recommendations
- Template improvement suggestions (if needed)
- Implementation priority rankings

### Engineering Rules Compliance Documentation
**Compliance Report**:
- **Rules Applied**: quality-assurance.md, system-design-principles.md
- **Compliance Level**: Full compliance (100%)
- **Assessment Method**: PASS/CONCERNS/FAIL/WAIVED framework
- **Evidence Collection**: Structural and content analysis with examples
- **Quality Gates**: All benchmarking criteria validated

### Secondary Deliverables
- **Template Gap Analysis**: Specific template improvement recommendations
- **Task Author Guidance**: Best practices for future task creation
- **Compliance Checklist**: Quick reference for task authors
- **Trend Analysis**: Patterns in task evolution and compliance

### Validation Checklist
- [ ] All recent tasks identified and analyzed
- [ ] Template comparison completed systematically
- [ ] Compliance scoring applied consistently
- [ ] Gap analysis includes specific recommendations
- [ ] Engineering rules compliance documented
- [ ] Report format follows quality standards
- [ ] Evidence collected for all assessments
- [ ] Actionable next steps provided

## Success Criteria
- Comprehensive analysis of all recent tasks (created/modified in last 30 days)
- Clear compliance percentage with supporting evidence
- Specific gap identification with remediation recommendations
- Template effectiveness assessment with improvement suggestions
- Actionable benchmarking framework for future use

## Error Handling

### Missing Template File
- Attempt to locate alternative template sources
- Document template absence as critical finding
- Proceed with best-practice baseline if possible

### Inaccessible Task Files
- Log specific files that cannot be accessed
- Continue with available tasks
- Note limitations in final report

### Scoring Inconsistencies
- Document scoring methodology clearly
- Provide examples for each score level
- Allow manual override with justification

## Integration Points
- **Quality Assurance Workflow**: Provides systematic validation of task quality
- **Template Management**: Feeds back into template improvement process
- **Task Creation Training**: Identifies common gaps for educational focus
- **System Maintenance**: Ensures task ecosystem health and consistency

---
**Status**: READY FOR EXECUTION
**Estimated Duration**: 30-45 minutes
**Output Size**: 2000-4000 words
**Quality Level**: Production-ready analysis