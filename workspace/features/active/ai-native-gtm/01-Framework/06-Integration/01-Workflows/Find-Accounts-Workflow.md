# Find Accounts Workflow
**Purpose**: Automated account discovery and qualification using Apollo API for ICP prospecting  
**Status**: Active  
**Trigger**: When starting new prospecting campaigns or expanding target lists  
**API Integration**: [Apollo Organization Search API](https://docs.apollo.io/reference/organization-search)

## Workflow Overview
This workflow automates the discovery of target companies using Apollo's Organization Search API, applies ICP-specific qualification criteria, and generates actionable prospect lists for GTM campaigns.

## Pre-Workflow Checklist
- [ ] Apollo API credentials configured and tested
- [ ] ICP criteria defined and validated
- [ ] Target list parameters set (geography, size, industry)
- [ ] Qualification scoring framework established
- [ ] Output format and destination confirmed
- [ ] Schedule search execution time (15-30 minutes)

## Workflow Steps

### Phase 1: Search Configuration (5 minutes)
**Objective**: Configure Apollo API search parameters based on ICP criteria

**Process:**
1. **ICP Mapping** - Map ICP-C RPO criteria to Apollo search filters
2. **Search Parameters** - Set company size, industry, geography, and keywords
3. **API Configuration** - Configure authentication and rate limits
4. **Validation** - Test search parameters with sample query

**Deliverables:**
- Configured Apollo API search parameters
- ICP-specific filter mapping
- Search validation results

### Phase 2: Account Discovery (10-15 minutes)
**Objective**: Execute Apollo searches and discover target companies

**Process:**
1. **Primary Search** - Execute main search with core ICP criteria
2. **Secondary Searches** - Run additional searches with variations
3. **Data Collection** - Gather company data and contact information
4. **Deduplication** - Remove duplicate companies across searches
5. **Batch Processing** - Handle large result sets in batches (100 records per page)

**Deliverables:**
- Raw company data from Apollo API
- Deduplicated company list
- Search performance metrics

### Phase 3: ICP Qualification (5-10 minutes)
**Objective**: Apply ICP-specific qualification criteria to discovered companies

**Process:**
1. **Criteria Application** - Apply ICP-C RPO qualification criteria
2. **Scoring Algorithm** - Score companies based on fit probability
3. **Tier Classification** - Classify companies into priority tiers
4. **Data Enrichment** - Add additional company data and insights
5. **Quality Validation** - Verify company data accuracy and completeness

**Deliverables:**
- Qualified company list with scores
- Tier classification (Tier 1, 2, 3)
- Enriched company profiles

### Phase 4: List Generation (5 minutes)
**Objective**: Generate actionable prospect lists for GTM campaigns

**Process:**
1. **List Segmentation** - Create lists by tier and criteria
2. **Contact Identification** - Identify key decision makers
3. **Campaign Assignment** - Assign companies to appropriate campaigns
4. **Export Preparation** - Format data for CRM and campaign tools
5. **Documentation** - Create search summary and insights

**Deliverables:**
- Segmented prospect lists
- Contact information and decision makers
- Campaign assignment recommendations
- Search summary report

## Apollo API Integration

### Search Parameters for ICP-C RPO
**Company Size**: 50-5000 employees  
**Industry Keywords**: "Recruitment Process Outsourcing", "RPO", "Staffing", "Talent Acquisition"  
**Geographic Focus**: North America, Europe, Asia-Pacific  
**Revenue Range**: $5M-$500M annually  
**Technology Keywords**: "ATS", "CRM", "recruitment technology", "hiring automation"

### API Configuration
```json
{
  "api_endpoint": "https://api.apollo.io/api/v1/mixed_companies/search",
  "authentication": "Bearer [API_KEY]",
  "rate_limit": "100 requests per minute",
  "pagination": "100 records per page, max 500 pages",
  "filters": {
    "company_size": "50-5000",
    "industry": ["Recruitment Process Outsourcing", "Staffing"],
    "keywords": ["RPO", "recruitment", "talent acquisition"],
    "location": ["United States", "Canada", "United Kingdom", "Germany"],
    "revenue": "5000000-500000000"
  }
}
```

### Search Variations
**Search 1: Core RPO Companies**
- Industry: "Recruitment Process Outsourcing"
- Keywords: "RPO", "recruitment outsourcing"
- Size: 50-5000 employees

**Search 2: Staffing Companies**
- Industry: "Staffing", "Talent Acquisition"
- Keywords: "staffing", "recruitment", "hiring"
- Size: 50-5000 employees

**Search 3: Technology-Forward Recruiters**
- Keywords: "ATS", "recruitment technology", "hiring automation"
- Size: 50-5000 employees
- Technology focus

## ICP Qualification Criteria

### Tier 1: High-Priority Targets
**Criteria**: Perfect fit, high probability, immediate opportunity
- **Company Type**: Pure RPO companies
- **Size**: 100-2000 employees
- **Revenue**: $10M-$200M
- **Technology**: ATS/CRM integration ready
- **Geography**: North America, Europe
- **Score**: 85-100

### Tier 2: Medium-Priority Targets
**Criteria**: Good fit, medium probability, near-term opportunity
- **Company Type**: RPO + staffing mix
- **Size**: 50-1000 employees
- **Revenue**: $5M-$100M
- **Technology**: Basic tech stack
- **Geography**: North America, Asia-Pacific
- **Score**: 70-84

### Tier 3: Long-Term Targets
**Criteria**: Potential fit, lower probability, future opportunity
- **Company Type**: Staffing companies with RPO potential
- **Size**: 50-500 employees
- **Revenue**: $5M-$50M
- **Technology**: Limited tech integration
- **Geography**: Any
- **Score**: 50-69

## Qualification Scoring Algorithm

### Company Fit Score (0-100)
**Industry Alignment (30 points)**:
- Pure RPO: 30 points
- RPO + Staffing: 25 points
- Staffing with RPO potential: 20 points
- Other: 0 points

**Size Fit (20 points)**:
- 100-2000 employees: 20 points
- 50-100 employees: 15 points
- 200-1000 employees: 18 points
- 1000-5000 employees: 12 points
- Other: 0 points

**Technology Readiness (20 points)**:
- ATS + CRM integration: 20 points
- ATS only: 15 points
- Basic tech stack: 10 points
- Limited tech: 5 points

**Geographic Fit (15 points)**:
- North America: 15 points
- Europe: 12 points
- Asia-Pacific: 10 points
- Other: 5 points

**Revenue Fit (15 points)**:
- $10M-$200M: 15 points
- $5M-$100M: 12 points
- $25M-$100M: 13 points
- $100M-$500M: 10 points
- Other: 5 points

## Output Formats

### CRM Integration
**HubSpot Format**:
- Company name, website, industry
- Contact information and decision makers
- ICP score and tier classification
- Campaign assignment and next steps

**Salesforce Format**:
- Account records with ICP data
- Contact records with role information
- Lead scoring and qualification status
- Campaign membership and assignment

### Campaign Lists
**Email Campaign List**:
- Tier 1 companies for personalized outreach
- Contact information and personalization data
- Campaign-specific messaging recommendations

**LinkedIn Campaign List**:
- Tier 2 companies for social outreach
- LinkedIn profile information
- Connection and messaging recommendations

**Content Campaign List**:
- Tier 3 companies for nurture campaigns
- Content preferences and engagement history
- Nurture sequence recommendations

## Performance Tracking

### Search Metrics
**Discovery Rate**: Number of companies found per search
**Qualification Rate**: Percentage of companies that meet ICP criteria
**Tier Distribution**: Distribution across Tier 1, 2, 3
**Data Quality**: Completeness and accuracy of company data

### Campaign Performance
**List Utilization**: Percentage of companies used in campaigns
**Response Rate**: Response rate by tier and campaign type
**Conversion Rate**: Lead-to-opportunity conversion by tier
**ROI**: Return on investment for search and campaign activities

## Integration Points

### Framework Integration
**01-Framework/01-Prospecting**: Uses ICP definitions and targeting criteria
**01-Framework/02-Lead-Generation**: Feeds qualified leads to lead generation
**01-Framework/03-Discovery**: Provides company data for discovery calls
**01-Framework/04-Pipeline**: Feeds qualified opportunities to pipeline

### Tool Integration
**Apollo API**: Primary data source for company discovery
**CRM Systems**: HubSpot, Salesforce integration for lead management
**Campaign Tools**: Email and LinkedIn campaign integration
**Analytics Tools**: Performance tracking and optimization

## Success Metrics

### Search Success
**Discovery Volume**: 100+ qualified companies per search
**Qualification Rate**: 60%+ companies meet ICP criteria
**Data Quality**: 90%+ complete company profiles
**Search Efficiency**: <30 minutes per search execution

### Campaign Success
**List Utilization**: 80%+ companies used in campaigns
**Response Rate**: 15%+ response rate across all campaigns
**Conversion Rate**: 10%+ lead-to-opportunity conversion
**ROI**: 300%+ return on search and campaign investment

## Implementation Guidelines

### Setup Requirements
**Apollo API**: Active subscription with sufficient credits
**CRM Integration**: HubSpot or Salesforce connection
**Campaign Tools**: Email and LinkedIn campaign platforms
**Analytics**: Performance tracking and reporting tools

### Team Training
**API Usage**: Understanding Apollo API capabilities and limitations
**ICP Application**: How to apply qualification criteria effectively
**Data Management**: CRM integration and data quality management
**Campaign Execution**: How to use generated lists in campaigns

## Risk Mitigation

### API Limitations
**Rate Limits**: Respect Apollo API rate limits (100 requests/minute)
**Credit Management**: Monitor credit usage and optimize searches
**Data Quality**: Validate and clean data before campaign use
**Compliance**: Ensure GDPR and data privacy compliance

### Search Optimization
**Filter Refinement**: Use specific filters to narrow results
**Batch Processing**: Handle large result sets efficiently
**Deduplication**: Remove duplicate companies across searches
**Quality Control**: Validate company data accuracy

## Implementation Notes
- **Last Updated**: 2025-01-27
- **Created By**: System
- **Status**: Active
- **API Source**: [Apollo Organization Search API](https://docs.apollo.io/reference/organization-search)
- **Next Review**: 2025-02-27
