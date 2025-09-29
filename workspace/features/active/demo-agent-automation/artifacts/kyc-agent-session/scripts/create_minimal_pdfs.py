#!/usr/bin/env python3
"""
Create minimal working PDFs using the simplest possible approach
"""

import base64
import os
import json

def create_minimal_pdf(title, content_lines, filename):
    """Create the most minimal PDF possible that should work"""
    
    # Ultra-minimal PDF structure
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
>>
endobj

3 0 obj
<<
/Type /Page
/Parent 2 0 R
/MediaBox [0 0 612 792]
/Contents 4 0 R
>>
endobj

4 0 obj
<<
/Length 100
>>
stream
BT
/F1 12 Tf
50 750 Td
({title}) Tj
0 -20 Td
{chr(10).join([f'({line}) Tj 0 -15 Td' for line in content_lines if line.strip()])}
ET
endstream
endobj

xref
0 5
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000168 00000 n 
trailer
<<
/Size 5
/Root 1 0 R
>>
startxref
300
%%EOF"""
    
    # Write as binary
    with open(filename, 'wb') as f:
        f.write(pdf_content.encode('utf-8'))
    
    return filename

def create_utility_bill_pdf():
    """Create utility bill PDF"""
    content = [
        "Account Number: 1234567890",
        "Service Address: 123 MAIN ST, AUSTIN, TX 78701",
        "Billing Date: September 1, 2024",
        "Due Date: September 30, 2024",
        "Customer: John Smith",
        "",
        "Amount Due: $125.50"
    ]
    return create_minimal_pdf("AUSTIN ENERGY UTILITY BILL", content, "utility_bill_minimal.pdf")

def create_bank_statement_pdf():
    """Create bank statement PDF"""
    content = [
        "Account Holder: John Smith",
        "Account Number: ****1234",
        "Statement Date: August 31, 2024",
        "Account Type: Checking",
        "",
        "Current Balance: $5,250.00",
        "Available Balance: $5,250.00"
    ]
    return create_minimal_pdf("CHASE BANK STATEMENT", content, "bank_statement_minimal.pdf")

def create_drivers_license_pdf():
    """Create driver's license PDF"""
    content = [
        "Name: SMITH, JOHN",
        "DOB: 03/15/1985",
        "Address: 123 MAIN ST",
        "City: AUSTIN, TX 78701",
        "License #: 12345678",
        "Expires: 03/15/2030"
    ]
    return create_minimal_pdf("TEXAS DRIVER LICENSE", content, "drivers_license_minimal.pdf")

def encode_pdf_to_base64(pdf_path):
    """Encode a PDF file to base64 string"""
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Read PDF in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            pdf_bytes = pdf_file.read()
            # Encode to base64
            encoded = base64.b64encode(pdf_bytes)
            # Convert bytes to string
            return encoded.decode('utf-8')
    except Exception as e:
        print(f"Error encoding PDF {pdf_path}: {e}")
        return None

def create_minimal_kyc_payload():
    """Create KYC payload with minimal PDFs"""
    
    # Create PDFs
    print("Creating minimal PDF documents...")
    utility_pdf = create_utility_bill_pdf()
    bank_pdf = create_bank_statement_pdf()
    license_pdf = create_drivers_license_pdf()
    
    # Encode PDFs to base64
    print("Encoding PDFs to base64...")
    utility_b64 = encode_pdf_to_base64(utility_pdf)
    bank_b64 = encode_pdf_to_base64(bank_pdf)
    license_b64 = encode_pdf_to_base64(license_pdf)
    
    if not all([utility_b64, bank_b64, license_b64]):
        print("Error: Failed to encode one or more PDFs")
        return None
    
    # Get file sizes
    utility_size = os.path.getsize(utility_pdf)
    bank_size = os.path.getsize(bank_pdf)
    license_size = os.path.getsize(license_pdf)
    
    # Create payload
    payload = {
        "taskQuery": {
            "query": "Process KYC documents for customer John Smith with driver's license, utility bill, and bank statement. Validate documents, verify identity, assess risk, and make compliance decision.",
            "additionalInfo": "Customer: John Smith, DOB: 1985-03-15, Address: 123 Main Street, Austin, TX 78701, Occupation: Software Engineer, Income: $75,000-$100,000"
        },
        "parsingUrls": [],
        "encodedContextFiles": [
            {
                "data": f"data:application/pdf;base64,{license_b64}",
                "mimeType": "application/pdf",
                "fileName": "drivers_license.pdf",
                "fileSize": str(license_size)
            },
            {
                "data": f"data:application/pdf;base64,{utility_b64}",
                "mimeType": "application/pdf",
                "fileName": "utility_bill.pdf",
                "fileSize": str(utility_size)
            },
            {
                "data": f"data:application/pdf;base64,{bank_b64}",
                "mimeType": "application/pdf",
                "fileName": "bank_statement.pdf",
                "fileSize": str(bank_size)
            }
        ],
        "agentId": "d8b2e9b5-20da-4e69-81cf-5af2933124c9"
    }
    
    return payload

def main():
    """Main function"""
    print("Creating minimal PDFs...")
    
    # Create payload
    payload = create_minimal_kyc_payload()
    
    if payload:
        # Save payload
        with open('minimal_kyc_payload.json', 'w') as f:
            json.dump(payload, f, indent=2)
        
        print("✅ Successfully created:")
        print("  - utility_bill_minimal.pdf")
        print("  - bank_statement_minimal.pdf") 
        print("  - drivers_license_minimal.pdf")
        print("  - minimal_kyc_payload.json")
        
        # Show encoding info
        print(f"\n📊 Encoding Information:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            file_size = file_info['fileSize']
            encoded_size = len(file_info['data'])
            print(f"  - {filename}: {file_size} bytes → {encoded_size} chars base64")
            
        # Test PDF validity
        print(f"\n🔍 PDF Validity Test:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            pdf_path = filename.replace('.pdf', '_minimal.pdf')
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as f:
                    header = f.read(8)
                    print(f"  - {filename}: PDF header = {header}")
    else:
        print("❌ Failed to create payload")

if __name__ == "__main__":
    main()
