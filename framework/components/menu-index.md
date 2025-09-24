# Menu System Index

## 🎯 Simple Menu System for Templates

This system provides a clean, welcoming interface for new Nexus users.

```yaml
menu_configuration:
  default_menu: "template-menu"
  location: "framework/components/menus/template-menu.md"
  
  available_menus:
    template:
      file: "menus/template-menu.md"
      purpose: "Welcome and onboarding for new users"
      when: "Fresh template or first run"
      
    standard:
      file: "menus/standard-menu.md"  
      purpose: "Regular operations menu"
      when: "After onboarding complete"
      
    high_activity:
      file: "menus/high-activity-menu.md"
      purpose: "Multiple features in progress"
      when: "3+ active features"

menu_selection:
  priority: "Always show template menu for fresh systems"
  detection: "Check TEMPLATE-INDICATORS.md existence"
  fallback: "standard-menu.md"
```

## How It Works

1. **System Detection**: Checks for `TEMPLATE-INDICATORS.md`
2. **Menu Selection**: Shows appropriate menu
3. **User Guidance**: Provides contextual help

## Available Menus

- **template-menu.md** - First-time user experience
- **standard-menu.md** - Daily operations
- **high-activity-menu.md** - Power user interface
- **critical-menu.md** - System issues
- **clean-menu.md** - Fresh workspace

## Integration

The orchestrator automatically loads the right menu based on system state.

For new users, the template menu provides:
- Welcome message
- Quick setup (60 seconds)
- Interactive tutorial option
- Clear next steps

Ready to customize? Edit menus in `framework/components/menus/`