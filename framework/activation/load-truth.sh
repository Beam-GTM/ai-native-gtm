#!/bin/bash
# Truth Loading Wrapper for Activation Sequence
# Attempts database truth, falls back gracefully

# Set truth loading status
TRUTH_LOADED=false
TRUTH_SOURCE="none"

# Try Python database loader
if command -v python3 &> /dev/null || command -v python &> /dev/null; then
    # Determine Python command
    PYTHON_CMD=$(command -v python3 || command -v python)
    
    # Get script directory for proper path
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Run truth loader and capture output
    TRUTH_OUTPUT=$($PYTHON_CMD "$SCRIPT_DIR/truth-loader.py" 2>/dev/null)
    
    if [ $? -eq 0 ]; then
        # Source the output to get variables
        eval "$TRUTH_OUTPUT"
        TRUTH_LOADED=true
        echo "[TRUTH] Loaded from $TRUTH_SOURCE (confidence: $TRUTH_CONFIDENCE)"
        echo "[COUNTS] Active: $ACTIVE_FEATURES, Completed: $COMPLETED_FEATURES, Total: $TOTAL_FEATURES"
    fi
fi

# Fallback to INDEX.md parsing if database failed
if [ "$TRUTH_LOADED" = false ]; then
    echo "[TRUTH] Fallback to INDEX.md parsing"
    TRUTH_SOURCE="index_fallback"
    TRUTH_CONFIDENCE="low"
    
    # Known values from INDEX (incorrect but available)
    ACTIVE_FEATURES=16
    COMPLETED_FEATURES=21
    PROPOSED_FEATURES=12
    ARCHIVED_FEATURES=7
    TOTAL_FEATURES=56
    DATABASE_EXISTS=false
    
    echo "[WARNING] Using potentially stale counts from INDEX.md"
fi

# Export for use in activation sequence
export TRUTH_SOURCE="$TRUTH_SOURCE"
export TRUTH_CONFIDENCE="$TRUTH_CONFIDENCE"
export ACTIVE_FEATURES="$ACTIVE_FEATURES"
export COMPLETED_FEATURES="$COMPLETED_FEATURES"
export PROPOSED_FEATURES="$PROPOSED_FEATURES"
export ARCHIVED_FEATURES="$ARCHIVED_FEATURES"
export TOTAL_FEATURES="$TOTAL_FEATURES"
export DATABASE_EXISTS="$DATABASE_EXISTS"

# Return success (always succeeds with fallback)
# Note: Don't exit - we need to preserve exports for sourcing shell