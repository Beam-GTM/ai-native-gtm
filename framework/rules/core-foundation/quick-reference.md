<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Quick Reference Guide

## 📊 **QUICK REFERENCE GUIDE**

### **File Type Placement Matrix**
```yaml
file_type_locations:
  "PRD": → workspace/features/{status}/{name}/prd.md
  "Agent": → operations/agents/{category}/
  "Workflow": → operations/workflows/{category}/
  "Checklist": → operations/checklists/{category}/
  "Memory": → workspace/memory/{category}/
  "Template": → operations/templates/{category}/
  "Specification": → core/system-documentation/specifications/
  "Implementation Guide": → core/system-documentation/implementation-guides/
  "Engineering Rule": → operations/engineeringrules/
  "System Architecture": → core/architecture/
```

### **Common Mistakes & Corrections**
```yaml
common_violations:
  implementation_guide:
    wrong: "operations/implementations/guide.md"
    right: "core/system-documentation/implementation-guides/guide.md"
    reason: "Implementation guides document the system"
    
  agent_definition:
    wrong: "/.agents/new-agent.md"
    right: "operations/agents/{category}/new-agent.md"
    reason: "Agents are operational components"
    
  feature_work:
    wrong: "/feature-xyz.md"
    right: "workspace/features/active/feature-xyz/"
    reason: "Active work belongs in workspace"
```

