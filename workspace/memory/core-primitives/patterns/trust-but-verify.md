# Pattern: Trust But Verify

**Identified**: 2025-08-26T00:50:00Z  
**Severity**: HIGH  
**Category**: System Integrity

## Pattern Description
LLMs may update indices and documentation with counts or claims without verifying against actual filesystem state. This can lead to drift between documented structure and reality.

## Observed Behavior
During system-sync execution:
1. LLM updated INDEX files with counts (workflows: 2, tasks: 7)
2. Did not verify these counts against actual filesystem
3. User prompted verification revealed discrepancies:
   - Workflows were actually 3 (not 2)
   - Tasks were actually 10 (not 7)
   - Missing tasks in SYSTEM-STRUCTURE.md

## Root Cause
- Assumption-based updates rather than verification-based
- Not implementing "trust but verify" principle
- Relying on previous state without checking current reality

## Mitigation Strategy
```yaml
always_verify:
  before_claiming: "Check filesystem first"
  after_updating: "Verify changes match reality"
  
  implementation:
    - Count actual files before updating counts
    - List actual directories before updating lists
    - Verify existence before adding references
    - Audit after sync to ensure accuracy
```

## Code Pattern to Add
```yaml
# In any INDEX or structure update task:
verification_step:
  description: "Trust but verify - audit claims against filesystem"
  actions:
    - ls actual_directory | count
    - compare to INDEX claim
    - correct if mismatch
  rule: "NEVER trust, ALWAYS verify"
```

## Learning Applied
- Added filesystem verification step to system-sync task
- Added audit phase to update-all-indices task  
- Updated project memory with this learning
- Created this pattern documentation

## Future Prevention
1. Always use `ls` or filesystem check before claiming counts
2. Implement verification loops in all update tasks
3. Add "trust but verify" as engineering rule
4. Include filesystem audit in quality gates

## Related Patterns
- overengineering.md (tendency to add complexity without verification)
- assumption-based-execution.md (acting on assumptions vs facts)