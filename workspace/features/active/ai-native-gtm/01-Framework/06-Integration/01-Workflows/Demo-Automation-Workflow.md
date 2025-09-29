# Demo Automation Workflow
**Purpose**: Automated demo agent creation and deployment for high-value clients  
**Status**: Active
**Trigger**: When preparing for prospect demos or client presentations

## Workflow Overview
This workflow automates the creation of demo agents by generating step-by-step process flows, optimized prompts, and aligned test cases, then deploying via webhook integration.

## Pre-Workflow Checklist
- [ ] Identify demo type and client context
- [ ] Gather business objectives and requirements
- [ ] Prepare client-specific context and data
- [ ] Verify Beam Studio API credentials and endpoint availability
- [ ] Confirm webhook callback URL for async processing
- [ ] Schedule demo preparation time (30-60 minutes)

## Workflow Steps

### Phase 1: Context Gathering (10 minutes)
**Objective**: Collect all necessary information for demo creation

**Inputs Required:**
- Demo type (product demo, process demo, integration demo)
- Client context (industry, company size, use case)
- Business objectives (what should the demo achieve?)
- Technical requirements (APIs, integrations, specific features)
- Success criteria (what defines a successful demo?)
- Beam Studio API credentials (Bearer token, client ID)
- Webhook callback URL for processing completion

**Deliverables:**
- Context summary document
- Requirements checklist
- Success criteria definition

### Phase 2: Workflow Generation (15 minutes)
**Objective**: Create step-by-step text-based process flows

**Process:**
1. **Template Selection** - Choose appropriate demo template
2. **Customization** - Adapt template to client context
3. **Decision Points** - Define clear if/then logic branches
4. **Execution Steps** - Create detailed step-by-step instructions
5. **Validation** - Review workflow for completeness and clarity

**Deliverables:**
- Structured workflow document
- Decision tree visualization
- Execution checklist

### Phase 3: Prompt Engineering (15 minutes)
**Objective**: Generate intern-level clarity prompts optimized for straight-through processing

**Process:**
1. **Clarity Analysis** - Identify potential ambiguity points
2. **Prompt Optimization** - Rewrite for maximum clarity
3. **Decision Branch Mapping** - Ensure clear if/then logic
4. **Validation** - Test prompts for clarity and effectiveness
5. **Template Creation** - Save optimized prompts as templates

**Deliverables:**
- Optimized prompt library
- Clarity scoring report
- Decision branch documentation

### Phase 4: Test Case Generation (10 minutes)
**Objective**: Create test cases that exactly match prompt decision logic

**Process:**
1. **Path Analysis** - Map all possible execution paths
2. **Test Case Creation** - Generate scenarios for each path
3. **Validation** - Verify test cases cover all decision branches
4. **Success Criteria** - Define expected outcomes for each test
5. **Documentation** - Create test execution guide

**Deliverables:**
- Comprehensive test case library
- Test execution guide
- Validation checklist

### Phase 5: Beam Studio API Integration (10 minutes)
**Objective**: Package and deploy demo agent using Beam Studio API with correct payload format

**Process:**
1. **API Payload Creation** - Format data according to Beam Studio API specification
   - Customer information (name, DOB, address, occupation)
   - Document handling (base64 encoded files with proper MIME types)
   - Processing options (enhanced verification, risk assessment levels)
   - Callback configuration (webhook URL, timeout, retry settings)

2. **Authentication Setup** - Configure Beam Studio API credentials
   - Bearer token authentication
   - Client identifier for API requests
   - Request ID generation for tracking

3. **API Deployment** - Send package to Beam Studio API endpoint
   - Primary endpoint: `https://api.beamstudio.ai/v1/agents/kyc-processor`
   - Proper headers (Content-Type, Authorization, X-API-Version, X-Client-ID)
   - Error handling for 400, 401, 429, and 500 responses

4. **Response Processing** - Handle API responses and callbacks
   - Success response processing
   - Async processing with webhook callbacks
   - Error handling and retry logic

5. **Validation** - Verify successful deployment and functionality
   - API response validation
   - Test case execution
   - Webhook callback verification

**Deliverables:**
- Beam Studio API integrated demo agent
- API deployment confirmation with request ID
- Webhook callback verification
- Test execution results with API integration

## Post-Workflow Actions

### Immediate Actions (Next 24 hours)
- [ ] Test demo agent with sample scenarios
- [ ] Document any issues or improvements needed
- [ ] Share demo access with client team
- [ ] Schedule demo walkthrough session

### Follow-up Actions (Next Week)
- [ ] Monitor demo usage and performance
- [ ] Collect feedback from client team
- [ ] Iterate and improve based on feedback
- [ ] Document learnings for future demos

## Success Metrics
- **Generation Speed**: < 5 seconds for complete demo agent package
- **Prompt Clarity**: Measurable reduction in ambiguous decision points
- **Test Alignment**: 100% coverage of prompt decision branches
- **Deployment Reliability**: > 99% successful webhook deployments
- **Client Satisfaction**: 90%+ satisfaction with demo quality

## Integration Points
- **Beam Studio API**: Primary integration using `https://api.beamstudio.ai/v1/agents/kyc-processor`
- **API Documentation**: Complete reference at `https://api.beamstudio.ai/public-docs#/`
- **Webhook Callbacks**: Async processing completion notifications
- **Template System**: Local template library for workflows and prompts
- **CRM Integration**: Demo tracking and performance metrics
- **Client Communication**: Demo access and walkthrough coordination

## Tools and Resources
- **Beam Studio API**: Complete API integration with authentication and error handling
- **API Documentation**: Full reference at `https://api.beamstudio.ai/public-docs#/`
- **Template Library**: Pre-built demo templates for common scenarios
- **Prompt Optimization**: Clarity scoring and improvement tools
- **Test Case Generator**: Automated test case creation from workflows
- **Webhook Integration**: Async processing with callback support
- **Performance Monitoring**: Demo usage and effectiveness tracking
- **Code Examples**: JavaScript and Python implementation samples

## Quality Gates
- **Template System**: Workflow creation functional with clarity guidelines
- **Optimization Layer**: Prompt ambiguity detection and test case synchronization
- **Beam Studio API Integration**: Complete API integration with proper payload format
- **Authentication**: Bearer token and client ID configuration validated
- **Error Handling**: Comprehensive error handling for all API response codes
- **Integration Ready**: API deployment and live testing operational

## Risk Mitigation
- **Prompt Complexity**: Start with simple clarity rules, iterate based on results
- **Beam Studio API Integration**: Test thoroughly with example payloads and error scenarios
- **Authentication Issues**: Implement proper token validation and refresh logic
- **Rate Limiting**: Implement exponential backoff for 429 responses
- **Webhook Callbacks**: Ensure reliable callback handling and timeout management
- **Template Maintenance**: Design for easy updates and improvements

## Implementation Notes
- **Last Updated**: 2025-09-26
- **Created By**: System
- **Status**: Active
- **Beam Studio API Integration**: Complete with proper payload format
- **API Documentation**: `https://api.beamstudio.ai/public-docs#/`
- **Next Review**: 2025-10-26
