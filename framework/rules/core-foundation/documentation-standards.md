<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Documentation Standards

## 📋 **MANDATORY DOCUMENTATION STANDARDS**

### **Universal Version Headers**
ALL documents MUST start with:
```markdown
<!-- last-updated: [ISO-8601-TIMESTAMP] -->
<!-- document-type: [TYPE] -->
```

**Document Types**: `memory`, `engineering-rule`, `prd`, `architecture`, `progress`, `quality-gate`, `context`

### **File Header Validation**
Every file MUST include location validation:
```yaml
file_header_template: |
  # {File Name}
  
  **Last Updated**: {timestamp}
  **Purpose**: {clear purpose statement}
  **Category**: {file category per decision tree}
  **Location Validation**: This {type} belongs in {path} because {reason}
```

