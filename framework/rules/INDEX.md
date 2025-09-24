<!-- version: index-20250825-expanded -->
<!-- last-updated: 2025-08-25T14:00:00Z -->
<!-- document-type: engineering-rule-index -->

# Engineering Rules Index - Comprehensive Navigation Guide

## 📋 **NAVIGATION GUIDE**

This index provides navigation to all sharded engineering rules organized by domain, with descriptions and AI loading hints for optimal usage.

## 🎯 **LOADING STRATEGY**

```yaml
OPTIMAL_LOADING_PATTERN:
  1. Start here (INDEX.md) to understand structure
  2. Load only the specific shards you need for your task
  3. Use domain bundles for comprehensive work
  4. Cache frequently used rules during session
  5. Unload when switching to different domain
```

---

## 📁 **Core Foundation Rules**
*Source: core-foundation-rules.md*  
**Purpose**: Fundamental system standards that govern all operations  
**When to Load**: During system initialization, file operations, or documentation tasks

### **Shards & Loading Hints**

- **[File Placement & Organization Standards](./core-foundation/placement-standards.md)**
  - *Content*: Decision tree for file placement, root protection, category definitions
  - *Load When*: Creating new files, organizing structure, deciding where files belong
  - *Key Rules*: "What IS this file?" question, placement validation
  - *Size*: 1.5KB - Quick load

- **[Documentation Standards](./core-foundation/documentation-standards.md)**
  - *Content*: Version headers, document types, file validation templates
  - *Load When*: Creating any documentation, updating file headers
  - *Key Rules*: Mandatory version headers, document type classifications
  - *Size*: 0.9KB - Quick load

- **[System Design & Architecture Principles](./core-foundation/system-design-principles.md)**
  - *Content*: Problem-solving methodology, architecture reasoning, design patterns
  - *Load When*: Designing systems, making architectural decisions, planning implementations
  - *Key Rules*: 8-step methodology, SOLID principles, architecture reasoning process
  - *Size*: 3.6KB - Medium load

- **[Code & Architecture Documentation](./core-foundation/code-documentation.md)**
  - *Content*: C4 model, code documentation standards, Mermaid diagrams
  - *Load When*: Writing technical documentation, creating diagrams, documenting APIs
  - *Key Rules*: File/class/function documentation, C4 levels, diagram standards
  - *Size*: 4.9KB - Medium load

- **[Memory System Architecture](./core-foundation/memory-system.md)**
  - *Content*: Memory bank structure, assembly instructions, validation protocols
  - *Load When*: Setting up memory systems, creating feature contexts, agent activation
  - *Key Rules*: Two-tier architecture, memory bank assembly, context validation
  - *Size*: 6.6KB - Large load
  - *Critical For*: Agent activation sequences

- **[File Management & Organization](./core-foundation/file-management.md)**
  - *Content*: Organization patterns, cleanup protocols, link preservation
  - *Load When*: Reorganizing files, cleanup operations, maintaining structure
  - *Key Rules*: Safe movement strategy, link integrity, user-guided cleanup
  - *Size*: 5.3KB - Large load

- **[Compliance & Enforcement](./core-foundation/compliance-enforcement.md)**
  - *Content*: Automated validation, success metrics, violation recovery
  - *Load When*: Running compliance checks, handling violations
  - *Key Rules*: Monitoring systems, compliance indicators
  - *Size*: 1.4KB - Quick load

- **[Quick Reference Guide](./core-foundation/quick-reference.md)**
  - *Content*: File type matrix, common mistakes, quick lookups
  - *Load When*: Need quick answers about file placement or common patterns
  - *Key Rules*: Placement matrix, mistake corrections
  - *Size*: 1.4KB - Quick load

- **[Quality Assurance Standards](./core-foundation/quality-assurance.md)**
  - *Content*: Engineering excellence standards, general principles
  - *Load When*: Quality reviews, establishing standards
  - *Key Rules*: Quality standards, engineering principles
  - *Size*: 1.0KB - Quick load

---

## 📁 **Development Standards**
*Source: development-standards.md*  
**Purpose**: Code quality, testing, and implementation standards  
**When to Load**: During active development, code reviews, or test creation

### **Shards & Loading Hints**

- **[General Coding Standards](./development/coding-standards.md)**
  - *Content*: Universal coding principles, documentation requirements
  - *Load When*: Starting any coding task, establishing standards
  - *Key Rules*: Clean code, security, performance, error handling
  - *Size*: 1.8KB - Quick load
  - *Pairs Well With*: Language-specific standards

- **[Python-Specific Standards](./development/python-standards.md)**
  - *Content*: Python style, async patterns, type hints, anti-patterns
  - *Load When*: Writing Python code, reviewing Python PRs
  - *Key Rules*: Indentation care, async patterns, type hints mandatory
  - *Size*: 4.6KB - Medium load
  - *Critical For*: Python development

- **[Testing Standards](./development/testing-standards.md)**
  - *Content*: Test organization, scenarios, coverage requirements
  - *Load When*: Writing tests, setting up test suites, defining coverage
  - *Key Rules*: MECE principle, AAA pattern, 80% coverage minimum
  - *Size*: 4.5KB - Medium load
  - *Must Have For*: Test creation

- **[Code Review Standards](./development/code-review.md)**
  - *Content*: Review checklists, process, improvement patterns
  - *Load When*: Reviewing PRs, conducting code reviews
  - *Key Rules*: Functional/quality/security/performance reviews
  - *Size*: 1.6KB - Quick load

- **[Linting & Formatting](./development/linting-formatting.md)**
  - *Content*: Ruff configuration, when to run, handling issues
  - *Load When*: Setting up linting, fixing formatting issues
  - *Key Rules*: Run before commits, fix don't suppress
  - *Size*: 1.5KB - Quick load

- **[LLM Development Standards](./development/llm-development.md)**
  - *Content*: Prompt engineering, Pydantic models, GEval testing
  - *Load When*: Building LLM features, writing prompts
  - *Key Rules*: Prompt structure, output format placement
  - *Size*: 4.0KB - Medium load
  - *Specialized*: LLM features only

- **[MCP Tool Development](./development/mcp-tools.md)**
  - *Content*: Tool structure, definition patterns, guidelines
  - *Load When*: Creating MCP tools, defining tool interfaces
  - *Key Rules*: Atomicity, type safety, async operations
  - *Size*: 1.7KB - Quick load
  - *Specialized*: MCP development only

- **[Deployment Standards](./development/deployment.md)**
  - *Content*: Pre-deployment checklist, deployment process
  - *Load When*: Preparing for deployment, release validation
  - *Key Rules*: All tests passing, security scan, documentation updated
  - *Size*: 0.8KB - Quick load

- **[Quality Metrics](./development/quality-metrics.md)**
  - *Content*: Code quality targets, performance targets
  - *Load When*: Setting quality goals, measuring performance
  - *Key Rules*: Coverage >80%, response <200ms
  - *Size*: 0.8KB - Quick load

- **[Continuous Improvement](./development/continuous-improvement.md)**
  - *Content*: Regular activities, best practices evolution
  - *Load When*: Planning improvements, retrospectives
  - *Key Rules*: Regular reviews, pattern library
  - *Size*: 0.8KB - Quick load

---

## 📁 **Product Management Rules**
*Source: product-management-rules.md*  
**Purpose**: Product development lifecycle management  
**When to Load**: During product planning, sprint management, or stakeholder coordination

### **Shards & Loading Hints**

- **[PRD Writing Standards](./product-management/prd-writing.md)**
  - *Content*: Complete PRD structure, all 6 sections detailed
  - *Load When*: Creating PRDs, documenting requirements
  - *Key Rules*: Mandatory structure, technical PRD section
  - *Size*: 6.6KB - Large load
  - *Critical For*: PRD creation

- **[Agile & Sprint Management](./product-management/agile-sprint.md)**
  - *Content*: Sprint planning, story standards, estimation
  - *Load When*: Sprint planning, story writing, estimation sessions
  - *Key Rules*: 2-week sprints, story format, point scale
  - *Size*: 3.6KB - Medium load
  - *Pairs With*: Backlog management

- **[Backlog Management](./product-management/backlog-management.md)**
  - *Content*: Backlog structure, prioritization, epic management
  - *Load When*: Grooming backlog, prioritizing work
  - *Key Rules*: MoSCoW, WSJF, epic structure
  - *Size*: 2.6KB - Small load

- **[Stakeholder Management](./product-management/stakeholder-management.md)**
  - *Content*: Communication plans, stakeholder matrix, approval gates
  - *Load When*: Planning stakeholder engagement, getting approvals
  - *Key Rules*: Stakeholder matrix, approval checkpoints
  - *Size*: 2.3KB - Small load

- **[Metrics & Reporting](./product-management/metrics-reporting.md)**
  - *Content*: KPIs, sprint metrics, reporting templates
  - *Load When*: Creating reports, defining metrics
  - *Key Rules*: Velocity, quality, delivery metrics
  - *Size*: 2.0KB - Small load

- **[Release Management](./product-management/release-management.md)**
  - *Content*: Release planning, checklists, documentation
  - *Load When*: Planning releases, creating release notes
  - *Key Rules*: Release strategies, preparation checklist
  - *Size*: 2.1KB - Small load

- **[Quality Assurance in Product Management](./product-management/product-quality.md)**
  - *Content*: Requirements quality, product quality gates
  - *Load When*: Quality reviews, gate checks
  - *Key Rules*: Requirements criteria, quality gates
  - *Size*: 1.5KB - Quick load

- **[Retrospectives & Continuous Improvement](./product-management/retrospectives.md)**
  - *Content*: Retrospective formats, improvement frameworks
  - *Load When*: Running retrospectives, planning improvements
  - *Key Rules*: Retrospective structure, action tracking
  - *Size*: 2.1KB - Small load

- **[Compliance & Governance](./product-management/compliance-governance.md)**
  - *Content*: Decision rights, compliance requirements, audit process
  - *Load When*: Governance reviews, compliance checks
  - *Key Rules*: Decision authority matrix, audit areas
  - *Size*: 1.9KB - Quick load

---

## 📁 **System Operations Rules**
*Source: system-operations-rules.md*  
**Purpose**: System generation, maintenance, and operational excellence  
**When to Load**: During system operations, generation tasks, or maintenance activities

### **Shards & Loading Hints**

- **[System Generation Standards](./system-operations/system-generation.md)**
  - *Content*: Generation quality principles, architectural integrity, deployment readiness
  - *Load When*: Generating new systems, domain specialization
  - *Key Rules*: Quality preservation, architectural integrity, self-reference
  - *Size*: 5.7KB - Large load
  - *Critical For*: System generation

- **[Template Management Standards](./system-operations/template-management.md)**
  - *Content*: Template architecture, versioning, library governance
  - *Load When*: Creating/managing templates, template inheritance
  - *Key Rules*: Foundation authority, quality inheritance, consistency
  - *Size*: 3.5KB - Medium load

- **[File Management Standards](./system-operations/file-operations.md)**
  - *Content*: File analysis patterns, cleanup algorithms, user workflows
  - *Load When*: File reorganization, cleanup operations
  - *Key Rules*: Safe movement, link preservation, user control
  - *Size*: 5.2KB - Large load

- **[System Update Protocol](./system-operations/system-update-protocol.md)**
  - *Content*: Update phases, validation checklists, integration requirements
  - *Load When*: System-wide updates, protocol changes
  - *Key Rules*: 3-phase protocol, mandatory checklists
  - *Size*: 4.3KB - Medium load
  - *Critical For*: System updates

- **[System Architecture Operations](./system-operations/architecture-operations.md)**
  - *Content*: Health monitoring, maintenance operations
  - *Load When*: System health checks, maintenance planning
  - *Key Rules*: Health indicators, maintenance schedule
  - *Size*: 1.8KB - Quick load

- **[System Security Operations](./system-operations/security-operations.md)**
  - *Content*: Access control, security audits
  - *Load When*: Security reviews, access management
  - *Key Rules*: Access management, audit checklist
  - *Size*: 0.8KB - Quick load

- **[Performance Optimization](./system-operations/performance-optimization.md)**
  - *Content*: Performance standards, optimization strategies
  - *Load When*: Performance tuning, optimization planning
  - *Key Rules*: Response times, caching strategy
  - *Size*: 0.8KB - Quick load

- **[Emergency Procedures](./system-operations/emergency-procedures.md)**
  - *Content*: Recovery protocol, disaster recovery
  - *Load When*: System failures, emergency response
  - *Key Rules*: Emergency rollback, recovery procedure
  - *Size*: 0.9KB - Quick load
  - *Critical For*: Emergencies

- **[Operations Compliance & Governance](./system-operations/operations-governance.md)**
  - *Content*: Operational compliance, governance framework
  - *Load When*: Compliance reviews, governance decisions
  - *Key Rules*: Compliance requirements, decision authority
  - *Size*: 1.0KB - Quick load

---

## 🚀 **QUICK ACCESS BY TASK**

### **Common Tasks → Required Shards**

```yaml
TASK_BASED_LOADING:
  writing_code:
    - development/coding-standards.md
    - development/python-standards.md (if Python)
    - development/testing-standards.md
    
  creating_prd:
    - product-management/prd-writing.md
    - product-management/stakeholder-management.md
    
  organizing_files:
    - core-foundation/placement-standards.md
    - core-foundation/file-management.md
    - system-operations/file-operations.md
    
  system_update:
    - system-operations/system-update-protocol.md
    - system-operations/architecture-operations.md
    
  code_review:
    - development/code-review.md
    - development/linting-formatting.md
    - development/quality-metrics.md
    
  sprint_planning:
    - product-management/agile-sprint.md
    - product-management/backlog-management.md
    - product-management/metrics-reporting.md
```

## 💡 **LOADING OPTIMIZATION TIPS**

### **Bundle Loading Patterns**

```yaml
DOMAIN_BUNDLES:
  light_development:  # ~8KB total
    - development/coding-standards.md
    - development/code-review.md
    - development/linting-formatting.md
    
  full_development:  # ~22KB total
    - development/*.md  # Load all 10 shards
    
  product_essentials:  # ~12KB total
    - product-management/prd-writing.md
    - product-management/agile-sprint.md
    - product-management/backlog-management.md
    
  operations_core:  # ~13KB total
    - system-operations/system-generation.md
    - system-operations/template-management.md
    - system-operations/system-update-protocol.md
    
  emergency_kit:  # ~6KB total
    - system-operations/emergency-procedures.md
    - system-operations/architecture-operations.md
    - core-foundation/compliance-enforcement.md
```

### **Progressive Loading Strategy**

```yaml
PROGRESSIVE_LOADING:
  level_1_overview:  # Start here
    - INDEX.md (this file)
    
  level_2_task_specific:  # Load for specific task
    - 1-3 relevant shards
    
  level_3_domain_complete:  # For comprehensive work
    - All shards in one domain folder
    
  level_4_full_context:  # Rarely needed
    - Multiple domain folders
```

## 📊 **SHARD SIZE REFERENCE**

### **By Load Time Category**

```yaml
QUICK_LOAD:  # <1.5KB - Instant
  - 11 shards available
  - Load time: <50ms
  - Use for: Quick references, standards checks

SMALL_LOAD:  # 1.5-3KB - Fast
  - 9 shards available
  - Load time: <100ms
  - Use for: Specific guidance, focused tasks

MEDIUM_LOAD:  # 3-5KB - Moderate
  - 10 shards available
  - Load time: <200ms
  - Use for: Comprehensive guidance, complex tasks

LARGE_LOAD:  # >5KB - Substantial
  - 7 shards available
  - Load time: <500ms
  - Use for: Complete specifications, critical operations
```

## 🔄 **CONSOLIDATED FILES REFERENCE**

For backward compatibility or when needing complete domain coverage:

- **[core-foundation-rules.md](./core-foundation-rules.md)** - 771 lines, all core rules
- **[development-standards.md](./development-standards.md)** - 697 lines, all dev standards
- **[product-management-rules.md](./product-management-rules.md)** - 786 lines, all PM rules
- **[system-operations-rules.md](./system-operations-rules.md)** - 817 lines, all ops rules

*Note: Prefer sharded files for better performance and focused context*

---

**ENGINEERING RULES INDEX**: Your intelligent navigation system for 37 sharded engineering rules. Load smart, work efficient, maintain quality.