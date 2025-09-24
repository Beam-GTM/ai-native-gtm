# Feature Workspace
**Version**: 3.2.0  
**Purpose**: Active feature development and tracking

## Directory Structure
```
workspace/features/
├── FEATURES.md           # This file - feature registry
├── active/              # Currently active features
│   ├── README.md        # Active features guide
│   └── {feature}/       # Feature workspace
│       ├── plan.md      # Feature plan and requirements
│       ├── context.md   # Current state and decisions
│       ├── progress.md  # Implementation tracking
│       ├── decisions.md # Architecture decisions record
│       └── quality.md   # Quality gates tracking
├── completed/           # Completed features (last 30 days)
│   ├── README.md        # Completed features guide
│   └── {date}-{feature}/
├── patterns/            # Extracted patterns
│   ├── README.md        # Pattern guide
│   ├── solutions/       # Solution patterns
│   ├── workflows/       # Workflow patterns
│   ├── architectures/   # Architecture patterns
│   └── quality/         # Quality patterns
├── archive/             # Archived features (>30 days)
└── templates/           # Feature templates
    ├── feature-plan.md
    ├── feature-context.md
    └── feature-progress.md
```

## Active Features

| Feature | Status | Started | Target | Owner |
|---------|--------|---------|--------|-------|
| close-chat-workflow | Planned | 2025-08-26 | 2025-08-27 | Framework Team |
| orchestrator-template-synchronization | Planned | 2025-08-26 | TBD | Framework Team |
| memory-learnings-consolidation | Planned | 2025-08-26 | TBD | Framework Team |

## Feature Lifecycle

### 1. Initialize Feature
```bash
*feature init [name]
```
Creates:
- `active/{name}/plan.md` - Planning document
- `active/{name}/context.md` - Working context
- `active/{name}/progress.md` - Progress tracking

### 2. Work on Feature
```bash
*feature work [name]
```
- Loads feature context
- Updates progress automatically
- Tracks decisions with quality gates

### 3. Complete Feature
```bash
*feature complete [name]
```
- Runs quality validation
- Extracts patterns if applicable
- Moves to completed/

### 4. Archive Feature
After 30 days in completed/, features auto-archive to `.archive/`

## Feature Templates

### Plan Template (plan.md)
```markdown
# Feature: {Name}
**ID**: {feature-id}
**Started**: {date}
**Target**: {date}
**Priority**: high|medium|low

## Problem Statement
What problem are we solving?

## Success Criteria
- [ ] Measurable outcome 1
- [ ] Measurable outcome 2
- [ ] Measurable outcome 3

## Technical Approach
How will we solve this?

## Dependencies
- Dependency 1
- Dependency 2

## Risks
- Risk 1: Mitigation strategy
- Risk 2: Mitigation strategy
```

### Context Template (context.md)
```markdown
# Feature Context: {Name}
**Updated**: {timestamp}
**Phase**: planning|implementing|testing|validating

## Current Focus
What we're working on right now

## Recent Decisions
| Date | Decision | Rationale | Status |
|------|----------|-----------|--------|
| {date} | {decision} | {why} | PASS/CONCERNS |

## Active Blockers
- [ ] Blocker 1
- [ ] Blocker 2

## Next Actions
1. Immediate next step
2. Following step
3. After that
```

### Progress Template (progress.md)
```markdown
# Progress: {Feature Name}
**Completion**: {0-100}%
**Health**: 🟢 On Track | 🟡 At Risk | 🔴 Blocked

## Completed Tasks
- [x] Task 1 - {date}
- [x] Task 2 - {date}

## In Progress
- [ ] Current task (50%)
- [ ] Another task (20%)

## Upcoming
- [ ] Future task
- [ ] Another future task

## Metrics
- Lines of Code: {count}
- Tests Written: {count}
- Documentation: {status}
- Quality Gates Passed: {x}/{total}
```

## Pattern Extraction

### Tracking Patterns
Monitor features for:
1. **Repeated Solutions** (>3 occurrences)
2. **Common Workflows** (>2 features use same process)
3. **Architectural Patterns** (design patterns that work)
4. **Quality Issues** (recurring problems)

### Extraction Process
1. Identify pattern in completed features
2. Document in `patterns/{pattern-name}.md`
3. Create template if applicable
4. Update registry/components.md
5. Consider creating specialist agent

## Quality Integration

### Feature Quality Gates
Each feature must pass:
- [ ] Design Review (before implementation)
- [ ] Code Quality (during implementation)
- [ ] Testing Complete (before validation)
- [ ] Documentation Complete (before complete)
- [ ] Final Validation (before archival)

### Decision Framework
All decisions use: **PASS** | **CONCERNS** | **FAIL** | **WAIVED**

## Orchestrator Commands

### Feature Management
- `*feature init [name]` - Start new feature
- `*feature list` - Show all features
- `*feature status [name]` - Detailed feature status
- `*feature work [name]` - Switch to feature context
- `*feature update [name]` - Update progress
- `*feature complete [name]` - Mark complete
- `*feature archive` - Archive old features

### Pattern Management  
- `*pattern extract [feature]` - Extract patterns
- `*pattern list` - Show identified patterns
- `*pattern apply [pattern]` - Apply pattern to current work

## Metrics & Reporting

### Feature Metrics
Track per feature:
- Cycle Time (init → complete)
- Complexity Score (1-10)
- Quality Score (gates passed)
- Pattern Matches (reusable elements)

### System Metrics
- Active Features: 3
- Completed This Month: 10
- Patterns Extracted: 4
- Average Cycle Time: 1.5 days

## Integration Points

### With Orchestrator
- Orchestrator reads this registry
- Updates feature context during work
- Manages feature lifecycle
- Extracts patterns automatically

### With Components Registry
- Successful patterns → components
- Feature metrics inform evolution
- Components reference origin features

### With Quality System
- All features pass quality gates
- Decisions tracked consistently
- Evidence collected for validation