# Full Documentation Update Workflow
**Type**: Complete Documentation Refresh  
**Category**: Documentation  
**Complexity**: High  
**Duration**: 1-3 days  
**Agents Required**: Orchestrator, Analyst, Developer, Architect

## Purpose

Execute a comprehensive documentation refresh for an entire system or major subsystem. This workflow provides systematic, quality-gated documentation updates across all components, APIs, architecture, and user guides.

## When to Use This Workflow

### Ideal Scenarios
- **Major Version Releases**: Significant system changes requiring comprehensive documentation updates
- **New Team Onboarding**: Complete documentation refresh to support new team members
- **Compliance Requirements**: Regulatory or audit requirements for complete documentation
- **Architecture Overhauls**: Significant system architecture changes
- **Quarterly Reviews**: Scheduled comprehensive documentation maintenance
- **Legacy System Modernization**: Updating documentation during system modernization

### Not Suitable For
- **Minor Updates**: Use `update-documentation` task for targeted changes
- **Single Component Changes**: Use component-specific update tasks
- **Emergency Fixes**: Use quick update tasks for urgent documentation fixes

## Workflow Parameters

### Required Parameters
- `system` (string): System or project name to document
- `scope` (string): Documentation scope (full|architecture|api|components|user-guides)

### Optional Parameters
- `baseline_assessment` (boolean): Perform comprehensive baseline assessment (default: true)
- `quality_level` (string): Target quality level (minimal|standard|excellence) (default: standard)
- `include_generated` (boolean): Include auto-generated documentation (default: true)
- `migration_guide` (boolean): Create migration guide for breaking changes (default: false)

### Workflow Invocation Examples
```bash
*workflow full-documentation-update system:payment-platform scope:full
*workflow full-documentation-update system:user-service scope:api quality_level:excellence
*workflow full-documentation-update system:legacy-system scope:architecture migration_guide:true
```

## Workflow Phases

### Phase 1: Discovery & Assessment (1-4 hours)
**Agent**: Analyst  
**Purpose**: Comprehensive analysis of current state and requirements

#### 1.1 System Analysis
**Agent Task**: Analyze the target system completely

**Analysis Areas**:
- **Codebase Structure**: Repository organization, main components, dependencies
- **Technology Stack**: Languages, frameworks, databases, external services
- **Architecture Patterns**: Design patterns, architectural decisions, system boundaries
- **API Inventory**: REST endpoints, GraphQL schemas, gRPC services, webhook definitions
- **Configuration Systems**: Environment variables, config files, feature flags
- **Deployment Architecture**: Infrastructure, containers, orchestration, environments

**Deliverables**:
- System analysis report
- Component inventory
- Technology stack documentation
- Architecture assessment

#### 1.2 Documentation Inventory
**Agent Task**: Catalog all existing documentation

**Inventory Process**:
```bash
# Find all documentation files
find . -name "*.md" -o -name "*.rst" -o -name "*.txt" | grep -v node_modules

# Identify documentation types
- README files
- API documentation
- Architecture documents  
- User guides
- Developer guides
- Deployment documentation
- Troubleshooting guides
```

**Assessment Criteria**:
- **Coverage**: What's documented vs what exists
- **Currency**: How up-to-date documentation is
- **Quality**: Current quality level assessment
- **Gaps**: What's missing or incomplete
- **Redundancy**: Duplicate or overlapping documentation

**Deliverables**:
- Documentation inventory report
- Gap analysis
- Quality assessment baseline
- Recommendation priorities

#### 1.3 Stakeholder Requirements
**Agent Task**: Gather documentation requirements from stakeholders

**Stakeholder Categories**:
- **Developers**: Technical implementation details, APIs, troubleshooting
- **DevOps**: Deployment, configuration, monitoring, maintenance
- **Product Managers**: Feature documentation, user workflows, business logic
- **End Users**: User guides, tutorials, FAQ
- **Compliance**: Regulatory documentation, security policies, audit trails

**Requirements Gathering**:
```markdown
## Documentation Requirements Survey

### For Developers
- What areas of the system are hardest to understand?
- What documentation is most frequently referenced?
- What's missing that would help development velocity?
- What examples or tutorials would be most valuable?

### For DevOps
- What deployment/configuration issues occur repeatedly?
- What monitoring and troubleshooting documentation is needed?
- What operational procedures need documentation?

### For Product/Business
- What user workflows need better documentation?
- What business logic is undocumented?
- What compliance documentation is required?
```

**Deliverables**:
- Stakeholder requirements document
- Priority matrix
- Success criteria definition
- Acceptance criteria for each documentation area

### Phase 2: Planning & Architecture (2-4 hours)
**Agent**: Architect  
**Purpose**: Design comprehensive documentation architecture and update plan

#### 2.1 Documentation Architecture Design
**Agent Task**: Design the complete documentation structure

**Information Architecture**:
```markdown
## Proposed Documentation Structure

### Core Documentation
docs/
├── README.md                          # Project overview and quick start
├── CHANGELOG.md                       # Version history and changes
├── CONTRIBUTING.md                    # Developer contribution guide
├── architecture/                      # System architecture documentation
│   ├── system-overview.md            # High-level system architecture
│   ├── component-architecture.md     # Detailed component design
│   ├── data-architecture.md          # Data models and flow
│   ├── security-architecture.md      # Security design and controls
│   └── deployment-architecture.md    # Infrastructure and deployment
├── api/                              # API documentation
│   ├── api-reference.md              # Complete API reference
│   ├── authentication.md             # Authentication methods
│   ├── webhooks.md                   # Webhook documentation
│   └── examples/                     # API usage examples
├── components/                       # Individual component documentation
│   ├── [component-name]/             # Per-component documentation
│   │   ├── README.md                 # Component overview
│   │   ├── configuration.md          # Configuration options
│   │   ├── troubleshooting.md        # Common issues and solutions
│   │   └── examples/                 # Usage examples
├── guides/                           # User and developer guides
│   ├── getting-started.md            # Quick start guide
│   ├── installation.md               # Installation instructions
│   ├── configuration.md              # Configuration guide
│   ├── deployment.md                 # Deployment procedures
│   ├── monitoring.md                 # Monitoring and observability
│   └── troubleshooting.md            # General troubleshooting
├── tutorials/                        # Step-by-step tutorials
├── reference/                        # Reference materials
│   ├── glossary.md                   # Terms and definitions
│   ├── configuration-reference.md    # All configuration options
│   └── error-codes.md                # Error codes and meanings
└── assets/                           # Images, diagrams, examples
    ├── images/                       # Documentation images
    ├── diagrams/                     # Architecture diagrams
    └── examples/                     # Code and configuration examples
```

**Content Strategy**:
- **Layered Information**: Overview → Details → Reference
- **Audience Segmentation**: Role-based documentation paths
- **Progressive Disclosure**: Basic → Intermediate → Advanced content
- **Cross-Linking Strategy**: Logical navigation between related topics

**Deliverables**:
- Complete documentation architecture plan
- Content strategy document
- Template selection and customization plan
- Navigation and cross-linking strategy

#### 2.2 Update Implementation Plan
**Agent Task**: Create detailed implementation plan with phases and quality gates

**Implementation Phases**:
```yaml
# Documentation Update Phases
phase_1_foundation:
  duration: "4-8 hours"
  agent: "architect"
  deliverables:
    - system-overview.md
    - project README.md  
    - basic architecture documentation
  quality_gate: "Architecture documentation complete and accurate"

phase_2_api_documentation:
  duration: "6-12 hours"  
  agent: "developer"
  deliverables:
    - complete API reference
    - authentication documentation
    - API examples and tutorials
  quality_gate: "All APIs documented with working examples"

phase_3_component_documentation:
  duration: "8-16 hours"
  agent: "developer"  
  deliverables:
    - individual component guides
    - configuration documentation
    - troubleshooting guides
  quality_gate: "All major components documented"

phase_4_user_guides:
  duration: "4-8 hours"
  agent: "analyst"
  deliverables:
    - installation and setup guides
    - user tutorials and workflows
    - administrative guides
  quality_gate: "Complete user journey documentation"

phase_5_integration_validation:
  duration: "2-4 hours"
  agent: "orchestrator"
  deliverables:
    - integrated documentation review
    - cross-reference validation
    - final quality assessment
  quality_gate: "All documentation integrated and validated"
```

**Quality Gates**:
Each phase must pass quality validation before proceeding:
- **PASS**: Phase complete, ready for next phase
- **CONCERNS**: Minor issues, can proceed with noted items
- **FAIL**: Significant issues, phase must be repeated
- **WAIVED**: Issues accepted with explicit justification

**Deliverables**:
- Detailed implementation timeline
- Agent assignment plan
- Quality gate definitions
- Risk assessment and mitigation plan

### Phase 3: Foundation Documentation (4-8 hours)
**Agent**: Architect  
**Purpose**: Create core system and architecture documentation

#### 3.1 System Overview Documentation
**Agent Task**: Create comprehensive system overview

**System Overview Content**:
```markdown
# [System Name] - System Overview
**Purpose**: [What this system does and why it exists]
**Scope**: [What this system handles and what it doesn't]
**Audience**: [Who should read this document]

## Executive Summary
[2-3 paragraphs explaining the system at a high level]

## System Context
[How this system fits into the larger ecosystem]

## Core Capabilities
[Primary functions and features the system provides]

## Technology Stack
[High-level technology choices and rationale]

## Key Architectural Decisions
[Important design decisions and trade-offs]

## System Boundaries
[What's in scope vs out of scope]
```

**Quality Validation**:
- [ ] Accurate high-level system description
- [ ] Clear business context and value proposition
- [ ] Technology stack properly documented
- [ ] Architectural decisions explained with rationale

#### 3.2 Architecture Documentation
**Agent Task**: Create detailed architecture documentation using system-architecture template

**Architecture Content Areas**:
- **System Architecture**: Overall system design and component interactions
- **Data Architecture**: Data models, flows, and storage strategies  
- **Security Architecture**: Security controls, authentication, authorization
- **Deployment Architecture**: Infrastructure, environments, deployment patterns
- **Integration Architecture**: External system integrations and APIs

**Diagram Requirements**:
```markdown
# Required Architecture Diagrams
1. System Context Diagram - system boundaries and external interactions
2. Component Architecture - internal component relationships
3. Data Flow Diagram - how data moves through the system
4. Deployment Diagram - infrastructure and deployment topology
5. Security Architecture - security controls and data protection
```

**Quality Validation**:
- [ ] All architectural aspects covered comprehensively
- [ ] Diagrams accurately represent current implementation
- [ ] Architecture decisions documented with context
- [ ] Technical debt and constraints clearly noted

#### 3.3 Project Documentation
**Agent Task**: Create or update project-level documentation

**Project Documentation**:
- **README.md**: Project overview, quick start, basic usage
- **CONTRIBUTING.md**: Development guidelines, contribution process
- **CHANGELOG.md**: Version history and change documentation
- **LICENSE**: License information and terms

**Quality Validation**:
- [ ] README provides clear project overview and quick start
- [ ] Contributing guidelines are comprehensive and current
- [ ] Change log is complete and up-to-date
- [ ] All necessary project files are present

### Phase 4: API Documentation (6-12 hours)
**Agent**: Developer  
**Purpose**: Comprehensive API documentation with examples and testing

#### 4.1 API Reference Documentation  
**Agent Task**: Create complete API reference using api-reference template

**API Documentation Requirements**:
```markdown
# API Documentation Checklist
- [ ] All endpoints documented with complete parameters
- [ ] Request/response formats with real examples
- [ ] Authentication methods and examples
- [ ] Error codes with descriptions and resolution steps
- [ ] Rate limiting information
- [ ] SDK/client library examples
- [ ] Webhook documentation (if applicable)
- [ ] API versioning strategy
```

**Code Example Requirements**:
```bash
# All API examples must be tested and working
curl -X POST https://api.example.com/v1/users \
  -H "Authorization: Bearer token" \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Response example
{
  "id": "user_123",
  "name": "John Doe", 
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Quality Validation**:
- [ ] All public APIs documented completely
- [ ] All code examples tested and working
- [ ] Authentication methods clearly explained
- [ ] Error handling comprehensively documented

#### 4.2 API Usage Guides
**Agent Task**: Create API usage guides and tutorials

**API Guide Content**:
- **Getting Started**: Authentication setup, first API call
- **Common Workflows**: Typical API usage patterns
- **Advanced Usage**: Complex scenarios and integrations
- **Best Practices**: Performance, security, error handling
- **Migration Guides**: Version upgrade information (if needed)

**Quality Validation**:
- [ ] Clear getting started guide with working examples
- [ ] Common use cases documented with examples
- [ ] Best practices and security guidance provided
- [ ] Migration information complete (if applicable)

### Phase 5: Component Documentation (8-16 hours)
**Agent**: Developer  
**Purpose**: Individual component and service documentation

#### 5.1 Component Guide Creation
**Agent Task**: Document each major component using component-guide template

**Component Documentation Process**:
```markdown
# For each major component/service:
1. Create component guide from template
2. Document component purpose and scope
3. Define interfaces and contracts
4. Document configuration options
5. Provide usage examples
6. Document troubleshooting approaches
7. Include performance characteristics
```

**Component Categories**:
- **Core Services**: Main business logic components
- **Infrastructure Components**: Database, cache, message queue interfaces
- **Integration Components**: External service integrations
- **Utility Components**: Shared utilities and libraries

**Quality Validation**:
- [ ] All major components have comprehensive guides
- [ ] Interface contracts clearly documented
- [ ] Configuration options complete with examples
- [ ] Troubleshooting information practical and actionable

#### 5.2 Configuration Documentation
**Agent Task**: Create comprehensive configuration reference

**Configuration Documentation**:
```markdown
# Configuration Reference Structure
## Environment Variables
| Variable | Required | Default | Description | Example |
|----------|----------|---------|-------------|---------|
| API_KEY | Yes | - | External service API key | sk_test_123 |

## Configuration Files
### config/database.yaml
```yaml
database:
  host: localhost
  port: 5432
  name: app_db
  pool_size: 10
```

## Feature Flags
### Available Flags
- new_feature_enabled: Enable new feature (default: false)
- legacy_support: Support legacy API (default: true)
```

**Quality Validation**:
- [ ] All configuration options documented
- [ ] Default values and ranges specified
- [ ] Environment-specific variations noted
- [ ] Security considerations highlighted

### Phase 6: User Documentation (4-8 hours)
**Agent**: Analyst  
**Purpose**: End-user and operational documentation

#### 6.1 Installation & Setup Guides
**Agent Task**: Create comprehensive setup documentation

**Setup Documentation Structure**:
```markdown
# Installation Guide Structure
## Prerequisites  
- System requirements
- Dependencies  
- Access requirements

## Installation Steps
1. Download/clone instructions
2. Dependency installation
3. Configuration setup
4. Database setup (if needed)
5. First run verification

## Environment Setup
- Development environment
- Staging environment  
- Production considerations

## Troubleshooting Common Setup Issues
- Common error messages and solutions
- Verification steps
- Getting help resources
```

**Quality Validation**:
- [ ] Installation steps tested on clean environment
- [ ] All prerequisites clearly listed
- [ ] Troubleshooting covers common issues
- [ ] Instructions work for target skill level

#### 6.2 User Workflows & Tutorials
**Agent Task**: Create user-focused documentation

**User Documentation Areas**:
- **Getting Started**: First-time user experience
- **Common Tasks**: Frequently performed operations
- **Advanced Features**: Power user capabilities  
- **Administration**: System administration tasks
- **Troubleshooting**: End-user problem resolution

**Tutorial Structure**:
```markdown
# Tutorial Template
## Objective
[What the user will accomplish]

## Prerequisites  
[What the user needs before starting]

## Steps
1. [Detailed step with expected outcome]
2. [Next step with screenshots if helpful]
3. [Validation step to confirm success]

## Next Steps
[What to do after completing this tutorial]

## Troubleshooting
[Common issues and resolutions]
```

**Quality Validation**:
- [ ] Tutorials tested by non-expert users
- [ ] Screenshots/examples current and accurate
- [ ] User workflows cover major use cases
- [ ] Administrative procedures complete

### Phase 7: Integration & Validation (2-4 hours)
**Agent**: Orchestrator  
**Purpose**: Final integration, validation, and quality assurance

#### 7.1 Documentation Integration
**Agent Task**: Integrate all documentation pieces into cohesive whole

**Integration Tasks**:
```markdown
# Documentation Integration Checklist
- [ ] Create master navigation/index
- [ ] Validate all cross-references and links
- [ ] Ensure consistent formatting across all documents  
- [ ] Create searchable structure
- [ ] Generate table of contents
- [ ] Update all metadata and version information
```

**Navigation Structure**:
```markdown
# Documentation Navigation
## Quick Start
- [Getting Started](guides/getting-started.md)
- [Installation](guides/installation.md)  
- [First Steps](tutorials/first-steps.md)

## Architecture & Design
- [System Overview](architecture/system-overview.md)
- [Component Architecture](architecture/component-architecture.md)
- [API Design](api/api-reference.md)

## Developer Resources
- [API Reference](api/api-reference.md)
- [Component Guides](components/)
- [Configuration Reference](reference/configuration-reference.md)

## Operations
- [Deployment](guides/deployment.md)
- [Monitoring](guides/monitoring.md)
- [Troubleshooting](guides/troubleshooting.md)
```

**Quality Validation**:
- [ ] All internal links validated and working
- [ ] Navigation logical and complete
- [ ] Cross-references accurate and helpful
- [ ] Documentation structure intuitive

#### 7.2 Final Quality Assessment
**Agent Task**: Comprehensive quality validation using documentation quality criteria

**Quality Assessment Framework**:
```markdown
# Final Quality Assessment
## Accuracy (Critical)
- [ ] All technical information verified as correct
- [ ] Code examples tested and working  
- [ ] Version information current and accurate
- [ ] Links validated and functional

## Completeness (Critical)  
- [ ] All required sections present and complete
- [ ] Stakeholder requirements addressed
- [ ] No significant gaps in coverage
- [ ] Migration information complete (if needed)

## Clarity (High Priority)
- [ ] Clear, professional writing throughout
- [ ] Appropriate technical depth for audience
- [ ] Logical organization and flow
- [ ] Consistent terminology and style

## Currency (High Priority)
- [ ] All information reflects current implementation
- [ ] Change logs updated appropriately
- [ ] Version numbers aligned with software
- [ ] Deprecation notices current

## Usability (Medium Priority)
- [ ] Easy navigation and findability
- [ ] Good use of examples and illustrations
- [ ] Clear next steps and calls to action
- [ ] Appropriate depth for different skill levels
```

**Overall Quality Gate Decision**:
- **PASS**: Documentation meets all quality criteria, ready for publication
- **CONCERNS**: Minor issues identified, acceptable with noted improvements
- **FAIL**: Significant quality issues, major revisions required  
- **WAIVED**: Quality issues acknowledged but accepted with business justification

#### 7.3 Publication & Distribution
**Agent Task**: Publish completed documentation and notify stakeholders

**Publication Process**:
```markdown
# Documentation Publication
1. **Version Control**
   - Commit all documentation changes
   - Tag with appropriate version
   - Create release notes

2. **Distribution**
   - Update documentation site/wiki
   - Notify relevant teams and stakeholders
   - Update internal documentation indices

3. **Validation**
   - Verify published documentation is accessible
   - Test key workflows and examples
   - Confirm search functionality working

4. **Communication**
   - Send completion notification
   - Highlight major improvements
   - Provide feedback collection mechanism
```

**Success Communication**:
```markdown
# Documentation Update Complete

## Summary
Completed comprehensive documentation update for [System Name]

## Key Improvements
- ✅ 100% API coverage with working examples
- ✅ Complete architecture documentation with diagrams
- ✅ All major components documented
- ✅ User guides and tutorials updated
- ✅ Quality gates: PASS

## Statistics
- Documents updated: [count]
- New documentation: [count]  
- Quality score: [rating]
- Completion time: [hours]

## What's New
- [Key improvement 1]
- [Key improvement 2]
- [Key improvement 3]

## Next Steps
- Regular maintenance schedule established
- Feedback collection process active
- Quarterly review scheduled for [date]
```

## Deliverables & Artifacts

### Primary Deliverables
1. **Complete Documentation Suite**: All documentation updated and integrated
2. **Quality Assessment Report**: Final quality validation results
3. **Update Summary**: Comprehensive summary of changes and improvements
4. **Publication Confirmation**: Verification that documentation is live and accessible

### Supporting Artifacts
- **System Analysis Report**: Technical analysis of current system state
- **Documentation Architecture**: Information architecture and content strategy
- **Implementation Timeline**: Actual vs planned timeline with lessons learned
- **Quality Gate Results**: Results from each phase quality validation
- **Stakeholder Communication**: Summary of requirements and feedback

## Success Metrics

### Quantitative Metrics
- **Coverage**: Percentage of system components documented
- **Quality Score**: Average quality gate scores across all phases  
- **Completeness**: Percentage of identified requirements addressed
- **Accuracy**: Percentage of technical information validated as correct

### Qualitative Metrics  
- **Stakeholder Satisfaction**: Feedback from documentation users
- **Usability**: Ease of finding and using documentation
- **Maintainability**: How easy documentation will be to keep current
- **Business Impact**: Improvement in developer productivity, user satisfaction

### Success Criteria
- [ ] All major system components documented
- [ ] 100% of public APIs documented with examples
- [ ] All stakeholder requirements addressed
- [ ] Quality gates achieved: 90% PASS, 10% CONCERNS maximum
- [ ] Documentation architecture implemented as planned
- [ ] Publication successful with stakeholder notification complete

## Risk Management

### Common Risks & Mitigation

**Risk**: Technical complexity exceeds planned timeline  
**Mitigation**: Break complex components into phases, extend timeline if needed, focus on critical-path items first

**Risk**: Information sources unavailable or unreliable  
**Mitigation**: Identify multiple information sources, engage subject matter experts early, document assumptions

**Risk**: Quality validation failures  
**Mitigation**: Implement progressive quality checks, involve stakeholders in reviews, plan for iteration cycles

**Risk**: Stakeholder requirements change during process  
**Mitigation**: Lock requirements after planning phase, manage scope creep, plan for requirements evolution

### Escalation Triggers
- Multiple quality gate failures across phases
- Critical information sources unavailable  
- Timeline exceeds planned duration by >50%
- Stakeholder requirements fundamentally change
- Technical accuracy cannot be verified

## Context Integration

### Memory System Integration
```markdown
# Documentation workflow memory
workspace/memory/documentation/full-update-[date].md:
  system: [target-system]
  duration: [actual-hours]  
  quality_results: [summary]
  lessons_learned: [key-insights]
  follow_up_actions: [remaining-items]
```

### Feature Integration
For systems with active features, coordinate with:
- `workspace/features/active/[feature]/docs/`
- `workspace/features/completed/[feature]/documentation.md`

### Agent Handoff Summary
```markdown
# Workflow Completion Handoff
## System State
- Documentation: Complete and published
- Quality: [Overall gate result]  
- Coverage: [Percentage completion]

## Outstanding Items
- [Any remaining work items]
- [Follow-up actions needed]
- [Maintenance schedule established]

## Resources Created
- [List of major documentation artifacts]
- [Links to published documentation]
- [Quality assessment reports]
```

---
**Workflow Status**: Active  
**Quality Level**: Level 2 - Standard Documentation  
**Integration**: Full nexus Quality Framework  
**Version**: 1.0.0  
**Owner**: Documentation Team