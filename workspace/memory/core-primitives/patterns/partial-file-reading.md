# Pattern: Partial File Reading Default

**Identified**: 2025-08-26T01:10:00Z  
**Severity**: CRITICAL  
**Category**: Tool Behavior

## Pattern Description
The Read tool documentation states "By default, it reads up to 2000 lines" but LLMs often specify small limits (20-30 lines) to save tokens, missing critical content.

## Observed Behavior
1. Read tool WITHOUT limit parameter: Reads ENTIRE file ✅
2. Read tool WITH limit=20: Only reads first 20 lines ❌
3. LLM tendency: Often adds limit=20 or limit=30 "to be efficient"
4. Result: Missing 90%+ of file content

## Real Examples
- developer.md: 190 lines total, often read with limit=20 (missing 170 lines)
- design-new-feature.md: 837 lines, read with limit=100 (missing 737 lines)  
- system-sync.md: 388 lines, might read limit=50 (missing 338 lines)

## Root Cause
- Token conservation instinct
- Assumption that important content is at top
- Not checking total file length first
- Default behavior to add limits

## Critical Impact
For INDEX updates:
- Missing metadata deeper in files
- Can't validate full content
- Incomplete extraction
- False confidence in partial data

## Mitigation Strategy
```yaml
correct_reading_pattern:
  step_1: "Check file size first"
    command: wc -l filename.md
    
  step_2: "Read based on size"
    if_small: (<100 lines): Read without limit
    if_medium: (100-500 lines): Read without limit or full
    if_large: (>500 lines): Read first 200 for metadata
    
  never_do:
    - Add arbitrary limit=20 or limit=30
    - Assume top has all metadata
    - Read without knowing size
```

## Implementation Fix for update-indices-with-content
```python
def read_file_for_metadata(filepath):
    # FIRST: Check file size
    line_count = bash(f"wc -l {filepath}").split()[0]
    
    if int(line_count) <= 200:
        # Small file: read entirely
        content = read_file(filepath)  # NO LIMIT
    else:
        # Large file: read enough for metadata
        content = read_file(filepath, limit=100)
        # Log that partial read occurred
        log(f"Partial read: {filepath} has {line_count} lines, read 100")
    
    return content
```

## Learning Applied
Must update update-indices-with-content.md task to:
1. Always check file size first
2. Read entire small files
3. Document when partial reads occur
4. Never use arbitrary small limits

## Related Patterns
- trust-but-verify.md (verification of content)
- content-blind-updates.md (not reading files at all)

---
**Critical Insight**: The Read tool reads ENTIRE files when no limit specified. Stop adding unnecessary limits!