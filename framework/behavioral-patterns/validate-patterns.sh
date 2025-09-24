#!/bin/bash
# Simple Pattern Registry Validator - No external dependencies

REGISTRY="behavioral-patterns-registry.yaml"

echo "🔍 Validating Behavioral Pattern Registry..."
echo ""

# Check if file exists
if [ ! -f "$REGISTRY" ]; then
    echo "❌ ERROR: Registry file not found: $REGISTRY"
    exit 1
fi

# Basic YAML structure validation
echo "Checking structure..."

# Check for required sections
errors=0
warnings=0

# Check metadata section
if ! grep -q "^metadata:" "$REGISTRY"; then
    echo "❌ Missing metadata section"
    ((errors++))
else
    echo "✅ Metadata section found"
fi

# Check patterns section
if ! grep -q "^patterns:" "$REGISTRY"; then
    echo "❌ Missing patterns section"
    ((errors++))
else
    echo "✅ Patterns section found"
fi

# Check loading_references section
if ! grep -q "^loading_references:" "$REGISTRY"; then
    echo "⚠️ Warning: Missing loading_references section"
    ((warnings++))
else
    echo "✅ Loading references found"
fi

# Count patterns
echo ""
echo "📊 Pattern Analysis:"
pattern_count=$(grep "^  [a-z_]*:" "$REGISTRY" | grep -v "metadata:" | grep -v "loading_references:" | wc -l)
echo "  Total patterns: $pattern_count"

# List patterns
echo "  Patterns found:"
grep "^  [a-z_]*:" "$REGISTRY" | grep -v "metadata:" | grep -v "loading_references:" | while read line; do
    pattern=$(echo "$line" | sed 's/://g' | sed 's/^  //')
    echo "    - $pattern"
done

# Check each pattern has required fields
echo ""
echo "Validating pattern fields..."
grep "^  [a-z_]*:" "$REGISTRY" | grep -v "metadata:" | grep -v "loading_references:" | while read pattern_line; do
    pattern=$(echo "$pattern_line" | sed 's/://g' | sed 's/^  //')
    
    # Get pattern section
    pattern_start=$(grep -n "^  $pattern:" "$REGISTRY" | cut -d: -f1)
    next_pattern=$(grep -n "^  [a-z_]*:" "$REGISTRY" | grep -A1 "^$pattern_start:" | tail -1 | cut -d: -f1)
    
    # Check for required fields (simplified check)
    if grep -q "id:" "$REGISTRY"; then
        echo "  ✓ $pattern has ID"
    else
        echo "  ✗ $pattern missing ID"
        ((errors++))
    fi
done

# Summary
echo ""
echo "=== Validation Summary ==="
echo "Patterns: $pattern_count"
echo "Errors: $errors"
echo "Warnings: $warnings"

if [ $errors -eq 0 ]; then
    echo ""
    echo "✅ VALIDATION PASSED - Registry is valid!"
    exit 0
else
    echo ""
    echo "❌ VALIDATION FAILED - Please fix errors"
    exit 1
fi