<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.755627Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.261283Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Generate Feature Roadmap Task
**Task ID**: generate-roadmap  
**Category**: features
**Priority**: HIGH
**Trigger**: Feature INDEX updates, weekly schedule, manual command

## Purpose
Automatically generate visual feature roadmap from INDEX data, showing timelines, dependencies, and progress.

## Execution Steps

### Step 1: Load Feature Data
```yaml
action: LOAD_FEATURES
source: workspace/features/INDEX.md
extract:
  - active_features
  - completed_features
  - feature_progress
  - priorities
  - dependencies
```

### Step 2: Calculate Timeline
```yaml
action: TIMELINE_CALCULATION
process:
  - Map features to timeline based on progress
  - Calculate estimated completion dates
  - Identify critical path
  - Mark dependencies and blockers
```

### Step 3: Generate Visualizations
```yaml
action: CREATE_VISUALIZATIONS
outputs:
  gantt_chart:
    format: mermaid
    content: |
      gantt
        title Feature Development Roadmap
        dateFormat YYYY-MM-DD
        section Integration Layer
          Context Overflow Task :active, 2025-08-28, 7d
          Project Absorption :2025-09-04, 7d
        section Context7 MCP
          MCP Connection :2025-09-11, 7d
          API Documentation :2025-09-18, 7d
        section Distribution
          Template Genesis :2025-09-25, 7d
          GitHub Hub :2025-10-02, 7d
          
  dependency_graph:
    format: mermaid
    content: |
      graph TD
        A[Context Overflow] --> B[Project Absorption]
        B --> C[MCP Connection]
        C --> D[Script Generation]
        E[Template Genesis] --> F[Distribution Hub]
        F --> G[Learning Network]
```

### Step 4: Risk Assessment
```yaml
action: ASSESS_RISKS
criteria:
  at_risk:
    - progress < 20% and priority = "critical"
    - blocked_by_dependencies
    - no_updates_in_7_days
  healthy:
    - progress > 60%
    - clear_dependencies
    - regular_updates
```

### Step 5: Generate Roadmap Document
```yaml
action: WRITE_ROADMAP
output: workspace/features/ROADMAP.md
template: |
  # Feature Roadmap
  **Generated**: {{timestamp}}
  **Active Features**: {{active_count}}
  **Completion Rate**: {{completion_rate}}%
  
  ## Current Sprint (Week {{current_week}})
  {{sprint_features}}
  
  ## Timeline View
  {{gantt_chart}}
  
  ## Dependencies
  {{dependency_graph}}
  
  ## Risk Assessment
  {{risk_matrix}}
  
  ## Velocity Metrics
  - Features completed this week: {{weekly_completed}}
  - Average completion time: {{avg_completion_days}} days
  - Projected completion: {{projected_date}}
```

### Step 6: Update Indices
```yaml
action: UPDATE_REFERENCES
updates:
  - workspace/features/INDEX.md (last_roadmap_generated)
  - briefing/project-brief.md (milestone_status)
  - operations/agents/core/orchestrator.md (roadmap_cache)
```

## Success Criteria
- [ ] Roadmap generated with all active features
- [ ] Timeline accurately reflects progress
- [ ] Dependencies clearly mapped
- [ ] Risks identified and flagged
- [ ] Visualizations render correctly

## Integration Points
- Triggered by feature INDEX updates
- Called by orchestrator *roadmap command
- Scheduled weekly via system-maintenance workflow
- Updates dashboard metrics

## Output Example
```markdown
# Feature Roadmap | Generated: 2025-08-27T17:00:00Z

## 🎯 Current Sprint (Week 35)
### Active This Week
- ✅ Context Overflow Setup (Day 2/7) - 28% complete
- 🔄 Learning Analysis Pipeline (Day 5/14) - 65% complete
- ⚠️ Smart Architecture Transform (Day 1/21) - 20% complete [AT RISK]

## 📅 Timeline
[Gantt chart showing 3-month horizon with all features]

## 🔗 Dependencies
[Graph showing feature relationships and blockers]

## 📊 Metrics
- Velocity: 2.3 features/week (↑ 15% from last week)
- At Risk: 2 features requiring attention
- On Track: 4 features progressing well
```