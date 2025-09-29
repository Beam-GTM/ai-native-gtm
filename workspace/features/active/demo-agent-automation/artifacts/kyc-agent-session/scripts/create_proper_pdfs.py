#!/usr/bin/env python3
"""
Create proper PDFs and encode them correctly for KYC agent
Following proper base64 encoding guidelines
"""

import base64
import os
import json
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import black, blue, red

def create_utility_bill_pdf():
    """Create a proper utility bill PDF"""
    filename = 'utility_bill_proper.pdf'
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(blue)
    c.drawString(50, height - 50, "AUSTIN ENERGY")
    
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(black)
    c.drawString(50, height - 80, "UTILITY BILL")
    
    # Account Information
    y_pos = height - 120
    c.setFont("Helvetica", 12)
    c.drawString(50, y_pos, "Account Number: 1234567890")
    y_pos -= 20
    c.drawString(50, y_pos, "Service Address: 123 MAIN ST, AUSTIN, TX 78701")
    y_pos -= 20
    c.drawString(50, y_pos, "Billing Date: September 1, 2024")
    y_pos -= 20
    c.drawString(50, y_pos, "Due Date: September 30, 2024")
    y_pos -= 20
    c.drawString(50, y_pos, "Customer: John Smith")
    
    # Amount Due
    y_pos -= 40
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(red)
    c.drawString(50, y_pos, "Amount Due: $125.50")
    
    # Footer
    y_pos = 100
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    c.drawString(50, y_pos, "Thank you for choosing Austin Energy")
    c.drawString(50, y_pos - 15, "For questions, call 512-494-9400")
    
    c.save()
    return filename

def create_bank_statement_pdf():
    """Create a proper bank statement PDF"""
    filename = 'bank_statement_proper.pdf'
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    # Header
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(blue)
    c.drawString(50, height - 50, "CHASE BANK")
    
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(black)
    c.drawString(50, height - 80, "BANK STATEMENT")
    
    # Account Information
    y_pos = height - 120
    c.setFont("Helvetica", 12)
    c.drawString(50, y_pos, "Account Holder: John Smith")
    y_pos -= 20
    c.drawString(50, y_pos, "Account Number: ****1234")
    y_pos -= 20
    c.drawString(50, y_pos, "Statement Date: August 31, 2024")
    y_pos -= 20
    c.drawString(50, y_pos, "Account Type: Checking")
    
    # Balance Information
    y_pos -= 40
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(blue)
    c.drawString(50, y_pos, "Current Balance: $5,250.00")
    y_pos -= 25
    c.drawString(50, y_pos, "Available Balance: $5,250.00")
    
    # Footer
    y_pos = 100
    c.setFont("Helvetica", 10)
    c.setFillColor(black)
    c.drawString(50, y_pos, "This statement covers the period from August 1, 2024 to August 31, 2024")
    c.drawString(50, y_pos - 15, "For questions, call 1-800-935-9935")
    
    c.save()
    return filename

def create_drivers_license_pdf():
    """Create a driver's license as PDF (since we can't create proper images)"""
    filename = 'drivers_license_proper.pdf'
    c = canvas.Canvas(filename, pagesize=(4*inch, 2.5*inch))  # License size
    width, height = 4*inch, 2.5*inch
    
    # Border
    c.rect(10, 10, width-20, height-20)
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20, height - 30, "TEXAS")
    c.setFont("Helvetica-Bold", 12)
    c.drawString(20, height - 45, "DRIVER LICENSE")
    
    # Photo placeholder
    c.rect(width - 80, height - 80, 60, 60)
    c.setFont("Helvetica", 8)
    c.drawString(width - 75, height - 50, "PHOTO")
    
    # License Information
    y_pos = height - 80
    c.setFont("Helvetica", 10)
    c.drawString(20, y_pos, "Name: SMITH, JOHN")
    y_pos -= 15
    c.drawString(20, y_pos, "DOB: 03/15/1985")
    y_pos -= 15
    c.drawString(20, y_pos, "Address: 123 MAIN ST")
    y_pos -= 15
    c.drawString(20, y_pos, "City: AUSTIN, TX 78701")
    y_pos -= 15
    c.drawString(20, y_pos, "License #: 12345678")
    y_pos -= 15
    c.drawString(20, y_pos, "Expires: 03/15/2030")
    
    c.save()
    return filename

def encode_pdf_to_base64(pdf_path):
    """Encode a PDF file to base64 string following proper guidelines"""
    try:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        with open(pdf_path, 'rb') as pdf_file:
            pdf_bytes = pdf_file.read()
            encoded = base64.b64encode(pdf_bytes)
            return encoded.decode('utf-8')
    except Exception as e:
        print(f"Error encoding PDF {pdf_path}: {e}")
        return None

def create_proper_kyc_payload():
    """Create KYC payload with properly encoded PDFs"""
    
    # Create PDFs
    print("Creating PDF documents...")
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
    print("Creating proper PDFs with correct base64 encoding...")
    
    # Create payload
    payload = create_proper_kyc_payload()
    
    if payload:
        # Save payload
        with open('proper_kyc_payload.json', 'w') as f:
            json.dump(payload, f, indent=2)
        
        print("✅ Successfully created:")
        print("  - utility_bill_proper.pdf")
        print("  - bank_statement_proper.pdf") 
        print("  - drivers_license_proper.pdf")
        print("  - proper_kyc_payload.json")
        
        # Show encoding info
        print(f"\n📊 Encoding Information:")
        for file_info in payload['encodedContextFiles']:
            filename = file_info['fileName']
            file_size = file_info['fileSize']
            encoded_size = len(file_info['data'])
            print(f"  - {filename}: {file_size} bytes → {encoded_size} chars base64")
    else:
        print("❌ Failed to create payload")

if __name__ == "__main__":
    main()
