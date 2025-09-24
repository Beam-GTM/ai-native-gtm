<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# File Management & Organization

## 📁 **FILE MANAGEMENT & ORGANIZATION**

### **File Placement Standards**

#### **Root Level Protection**
```yaml
root_protection:
  STRICTLY_PROHIBITED:
    - New dot directories (.*)
    - Temporary files
    - Implementation files
    - Any file not explicitly approved
    
  APPROVED_ROOT_FILES_ONLY:
    - AI-NAVIGATION-INDEX.md
    - CLAUDE.md
    - .gitignore
    - README.md
```

#### **Automatic Placement Validation**
```yaml
before_creating_any_file:
  step_1: "Ask: What IS this file?"
  step_2: "Determine location per decision tree"
  step_3: "Include location validation in header"
  step_4: "Create file in validated location"
  
never_do:
  - Create files at root without explicit approval
  - Create new categories without systematic analysis
  - Skip location validation header
  - Ignore existing patterns
```

### **Organization Patterns**

#### **Status-Based Organization**
```yaml
status_folders:
  planned/:
    purpose: "Future work being planned or designed"
    ai_behavior: "Help with planning and preparation"
    retention: "Move to active/ when implementation begins"
    
  active/:
    purpose: "Current work requiring attention"
    ai_behavior: "Prioritize these files first"
    retention: "Move to completed/ when done"
    
  completed/:
    purpose: "Finished work ready for use"
    ai_behavior: "Reference for context"
    retention: "Move to archived/ after 90 days"
    
  archived/:
    purpose: "Historical reference"
    ai_behavior: "Reference only if needed"
    retention: "Permanent with periodic cleanup"
```

#### **Automatic Folder Layering**
```yaml
large_directory_management:
  trigger_threshold: 15  # Files per directory
  
  layering_strategies:
    by_category:
      pattern: "{category}/{subcategory}/{files}"
      example: "agents/core/, agents/specialists/"
      
    by_date:
      pattern: "YYYY-MM/{files}"
      example: "completed/2025-01/, completed/2025-02/"
      
    by_status:
      pattern: "planned/, active/, completed/, archived/{files}"
      example: "features/ with mixed status files"

  auto_layering_rules:
    agents_folder:
      threshold: 12
      strategy: "by_category"
      categories: ["core", "specialists", "coordinators", "experimental"]
      
    features_folder:
      threshold: 10  
      strategy: "by_status"
      statuses: ["planned", "active", "completed", "archived"]
      
    completed_work:
      threshold: 8
      strategy: "by_date"
      pattern: "YYYY-MM/"
```

### **Intelligent File Cleanup Protocol**

#### **Cleanup Workflow**
```yaml
cleanup_workflow:
  phase_1_analysis:
    - Scan entire structure
    - Identify status indicators
    - Map cross-references
    - Analyze placement violations
    
  phase_2_planning:
    - Present reorganization plan
    - Get user approval
    - Calculate link impacts
    - Plan safe moves
    
  phase_3_execution:
    - Create backup first
    - Move files systematically
    - Update all references
    - Validate integrity
```

#### **Safe File Movement Strategy**
```yaml
before_moving_any_file:
  link_impact_analysis:
    - Scan codebase for references to file path
    - Identify markdown links, imports, file references
    - Calculate update impact scope
  
  dependency_chain_analysis:
    - Check agent activation sequences
    - Verify orchestrator command dependencies
    - Identify workflow integration points
  
  risk_assessment:
    HIGH_RISK: "Core agent files, orchestrator dependencies"
    MEDIUM_RISK: "Memory files with cross-references"
    LOW_RISK: "Isolated documentation without references"

file_movement_execution:
  1_backup: "Create snapshot of current state"
  2_collect: "Gather all file references"
  3_move: "Physically move file to new location"
  4_update: "Update all references to new path"
  5_validate: "Verify all links functional"
  6_cleanup: "Remove empty directories if appropriate"
```

#### **Link Integrity Preservation**
```yaml
link_types_to_detect:
  - Markdown relative: "[text](./path/file.md)"
  - Markdown absolute: "[text](/absolute/path/file.md)"
  - YAML references: "dependency_file: 'path/file.md'"
  - Import statements: "from path.file import something"
  - Include statements: "<!-- include: path/file.md -->"
  - Agent activation: "Read file references in activation"

update_strategies:
  relative_links: "Calculate new relative path from source"
  absolute_links: "Update absolute path to new location"
  yaml_references: "Update path values maintaining structure"
  cross_repository: "Preserve repository references"
  agent_activation: "Update dependency paths and workflows"
```

### **Cleanup Commands**
```yaml
available_commands:
  "*analyze-structure": "Analyze file organization health"
  "*cleanup-interactive": "Interactive cleanup with user control"
  "*safe-move [src] [dst]": "Move file with automatic link updates"
  "*validate-structure": "Validate against placement rules"
  "*check-links": "Verify all cross-references"
  "*emergency-restore": "Restore from backup if cleanup fails"
```

