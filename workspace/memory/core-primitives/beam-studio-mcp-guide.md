# Beam Studio MCP Integration Guide

**Created**: 2025-09-29T18:30:00Z  
**Purpose**: Quick reference for proper Beam Studio MCP usage with document processing

## 🚨 **CRITICAL DISCOVERY**

**MCP startTask tool ≠ Full Beam Studio API**

- **MCP startTask**: Only accepts simple `query` string
- **Beam Studio API**: Requires complete JSON payload structure
- **Solution**: Use direct curl POST to webhook URL

## 📋 **Correct JSON Payload Structure**

```json
{
  "taskQuery": {
    "query": "Your task description here",
    "additionalInfo": "Detailed customer data and context"
  },
  "parsingUrls": [],
  "encodedContextFiles": [
    {
      "data": "base64_encoded_pdf_data",
      "mimeType": "application/pdf",
      "fileName": "document_name.pdf",
      "fileSize": "820"
    }
  ],
  "agentId": "your-agent-id"
}
```

## 🔧 **Implementation Commands**

### **1. Create JSON Payload File**
```bash
# Save payload as .json file
echo '{"taskQuery": {...}, "encodedContextFiles": [...], "agentId": "..."}' > payload.json
```

### **2. Send via Direct Webhook**
```bash
curl -X POST "https://api.beamstudio.ai/agent-tasks/{task-id}/webhook/{webhook-id}" \
  -H "Content-Type: application/json" \
  -d @payload.json
```

### **3. Monitor with MCP**
```bash
# Use MCP listenTask tool with returned task ID
mcp_beamstudio_listenTask --taskId "returned-task-id"
```

## 📊 **Key Fields Explained**

- **taskQuery.query**: Main task description
- **taskQuery.additionalInfo**: Detailed context and customer data
- **encodedContextFiles**: Array of base64 encoded documents
- **encodedContextFiles.data**: Base64 encoded PDF content
- **encodedContextFiles.mimeType**: Document type (application/pdf)
- **encodedContextFiles.fileName**: Document name
- **encodedContextFiles.fileSize**: File size in bytes
- **agentId**: Target agent identifier
- **parsingUrls**: Usually empty array []

## 🎯 **Use Cases**

- **KYC Verification**: Identity documents, address proof, risk assessment
- **Debt Collection**: Customer data, payment history, contact strategies
- **Document Processing**: OCR, data extraction, compliance checking
- **Multi-Market**: Brazil (LGPD), Mexico (LPDP), Colombia (Ley 1581)

## ⚠️ **Common Mistakes**

1. **Using MCP startTask for complex workflows** ❌
2. **Missing encodedContextFiles structure** ❌
3. **Incorrect mimeType or fileSize** ❌
4. **Not using direct webhook API** ❌

## ✅ **Best Practices**

1. **Always use direct webhook for document processing** ✅
2. **Include proper base64 encoding with metadata** ✅
3. **Use MCP listenTask for monitoring** ✅
4. **Test with simple queries first** ✅
5. **Validate JSON structure before sending** ✅

---
*This guide ensures proper Beam Studio MCP integration for complex document processing workflows.*
