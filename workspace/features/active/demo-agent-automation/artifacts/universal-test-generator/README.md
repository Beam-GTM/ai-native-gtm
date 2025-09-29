# Universal Test Case Generator

A completely generic framework for generating test cases with PDF documents and agent payloads for any business context.

## Location
This tool is part of the demo agent automation artifacts and provides a universal solution for test case generation across any business context.

## Quick Start

```bash
# Navigate to the universal test generator
cd workspace/features/active/demo-agent-automation/artifacts/universal-test-generator/

# Generate test cases for any context
python3 universal_test_generator.py --context invoices --scenarios 3 --agent-id YOUR_AGENT_ID
python3 universal_test_generator.py --context orders --scenarios 5 --agent-id YOUR_AGENT_ID
python3 universal_test_generator.py --context pos --scenarios 2 --agent-id YOUR_AGENT_ID
```

## Files

- **`universal_test_generator.py`** - Main framework (use this one)
- **`test_case_generation_workflow.py`** - Original complex version
- **`README_Universal_Test_Generator.md`** - Complete documentation
- **`example_usage.py`** - Usage examples
- **`contexts/`** - Context-specific configurations
- **`templates/`** - PDF templates for different contexts

## Core Methodology

This framework abstracts the learnings from PDF generation and encoding:

1. **PDF Generation**: Creates valid PDF documents using a template system
2. **Base64 Encoding**: Encodes PDFs for agent consumption  
3. **Payload Creation**: Generates agent-ready JSON payloads
4. **Validation**: Ensures PDFs are valid and payloads are correct

## Key Features

- **Context Agnostic**: Works with any business context
- **Generic PDF Generation**: Creates valid PDFs without external dependencies
- **Universal Encoding**: Handles base64 encoding for any PDF files
- **STP Optimization**: Includes Straight-Through Processing indicators
- **Flexible Data Generation**: Generates realistic test data for any context

## Supported Contexts

- **invoices**: invoice, receipt, purchase_order
- **orders**: order_form, shipping_label, delivery_confirmation
- **pos**: transaction_receipt, payment_confirmation, refund_document
- **kyc**: identity_document, address_proof, financial_statement
- **custom**: Any context automatically handled

## Output Structure

```
test_cases_{context}_{timestamp}/
├── pdfs/                    # Generated PDF files
├── payloads/                # Agent-ready JSON payloads
└── generation_summary.json  # Summary report
```

## Integration

Generated payloads can be directly sent to any agent webhook:

```bash
curl -X POST "YOUR_AGENT_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d @test_cases_invoices_20240926_123456/payloads/invoices_scenario_1_payload.json
```

## Dependencies

- Python 3.6+
- Standard library only (no external dependencies)

## Related Artifacts

This universal test generator complements other demo automation artifacts:
- **kyc-agent-session/**: KYC-specific implementation examples
- **kyc-agent-workflow.yaml**: KYC agent workflow definition

The universal generator can be used to create test cases for any agent workflow, not just KYC.
