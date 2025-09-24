# Nexus-Base Operations Manifest
**Version**: 3.2.0  
**Strategy**: Dynamic Lazy Loading  
**Updated**: 2025-08-29T08:33:00Z (System Sync Phase 4)
**Architecture**: Lean Feature-Driven with Pattern-Based Growth

## Resource Registry (Verified 2025-08-29T08:33:00Z)

### Agents (17 Total - Updated)
- **Index**: `operations/agents/INDEX.md`
- **Categories**: core (3), specialists (5), coordinators (3), experimental (1)
- **Verified Count**: 17 agent files found via filesystem scan
- **Loading**: On-demand via `*agent [name]`
- **Growth Pattern**: Extract specialist when task handled >3x/week
- **Dependency Health**: 23% (Phase 2 validation - needs improvement)

### Workflows (12 Total - Updated)
- **Index**: `framework/workflows/INDEX.md`
- **Operations**: 2 active workflows
- **Framework**: 10 framework workflows (plan-feature, implement-feature, close-chat, etc.)
- **Loading**: On-demand via `*workflow [name]`
- **Growth Pattern**: Extract workflow when pattern used >2x/week

### Tasks (43 Total - Updated)
- **Index**: `framework/tasks/` directory
- **Active**: All system-sync, validation, memory, and analysis tasks
- **Super Task**: system-sync.md orchestrates 5-phase maintenance (validated)
- **Loading**: On-demand via `*task [name]`
- **Growth Pattern**: Extract task when specific operation repeated >5x/week
- **Critical Tasks**: validate-bidirectional-dependencies.md (Phase 2 executed)

### Features (35 Total - Updated)
- **Registry**: `workspace/features/INDEX.md`
- **Active**: 16 feature directories (filesystem verified)
- **Completed**: 19 feature directories (filesystem verified)
- **Templates**: `framework/templates/features/` (centralized)
- **Pattern Extraction**: Automatic from completed features
- **Dependency Coverage**: 3% of feature files have dependency metadata (needs improvement)

### Templates (194 Total - Updated)
- **Framework**: `framework/templates/` (centralized registry)
- **YAML Templates**: 194 template files (filesystem count)
- **Categories**: agents, features, workflows, tasks, system
- **Loading**: On-demand during generation

### Engineering Rules (0 Active - Consolidated)
- **Status**: Consolidated/migrated to other framework components
- **Previous**: 39 rules across 4 categories
- **Current**: Engineering principles integrated into templates and workflows
- **Compliance**: Via template validation and quality gates

## Loading Strategy

### Bootstrap (Always Loaded)
```yaml
files:
  - orchestrator.md (self)
  - operations/MANIFEST.md (this file)
  - SYSTEM-STRUCTURE.md (system map)
timing: On activation
size: ~500 lines total
```

### Discovery (On Help/Menu)
```yaml
files:
  - operations/agents/INDEX.md
  - operations/workflows/INDEX.md
  - operations/tasks/INDEX.md
timing: On first interaction
size: ~30 lines per index
```

### Feature Context (On Activation)
```yaml
pattern: "*feature work {name}" → workspace/features/active/{name}/*.md
files:
  - plan.md
  - context.md
  - progress.md
timing: On feature selection
```

### Resource Loading (On Command)
```yaml
pattern: "*{command} {name}" → {type}/{category}/{name}.md
examples:
  - *agent developer → agents/specialists/developer.md
  - *workflow development → workflows/development.md
  - *feature init test → creates workspace/features/active/test/
timing: On command execution
```

## Resolution Patterns

### Command Resolution Chain
1. Parse command and arguments
2. Check cache for loaded resource
3. Determine resource type (agent/workflow/task/feature)
4. Load index if not cached
5. Resolve to specific file path
6. Load resource file
7. Follow cascading references
8. Cache for session

### Path Resolution
```yaml
agents:
  pattern: agents/{category}/{name}.md
  categories: [core, specialists, coordinators, experimental]
  
workflows:
  pattern: workflows/{name}.md
  current: [development]
  
tasks:
  pattern: tasks/{category}/{name}.md
  categories: [] # Will grow as patterns emerge
  
features:
  pattern: workspace/features/active/{name}/*.md
  lifecycle: active → completed → patterns → archive
```

## Quality Framework

### Decision Gates
All decisions use: **PASS** | **CONCERNS** | **FAIL** | **WAIVED**

### Feature Quality Gates
- Design Review (before implementation)
- Code Quality (during implementation)
- Testing Complete (before validation)
- Documentation Complete (before complete)
- Final Validation (before archival)

## Cache Management

### Caching Strategy
- **Session Cache**: Resources cached for current session
- **Feature Cache**: Active feature context retained
- **Index Cache**: Indices cached after first load
- **Clear Pattern**: Cache cleared on `*exit` or feature complete

## Performance Metrics

### Target Performance
| Metric | Target | Method |
|--------|--------|--------|
| Activation | <20ms | Load only bootstrap |
| Help Display | <50ms | Use indices only |
| Command Exec | <100ms | Direct resolution |
| Memory Usage | <64KB | Lazy loading |
| Feature Switch | <200ms | Context preservation |

## Growth Triggers

### Pattern Recognition
Monitor for:
- **Agent Tasks**: Same type >3x/week → Extract specialist
- **Workflow Patterns**: Same sequence >2x/week → Extract workflow
- **Task Repetition**: Same operation >5x/week → Extract task
- **Feature Success**: Pattern in 3+ features → Extract to framework

### Expansion Protocol
1. Identify pattern emergence
2. Document in patterns/
3. Extract minimal definition
4. Update relevant index
5. Test integration
6. Update MANIFEST.md

## System Evolution Path
```
V3.1 (Current) → Pattern Emergence → Component Extraction → Registry Update → V3.2
│
├── 11 Agents → Monitor usage → Extract when needed
├── 1 Workflow → Track patterns → Add workflows
├── 0 Tasks → Observe repetition → Create tasks
└── Features → Extract patterns → Build components
```

## Critical System Maintenance

### System Synchronization Commands
- `*sync` - Full system synchronization (recommended daily)
- `*sync-check` - Dry run to preview changes
- `*sync-structure` - Update SYSTEM-STRUCTURE.md only
- `*sync-indices` - Update all INDEX files
- `*sync-validate` - Run dependency validation
- `*maintenance` - Interactive maintenance menu

### Auto-Trigger Conditions
- **On Startup**: Check if last sync >24h ago → Recommend sync
- **Critical Alert**: If last sync >48h ago → Urgent sync warning
- **Feature Complete**: Prompt for sync after feature completion
- **Milestone Reached**: Force sync before milestones

### Maintenance Task Locations
- **Super Task**: framework/tasks/system/system-sync.md
- **Structure Update**: framework/tasks/system/update-system-structure.md
- **Index Updates**: framework/tasks/system/update-all-indices.md
- **Dependency Check**: framework/tasks/validation/validate-dependencies.md
- **Workflow**: operations/workflows/system-maintenance.md

## Navigation Integration
- **Entry Point**: CLAUDE.md (orchestrator configuration)
- **Manifest**: operations/MANIFEST.md (this file)
- **Indices**: Dynamic loading from INDEX.md files
- **Features**: workspace/features/FEATURES.md
- **Framework**: framework/FRAMEWORK.md