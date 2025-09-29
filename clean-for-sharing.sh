#!/bin/bash
echo "🧹 Cleaning Nexus template for sharing..."

# Remove personal company data
echo "Removing personal company data..."
rm -rf Companies/Allied-Global
rm -rf Companies/Booth-and-Partners
rm -rf Companies/Fraisa
rm -rf Companies/ICS
rm -rf Companies/Maersk
rm -rf Companies/Rivertrace
rm -rf Companies/SCG
rm -rf Companies/Sportsbet
rm -rf Companies/Userled
rm -rf Companies/Ryno
rm -rf Companies/Beurer

# Remove personal workspace data
echo "Removing personal workspace data..."
rm -rf workspace/memory/active/*
rm -rf workspace/memory/consolidated/*
rm -rf workspace/memory/core-primitives/chat-sessions/*
rm -rf workspace/memory/core-primitives/learnings/*
rm -rf workspace/memory/core-primitives/patterns/*
rm -rf workspace/memory/patterns/*
rm -rf workspace/memory/session-reports/*
rm -rf workspace/memory/sessions/*
rm -rf workspace/data-output/*
rm -f workspace/memory/project-memory.md
rm -f workspace/memory/system-sync-state.yaml
rm -rf workspace/features/active/ai-native-gtm/01-Framework/01-Prospecting/*
rm -rf workspace/features/active/ai-native-gtm/01-Framework/02-Lead-Generation/*
rm -rf workspace/features/active/ai-native-gtm/01-Framework/03-Discovery/*
rm -rf workspace/features/active/ai-native-gtm/01-Framework/04-Pipeline/*
rm -rf workspace/features/active/ai-native-gtm/01-Framework/06-Integration/*
rm -rf workspace/features/active/ai-native-gtm/02-Operations/*
rm -rf workspace/features/active/demo-agent-automation/*
rm -rf workspace/features/active/onboarding-experience/*
rm -rf workspace/features/active/transcript-processing-automation/*
rm -rf workspace/features/completed/*
rm -rf workspace/features/proposed/*
rm -rf workspace/inputs/*

# Remove personal notes
echo "Removing personal notes..."
rm -rf personal/

# Create clean workspace structure
mkdir -p workspace/memory/active
mkdir -p workspace/memory/consolidated
mkdir -p workspace/memory/core-primitives/chat-sessions
mkdir -p workspace/memory/core-primitives/learnings
mkdir -p workspace/memory/core-primitives/patterns
mkdir -p workspace/memory/patterns
mkdir -p workspace/memory/session-reports
mkdir -p workspace/memory/sessions
mkdir -p workspace/data-output
mkdir -p workspace/features/active
mkdir -p workspace/features/completed
mkdir -p workspace/features/proposed
mkdir -p workspace/inputs/learnings/schemas

# Create a placeholder project-memory.md
echo "# PROJECT MEMORY | Clean Template" > workspace/memory/project-memory.md
echo "- This is a clean template for sharing." >> workspace/memory/project-memory.md
echo "- All personal data has been removed." >> workspace/memory/project-memory.md

# Create example company structure
mkdir -p examples/Companies/Example-Company/transcripts/processed
mkdir -p examples/Companies/Example-Company/emails/outbound
mkdir -p examples/Companies/Example-Company/documents

# Create example workspace features
mkdir -p examples/workspace/features/active/example-feature
mkdir -p examples/workspace/memory/core-primitives

echo "✅ Nexus template cleaned for sharing"
echo "📁 What's included:"
echo "   - Complete framework/ (core system)"
echo "   - Complete operations/ (agents and workflows)"
echo "   - Complete structure/ (blueprints)"
echo "   - Complete briefing/ (templates)"
echo "   - Complete docs/ (documentation)"
echo "   - Clean workspace/ (structure only)"
echo "   - Examples/ (example implementations)"
echo ""
echo "📁 What's removed:"
echo "   - Personal company data"
echo "   - Personal workspace data"
echo "   - Personal notes and projects"
echo "   - Sensitive configuration files"
