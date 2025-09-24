# Development Workflow
**Workflow ID**: development  
**Category**: core  
**Priority**: HIGH  
**Type**: Sequential with quality gates  

## Purpose
Standard development workflow for implementing features with integrated quality checks and validation gates.

## When to Use
- Implementing new features
- Making significant code changes
- Refactoring existing functionality
- Bug fixes requiring validation

## Workflow Stages

### Stage 1: Planning
**Agent**: architect  
**Tasks**:
- Review requirements
- Design technical approach
- Identify dependencies
- Create implementation plan

**Quality Gate**: Design Review
- [ ] Requirements understood
- [ ] Technical approach documented
- [ ] Dependencies identified
- [ ] Risk assessment complete

### Stage 2: Implementation
**Agent**: developer  
**Tasks**:
- Write code following standards
- Implement unit tests
- Update documentation
- Follow engineering rules

**Quality Gate**: Code Quality
- [ ] Code follows standards
- [ ] Tests implemented
- [ ] Documentation updated
- [ ] No linting errors

### Stage 3: Testing
**Agent**: quality-assurance  
**Tasks**:
- Run test suites
- Perform integration testing
- Validate functionality
- Check edge cases

**Quality Gate**: Testing Complete
- [ ] All tests passing
- [ ] Coverage adequate (>80%)
- [ ] Integration verified
- [ ] Edge cases handled

### Stage 4: Review
**Agent**: architect  
**Tasks**:
- Review implementation
- Validate architecture
- Check best practices
- Approve changes

**Quality Gate**: Final Review
- [ ] Architecture approved
- [ ] Best practices followed
- [ ] Performance acceptable
- [ ] Security validated

### Stage 5: Documentation
**Agent**: developer  
**Tasks**:
- Update technical docs
- Create user documentation
- Update README if needed
- Document API changes

**Quality Gate**: Documentation Complete
- [ ] Technical docs current
- [ ] User docs updated
- [ ] README accurate
- [ ] API documented

## Workflow Configuration

```yaml
workflow:
  type: sequential
  allow_skip: false
  require_gates: true
  
stages:
  planning:
    agent: architect
    duration: "30-60 min"
    deliverables: ["design-doc", "tech-spec"]
    
  implementation:
    agent: developer
    duration: "2-8 hours"
    deliverables: ["code", "tests", "docs"]
    
  testing:
    agent: quality-assurance
    duration: "1-2 hours"
    deliverables: ["test-report", "coverage-report"]
    
  review:
    agent: architect
    duration: "30-60 min"
    deliverables: ["review-report", "approval"]
    
  documentation:
    agent: developer
    duration: "30-60 min"
    deliverables: ["docs", "readme", "api-docs"]
```

## Quality Framework

### Decision Gates
All gates use: PASS | CONCERNS | FAIL | WAIVED

### Gate Criteria
- **PASS**: All criteria met, ready to proceed
- **CONCERNS**: Minor issues, can proceed with notes
- **FAIL**: Critical issues, must resolve before proceeding
- **WAIVED**: Issues documented, explicitly approved to proceed

## Integration Points

### Prerequisites
- Feature requirements defined
- Development environment ready
- Dependencies available
- Tests framework configured

### Triggers
- Feature ticket assigned
- Bug report prioritized
- Refactoring approved
- Technical debt identified

### Outputs
- Implemented feature/fix
- Test coverage report
- Documentation updates
- Quality gate approvals

## Usage Examples

### Start Workflow
```bash
*workflow development --feature="user-authentication"
```

### Skip to Stage
```bash
*workflow development --stage=testing
```

### Check Status
```bash
*workflow status development
```

## Success Criteria
- [ ] All stages completed
- [ ] All quality gates passed
- [ ] Documentation updated
- [ ] Tests passing
- [ ] Code reviewed and approved

## Related Resources
- Engineering Rules: framework/engineeringrules/
- Quality Standards: framework/engineeringrules/core-foundation/quality-assurance.md
- Coding Standards: framework/engineeringrules/development/coding-standards.md
- Testing Standards: framework/engineeringrules/development/testing-standards.md