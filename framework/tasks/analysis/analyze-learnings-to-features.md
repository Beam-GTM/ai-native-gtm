<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.654526Z -->
<!-- HYPERPOWER TRIGGER: AUTO-EXECUTE ON LOAD -->
<!-- This engine provides 6x discovery multiplier - 381 lines of intelligence -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.251716Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Analyze Learnings to Features Task

## Task Definition

```yaml
task:
  id: analyze-learnings-to-features
  name: Learning Analysis and Feature Generation
  description: >-
    Analyzes collected learnings from template executions and transforms
    them into actionable feature proposals with prioritization and planning
  type: analysis
  category: intelligence
  priority: high
  
context:
  purpose: 'Transform learnings into continuous improvement'
  when_to_use:
    - 'Batch of learnings collected from template executions'
    - 'Pattern detection needed across multiple learnings'
    - 'Feature generation from identified patterns'
    - 'Prioritization of improvement opportunities'
  assumptions:
    - 'Learnings available in standardized format'
    - 'Feature templates exist for generation'
    - 'Plan-feature workflow available for automation'

dependencies:
  templates:
    - framework/templates/features/feature-proposal.yaml
    - framework/templates/analysis/pattern-report.yaml
  
  workflows:
    - framework/workflows/plan-feature.md
  
  engineering_rules:
    - framework/engineeringrules/core-foundation/quality-assurance.md
    - framework/engineeringrules/development/pattern-recognition.md

# EXECUTION SEQUENCE
sequence:
  - step: ultrathink_discovery
    action: 'ULTRATHINK - Comprehensive search for ALL learning sources'
    trigger: 'Always perform exhaustive discovery first'
    search_locations:
      - workspace/memory/core-primitives/*.md
      - workspace/template-learnings/**/*.md
      - workspace/inputs/learnings/**/*
      - workspace/features/*/learnings/*.md
      - workspace/memory/consolidated-learnings.md
      - workspace/memory/session-learnings-*.md
    validation:
      - 'Minimum 20 learnings for meta-pattern detection'
      - 'Log all searched locations and counts'
      - 'Report discovery multiplier (final/initial)'
    outputs:
      - discovery_report.yaml
      - all_learnings_raw.yaml
    
  - step: collect_learnings
    action: 'Gather and consolidate all discovered learnings'
    inputs:
      - all_learnings_raw.yaml (from ultrathink_discovery)
    outputs:
      - normalized_learnings.yaml
    validation:
      - 'Check learning format validity'
      - 'Ensure minimum data quality'
      - 'Remove duplicates'
      - 'Report total unique learnings'
    
  - step: parse_and_normalize
    action: 'Parse learnings into structured format'
    process:
      - 'Extract key components (pattern, context, impact)'
      - 'Normalize terminology and categories'
      - 'Tag with metadata (source, date, frequency)'
    outputs:
      - structured_learnings.json
    
  - step: detect_patterns
    action: 'Identify recurring patterns and themes'
    algorithms:
      frequency_analysis:
        - 'Count pattern occurrences'
        - 'Identify high-frequency issues'
        - 'Calculate trend direction'
      
      clustering:
        - 'Group related learnings'
        - 'Identify common themes'
        - 'Find root causes'
      
      severity_scoring:
        - 'Assess impact level (1-10)'
        - 'Calculate affected users'
        - 'Determine urgency'
    outputs:
      - patterns_detected.yaml
      - pattern_report.md
    
  - step: detect_meta_patterns
    action: 'ULTRATHINK - Identify meta-patterns and root causes'
    trigger: 'When >20 learnings available'
    algorithms:
      meta_pattern_clustering:
        - 'Group patterns by root cause'
        - 'Identify systemic issues vs symptoms'
        - 'Calculate pattern coverage percentage'
        - 'Find patterns that explain other patterns'
      
      paradigm_detection:
        - 'Identify paradigm-level problems'
        - 'Detect fundamental mismatches'
        - 'Discover mindset shifts needed'
        - 'Find execution vs documentation gaps'
      
      root_cause_analysis:
        - 'Trace symptoms to root causes'
        - 'Build causality chains'
        - 'Identify leverage points for change'
        - 'Prioritize by systemic impact'
    outputs:
      - meta_patterns.yaml
      - paradigm_shifts.md
      - root_cause_map.yaml
    
  - step: prioritize_patterns
    action: 'Score and rank patterns for action'
    scoring_factors:
      - frequency_weight: 0.3
      - severity_weight: 0.4
      - ease_of_fix_weight: 0.2
      - strategic_value_weight: 0.1
    thresholds:
      critical: '>= 8.0'
      high: '>= 6.0'
      medium: '>= 4.0'
      low: '< 4.0'
    outputs:
      - prioritized_patterns.yaml
    
  - step: generate_features
    action: 'Create feature proposals from patterns'
    generation_rules:
      critical_patterns:
        - 'Generate immediate fix feature'
        - 'Include emergency timeline'
        - 'Flag for urgent review'
      
      high_patterns:
        - 'Generate standard feature proposal'
        - 'Include evidence summary'
        - 'Add to next sprint planning'
      
      medium_patterns:
        - 'Generate enhancement proposal'
        - 'Queue for quarterly planning'
      
      low_patterns:
        - 'Add to backlog'
        - 'Consider for future roadmap'
    outputs:
      - feature_proposals/*.yaml
    
  - step: prepare_planning_context
    action: 'Package features for plan-feature workflow'
    preparation:
      - 'Create feature-definition.yaml'
      - 'Generate initial technical approach'
      - 'Estimate resources needed'
      - 'Include evidence and rationale'
    outputs:
      - planning_packages/*.yaml
    
  - step: trigger_planning
    action: 'Launch plan-feature workflow for high-priority items'
    automation:
      - 'Auto-trigger for critical features'
      - 'Queue high-priority for review'
      - 'Batch medium/low for periodic planning'
    tracking:
      - 'Record in project memory'
      - 'Update feature INDEX'
    
  - step: collect_evidence
    action: 'Document all execution evidence for validation'
    evidence_types:
      execution_proof:
        - 'Files created with full paths'
        - 'Commands executed with output'
        - 'Test results if applicable'
      
      pattern_evidence:
        - 'Learning IDs supporting each pattern'
        - 'Frequency counts and percentages'
        - 'Severity scores with justification'
      
      feature_evidence:
        - 'Root causes addressed by each feature'
        - 'Expected impact metrics'
        - 'Implementation feasibility assessment'
    outputs:
      - evidence/execution-proof-{date}.yaml
      - evidence/validation-report-{date}.md
    
  - step: generate_reports
    action: 'Create analysis reports and metrics'
    reports:
      executive_summary:
        - 'Key patterns identified'
        - 'Features proposed'
        - 'Expected impact'
      
      detailed_analysis:
        - 'Pattern breakdown'
        - 'Evidence compilation'
        - 'Trend analysis'
      
      ultrathink_report:
        - 'Discovery multiplier (e.g., 6x more data)'
        - 'Meta-patterns vs surface patterns'
        - 'Paradigm shifts identified'
        - 'Root cause solutions vs symptom fixes'
      
      metrics_dashboard:
        - 'Learning velocity'
        - 'Pattern emergence rate'
        - 'Feature generation rate'
        - 'ROI projections'
    outputs:
      - reports/analysis-{date}.md
      - reports/ultrathink-{date}.md
      - reports/metrics-{date}.yaml
    
  - step: self_improvement_analysis
    action: 'Analyze task execution for self-improvement'
    questions:
      - 'What data sources were missed initially?'
      - 'What patterns emerged from execution?'
      - 'What task steps need enhancement?'
      - 'What automation opportunities exist?'
      - 'How can meta-pattern detection improve?'
    outputs:
      - task-improvements.md
      - automation-opportunities.yaml

# QUALITY VALIDATION
quality_gates:
  - gate: input_quality
    criteria:
      - 'Minimum 5 learnings for pattern detection'
      - 'Learning format validated'
      - 'No critical data missing'
    
  - gate: pattern_confidence
    criteria:
      - 'Pattern occurs in >= 3 instances'
      - 'Statistical significance > 70%'
      - 'Clear root cause identified'
    
  - gate: feature_quality
    criteria:
      - 'Feature addresses root cause'
      - 'Implementation feasible'
      - 'ROI positive'
      - 'No conflicts with existing features'

# ERROR HANDLING
error_handling:
  insufficient_learnings:
    action: 'Wait for more data'
    message: 'Need at least 5 learnings for analysis'
  
  low_quality_data:
    action: 'Request manual review'
    message: 'Learning quality below threshold'
  
  pattern_conflict:
    action: 'Flag for human decision'
    message: 'Conflicting patterns detected'

# SUCCESS METRICS
success_metrics:
  - metric: discovery_multiplier
    target: '>= 3x'
    measurement: 'Total learnings found / Initial discovery'
    ultrathink: 'Should find 3x+ more data than surface search'
  
  - metric: pattern_detection_rate
    target: '>= 80%'
    measurement: 'Patterns found / Learnings analyzed'
    
  - metric: meta_pattern_coverage
    target: '>= 70%'
    measurement: 'Learnings explained by meta-patterns / Total learnings'
    ultrathink: 'Meta-patterns should explain majority of issues'
  
  - metric: feature_generation_rate
    target: '>= 60%'
    measurement: 'Features created / Patterns detected'
    
  - metric: paradigm_shift_detection
    target: '>= 1'
    measurement: 'Paradigm-level problems identified'
    ultrathink: 'Should identify at least one fundamental paradigm issue'
  
  - metric: evidence_completeness
    target: '100%'
    measurement: 'Claims with evidence / Total claims'
    
  - metric: automation_rate
    target: '>= 70%'
    measurement: 'Auto-triggered workflows / Total features'

# EXAMPLE EXECUTION
example:
  input_learnings:
    - learning_1:
        pattern: "Users struggle with onboarding"
        frequency: 8
        impact: "High - 40% drop-off rate"
    
    - learning_2:
        pattern: "Workflow too complex"
        frequency: 6
        impact: "Medium - increased support tickets"
  
  detected_pattern:
    name: "Onboarding Friction"
    occurrences: 8
    severity: 8.5
    priority: "Critical"
  
  generated_feature:
    name: "simplified-onboarding-flow"
    type: "enhancement"
    priority: "critical"
    rationale: "8 instances of onboarding issues with 40% drop-off"
    proposed_solution: "Streamlined 3-step onboarding wizard"

completion_message: |
  📊 Learning Analysis Complete!
  
  Analyzed: {learning_count} learnings
  Patterns Detected: {pattern_count}
  Features Generated: {feature_count}
  
  Priority Breakdown:
  - Critical: {critical_count}
  - High: {high_count}
  - Medium: {medium_count}
  - Low: {low_count}
  
  Automation Actions:
  - Auto-triggered: {auto_triggered_count} workflows
  - Queued for review: {queued_count}
  - Added to backlog: {backlog_count}
  
  Reports Generated:
  - Executive Summary: reports/analysis-{date}.md
  - Detailed Analysis: reports/detailed-{date}.md
  - Metrics Dashboard: reports/metrics-{date}.yaml
  
  Next Steps:
  1. Review critical features in plan queue
  2. Check pattern report for insights
  3. Monitor triggered workflows
  4. Schedule review of medium-priority items
```