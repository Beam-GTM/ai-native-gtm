#!/usr/bin/env python3
"""
KYC Driver's License PDF Template
"""

def generate_pdf(data, filename):
    """Generate a Brazilian driver's license PDF"""
    
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
/Length 400
>>
stream
BT
/F1 12 Tf
100 700 Td
(CARTEIRA NACIONAL DE HABILITAÇÃO) Tj
0 -20 Td
(CNH - Categoria B) Tj
0 -30 Td
(Nome: {data.get('name', 'N/A')}) Tj
0 -20 Td
(Data de Nascimento: {data.get('dob', 'N/A')}) Tj
0 -20 Td
(Endereço: {data.get('address', 'N/A')}) Tj
0 -20 Td
(Cidade: {data.get('city', 'N/A')} - {data.get('state', 'N/A')}) Tj
0 -20 Td
(CEP: {data.get('zip', 'N/A')}) Tj
0 -20 Td
(RG: {data.get('rg', 'N/A')}) Tj
0 -20 Td
(CPF: {data.get('cpf', 'N/A')}) Tj
0 -20 Td
(Registro: {data.get('license_number', 'N/A')}) Tj
0 -20 Td
(Validade: {data.get('expiry_date', 'N/A')}) Tj
0 -20 Td
(Altura: {data.get('height', 'N/A')}) Tj
0 -20 Td
(Peso: {data.get('weight', 'N/A')}) Tj
0 -20 Td
(Olhos: {data.get('eyes', 'N/A')}) Tj
0 -20 Td
(Cabelos: {data.get('hair', 'N/A')}) Tj
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
781
%%EOF"""

    with open(filename, 'wb') as f:
        f.write(pdf_content.encode('utf-8'))
    
    return filename
