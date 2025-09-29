#!/usr/bin/env python3
"""
KYC Utility Bill PDF Template
"""

def generate_pdf(data, filename):
    """Generate a Brazilian utility bill PDF"""
    
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
/Length 500
>>
stream
BT
/F1 12 Tf
100 700 Td
({data.get('company', 'ENEL DISTRIBUIÇÃO SÃO PAULO')}) Tj
0 -20 Td
(Conta de Energia Elétrica) Tj
0 -30 Td
(Número da Instalação: {data.get('account_number', 'N/A')}) Tj
0 -20 Td
(Cliente: {data.get('customer_name', 'N/A')}) Tj
0 -20 Td
(CPF/CNPJ: {data.get('cpf', 'N/A')}) Tj
0 -20 Td
(Endereço: {data.get('address', 'N/A')}) Tj
0 -20 Td
(Bairro: {data.get('neighborhood', 'Centro')}) Tj
0 -20 Td
(Cidade: {data.get('city', 'N/A')} - {data.get('state', 'N/A')}) Tj
0 -20 Td
(CEP: {data.get('zip', 'N/A')}) Tj
0 -30 Td
(Período de Referência: {data.get('billing_period', 'N/A')}) Tj
0 -20 Td
(Vencimento: {data.get('due_date', 'N/A')}) Tj
0 -20 Td
(Valor a Pagar: {data.get('amount', 'N/A')}) Tj
0 -30 Td
(Detalhamento do Consumo:) Tj
0 -20 Td
(Consumo: {data.get('consumption', 'N/A')}) Tj
0 -20 Td
(Tarifa: {data.get('tariff', 'N/A')}) Tj
0 -20 Td
(Energia: {data.get('energy_cost', 'N/A')}) Tj
0 -20 Td
(ICMS: {data.get('tax', 'N/A')}) Tj
0 -20 Td
(Total: {data.get('total', 'N/A')}) Tj
0 -30 Td
(Formas de Pagamento: PIX, Boleto, Débito) Tj
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
881
%%EOF"""

    with open(filename, 'wb') as f:
        f.write(pdf_content.encode('utf-8'))
    
    return filename
