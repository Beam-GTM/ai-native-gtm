<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Metrics & Reporting

## 📈 **METRICS & REPORTING**

### **Product Metrics**

#### **Key Performance Indicators (KPIs)**
```yaml
product_kpis:
  velocity_metrics:
    story_points_completed: "Points per sprint"
    velocity_trend: "3-sprint rolling average"
    predictability: "Actual vs committed"
    
  quality_metrics:
    defect_rate: "Bugs per story point"
    escaped_defects: "Production bugs per release"
    test_coverage: "Percentage of code covered"
    
  delivery_metrics:
    cycle_time: "Start to done duration"
    lead_time: "Request to delivery duration"
    throughput: "Stories completed per sprint"
    
  value_metrics:
    customer_satisfaction: "NPS, CSAT scores"
    feature_adoption: "Usage of new features"
    business_impact: "Revenue, cost savings, efficiency"
```

#### **Sprint Metrics**
```yaml
sprint_metrics:
  commitment_accuracy: "(Completed points / Committed points) * 100"
  scope_change: "(Added points / Original points) * 100"
  spillover_rate: "(Incomplete stories / Total stories) * 100"
  
  burndown_tracking:
    ideal_burndown: "Linear from total to zero"
    actual_burndown: "Daily remaining work"
    burndown_variance: "Actual vs ideal"
```

### **Reporting Standards**

#### **Sprint Report Template**
```yaml
sprint_report:
  executive_summary:
    - Sprint goal and achievement status
    - Key deliverables completed
    - Major blockers or issues
    - Next sprint focus
    
  detailed_metrics:
    - Velocity and capacity utilization
    - Quality metrics and test results
    - Team health and morale indicators
    - Technical debt addressed
    
  retrospective_insights:
    - What went well
    - What needs improvement
    - Action items for next sprint
    
  stakeholder_feedback:
    - Customer feedback received
    - Stakeholder satisfaction
    - Feature adoption metrics
```

