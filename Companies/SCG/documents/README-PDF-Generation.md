# Thai Construction Document - PDF Generation Instructions

## 📄 Sample Document Created

**File**: `Sample-Thai-Construction-Document.html`  
**Purpose**: Sample Thai construction completion certificate for SCG demo agent testing  
**Format**: Professional HTML document with Thai text and construction terminology  

## 🎯 Document Features

### Thai Construction Content
- **Contractor**: สมชาย ไฟฟ้า (Somchai Electric Co., Ltd.)
- **Project ID**: SCG-2024-ELEC-001
- **Work Type**: งานไฟฟ้า (Electrical Work)
- **Completion Date**: 15 กันยายน 2567
- **Total Amount**: 144,450 บาท
- **Quality Status**: ผ่าน (Passed)

### Key Elements for Demo Agent Testing
1. **Thai Text Extraction**: All text in Thai script for OCR testing
2. **Construction Terminology**: Industry-specific vocabulary
3. **Financial Data**: Cost breakdown and payment information
4. **Quality Certificates**: Thai Industrial Standards compliance
5. **Bank Details**: Payment processing information

## 🔧 PDF Generation Methods

### Method 1: Browser Print to PDF (Recommended)
1. Open `Sample-Thai-Construction-Document.html` in any web browser
2. Press `Ctrl+P` (Windows) or `Cmd+P` (Mac)
3. Select "Save as PDF" as destination
4. Choose A4 paper size
5. Enable "Background graphics" for proper styling
6. Save as `Sample-Thai-Construction-Document.pdf`

### Method 2: Python Script (Advanced)
```bash
# Install weasyprint
pip install weasyprint

# Run the generation script
python generate-pdf.py
```

### Method 3: Online HTML to PDF Converter
1. Upload the HTML file to any online HTML-to-PDF converter
2. Ensure Thai font support is enabled
3. Download the generated PDF

## 📊 Document Processing Test Points

### OCR Extraction Targets
- **Contractor Name**: สมชาย ไฟฟ้า (Somchai Electric)
- **Project ID**: SCG-2024-ELEC-001
- **Work Type**: งานไฟฟ้า (Electrical Work)
- **Completion Date**: 15 กันยายน 2567
- **Total Amount**: 144,450 บาท
- **Quality Status**: ผ่าน (Passed)

### Contract Verification Points
- **Work Scope**: Electrical system installation and renovation
- **Material Specifications**: PVC cables, LED lights, control panels
- **Timeline**: August 1 - September 15, 2024 (45 days)
- **Quality Standards**: Thai Industrial Standards compliance

### Quality Verification Points
- **Quality Certificates**: Present and valid
- **Inspection Report**: Passed all tests
- **Safety Compliance**: Documented
- **Material Quality**: Standard specifications met

### Payment Processing Points
- **Payment Amount**: 144,450 THB
- **Bank Details**: Kasikorn Bank account provided
- **Tax Calculation**: 7% VAT included
- **Payment Terms**: Standard 30-day terms

## 🎯 Demo Agent Testing Scenarios

### Scenario 1: Successful Processing
- **Expected**: Full document processing with approval
- **Processing Time**: < 2 hours
- **Outcome**: Payment approved and processed

### Scenario 2: OCR Accuracy Challenge
- **Expected**: High accuracy Thai text extraction
- **Target**: > 95% OCR accuracy
- **Fallback**: Manual review if accuracy < 80%

### Scenario 3: Contract Compliance
- **Expected**: Work scope matches contract requirements
- **Verification**: Electrical work within specifications
- **Outcome**: Compliance verified, proceed to payment

### Scenario 4: Quality Standards
- **Expected**: All quality certificates present and valid
- **Verification**: Thai Industrial Standards compliance
- **Outcome**: Quality standards met, approval granted

## 📋 File Structure

```
Companies/SCG/documents/
├── Sample-Thai-Construction-Document.html    # Main HTML document
├── Sample-Thai-Construction-Document.md      # Markdown version
├── generate-pdf.py                          # PDF generation script
├── README-PDF-Generation.md                 # This file
└── Sample-Thai-Construction-Document.pdf    # Generated PDF (after conversion)
```

## 🌐 Browser Compatibility

### Recommended Browsers
- **Chrome**: Full Thai font support
- **Firefox**: Full Thai font support
- **Safari**: Full Thai font support
- **Edge**: Full Thai font support

### Font Requirements
- **Thai Fonts**: Sarabun, TH Sarabun New, or similar
- **Fallback**: Arial, sans-serif
- **Monospace**: Courier New for project IDs

## 🎨 Document Styling

### Color Scheme
- **Primary Blue**: #1e40af (SCG branding)
- **Success Green**: #dcfce7 (Quality certificates)
- **Warning Yellow**: #fef3c7 (Cost breakdown)
- **Neutral Gray**: #f8fafc (Work details)

### Layout Features
- **A4 Page Size**: Optimized for printing
- **Professional Header**: SCG branding and document title
- **Sectioned Layout**: Clear information organization
- **Highlighted Key Data**: Important information emphasized
- **Signature Section**: Professional completion certification

---

**This document serves as a realistic test case for the SCG Contractor Payment Verification Demo Agent, providing authentic Thai construction terminology and business processes for accurate testing and validation.**
