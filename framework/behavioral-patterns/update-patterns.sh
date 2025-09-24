#!/bin/bash
# Behavioral Pattern Update Script - Centralized Pattern Management
# Purpose: Automate pattern updates with versioning and validation

set -e  # Exit on error

# Configuration
REGISTRY="behavioral-patterns-registry.yaml"
BACKUP_DIR="archive"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
DATE=$(date +%Y-%m-%d)

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Behavioral Pattern Update System ===${NC}"
echo "Registry: $REGISTRY"
echo "Timestamp: $TIMESTAMP"
echo ""

# Function to validate YAML
validate_yaml() {
    python3 -c "import yaml; yaml.safe_load(open('$1'))" 2>/dev/null
    return $?
}

# Function to count patterns
count_patterns() {
    grep "^  [a-z_]*:" "$1" | grep -v "^  #" | wc -l
}

# Function to extract pattern names
get_pattern_names() {
    grep "^  [a-z_]*:" "$1" | grep -v "^  #" | sed 's/://g' | sed 's/^  //'
}

# 1. Check if registry exists
if [ ! -f "$REGISTRY" ]; then
    echo -e "${RED}ERROR: Registry file not found: $REGISTRY${NC}"
    exit 1
fi

# 2. Create backup
echo "📦 Creating backup..."
mkdir -p "$BACKUP_DIR"
BACKUP_FILE="$BACKUP_DIR/registry-$TIMESTAMP.yaml"
cp "$REGISTRY" "$BACKUP_FILE"
echo -e "${GREEN}✓ Backup created: $BACKUP_FILE${NC}"

# 3. Validate current registry
echo ""
echo "🔍 Validating current registry..."
if validate_yaml "$REGISTRY"; then
    echo -e "${GREEN}✓ Current registry is valid YAML${NC}"
else
    echo -e "${RED}✗ Current registry has invalid YAML syntax${NC}"
    exit 1
fi

# 4. Count patterns
echo ""
echo "📊 Analyzing patterns..."
PATTERN_COUNT=$(count_patterns "$REGISTRY")
echo "Found $PATTERN_COUNT patterns:"
get_pattern_names "$REGISTRY" | while read pattern; do
    echo "  - $pattern"
done

# 5. Update metadata
echo ""
echo "📝 Updating metadata..."
# Update last_updated date
if grep -q "last_updated:" "$REGISTRY"; then
    sed -i.tmp "s/last_updated: .*/last_updated: \"$DATE\"/" "$REGISTRY"
    rm -f "$REGISTRY.tmp"
    echo -e "${GREEN}✓ Updated last_updated to $DATE${NC}"
fi

# 6. Validate after updates
echo ""
echo "🔍 Validating updated registry..."
if validate_yaml "$REGISTRY"; then
    echo -e "${GREEN}✓ Updated registry is valid${NC}"
else
    echo -e "${RED}✗ Updated registry has invalid syntax - rolling back${NC}"
    cp "$BACKUP_FILE" "$REGISTRY"
    exit 1
fi

# 7. Generate pattern statistics
echo ""
echo "📈 Generating pattern statistics..."
cat > PATTERN-STATISTICS.md << EOF
# Behavioral Pattern Statistics
**Generated**: $DATE $TIMESTAMP
**Total Patterns**: $PATTERN_COUNT
**Registry Version**: $(grep "version:" "$REGISTRY" | head -1 | cut -d'"' -f2)

## Pattern Coverage
EOF

# Calculate total coverage
grep "failure_rate:" "$REGISTRY" | while read line; do
    rate=$(echo "$line" | grep -oE "[0-9]+")
    echo "- Pattern prevents: ${rate}% of failures"
done >> PATTERN-STATISTICS.md

# 8. Generate update report
echo ""
echo "📄 Generating update report..."
cat > LAST-UPDATE.md << EOF
# Last Pattern Registry Update
**Date**: $DATE
**Time**: $TIMESTAMP
**Pattern Count**: $PATTERN_COUNT
**Registry**: $REGISTRY
**Backup**: $BACKUP_FILE

## Patterns in Registry
$(get_pattern_names "$REGISTRY" | sed 's/^/- /')

## Validation Status
- YAML Syntax: ✅ Valid
- Pattern Count: $PATTERN_COUNT patterns
- Backup Created: ✅ $BACKUP_FILE

## Next Steps
1. Review changes in $REGISTRY
2. Test pattern loading in templates
3. Commit changes if satisfactory
EOF

echo -e "${GREEN}✓ Update report generated: LAST-UPDATE.md${NC}"

# 9. Show diff if changes were made
echo ""
echo "📋 Changes from backup:"
if diff -q "$BACKUP_FILE" "$REGISTRY" > /dev/null; then
    echo "No changes detected (metadata update only)"
else
    echo -e "${YELLOW}Changes detected:${NC}"
    diff -u "$BACKUP_FILE" "$REGISTRY" | head -20 || true
fi

# 10. Final summary
echo ""
echo -e "${GREEN}=== Update Complete ===${NC}"
echo "✅ Registry validated and updated"
echo "✅ Backup created at: $BACKUP_FILE"
echo "✅ Statistics generated: PATTERN-STATISTICS.md"
echo "✅ Update report: LAST-UPDATE.md"
echo ""
echo "Pattern Registry Status:"
echo "  Patterns: $PATTERN_COUNT"
echo "  Version: $(grep "version:" "$REGISTRY" | head -1 | cut -d'"' -f2)"
echo "  Updated: $DATE"

# Optional: Git operations
if [ "$1" = "--commit" ]; then
    echo ""
    echo "📤 Committing changes..."
    git add "$REGISTRY" LAST-UPDATE.md PATTERN-STATISTICS.md
    git commit -m "Update behavioral patterns: $PATTERN_COUNT patterns, $DATE"
    echo -e "${GREEN}✓ Changes committed${NC}"
fi

echo ""
echo "💡 Tip: Run with --commit to automatically commit changes"