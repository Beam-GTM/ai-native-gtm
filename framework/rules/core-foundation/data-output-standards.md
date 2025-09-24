# Data Output Standards
**Category**: Core Foundation  
**Priority**: HIGH  
**Enforcement**: MANDATORY  

## Rule Statement
All system-generated outputs, reports, and data files MUST be stored in the organized `workspace/data-output/` directory structure, never in workspace root or feature directories.

## Rationale
- **Organization**: Centralized location for all outputs makes them easy to find
- **Cleanliness**: Prevents workspace root from becoming cluttered
- **Consistency**: Standard location across all tasks and agents
- **Automation**: Enables automated cleanup and archival
- **Tracking**: Simplifies monitoring and metrics collection

## Implementation Requirements

### Directory Structure
```
workspace/data-output/
├── validation-reports/    # Validation and integrity checks
├── system-reports/       # System status and health
├── task-outputs/         # Task execution results
├── feature-reports/      # Feature completion summaries
├── quality-reports/      # Quality gate decisions
├── index-updates/        # Index and registry updates
└── README.md            # Documentation
```

### File Naming Convention
```
{report-type}-{identifier}-{date}.{extension}
```

Examples:
- `validation-report-2025-08-25.md`
- `quality-gate-auth-feature-2025-08-25.md`
- `index-update-report-2025-08-25-143022.md`

### Required Behaviors

#### For Tasks
```yaml
task_output_requirements:
  - Always write to appropriate subdirectory
  - Include timestamp in filename
  - Use markdown for human-readable reports
  - Use JSON/YAML for machine-readable data
  - Never write to workspace root
```

#### For Agents
```yaml
agent_output_requirements:
  - Check directory exists before writing
  - Create timestamped files
  - Use consistent naming patterns
  - Document output location in logs
```

#### For Workflows
```yaml
workflow_output_requirements:
  - Aggregate outputs in feature-reports/
  - Link to individual task outputs
  - Generate summary reports
  - Track all generated files
```

## Compliance Checklist

### Task Compliance
- [ ] Output path includes `workspace/data-output/`
- [ ] Appropriate subdirectory selected
- [ ] Filename includes timestamp
- [ ] Format appropriate for content type

### Code Examples

#### Correct Implementation
```yaml
# Task writing validation report
output_location: workspace/data-output/validation-reports/validation-report-2025-08-25.md

# Feature completion report
output_location: workspace/data-output/feature-reports/auth-feature-completion-2025-08-25.md

# Task output
output_location: workspace/data-output/task-outputs/index-update-2025-08-25-143022.md
```

#### Incorrect Implementation
```yaml
# WRONG: Writing to workspace root
output_location: workspace/validation-report.md

# WRONG: Writing to feature directory
output_location: workspace/features/active/my-feature/report.md

# WRONG: No timestamp
output_location: workspace/data-output/report.md
```

## Enforcement Mechanisms

### Automated Checks
1. Pre-commit hooks verify output paths
2. Task validation checks for compliance
3. Weekly cleanup of non-compliant files

### Manual Review
1. Code review includes output location check
2. Quality gates verify report locations
3. System audits check for stray files

## Migration Path

### For Existing Reports
1. Identify reports in wrong locations
2. Move to appropriate data-output subdirectory
3. Update references in documentation
4. Update generating tasks/agents

### For New Development
1. Always use data-output from start
2. Include in task templates
3. Document in agent specifications
4. Validate in testing

## Exceptions
- Active context files remain in workspace/memory/
- Feature-specific files remain in feature directories
- System configuration files remain at root
- Only OUTPUTS go to data-output

## Related Rules
- File Management Standards
- Documentation Standards
- Quality Assurance Rules
- System Design Principles

## Validation
```bash
# Check for files in wrong location
find workspace -name "*report*.md" -not -path "*/data-output/*"

# Verify data-output structure
ls -la workspace/data-output/

# Count reports by type
find workspace/data-output -type f -name "*.md" | wc -l
```

## Consequences of Non-Compliance
- **MINOR**: Single file in wrong location - Move to correct location
- **MAJOR**: Task consistently outputs to wrong location - Fix task
- **CRITICAL**: System generating files in root - Block deployment

## Version History
- 2025-08-25: Initial rule creation
- 2025-08-25: Added enforcement mechanisms