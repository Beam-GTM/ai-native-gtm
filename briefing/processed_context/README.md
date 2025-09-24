# 📁 Processed Context Archive

## 🎯 What This Folder Contains

This folder automatically stores your processed project context files after the system analyzes them for personalization.

## 📂 Archive Structure

Each context processing session creates a timestamped folder:

```
processed_context/
├── README.md                           # This file
├── context-2024-01-15-14-30-22/       # Processing session 1
│   ├── original_files/                 # Your original files
│   │   ├── my-project.md
│   │   ├── requirements.txt
│   │   └── api-spec.yaml
│   ├── analysis_report.md              # What the system extracted
│   ├── personalization_log.md          # How system was customized
│   └── archive_manifest.md             # Summary of this processing
├── context-2024-01-20-09-15-45/       # Processing session 2 (if you add more context later)
│   └── ...
└── latest -> context-2024-01-20-09-15-45/  # Symlink to most recent
```

## 🔄 Automatic Processing

### When Context is Processed:
1. **You add files** → `../context_input/` folder
2. **System detects** → Files during startup
3. **Analysis happens** → AI extracts project info
4. **Files get moved** → To timestamped archive here
5. **System personalizes** → Based on your context
6. **Input folder cleaned** → Ready for next time

### What Gets Archived:
- ✅ **All your original files** - Exactly as you provided them
- ✅ **Analysis report** - What the system understood
- ✅ **Personalization log** - How it customized itself
- ✅ **Processing manifest** - Summary of the session

## 📊 Archive Contents Explained

### `original_files/`
Your files exactly as you provided them:
- Preserves file names, structure, content
- Nothing modified or altered
- Perfect backup of your input

### `analysis_report.md`
What the AI system extracted:
```markdown
# Analysis Report

## Detected Project Type
Web application with REST API

## Technology Stack
- Frontend: React
- Backend: Node.js + Express  
- Database: PostgreSQL

## Key Features Identified
- User authentication
- Product catalog
- Shopping cart
- Payment processing

## Domain Focus
E-commerce / Online Retail
```

### `personalization_log.md`
How the system customized itself:
```markdown
# Personalization Log

## Agents Configured
- developer: Specialized for React + Node.js
- architect: Focused on e-commerce patterns
- ux-expert: E-commerce UX best practices

## Templates Prioritized
- user-authentication
- product-catalog
- payment-integration

## Workflows Emphasized
- feature-planning (e-commerce focused)
- api-development
- frontend-components
```

### `archive_manifest.md`
Quick summary:
```markdown
# Archive Manifest

**Processing Date**: 2024-01-15 14:30:22
**Files Processed**: 4 files
**Project Type**: E-commerce Web App
**Personalization**: Complete
**System Status**: Ready for development
```

## 🎯 Using Archived Context

### View Your Context
```bash
# See what context was processed
cat processed_context/latest/analysis_report.md

# View personalization details
cat processed_context/latest/personalization_log.md

# Check original files
ls processed_context/latest/original_files/
```

### Update Context
If you want to add more context later:
1. Drop new files in `../context_input/`
2. System processes incrementally
3. Creates new timestamped archive
4. Merges with existing personalization

## 🔍 Archive Benefits

### Perfect Memory
- **Never lose context** - Always available
- **Track evolution** - See how project understanding grew
- **Compare versions** - Multiple processing sessions
- **Audit trail** - Know what influenced personalization

### System Intelligence
- **Learning base** - System learns from your patterns
- **Template improvement** - Better defaults for similar projects
- **Agent training** - Smarter responses based on your domain
- **Workflow optimization** - More relevant suggestions

## 🧹 Archive Maintenance

### Automatic Cleanup
- Archives are kept indefinitely by default
- Each archive is small (typically < 10MB)
- No automatic deletion (your context is valuable)

### Manual Cleanup (If Needed)
```bash
# Remove old archives (careful!)
rm -rf processed_context/context-YYYY-MM-DD-*

# Keep only latest
# (Not recommended - context history is valuable)
```

## 💡 Pro Tips

### Better Context Analysis
- **Be descriptive** - More detailed files = better personalization
- **Include examples** - Show what you want to build
- **Add context files** - Requirements, user stories, technical specs
- **Update regularly** - Add new context as project evolves

### Archive Organization
- **Check analysis reports** - See what system understood
- **Review personalization** - Understand system customizations  
- **Compare sessions** - Track project understanding evolution
- **Use for documentation** - Great project history

---

**Your context is safely archived and your personalized Nexus system is ready to help you build amazing things!** 🚀