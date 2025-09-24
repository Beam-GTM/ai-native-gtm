<!-- version: 3.2.0 -->
<!-- system_version: 3.2.0 -->
<!-- last_modified: 2025-08-28T02:17:41.183887Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:17:11.283014Z -->
<!-- migration_path: auto-generated -->

<!-- last_modified: 2025-08-28T02:14:16Z -->
<!-- migration_path: auto-generated -->

# Task: Quick Setup - 60 Second Personalization

**Purpose**: Fast, interactive setup to personalize your Nexus template

## Welcome Sequence

Display:
```
╔══════════════════════════════════════════════════════════════╗
║         🚀 NEXUS QUICK SETUP - Let's Build Together! 🚀      ║
╚══════════════════════════════════════════════════════════════╝

Welcome! I'm excited to help you set up your automation system.
In just 60 seconds, we'll transform this template into YOUR 
personal AI-powered automation platform.

Ready? Let's go! 🎯
```

## Step 1: Project Name (10 seconds)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    STEP 1 OF 4: PROJECT NAME                  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What are you building? (Examples: "Task Manager", "DevOps Pipeline", "AI Assistant")

> [User Input]
```

**Smart Defaults**: If user just presses Enter, suggest based on context

## Step 2: Primary Goal (15 seconds)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                    STEP 2 OF 4: YOUR GOAL                     
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Great! [PROJECT_NAME] sounds awesome! 🎉

What's the main problem you want to solve?

Quick options (or type your own):
  [A] Automate repetitive tasks
  [B] Build software faster
  [C] Manage complex workflows
  [D] Create AI-powered tools
  [E] Something else (describe)

> [User Input]
```

## Step 3: Experience Level (10 seconds)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 STEP 3 OF 4: YOUR EXPERIENCE                  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

How familiar are you with automation systems?

  [1] 🌱 Beginner - Show me everything!
  [2] 🌿 Some experience - I know the basics
  [3] 🌳 Expert - Just the advanced stuff

> [User Input]
```

## Step 4: First Action (15 seconds)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 STEP 4 OF 4: FIRST ACTION                     
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Perfect! Last question - what would you like to do first?

  [1] 🎓 Take the interactive tutorial (recommended for beginners)
  [2] 🚀 Build my first feature right away
  [3] 📚 Import my existing documentation
  [4] 🔍 Explore what Nexus can do
  [5] 💬 Just chat - I'll figure it out

> [User Input]
```

## Configuration Phase (10 seconds)

Behind the scenes, quickly:
1. Update `briefing/project-brief.md` with project details
2. Remove `TEMPLATE-STATE-ACTIVE` from CRITICAL-DIRECTIVES.md
3. Add first entry to project-memory.md
4. Update CLAUDE.md with project context
5. Configure workspace/features/INDEX.md

Show progress:
```
🔧 Configuring your workspace...
  ✅ Project brief created
  ✅ Memory system initialized  
  ✅ AI agents configured
  ✅ Workspace personalized
```

## Success Celebration

```
╔══════════════════════════════════════════════════════════════╗
║           ✨ SETUP COMPLETE - WELCOME TO NEXUS! ✨           ║
╚══════════════════════════════════════════════════════════════╝

🎉 Congratulations! Your [PROJECT_NAME] is ready!

Your personalized Nexus system includes:
  • 11 specialized AI agents ready to help
  • Intelligent workflow automation
  • Natural language understanding
  • Pattern-based learning that improves over time

[DYNAMIC NEXT STEPS based on Step 4 choice]

──────────────────────────────────────────────────────────────

💡 Pro Tip: Just describe what you need in plain English.
I understand natural language and will figure out the best
way to help you!

Type anything to get started, or say "help" for options.
```

## Dynamic Routing

Based on Step 4 choice, automatically:
- Choice 1 → Launch framework learning system
- Choice 2 → Launch plan-feature workflow
- Choice 3 → Guide to briefing/context/ folder
- Choice 4 → Show capability showcase
- Choice 5 → Return to main menu

## Error Handling

- If user skips any field → Use smart defaults
- If setup interrupted → Save progress, allow resume
- Always remove template markers even on partial completion

## Success Metrics

- [ ] Completed in under 60 seconds
- [ ] User understands next steps
- [ ] Template markers removed
- [ ] Project configured correctly
- [ ] User feels welcomed and excited