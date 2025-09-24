<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.728673Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.258338Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Create Feature Checklist

**Category**: feature-management
**Complexity**: standard
**Prerequisites**: Feature definition completed, workspace directory exists

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
    - framework/engineeringrules/core-foundation/documentation-standards.md  # Documentation quality standards
    - framework/engineeringrules/core-foundation/quality-assurance.md       # Quality validation requirements
    - framework/engineeringrules/core-foundation/file-management.md         # File organization standards
    
  # CONDITIONALLY REQUIRED (loaded based on task context)
  contextual_rules:
    - condition: "Feature involves testing components"
      rule: framework/engineeringrules/development/testing-standards.md
      reason: "Testing checklist requirements"
    - condition: "Feature involves API development"
      rule: framework/engineeringrules/development/coding-standards.md
      reason: "API validation checklist items"
    - condition: "Feature involves UI components"
      rule: framework/engineeringrules/product-management/product-quality.md
      reason: "UI/UX validation requirements"
    
  # REPOSITORY-SPECIFIC (loaded based on implementation target)
  repository_specific:
    - repository: nexus-base
      rules: [framework/engineeringrules/system-operations/template-management.md]
      override_behavior: "enhance_with_system_specific"

rule_application_context:
  load_timing: "During task prerequisite validation phase"
  scope: "Apply throughout checklist generation and validation"
  inheritance: "Top-level rules + repository-specific overrides"
  validation: "All checklist items must align with loaded rules"
  conflict_resolution: "Repository-specific overrides top-level, user can waive"
```

### Rule Loading Strategy
```yaml
loading_strategy:
  phase_1_always_load:
    - framework/engineeringrules/core-foundation/documentation-standards.md: "Checklist documentation quality"
    - framework/engineeringrules/core-foundation/quality-assurance.md: "Validation requirements"
    - framework/engineeringrules/core-foundation/file-management.md: "Checklist file organization"
    
  phase_2_context_based:
    - if: "Feature type == 'backend' or 'fullstack'"
      load: framework/engineeringrules/development/testing-standards.md
      apply: "Backend testing checklist items"
    - if: "Feature type == 'frontend' or 'fullstack'"
      load: framework/engineeringrules/product-management/product-quality.md
      apply: "UI/UX validation items"
      
  phase_3_repository_specific:
    detection_method: "pwd analysis or workspace/memory/project-memory.md"
    loading_pattern: "load + merge + override"
    conflict_resolution: "repository_specific_wins"
```

## Prerequisites

**BEFORE STARTING THIS TASK:**

### Context Loading and Validation

**Context Loading Sequence:**
```yaml
context_loading_sequence:
  step_1_feature_context:
    location: "workspace/features/active/{feature-name}/"
    files: ["prd.md", "progress.md", "active-context.md"]
    validation: "Feature context files exist and contain feature definition"
  
  step_2_feature_inputs:
    location: "workspace/features/active/{feature-name}/"
    files: ["feature-definition-inputs.md", "technical-planning-inputs.md"]
    validation: "Planning inputs available with feature type and requirements"
  
  step_3_template_context:
    location: "framework/templates/features/"
    files: ["checklist.yaml"]
    validation: "Checklist template available for generation"
  
  step_4_context_consistency:
    validation_points:
      - "Feature name and type are defined"
      - "Success criteria are measurable"
      - "Technical components are identified"
      - "Quality requirements are specified"
```

**Context Update Triggers:**
```yaml
context_update_triggers:
  during_task_execution:
    - trigger: "checklist_items_identified"
      update: "workspace/features/active/{feature-name}/active-context.md"
      content: "Checklist creation progress, identified validation points"
    
    - trigger: "checklist_generated"
      update: "workspace/features/active/{feature-name}/progress.md"
      content: "Checklist created, validation requirements documented"
    
    - trigger: "quality_gate_passed"
      update: "workspace/features/active/{feature-name}/quality-gates.md"
      content: "Checklist quality validation status"
  
  post_task_completion:
    - update: "workspace/features/active/{feature-name}/feature-checklist.md"
      content: "Complete feature-specific checklist document"
    - update: "workspace/features/active/{feature-name}/active-context.md"
      content: "Checklist ready for use, next steps defined"
```

### Validation Requirements

**Pre-Execution Validation:**
- [ ] Load and review operations/checklists/quality-gate.md
- [ ] Validate feature context is complete
- [ ] Confirm engineering rules are loaded

**Quality Gates During Execution:**
- [ ] Checklist comprehensiveness validation
- [ ] Engineering rules alignment check
- [ ] User approval of checklist items

**Post-Execution Validation:**
- [ ] Execute checklist validation using generated checklist
- [ ] Update context files with checklist status
- [ ] Prepare handoff for feature implementation

### Engineering Rules Loading (MANDATORY)
- [ ] Load primary engineering rules for documentation and quality
- [ ] Detect feature type and load contextual rules
- [ ] Parse rule requirements for checklist items
- [ ] Resolve any rule conflicts
- [ ] Confirm rule application with user

### Required Inputs
- [ ] Feature name from workspace/features/active/{feature-name}/
- [ ] Feature type (frontend/backend/fullstack/integration)
- [ ] Success criteria from prd.md
- [ ] Technical components from technical-planning-inputs.md
- [ ] Quality requirements from quality-gates.md

### Required Agent State
- [ ] Agent has engineering rules loaded
- [ ] Agent understands feature context
- [ ] Agent has checklist template access
- [ ] Agent can generate comprehensive validation items

### Environmental Requirements
- [ ] User available for checklist approval
- [ ] Write access to feature workspace
- [ ] Access to framework/templates/features/checklist.yaml

**CRITICAL:** If feature context is incomplete, STOP and request resolution.

## Task Execution Workflow

### Step 1: Engineering Rules Loading & Validation

**Rule Loading Sequence:**

1. **Load Primary Rules** (Always Required)
   ```bash
   - Read framework/engineeringrules/core-foundation/documentation-standards.md
   - Parse documentation quality requirements
   - Read framework/engineeringrules/core-foundation/quality-assurance.md
   - Parse validation criteria
   - Read framework/engineeringrules/core-foundation/file-management.md
   - Parse organization standards
   ```

2. **Context-Based Rule Loading**
   ```yaml
   rule_loading_logic:
     backend_features:
       condition: "feature_type includes 'backend'"
       load: [testing-standards.md, coding-standards.md]
       apply_to: "Backend validation checklist items"
     frontend_features:
       condition: "feature_type includes 'frontend'"
       load: [product-quality.md, ux-standards.md]
       apply_to: "UI/UX validation checklist items"
     integration_features:
       condition: "feature_type == 'integration'"
       load: [system-design-rules.md, api-standards.md]
       apply_to: "Integration validation items"
   ```

3. **Repository-Specific Rule Loading**
   ```yaml
   repository_detection:
     current_repository: nexus-base
     additional_rules_path: framework/engineeringrules/system-operations/
     loading_pattern:
       - load: template-management.md
       - merge_with: top_level_rules  
       - priority: repository_overrides_top_level
   ```

**Engineering Rules Validation** 🔴

Present loaded rules summary to user:

**Loaded Engineering Rules:**
- ✅ **Documentation Standards**: Comprehensive documentation requirements
- ✅ **Quality Assurance**: Validation and testing requirements  
- ✅ **File Management**: Organization and structure standards
- ✅ **Feature-Specific Rules**: Based on feature type

**Rule Application Confirmation:**

1. **Apply all loaded rules** - Generate comprehensive checklist
2. **Focus on critical rules** - Priority validation items only
3. **Custom checklist scope** - User-defined validation points
4. **Add additional rules** - Load more specific standards
5. **Minimal compliance** - Essential validation only

**WAIT FOR USER RESPONSE** - Ensure rule application approach confirmed.

### Step 2: Feature Context Analysis

**Analyze Feature for Checklist Requirements:**

Based on loaded engineering rules and feature context:

**Current Feature Understanding:**
- **Feature Name**: {from workspace/features/active/{feature-name}/}
- **Feature Type**: {frontend/backend/fullstack/integration}
- **Success Criteria**: {from prd.md}
- **Technical Components**: {from technical-planning-inputs.md}
- **Quality Requirements**: {from quality-gates.md}
- **Risk Areas**: {from resource-planning-inputs.md}

**Checklist Scope Determination:**

1. **Functional Validation** - Core feature functionality works?
2. **Technical Validation** - Code quality and standards met?
3. **Integration Validation** - System integration points tested?
4. **Performance Validation** - Performance requirements met?
5. **Security Validation** - Security requirements addressed?
6. **Documentation Validation** - Documentation complete?
7. **User Experience Validation** - UX requirements satisfied?
8. **Deployment Validation** - Deployment readiness confirmed?
9. **Monitoring Validation** - Observability in place?

**MANDATORY:** Present checklist categories, wait for user confirmation.

### Step 3: Generate Feature Checklist

**Create Comprehensive Feature Checklist:**

Based on engineering rules and feature analysis:

```markdown
# Feature Checklist: {feature-name}
Generated: {timestamp}
Feature Type: {feature-type}
Compliance Framework: PASS/CONCERNS/FAIL/WAIVED

## Pre-Implementation Checklist
Based on framework/engineeringrules/core-foundation/documentation-standards.md:

### Planning & Design
- [ ] Feature PRD is complete and approved
- [ ] Success criteria are measurable and clear
- [ ] Technical approach is documented
- [ ] Dependencies are identified and available
- [ ] Risk mitigation strategies defined
- [ ] Timeline and milestones established

### Engineering Standards
- [ ] Coding standards documentation reviewed
- [ ] Testing strategy defined
- [ ] Code review process understood
- [ ] Documentation requirements clear
- [ ] Performance benchmarks established

## Implementation Checklist
Based on loaded engineering rules:

### Core Functionality
{Generate based on feature type and requirements}
- [ ] Primary use case implemented
- [ ] Edge cases handled
- [ ] Error scenarios addressed
- [ ] Input validation complete
- [ ] Output formatting correct

### Code Quality
Based on framework/engineeringrules/development/coding-standards.md:
- [ ] Code follows style guidelines
- [ ] Functions are properly documented
- [ ] Variable naming is consistent
- [ ] Code is DRY (Don't Repeat Yourself)
- [ ] Complexity is manageable

### Testing
Based on framework/engineeringrules/development/testing-standards.md:
- [ ] Unit tests written and passing
- [ ] Integration tests implemented
- [ ] Edge cases tested
- [ ] Performance tests completed
- [ ] Security tests passed

## Integration Checklist
{Generate based on integration points}

### API Integration (if applicable)
- [ ] API endpoints documented
- [ ] Authentication implemented
- [ ] Error responses standardized
- [ ] Rate limiting configured
- [ ] API versioning strategy defined

### Database Integration (if applicable)
- [ ] Schema changes documented
- [ ] Migrations tested
- [ ] Indexes optimized
- [ ] Backup strategy verified
- [ ] Data integrity maintained

### System Integration
- [ ] Dependencies validated
- [ ] Service communication tested
- [ ] Monitoring integrated
- [ ] Logging implemented
- [ ] Alerts configured

## Quality Assurance Checklist

### Functional Testing
- [ ] All acceptance criteria met
- [ ] User workflows validated
- [ ] Business logic verified
- [ ] Data processing accurate
- [ ] Results match expectations

### Non-Functional Testing
- [ ] Performance benchmarks met
- [ ] Security requirements satisfied
- [ ] Accessibility standards followed
- [ ] Browser/device compatibility tested
- [ ] Load testing completed

### Documentation
Based on framework/engineeringrules/core-foundation/documentation-standards.md:
- [ ] User documentation created
- [ ] API documentation complete
- [ ] Configuration guides written
- [ ] Troubleshooting guide prepared
- [ ] Release notes drafted

## Deployment Readiness Checklist

### Pre-Deployment
- [ ] Code reviewed and approved
- [ ] All tests passing
- [ ] Documentation complete
- [ ] Configuration verified
- [ ] Rollback plan prepared

### Deployment
- [ ] Deployment scripts tested
- [ ] Environment variables configured
- [ ] Secrets management verified
- [ ] Health checks implemented
- [ ] Smoke tests prepared

### Post-Deployment
- [ ] Monitoring active
- [ ] Alerts configured
- [ ] Performance baseline established
- [ ] User acceptance confirmed
- [ ] Knowledge transfer complete

## Sign-off Checklist

### Stakeholder Approval
- [ ] Product owner approval
- [ ] Technical lead approval
- [ ] QA sign-off
- [ ] Security review passed
- [ ] Compliance verified

### Final Validation
- [ ] All checklist items addressed
- [ ] Exceptions documented
- [ ] Risks accepted
- [ ] Handoff complete
- [ ] Feature ready for production

## Quality Gate Status
{To be completed during validation}

Gate: Feature Checklist Completeness
Status: {PASS/CONCERNS/FAIL/WAIVED}
Evidence: {checklist_items_completed}
Notes: {specific_validation_notes}
```

**SAVE TO:** workspace/features/active/{feature-name}/feature-checklist.md

### Step 4: Checklist Validation & Customization

**Review Generated Checklist with User:**

1. **Review completeness** - Are all validation areas covered?
2. **Add custom items** - Feature-specific validation points?
3. **Remove irrelevant items** - Not applicable sections?
4. **Adjust priority** - Critical vs nice-to-have items?
5. **Define thresholds** - Minimum compliance levels?

**WAIT FOR USER FEEDBACK** - Customize checklist as needed.

### Quality Gate: Checklist Comprehensiveness

**Compliance Assessment Framework:**

```yaml
compliance_assessment:
  checklist_coverage:
    rules_source: framework/engineeringrules/core-foundation/quality-assurance.md
    criteria: "All feature aspects have validation points"
    evidence_required: "Checklist sections mapped to requirements"
    assessment_method: "Coverage analysis"
    pass_threshold: "90% requirement coverage"
    
  engineering_alignment:
    rules_source: loaded engineering rules
    criteria: "Checklist items align with standards"
    evidence_required: "Rule-to-checklist mapping"
    assessment_method: "Compliance verification"
    pass_threshold: "All rules addressed"
```

**Detailed Compliance Check:**

#### Documentation Standards Compliance
**Criteria from documentation-standards.md:**
- Checklist is well-structured and clear
- All sections have descriptions
- Validation criteria are specific

**Evidence Collection:**
- [x] Checklist follows template structure
- [x] Items are actionable and measurable
- [x] Documentation requirements included

**Assessment**: {PASS/CONCERNS/FAIL/WAIVED}
**Evidence Summary**: Comprehensive checklist covering all feature aspects
**Compliance Notes**: Aligned with Nexus quality standards

**Engineering Rules Quality Decision** 🔴

Based on compliance assessment, select overall status:

1. **FULL COMPLIANCE** - Checklist comprehensive, proceed
2. **COMPLIANT with additions** - Add suggested improvements
3. **PARTIAL COMPLIANCE** - Address missing areas
4. **NEEDS REVISION** - Significant gaps to address
5. **WAIVED by User** - User accepts current state

**Context Update After Quality Gate:**
```yaml
post_quality_gate_context_update:
  location: "workspace/features/active/{feature-name}/quality-gates.md"
  content: |
    ## Quality Gate: Feature Checklist Creation - {timestamp}
    **Gate Status**: {PASS/CONCERNS/FAIL/WAIVED}
    **Checklist Coverage**: {coverage_percentage}
    **Engineering Rules Applied**: {rules_list}
    **Customizations Made**: {user_customizations}
    **Ready for Use**: {yes/no}
```

## Task Outputs with Engineering Rules Compliance

### Primary Deliverable
**Document Type**: Feature Validation Checklist
**Location**: workspace/features/active/{feature-name}/feature-checklist.md
**Format**: Markdown checklist with categories
**Engineering Rules Compliance**: Full compliance with quality standards

**Required Sections (Rule-Driven):**
```yaml
document_structure:
  sections:
    - pre_implementation:
        required: true
        rule_source: framework/engineeringrules/core-foundation/documentation-standards.md
        compliance_criteria: "Planning validation points defined"
        content_requirements: "PRD, design, standards checks"
        
    - implementation:
        required: true
        rule_source: framework/engineeringrules/development/coding-standards.md
        compliance_criteria: "Code quality validation defined"
        content_requirements: "Functionality, quality, testing checks"
        
    - integration:
        required: true
        rule_source: framework/engineeringrules/core-foundation/system-design-principles.md
        compliance_criteria: "Integration points validated"
        content_requirements: "API, database, system checks"
        
    - quality_assurance:
        required: true
        rule_source: framework/engineeringrules/core-foundation/quality-assurance.md
        compliance_criteria: "QA validation comprehensive"
        content_requirements: "Functional, non-functional, documentation"
        
    - deployment:
        required: true
        rule_source: framework/engineeringrules/system-operations/operations-governance.md
        compliance_criteria: "Deployment readiness validated"
        content_requirements: "Pre, during, post deployment checks"
```

### Engineering Rules Compliance Documentation
**Compliance Report**:
- **Rules Applied**: All loaded documentation and quality rules
- **Compliance Level**: {percentage} compliance achieved
- **Deviations**: Any waived or modified requirements
- **Justifications**: Reasons for any deviations
- **Future Actions**: Improvements for next iteration

### Secondary Deliverables
- **Checklist Coverage Report**: Mapping of requirements to checklist items
- **Customization Log**: User-requested modifications documented
- **Quality Gate Report**: Validation results and evidence

### Validation Checklist (Rule-Enhanced)
- [ ] All feature requirements have validation points
- [ ] Documentation standards met per documentation-standards.md
- [ ] Quality assurance standards met per quality-assurance.md
- [ ] Feature-specific rules addressed
- [ ] Checklist is actionable and measurable
- [ ] User has approved final checklist
- [ ] Context files updated with checklist status

### Context Handoff Preparation
**Task Completion Context Updates:**
```yaml
task_completion_context_handoff:
  primary_context_update:
    location: "workspace/features/active/{feature-name}/active-context.md"
    content: |
      ## Task Completion: Feature Checklist Created - {timestamp}
      **Completed Task**: create-feature-checklist
      **Final Status**: COMPLETED
      **Deliverables Created**: feature-checklist.md
      **Engineering Rules Compliance**: {compliance_status}
      **Checklist Items**: {total_items} validation points
      **Ready for Implementation**: Yes
      **Next Steps**: Use checklist during feature implementation
  
  progress_tracking_update:
    location: "workspace/features/active/{feature-name}/progress.md"
    content: |
      ## Progress Update: Checklist Created - {timestamp}
      **Task**: create-feature-checklist - COMPLETED
      **Deliverables**: feature-checklist.md with {total_items} items
      **Quality Status**: {quality_assessment}
      **Usage**: Ready for implementation validation
```

### Context Validation Checklist (Enhanced)
- [ ] Checklist document created and saved
- [ ] Context locations updated with results
- [ ] Progress tracking shows checklist ready
- [ ] Quality gates passed and documented
- [ ] Handoff context prepared for implementation team