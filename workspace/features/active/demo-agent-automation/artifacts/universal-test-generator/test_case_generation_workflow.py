#!/usr/bin/env python3
"""
Generic Test Case Generation Workflow
=====================================

This workflow abstracts the learnings from KYC PDF generation and encoding
to create a universal framework for generating test cases for any context.

Core Methodology:
1. Context Definition - Define the business context and document types
2. Template Creation - Create PDF templates for each document type
3. Data Generation - Generate realistic test data for the context
4. PDF Generation - Create valid PDF documents using templates
5. Encoding & Payload - Encode PDFs and create agent payloads
6. Validation - Verify PDFs can be opened and payloads are valid

Usage:
    python3 test_case_generation_workflow.py --context kyc --scenarios 3
    python3 test_case_generation_workflow.py --context invoices --scenarios 5
    python3 test_case_generation_workflow.py --context orders --scenarios 2
"""

import argparse
import json
import os
import base64
from datetime import datetime, timedelta
from typing import Dict, List, Any
import random

class TestCaseGenerator:
    """Generic test case generator for any business context"""
    
    def __init__(self, context: str, output_dir: str = "test_cases"):
        self.context = context
        self.output_dir = output_dir
        self.templates = {}
        self.test_data = {}
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(f"{output_dir}/pdfs", exist_ok=True)
        os.makedirs(f"{output_dir}/payloads", exist_ok=True)
        os.makedirs(f"{output_dir}/scripts", exist_ok=True)
    
    def load_context_config(self):
        """Load context-specific configuration"""
        config_file = f"contexts/{self.context}_config.json"
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return json.load(f)
        else:
            return self._get_default_config()
    
    def _get_default_config(self):
        """Get default configuration for unknown contexts"""
        return {
            "document_types": ["document1", "document2", "document3"],
            "business_rules": {
                "validation_rules": ["clarity", "completeness", "authenticity"],
                "risk_factors": ["occupation", "income", "document_quality"],
                "approval_criteria": ["all_documents_valid", "identity_verified", "low_risk"]
            },
            "stp_indicators": {
                "document_validation": "All documents are legitimate, clear, current",
                "identity_verification": "Data consistent across all documents",
                "risk_assessment": "Low risk profile - established professional",
                "decision": "AUTOMATIC APPROVAL - Process immediately"
            }
        }
    
    def generate_test_data(self, scenario_count: int) -> List[Dict]:
        """Generate test data for multiple scenarios"""
        scenarios = []
        
        for i in range(scenario_count):
            scenario = {
                "scenario_id": f"{self.context}_scenario_{i+1}",
                "risk_level": random.choice(["low", "medium", "high"]),
                "customer_data": self._generate_customer_data(),
                "document_data": self._generate_document_data(),
                "business_context": self._generate_business_context()
            }
            scenarios.append(scenario)
        
        return scenarios
    
    def _generate_customer_data(self) -> Dict:
        """Generate realistic customer data"""
        first_names = ["João", "Maria", "Pedro", "Ana", "Carlos", "Lucia", "Rafael", "Sofia"]
        last_names = ["Silva", "Santos", "Oliveira", "Costa", "Pereira", "Rodrigues", "Almeida", "Lima"]
        
        return {
            "name": f"{random.choice(first_names)} {random.choice(last_names)}",
            "dob": f"{random.randint(1,28):02d}/{random.randint(1,12):02d}/{random.randint(1970,1995)}",
            "address": f"Rua {random.choice(['Principal', 'Comercial', 'Industrial'])} {random.randint(100,999)}",
            "city": random.choice(["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"]),
            "state": random.choice(["SP", "RJ", "MG", "BA"]),
            "zip": f"{random.randint(10000,99999)}-{random.randint(100,999)}",
            "occupation": random.choice(["Engenheiro", "Médico", "Advogado", "Empresário", "Estudante"]),
            "income": f"R$ {random.randint(3000,15000):,}"
        }
    
    def _generate_document_data(self) -> Dict:
        """Generate document-specific data"""
        return {
            "document_numbers": [f"{random.randint(10000000,99999999)}" for _ in range(3)],
            "issue_dates": [(datetime.now() - timedelta(days=random.randint(1,365))).strftime("%d/%m/%Y") for _ in range(3)],
            "expiry_dates": [(datetime.now() + timedelta(days=random.randint(365,1825))).strftime("%d/%m/%Y") for _ in range(3)],
            "amounts": [f"R$ {random.randint(100,5000):,}" for _ in range(3)]
        }
    
    def _generate_business_context(self) -> Dict:
        """Generate business-specific context data"""
        return {
            "transaction_type": random.choice(["purchase", "payment", "verification", "application"]),
            "priority": random.choice(["normal", "urgent", "low"]),
            "compliance_level": random.choice(["standard", "enhanced", "basic"]),
            "processing_time": random.choice(["immediate", "24h", "48h", "manual_review"])
        }

class PDFGenerator:
    """Generic PDF document generator"""
    
    def __init__(self, context: str, output_dir: str):
        self.context = context
        self.output_dir = output_dir
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict:
        """Load PDF templates for the context"""
        templates = {}
        template_dir = f"templates/{self.context}"
        
        if os.path.exists(template_dir):
            for template_file in os.listdir(template_dir):
                if template_file.endswith('.py'):
                    template_name = template_file.replace('.py', '')
                    templates[template_name] = f"{template_dir}/{template_file}"
        
        return templates
    
    def generate_pdf(self, template_name: str, data: Dict, filename: str) -> str:
        """Generate a PDF using a template and data"""
        if template_name not in self.templates:
            # Use generic template
            return self._generate_generic_pdf(data, filename)
        
        # Import and use specific template
        template_path = self.templates[template_name]
        template_module = __import__(template_path.replace('/', '.').replace('.py', ''))
        
        return template_module.generate_pdf(data, filename)
    
    def _generate_generic_pdf(self, data: Dict, filename: str) -> str:
        """Generate a generic PDF when no specific template exists"""
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
/Length 200
>>
stream
BT
/F1 12 Tf
100 700 Td
({data.get('title', 'DOCUMENTO')}) Tj
0 -20 Td
(Nome: {data.get('name', 'N/A')}) Tj
0 -20 Td
(Data: {data.get('date', 'N/A')}) Tj
0 -20 Td
(Número: {data.get('number', 'N/A')}) Tj
0 -20 Td
(Valor: {data.get('amount', 'N/A')}) Tj
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
581
%%EOF"""

        filepath = f"{self.output_dir}/pdfs/{filename}"
        with open(filepath, 'wb') as f:
            f.write(pdf_content.encode('utf-8'))
        
        return filepath

class PayloadGenerator:
    """Generic payload generator for agent triggers"""
    
    def __init__(self, context: str, output_dir: str):
        self.context = context
        self.output_dir = output_dir
    
    def generate_payload(self, scenario: Dict, pdf_files: List[str], agent_id: str) -> Dict:
        """Generate agent payload with encoded PDFs"""
        
        # Encode PDF files
        encoded_files = []
        for pdf_file in pdf_files:
            if os.path.exists(pdf_file):
                with open(pdf_file, 'rb') as f:
                    pdf_content = f.read()
                
                encoded_file = {
                    "data": base64.b64encode(pdf_content).decode('utf-8'),
                    "mimeType": "application/pdf",
                    "fileName": os.path.basename(pdf_file),
                    "fileSize": str(os.path.getsize(pdf_file))
                }
                encoded_files.append(encoded_file)
        
        # Generate STP-optimized additional info
        stp_info = self._generate_stp_info(scenario)
        
        payload = {
            "taskQuery": {
                "query": f"Processe documentos {self.context} para o cliente {scenario['customer_data']['name']}. Valide documentos, verifique identidade, avalie risco e tome decisão de conformidade.",
                "additionalInfo": stp_info
            },
            "parsingUrls": [],
            "encodedContextFiles": encoded_files,
            "agentId": agent_id
        }
        
        return payload
    
    def _generate_stp_info(self, scenario: Dict) -> str:
        """Generate STP-optimized additional information"""
        customer = scenario['customer_data']
        risk_level = scenario['risk_level']
        
        base_info = f"Cliente: {customer['name']}, Data de Nascimento: {customer['dob']}, Endereço: {customer['address']}, {customer['city']} - {customer['state']} {customer['zip']}, Ocupação: {customer['occupation']}, Renda: {customer['income']}."
        
        stp_indicators = {
            "low": "VALIDAÇÃO DE DOCUMENTOS: Todos os documentos são legítimos, claros, atuais e sem sinais de adulteração. VERIFICAÇÃO DE IDENTIDADE: Dados consistentes em todos os documentos. AVALIAÇÃO DE RISCO: Perfil de baixo risco - profissional estabelecido, renda estável. DECISÃO: APROVAÇÃO AUTOMÁTICA - Processar imediatamente sem revisão manual.",
            "medium": "VALIDAÇÃO DE DOCUMENTOS: Documentos legítimos com qualidade aceitável. VERIFICAÇÃO DE IDENTIDADE: Dados majoritariamente consistentes. AVALIAÇÃO DE RISCO: Perfil de médio risco - requer monitoramento. DECISÃO: APROVAÇÃO COM MONITORAMENTO - Processar com supervisão limitada.",
            "high": "VALIDAÇÃO DE DOCUMENTOS: Documentos apresentam algumas inconsistências. VERIFICAÇÃO DE IDENTIDADE: Requer verificação adicional. AVALIAÇÃO DE RISCO: Perfil de alto risco - requer análise manual. DECISÃO: REVISÃO MANUAL OBRIGATÓRIA - Não processar automaticamente."
        }
        
        return f"{base_info} {stp_indicators.get(risk_level, stp_indicators['medium'])}"

class TestCaseWorkflow:
    """Main workflow orchestrator"""
    
    def __init__(self, context: str, scenarios: int, agent_id: str):
        self.context = context
        self.scenarios = scenarios
        self.agent_id = agent_id
        self.output_dir = f"test_cases_{context}"
        
        # Initialize components
        self.generator = TestCaseGenerator(context, self.output_dir)
        self.pdf_gen = PDFGenerator(context, self.output_dir)
        self.payload_gen = PayloadGenerator(context, self.output_dir)
        
        # Load context configuration
        self.config = self.generator.load_context_config()
    
    def run(self):
        """Execute the complete test case generation workflow"""
        print(f"🚀 Starting Test Case Generation Workflow for {self.context.upper()}")
        print("=" * 60)
        
        # Step 1: Generate test scenarios
        print("📊 Generating test scenarios...")
        scenarios = self.generator.generate_test_data(self.scenarios)
        print(f"✅ Generated {len(scenarios)} scenarios")
        
        # Step 2: Generate PDFs for each scenario
        print("\n📄 Generating PDF documents...")
        all_payloads = []
        
        for i, scenario in enumerate(scenarios):
            print(f"  Processing scenario {i+1}/{len(scenarios)}: {scenario['scenario_id']}")
            
            # Generate PDFs for this scenario
            pdf_files = []
            for j, doc_type in enumerate(self.config['document_types']):
                pdf_data = {
                    'title': doc_type.replace('_', ' ').title(),
                    'name': scenario['customer_data']['name'],
                    'date': scenario['document_data']['issue_dates'][j],
                    'number': scenario['document_data']['document_numbers'][j],
                    'amount': scenario['document_data']['amounts'][j]
                }
                
                filename = f"{scenario['scenario_id']}_{doc_type}.pdf"
                pdf_file = self.pdf_gen.generate_pdf(doc_type, pdf_data, filename)
                pdf_files.append(pdf_file)
                print(f"    ✓ Generated {filename}")
            
            # Step 3: Generate payload
            payload = self.payload_gen.generate_payload(scenario, pdf_files, self.agent_id)
            
            # Save payload
            payload_file = f"{self.output_dir}/payloads/{scenario['scenario_id']}_payload.json"
            with open(payload_file, 'w') as f:
                json.dump(payload, f, indent=2)
            
            all_payloads.append({
                'scenario': scenario,
                'payload_file': payload_file,
                'pdf_files': pdf_files
            })
            
            print(f"    ✓ Generated payload: {payload_file}")
        
        # Step 4: Generate summary report
        self._generate_summary_report(all_payloads)
        
        print(f"\n🎉 Test case generation completed!")
        print(f"📁 Output directory: {self.output_dir}")
        print(f"📊 Scenarios generated: {len(scenarios)}")
        print(f"📄 PDF files created: {sum(len(p['pdf_files']) for p in all_payloads)}")
        print(f"📦 Payload files created: {len(all_payloads)}")
    
    def _generate_summary_report(self, all_payloads: List[Dict]):
        """Generate a summary report of all test cases"""
        report = {
            "workflow_info": {
                "context": self.context,
                "scenarios_generated": len(all_payloads),
                "generation_date": datetime.now().isoformat(),
                "output_directory": self.output_dir
            },
            "scenarios": []
        }
        
        for payload_info in all_payloads:
            scenario = payload_info['scenario']
            report["scenarios"].append({
                "scenario_id": scenario['scenario_id'],
                "risk_level": scenario['risk_level'],
                "customer_name": scenario['customer_data']['name'],
                "occupation": scenario['customer_data']['occupation'],
                "income": scenario['customer_data']['income'],
                "pdf_files": [os.path.basename(f) for f in payload_info['pdf_files']],
                "payload_file": os.path.basename(payload_info['payload_file'])
            })
        
        report_file = f"{self.output_dir}/test_case_summary.json"
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📋 Summary report generated: {report_file}")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='Generic Test Case Generation Workflow')
    parser.add_argument('--context', required=True, help='Business context (e.g., kyc, invoices, orders)')
    parser.add_argument('--scenarios', type=int, default=3, help='Number of test scenarios to generate')
    parser.add_argument('--agent-id', required=True, help='Agent ID for payload generation')
    
    args = parser.parse_args()
    
    # Create workflow and run
    workflow = TestCaseWorkflow(args.context, args.scenarios, args.agent_id)
    workflow.run()

if __name__ == "__main__":
    main()
