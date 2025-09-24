#!/bin/bash
# Demo script to show how reorganization indicators auto-update

echo "🔍 Reorganization Indicator Auto-Update Demo"
echo "============================================"
echo ""

# Function to update a single INDEX file
update_single_index() {
    local index_file=$1
    local dir=$(dirname "$index_file")
    
    echo "📁 Checking: $index_file"
    
    # Count actual items
    local file_count=$(find "$dir" -maxdepth 1 -type f 2>/dev/null | wc -l)
    local dir_count=$(find "$dir" -maxdepth 1 -type d ! -path "$dir" 2>/dev/null | wc -l)
    local max_depth=$(find "$dir" -type d 2>/dev/null | awk -F/ '{print NF}' | sort -n | tail -1)
    local total_files=$(find "$dir" -type f 2>/dev/null | wc -l)
    
    # Calculate complexity score (simplified for demo)
    local complexity=$(echo "scale=2; ($file_count/10)*0.4 + ($max_depth/3)*0.3 + ($total_files/50)*0.3" | bc)
    
    # Determine status
    local indicator
    if (( $(echo "$complexity > 2.0" | bc -l) )) || [ "$file_count" -gt 20 ]; then
        indicator="🔴 CRITICAL"
    elif (( $(echo "$complexity > 1.5" | bc -l) )) || [ "$file_count" -gt 15 ]; then
        indicator="🟡 WARNING"
    else
        indicator="🟢 HEALTHY"
    fi
    
    echo "  ├─ Files: $file_count | Subdirs: $dir_count"
    echo "  ├─ Depth: $max_depth levels | Total: $total_files files"
    echo "  ├─ Complexity Score: $complexity"
    echo "  └─ Status: $indicator"
    echo ""
}

# Example: Check the main INDEX files
echo "📊 Current Reorganization Status:"
echo "---------------------------------"

# Check Operations INDEX
if [ -f "nexus-base/operations/INDEX.md" ]; then
    update_single_index "nexus-base/operations/INDEX.md"
fi

# Check Features INDEX
if [ -f "nexus-base/workspace/features/INDEX.md" ]; then
    update_single_index "nexus-base/workspace/features/INDEX.md"
fi

# Check Framework INDEX
if [ -f "nexus-base/framework/INDEX.md" ]; then
    update_single_index "nexus-base/framework/INDEX.md"
fi

echo "✨ Auto-update complete!"
echo ""
echo "💡 To make this automatic:"
echo "  1. Run during system-sync (already integrated)"
echo "  2. Run on orchestrator activation (checks on load)"
echo "  3. Run manually: bash framework/tasks/organization/demo-update-indicators.sh"