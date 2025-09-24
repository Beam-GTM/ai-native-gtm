<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:40.925460Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.275173Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Update Reorganization Indicators Task
**Version**: 1.0.0
**Type**: automation-task
**Trigger**: Automatic on INDEX.md load or manual execution
**Purpose**: Dynamically update reorganization indicators in INDEX files with real metrics

## Execution Protocol

### Phase 1: Scan Directory Structure
```bash
# For each INDEX.md file with REORGANIZATION-TRIGGER
for index_file in $(grep -l "REORGANIZATION-TRIGGER" **/INDEX.md); do
    dir=$(dirname "$index_file")
    
    # Calculate metrics
    item_count=$(find "$dir" -maxdepth 1 -type f | wc -l)
    subdir_count=$(find "$dir" -maxdepth 1 -type d | wc -l)
    max_depth=$(find "$dir" -type d | awk -F/ '{print NF}' | sort -n | tail -1)
    total_items=$(find "$dir" -type f | wc -l)
    
    # Calculate complexity score
    complexity=$(echo "scale=2; ($item_count/10)*0.4 + ($max_depth/3)*0.3 + ($total_items/50)*0.3" | bc)
done
```

### Phase 2: Determine Status
```yaml
status_calculation:
  critical:
    condition: "complexity > 2.0 OR items > 20 OR depth > 5"
    indicator: "🔴 CRITICAL"
    
  warning:
    condition: "complexity > 1.5 OR items > 15 OR depth > 4"
    indicator: "🟡 WARNING"
    
  healthy:
    condition: "complexity <= 1.5 AND items <= 15 AND depth <= 4"
    indicator: "🟢 HEALTHY"
```

### Phase 3: Update INDEX Files
```yaml
update_pattern:
  find_block: |
    <!-- REORGANIZATION-CHECK
    ...existing content...
    -->
    
  replace_with: |
    <!-- REORGANIZATION-CHECK
      Status: {calculated_indicator}
      Items: {actual_count}/{threshold} {item_type}
      Depth: {actual_depth}/{max_depth} levels
      Total: {total_items} files
      Score: {complexity_score} ({status_range})
      Action: {recommended_action}
      Updated: {timestamp}
    -->
```

## Integration Points

### 1. Orchestrator Activation
Add to orchestrator.md activation sequence (Step 10.5):
```yaml
reorganization_check:
  trigger: "After loading INDEX files"
  action: "Execute update-reorganization-indicators.md"
  scope: "All loaded INDEX.md files"
  timing: "Parallel with menu generation"
```

### 2. System-Sync Integration
Add to system-sync.md workflow:
```yaml
phase_2.5_reorganization_check:
  description: "Update reorganization indicators"
  task: "framework/tasks/organization/update-reorganization-indicators.md"
  when: "After index updates, before validation"
```

### 3. Close-Chat Integration
Add to close-chat workflow:
```yaml
engine_3_cleanup:
  reorganization_check:
    task: "update-reorganization-indicators.md"
    purpose: "Flag folders needing cleanup before next session"
```

## Automation Script

### Bash Implementation
```bash
#!/bin/bash
# update-reorganization-indicators.sh

update_index_indicators() {
    local index_file=$1
    local dir=$(dirname "$index_file")
    
    # Calculate real metrics
    local items=$(ls -1 "$dir" 2>/dev/null | wc -l)
    local subdirs=$(find "$dir" -maxdepth 1 -type d ! -path "$dir" | wc -l)
    local depth=$(find "$dir" -type d | awk -F/ '{print NF}' | sort -n | tail -1)
    local total=$(find "$dir" -type f 2>/dev/null | wc -l)
    
    # Calculate complexity (using awk for decimal math)
    local complexity=$(awk "BEGIN {print ($items/10)*0.4 + ($depth/3)*0.3 + ($total/50)*0.3}")
    
    # Determine status
    local status indicator action
    if (( $(echo "$complexity > 2.0" | bc -l) )); then
        status="CRITICAL"
        indicator="🔴 CRITICAL"
        action="Immediate reorganization needed"
    elif (( $(echo "$complexity > 1.5" | bc -l) )); then
        status="WARNING" 
        indicator="🟡 WARNING"
        action="Consider reorganization soon"
    else
        status="HEALTHY"
        indicator="🟢 HEALTHY"
        action="Structure is well-organized"
    fi
    
    # Update the INDEX file
    update_block="<!-- REORGANIZATION-CHECK
  Status: $indicator
  Items: $items/20 files ($subdirs subdirs)
  Depth: $depth/5 levels
  Total: $total files
  Score: $complexity ($status range)
  Action: $action
  Updated: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
-->"
    
    # Use sed to update between the markers
    sed -i '/<!-- REORGANIZATION-CHECK/,/-->/{
        c\
'"$update_block"'
    }' "$index_file"
    
    echo "✅ Updated $index_file: $indicator (score: $complexity)"
}

# Main execution
echo "🔍 Scanning for INDEX files with reorganization triggers..."

for index in $(find . -name "INDEX.md" -exec grep -l "REORGANIZATION-TRIGGER" {} \;); do
    update_index_indicators "$index"
done

echo "✨ Reorganization indicators updated!"
```

## Python Alternative
```python
#!/usr/bin/env python3
# update_reorganization_indicators.py

import os
import re
from pathlib import Path
from datetime import datetime

def calculate_metrics(directory):
    """Calculate folder metrics"""
    items = len(os.listdir(directory))
    subdirs = sum(1 for d in os.listdir(directory) 
                  if os.path.isdir(os.path.join(directory, d)))
    
    # Calculate depth
    max_depth = 0
    for root, dirs, files in os.walk(directory):
        depth = root.replace(directory, '').count(os.sep)
        if depth > max_depth:
            max_depth = depth
    
    # Total files
    total_files = sum(len(files) for _, _, files in os.walk(directory))
    
    # Complexity score
    complexity = (items/10)*0.4 + (max_depth/3)*0.3 + (total_files/50)*0.3
    
    return {
        'items': items,
        'subdirs': subdirs,
        'depth': max_depth,
        'total': total_files,
        'complexity': round(complexity, 2)
    }

def determine_status(metrics):
    """Determine reorganization status"""
    complexity = metrics['complexity']
    
    if complexity > 2.0 or metrics['items'] > 20 or metrics['depth'] > 5:
        return {
            'indicator': '🔴 CRITICAL',
            'status': 'CRITICAL',
            'action': 'Immediate reorganization needed'
        }
    elif complexity > 1.5 or metrics['items'] > 15 or metrics['depth'] > 4:
        return {
            'indicator': '🟡 WARNING',
            'status': 'WARNING',
            'action': 'Consider reorganization soon'
        }
    else:
        return {
            'indicator': '🟢 HEALTHY',
            'status': 'HEALTHY',
            'action': 'Structure is well-organized'
        }

def update_index_file(index_path):
    """Update INDEX.md with real metrics"""
    directory = os.path.dirname(index_path)
    metrics = calculate_metrics(directory)
    status = determine_status(metrics)
    
    # Create update block
    update_block = f"""<!-- REORGANIZATION-CHECK
  Status: {status['indicator']}
  Items: {metrics['items']}/20 files ({metrics['subdirs']} subdirs)
  Depth: {metrics['depth']}/5 levels
  Total: {metrics['total']} files
  Score: {metrics['complexity']} ({status['status']} range)
  Action: {status['action']}
  Updated: {datetime.utcnow().isoformat()}Z
-->"""
    
    # Read file
    with open(index_path, 'r') as f:
        content = f.read()
    
    # Update content
    pattern = r'<!-- REORGANIZATION-CHECK.*?-->'
    updated = re.sub(pattern, update_block, content, flags=re.DOTALL)
    
    # Write back
    with open(index_path, 'w') as f:
        f.write(updated)
    
    print(f"✅ Updated {index_path}: {status['indicator']} (score: {metrics['complexity']})")

# Main execution
if __name__ == "__main__":
    print("🔍 Scanning for INDEX files with reorganization triggers...")
    
    for index_file in Path('.').rglob('INDEX.md'):
        with open(index_file) as f:
            if 'REORGANIZATION-TRIGGER' in f.read():
                update_index_file(index_file)
    
    print("✨ Reorganization indicators updated!")
```

## Manual Execution

### Quick Update Command
```bash
# One-liner to update all indicators
find . -name "INDEX.md" -exec grep -l "REORGANIZATION-TRIGGER" {} \; | xargs -I {} bash -c 'framework/tasks/organization/update-reorganization-indicators.sh {}'
```

### Verification Command
```bash
# Check current status of all indicators
grep -A 7 "REORGANIZATION-CHECK" **/INDEX.md | grep "Status:"
```

## Expected Output Example

### Before (Static)
```markdown
<!-- REORGANIZATION-CHECK
  Status: 🟢 HEALTHY
  Items: 4/20 subdirs
  Depth: 2/5 levels
  Total: ~50 files
  Score: 0.8 (Healthy range)
  Action: Structure is well-organized
-->
```

### After (Dynamic)
```markdown
<!-- REORGANIZATION-CHECK
  Status: 🟡 WARNING
  Items: 18/20 files (8 subdirs)
  Depth: 4/5 levels
  Total: 127 files
  Score: 1.7 (WARNING range)
  Action: Consider reorganization soon
  Updated: 2025-08-27T01:15:30Z
-->
```

## Quality Gates

### Validation Checklist
- [ ] Script correctly counts items in directories
- [ ] Depth calculation is accurate
- [ ] Complexity formula produces valid scores
- [ ] Status thresholds align with cleanup task
- [ ] INDEX files update without corruption
- [ ] Timestamps reflect actual update time

## Error Handling

### Common Issues
1. **Permission denied**: Check read permissions on directories
2. **INDEX corruption**: Backup before updating
3. **Missing bc/awk**: Install required tools
4. **Pattern mismatch**: Verify REORGANIZATION-CHECK format

### Recovery
```bash
# Restore from backup if update fails
cp INDEX.md.bak INDEX.md

# Validate INDEX structure
grep -c "REORGANIZATION-TRIGGER" INDEX.md
grep -c "REORGANIZATION-CHECK" INDEX.md
```

---
*Task created: 2025-08-27*
*Auto-updates reorganization indicators in INDEX files*