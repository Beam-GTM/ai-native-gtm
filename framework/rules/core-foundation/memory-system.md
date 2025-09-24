<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Memory System Architecture

## 🧠 **MEMORY SYSTEM ARCHITECTURE**

### **Critical Agent Activation Requirements**
ALL agents MUST include in activation:
```yaml
STEP 2: Execute `date -u +"%Y-%m-%dT%H:%M:%SZ"` for timestamp loading
```

**Purpose**:
- Ensures agents have access to real current timestamps
- Prevents hardcoded timestamps in documentation
- Maintains accurate documentation version control
- Enables proper memory bank update timestamps

### **Memory Bank Core Structure**
```yaml
core_files:
  context-map.md:
    location: "operations/engineeringrules/"
    purpose: "Navigation hub and document relationships"
    priority: "Read FIRST"
    
  project-brief.md:
    location: "core/project-foundation/"
    purpose: "Foundation document shaping all other files"
    content: "Project objectives, scope, success metrics"
    
  product-context.md:
    location: "core/project-foundation/"
    purpose: "Business justification and user goals"
    content: "Market landscape, user problems, business goals"
    
  system-architecture.md:
    location: "workspace/.memory/"
    purpose: "Technical architecture and components"
    content: "C4 Model, repository architecture, decisions"
    
  tech-stack.md:
    location: "workspace/.memory/"
    purpose: "Complete technology inventory"
    content: "Technologies by repository, versions, dependencies"
    
  development-workflow.md:
    location: "workspace/.memory/"
    purpose: "Development processes and coordination"
    content: "Workflow overview, agent coordination, quality"
    
  key-learnings.md:
    location: "workspace/.memory/"
    purpose: "Architectural wisdom and lessons"
    content: "Design principles, what works/avoid, guidelines"
```

### **Feature Documentation Structure**
```yaml
per_feature_files:
  prd.md:
    purpose: "Product Requirements Document"
    format: "Must follow prd-writing-rules.md exactly"
    content: "Requirements, constraints, dependencies"
    
  progress.md:
    purpose: "Implementation tracking across repositories"
    content: "Completed, in-progress, pending, blockers"
    references: "TODOs from prd.md"
    
  active-context.md:
    purpose: "Current implementation context"
    content: "Work focus, codebase sections, integration points"
    critical: "Enables agent continuation after interruption"
    
  quality-gates.md:
    purpose: "Quality validation across repositories"
    content: "Test results, metrics, compliance, issues"
    sections: "Separate sections per repository"
```

### **Memory Bank Assembly Instructions**

#### **TOP-DOWN Assembly (New Projects)**

**Step 1: Initialize V2 Memory Structure**
```bash
# Create V2 directory structure  
mkdir -p core/project-foundation
mkdir -p workspace/features
mkdir -p workspace/.memory

# Core files distributed across structure:
# - Foundation files in core/project-foundation/
# - Memory files in workspace/.memory/
# - Context map in operations/engineeringrules/
```

**Step 2: Populate Core Files Using Templates**
1. **context-map.md** (MANDATORY FIRST)
   - Location: `operations/engineeringrules/context-map.md`
   - Content: Navigation paths and document relationships
   
2. **project-brief.md** (FOUNDATION)
   - Structure Reference: Follow priority "1-foundation" template
   - Content: Project objectives, scope, success metrics
   
3. **product-context.md** (BUSINESS)
   - Structure Reference: Follow priority "2-context" template
   - Content: Market landscape, user problems, business goals
   
4. **system-architecture.md** (TECHNICAL)
   - Structure Reference: Follow priority "3-architecture" template
   - Content: C4 Model diagrams, architecture decisions
   
5. **tech-stack.md** (TECHNOLOGY)
   - Structure Reference: Follow priority "4-technology" template
   - Content: Complete technology inventory by repository
   
6. **development-workflow.md** (PROCESS)
   - Structure Reference: Follow priority "5-process" template
   - Content: Development processes, agent coordination
   
7. **key-learnings.md** (WISDOM)
   - Structure Reference: Follow priority "6-wisdom" template
   - Content: Lessons learned, best practices

**Step 3: Initialize Repository Memory**
```bash
# For each repository
cd {repo-name}/
mkdir -p .memory
touch .memory/repository-context.md
touch .memory/key-learnings.md
```

#### **BOTTOM-UP Assembly (Existing Codebases)**

**Step 1: Analyze Existing Codebase**
```bash
# Repository Discovery
find . -name "*.md" -type f > existing-docs.txt
find . -name "*.json" -type f > package-files.txt
find . -name "*.yaml" -o -name "*.yml" > config-files.txt

# Technology Stack Analysis
find . -name "package.json" -exec echo "=== {} ===" \; -exec cat {} \;
find . -name "requirements.txt" -exec echo "=== {} ===" \; -exec cat {} \;
find . -name "Cargo.toml" -exec echo "=== {} ===" \; -exec cat {} \;

# Integration Point Discovery
grep -r "import\|require\|from" --include="*.js" --include="*.ts" . | head -50
grep -r "api\|endpoint\|route" --include="*.js" --include="*.ts" . | head -20
```

**Step 2: Extract Repository Information**
Analysis Checklist:
- [ ] Technology Stack: What languages/frameworks?
- [ ] Primary Functions: What does this repository DO?
- [ ] Data Models: What entities/data structures exist?
- [ ] APIs/Interfaces: What does it expose/consume?
- [ ] Dependencies: What external services/repos needed?
- [ ] Integration Points: How does it connect to other systems?

**Step 3: Create Memory Bank from Analysis**
Follow TOP-DOWN Step 2-3 but populate with discovered information

### **Validation Protocol**

#### **Pre-Implementation Validation**
- [ ] All file names use kebab-case exactly
- [ ] All cross-references use correct relative paths
- [ ] All required sections present in each file type
- [ ] No placeholder TODOs remain

#### **Post-Implementation Validation**
- [ ] Agent can load context-map.md successfully
- [ ] All cross-reference links resolve correctly
- [ ] Repository contexts accurately reflect integration points
- [ ] Technology stacks match actual implementations

#### **Disaster Recovery**
If memory bank assembly fails:
1. **Immediate**: Stop all development work
2. **Diagnose**: Check file naming, cross-references, missing sections
3. **Repair**: Follow assembly instructions exactly
4. **Validate**: Run through validation protocol completely
5. **Resume**: Only after 100% validation success

