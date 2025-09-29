# Updated Risk Assessment Prompt

## **KYC Risk Assessment - Step 3 (Updated)**

You are assessing the risk level of the customer based on verification results and customer profile.

**INPUT DATA:**
- Verification Status: {verification_status}
- Customer Profile: {customer_data}
- Document Quality: {document_quality}
- Watchlist Status: {watchlist_status}

**REQUIRED OUTPUT VARIABLES:**
The system needs these specific variables extracted:

1. **Customer Occupation**: Extract from customer data or infer from profile
2. **Document Quality Score**: Assess based on document validation results

**RISK FACTORS:**

**1. OCCUPATION RISK ASSESSMENT:**
- **High Risk Occupations**: Politically exposed persons, cash-intensive businesses, high-value asset dealers
- **Medium Risk Occupations**: Self-employed, new business owners, international workers
- **Low Risk Occupations**: Salaried employees, established professionals, government workers

**2. DOCUMENT QUALITY RISK:**
- **Score 90-100**: Excellent quality, clear scans, all information legible
- **Score 70-89**: Good quality, minor issues, mostly legible
- **Score 50-69**: Fair quality, some blurriness or missing information
- **Score 0-49**: Poor quality, significant issues, hard to read

**3. OTHER RISK INDICATORS:**
- PEP (Politically Exposed Person) status
- High-risk country of residence
- Unusual transaction patterns
- Sanctions list matches
- Age of documents
- Document authenticity

**RISK SCORING:**
- 0-30: Low Risk
- 31-70: Medium Risk
- 71-100: High Risk

**OUTPUT FORMAT:**
```json
{
  "customer_occupation": "extracted_or_inferred_occupation",
  "document_quality_score": 0-100,
  "risk_score": 0-100,
  "risk_level": "low|medium|high",
  "risk_factors": ["occupation_risk", "document_quality_risk", "other_factors"],
  "occupation_risk_level": "low|medium|high",
  "document_quality_risk_level": "low|medium|high",
  "mitigation_required": true|false,
  "next_action": "proceed|manual_review|reject"
}
```

## **Key Improvements:**

1. **Explicit Variable Extraction**: Clearly extracts `customer_occupation` and `document_quality_score`
2. **Occupation Risk Assessment**: Specific guidance for evaluating occupation risk
3. **Document Quality Scoring**: Clear scoring system for document quality
4. **Structured Output**: Ensures all required variables are provided
5. **Risk Level Breakdown**: Separate risk levels for different factors

## **Usage Instructions:**

Replace the existing `risk_assessment_prompt` in your KYC workflow with this updated version. This should resolve the "AI was not able to infer these variables" issue by explicitly extracting and providing the required occupation and document quality variables.
