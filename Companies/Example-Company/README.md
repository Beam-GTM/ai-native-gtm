# Example Company - Template Structure

This is an example company structure showing how to organize client work in the Nexus GTM system.

## Directory Structure
```
Companies/Example-Company/
├── README.md                    # This file - company overview
├── documents/                   # Company documents and analysis
│   ├── company-overview.md      # Basic company information
│   ├── demo-agent-package.yaml  # Demo agent configuration
│   ├── intelligence-summary.md  # Business intelligence report
│   └── partnership-analysis.md  # Partnership opportunity analysis
├── emails/                      # Email communications
│   └── outbound/               # Outbound email templates
│       ├── initial-outreach.md  # First contact email
│       └── follow-up.md         # Follow-up email templates
├── transcripts/                 # Meeting transcripts and analysis
│   ├── intro-call.md           # Initial discovery call
│   ├── demo-call.md            # Demo presentation call
│   └── processed/              # Processed transcript analysis
│       └── transcript-analysis.yaml
└── test-cases/                 # Test cases and validation
    ├── demo-test-cases.yaml    # Demo validation tests
    └── automation-tests.json   # Automation test scenarios
```

## Usage
1. **Copy this structure** for new companies
2. **Rename directories** to match company name
3. **Update content** with actual company data
4. **Use workflows** to populate content automatically

## Workflow Commands
- `@create-company` - Create new company structure
- `@demo-automation-workflow` - Set up demo automation
- `@transcript-processing-workflow` - Process meeting transcripts
- `@follow-up-automation` - Create follow-up sequences

---
*This is a template structure for demonstration purposes.*