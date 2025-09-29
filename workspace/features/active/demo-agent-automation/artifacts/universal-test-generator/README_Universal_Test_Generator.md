# Universal Test Case Generator

A completely generic framework for generating test cases with PDF documents and agent payloads for any business context.

## Core Methodology

This framework abstracts the learnings from PDF generation and encoding into a universal system:

1. **PDF Generation**: Creates valid PDF documents using a template system
2. **Base64 Encoding**: Encodes PDFs for agent consumption
3. **Payload Creation**: Generates agent-ready JSON payloads
4. **Validation**: Ensures PDFs are valid and payloads are correct

## Key Features

- **Context Agnostic**: Works with any business context (invoices, orders, POS, KYC, etc.)
- **Generic PDF Generation**: Creates valid PDFs without external dependencies
- **Universal Encoding**: Handles base64 encoding for any PDF files
- **STP Optimization**: Includes Straight-Through Processing indicators
- **Flexible Data Generation**: Generates realistic test data for any context

## Usage

### Basic Usage
```bash
python3 universal_test_generator.py --context invoices --scenarios 3 --agent-id YOUR_AGENT_ID
python3 universal_test_generator.py --context orders --scenarios 5 --agent-id YOUR_AGENT_ID
python3 universal_test_generator.py --context pos --scenarios 2 --agent-id YOUR_AGENT_ID
```

### Parameters
- `--context`: Business context (invoices, orders, pos, kyc, etc.)
- `--scenarios`: Number of test scenarios to generate
- `--agent-id`: Agent ID for payload generation

## Output Structure

```
test_cases_{context}_{timestamp}/
├── pdfs/
│   ├── {context}_scenario_1_{doc_type}.pdf
│   ├── {context}_scenario_2_{doc_type}.pdf
│   └── ...
├── payloads/
│   ├── {context}_scenario_1_payload.json
│   ├── {context}_scenario_2_payload.json
│   └── ...
└── generation_summary.json
```

## Supported Contexts

### Invoices
- Document types: invoice, receipt, purchase_order
- Fields: vendor, tax_id, amount, due_date, etc.

### Orders
- Document types: order_form, shipping_label, delivery_confirmation
- Fields: order_number, shipping_address, tracking_number, etc.

### POS (Point of Sale)
- Document types: transaction_receipt, payment_confirmation, refund_document
- Fields: transaction_id, payment_method, terminal_id, etc.

### KYC (Know Your Customer)
- Document types: identity_document, address_proof, financial_statement
- Fields: customer_name, document_number, verification_status, etc.

### Custom Contexts
The framework automatically handles any context by generating generic document types and fields.

## PDF Generation

The framework creates valid PDF documents with:
- Proper PDF structure (header, objects, xref table, trailer)
- UTF-8 encoding for international characters
- Binary mode file writing
- Consistent formatting and layout

## Base64 Encoding

All PDFs are properly encoded using:
- Binary file reading
- Base64 encoding
- UTF-8 string conversion
- Correct MIME types and file sizes

## STP Optimization

Each payload includes Straight-Through Processing indicators:
- **Low Risk**: Automatic approval with immediate processing
- **Medium Risk**: Approval with monitoring
- **High Risk**: Manual review required

## Example Output

### Generated PDF
A valid PDF document with proper structure containing the test data.

### Generated Payload
```json
{
  "taskQuery": {
    "query": "Process invoices documents for Customer 1. Validate invoices, verify amounts, check vendor information, and approve payments.",
    "additionalInfo": "Customer: Customer 1. Customer ID: CUST0001. Email: customer1@example.com. Phone: +1-555-123-4567. Amount: $1,234. Date: 2024-09-15. Status: pending. DOCUMENT VALIDATION: All documents are legitimate, clear, and current. VERIFICATION: Information is consistent across all documents. RISK ASSESSMENT: Low risk profile - established customer, stable history. DECISION: AUTOMATIC APPROVAL - Process immediately without manual review."
  },
  "parsingUrls": [],
  "encodedContextFiles": [
    {
      "data": "JVBERi0xLjQK...",
      "mimeType": "application/pdf",
      "fileName": "invoices_scenario_1_invoice.pdf",
      "fileSize": "1234"
    }
  ],
  "agentId": "YOUR_AGENT_ID"
}
```

## Integration

The generated payloads can be directly sent to any agent webhook:

```bash
curl -X POST "YOUR_AGENT_WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -d @test_cases_invoices_20240926_123456/payloads/invoices_scenario_1_payload.json
```

## Extensibility

The framework is designed to be easily extensible:

1. **New Contexts**: Add new context types by extending the document type mappings
2. **Custom Fields**: Modify the data generation methods for context-specific fields
3. **PDF Templates**: Create custom PDF templates for specific document types
4. **STP Rules**: Customize STP indicators for different business rules

## Dependencies

- Python 3.6+
- Standard library only (no external dependencies)

## Core Learnings Applied

1. **Two-Script Approach**: Separate PDF generation from encoding
2. **Binary File Handling**: Proper binary mode for PDF creation and reading
3. **UTF-8 Encoding**: Consistent character encoding throughout
4. **PDF Structure**: Valid PDF format with proper headers and objects
5. **Base64 Encoding**: Correct encoding for agent consumption
6. **STP Optimization**: Clear indicators for automated processing
