<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Template Management Standards

## 📋 **TEMPLATE MANAGEMENT STANDARDS**

### **Template Architecture Principles**

#### **Foundation Template Authority**
```yaml
CRITICAL_RULE: nexus-base.template is authoritative foundation
  - ALL domain templates MUST inherit from base
  - NO modifications without comprehensive analysis
  - Foundation captures 100% of current sophistication
  - Domain templates enhance (never replace) capabilities
```

#### **Quality Inheritance Mandate**
```yaml
CRITICAL_RULE: Template inheritance MUST preserve quality
  - NO quality degradation in domain templates
  - Domain specializations enhance sophistication
  - Template variables maintain integrity
  - Template customizations preserve excellence
```

#### **Template Consistency Requirements**
```yaml
CRITICAL_RULE: All templates MUST follow consistent patterns
  - Template structure consistent across variations
  - Template variable naming follows conventions
  - Template documentation format consistent
  - Template versioning systematic with tracking
```

### **Template Structure Standards**

#### **Template File Organization**
```yaml
directory_structure:
  operations/templates/:
    systems/:
      - nexus-base.template  # Foundation (authoritative)
      - domain-variants/         # Specialized templates
    domains/:
      - {domain-name}.template   # Domain specializations
    components/:
      - agents/                  # Agent components
      - workflows/               # Workflow components
      - contexts/                # Context components

naming_conventions:
  - Domain: {domain-name}-{specialization}.template
  - Component: {component-type}-{domain}.template
  - System: {system-name}-{version}.template
```

#### **Template Content Standards**
```yaml
mandatory_sections:
  - Template Overview: Purpose, inheritance, quality
  - Domain Specialization: Customization points
  - Generated System Structure: Complete architecture
  - Quality Framework: Validation and compliance
  - Generation Configuration: Variables and patterns

variable_standards:
  - Variables use UPPERCASE: {{DOMAIN_NAME}}
  - Required variables documented with validation
  - Optional variables include sensible defaults
  - Variable descriptions comprehensive
```

### **Template Versioning Standards**

#### **Version Control Requirements**
```yaml
version_control:
  - Versions tracked: Major.Minor.Patch
  - Changes documented with impact analysis
  - Evolution tracked with quality assessment
  - Compatibility maintained across iterations
  - Deprecation handled with migration strategy

change_management:
  - Breaking changes: Major version + migration guide
  - Enhancements: Minor version + documentation
  - Bug fixes: Patch version + validation
  - Testing required before release
```

### **Template Library Governance**

#### **Library Standards**
```yaml
library_organization:
  - Templates categorized by domain and type
  - Library searchable with indexing and metadata
  - Relationships documented with mapping
  - Library maintainable with procedures
  - Library expandable with new patterns

quality_control:
  - Review process with validation requirements
  - Approval workflow with expert testing
  - Maintenance procedures with updates
  - Documentation comprehensive for developers
```

