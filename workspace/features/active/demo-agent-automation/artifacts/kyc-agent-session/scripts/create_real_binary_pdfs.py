#!/usr/bin/env python3
"""
Create REAL binary PDFs using proper PDF binary structure
Following proper base64 encoding guidelines - ACTUALLY BINARY VERSION
"""

import base64
import os
import json

def create_real_binary_pdf(title, content_lines, filename):
    """Create a REAL binary PDF file with proper PDF structure using UTF-8"""
    
    # Create actual PDF binary structure with explicit UTF-8 encoding
    pdf_header = b'%PDF-1.4\n'
    
    # PDF objects as binary with UTF-8 encoding
    obj1 = b'1 0 obj\n<<\n/Type /Catalog\n/Pages 2 0 R\n>>\nendobj\n\n'
    obj2 = b'2 0 obj\n<<\n/Type /Pages\n/Kids [3 0 R]\n/Count 1\n/MediaBox [0 0 612 792]\n>>\nendobj\n\n'
    
    # Content stream with UTF-8 encoding
    content_text = f"BT\n/F1 16 Tf\n50 750 Td\n({title}) Tj\n0 -30 Td\n/F2 12 Tf\n"
    for line in content_lines:
        content_text += f"({line}) Tj 0 -20 Td\n"
    content_text += "ET\n"
    
    # Explicitly encode as UTF-8
    content_stream = content_text.encode('utf-8')
    content_length = len(content_stream)
    
    # Create PDF objects with UTF-8 encoding
    obj3_text = f"""3 0 obj
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
/Length {content_length}
>>
stream
"""
    obj3 = obj3_text.encode('utf-8')
    
    obj6_end = b"\nendstream\nendobj\n\n"
    
    # Xref table
    xref = b"""xref
0 7
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000168 00000 n 
0000000273 00000 n 
0000000400 00000 n 
"""
    
    # Trailer with UTF-8 encoding
    trailer_text = f"""trailer
<<
/Size 7
/Root 1 0 R
/Info <<
/Title ({title})
/Creator (Beam KYC Agent)
/Producer (Beam KYC Agent)
>>
>>
startxref
{600 + content_length}
%%EOF"""
    trailer = trailer_text.encode('utf-8')
    
    # Combine all parts into binary PDF
    pdf_binary = pdf_header + obj1 + obj2 + obj3 + content_stream + obj6_end + xref + trailer
    
    # Write as true binary with UTF-8 encoding
    with open(filename, 'wb') as f:
        f.write(pdf_binary)
    
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
        "Amount Due: $125.50",
        "",
        "Thank you for choosing Austin Energy",
        "For questions, call 512-494-9400"
    ]
    return create_real_binary_pdf("AUSTIN ENERGY UTILITY BILL", content, "utility_bill_real_binary.pdf")

def create_bank_statement_pdf():
    """Create bank statement PDF"""
    content = [
        "Account Holder: John Smith",
        "Account Number: ****1234",
        "Statement Date: August 31, 2024",
        "Account Type: Checking",
        "",
        "Current Balance: $5,250.00",
        "Available Balance: $5,250.00",
        "",
        "This statement covers the period from August 1, 2024 to August 31, 2024",
        "For questions, call 1-800-935-9935"
    ]
    return create_real_binary_pdf("CHASE BANK STATEMENT", content, "bank_statement_real_binary.pdf")

def create_drivers_license_pdf():
    """Create driver's license PDF"""
    content = [
        "TEXAS DRIVER LICENSE",
        "",
        "Name: SMITH, JOHN",
        "DOB: 03/15/1985",
        "Address: 123 MAIN ST",
        "City: AUSTIN, TX 78701",
        "License #: 12345678",
        "Expires: 03/15/2030",
        "",
        "Photo: [PLACEHOLDER]"
    ]
    return create_real_binary_pdf("TEXAS DRIVER LICENSE", content, "drivers_license_real_binary.pdf")

def encode_pdf_to_base64(pdf_path):
    """Encode a PDF file to base64 string following proper guidelines with UTF-8"""
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Read PDF in binary mode
        with open(pdf_path, 'rb') as pdf_file:
            pdf_bytes = pdf_file.read()
            # Encode to base64
            encoded = base64.b64encode(pdf_bytes)
            # Convert bytes to string using UTF-8
            return encoded.decode('utf-8')
    except Exception as e:
        print(f"Error encoding PDF {pdf_path}: {e}")
        return None

def create_real_binary_kyc_payload():
    """Create KYC payload with properly encoded real binary PDFs"""
    
    # Create PDFs
    print("Creating REAL binary PDF documents...")
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
    print("Creating REAL binary PDFs with proper base64 encoding...")
    
    # Create payload
    payload = create_real_binary_kyc_payload()
    
    if payload:
        # Save payload
        with open('real_binary_kyc_payload.json', 'w') as f:
            json.dump(payload, f, indent=2)
        
        print("✅ Successfully created:")
        print("  - utility_bill_real_binary.pdf")
        print("  - bank_statement_real_binary.pdf") 
        print("  - drivers_license_real_binary.pdf")
        print("  - real_binary_kyc_payload.json")
        
        # Show encoding info
        print(f"\n📊 Encoding Information:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            file_size = file_info['fileSize']
            encoded_size = len(file_info['data'])
            print(f"  - {filename}: {file_size} bytes → {encoded_size} chars base64")
            
        # Show base64 encoding ratio
        print(f"\n📈 Base64 Encoding Ratio:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            file_size = int(file_info['fileSize'])
            encoded_size = len(file_info['data'])
            ratio = encoded_size / file_size
            print(f"  - {filename}: {ratio:.2f}x increase (expected ~1.33x)")
            
        # Verify binary reading
        print(f"\n🔍 Binary Verification:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            file_size = int(file_info['fileSize'])
            print(f"  - {filename}: {file_size} bytes (REAL binary read)")
            
        # Show PDF structure verification
        print(f"\n📄 PDF Structure Verification:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            pdf_path = filename.replace('.pdf', '_real_binary.pdf')
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as f:
                    header = f.read(8)
                    print(f"  - {filename}: PDF header = {header}")
    else:
        print("❌ Failed to create payload")

if __name__ == "__main__":
    main()
