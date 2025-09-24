<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.007260Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.281756Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Personalize Template

**Purpose**: Guide user through template personalization to set up their project

## Execution Steps

### Step 1: Gather Project Information
Ask the user:

```
🎯 Let's personalize your Nexus template! (2 minutes)

Please provide:
1. **Project Name**: What are you building?
2. **Primary Goal**: What do you want to automate?
3. **Tech Stack** (optional): What technologies will you use?
4. **Team Size** (optional): Solo or team project?
```

### Step 2: Update Project Brief
Update briefing/project-brief.md with:
- Project name and description
- Primary goals and objectives
- Technical context
- Success metrics

### Step 3: Update CLAUDE.md
Add project-specific instructions to CLAUDE.md:
- Key project conventions
- Important context
- Special requirements

### Step 4: Remove Template Markers
1. Remove TEMPLATE-STATE-ACTIVE from CRITICAL-DIRECTIVES.md
2. Update project-memory.md with first entry about personalization
3. Update workspace/features/INDEX.md to reflect project name

### Step 5: Confirm Completion
Display:
```
✅ Template personalized successfully!

Your Nexus system is now configured for: [PROJECT_NAME]

Next steps:
• Type "2" to learn the platform
• Type "3" to add your existing documentation
• Type "4" to build your first feature
```

## Success Criteria
- [ ] Project brief updated with real project info
- [ ] Template markers removed
- [ ] Project memory initialized
- [ ] User sees confirmation message

## Error Handling
- If user skips fields, use sensible defaults
- Preserve any existing customizations
- Always remove template markers even if partial info provided