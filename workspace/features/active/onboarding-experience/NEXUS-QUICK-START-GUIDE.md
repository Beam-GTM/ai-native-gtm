# 🚀 Nexus Quick Start: From Zero to Working Features in 15 Minutes

## 👤 **Who You Are**
**New to Cursor/Claude Code + AI Development**
- First time using AI-powered development
- Want to build features that actually work
- Need clear, simple guidance
- Want to avoid common mistakes

---

## 🎯 **What Nexus Really Is** (30 seconds)
```
Traditional Development: Write Code → Debug → Deploy
Nexus Development: Describe Intent → AI Plans → AI Builds → You Validate
```

**Think of it as:** Having an AI development team that needs clear instructions and validation

---

## ⚡ **Your First 5 Minutes: Setup**

### For Claude Code Users:
```bash
1. Download Nexus template
2. Open in Claude Code
3. Say: "claude hi"
4. System auto-detects and configures
```

### For Cursor Users:
```bash
1. Download Nexus template
2. Open in Cursor
3. Link: @orchestrator.md
4. Start conversation with AI
```

### Step 2: System Auto-Setup (60 seconds)
```
System: "🎯 FRESH TEMPLATE DETECTED! Choose setup path:"
You: "Go" (or "1" for Quick Setup)
System: Asks 4 simple questions
You: Answer them
Result: ✅ System configured and ready!
```

---

## 🔄 **The 3-Session Success Pattern**

### **Visual Workflow: How Features Actually Get Built**

```mermaid
graph LR
    subgraph "SESSION 1: PLANNING (20 min)"
        A[💭 "I need user login"] --> B[📝 @plan-feature user-login]
        B --> C[🎯 AI asks questions]
        C --> D[📋 5 Planning Files Created]
        D --> E[💾 @close-chat.md to save]
    end
    
    subgraph "SESSION 2: BUILDING (30 min)"
        F[🔄 New chat] --> G[💻 @implement-feature user-login]
        G --> H[🔨 AI creates workspace]
        H --> I[⚡ You guide development]
        I --> J[💾 @close-chat.md to save]
    end
    
    subgraph "SESSION 3: VALIDATION (15 min)"
        K[🔍 New chat] --> L[✅ Test the feature]
        L --> M[🛡️ ULTRATHINK validation]
        M --> N[📊 Evidence of success]
        N --> O[💾 @close-chat.md to complete]
    end
    
    E --> F
    J --> K
    
    style A fill:#e3f2fd
    style E fill:#c8e6c9
    style J fill:#c8e6c9
    style O fill:#c8e6c9
```

---

## 🎬 **Live Example: Building Email Automation**

### **Session 1: Planning (What to Build)**

#### Claude Code:
```yaml
You: "claude hi"
System: [Shows menu]
You: "@plan-feature email-automation"
```

#### Cursor:
```yaml
You: "@orchestrator.md"
You: [Start conversation]
System: [Shows menu]
You: "@plan-feature email-automation"
```

**Both platforms then:**
```yaml
System asks:
- "What triggers the emails?"
- "Who receives them?"  
- "What content should they have?"
- "Any integrations needed?"

You answer each question.

System creates:
✅ feature-definition.yaml
✅ technical-design.yaml
✅ resource-plan.yaml
✅ PRD.md
✅ progress.md

You: "@close-chat.md"  # CRITICAL - Saves everything!
```

### **Session 2: Implementation (How to Build)**
```yaml
[New session]
Claude Code: "claude hi"
Cursor: "@orchestrator.md"

System: [Remembers your feature]
You: "@implement-feature email-automation"

System creates workspace:
📁 email-automation/
  ├── prd.md (requirements)
  ├── progress.md (tracking)
  ├── quality-gates.md (validation)
  └── active-context.md (current state)

You: "Now build the email sender function"
System: [Creates actual code]
You: "Test it"
System: [Runs tests]

You: "@close-chat.md"  # Saves progress
```

### **Session 3: Validation (Does it Work?)**
```yaml
[New session]
Claude Code: "claude hi"
Cursor: "@orchestrator.md"

You: "Let's validate email-automation"

ULTRATHINK Questions:
❓ "Show me it actually sending an email"
❓ "What happens if email fails?"
❓ "Where's the proof it works?"

You provide evidence:
✅ Test email sent successfully
✅ Error handling demonstrated
✅ Configuration verified

You: "@close-chat.md"  # Marks feature complete
```

---

## 🚨 **TOP 5 BEGINNER MISTAKES** (Avoid These!)

### ❌ **Mistake #1: Forgetting to close chat properly**
```
Impact: Lose all your work and context
Fix: ALWAYS end with "@close-chat.md" - it triggers 5 automatic save systems
Remember: @close-chat.md = Save button
Safe alternatives: "close-chat" or "close" or "@close-chat.md"
```

### ❌ **Mistake #2: Trying to build without planning**
```
Impact: AI doesn't know what you want, builds wrong thing
Fix: Always start with "@plan-feature [name]"
Remember: 20 minutes planning saves 2 hours fixing
```

### ❌ **Mistake #3: Not testing (Success Theater)**
```
AI says: "Feature complete!"
Reality: You never tested it
Fix: ALWAYS demand proof - "Show me it working"
Remember: No proof = Not done
Use ULTRATHINK validation!
```

### ❌ **Mistake #4: Not using @ for files**
```
Bad: "run close-chat"
Good: "@close-chat.md"
Remember: Always use @filename to be safe
```

### ❌ **Mistake #5: Multiple interfering features**
```
OK: Multiple features if they're independent
Bad: Features that conflict or share code
Fix: Complete one before starting another if they interfere
Remember: Parallel is fine if features don't overlap
```

---

## 🛡️ **The ULTRATHINK Safety Net**

### What It Is
A **CRITICAL validation system** that forces you to prove things actually work

### The 5 Questions That Save You (MUST USE!)
1. **"What did we ACTUALLY test?"** (Not what we configured)
2. **"Can we PROVE it works?"** (Show me the output)
3. **"What BROKE that we're ignoring?"** (Be honest)
4. **"What files appeared that we don't understand?"** (Mystery = danger)
5. **"Are we pretending or achieving?"** (Documentation ≠ Implementation)

### When to Use ULTRATHINK
- **MANDATORY**: End of EVERY session
- **MANDATORY**: Before marking ANYTHING complete
- **CRITICAL**: When something seems "too easy"
- **ESSENTIAL**: During @close-chat.md workflow

---

## 📊 **Success Metrics: How You Know It's Working**

### ✅ **Good Signs**
- Your features have 5 planning files before building starts
- You can show actual output/results (not just code)
- Each session ends with "@close-chat.md"
- ULTRATHINK validation passes with evidence
- System remembers your work between sessions

### ⚠️ **Warning Signs**
- Lots of documentation but nothing runs
- Can't show proof of functionality
- Lost context between sessions (forgot @close-chat.md)
- Skipping ULTRATHINK validation
- Interfering features running in parallel

---

## 🎯 **Your Action Plan**

### **Today (15 minutes)**

#### Claude Code:
1. Setup Nexus in Claude Code
2. Say "claude hi"
3. Run quick setup ("Go")
4. Try: `@plan-feature hello-world`
5. Say "@close-chat.md" to save

#### Cursor:
1. Setup Nexus in Cursor
2. Link @orchestrator.md
3. Start conversation
4. Run quick setup ("Go")
5. Try: `@plan-feature hello-world`
6. Say "@close-chat.md" to save

### **Tomorrow (45 minutes)**
1. New session (claude hi OR @orchestrator.md)
2. `@implement-feature hello-world`
3. Build something simple
4. Test it with ULTRATHINK
5. Say "@close-chat.md"

### **Day 3 (30 minutes)**
1. New session (claude hi OR @orchestrator.md)
2. Validate with ULTRATHINK (5 questions)
3. Get proof it works
4. Mark complete
5. "@close-chat.md"
6. Celebrate! 🎉

---

## 💡 **Remember These 5 Things**

1. **Always use @close-chat.md** - It's your save button
2. **Start correctly** - Claude Code: "claude hi" | Cursor: "@orchestrator.md"
3. **ULTRATHINK validation** - Use it EVERY session
4. **Plan before building** - Use @plan-feature first
5. **Parallel OK if independent** - Multiple features fine if not interfering

---

## 🚀 **Quick Command Reference**

### Starting a Session:
```bash
# Claude Code
claude hi                   # Start system in Claude Code

# Cursor
@orchestrator.md           # Start system in Cursor
```

### Essential Commands (Both Platforms):
```bash
@plan-feature [name]        # Plan what to build
@implement-feature [name]   # Build from plan
@close-chat.md             # SAVE EVERYTHING (Critical!)
close-chat / close         # Alternative save commands

# When stuck
explain [what confused you] # Get help
@agent developer.md        # Talk to coding specialist
@agent architect.md        # Talk to design specialist
```

---

## 📈 **Your Success Path**

### Week 1: Learn the Basics
- Master the 3-session pattern
- Build 3 simple features
- Practice ULTRATHINK validation
- Get comfortable with @close-chat.md

### Week 2: Build Confidence  
- Try slightly complex features
- Run ULTRATHINK on everything
- Use @ prefix consistently
- Start recognizing patterns

### Week 3: Become Productive
- Build real features for your project
- Work with different agents (@agent files)
- Run parallel non-interfering features
- Contribute your learnings

---

## 🎬 **Start Now!**

### Claude Code Users:
```bash
1. Open Claude Code
2. Say: claude hi
3. Choose: Go (Quick Setup)
4. Begin your first feature with @plan-feature!
```

### Cursor Users:
```bash
1. Open Cursor
2. Link: @orchestrator.md
3. Start conversation
4. Choose: Go (Quick Setup)
5. Begin your first feature with @plan-feature!
```

**Critical Reminders:**
- ✅ ULTRATHINK validation is MANDATORY
- ✅ Always use @filename format for commands
- ✅ @close-chat.md saves your work
- ✅ Claude Code: "claude hi" | Cursor: "@orchestrator.md"
- ✅ Multiple features OK if not interfering

**Remember:** Nexus makes development systematic. Follow the patterns, use ULTRATHINK validation, and always @close-chat.md!

---

*🎯 This guide gets you from zero to productive in 15 minutes. Focus on the 3-session pattern, ULTRATHINK validation, and always @close-chat.md!*