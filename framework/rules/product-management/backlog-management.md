<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Backlog Management

## 📊 **BACKLOG MANAGEMENT**

### **Product Backlog Standards**

#### **Backlog Structure**
```yaml
backlog_hierarchy:
  epics:
    definition: "Large bodies of work spanning multiple sprints"
    duration: "3-6 months"
    breakdown: "Contains multiple features"
    
  features:
    definition: "Deliverable functionality providing value"
    duration: "2-4 sprints"
    breakdown: "Contains multiple user stories"
    
  user_stories:
    definition: "Smallest unit of deliverable value"
    duration: "Within single sprint"
    breakdown: "Contains multiple tasks"
    
  tasks:
    definition: "Technical work items"
    duration: "Hours to days"
    breakdown: "Atomic work units"
```

#### **Prioritization Framework**
```yaml
prioritization_methods:
  moscow:
    must_have: "Critical for release"
    should_have: "Important but not critical"
    could_have: "Desirable if time permits"
    wont_have: "Out of scope for this release"
    
  value_vs_effort:
    high_value_low_effort: "Quick wins - Priority 1"
    high_value_high_effort: "Strategic - Priority 2"
    low_value_low_effort: "Fill-ins - Priority 3"
    low_value_high_effort: "Avoid - Priority 4"
    
  wsjf: # Weighted Shortest Job First
    formula: "Cost_of_Delay / Job_Duration"
    factors:
      - User_business_value
      - Time_criticality
      - Risk_reduction
      - Opportunity_enablement
```

#### **Backlog Grooming Standards**
```yaml
grooming_schedule:
  frequency: "Weekly or bi-weekly"
  duration: "1-2 hours"
  participants: ["Product Owner", "Scrum Master", "Tech Lead", "Team Representatives"]
  
grooming_activities:
  - Review and update priorities
  - Break down large items
  - Add acceptance criteria
  - Estimate new items
  - Remove obsolete items
  - Identify dependencies
  - Clarify requirements
```

### **Epic Management**

#### **Epic Structure**
```yaml
epic_template:
  title: "Clear, descriptive title"
  
  business_case:
    problem_statement: "What problem are we solving?"
    business_value: "What value does this deliver?"
    success_metrics: "How do we measure success?"
    
  scope:
    included: "What's in scope"
    excluded: "What's out of scope"
    assumptions: "Key assumptions"
    constraints: "Known constraints"
    
  delivery:
    milestones: "Key delivery points"
    dependencies: "External dependencies"
    risks: "Identified risks"
    timeline: "Expected duration"
```

