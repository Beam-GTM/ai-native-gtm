<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.340527Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Nexus Template System
**Version**: 1.0.0  
**Updated**: 2025-08-28T00:50:00Z  
**Purpose**: User guide for Nexus template system usage and navigation

## 🎯 Quick Start

**Template Location**: `framework/templates/`  
**Central Registry**: `INDEX.md` - Complete template catalog with metadata  
**Total Templates**: 16 templates across 5 categories  

### **Finding Templates**
1. **Browse INDEX.md** - Complete catalog with descriptions
2. **Use Orchestrator Commands** - `*templates` for interactive discovery  
3. **Navigate Categories** - Browse subdirectories by type

### **Using Templates**
1. **Select Appropriate Template** - Match template to your needs
2. **Read Template Documentation** - Follow variable substitution patterns  
3. **Apply Template** - Use orchestrator commands or manual application
4. **Validate Results** - Ensure template execution successful

## 📁 Template Categories

### **agents/** - Agent Templates (2 templates)
Create sophisticated agents with Nexus patterns and intelligence framework
- `agent.yaml` - Core agent template (50KB+ comprehensive)
- `agent.yaml.backup.2025-08-26` - Previous version backup

### **features/** - Feature Templates (7 templates)
Feature planning, tracking, and management templates
- `active-context.yaml` - Current work focus tracking
- `feature-index.yaml` - Feature metadata generation  
- `index-generator.yaml` - Automated index generation
- `index.yaml` - General feature indexing
- `prd.yaml` - Product Requirements Document
- `progress.yaml` - Implementation tracking
- `quality-gates.yaml` - Quality validation framework

### **workflows/** - Workflow Templates (2 templates)  
Multi-step process coordination and behavioral control
- `workflow.yaml` - Core workflow definition
- `workflow-scope-enforcement.yaml` - Behavioral control framework

### **tasks/** - Task Templates (2 templates)
Executable procedures and automation triggers
- `task.yaml` - Executable workflow procedures
- `task-activation-triggers.yaml` - Task execution triggers

### **system/** - System Templates (3 templates)
Quality validation and system specification templates
- `validation.yaml` - Quality validation procedures
- `checklist.yaml` - Quality assurance checklists  
- `document_template.md` - Template format specification (SPECIFICATION)

## 🔧 Orchestrator Commands

**Template Discovery Commands** (Integration in progress):
```
*templates                 # Show all templates by category
*template-list agents      # List templates in agents category  
*template-list features    # List templates in features category
*template-help agent.yaml  # Show template usage guide
*template-create prd.yaml  # Create document from template
```

## 📖 Template Usage Guidelines

### **Template Selection**
- **Building Agents**: Use `agents/agent.yaml` for comprehensive agent creation
- **Planning Features**: Use `features/prd.yaml` for requirements documentation
- **Creating Workflows**: Use `workflows/workflow.yaml` for process definition
- **Task Automation**: Use `tasks/task.yaml` for executable procedures
- **Quality Validation**: Use `system/validation.yaml` for validation procedures

### **Variable Substitution**
Most templates use `{{variable_name}}` syntax for customization:
- `{{agent_name}}` - Agent name in kebab-case
- `{{feature_name}}` - Feature name and identification  
- `{{workflow_id}}` - Workflow identifier
- `{{description}}` - Component description text

### **Template Validation**
- All templates should follow `system/document_template.md` specification
- YAML templates require valid syntax and structure
- Variables must be consistently defined and used
- LLM executability should be verified before deployment

## 🎯 Template Development

### **Creating New Templates**
1. **Follow Specification** - Use `system/document_template.md` format
2. **Choose Category** - Place in appropriate subdirectory
3. **Document Variables** - Clear variable definitions and examples
4. **Update Registry** - Add to `INDEX.md` catalog
5. **Test Execution** - Verify LLM can execute template

### **Template Standards**
- **YAML Format** - Use structured YAML for metadata and instructions
- **Variable Consistency** - Consistent naming across related templates
- **Documentation** - Clear usage instructions and examples
- **LLM Compatibility** - Natural language instructions for LLM execution

## 📊 System Integration

**Template System integrates with:**
- **Orchestrator** - Template discovery and execution commands
- **Workflows** - Template-driven process automation
- **Quality Gates** - Template validation and compliance
- **Feature Management** - Template-based feature creation
- **Agent System** - Agent creation and enhancement

## 🔄 Template Versioning

**Version Management**:
- Templates use semantic versioning (major.minor.patch)
- Backup files created before major modifications
- Version history maintained in template metadata
- Rollback capabilities for failed template updates

**Current Status**:
- Template system v1.0.0 - Initial consolidation complete
- All templates cataloged and organized
- Category structure implemented
- Discovery system ready for orchestrator integration

## 🚀 Future Enhancements

**Phase 2 (HIGH Priority)**: Template Standardization
- Validation framework for specification compliance
- LLM executability verification system
- Template format standardization

**Phase 3 (MEDIUM Priority)**: Discovery Integration  
- Full orchestrator command implementation
- Interactive template selection and guidance
- Template help system integration

**Phase 4 (FUTURE Priority)**: Advanced Features
- Template generation and creation systems
- Advanced version management automation
- Usage analytics and optimization

---

**Template System Status**: ✅ **OPERATIONAL**  
**Discovery**: Available through INDEX.md and category browsing  
**Integration**: Ready for orchestrator command implementation  
**Quality**: Pending Phase 2 validation framework implementation