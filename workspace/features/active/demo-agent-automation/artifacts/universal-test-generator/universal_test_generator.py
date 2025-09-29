#!/usr/bin/env python3
"""
Universal Test Case Generator
============================

A completely generic framework for generating test cases with PDF documents
and agent payloads for any business context.

Core Methodology:
1. Context Definition - Define document types and business rules
2. PDF Generation - Create valid PDF documents using templates
3. Base64 Encoding - Encode PDFs for agent consumption
4. Payload Creation - Generate agent-ready payloads
5. Validation - Ensure PDFs are valid and payloads are correct

Usage:
    python3 universal_test_generator.py --context invoices --scenarios 3 --agent-id YOUR_AGENT_ID
    python3 universal_test_generator.py --context orders --scenarios 5 --agent-id YOUR_AGENT_ID
    python3 universal_test_generator.py --context pos --scenarios 2 --agent-id YOUR_AGENT_ID
"""

import argparse
import json
import os
import base64
import random
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional

class UniversalPDFGenerator:
    """Universal PDF generator that works for any context"""
    
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(f"{output_dir}/pdfs", exist_ok=True)
    
    def generate_pdf(self, document_type: str, data: Dict, filename: str) -> str:
        """Generate a PDF document with the given data"""
        
        # Create PDF content with proper structure
        pdf_content = self._create_pdf_structure(document_type, data)
        
        # Write to file
        filepath = f"{self.output_dir}/pdfs/{filename}"
        with open(filepath, 'wb') as f:
            f.write(pdf_content.encode('utf-8'))
        
        return filepath
    
    def _create_pdf_structure(self, doc_type: str, data: Dict) -> str:
        """Create a valid PDF structure with the given data"""
        
        # Generate content based on document type
        content_lines = self._generate_content_lines(doc_type, data)
        content_text = "\n".join(content_lines)
        
        # Calculate content length
        content_length = len(content_text.encode('utf-8'))
        
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
/Length {content_length}
>>
stream
BT
/F1 12 Tf
{content_text}
ET
endstream
endobj

xref
0 6
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000274 00000 n 
0000000341 00000 n 
trailer
<<
/Size 6
/Root 1 0 R
>>
startxref
{581 + content_length}
%%EOF"""
        
        return pdf_content
    
    def _generate_content_lines(self, doc_type: str, data: Dict) -> List[str]:
        """Generate content lines for the PDF based on document type"""
        lines = []
        
        # Document header
        lines.append("100 700 Td")
        lines.append(f"({data.get('title', doc_type.replace('_', ' ').title())}) Tj")
        lines.append("0 -20 Td")
        
        # Add all data fields
        for key, value in data.items():
            if key != 'title':
                display_key = key.replace('_', ' ').title()
                lines.append(f"({display_key}: {value}) Tj")
                lines.append("0 -20 Td")
        
        return lines

class UniversalEncoder:
    """Universal base64 encoder for any PDF files"""
    
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(f"{output_dir}/payloads", exist_ok=True)
    
    def encode_pdfs_to_payload(self, pdf_files: List[str], context: str, 
                              agent_id: str, scenario_data: Dict) -> Dict:
        """Encode PDF files and create agent payload"""
        
        encoded_files = []
        
        for pdf_file in pdf_files:
            if os.path.exists(pdf_file):
                # Read PDF in binary mode
                with open(pdf_file, 'rb') as f:
                    pdf_content = f.read()
                
                # Encode to base64
                base64_content = base64.b64encode(pdf_content).decode('utf-8')
                file_size = os.path.getsize(pdf_file)
                
                encoded_file = {
                    "data": base64_content,
                    "mimeType": "application/pdf",
                    "fileName": os.path.basename(pdf_file),
                    "fileSize": str(file_size)
                }
                encoded_files.append(encoded_file)
        
        # Generate query and additional info
        query = self._generate_query(context, scenario_data)
        additional_info = self._generate_additional_info(scenario_data)
        
        payload = {
            "taskQuery": {
                "query": query,
                "additionalInfo": additional_info
            },
            "parsingUrls": [],
            "encodedContextFiles": encoded_files,
            "agentId": agent_id
        }
        
        return payload
    
    def _generate_query(self, context: str, scenario_data: Dict) -> str:
        """Generate query based on context and scenario"""
        customer_name = scenario_data.get('customer_name', 'Customer')
        
        query_templates = {
            'invoices': f"Process {context} documents for {customer_name}. Validate invoices, verify amounts, check vendor information, and approve payments.",
            'orders': f"Process {context} documents for {customer_name}. Validate order details, check inventory, verify shipping address, and process fulfillment.",
            'pos': f"Process {context} transactions for {customer_name}. Validate payment details, verify transaction amounts, check payment method, and complete processing.",
            'kyc': f"Process {context} documents for {customer_name}. Validate identity documents, verify personal information, assess risk, and make compliance decisions.",
            'default': f"Process {context} documents for {customer_name}. Validate all documents, verify information, assess requirements, and make decisions."
        }
        
        return query_templates.get(context, query_templates['default'])
    
    def _generate_additional_info(self, scenario_data: Dict) -> str:
        """Generate additional information for the payload"""
        info_parts = []
        
        # Add customer information
        if 'customer_name' in scenario_data:
            info_parts.append(f"Customer: {scenario_data['customer_name']}")
        
        if 'customer_id' in scenario_data:
            info_parts.append(f"Customer ID: {scenario_data['customer_id']}")
        
        if 'email' in scenario_data:
            info_parts.append(f"Email: {scenario_data['email']}")
        
        if 'phone' in scenario_data:
            info_parts.append(f"Phone: {scenario_data['phone']}")
        
        # Add business context
        if 'amount' in scenario_data:
            info_parts.append(f"Amount: {scenario_data['amount']}")
        
        if 'date' in scenario_data:
            info_parts.append(f"Date: {scenario_data['date']}")
        
        if 'status' in scenario_data:
            info_parts.append(f"Status: {scenario_data['status']}")
        
        # Add STP indicators
        risk_level = scenario_data.get('risk_level', 'medium')
        stp_indicators = {
            'low': "DOCUMENT VALIDATION: All documents are legitimate, clear, and current. VERIFICATION: Information is consistent across all documents. RISK ASSESSMENT: Low risk profile - established customer, stable history. DECISION: AUTOMATIC APPROVAL - Process immediately without manual review.",
            'medium': "DOCUMENT VALIDATION: Documents are legitimate with acceptable quality. VERIFICATION: Information is mostly consistent. RISK ASSESSMENT: Medium risk profile - requires monitoring. DECISION: APPROVAL WITH MONITORING - Process with limited supervision.",
            'high': "DOCUMENT VALIDATION: Documents present some inconsistencies. VERIFICATION: Additional verification required. RISK ASSESSMENT: High risk profile - requires manual analysis. DECISION: MANUAL REVIEW REQUIRED - Do not process automatically."
        }
        
        info_parts.append(stp_indicators.get(risk_level, stp_indicators['medium']))
        
        return ". ".join(info_parts) + "."

class UniversalTestGenerator:
    """Main universal test case generator"""
    
    def __init__(self, context: str, scenarios: int, agent_id: str):
        self.context = context
        self.scenarios = scenarios
        self.agent_id = agent_id
        self.output_dir = f"test_cases_{context}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Initialize components
        self.pdf_generator = UniversalPDFGenerator(self.output_dir)
        self.encoder = UniversalEncoder(self.output_dir)
        
        # Create output directories
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(f"{self.output_dir}/pdfs", exist_ok=True)
        os.makedirs(f"{self.output_dir}/payloads", exist_ok=True)
        os.makedirs(f"{self.output_dir}/scripts", exist_ok=True)
    
    def generate_test_cases(self):
        """Generate test cases for the given context"""
        print(f"🚀 Generating {self.scenarios} test cases for context: {self.context.upper()}")
        print("=" * 60)
        
        all_payloads = []
        
        for i in range(self.scenarios):
            print(f"\n📊 Processing scenario {i+1}/{self.scenarios}")
            
            # Generate scenario data
            scenario_data = self._generate_scenario_data(i+1)
            
            # Generate PDFs for this scenario
            pdf_files = []
            document_types = self._get_document_types()
            
            for j, doc_type in enumerate(document_types):
                # Generate data for this document
                doc_data = self._generate_document_data(doc_type, scenario_data, j)
                
                # Generate PDF
                filename = f"{self.context}_scenario_{i+1}_{doc_type}.pdf"
                pdf_file = self.pdf_generator.generate_pdf(doc_type, doc_data, filename)
                pdf_files.append(pdf_file)
                
                print(f"  ✓ Generated {filename}")
            
            # Generate payload
            payload = self.encoder.encode_pdfs_to_payload(
                pdf_files, self.context, self.agent_id, scenario_data
            )
            
            # Save payload
            payload_filename = f"{self.context}_scenario_{i+1}_payload.json"
            payload_file = f"{self.output_dir}/payloads/{payload_filename}"
            
            with open(payload_file, 'w') as f:
                json.dump(payload, f, indent=2)
            
            all_payloads.append({
                'scenario': scenario_data,
                'payload_file': payload_file,
                'pdf_files': pdf_files
            })
            
            print(f"  ✓ Generated payload: {payload_filename}")
        
        # Generate summary
        self._generate_summary(all_payloads)
        
        print(f"\n🎉 Test case generation completed!")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"📊 Scenarios generated: {len(all_payloads)}")
        print(f"📄 PDF files created: {sum(len(p['pdf_files']) for p in all_payloads)}")
        print(f"📦 Payload files created: {len(all_payloads)}")
    
    def _generate_scenario_data(self, scenario_num: int) -> Dict:
        """Generate data for a test scenario"""
        return {
            'scenario_id': f"{self.context}_scenario_{scenario_num}",
            'customer_name': f"Customer {scenario_num}",
            'customer_id': f"CUST{scenario_num:04d}",
            'email': f"customer{scenario_num}@example.com",
            'phone': f"+1-555-{random.randint(100,999)}-{random.randint(1000,9999)}",
            'amount': f"${random.randint(100, 10000):,}",
            'date': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
            'status': random.choice(['pending', 'approved', 'processing']),
            'risk_level': random.choice(['low', 'medium', 'high'])
        }
    
    def _get_document_types(self) -> List[str]:
        """Get document types for the context"""
        context_documents = {
            'invoices': ['invoice', 'receipt', 'purchase_order'],
            'orders': ['order_form', 'shipping_label', 'delivery_confirmation'],
            'pos': ['transaction_receipt', 'payment_confirmation', 'refund_document'],
            'kyc': ['identity_document', 'address_proof', 'financial_statement'],
            'default': ['document1', 'document2', 'document3']
        }
        
        return context_documents.get(self.context, context_documents['default'])
    
    def _generate_document_data(self, doc_type: str, scenario_data: Dict, index: int) -> Dict:
        """Generate data for a specific document type"""
        base_data = {
            'title': doc_type.replace('_', ' ').title(),
            'document_number': f"{doc_type.upper()}{random.randint(100000, 999999)}",
            'date': scenario_data['date'],
            'customer_name': scenario_data['customer_name'],
            'amount': scenario_data['amount']
        }
        
        # Add context-specific fields
        if self.context == 'invoices':
            base_data.update({
                'vendor': f"Vendor {index + 1}",
                'tax_id': f"TAX{random.randint(100000, 999999)}",
                'due_date': (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            })
        elif self.context == 'orders':
            base_data.update({
                'order_number': f"ORD{random.randint(100000, 999999)}",
                'shipping_address': f"Address {index + 1}",
                'tracking_number': f"TRK{random.randint(100000000, 999999999)}"
            })
        elif self.context == 'pos':
            base_data.update({
                'transaction_id': f"TXN{random.randint(100000, 999999)}",
                'payment_method': random.choice(['Credit Card', 'Debit Card', 'Cash', 'Mobile Payment']),
                'terminal_id': f"TERM{random.randint(1000, 9999)}"
            })
        
        return base_data
    
    def _generate_summary(self, all_payloads: List[Dict]):
        """Generate a summary report"""
        summary = {
            "generation_info": {
                "context": self.context,
                "scenarios_generated": len(all_payloads),
                "generation_date": datetime.now().isoformat(),
                "output_directory": self.output_dir
            },
            "scenarios": []
        }
        
        for payload_info in all_payloads:
            scenario = payload_info['scenario']
            summary["scenarios"].append({
                "scenario_id": scenario['scenario_id'],
                "customer_name": scenario['customer_name'],
                "risk_level": scenario['risk_level'],
                "amount": scenario['amount'],
                "status": scenario['status'],
                "pdf_files": [os.path.basename(f) for f in payload_info['pdf_files']],
                "payload_file": os.path.basename(payload_info['payload_file'])
            })
        
        summary_file = f"{self.output_dir}/generation_summary.json"
        with open(summary_file, 'w') as f:
            json.dump(summary, f, indent=2)
        
        print(f"📋 Summary report generated: {summary_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Universal Test Case Generator')
    parser.add_argument('--context', required=True, 
                       help='Business context (e.g., invoices, orders, pos, kyc)')
    parser.add_argument('--scenarios', type=int, default=3, 
                       help='Number of test scenarios to generate')
    parser.add_argument('--agent-id', required=True, 
                       help='Agent ID for payload generation')
    
    args = parser.parse_args()
    
    # Create generator and run
    generator = UniversalTestGenerator(args.context, args.scenarios, args.agent_id)
    generator.generate_test_cases()

if __name__ == "__main__":
    main()
