#!/usr/bin/env python3
"""
Create robust PDFs that work with Beam platform
"""

import base64
import json
from io import BytesIO

def create_robust_pdf(title, content_lines):
    """Create a more robust PDF that should work with Beam platform"""
    
    # More complete PDF with proper structure
    pdf_content = f"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
/OpenAction [3 0 R /FitH null]
>>
endobj

2 0 obj
<<
/Type /Pages
/Kids [3 0 R]
/Count 1
/MediaBox [0 0 612 792]
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/Resources <<
/Font <<
/F1 4 0 R
/F2 5 0 R
>>
/ProcSet [/PDF /Text]
>>
/Contents 6 0 R
>>
endobj

4 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica-Bold
>>
endobj

5 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
endobj

6 0 obj
<<
/Length {len(content_lines) * 50 + 200}
>>
stream
BT
/F1 16 Tf
50 750 Td
({title}) Tj
0 -30 Td
/F2 12 Tf
{chr(10).join([f'({line}) Tj 0 -20 Td' for line in content_lines])}
ET
endstream
endobj

xref
0 7
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000168 00000 n 
0000000273 00000 n 
0000000400 00000 n 
trailer
<<
/Size 7
/Root 1 0 R
/Info <<
/Title ({title})
/Creator (Beam KYC Agent)
>>
>>
startxref
{600 + len(content_lines) * 50}
%%EOF"""
    
    return pdf_content.encode('utf-8')

def create_robust_jpeg():
    """Create a more robust JPEG that should work with Beam platform"""
    
    # Create a larger, more realistic JPEG
    jpeg_data = bytes([
        # JPEG Header
        0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01, 0x01, 0x01, 0x00, 0x48, 0x00, 0x48, 0x00, 0x00,
        # Quantization Table
        0xFF, 0xDB, 0x00, 0x43, 0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 0x07, 0x07, 0x09, 0x09, 0x08, 0x0A, 0x0C,
        0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12, 0x13, 0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A, 0x1C, 0x1C, 0x20,
        0x24, 0x2E, 0x27, 0x20, 0x22, 0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29, 0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27,
        0x39, 0x3D, 0x38, 0x32, 0x3C, 0x2E, 0x33, 0x34, 0x32, 0xFF, 0xDB, 0x00, 0x43, 0x01, 0x09, 0x09, 0x09, 0x0C, 0x0B, 0x0C,
        0x18, 0x0D, 0x0D, 0x18, 0x32, 0x21, 0x1C, 0x21, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32, 0x32,
        # Start of Frame
        0xFF, 0xC0, 0x00, 0x11, 0x08, 0x01, 0x00, 0x01, 0x00, 0x01, 0x01, 0x11, 0x00, 0x02, 0x11, 0x01, 0x03, 0x11, 0x01,
        # Huffman Tables
        0xFF, 0xC4, 0x00, 0x14, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08,
        0xFF, 0xC4, 0x00, 0x14, 0x10, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        # Start of Scan
        0xFF, 0xDA, 0x00, 0x0C, 0x03, 0x01, 0x00, 0x02, 0x11, 0x03, 0x11, 0x00, 0x3F, 0x00, 0x8A, 0x00, 0x05,
        # End of Image
        0xFF, 0xD9
    ])
    
    return jpeg_data

def create_robust_payload():
    """Create a robust payload with larger, more complete documents"""
    
    print("Creating robust JPEG...")
    jpeg_data = create_robust_jpeg()
    jpeg_base64 = base64.b64encode(jpeg_data).decode()
    jpeg_size = len(jpeg_data)
    print(f"JPEG size: {jpeg_size} bytes")
    
    print("Creating robust utility bill PDF...")
    utility_pdf = create_robust_pdf("AUSTIN ENERGY UTILITY BILL", [
        "Account Number: 1234567890",
        "Service Address: 123 MAIN ST, AUSTIN, TX 78701",
        "Billing Date: September 1, 2024",
        "Amount Due: $125.50",
        "Due Date: September 30, 2024",
        "Customer: John Smith"
    ])
    utility_base64 = base64.b64encode(utility_pdf).decode()
    utility_size = len(utility_pdf)
    print(f"Utility PDF size: {utility_size} bytes")
    
    print("Creating robust bank statement PDF...")
    bank_pdf = create_robust_pdf("CHASE BANK STATEMENT", [
        "Account Holder: John Smith",
        "Account Number: ****1234",
        "Statement Date: August 31, 2024",
        "Current Balance: $5,250.00",
        "Available Balance: $5,250.00",
        "Account Type: Checking"
    ])
    bank_base64 = base64.b64encode(bank_pdf).decode()
    bank_size = len(bank_pdf)
    print(f"Bank PDF size: {bank_size} bytes")
    
    # Create the payload
    payload = {
        "taskQuery": {
            "query": "Process KYC documents for customer John Smith with driver's license, utility bill, and bank statement. Validate documents, verify identity, assess risk, and make compliance decision.",
            "additionalInfo": "Customer: John Smith, DOB: 1985-03-15, Address: 123 Main Street, Austin, TX 78701, Occupation: Software Engineer, Income: $75,000-$100,000"
        },
        "parsingUrls": [],
        "encodedContextFiles": [
            {
                "data": f"data:image/jpeg;base64,{jpeg_base64}",
                "mimeType": "image/jpeg",
                "fileName": "drivers_license.jpg",
                "fileSize": str(jpeg_size)
            },
            {
                "data": f"data:application/pdf;base64,{utility_base64}",
                "mimeType": "application/pdf",
                "fileName": "utility_bill.pdf",
                "fileSize": str(utility_size)
            },
            {
                "data": f"data:application/pdf;base64,{bank_base64}",
                "mimeType": "application/pdf",
                "fileName": "bank_statement.pdf",
                "fileSize": str(bank_size)
            }
        ],
        "agentId": "d8b2e9b5-20da-4e69-81cf-5af2933124c9"
    }
    
    return payload

if __name__ == "__main__":
    print("🔧 Creating robust documents for Beam platform...")
    print("=" * 60)
    
    payload = create_robust_payload()
    
    # Save robust payload
    with open('robust_kyc_payload.json', 'w') as f:
        json.dump(payload, f, indent=2)
    
    print("\n" + "=" * 60)
    print("✅ Robust payload created: robust_kyc_payload.json")
    print(f"📄 Driver's License: {payload['encodedContextFiles'][0]['fileSize']} bytes")
    print(f"📄 Utility Bill: {payload['encodedContextFiles'][1]['fileSize']} bytes")
    print(f"📄 Bank Statement: {payload['encodedContextFiles'][2]['fileSize']} bytes")
    
    # Test file creation
    print("\n🔍 Testing file creation...")
    try:
        with open('test_robust_utility.pdf', 'wb') as f:
            f.write(base64.b64decode(payload['encodedContextFiles'][1]['data'].split(',')[1]))
        print("✅ Robust utility PDF created successfully")
        os.remove('test_robust_utility.pdf')
    except Exception as e:
        print(f"❌ File creation failed: {e}")
