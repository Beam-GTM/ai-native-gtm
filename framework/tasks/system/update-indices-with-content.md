<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.230451Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.305666Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Update Indices with Content Verification

<!-- 🔴 DIRECTIVE #1 ENFORCEMENT: ALWAYS READ COMPLETE FILES -->
<!-- CRITICAL: This task reads many files for content extraction - never use limit parameter -->
<!-- This directive OVERRIDES token conservation - read files completely -->
<!-- VIOLATION = Missing critical file content for accurate index generation -->

## 🔴 PRE-EXECUTION DIRECTIVE CHECK
**MANDATORY**: Before executing this task, verify:
- [ ] All file reads will use complete files (no limit parameter)
- [ ] Content extraction will read complete file headers and descriptions
- [ ] Dependency analysis will scan complete file contents
- [ ] Index updates will be based on comprehensive file analysis

**Task ID**: update-indices-with-content  
**Category**: system-maintenance  
**Priority**: CRITICAL  
**Type**: Content-aware index generation  
**Dependencies**: Read tool, pattern matching

## Purpose
Generate accurate INDEX files by reading actual file content and extracting metadata, not just counting files. This ensures indices reflect reality, not assumptions.

## Problem Statement
Current index updates only count files without reading their content. This leads to:
- Missing metadata (descriptions, status, priority)
- Incorrect categorization
- No validation of file internals
- Assumptions about file purpose

## Solution Approach
Read each file's header/frontmatter to extract actual metadata and build indices from real content.

## 🆕 BIDIRECTIONAL DEPENDENCY BLOCKS

### Standard Dependency Block Format
```markdown
<!-- dependencies
upstream:
  - path/to/file-i-depend-on.md
  - path/to/another-dependency.yaml
downstream:
  - path/to/file-that-depends-on-me.md
  - path/to/another-consumer.md
validated: 2025-08-26T12:00:00Z
health: 95%
-->
```

### Extraction and Validation
```yaml
dependency_extraction:
  block_pattern: "<!-- dependencies([\\s\\S]*?)-->"
  content_patterns:
    agent_tasks: "task[s]?:\\s*([\\w/-]+\\.md)"
    agent_workflows: "workflow[s]?:\\s*([\\w/-]+\\.md)"
    workflow_agents: "agent[s]?:\\s*([\\w/-]+)"
    workflow_tasks: "uses:\\s*([\\w/-]+\\.md)"
    task_references: "executed_by:\\s*([\\w/-]+)"
    
bidirectional_validation:
  for_each_upstream_reference:
    - Verify file exists
    - Check we're in their downstream list
    - Auto-add if missing
    
  for_each_downstream_reference:
    - Verify file exists  
    - Check we're in their upstream list
    - Auto-add if missing
```

## Metadata Extraction Patterns

### Agent Files
```yaml
agent_metadata:
  location: "First 5 lines or YAML frontmatter"
  fields_to_extract:
    - name: (from frontmatter or # Agent Name)
    - description: (from frontmatter or first paragraph)
    - category: (from directory: core|specialists|coordinators|experimental)
    - whenToUse: (from YAML block if present)
    - dependencies: (from dependencies section)
```

### Workflow Files
```yaml
workflow_metadata:
  location: "Header section"
  fields_to_extract:
    - workflow_id: **Workflow ID**: {value}
    - category: **Category**: {value}
    - priority: **Priority**: {value}
    - type: **Type**: {value}
    - purpose: From ## Purpose section
```

### Task Files  
```yaml
task_metadata:
  location: "Header section"
  fields_to_extract:
    - task_id: **Task ID**: {value}
    - category: **Category**: {value}
    - priority: **Priority**: {value}
    - execution: **Execution**: {value}
    - purpose: From ## Purpose section
```

### Feature Files (PRD)
```yaml
feature_metadata:
  location: "PRD header"
  fields_to_extract:
    - feature_id: **Feature ID**: {value}
    - priority: **Priority**: {value}
    - owner: **Owner**: {value}
    - created: **Created**: {value}
    - status: From progress.md if exists
    - progress: From progress.md "Overall Progress: X%"
```

## Execution Steps

### Step 1: Discovery Phase
```yaml
discovery:
  agents:
    - Find all .md files in operations/agents/*/
    - Group by category directory
    
  workflows:
    - Find all .md files in operations/workflows/
    - Find all .md files in framework/workflows/
    
  tasks:
    - Find all .md files in framework/tasks/
    - Find all .md files in operations/tasks/ (if any)
    
  features:
    - Find all directories in workspace/features/active/
    - Find all directories in workspace/features/completed/
```

### Step 2: Content Reading Phase with Dependency Extraction
```yaml
# CRITICAL: Check file size FIRST, then read appropriately
# NEW: Extract and validate dependency blocks

for_each_agent:
  1. Check file size: wc -l {file}
  2. If <=200 lines: Read ENTIRE file (no limit)
  3. If >200 lines: Read first 100 lines for metadata
  4. Extract YAML frontmatter if present
  5. Extract name from frontmatter OR filename
  6. Extract description from frontmatter OR first paragraph
  7. Extract dependency block OR generate from content patterns
  8. Validate bidirectional references
  9. Store metadata and dependencies in structure

for_each_workflow:
  1. Check file size: wc -l {file}
  2. If <=500 lines: Read ENTIRE file (no limit)
  3. If >500 lines: Read first 150 lines (workflows can be 800+ lines)
  4. Extract Workflow ID from **Workflow ID**: line
  5. Extract Category, Priority, Type
  6. Extract Purpose section
  7. Extract/generate dependency block
  8. Validate bidirectional references
  9. Validate ID matches filename

for_each_task:
  1. Check file size: wc -l {file}
  2. If <=300 lines: Read ENTIRE file (no limit)
  3. If >300 lines: Read first 100 lines
  4. Extract Task ID from **Task ID**: line  
  5. Extract Category, Priority, Execution
  6. Extract Purpose section
  7. Extract/generate dependency block
  8. Validate bidirectional references
  9. Store in category groups

for_each_feature:
  1. Check prd.md size: wc -l prd.md
  2. Read appropriately (usually entire file <200 lines)
  3. Extract Feature ID, Priority, Owner
  4. Check progress.md size and read appropriately
  5. Extract current progress percentage
  6. Determine status from progress

NEVER USE ARBITRARY LIMITS LIKE 20 OR 30 LINES!
```

### Step 2.5: Bidirectional Dependency Validation (NEW - CRITICAL)
```yaml
action: VALIDATE_AND_FIX_BIDIRECTIONAL
for_each_file_with_dependencies:
  deps = extract_dependency_block(file)
  
  # Check upstream references
  for upstream in deps.upstream:
    if not exists(upstream):
      log_error("Broken reference: {file} -> {upstream}")
      comment_out_reference(file, upstream)
    else:
      upstream_deps = extract_dependency_block(upstream)
      if file not in upstream_deps.downstream:
        log_warning("Missing backlink in {upstream}")
        add_to_downstream(upstream, file)
        
  # Check downstream references
  for downstream in deps.downstream:
    if not exists(downstream):
      log_error("Broken downstream: {file} <- {downstream}")
      remove_from_downstream(file, downstream)
    else:
      downstream_deps = extract_dependency_block(downstream)
      if file not in downstream_deps.upstream:
        log_warning("Missing forward link in {downstream}")
        add_to_upstream(downstream, file)
        
  # Update health score
  health = calculate_health(deps)
  update_dependency_block(file, deps, health)
```

### Step 3: Index Generation Phase
```yaml
agent_index_structure:
  metadata:
    total_count: {actual_count}
    last_updated: {timestamp}
    
  categories:
    core:
      count: {count}
      agents:
        - name: {from_content}
          file: {filename}
          description: {from_content}
          dependencies: {extracted_deps}
          health: {dependency_health}
          
    specialists:
      count: {count}
      agents: [...]
      
workflow_index_structure:
  metadata:
    total_count: {actual_count}
    sources:
      operations: {count}
      framework: {count}
      
  workflows:
    - id: {from_content}
      name: {from_content}
      category: {from_content}
      priority: {from_content}
      file: {path}
      purpose: {from_content}
      dependencies: {extracted_deps}
      bidirectional_valid: {true/false}
      
feature_index_structure:
  active:
    - feature_id: {from_prd}
      name: {directory_name}
      priority: {from_prd}
      status: {from_progress}
      progress: {from_progress}
      owner: {from_prd}
      path: {directory_path}
      description: {from_prd_summary}
```

### Step 4: Validation Phase with Dependency Checks
```yaml
validation_checks:
  dependency_validation:
    - All files have dependency blocks
    - All dependencies bidirectional
    - No circular dependencies detected
    - Health scores above 90%
    
  id_filename_match:
    - Workflow ID matches filename
    - Task ID matches filename  
    - Feature ID consistent across files
    
  required_fields:
    - All agents have name and description
    - All workflows have ID and purpose
    - All tasks have ID and category
    - All features have ID and priority
    
  cross_reference:
    - Referenced dependencies exist
    - Categories are valid
    - Paths are correct
```

### Step 5: Comparison & Update
```yaml
comparison:
  1. Load existing INDEX.md
  2. Compare with generated index
  3. Identify differences:
     - Added items
     - Removed items
     - Changed metadata
  4. Generate change report

update_strategy:
  preserve:
    - User comments
    - Manual annotations
    - Custom sections
    
  replace:
    - Counts
    - Metadata from files
    - Timestamps
    - Generated sections
```

## Implementation Example

### Reading Agent Metadata
```python
# Pseudo-code for clarity
def extract_agent_metadata(filepath):
    content = read_file(filepath, limit=20)
    
    # Check for YAML frontmatter
    if content.startswith('---'):
        frontmatter = extract_yaml_block(content)
        name = frontmatter.get('name', filename_without_ext)
        description = frontmatter.get('description', '')
    else:
        # Extract from markdown
        name = extract_after_pattern(content, '# ')
        description = extract_first_paragraph(content)
    
    return {
        'name': name,
        'description': description,
        'category': parent_directory_name,
        'file': filepath
    }
```

### Reading Feature Metadata
```python
def extract_feature_metadata(feature_dir):
    # Read PRD
    prd_content = read_file(f"{feature_dir}/prd.md", limit=30)
    feature_id = extract_after_pattern(prd_content, '**Feature ID**: ')
    priority = extract_after_pattern(prd_content, '**Priority**: ')
    owner = extract_after_pattern(prd_content, '**Owner**: ')
    
    # Read progress if exists
    if file_exists(f"{feature_dir}/progress.md"):
        progress_content = read_file(f"{feature_dir}/progress.md", limit=20)
        progress = extract_after_pattern(progress_content, 'Overall Progress: ')
        status = determine_status_from_progress(progress)
    else:
        progress = 0
        status = 'planned'
    
    return {
        'feature_id': feature_id,
        'name': directory_name,
        'priority': priority,
        'status': status,
        'progress': progress,
        'owner': owner,
        'path': feature_dir
    }
```

## Error Handling

### File Read Errors
- Log and skip file
- Add to error report
- Continue with remaining files

### Missing Metadata
- Use sensible defaults
- Flag for manual review
- Document in report

### Malformed Content
- Attempt recovery with fallback patterns
- Log issue for investigation
- Use filename as last resort

## Performance Considerations

### Batch Reading
- Read files in batches of 10
- Use parallel reads where possible
- Cache read content for reuse

### Incremental Updates
- Track file modification times
- Only re-read changed files
- Maintain metadata cache

## Success Criteria
- [ ] All indices reflect actual file content
- [ ] No assumptions about file metadata
- [ ] Validation passes for all entries
- [ ] Change report shows accurate updates
- [ ] Performance within 30 seconds

## Usage
```bash
# Full update with content reading
*task update-indices-with-content

# Specific category only
*task update-indices-with-content --category=agents

# Dry run to see changes
*task update-indices-with-content --dry-run

# With detailed logging
*task update-indices-with-content --verbose
```

## Output
- Updated INDEX.md files with accurate metadata
- Dependency blocks added/updated in all files
- Bidirectional validation report
- Dependency registry in workspace/data-output/validation-reports/
- Change report in workspace/data-output/index-updates/
- Validation report with any issues found
- Performance metrics

## Integration with Bidirectional Validation
```yaml
integration:
  calls: framework/tasks/validation/validate-bidirectional-dependencies.md
  when: After content extraction, before index generation
  purpose: Ensure all dependencies are bidirectional
  
auto_fixes:
  - Add missing dependency blocks
  - Fix missing backlinks
  - Remove broken references
  - Update health scores
```

## Related Tasks
- update-all-indices.md (count-based predecessor)
- validate-dependencies.md (uses extracted metadata)
- validate-bidirectional-dependencies.md (NEW - ensures bidirectional integrity)
- system-sync.md (calls this task)

---
**Remember**: Trust but verify - always read actual content, never assume!