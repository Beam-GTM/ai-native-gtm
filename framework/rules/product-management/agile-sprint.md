<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Agile & Sprint Management

## 🏃 **AGILE & SPRINT MANAGEMENT**

### **Sprint Planning Standards**

#### **Sprint Structure Requirements**
```yaml
sprint_configuration:
  duration: 2_weeks_standard
  capacity_planning: 80%_of_available_hours
  buffer: 20%_for_overhead_and_interruptions
  
sprint_ceremony_schedule:
  sprint_planning: Day_1_morning
  daily_standups: Every_day_15_minutes
  sprint_review: Last_day_afternoon
  retrospective: Last_day_after_review
```

#### **Sprint Goal Definition**
- **SMART Goals**: Specific, Measurable, Achievable, Relevant, Time-bound
- **Single Focus**: One primary objective per sprint
- **Business Value**: Clear connection to business outcomes
- **Team Commitment**: Full team buy-in and understanding

#### **Capacity Planning**
```yaml
capacity_calculation:
  available_hours: team_members * working_days * hours_per_day
  productive_capacity: available_hours * 0.8
  story_points: productive_capacity / velocity_factor
  
allocation_guidelines:
  new_features: 60%
  bug_fixes: 20%
  technical_debt: 10%
  support_and_maintenance: 10%
```

### **User Story Standards**

#### **Story Format**
```yaml
user_story_template:
  format: "As a [persona], I want [functionality] so that [benefit]"
  
  components:
    persona: Specific user type or role
    functionality: Clear action or capability
    benefit: Business or user value delivered
```

#### **Acceptance Criteria**
```yaml
acceptance_criteria_format:
  structure: Given_When_Then
  
  template:
    given: "[precondition or context]"
    when: "[action or trigger]"
    then: "[expected outcome]"
    
  requirements:
    - Testable and verifiable
    - Clear pass/fail conditions
    - Complete coverage of scenarios
    - Edge cases included
```

#### **Definition of Ready**
```yaml
story_ready_checklist:
  - Clear user story statement
  - Acceptance criteria defined
  - Dependencies identified
  - Effort estimated
  - Priority assigned
  - Technical approach discussed
  - Test approach defined
  - UX/UI designs available (if applicable)
```

#### **Definition of Done**
```yaml
story_done_checklist:
  - Code complete and reviewed
  - Unit tests written and passing
  - Integration tests passing
  - Documentation updated
  - Acceptance criteria met
  - Product Owner approval
  - Deployed to staging
  - No critical bugs
```

### **Story Sizing & Estimation**

#### **Story Point Guidelines**
```yaml
story_point_scale:
  1_point: 
    effort: "2-4 hours"
    complexity: "Trivial change"
    risk: "No risk"
    
  2_points:
    effort: "4-8 hours"
    complexity: "Simple, well-understood"
    risk: "Minimal risk"
    
  3_points:
    effort: "1-2 days"
    complexity: "Moderate, some unknowns"
    risk: "Low risk"
    
  5_points:
    effort: "2-3 days"
    complexity: "Complex, multiple components"
    risk: "Moderate risk"
    
  8_points:
    effort: "3-5 days"
    complexity: "Very complex, significant unknowns"
    risk: "High risk"
    
  13_points:
    effort: "1-2 weeks"
    complexity: "Extremely complex"
    risk: "Very high risk"
    note: "Should be broken down"
```

#### **Estimation Techniques**
1. **Planning Poker**: Team consensus through discussion
2. **T-Shirt Sizing**: Quick relative sizing (XS, S, M, L, XL)
3. **Affinity Mapping**: Grouping similar stories
4. **Three-Point Estimation**: Optimistic, Realistic, Pessimistic

