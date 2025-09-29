#!/usr/bin/env python3
"""
Create working PDFs using a different approach - HTML to PDF conversion
"""

import base64
import os
import json
import subprocess
import tempfile

def create_html_document(title, content_lines, filename):
    """Create an HTML document that can be converted to PDF"""
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{ 
            font-family: Arial, sans-serif; 
            margin: 40px; 
            line-height: 1.6;
        }}
        .header {{ 
            text-align: center; 
            margin-bottom: 30px; 
            border-bottom: 2px solid #333;
            padding-bottom: 20px;
        }}
        .content {{ 
            margin: 20px 0; 
        }}
        .line {{ 
            margin: 8px 0; 
            padding: 5px 0;
        }}
        .amount {{ 
            font-size: 18px; 
            font-weight: bold; 
            color: #cc0000; 
        }}
        .balance {{ 
            font-size: 18px; 
            font-weight: bold; 
            color: #006600; 
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
    </div>
    
    <div class="content">
"""
    
    for line in content_lines:
        if line.startswith("Amount Due:") or "Balance:" in line:
            html_content += f'        <div class="line"><span class="amount">{line}</span></div>\n'
        elif line.startswith("Current Balance:") or line.startswith("Available Balance:"):
            html_content += f'        <div class="line"><span class="balance">{line}</span></div>\n'
        elif line == "":
            html_content += '        <div class="line"><br></div>\n'
        else:
            html_content += f'        <div class="line">{line}</div>\n'
    
    html_content += """    </div>
</body>
</html>"""
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    return filename

def html_to_pdf_with_wkhtmltopdf(html_file, pdf_file):
    """Convert HTML to PDF using wkhtmltopdf"""
    try:
        # Try to use wkhtmltopdf if available
        result = subprocess.run([
            'wkhtmltopdf', 
            '--page-size', 'A4',
            '--margin-top', '0.75in',
            '--margin-right', '0.75in',
            '--margin-bottom', '0.75in',
            '--margin-left', '0.75in',
            '--encoding', 'UTF-8',
            html_file, 
            pdf_file
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
        else:
            print(f"wkhtmltopdf error: {result.stderr}")
            return False
    except FileNotFoundError:
        print("wkhtmltopdf not found, trying alternative method")
        return False

def create_simple_pdf_manual(title, content_lines, filename):
    """Create a very simple PDF manually with minimal structure"""
    
    # Create a minimal but valid PDF
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
/Resources <<
/Font <<
/F1 5 0 R
>>
>>
>>
endobj

4 0 obj
<<
/Length 200
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

5 0 obj
<<
/Type /Font
/Subtype /Type1
/BaseFont /Helvetica
>>
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
400
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
        "Amount Due: $125.50",
        "",
        "Thank you for choosing Austin Energy",
        "For questions, call 512-494-9400"
    ]
    
    # Try HTML to PDF first
    html_file = "utility_bill_temp.html"
    pdf_file = "utility_bill_working.pdf"
    
    create_html_document("AUSTIN ENERGY UTILITY BILL", content, html_file)
    
    if html_to_pdf_with_wkhtmltopdf(html_file, pdf_file):
        os.remove(html_file)  # Clean up
        return pdf_file
    else:
        # Fallback to manual PDF
        os.remove(html_file)  # Clean up
        return create_simple_pdf_manual("AUSTIN ENERGY UTILITY BILL", content, pdf_file)

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
    
    # Try HTML to PDF first
    html_file = "bank_statement_temp.html"
    pdf_file = "bank_statement_working.pdf"
    
    create_html_document("CHASE BANK STATEMENT", content, html_file)
    
    if html_to_pdf_with_wkhtmltopdf(html_file, pdf_file):
        os.remove(html_file)  # Clean up
        return pdf_file
    else:
        # Fallback to manual PDF
        os.remove(html_file)  # Clean up
        return create_simple_pdf_manual("CHASE BANK STATEMENT", content, pdf_file)

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
    
    # Try HTML to PDF first
    html_file = "drivers_license_temp.html"
    pdf_file = "drivers_license_working.pdf"
    
    create_html_document("TEXAS DRIVER LICENSE", content, html_file)
    
    if html_to_pdf_with_wkhtmltopdf(html_file, pdf_file):
        os.remove(html_file)  # Clean up
        return pdf_file
    else:
        # Fallback to manual PDF
        os.remove(html_file)  # Clean up
        return create_simple_pdf_manual("TEXAS DRIVER LICENSE", content, pdf_file)

def encode_pdf_to_base64(pdf_path):
    """Encode a PDF file to base64 string following proper guidelines"""
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

def create_working_kyc_payload():
    """Create KYC payload with working PDFs"""
    
    # Create PDFs
    print("Creating working PDF documents...")
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
    print("Creating working PDFs with proper encoding...")
    
    # Create payload
    payload = create_working_kyc_payload()
    
    if payload:
        # Save payload
        with open('working_kyc_payload.json', 'w') as f:
            json.dump(payload, f, indent=2)
        
        print("✅ Successfully created:")
        print("  - utility_bill_working.pdf")
        print("  - bank_statement_working.pdf") 
        print("  - drivers_license_working.pdf")
        print("  - working_kyc_payload.json")
        
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
            pdf_path = filename.replace('.pdf', '_working.pdf')
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as f:
                    header = f.read(8)
                    print(f"  - {filename}: PDF header = {header}")
                    
                    # Try to read more to verify structure
                    f.seek(0)
                    content = f.read(100)
                    if b'%%EOF' in content:
                        print(f"    ✅ Valid PDF structure detected")
                    else:
                        print(f"    ⚠️  PDF structure may be incomplete")
    else:
        print("❌ Failed to create payload")

if __name__ == "__main__":
    main()
