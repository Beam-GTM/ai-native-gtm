<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# File Management Standards

## 🔧 **FILE MANAGEMENT STANDARDS**

### **File Structure Analysis Patterns**

#### **Intelligent Root File Analysis**
```yaml
outdated_files_pattern:
  detection: Root files from completed phases
  analysis: Review features/ and checklists/ for status
  example: "NEXIS_IMPLEMENTATION.md" when complete
  decision: Archive, delete, or reorganize
  action: Present analysis, get approval

duplicate_documentation:
  detection: Multiple files covering same topic
  analysis: Content similarity and cross-reference
  example: Multiple READMEs with overlap
  decision: Consolidate, maintain, or archive
  action: Present options, get preference

legacy_system_files:
  detection: Files from previous versions
  analysis: Review history and architecture
  example: Old framework files
  decision: Archive, delete, or document
  action: Present analysis, get decision
```

#### **Logical Hierarchy Enhancement**
```yaml
flat_structure_improvement:
  detection: Directories with >15 files
  analysis: Content analysis and grouping
  example: agents/ with 15 files to group
  decision: Approve subdivision criteria
  action: Present suggestions, get preferences

topic_based_organization:
  detection: Files for better organization
  analysis: Content and relationship mapping
  example: Mixed implementation and reference
  decision: Choose organizational scheme
  action: Present options, get preference

progressive_complexity:
  detection: Materials without structure
  analysis: Complexity and journey mapping
  example: Advanced mixed with basics
  decision: Approve progressive organization
  action: Present paths, get approval
```

### **Intelligent Cleanup Algorithms**

#### **Safe File Movement Strategy**
```yaml
pre_move_analysis:
  link_impact:
    - Scan codebase for references
    - Identify markdown links and imports
    - Calculate update impact scope
  
  dependency_chain:
    - Check agent activation sequences
    - Verify orchestrator dependencies
    - Identify workflow integrations
  
  risk_assessment:
    HIGH: Core agent files, orchestrator
    MEDIUM: Memory files with references
    LOW: Isolated documentation
```

#### **Safe Move Protocol**
```yaml
file_movement_execution:
  1_backup: Create snapshot of current state
  2_collect: Gather all file references
  3_move: Physically move file to location
  4_update: Update all references to path
  5_validate: Verify all links functional
  6_cleanup: Remove empty directories
```

### **Link Integrity Preservation**

#### **Automatic Link Detection**
```yaml
link_types_to_detect:
  - Markdown relative: "[text](./path/file.md)"
  - Markdown absolute: "[text](/absolute/path/file.md)"
  - YAML references: "dependency_file: 'path/file.md'"
  - Import statements: "from path.file import something"
  - Include statements: "<!-- include: path/file.md -->"
  - Agent activation: Read file references
```

#### **Link Update Strategies**
```yaml
update_strategies:
  relative_links: Calculate new relative path
  absolute_links: Update absolute path
  yaml_references: Update maintaining structure
  cross_repository: Preserve repository references
  agent_activation: Update dependency paths
```

### **User-Guided Cleanup Workflows**

#### **Interactive Cleanup Process**
```yaml
analysis_phase:
  1_scanning: Recursively scan directories
  2_contextual: Review features and usage
  3_relevance: Determine if files needed
  4_hierarchy: Identify improvements
  5_planning: Present findings for decisions

execution_phase:
  1_present: Show findings with explanations
  2_decisions: Get approval for changes
  3_selective: Execute approved operations
  4_confirmation: Confirm each batch
  5_feedback: Show results and get approval
  6_abort: Allow stop and rollback
```

#### **Cleanup Commands**
```yaml
analysis_commands:
  "*analyze-structure": File relevance analysis
  "*structure-health": Check organization health
  "*cleanup-plan": Generate cleanup plan
  "*hierarchy-review": Analyze hierarchy improvements

execution_commands:
  "*cleanup-interactive": Interactive cleanup session
  "*safe-move [src] [dst]": Move with link updates
  "*batch-organize [category]": Organize category
  "*archive-outdated": Archive outdated files

validation_commands:
  "*validate-structure": Validate against rules
  "*check-links": Comprehensive link validation
  "*emergency-restore": Restore from backup
  "*backup-create": Create comprehensive backup
```

### **User Control Principles**
```yaml
before_operations:
  - User must explicitly approve plan
  - User chooses between suggested actions
  - User can modify or reject recommendations
  - User can abort and rollback

during_execution:
  - Each batch requires confirmation
  - User sees results before proceeding
  - User can adjust strategy
  - Emergency stop always available

after_operations:
  - User reviews all changes
  - User confirms satisfaction
  - User decides next steps
  - User can request selective rollback
```

