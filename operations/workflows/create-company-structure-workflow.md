# Company Structure Creation Workflow

<!-- dependencies
upstream:
  # AUTO-DETECTED Agents (from sequence steps):
  - operations/agents/core/orchestrator.md  # Step: company_structure_creation
  
  # AUTO-DETECTED Tasks (from uses/executes):
  - framework/tasks/memory/update-project-memory.md  # Context updates
  
  # AUTO-DETECTED Engineering Rules:
  - framework/engineeringrules/core-foundation/file-management.md  # Applied in: folder_creation
  - framework/engineeringrules/core-foundation/system-design-principles.md  # Applied in: structure_design
  
downstream:
  # AUTO-DETECTED callers:
  - transcript-processing-automation  # Workflow dependency for company setup
  
validated: 2025-09-17T18:00:00Z
health: 100%
generator: framework/templates/workflow.yaml
-->

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: This workflow reads multiple files - never use limit parameter -->
<!-- This directive OVERRIDES token conservation - read files completely -->
<!-- VIOLATION = Missing critical workflow steps and validation processes -->

## 🔴 PRE-WORKFLOW DIRECTIVE CHECK + BEHAVIORAL CORRECTION
**MANDATORY**: Before executing this workflow, verify:
- [ ] All file reads will use complete files (no limit parameter)
- [ ] Agent file reads will capture complete operational instructions
- [ ] Task file reads will be comprehensive for proper execution
- [ ] Context file reads will provide complete workflow state

## 🧠 BEHAVIORAL CORRECTION PROTOCOL (Mental Model Framework)
**MANDATORY FIRST**: Apply behavioral pattern prevention before workflow execution:
{{load_behavioral_patterns: workflow_patterns}}
<!-- Loads: execution_documentation_paradox, false_completion_syndrome, basic_operations_failure -->

## Workflow Definition

```yaml
workflow:
  id: create-company-structure
  name: Company Folder Structure Creation
  description: >-
    Automated workflow for creating standardized company folder structures
    for the transcript processing automation system. Creates consistent
    organizational hierarchy for transcripts, emails, and documents.
  type: specialized
  project_types:
    - sales-automation
    - document-organization
    - company-onboarding
  complexity: low
  target_system: filesystem

context:
  situation: 'User identifies new company requiring folder structure for transcript processing'
  assumptions:
    - 'Company name provided by user'
    - 'Standard three-folder structure required'
    - 'Filesystem write access available'
  success_criteria:
    - 'Company folder created with proper naming'
    - 'Three sub-folders created: transcripts, emails, documents'
    - 'Structure validation completed'
    - 'Ready for transcript processing workflow'

# WORKFLOW SEQUENCE
sequence:
  - step: company_identification
    agent: orchestrator
    action: 'Collect and validate company name input'
    creates: company_name_validated
    requires: []
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Company name collection and validation:
      - Prompt user for company name
      - Apply naming conventions (remove special characters if needed)
      - Validate uniqueness (check if folder already exists)
      - Confirm name with user before proceeding
      
      SAVE OUTPUT: Validated company name for folder creation

  - step: folder_structure_creation
    agent: orchestrator
    action: 'Create standardized company folder structure'
    creates: company_folder_structure
    requires:
      - company_name_validated
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Folder structure creation:
      - Create Companies/{company-name}/ directory
      - Create Companies/{company-name}/transcripts/ subdirectory
      - Create Companies/{company-name}/emails/ subdirectory  
      - Create Companies/{company-name}/documents/ subdirectory
      - Verify all folders created successfully
      
      SAVE OUTPUT: Complete folder structure ready for use

  - step: structure_validation
    agent: orchestrator
    action: 'Validate folder structure and confirm readiness'
    creates: validation_complete
    requires:
      - company_folder_structure
    integrated_task: framework/tasks/memory/update-project-memory.md
    notes: |
      Structure validation:
      - Verify all three folders exist and are accessible
      - Check folder permissions are correct
      - Confirm structure matches standard template
      - Report successful creation to user
      
      SAVE OUTPUT: Validation confirmation and readiness status

# QUALITY GATES
quality_gates:
  - gate: company_name_valid
    trigger: 'after company_identification'
    criteria:
      - 'Company name is non-empty and valid'
      - 'No existing folder with same name'
      - 'Name follows naming conventions'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'company_name_validated'

  - gate: folder_structure_complete
    trigger: 'after folder_structure_creation'
    criteria:
      - 'All three folders created successfully'
      - 'Folder structure matches template'
      - 'No filesystem errors during creation'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'company_folder_structure'

  - gate: structure_validated
    trigger: 'after structure_validation'
    criteria:
      - 'All folders accessible and writable'
      - 'Structure ready for transcript processing'
      - 'No validation errors detected'
    validation_method: 'PASS/CONCERNS/FAIL/WAIVED'
    required_evidence:
      - 'validation_complete'

# HANDOFF PROTOCOL
handoff_protocol:
  to_transcript_processing:
    trigger: 'structure_validated gate PASSED'
    artifacts_provided:
      - company_name_validated
      - company_folder_structure
      - validation_complete
    
    handoff_message: |
      Company Structure Created - Ready for Transcript Processing
      
      Company: {company-name}
      Structure: Companies/{company-name}/transcripts/emails/documents/
      Status: Validated and ready
      
      Transcript processing can now proceed with:
      - Organized storage location ready
      - Standardized folder structure
      - Proper file organization foundation
      
      Next: Process transcripts using transcript-processing-automation

# FLOW DIAGRAM
flow_diagram: |
  ```mermaid
  graph TD
      A[Start: New Company Identified] --> B[Collect Company Name]
      B --> C{Name Valid?}
      
      C -->|Yes| D[Create Company Folder]
      C -->|No| E[Request Valid Name]
      E --> B
      
      D --> F[Create transcripts/ Subfolder]
      F --> G[Create emails/ Subfolder]
      G --> H[Create documents/ Subfolder]
      
      H --> I[Validate Structure]
      I --> J{Structure Valid?}
      
      J -->|Yes| K[Structure Ready]
      J -->|No| L[Fix Issues]
      L --> I
      
      K --> M[Ready for Transcript Processing]
      
      style M fill:#90EE90
      style A fill:#FFE4B5
      style I fill:#ADD8E6
      style J fill:#F0E68C
  ```

# RESOURCE MANAGEMENT
resource_management:
  required_inputs:
    - "company_name": "Name of company for folder creation"

  generated_artifacts:
    - "company_folder_structure": "Complete organized folder hierarchy"
    - "structure_validation": "Confirmation of successful creation"

  dependency_chain:
    - "Company name must be provided first"
    - "Folder creation depends on valid name"
    - "Validation depends on successful folder creation"

# ORCHESTRATION ENGINE
orchestration_engine:
  execution_mode: "automatic"

  automation_rules:
    - "Automatically proceed through steps when validation passes"
    - "Create folders immediately after name validation"
    - "Validate structure immediately after creation"
    - "Report success/failure status clearly"

  user_interaction_points:
    - company_name_input: "User provides company name"
    - validation_confirmation: "User confirms structure creation success"

  error_handling:
    - name_validation_failure: "Re-prompt for valid company name"
    - folder_creation_failure: "Report filesystem error and retry"
    - validation_failure: "Identify and fix structural issues"

# SUCCESS COMPLETION
completion_message: |
  🎯 Company Structure Created Successfully!
  
  Company: {company-name}
  Location: Companies/{company-name}/
  Folders: transcripts/ emails/ documents/
  
  ✅ Folder structure created and validated
  ✅ Ready for transcript processing
  ✅ Organized storage system established
  
  Next Steps:
  1. Process transcripts using transcript-processing-automation
  2. Generated emails will be stored in emails/ folder
  3. Related documents can be stored in documents/ folder
  
  Company onboarding complete!
```
