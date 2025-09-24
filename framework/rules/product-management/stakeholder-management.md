<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Stakeholder Management

## 🔄 **STAKEHOLDER MANAGEMENT**

### **Stakeholder Communication**

#### **Communication Plan**
```yaml
stakeholder_communication:
  executive_stakeholders:
    frequency: "Monthly or milestone-based"
    format: "Executive summary dashboard"
    content: ["Progress vs goals", "Key metrics", "Risks", "Decisions needed"]
    
  business_stakeholders:
    frequency: "Sprint reviews"
    format: "Demo and discussion"
    content: ["Sprint achievements", "Upcoming work", "Feedback collection"]
    
  technical_stakeholders:
    frequency: "Weekly sync"
    format: "Technical discussion"
    content: ["Technical decisions", "Architecture changes", "Dependencies"]
    
  end_users:
    frequency: "Release-based"
    format: "Release notes and updates"
    content: ["New features", "Improvements", "Known issues"]
```

#### **Stakeholder Matrix**
```yaml
stakeholder_analysis:
  high_power_high_interest:
    engagement: "Manage closely"
    communication: "Regular, detailed updates"
    examples: ["Product sponsors", "Key customers"]
    
  high_power_low_interest:
    engagement: "Keep satisfied"
    communication: "Concise, relevant updates"
    examples: ["Senior executives", "Compliance officers"]
    
  low_power_high_interest:
    engagement: "Keep informed"
    communication: "Regular information sharing"
    examples: ["Team members", "End users"]
    
  low_power_low_interest:
    engagement: "Monitor"
    communication: "Minimal, as needed"
    examples: ["Peripheral teams", "Vendors"]
```

### **Approval & Sign-off Process**

#### **Approval Gates**
```yaml
approval_checkpoints:
  concept_approval:
    approvers: ["Product Manager", "Business Sponsor"]
    criteria: ["Business case validated", "Resources available"]
    
  design_approval:
    approvers: ["Product Owner", "UX Lead", "Tech Lead"]
    criteria: ["User flows complete", "Technical feasibility confirmed"]
    
  release_approval:
    approvers: ["Product Owner", "QA Lead", "Operations"]
    criteria: ["Acceptance criteria met", "Quality gates passed", "Deployment ready"]
```

