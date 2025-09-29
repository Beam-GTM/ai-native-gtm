#!/usr/bin/env python3
"""
Script to create actual KYC documents and encode them to base64
"""

import base64
import json
from io import BytesIO

def create_drivers_license():
    """Create a simple driver's license image and encode to base64"""
    try:
        from PIL import Image, ImageDraw, ImageFont
        
        # Create a simple driver's license image
        img = Image.new('RGB', (600, 400), color='white')
        draw = ImageDraw.Draw(img)
        
        # Add border
        draw.rectangle([10, 10, 590, 390], outline='black', width=3)
        
        # Add text content
        draw.text((50, 50), 'TEXAS DRIVER LICENSE', fill='black')
        draw.text((50, 100), 'Name: JOHN SMITH', fill='black')
        draw.text((50, 130), 'DOB: 03/15/1985', fill='black')
        draw.text((50, 160), 'Address: 123 MAIN ST, AUSTIN, TX 78701', fill='black')
        draw.text((50, 190), 'License #: DL123456789', fill='black')
        draw.text((50, 220), 'Expires: 03/15/2026', fill='black')
        draw.text((50, 250), 'Class: C', fill='black')
        draw.text((50, 280), 'Height: 6-0', fill='black')
        draw.text((50, 310), 'Weight: 180', fill='black')
        draw.text((50, 340), 'Sex: M', fill='black')
        
        # Convert to base64
        buffer = BytesIO()
        img.save(buffer, format='JPEG')
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return img_base64, len(buffer.getvalue())
        
    except ImportError:
        print("PIL not available, creating minimal base64")
        # Fallback: create a minimal valid JPEG base64
        minimal_jpeg = "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/2wBDAQcHBwoIChMKChMoGhYaKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCj/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAv/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFQEBAQAAAAAAAAAAAAAAAAAAAAX/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCdABmX/9k="
        return minimal_jpeg, 1024

def create_pdf_document(title, content):
    """Create a simple PDF document and encode to base64"""
    # Minimal valid PDF content
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
/MediaBox [0 0 595 842]
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
/Length 44
>>
stream
BT
/F1 12 Tf
250 700 Td
({title}) Tj
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
365
%%EOF"""
    
    pdf_bytes = pdf_content.encode('utf-8')
    pdf_base64 = base64.b64encode(pdf_bytes).decode()
    
    return pdf_base64, len(pdf_bytes)

def create_kyc_payload():
    """Create the complete KYC payload with real base64 documents"""
    
    # Create documents
    print("Creating driver's license...")
    dl_base64, dl_size = create_drivers_license()
    
    print("Creating utility bill PDF...")
    utility_base64, utility_size = create_pdf_document("AUSTIN ENERGY UTILITY BILL", "Account: 1234567890\\nService Address: 123 MAIN ST, AUSTIN, TX 78701\\nBilling Date: 2024-09-01\\nAmount Due: $125.50")
    
    print("Creating bank statement PDF...")
    bank_base64, bank_size = create_pdf_document("CHASE BANK STATEMENT", "Account Holder: JOHN SMITH\\nAccount: ****1234\\nStatement Date: 2024-08-31\\nBalance: $5,250.00")
    
    # Create the payload
    payload = {
        "taskQuery": {
            "query": "Process KYC documents for customer John Smith with driver's license, utility bill, and bank statement. Validate documents, verify identity, assess risk, and make compliance decision.",
            "additionalInfo": "Customer: John Smith, DOB: 1985-03-15, Address: 123 Main Street, Austin, TX 78701, Occupation: Software Engineer, Income: $75,000-$100,000"
        },
        "parsingUrls": [],
        "encodedContextFiles": [
            {
                "data": f"data:image/jpeg;base64,{dl_base64}",
                "mimeType": "image/jpeg",
                "fileName": "drivers_license.jpg",
                "fileSize": str(dl_size)
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
    print("Creating KYC documents and payload...")
    
    payload = create_kyc_payload()
    
    # Save to file
    with open('real_kyc_payload.json', 'w') as f:
        json.dump(payload, f, indent=2)
    
    print("✅ Real KYC payload created: real_kyc_payload.json")
    print(f"📄 Driver's License: {payload['encodedContextFiles'][0]['fileSize']} bytes")
    print(f"📄 Utility Bill: {payload['encodedContextFiles'][1]['fileSize']} bytes")
    print(f"📄 Bank Statement: {payload['encodedContextFiles'][2]['fileSize']} bytes")
