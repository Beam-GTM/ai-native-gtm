# Behavioral Pattern Update Guide
**Version**: 1.0  
**Purpose**: How to update behavioral patterns in the centralized registry  
**Architecture**: Reference-based pattern loading system

## 🎯 Update Process Overview

### Single Point of Update
All behavioral patterns are managed in **ONE central location**:
- **Registry File**: `framework/behavioral-patterns/behavioral-patterns-registry.yaml`
- **No Template Updates Required**: Templates use references, automatically get updates
- **No Agent Updates Required**: Agents load registry through static activation

## 📝 How to Update Patterns

### 1. Adding a New Pattern

Edit `behavioral-patterns-registry.yaml` and add to the `patterns` section:

```yaml
patterns:
  your_new_pattern:
    id: "pattern-id"
    name: "Pattern Name"
    failure_rate: "X%"
    severity: "critical|high|medium"
    description: "What this pattern prevents"
    
    pre_execution_check:
      question: "Check question"
      validation: "Validation approach"
      evidence_required: "Evidence needed"
    
    activation_trigger: |
      {{#behavioral_check}}
      **🧠 PATTERN CHECK**
      - [ ] Your check items
      {{/behavioral_check}}
    
    post_completion_validation: |
      **🧠 PATTERN VALIDATION**
      - [ ] Your validation items
```

### 2. Updating Existing Patterns

Simply edit the pattern in the registry:
1. Open `behavioral-patterns-registry.yaml`
2. Find the pattern to update
3. Make changes
4. Update `metadata.last_updated`
5. Save

**That's it!** All templates and agents automatically use the updated pattern.

### 3. Adding Patterns to Pattern Sets

Update the `loading_references` section to include your pattern in appropriate sets:

```yaml
loading_references:
  critical_patterns:
    - execution_documentation_paradox
    - false_completion_syndrome
    - basic_operations_failure
    - your_new_pattern  # Add here if critical
```

## 🔄 Version Management

### Pattern Versioning
```yaml
metadata:
  version: "1.1"  # Increment for significant changes
  last_updated: "2025-08-28"
  changelog:
    - "1.1: Added new_pattern_name"
    - "1.0: Initial registry with 5 core patterns"
```

### Backup Before Major Updates
```bash
# Create versioned backup
cp behavioral-patterns-registry.yaml \
   archive/behavioral-patterns-registry-v$(date +%Y%m%d).yaml
```

## 🚀 Update Script (Automated)

Create `update-patterns.sh`:

```bash
#!/bin/bash
# Behavioral Pattern Update Script

REGISTRY="framework/behavioral-patterns/behavioral-patterns-registry.yaml"
BACKUP_DIR="framework/behavioral-patterns/archive"

# 1. Create backup
echo "Creating backup..."
mkdir -p $BACKUP_DIR
cp $REGISTRY "$BACKUP_DIR/registry-$(date +%Y%m%d-%H%M%S).yaml"

# 2. Update timestamp in registry
echo "Updating timestamp..."
sed -i "s/last_updated: .*/last_updated: \"$(date +%Y-%m-%d)\"/" $REGISTRY

# 3. Validate YAML syntax
echo "Validating YAML..."
python -c "import yaml; yaml.safe_load(open('$REGISTRY'))" || {
    echo "ERROR: Invalid YAML syntax!"
    exit 1
}

# 4. Count patterns
PATTERN_COUNT=$(grep -c "^  [a-z_]*:$" $REGISTRY | head -1)
echo "Registry contains $PATTERN_COUNT patterns"

# 5. Generate update report
echo "Generating update report..."
cat > LAST-UPDATE.md << EOF
# Last Pattern Update
**Date**: $(date +%Y-%m-%d)
**Patterns**: $PATTERN_COUNT
**Registry**: $REGISTRY
**Backup**: $BACKUP_DIR/registry-$(date +%Y%m%d-%H%M%S).yaml
EOF

echo "✅ Pattern update complete!"
```

## 📊 Pattern Metrics Tracking

Track pattern effectiveness in `PATTERN-METRICS.yaml`:

```yaml
pattern_metrics:
  execution_documentation_paradox:
    occurrences_prevented: 0
    last_triggered: null
    effectiveness_score: null
    
  # Update these based on actual usage
```

## 🔍 Testing Pattern Updates

### Manual Testing
1. Load a template that uses the pattern
2. Verify pattern text appears correctly
3. Check that behavioral checks are properly formatted

### Automated Testing
```python
# test-patterns.py
import yaml

def test_pattern_registry():
    with open('behavioral-patterns-registry.yaml', 'r') as f:
        registry = yaml.safe_load(f)
    
    # Check all patterns have required fields
    for pattern_id, pattern in registry['patterns'].items():
        assert 'id' in pattern
        assert 'name' in pattern
        assert 'failure_rate' in pattern
        assert 'activation_trigger' in pattern
        print(f"✓ Pattern {pattern_id} valid")
    
    print(f"✅ All {len(registry['patterns'])} patterns valid")

if __name__ == "__main__":
    test_pattern_registry()
```

## 🎯 Benefits of Centralized Updates

### What You DON'T Need to Do:
- ❌ Update individual templates
- ❌ Update agent files
- ❌ Search for pattern references
- ❌ Worry about version mismatches
- ❌ Maintain multiple pattern files

### What You DO:
- ✅ Edit ONE file: `behavioral-patterns-registry.yaml`
- ✅ All templates automatically use updated patterns
- ✅ All agents get updates through static activation
- ✅ Version control tracks all changes in one place

## 🔄 Update Frequency

### Recommended Schedule
- **Weekly**: Review pattern effectiveness
- **Monthly**: Update patterns based on new learnings
- **Quarterly**: Major pattern additions/revisions

### Trigger-Based Updates
- **New Learning**: When core learnings reveal new patterns
- **Pattern Failure**: When pattern doesn't prevent expected failure
- **Coverage Gap**: When new failure type discovered

## 📝 Update Checklist

When updating patterns:
- [ ] Back up current registry
- [ ] Make pattern changes
- [ ] Update metadata version and date
- [ ] Validate YAML syntax
- [ ] Test pattern loading
- [ ] Document changes in changelog
- [ ] Update PATTERN-METRICS.yaml if needed
- [ ] Commit with descriptive message

## 🚨 Important Notes

1. **No Cascade Updates Required**: Beauty of reference-based system
2. **Instant Propagation**: Next template/agent load uses new patterns
3. **No Restart Required**: Changes effective immediately
4. **Version Control Friendly**: All changes in one file

## Example Update Workflow

```bash
# 1. Create feature branch
git checkout -b update-behavioral-patterns

# 2. Edit registry
vim framework/behavioral-patterns/behavioral-patterns-registry.yaml

# 3. Run update script
./update-patterns.sh

# 4. Test changes
python test-patterns.py

# 5. Commit
git add -A
git commit -m "Update behavioral patterns: [description]"

# 6. Push
git push origin update-behavioral-patterns
```

---

**The power of centralization**: Update once, apply everywhere. This is the architectural advantage of reference-based pattern loading!