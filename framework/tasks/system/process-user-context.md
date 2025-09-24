# Process User Context Task

## 🎯 Purpose
Analyze user-provided context files, generate personalized project brief, and clean up input folder automatically.

## 📋 Task Overview

**Input**: Files in `briefing/context_input/`
**Output**: Personalized `briefing/project-brief.md` + archived context
**Cleanup**: Automatic context folder management

## 🔄 Processing Steps

### Phase 1: Context Discovery
```yaml
discovery:
  scan_folder: "briefing/context_input/"
  identify_files: "List all user-provided files"
  categorize_content:
    - requirements: "*.md, *.txt with requirements"
    - technical: "*.yaml, *.json, API specs"
    - business: "PRDs, business cases"
    - reference: "Examples, mockups, docs"
```

### Phase 2: Content Analysis
```yaml
analysis:
  extract_project_info:
    - project_type: "web app, API, mobile, etc."
    - technology_stack: "frameworks, languages, tools"
    - domain: "e-commerce, fintech, healthcare, etc."
    - complexity: "simple, medium, enterprise"
    - team_size: "solo, small team, large team"
    
  identify_requirements:
    - functional: "features, capabilities"
    - non_functional: "performance, security, scale"
    - constraints: "budget, timeline, platform"
    
  determine_patterns:
    - architecture_style: "microservices, monolith, serverless"
    - development_approach: "agile, waterfall, lean"
    - quality_level: "prototype, production, enterprise"
```

### Phase 3: Personalization Generation
```yaml
personalization:
  create_project_brief:
    template: "framework/templates/briefing/personalized-brief.yaml"
    populate_with: "analyzed context data"
    
  customize_agents:
    - select_relevant_agents: "based on project type"
    - configure_terminology: "domain-specific language"
    - set_default_workflows: "appropriate for project"
    
  generate_recommendations:
    - suggested_features: "based on project goals"
    - recommended_templates: "matching project patterns"
    - workflow_priorities: "aligned with development approach"
```

### Phase 4: Context Archival & Cleanup
```yaml
cleanup:
  create_archive:
    destination: "briefing/processed_context/"
    timestamp: "YYYY-MM-DD-HH-MM-SS"
    structure: |
      briefing/processed_context/
      └── context-YYYY-MM-DD-HH-MM-SS/
          ├── original_files/          # User's original files
          ├── analysis_report.md       # What we extracted
          ├── personalization_log.md   # What we customized
          └── archive_manifest.md      # Summary of processing
          
  move_files:
    from: "briefing/context_input/*"
    to: "briefing/processed_context/context-{timestamp}/original_files/"
    preserve: "original file structure and names"
    
  clean_input_folder:
    remove: "All user files (now archived)"
    keep: "README.md for next time"
    add: "SUCCESS-context-processed.md with summary"
```

### Phase 5: System Update
```yaml
system_update:
  update_project_brief:
    replace: "briefing/project-brief.md"
    with: "personalized version based on context"
    
  configure_agents:
    update: "operations/agents/*/context-awareness"
    with: "project-specific terminology and focus"
    
  customize_templates:
    priority: "templates matching user's project type"
    configure: "default values based on context"
    
  remove_template_indicators:
    delete: "TEMPLATE-INDICATORS.md"
    signal: "system is now personalized"
```

## 📊 Success Validation

### Required Outputs
- [x] `briefing/project-brief.md` - Personalized project brief
- [x] `briefing/processed_context/` - Archived original context
- [x] `briefing/context_input/SUCCESS-context-processed.md` - Processing summary
- [x] Updated agent configurations with domain awareness
- [x] Template indicators removed (system no longer "fresh")

### Quality Checks
```yaml
validation:
  project_brief_quality:
    - contains_project_name: true
    - identifies_technology_stack: true
    - describes_key_features: true
    - sets_development_approach: true
    
  context_preservation:
    - all_original_files_archived: true
    - analysis_report_generated: true
    - processing_log_complete: true
    
  system_personalization:
    - agents_have_domain_context: true
    - templates_configured_appropriately: true
    - workflows_prioritized_correctly: true
```

## 🎯 Processing Examples

### Example 1: E-commerce Project
```yaml
input_files:
  - "ecommerce-requirements.md"
  - "user-stories.txt"
  - "api-endpoints.yaml"
  
detected_context:
  project_type: "E-commerce Web Application"
  technology: "REST API + React Frontend"
  domain: "Online Retail"
  complexity: "Medium"
  
personalization:
  agents_prioritized: ["developer", "ux-expert", "architect"]
  templates_suggested: ["feature/user-auth", "feature/payment", "feature/catalog"]
  workflows_emphasized: ["plan-feature", "implement-feature", "quality-check"]
```

### Example 2: API Project
```yaml
input_files:
  - "api-specification.yaml"
  - "data-models.md"
  - "authentication-requirements.txt"
  
detected_context:
  project_type: "REST API Service"
  technology: "Node.js + Express"
  domain: "Backend Services"
  complexity: "Simple-Medium"
  
personalization:
  agents_prioritized: ["developer", "architect", "quality-assurance"]
  templates_suggested: ["api/endpoint", "api/auth", "api/testing"]
  workflows_emphasized: ["implement-feature", "api-testing", "deployment"]
```

## 🔄 Context Lifecycle

### Phase 1: Collection
- User drops files in `context_input/`
- System detects new content
- Triggers processing workflow

### Phase 2: Processing
- Content analysis and extraction
- Project brief generation
- System personalization

### Phase 3: Archival
- Original files moved to timestamped archive
- Processing reports generated
- Input folder cleaned for reuse

### Phase 4: Operational
- System operates with personalized context
- Original context available in archive
- Ready for additional context updates

## 🚨 Error Handling

### No Context Provided
```yaml
if_empty_folder:
  action: "Skip processing, keep template state"
  message: "No context provided, using default template"
  next_step: "Standard template setup"
```

### Invalid/Unreadable Files
```yaml
if_invalid_files:
  action: "Process readable files, note issues"
  create: "analysis_report.md with file processing status"
  continue: "with partial context analysis"
```

### Processing Failures
```yaml
if_processing_fails:
  action: "Preserve original files, log error"
  rollback: "Keep template state active"
  notify: "User of processing failure with details"
```

## 💡 Smart Features

### Incremental Processing
- Can process additional context later
- Merges new context with existing
- Updates personalization accordingly

### Context Suggestions
- Identifies missing information
- Suggests additional context to provide
- Guides user to better personalization

### Learning Integration
- Captures successful patterns
- Improves future context processing
- Builds template intelligence over time

## 🎯 Integration Points

### Triggers
- `onboarding-experience` feature calls this task
- `orchestrator` detects context and triggers processing
- Manual trigger via `@process-context` command

### Dependencies
- Requires `briefing/context_input/` folder
- Uses `framework/templates/briefing/` templates
- Integrates with agent configuration system

### Outputs Used By
- All agents (context-aware operations)
- Feature templates (personalized defaults)
- Workflow systems (appropriate prioritization)
- Menu systems (relevant suggestions)

---

**This task transforms a generic template into a personalized system that understands your specific project and domain.**