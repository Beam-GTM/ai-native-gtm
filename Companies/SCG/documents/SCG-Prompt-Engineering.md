# SCG Contractor Payment Verification - Prompt Engineering
**Generated**: 2025-09-19T11:05:00Z  
**Framework**: Demo Agent Automation - Prompt Engineer Component  
**Clarity Level**: Intern-Level (Explicit enough for minimal context)

---

## 🎯 Prompt Engineering Principles

### Clarity Standards
- **Intern-Level Clarity**: Explicit enough for someone with minimal construction/accounting context
- **Decision Branch Logic**: Clear if/then statements with unambiguous paths
- **Construction Domain**: Thai construction terminology and processes
- **Error Handling**: Explicit error conditions and escalation paths

---

## 📋 Core Processing Prompts

### 1. Thai OCR Processing & Translation Prompt

```
TASK: Extract and translate Thai construction completion certificate to English

INPUT: Thai construction document (PDF/image) + supporting materials

VALIDATION STEPS:
1. IF document format is PDF or image → PROCEED to OCR processing
2. IF document format is unsupported → RETURN error "Unsupported format. Please submit PDF or image file."
3. IF document is empty or corrupted → RETURN error "Document appears corrupted. Please resubmit."

OCR PROCESSING:
1. EXTRACT all visible Thai text from document
2. IDENTIFY document type (completion certificate, material receipt, inspection report)
3. STRUCTURE extracted text into logical sections

OUTPUT VARIABLES TO EXTRACT:
- contractor_name: "English contractor company name"
- project_id: "SCG project identifier"
- work_type: "Type of construction work performed"
- completion_date: "Work completion date"
- material_cost: "Total material costs in THB"
- labor_cost: "Total labor costs in THB"
- other_costs: "Other service costs in THB"
- total_amount: "Total project amount in THB"
- vat_amount: "VAT amount in THB"
- final_amount: "Final amount after VAT in THB"
- quality_status: "Quality compliance status"
- inspection_date: "Quality inspection date"
- bank_account: "Contractor bank account number"
- bank_name: "Contractor bank name"
- work_description: "Detailed work description in English"
- material_list: "List of materials used in English"
- quality_certificates: "Quality certificate status"
- inspector_name: "Quality inspector name"
- inspector_license: "Inspector license number"

IF text extraction fails or accuracy < 80% → ESCALATE to manual OCR review
IF text extraction succeeds → PROCEED to contract verification

OUTPUT: Structured English data with all extracted variables + extraction confidence score
```

### 2. Contract Compliance Verification Prompt

```
TASK: Verify work completion against contract specifications using extracted variables

INPUT: Extracted variables from Thai OCR Processing + Contract details from SCG system

EXTRACTED VARIABLES USED:
- project_id: "SCG project identifier"
- work_type: "Type of construction work performed"
- work_description: "Detailed work description in English"
- material_list: "List of materials used in English"
- completion_date: "Work completion date"
- total_amount: "Total project amount in THB"

VERIFICATION PROCESS:
1. MATCH project_id to contract database
2. COMPARE work_type and work_description to contract specifications
3. VERIFY material_list matches contract requirements
4. CHECK completion_date against contract schedule
5. VALIDATE total_amount against contract budget

CONTRACT COMPLIANCE CHECKS:
- IF work scope matches contract → PROCEED to quality verification
- IF work scope exceeds contract → FLAG for contract amendment review
- IF work scope is incomplete → FLAG for completion verification
- IF materials don't match specifications → FLAG for material compliance review

TIMELINE VERIFICATION:
- IF completion_date is within contract timeline → PROCEED
- IF completion_date exceeds contract timeline → FLAG for delay analysis
- IF completion_date is significantly early → FLAG for quality verification

COST VERIFICATION:
- IF total_amount is within contract budget → PROCEED
- IF total_amount exceeds contract budget → FLAG for budget review
- IF total_amount is significantly under budget → FLAG for work verification

OUTPUT: Contract compliance status + specific compliance issues (if any)
```

### 3. Quality Standards Verification Prompt

```
TASK: Verify work meets SCG quality standards using extracted variables

INPUT: Extracted variables from Thai OCR Processing + SCG quality standards

EXTRACTED VARIABLES USED:
- quality_status: "Quality compliance status"
- quality_certificates: "Quality certificate status"
- inspection_date: "Quality inspection date"
- inspector_name: "Quality inspector name"
- inspector_license: "Inspector license number"
- material_list: "List of materials used in English"

QUALITY VERIFICATION PROCESS:
1. CHECK quality_certificates for required certifications
2. VERIFY quality_status indicates passed inspection
3. CONFIRM inspection_date is recent and valid
4. VALIDATE inspector_name and inspector_license credentials
5. CHECK material_list for quality compliance

QUALITY STANDARDS CHECKLIST:
- IF quality_certificates present and valid → PROCEED
- IF quality_certificates missing → FLAG for quality review
- IF quality_status indicates "ผ่าน" (passed) → PROCEED
- IF quality_status indicates "ไม่ผ่าน" (failed) → FLAG for re-inspection
- IF inspection_date is within acceptable timeframe → PROCEED
- IF inspection_date is too old → FLAG for recent inspection

INSPECTOR CREDENTIALS VERIFICATION:
- IF inspector_name and inspector_license are valid → PROCEED
- IF inspector credentials are invalid → FLAG for credential review
- IF inspector is not licensed → FLAG for licensed inspector

MATERIAL QUALITY VERIFICATION:
- IF material_list meets SCG specifications → PROCEED
- IF materials are substandard → FLAG for material replacement
- IF material documentation incomplete → FLAG for documentation review

OUTPUT: Quality compliance status + quality issues (if any)
```

### 4. Project Manager Approval Routing Prompt

```
TASK: Route approval request to appropriate project manager using extracted variables

INPUT: Extracted variables from Thai OCR Processing + SCG project management system

EXTRACTED VARIABLES USED:
- project_id: "SCG project identifier"
- final_amount: "Final amount after VAT in THB"
- contractor_name: "English contractor company name"
- work_type: "Type of construction work performed"
- completion_date: "Work completion date"
- quality_status: "Quality compliance status"

ROUTING LOGIC:
1. EXTRACT project_id from extracted variables
2. LOOKUP project manager assignment in SCG system using project_id
3. DETERMINE approval level based on final_amount
4. ROUTE to appropriate approver

APPROVAL LEVELS:
- IF final_amount < 350,000 THB (~$10,000) → Route to Project Supervisor
- IF final_amount 350,000 - 1,750,000 THB ($10,000 - $50,000) → Route to Project Manager
- IF final_amount > 1,750,000 THB ($50,000) → Route to Senior Project Manager
- IF final_amount > 3,500,000 THB ($100,000) → Route to Regional Manager

ROUTING CONDITIONS:
- IF all verifications passed → Route for approval
- IF any verification failed → Route for review with failure details
- IF quality_status indicates issues → Route to Quality Manager first
- IF contract compliance issues → Route to Contract Manager first

OUTPUT: Approval routing decision + approver assignment + routing reason
```

### 5. Payment Processing Prompt

```
TASK: Process contractor payment after approval using extracted variables

INPUT: Approved payment request + extracted variables from Thai OCR Processing

EXTRACTED VARIABLES USED:
- final_amount: "Final amount after VAT in THB"
- contractor_name: "English contractor company name"
- bank_account: "Contractor bank account number"
- bank_name: "Contractor bank name"
- project_id: "SCG project identifier"
- work_type: "Type of construction work performed"

PAYMENT CALCULATION:
1. USE final_amount as gross payment amount
2. CALCULATE tax withholding (if applicable)
3. CALCULATE net payment amount
4. VERIFY bank_account and bank_name details

PAYMENT PROCESSING:
- IF all calculations correct → INITIATE bank transfer
- IF calculation errors → FLAG for manual review
- IF bank details invalid → FLAG for contractor contact
- IF payment amount exceeds approval → FLAG for re-approval

BANK TRANSFER INITIATION:
- IF bank transfer successful → UPDATE payment status to "Paid"
- IF bank transfer fails → RETRY up to 3 times
- IF all retries fail → ESCALATE to finance team

PAYMENT TRACKING:
- ASSOCIATE payment with project_id
- RECORD work_type for audit purposes
- LINK payment to contractor_name for reporting

OUTPUT: Payment processing status + transaction ID + payment confirmation
```

### 6. Audit Trail Generation Prompt

```
TASK: Create comprehensive audit trail for compliance using all extracted variables

INPUT: All extracted variables + complete processing data + all decision points

EXTRACTED VARIABLES FOR AUDIT:
- All 19 extracted variables from Thai OCR Processing
- Contract compliance assessment
- Quality compliance status
- Approval decision and comments
- Payment confirmation and tracking

AUDIT TRAIL COMPONENTS:
1. DOCUMENT PROCESSING HISTORY
   - Document received timestamp
   - OCR processing results with confidence scores
   - All extracted variables with values
   - Processing time and errors

2. VERIFICATION RESULTS
   - Contract compliance status using extracted variables
   - Quality standards verification using extracted variables
   - Compliance issues identified
   - Resolution actions taken

3. APPROVAL WORKFLOW
   - Approval routing decision based on extracted variables
   - Approver assignment using project_id and final_amount
   - Approval/rejection decision
   - Approval comments and conditions

4. PAYMENT PROCESSING
   - Payment calculation details using extracted variables
   - Bank transfer initiation using bank_account and bank_name
   - Payment confirmation
   - Transaction tracking information

5. EXTRACTED DATA AUDIT
   - Complete record of all 19 extracted variables
   - Source document reference
   - Extraction confidence scores
   - Translation accuracy metrics

OUTPUT: Complete audit trail document + compliance report + extracted data log
```

---

## 🔄 Error Handling Prompts

### Document Processing Error Prompt

```
TASK: Handle document processing errors

ERROR CONDITIONS:
- IF OCR accuracy < 80% → ESCALATE to manual OCR review
- IF translation confidence < 90% → ESCALATE to manual translation
- IF document format unsupported → RETURN error to contractor
- IF document corrupted → REQUEST resubmission

ERROR RESPONSES:
- OCR Error: "Document text extraction failed. Please resubmit with clearer image."
- Translation Error: "Document translation requires manual review. Processing will continue with human oversight."
- Format Error: "Unsupported document format. Please submit PDF or image file."
- Corruption Error: "Document appears corrupted. Please resubmit original document."

OUTPUT: Error status + error message + next action required
```

### Contract Compliance Error Prompt

```
TASK: Handle contract compliance failures

COMPLIANCE FAILURES:
- IF work scope mismatch → FLAG for contract amendment
- IF material specification violation → FLAG for material review
- IF timeline violation → FLAG for delay analysis
- IF quality standard failure → FLAG for quality review

ESCALATION PATHS:
- Contract Issues → Route to Contract Manager
- Quality Issues → Route to Quality Manager
- Timeline Issues → Route to Project Manager
- Material Issues → Route to Procurement Manager

OUTPUT: Compliance failure details + escalation assignment + required actions
```

---

## 📊 Success Metrics Prompts

### Performance Tracking Prompt

```
TASK: Track and report processing performance

METRICS TO TRACK:
1. DOCUMENT PROCESSING TIME
   - Start: Document ingestion timestamp
   - End: Payment processing completion timestamp
   - Target: < 24 hours total processing time

2. OCR ACCURACY
   - Measure: Text extraction accuracy percentage
   - Target: > 95% accuracy on Thai construction documents

3. CONTRACT COMPLIANCE RATE
   - Measure: Percentage of first-pass compliance
   - Target: > 90% compliance rate

4. PAYMENT PROCESSING SPEED
   - Measure: Time from approval to payment
   - Target: < 24 hours payment processing

5. ERROR RATE
   - Measure: Percentage requiring manual intervention
   - Target: < 2% error rate

OUTPUT: Performance metrics report + improvement recommendations
```

---

**Prompt Engineering Complete**: All prompts designed with intern-level clarity, explicit decision branches, and construction domain expertise.
