# Claude Code Configuration for Nexus

This directory contains Claude Code configurations including subagents, hooks, and custom commands for the Nexus system.

## Directory Structure

```
.claude/
├── agents/           # Subagent definitions
├── commands/         # Custom slash commands
├── hooks/           # Hook scripts
├── settings.json    # Main configuration
└── tool-history.md  # Tool usage log (generated)
```

## Subagents

10 specialized Nexus agents converted to Claude Code subagents:

- **architect** - System architecture and design
- **developer** - Feature implementation
- **product-manager** - Product strategy and PRDs
- **quality-assurance** - Testing and validation
- **ux-expert** - UI/UX design
- **analyst** - Business analysis
- **product-owner** - Product ownership
- **scrum-master** - Agile coordination
- **explainer** - Documentation and explanation
- **llm-whisperer** - AI optimization

### Using Subagents

Invoke subagents using natural language:
- "Use the architect subagent to design the system"
- "Have the developer implement this feature"
- "Get the quality-assurance agent to review this"

Or use the Task tool programmatically.

## Custom Commands

Available slash commands in `.claude/commands/`:

### System Status
- `/nexus-status` - Show complete system status
- `/view-tool-history` - View tool usage history

### Development
- `/feature-start <name>` - Initialize new feature structure
- `/invoke-agent <name> [task]` - Invoke specific agent
- `/quality-check` - Run quality validation

### Usage Examples

```bash
# Check system status
/nexus-status

# Start a new feature
/feature-start user-authentication

# Run quality checks
/quality-check

# View tool usage
/view-tool-history
```

## Hooks

Configured in `settings.json` to track and log tool usage:

### Active Hooks

1. **PreToolUse** - Logs all tool invocations with parameters
2. **PostToolUse** - Adds completion status for each tool type
3. **UserPromptSubmit** - Marks user prompts in history
4. **SessionStart** - Logs session initialization
5. **SubagentStop** - Tracks subagent completions

### Tool History

All tool usage is logged to `.claude/tool-history.md` with:
- Timestamps for each operation
- Tool names and parameters
- File paths for file operations
- Commands executed
- Search patterns
- Completion status

View history with: `/view-tool-history`

## Configuration

### settings.json

Main configuration file containing:
- Agent settings
- Hook definitions
- Tool matchers
- Command mappings

### Customization

To add new hooks, edit `settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "ToolName",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here"
          }
        ]
      }
    ]
  }
}
```

## Integration with Nexus

### Memory System
Hooks and commands integrate with Nexus's memory system:
- Features tracked in `Nexus/workspace/features/active/`
- Memory stored in `Nexus/workspace/memory/`
- Quality gates in feature directories

### Engineering Rules
Commands validate against Nexus engineering rules:
- Located in `Nexus/operations/engineeringrules/`
- Automatically checked by quality commands

### Workflow Coordination
Subagents coordinate through:
- Context handoffs in memory system
- Quality gate validations
- Progress tracking in feature directories

## Troubleshooting

### Hooks Not Firing
1. Check `settings.json` syntax
2. Verify Claude Code is using project settings
3. Check hook command syntax for your OS

### Commands Not Found
1. Ensure `.md` extension on command files
2. Check frontmatter syntax
3. Verify command name matches filename

### Tool History Issues
1. Check write permissions for `.claude/`
2. Verify PowerShell available (Windows)
3. Check bash available (Unix/Linux/Mac)

## Maintenance

### Regular Tasks
- Review tool history: `/view-tool-history`
- Clean old history: Backup and clear as needed
- Update hooks: Edit `settings.json`
- Add commands: Create new `.md` files in `commands/`

### Backup
Important files to backup:
- `settings.json` - Main configuration
- `commands/` - Custom commands
- `agents/` - Subagent definitions
- `tool-history.md` - Usage history

## Support

For issues or questions:
1. Check Nexus documentation
2. Review Context7 Claude Code docs
3. Check hook/command logs in `tool-history.md`