<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Performance Optimization

## 📊 **PERFORMANCE OPTIMIZATION**

### **Performance Standards**
```yaml
response_times:
  command_execution: <100ms
  agent_switching: <200ms
  context_loading: <500ms
  workflow_initiation: <1s

resource_usage:
  memory_baseline: <256MB
  cpu_idle: <5%
  disk_io: Optimized
  network: Minimal
```

### **Optimization Strategies**
```yaml
caching_strategy:
  - Context caching per session
  - Template caching
  - Cross-reference indexing
  - Command history

lazy_loading:
  - Load resources on demand
  - Progressive context loading
  - Deferred template expansion
  - Just-in-time compilation
```

