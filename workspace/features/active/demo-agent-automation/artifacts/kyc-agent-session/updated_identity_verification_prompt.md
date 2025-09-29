# Updated Identity Verification Prompt

## **KYC Identity Verification - Step 2 (Updated)**

You are verifying a customer's identity using validated documents and external sources.

**CUSTOMER INFORMATION:**
- Full Name: {customer_data.customer_full_name}
- Date of Birth: {customer_data.date_of_birth}
- Address: {customer_data.customer_address}
- Government ID Number: {customer_data.id_number}

**DOCUMENT DATA (for verification):**
- Driver's License Name: {documents.government_id_document.document_data.name}
- Driver's License DOB: {documents.government_id_document.document_data.dob}
- Driver's License Address: {documents.government_id_document.document_data.address}
- Driver's License Number: {documents.government_id_document.document_data.license_number}

**VERIFICATION SOURCES:**
1. **Government Database**: Check official records
2. **Credit Bureau**: Verify identity history
3. **Watchlist Screening**: Check against sanctions/PEP lists

**VERIFICATION RULES:**
1. **Name Match**: Does the name match across all sources?
2. **Address Verification**: Does the address match government records?
3. **ID Validation**: Is the government ID valid and not reported stolen?
4. **Watchlist Check**: Is the customer on any sanctions or PEP lists?
5. **Document Data Consistency**: Do the extracted document data match the customer information?

**DECISION LOGIC:**
- IF all verifications PASS AND no watchlist matches → PROCEED to risk assessment
- IF any verification FAILS → FLAG for manual review with specific failure reason
- IF watchlist MATCH found → IMMEDIATE rejection with compliance reason
- IF document data doesn't match customer info → FLAG for manual review

**OUTPUT FORMAT:**
```json
{
  "verification_status": "verified|flagged|rejected",
  "verification_results": {
    "government_db": "pass|fail|error",
    "credit_bureau": "pass|fail|error",
    "watchlist_screening": "clear|match|error",
    "document_consistency": "pass|fail|error"
  },
  "match_details": "specific_watchlist_match_if_any",
  "consistency_issues": ["specific_inconsistency_if_any"],
  "next_action": "proceed|manual_review|reject"
}
```

## **Key Improvements:**

1. **Proper Variable Mapping**: Uses correct nested paths like `{customer_data.customer_full_name}` and `{documents.government_id_document.document_data.name}`

2. **Document Data Integration**: Includes extracted document data for verification

3. **Enhanced Consistency Checking**: Adds document data consistency verification

4. **Better Error Handling**: Includes specific error states and consistency issues

5. **Robust Output Format**: More detailed response structure with specific failure reasons

## **Usage Instructions:**

Replace the existing `identity_verification_prompt` in your KYC workflow with this updated version. This should resolve the second node failure when documents are present.
