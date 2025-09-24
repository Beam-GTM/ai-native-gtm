# Interactive System Setup - Baseline Template Welcome

## Task Definition
TASK NAME: system-setup  
PURPOSE: Interactive onboarding for fresh Nexus baseline template  
SCOPE: Introduce core workflows, folder structure, and next steps

## Execution Context
CRITICAL: THIS TASK OVERRIDES NORMAL MENU BEHAVIOR
Automatically triggered when TEMPLATE-STATE-ACTIVE marker detected

## Initial Welcome

```
🎉 WELCOME TO YOUR NEXUS SYSTEM!

🎯 BASELINE TEMPLATE READY!
Your Language-Based Operating System is ready to use.

📊 What You Have:
• 🤖 12 specialized AI agents 
• 🗺️ Structure Maps for navigation
• 🔄 Ready-to-use workflows and tasks
• 📚 Self-learning memory system

⚡ Quick Start:
1. 🚀 Go - Start using your system now (RECOMMENDED)
2. 🎓 Learn - Take the 15-minute tutorial
3. 🗺️ Explore - See system structure with maps
4. 📖 Docs - Read documentation

💡 Tips:
• Just describe what you want to build in plain English
• Try: "help me create a new feature" or "show me around"
• Use Structure Maps: "*task generate-structure-maps"

Ready to get started?

> [Wait for user choice: 1, 2, 3, 4, or just describe your needs]
```

## Interactive System Introduction

### Path 1: Quick Go (Main Path)
TRIGGER: User selects 1, types "go", or presses Enter

```
🚀 PERFECT! Let's get your Nexus system personalized for you.

I'll ask you a few quick questions to create your project brief, then show you how everything works.

STEP 1: TELL ME ABOUT YOUR PROJECT

🎯 What are you building or working on?
Examples: 
• "Task management system"
• "E-commerce website"  
• "Data analysis pipeline"
• "Personal productivity tools"
• "Just exploring what's possible"

> [WAIT FOR PROJECT DESCRIPTION]

📊 What's your main goal with this project?
A) Automate repetitive tasks
B) Build software faster  
C) Manage complex workflows
D) Create AI-powered tools
E) Learn and experiment
F) Something else (describe)

> [WAIT FOR GOAL SELECTION]

🎓 How would you describe your experience level?
1) 🌱 New to development/automation
2) 🌿 Some experience with tools and systems
3) 🌳 Experienced developer/technical person

> [WAIT FOR EXPERIENCE LEVEL]

🚀 What would you like to do first?
1) Start planning a specific feature
2) Take a quick tour of the system
3) Learn the core workflows step-by-step
4) Generate structure maps to see the big picture

> [WAIT FOR FIRST ACTION CHOICE]

Based on your answers, I'll create a personalized project brief and show you exactly how to succeed with Nexus!
```

### Step 2: Project Brief Creation & System Introduction

After gathering user information, respond with:

```
✨ EXCELLENT! Creating your personalized project brief now...

📋 YOUR PROJECT BRIEF:
```
Project: [USER'S PROJECT DESCRIPTION]
Goal: [USER'S SELECTED GOAL] 
Experience: [USER'S LEVEL]
Next Action: [USER'S CHOICE]
Setup Date: [CURRENT DATE]
```

This brief is now saved to briefing/project-brief.md and will guide all our work together.

STEP 2: YOUR NEXUS SYSTEM STRUCTURE

Now let me show you how your system is organized:

📁 YOUR NEXUS SYSTEM LAYOUT:
├── 🏗️ structure/      → System blueprints & navigation maps
├── 🤖 operations/     → Your 12 AI agents & their workflows  
├── ⚙️ framework/      → Ready-to-use tasks & workflows
├── 💼 workspace/      → YOUR active work area (features, memory)
├── 📋 briefing/       → Project setup & configuration (your brief is here!)
└── 📚 templates/      → Reusable components & patterns

🎯 KEY UNDERSTANDING:
• workspace/ = Where YOU work on features
• operations/ = AI agents that help you
• framework/ = Tools and workflows ready to use
• briefing/ = Your project information and setup

STEP 3: THE 3 CORE WORKFLOWS YOU NEED TO KNOW

Your Nexus system runs on 3 essential workflows:

🔄 THE NEXUS WORKFLOW CYCLE:

1️⃣ PLAN-FEATURE WORKFLOW 📋
```
Purpose: Plan what you want to build with structured elicitation
Command: plan-feature [feature-name]
Output: 5 planning artifacts that define exactly what to build
Duration: 30-45 minutes of interactive planning
```

2️⃣ IMPLEMENT-FEATURE WORKFLOW 🔨  
```
Purpose: Turn planning artifacts into organized workspace for building
Command: implement-feature [same-feature-name]
Creates: workspace/features/active/[feature-name]/ with all context
Output: PRD, progress tracking, quality gates, checklist
```

3️⃣ CLOSE-CHAT WORKFLOW 💾
```
Purpose: Save progress, capture learnings, preserve memory
Command: bye, exit, quit, close, @close-chat
Critical: NEVER skip this! It's how your system learns and remembers
Runs: 5-engine system (capture, validate, memory, lifecycle, sync)
```

🌟 THE SUCCESS PATTERN:
```
Session 1: plan-feature [name] → bye (saves planning)
Session 2: implement-feature [name] → build → bye (saves progress)  
Session 3: continue work → complete → bye (archives feature)
```

STEP 4: NEXT STEPS FOR YOU

Based on your choice "[USER'S FIRST ACTION]", here's what I recommend:

[If chose "Start planning a feature":]
Perfect! Let's start with planning. The key is to be specific:
• Good: "plan-feature user-login-system" 
• Good: "plan-feature email-automation"
• Bad: "plan-feature make-it-better"

Ready to plan your first feature? Just tell me what you want to build!

[If chose "Take a tour":]
Great! Let me show you around. Try these commands:
• "generate structure maps" (see system visually)
• "show me my workspace folder" 
• "list my agents"

[If chose "Learn workflows":]
Perfect! We just covered the 3 core workflows. Would you like to:
• Try the plan-feature workflow with a simple example
• See how workspace folders are organized
• Understand why closing chat is so important

[If chose "Generate structure maps":]
Excellent! Structure maps show you how everything connects:
Command: *task generate-structure-maps

This will create visual diagrams of your system architecture.

💡 CRITICAL REMINDER:
When you're done with today's session, remember to say "bye" - this triggers the close-chat workflow that saves everything and prepares for your next session.

Ready to start building? What would you like to do first?
```

### Intelligent Follow-Up Responses

#### Response 1: Plan-Feature Workflow Introduction
```
📋 EXCELLENT CHOICE! The plan-feature workflow is where all successful features begin.

Here's what happens in the plan-feature workflow:

🎯 THE PLAN-FEATURE PROCESS:
```
Step 1: Feature Definition → Clear scope and boundaries
Step 2: Elicitation Session → Interactive discovery of requirements  
Step 3: Technical Planning → Architecture and dependencies
Step 4: Resource Planning → What you need to build it
Step 5: Artifact Generation → 5 structured files for implementation
```

💡 WHY PLANNING MATTERS:
• Prevents 90% of common implementation failures
• Uses interactive elicitation to discover hidden requirements
• Creates structured artifacts that feed directly into implementation
• Takes 30-45 minutes but saves hours of rework

🚀 WANT TO TRY IT? 

Here's how to start:
`plan-feature [simple-name]`

Examples:
• `plan-feature email-automation`
• `plan-feature user-dashboard` 
• `plan-feature data-export`

The system will:
1. Ask you detailed questions about what you want
2. Help you discover requirements you hadn't thought of
3. Generate 5 planning files automatically
4. Prepare everything for the next phase (implementation)

Would you like to:
A) Try planning a real feature right now
B) Learn about the implement-feature workflow next  
C) See the complete 3-phase development cycle
D) Ask questions about planning

What interests you? [A/B/C/D or describe]
```

#### Response 2: Implement-Feature Workflow Introduction  
```
🔨 PERFECT! The implement-feature workflow turns planning into working code.

Here's what the implement-feature workflow does:

⚙️ THE IMPLEMENT-FEATURE PROCESS:
```
Step 1: Validate Artifacts → Ensure planning is complete
Step 2: Create Workspace → Organized folder structure in workspace/
Step 3: Generate PRD → Product requirements from planning artifacts
Step 4: Setup Tracking → Progress monitoring and quality gates
Step 5: Initialize Context → Everything ready for development
```

📁 WHERE WORK HAPPENS:
```
workspace/features/active/[your-feature-name]/
├── prd.md           → What you're building (from planning)
├── progress.md      → Track implementation progress
├── active-context.md → Current work context
├── quality-gates.md → Validation checkpoints
└── feature-checklist.md → Step-by-step completion guide
```

🎯 WHY STRUCTURED IMPLEMENTATION WORKS:
• All planning context automatically imported
• Clear progress tracking prevents getting lost
• Quality gates ensure you don't skip important steps  
• Perfect context preservation between sessions

🚀 HOW TO USE IT:

First you need planning artifacts from plan-feature, then:
`implement-feature [same-name-as-planned]`

The system will:
1. Create a complete workspace for your feature
2. Import all planning context automatically
3. Set up progress tracking and quality gates
4. Give you a clear path to completion

Would you like to:
A) Learn about the planning phase first (you need it before implementing)
B) See the complete 3-phase workflow
C) Understand how workspace/ folders are organized  
D) Learn about quality gates and progress tracking

What interests you? [A/B/C/D or describe]
```

#### Response 3: Close-Chat Workflow Introduction
```
💾 BRILLIANT QUESTION! Close-chat is the most critical workflow - it's how your system learns and remembers.

Here's why close-chat matters:

🧠 THE CLOSE-CHAT 5-ENGINE SYSTEM:
```
Engine 1: Session Capture → Learns from what you did this session
Engine 2: System Validation → Checks system health and integrity  
Engine 3: Memory Management → Updates memory, rotates if needed
Engine 4: Feature Lifecycle → Moves completed features to archive
Engine 5: System Sync → Keeps everything aligned and current
```

⚠️ CRITICAL UNDERSTANDING:
Without proper session closure, you lose:
• Context between sessions (no memory of what you did)
• Learning patterns (system can't improve) 
• Progress tracking (features stuck in limbo)
• System integrity (files get out of sync)

🎯 HOW TO CLOSE PROPERLY:
Just say any of these when you're done:
• `bye`
• `exit`  
• `quit`
• `close`
• `@close-chat`

The system automatically:
1. Captures what you learned this session
2. Updates memory with new patterns
3. Archives completed features (if progress = 100%)
4. Syncs all system files
5. Prepares context for your next session

💡 GOLDEN RULE: 
**NEVER end significant work without closing chat properly!**

This is how your system gets smarter over time and remembers context perfectly between sessions.

Would you like to:
A) Learn about the complete development workflow (plan → implement → close)
B) Understand what happens to your memory between sessions
C) See how features move through their lifecycle  
D) Try the other core workflows first

What interests you? [A/B/C/D or describe]
```

#### Response 6: Golden Path - Complete Development Cycle
```
🆘 PERFECT! Let me show you the proven golden path that leads to 90%+ feature success rates.

🌟 THE NEXUS GOLDEN PATH (3-Phase Development):

PHASE 1: PLANNING SESSION 📋
```
1. Start: `plan-feature [simple-name]`
2. Interactive elicitation discovers requirements  
3. System generates 5 planning artifacts
4. Close: `bye` (saves planning to memory)
```

PHASE 2: IMPLEMENTATION SESSION 🔨
```  
1. New session: `hi` 
2. Start: `implement-feature [same-name]`
3. System creates workspace from planning artifacts
4. You build the actual feature with clear guidance
5. Progress tracking keeps you on path
6. Close: `bye` (saves progress to memory)
```

PHASE 3: VALIDATION & COMPLETION ✅
```
1. New session: `hi`
2. Continue implementation work  
3. Quality gates ensure completeness
4. ULTRATHINK validation requires proof of functionality
5. Feature moves to completed/ when done
6. Close: `bye` (archives completed feature)
```

📊 WHY THIS WORKS (Success Patterns):
• Structured planning prevents 90% of implementation failures
• Session-based work maintains focus and quality
• Memory system preserves perfect context between sessions
• Quality gates prevent incomplete or broken solutions
• Evidence-based validation (ULTRATHINK) prevents false success claims

🎯 YOUR FIRST FEATURE SHOULD BE SIMPLE:
Good examples:
• "Add utility function for date formatting"
• "Create contact form component" 
• "Set up email notification system"
• "Build simple data export feature"

Bad examples (too vague):
• "Improve the system"
• "Make it better"
• "Automate everything"

🚀 READY TO START?

I recommend beginning with:
`plan-feature [your-simple-idea]`

The system will guide you through interactive elicitation to discover exactly what you want to build.

Would you like to:
A) Try planning your first feature right now
B) Learn more about what makes features successful
C) Understand the folder structure first
D) See examples of successful features

What sounds good? [A/B/C/D or describe your interest]
```

## System Ready Completion

After any setup path, conclude with:

```
✨ CONGRATULATIONS! Your Nexus system is personalized and ready!

📋 YOUR SETUP IS COMPLETE:
• ✅ Project brief created and saved
• ✅ System structure explained  
• ✅ Core workflows introduced (plan → implement → close)
• ✅ Next steps identified

🎯 TO START BUILDING:

The best first step is always planning. Try:
`plan-feature [your-idea]`

Good first features:
• "plan-feature contact-form"
• "plan-feature data-export" 
• "plan-feature user-profile"
• "plan-feature email-notifications"

The system will guide you through interactive elicitation to discover exactly what you need to build.

💡 CRITICAL REMINDER BEFORE YOU START:
When you finish any work session, always say:
• `bye` or `exit` or `quit` or `close`

This triggers the close-chat workflow that:
• Saves your progress to memory
• Captures what you learned
• Prepares context for next session
• Archives completed features

🌟 YOUR SUCCESS PATTERN:
1. Plan first: `plan-feature [name]` → `bye`
2. Implement: `implement-feature [name]` → work → `bye`  
3. Complete: continue → quality gates → `bye`

Ready to plan your first feature? Just tell me what you want to build!
```

## Advanced Intelligence

### Smart Follow-Up Questions
Based on user responses, ask contextual questions:
- If they mention existing project: "Do you have documentation I should see first?"
- If they seem experienced: "Have you used similar systems before?"
- If they mention specific technology: "Are you building [frontend/backend/automation/etc]?"
- If they seem uncertain: "What's the smallest thing you'd like to improve or automate?"

### Context-Aware Suggestions
- New developers → Suggest plan-feature first
- System architects → Show Structure Maps
- Project managers → Explain workspace organization
- Experienced users → Jump to golden path

### Adaptive Responses
- Beginner language for new users
- Technical depth for experienced users  
- Visual examples for visual learners
- Step-by-step for systematic thinkers

## Quality Gates
- [ ] User understands folder structure
- [ ] Core workflows introduced (plan, implement, close)
- [ ] Golden path explained with rationale
- [ ] Next steps are clear and actionable
- [ ] User can start their first feature confidently

---

TASK STATUS: Production Ready
COMPLEXITY: Adaptive (5 minutes to 30 minutes based on user needs)  
USER EXPERIENCE: Interactive, Educational, Engaging