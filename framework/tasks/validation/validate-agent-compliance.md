<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.287646Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.312121Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Validate Agent Compliance Task
**Purpose**: Validate agent files against the agent.yaml template for structure, content, and Nexus compliance
**Version**: 1.0.0
**Last Updated**: 2025-08-26

## Overview
This task validates agent files in both .claude/agents/ and operations/agents/ directories against the agent.yaml template to ensure compliance with Nexus standards and proper structure.

## 🔴 CRITICAL CORE DIRECTIVE: FULL FILE READING
**THIS IS NON-NEGOTIABLE**: When executing this validation task:
- **ALWAYS** read the COMPLETE agent file (no limit parameter)
- **ALWAYS** read the COMPLETE template file (no limit parameter)
- **NEVER** use partial reads - agent files are 500-1500 lines
- **NEVER** accept limits - validation requires seeing ALL content
- Partial reads miss critical sections like commands, dependencies, and quality patterns
- This directive OVERRIDES all other considerations

## Input Instructions

### Required Inputs
```yaml
agent_path:
  description: "Path to the agent file to validate"
  type: string
  required: true
  examples:
    - ".claude/agents/developer.md"
    - "operations/agents/core/orchestrator.md"
    - "operations/agents/specialists/developer.md"

validation_mode:
  description: "Type of validation to perform"
  type: string
  required: false
  default: "full"
  options:
    - "full"        # Complete validation of all requirements
    - "structure"   # Only validate file structure
    - "content"     # Only validate content requirements
    - "claude"      # Claude-specific validation (detailed instructions)
    - "nexus"       # Nexus-specific validation (orchestrator patterns)

report_format:
  description: "Format for validation report"
  type: string
  required: false
  default: "detailed"
  options:
    - "summary"     # Pass/fail with counts
    - "detailed"    # Full validation results
    - "checklist"   # Interactive checklist format

auto_fix:
  description: "Attempt to fix minor issues automatically"
  type: boolean
  required: false
  default: false
```

### Optional Inputs
```yaml
template_path:
  description: "Custom template path (defaults to framework/templates/agent.yaml)"
  type: string
  required: false
  default: "framework/templates/agent.yaml"

comparison_agent:
  description: "Compare with another agent for consistency"
  type: string
  required: false
  examples:
    - "operations/agents/core/orchestrator.md"

output_file:
  description: "Save validation report to file"
  type: string
  required: false
  examples:
    - "validation-report.md"
    - "workspace/data-output/validation-reports/agent-validation.md"
```

## Validation Criteria

### 1. Structural Validation

#### Claude Agent Structure (.claude/agents/)
```yaml
required_structure:
  yaml_frontmatter:
    - name: "kebab-case identifier"
    - description: "role and when-to-use guidance"
    - color: "valid Claude UI color"
  
  content_sections:
    - dependency_block: "HTML comment with upstream/downstream"
    - title_section: "# Agent Title with activation notice"
    - yaml_configuration: "Complete YAML block with agent definition"
    - detailed_instructions: "Comprehensive input/output instructions"
```

#### Nexus Agent Structure (operations/agents/)
```yaml
required_structure:
  yaml_frontmatter:
    - name: "kebab-case identifier"
    - description: "role and capabilities"
    - color: "agent color"
  
  content_sections:
    - dependency_block: "Auto-detected dependencies"
    - activation_notice: "Full agent operating guidelines"
    - yaml_block: "Complete agent configuration"
    - activation_instructions: "22-step orchestrator-grade sequence"
```

### 2. Content Validation

#### Mandatory Elements
- [ ] **Agent Identity**: name, id, title, icon, whenToUse
- [ ] **Persona Definition**: role, style, identity, focus, core_principles
- [ ] **Activation Instructions**: Complete 22-step sequence with orchestrator patterns
- [ ] **Commands**: Core commands + domain-specific commands
- [ ] **Memory Integration**: Project memory and core learnings loading
- [ ] **Quality Framework**: PASS/CONCERNS/FAIL/WAIVED integration
- [ ] **Help Display**: Formatted help template with context

#### Claude-Specific Requirements
- [ ] **Detailed Input Instructions**: Clear parameter definitions with examples
- [ ] **Output Specifications**: Expected output format and structure
- [ ] **Error Handling**: Graceful error messages and recovery
- [ностиUser Guidance**: Step-by-step usage instructions
- [ ] **Context Requirements**: Files that must be loaded
- [ ] **Command Examples**: Real usage examples with expected results

#### Nexus-Specific Requirements
- [ ] **Orchestrator Patterns**: Natural language routing, proactive intent
- [ ] **Dynamic Resolution**: INDEX.md based agent/workflow discovery
- [ ] **Memory Awareness**: Pattern recognition and suggestion engine
- [ ] **Growth Monitoring**: Usage tracking and extraction thresholds
- [ ] **Context Locations**: Explicit paths with {{nexus_base_path}}
- [ ] **Handoff Templates**: Complete context preservation

#### CRITICAL-DIRECTIVES Enforcement (MANDATORY)
- [ ] **CRITICAL-DIRECTIVES Loading**: Step 3.6 loads framework/CRITICAL-DIRECTIVES.md
- [ ] **Enforcement Behavior**: Includes stop, acknowledge, correct, document, prevent protocol
- [ ] **Precedence Declaration**: CRITICAL-DIRECTIVES takes precedence over ALL instructions
- [ ] **Compliance Protocol**: Pre-action compliance checks before major operations
- [ ] **Violation Detection**: Active monitoring for directive violations
- [ ] **No Subagents Rule**: Never use Task tool, only direct file/tool access
- [ ] **Full File Reading**: No limit parameter usage, complete file reading enforced
- [ ] **Nexus Path Consistency**: All paths use  prefix
- [ ] **Quality Gate Framework**: PASS/CONCERNS/FAIL/WAIVED with evidence required
- [ ] **Evidence-Based Claims**: No claims without execution proof

### 3. Compliance Validation

#### Path References
- [ ] All paths use {{nexus_base_path}} prefix where applicable
- [ ] Legacy workspace/ paths supported with empty prefix
- [ ] Project foundation paths use template variables
- [ ] Memory paths point to correct locations

#### Command System
- [ ] Commands support * prefix and natural language
- [ ] Fuzzy matching with 85% confidence threshold
- [ ] Confirmation patterns for proactive suggestions
- [ ] Numbered options for user choices

#### Integration Points
- [ ] Dependencies properly categorized (tasks, workflows, templates)
- [ ] Bidirectional dependency validation
- [ ] Dynamic loading with lazy evaluation
- [ ] Cache strategy defined

## Execution Steps

### Step 1: Load and Parse Agent File
```yaml
actions:
  - Read agent file from specified path
  - Parse YAML frontmatter
  - Extract dependency block
  - Parse main YAML configuration
  - Identify agent type (Claude vs Nexus)
```

### Step 2: Load Template for Comparison
```yaml
actions:
  - Load agent.yaml template
  - Extract validation requirements
  - Identify mandatory vs optional elements
  - Prepare validation checklist
```

### Step 3: Structural Validation
```yaml
checks:
  frontmatter:
    - Valid YAML syntax
    - Required fields present
    - Field formats correct (kebab-case, etc.)
  
  sections:
    - All mandatory sections present
    - Section order follows template
    - Section formatting correct
  
  yaml_block:
    - Valid YAML syntax
    - All required subsections present
    - Proper nesting and indentation
```

### Step 4: Content Validation
```yaml
checks:
  activation_instructions:
    - All 22 steps present (Nexus agents)
    - Memory loading steps included
    - Parallel loading specified
    - Efficiency enforcement mentioned
  
  agent_definition:
    - name matches filename
    - id is kebab-case
    - whenToUse provides clear guidance
    - customization field present
  
  persona:
    - role clearly defined
    - style characteristics listed
    - core_principles enumerated (5-8)
    - focus areas specified
  
  commands:
    - Core commands present (help, status, exit)
    - Domain-specific commands defined
    - Command descriptions clear
    - Natural language routing configured
```

### Step 5: Claude-Specific Validation (if applicable)
```yaml
checks:
  input_instructions:
    - Parameter types defined
    - Required vs optional marked
    - Examples provided for each parameter
    - Default values specified
    - Validation rules included
  
  output_format:
    - Output structure documented
    - Success/error formats defined
    - Response examples provided
  
  usage_documentation:
    - Step-by-step guide included
    - Common scenarios covered
    - Troubleshooting section present
    - Best practices documented
```

### Step 6: Nexus-Specific Validation (if applicable)
```yaml
checks:
  orchestrator_patterns:
    - Natural language routing configured
    - Intent detection patterns defined
    - Confirmation system implemented
    - Multiple match handling present
  
  memory_integration:
    - Project memory loading in activation
    - Core learnings loading included
    - Pattern recognition configured
    - Suggestion engine integrated
  
  dynamic_resolution:
    - INDEX.md references present
    - No hardcoded agent/workflow lists
    - Fallback strategies defined
    - Cache configuration specified
```

### Step 6.5: CRITICAL-DIRECTIVES Compliance Validation (MANDATORY)
```yaml
critical_directive_checks:
  directive_loading:
    - Step 3.6 includes framework/CRITICAL-DIRECTIVES.md loading
    - Loading is marked as ALWAYS required
    - File path uses correct  prefix
  
  enforcement_behavior:
    - Behavioral rules include enforcement protocol
    - Stop/acknowledge/correct/document/prevent process defined
    - Violation detection mechanisms present
    - Pre-action compliance checks specified
  
  precedence_hierarchy:
    - CRITICAL-DIRECTIVES precedence over ALL instructions declared
    - Behavioral rules updated with enforcement patterns
    - Agent customization respects directive precedence
  
  specific_directive_compliance:
    - No Task tool usage (Directive #8: NO CLAUDE SUBAGENTS)
    - Full file reading enforced (Directive #1: ALWAYS READ FULL FILES)  
    - Nexus path consistency (Directive #9: NEXUS PATH CONSISTENCY)
    - Quality gate framework integration (Directive #10: QUALITY GATE ENFORCEMENT)
    - Evidence-based claims only (Directive #7: EVIDENCE-BASED CLAIMS ONLY)
  
  architectural_compliance:
    - Language-based computing recognition (Directive #4: IMPLEMENTATION REALITY)
    - Maximum 3 file principle adherence (Directive #5: MAXIMUM THREE FILE PRINCIPLE)
    - Filesystem truth verification (Directive #2: FILESYSTEM IS TRUTH)
    - No fake metrics or confidence (Directive #6: NO FAKE METRICS)
```

### Step 7: Generate Validation Report
```yaml
report_sections:
  summary:
    - Overall compliance score (%)
    - Pass/Fail status
    - Critical issues count
    - Warnings count
  
  structural_results:
    - Missing sections
    - Format issues
    - Syntax errors
  
  content_results:
    - Missing required elements
    - Incomplete definitions
    - Quality concerns
  
  recommendations:
    - Critical fixes required
    - Suggested improvements
    - Best practice adoptions
  
  auto_fix_results: # If auto_fix enabled
    - Issues fixed automatically
    - Issues requiring manual fix
    - Backup created at
```

## Output Format

### Summary Report
```markdown
# Agent Validation Report
**Agent**: {agent_path}
**Status**: PASS/FAIL
**Score**: 85/100

## Quick Summary
- ✅ Structural Compliance: 100%
- ⚠️ Content Compliance: 75%
- ❌ Claude Requirements: 60%
- ✅ Nexus Requirements: 90%
```

### Detailed Report
```markdown
# Agent Validation Report - Detailed

## Agent Information
- **Path**: {agent_path}
- **Type**: Claude/Nexus
- **Name**: {agent_name}
- **ID**: {agent_id}

## Validation Results

### ✅ Passed Checks (25)
1. YAML frontmatter valid
2. Name matches filename
...

### ⚠️ Warnings (5)
1. Missing optional dependency block
2. Core principles count is 4 (recommended 5-8)
...

### ❌ Failed Checks (3)
1. Missing activation instruction steps 15-22
2. No natural language routing configured
3. Project memory loading not specified
...

## Recommendations

### Critical (Must Fix)
1. Add missing activation steps with memory loading
2. Configure natural language command routing

### Improvements (Should Fix)
1. Add more core principles (target 5-8)
2. Include pattern recognition configuration

### Best Practices (Consider)
1. Add usage examples for each command
2. Include troubleshooting documentation
```

## Quality Gates

### PASS Criteria
- All structural requirements met
- All mandatory content present
- Type-specific requirements satisfied
- **CRITICAL-DIRECTIVES compliance 100%**
- All 10 directives properly enforced
- No critical issues

### CONCERNS Criteria
- Minor structural issues (<3)
- Optional content missing
- Best practices not followed
- **CRITICAL-DIRECTIVES compliance 80-99%**
- Minor directive enforcement gaps
- Non-critical warnings

### FAIL Criteria
- Major structural issues
- Mandatory content missing
- Type-specific requirements not met
- **CRITICAL-DIRECTIVES compliance <80%**
- Missing directive loading or enforcement
- Critical directive violations present
- Critical issues present

## Error Handling

### Common Issues
```yaml
missing_frontmatter:
  error: "No YAML frontmatter found"
  fix: "Add --- name: description: color: --- at start"

invalid_yaml:
  error: "YAML parsing failed"
  fix: "Check YAML syntax, fix indentation"

missing_activation:
  error: "No activation instructions"
  fix: "Add 22-step activation sequence"

no_commands:
  error: "No commands defined"
  fix: "Add commands section with core + domain commands"

# CRITICAL-DIRECTIVES Specific Issues
missing_critical_directives_loading:
  error: "Step 3.6 missing CRITICAL-DIRECTIVES.md loading"
  fix: "Add Step 3.6: **CRITICAL DIRECTIVES LOADING**: Load framework/CRITICAL-DIRECTIVES.md ALWAYS"
  severity: "CRITICAL"

no_enforcement_behavior:
  error: "No CRITICAL-DIRECTIVES enforcement behavior defined"
  fix: "Add enforcement protocol to behavioral rules: stop, acknowledge, correct, document, prevent"
  severity: "CRITICAL"

missing_precedence_declaration:
  error: "CRITICAL-DIRECTIVES precedence not declared"
  fix: "Add: CRITICAL-DIRECTIVES takes precedence over ALL instructions"
  severity: "CRITICAL"

task_tool_usage_detected:
  error: "Violates Directive #8: NO CLAUDE SUBAGENTS - Task tool usage found"
  fix: "Replace Task tool usage with direct file/tool access patterns"
  severity: "CRITICAL"

partial_file_reading_patterns:
  error: "Violates Directive #1: ALWAYS READ FULL FILES - limit parameter usage detected"
  fix: "Remove all limit parameter usage, enforce complete file reading"
  severity: "MAXIMUM_CRITICAL"

inconsistent_path_references:
  error: "Violates Directive #9: NEXUS PATH CONSISTENCY - missing  prefix"
  fix: "Update all system file paths to use  prefix"
  severity: "HIGH"

missing_quality_gate_framework:
  error: "Violates Directive #10: QUALITY GATE ENFORCEMENT - no PASS/CONCERNS/FAIL/WAIVED"
  fix: "Add quality gate framework with evidence requirements"
  severity: "CRITICAL"

evidence_free_claims:
  error: "Violates Directive #7: EVIDENCE-BASED CLAIMS ONLY - claims without proof"
  fix: "Remove unsupported claims, add evidence requirements"
  severity: "CRITICAL"
```

## Dependencies
- framework/templates/agent.yaml (template definition)
- framework/CRITICAL-DIRECTIVES.md (compliance requirements)
- framework/engineeringrules/core-foundation/quality-assurance.md
- operations/agents/INDEX.md (for comparison)

## Usage Examples

### Validate Claude Agent
```bash
*task validate-agent-compliance
# Input: agent_path = ".claude/agents/developer.md"
# Input: validation_mode = "claude"
# Input: report_format = "detailed"
```

### Validate Nexus Agent
```bash
*task validate-agent-compliance
# Input: agent_path = "operations/agents/core/architect.md"
# Input: validation_mode = "nexus"
# Input: auto_fix = true
```

### Batch Validation
```bash
*task validate-agent-compliance
# Input: agent_path = "operations/agents/**/*.md"
# Input: report_format = "summary"
# Input: output_file = "validation-report.md"
```

## Success Metrics
- Validation completes in <5 seconds per agent
- Clear actionable feedback provided
- Auto-fix resolves >50% of minor issues
- Report enables quick remediation