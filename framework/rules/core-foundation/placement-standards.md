<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# File Placement & Organization Standards

## 🎯 **CORE PRINCIPLES**

### **The One Question That Matters**
```yaml
primary_decision: "What IS this file?"

answer_tree:
  DOCUMENTING_SYSTEM:
    location: "core/system-documentation/"
    subcategories: 
      - implementation-guides/  # How to implement features
      - specifications/         # Technical specifications
      - components/            # Component documentation
      - diagrams/              # Architecture diagrams
    
  OPERATING_SYSTEM:
    location: "operations/"
    subcategories:
      - agents/                # Agent definitions
      - workflows/             # Workflow definitions
      - tasks/                 # Task definitions
      - engineeringrules/      # Engineering standards
      - templates/             # System templates
      - checklists/            # Validation checklists
    
  ACTIVE_WORK:
    location: "workspace/"
    subcategories:
      - features/active/       # Current development
      - features/completed/    # Finished features
      - memory/                # System memory
      - generation/            # Generated systems
      - repositories/          # Repository work
    
  PROJECT_FOUNDATION:
    location: "core/"
    subcategories:
      - project-foundation/    # Core project docs
      - architecture/          # System architecture
```

