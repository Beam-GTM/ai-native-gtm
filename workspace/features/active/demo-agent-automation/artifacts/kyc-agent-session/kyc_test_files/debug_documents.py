#!/usr/bin/env python3
"""
Debug script to create and validate KYC documents for Beam platform
"""

import base64
import json
import os
from io import BytesIO

def create_minimal_jpeg():
    """Create a minimal valid JPEG image"""
    # Minimal JPEG header + data + footer
    jpeg_data = bytes([
        0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01, 0x01, 0x01, 0x00, 0x48, 0x00, 0x48, 0x00, 0x00,
        0xFF, 0xDB, 0x00, 0x43, 0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 0x07, 0x07, 0x09, 0x09, 0x08, 0x0A, 0x0C,
        0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12, 0x13, 0x0F, 0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A, 0x1C, 0x1C, 0x20,
        0x24, 0x2E, 0x27, 0x20, 0x22, 0x2C, 0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29, 0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27,
        0x39, 0x3D, 0x38, 0x32, 0x3C, 0x2E, 0x33, 0x34, 0x32, 0xFF, 0xC0, 0x00, 0x11, 0x08, 0x00, 0x10, 0x00, 0x10, 0x01, 0x01,
        0x11, 0x00, 0x02, 0x11, 0x01, 0x03, 0x11, 0x01, 0xFF, 0xC4, 0x00, 0x14, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0xFF, 0xC4, 0x00, 0x14, 0x10, 0x01, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0xDA, 0x00, 0x0C, 0x03, 0x01, 0x00, 0x02,
        0x11, 0x03, 0x11, 0x00, 0x3F, 0x00, 0x8A, 0x00, 0x05, 0xFF, 0xD9
    ])
    
    return jpeg_data

def create_simple_pdf(content="Hello World"):
    """Create a simple valid PDF"""
    pdf_content = f"""%PDF-1.4
1 0 obj
<<
/Type /Catalog
/Pages 2 0 R
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
>>
>>
/Contents 5 0 R
>>
endobj

4 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
endobj

5 0 obj
<<
/Length {len(content) + 20}
>>
stream
BT
/F1 12 Tf
50 700 Td
({content}) Tj
ET
endstream
endobj

xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000168 00000 n 
0000000273 00000 n 
trailer
<<
/Size 6
/Root 1 0 R
>>
startxref
{400 + len(content)}
%%EOF"""
    
    return pdf_content.encode('utf-8')

def validate_base64(data):
    """Validate base64 data"""
    try:
        decoded = base64.b64decode(data)
        return True, len(decoded)
    except Exception as e:
        return False, str(e)

def create_debug_payload():
    """Create a debug payload with validated documents"""
    
    print("Creating minimal JPEG...")
    jpeg_data = create_minimal_jpeg()
    jpeg_base64 = base64.b64encode(jpeg_data).decode()
    jpeg_valid, jpeg_size = validate_base64(jpeg_base64)
    print(f"JPEG valid: {jpeg_valid}, size: {jpeg_size}")
    
    print("Creating utility bill PDF...")
    utility_pdf = create_simple_pdf("AUSTIN ENERGY UTILITY BILL\nAccount: 1234567890\nAddress: 123 MAIN ST, AUSTIN, TX 78701\nAmount: $125.50")
    utility_base64 = base64.b64encode(utility_pdf).decode()
    utility_valid, utility_size = validate_base64(utility_base64)
    print(f"Utility PDF valid: {utility_valid}, size: {utility_size}")
    
    print("Creating bank statement PDF...")
    bank_pdf = create_simple_pdf("CHASE BANK STATEMENT\nAccount Holder: JOHN SMITH\nAccount: ****1234\nBalance: $5,250.00")
    bank_base64 = base64.b64encode(bank_pdf).decode()
    bank_valid, bank_size = validate_base64(bank_base64)
    print(f"Bank PDF valid: {bank_valid}, size: {bank_size}")
    
    # Test if we can save and read the files
    print("\nTesting file creation...")
    try:
        with open('test_drivers_license.jpg', 'wb') as f:
            f.write(jpeg_data)
        print("✅ JPEG file created successfully")
        os.remove('test_drivers_license.jpg')
    except Exception as e:
        print(f"❌ JPEG file creation failed: {e}")
    
    try:
        with open('test_utility.pdf', 'wb') as f:
            f.write(utility_pdf)
        print("✅ Utility PDF created successfully")
        os.remove('test_utility.pdf')
    except Exception as e:
        print(f"❌ Utility PDF creation failed: {e}")
    
    try:
        with open('test_bank.pdf', 'wb') as f:
            f.write(bank_pdf)
        print("✅ Bank PDF created successfully")
        os.remove('test_bank.pdf')
    except Exception as e:
        print(f"❌ Bank PDF creation failed: {e}")
    
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
    print("🔍 Debugging KYC document creation...")
    print("=" * 50)
    
    payload = create_debug_payload()
    
    # Save debug payload
    with open('debug_kyc_payload.json', 'w') as f:
        json.dump(payload, f, indent=2)
    
    print("\n" + "=" * 50)
    print("✅ Debug payload created: debug_kyc_payload.json")
    print(f"📄 Driver's License: {payload['encodedContextFiles'][0]['fileSize']} bytes")
    print(f"📄 Utility Bill: {payload['encodedContextFiles'][1]['fileSize']} bytes")
    print(f"📄 Bank Statement: {payload['encodedContextFiles'][2]['fileSize']} bytes")
    
    # Test the base64 data
    print("\n🔍 Testing base64 data...")
    for i, file_info in enumerate(payload['encodedContextFiles']):
        data_url = file_info['data']
        base64_data = data_url.split(',')[1]
        valid, size = validate_base64(base64_data)
        print(f"File {i+1} ({file_info['fileName']}): Valid={valid}, Size={size}")
