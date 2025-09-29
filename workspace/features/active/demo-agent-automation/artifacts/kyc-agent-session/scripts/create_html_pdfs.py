#!/usr/bin/env python3
"""
Create HTML-based PDFs for KYC documents
"""

import base64
import json

def create_utility_bill_html():
    """Create HTML for utility bill"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Austin Energy Utility Bill</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { text-align: center; margin-bottom: 30px; }
            .company-name { font-size: 24px; font-weight: bold; color: #0066cc; }
            .bill-title { font-size: 18px; margin-top: 10px; }
            .bill-info { margin: 20px 0; }
            .info-row { margin: 8px 0; }
            .label { font-weight: bold; display: inline-block; width: 150px; }
            .amount { font-size: 18px; font-weight: bold; color: #cc0000; }
            .footer { margin-top: 40px; font-size: 12px; color: #666; }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="company-name">AUSTIN ENERGY</div>
            <div class="bill-title">UTILITY BILL</div>
        </div>
        
        <div class="bill-info">
            <div class="info-row">
                <span class="label">Account Number:</span> 1234567890
            </div>
            <div class="info-row">
                <span class="label">Service Address:</span> 123 MAIN ST, AUSTIN, TX 78701
            </div>
            <div class="info-row">
                <span class="label">Billing Date:</span> September 1, 2024
            </div>
            <div class="info-row">
                <span class="label">Due Date:</span> September 30, 2024
            </div>
            <div class="info-row">
                <span class="label">Customer:</span> John Smith
            </div>
        </div>
        
        <div class="bill-info">
            <div class="info-row">
                <span class="label">Amount Due:</span> <span class="amount">$125.50</span>
            </div>
        </div>
        
        <div class="footer">
            <p>Thank you for choosing Austin Energy</p>
            <p>For questions, call 512-494-9400</p>
        </div>
    </body>
    </html>
    """
    return html_content

def create_bank_statement_html():
    """Create HTML for bank statement"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Chase Bank Statement</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { text-align: center; margin-bottom: 30px; }
            .bank-name { font-size: 24px; font-weight: bold; color: #0066cc; }
            .statement-title { font-size: 18px; margin-top: 10px; }
            .account-info { margin: 20px 0; }
            .info-row { margin: 8px 0; }
            .label { font-weight: bold; display: inline-block; width: 150px; }
            .balance { font-size: 18px; font-weight: bold; color: #006600; }
            .footer { margin-top: 40px; font-size: 12px; color: #666; }
        </style>
    </head>
    <body>
        <div class="header">
            <div class="bank-name">CHASE BANK</div>
            <div class="statement-title">BANK STATEMENT</div>
        </div>
        
        <div class="account-info">
            <div class="info-row">
                <span class="label">Account Holder:</span> John Smith
            </div>
            <div class="info-row">
                <span class="label">Account Number:</span> ****1234
            </div>
            <div class="info-row">
                <span class="label">Statement Date:</span> August 31, 2024
            </div>
            <div class="info-row">
                <span class="label">Account Type:</span> Checking
            </div>
        </div>
        
        <div class="account-info">
            <div class="info-row">
                <span class="label">Current Balance:</span> <span class="balance">$5,250.00</span>
            </div>
            <div class="info-row">
                <span class="label">Available Balance:</span> <span class="balance">$5,250.00</span>
            </div>
        </div>
        
        <div class="footer">
            <p>This statement covers the period from August 1, 2024 to August 31, 2024</p>
            <p>For questions, call 1-800-935-9935</p>
        </div>
    </body>
    </html>
    """
    return html_content

def create_drivers_license_html():
    """Create HTML for driver's license"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Texas Driver's License</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .license { border: 3px solid #000; padding: 20px; width: 400px; margin: 0 auto; }
            .header { text-align: center; margin-bottom: 20px; }
            .state-name { font-size: 20px; font-weight: bold; }
            .license-title { font-size: 16px; margin-top: 5px; }
            .license-info { margin: 15px 0; }
            .info-row { margin: 8px 0; }
            .label { font-weight: bold; display: inline-block; width: 120px; }
            .photo-placeholder { 
                width: 80px; height: 100px; 
                border: 2px solid #000; 
                background-color: #f0f0f0; 
                display: inline-block; 
                vertical-align: top;
                margin-right: 20px;
            }
            .info-section { display: inline-block; vertical-align: top; }
        </style>
    </head>
    <body>
        <div class="license">
            <div class="header">
                <div class="state-name">TEXAS</div>
                <div class="license-title">DRIVER LICENSE</div>
            </div>
            
            <div class="license-info">
                <div class="photo-placeholder">PHOTO</div>
                <div class="info-section">
                    <div class="info-row">
                        <span class="label">Name:</span> SMITH, JOHN
                    </div>
                    <div class="info-row">
                        <span class="label">DOB:</span> 03/15/1985
                    </div>
                    <div class="info-row">
                        <span class="label">Address:</span> 123 MAIN ST
                    </div>
                    <div class="info-row">
                        <span class="label">City:</span> AUSTIN, TX 78701
                    </div>
                    <div class="info-row">
                        <span class="label">License #:</span> 12345678
                    </div>
                    <div class="info-row">
                        <span class="label">Expires:</span> 03/15/2030
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

def html_to_base64(html_content):
    """Convert HTML to base64"""
    return base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

def create_html_payload():
    """Create payload with HTML-based documents"""
    
    # Create HTML documents
    utility_html = create_utility_bill_html()
    bank_html = create_bank_statement_html()
    license_html = create_drivers_license_html()
    
    # Convert to base64
    utility_b64 = html_to_base64(utility_html)
    bank_b64 = html_to_base64(bank_html)
    license_b64 = html_to_base64(license_html)
    
    # Create payload
    payload = {
        "taskQuery": {
            "query": "Process KYC documents for customer John Smith with driver's license, utility bill, and bank statement. Validate documents, verify identity, assess risk, and make compliance decision.",
            "additionalInfo": "Customer: John Smith, DOB: 1985-03-15, Address: 123 Main Street, Austin, TX 78701, Occupation: Software Engineer, Income: $75,000-$100,000"
        },
        "parsingUrls": [],
        "encodedContextFiles": [
            {
                "data": f"data:text/html;base64,{license_b64}",
                "mimeType": "text/html",
                "fileName": "drivers_license.html",
                "fileSize": str(len(license_html))
            },
            {
                "data": f"data:text/html;base64,{utility_b64}",
                "mimeType": "text/html",
                "fileName": "utility_bill.html",
                "fileSize": str(len(utility_html))
            },
            {
                "data": f"data:text/html;base64,{bank_b64}",
                "mimeType": "text/html",
                "fileName": "bank_statement.html",
                "fileSize": str(len(bank_html))
            }
        ],
        "agentId": "d8b2e9b5-20da-4e69-81cf-5af2933124c9"
    }
    
    return payload

def main():
    """Main function"""
    print("Creating HTML-based KYC documents...")
    
    # Create payload
    payload = create_html_payload()
    
    # Save payload
    with open('html_kyc_payload.json', 'w') as f:
        json.dump(payload, f, indent=2)
    
    # Save individual HTML files
    with open('drivers_license.html', 'w') as f:
        f.write(create_drivers_license_html())
    
    with open('utility_bill.html', 'w') as f:
        f.write(create_utility_bill_html())
    
    with open('bank_statement.html', 'w') as f:
        f.write(create_bank_statement_html())
    
    print("✅ HTML documents created:")
    print("  - drivers_license.html")
    print("  - utility_bill.html") 
    print("  - bank_statement.html")
    print("  - html_kyc_payload.json")
    
    print(f"\n📊 File sizes:")
    print(f"  - License HTML: {len(create_drivers_license_html())} bytes")
    print(f"  - Utility HTML: {len(create_utility_bill_html())} bytes")
    print(f"  - Bank HTML: {len(create_bank_statement_html())} bytes")

if __name__ == "__main__":
    main()
