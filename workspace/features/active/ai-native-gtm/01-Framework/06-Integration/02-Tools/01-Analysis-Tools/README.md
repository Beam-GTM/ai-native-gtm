# Apollo API Integration Setup
**Purpose**: Complete setup and configuration for Apollo API integration  
**Status**: Active  
**Documentation**: [Apollo API Docs](https://docs.apollo.io/)

## Quick Start

### 1. Get Your Apollo API Key
1. Go to [Apollo API Settings](https://app.apollo.io/settings/integrations/api)
2. Create a new API key
3. Copy the API key for configuration

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Environment Variables
```bash
export APOLLO_API_KEY='your_apollo_api_key_here'
```

### 4. Run Setup Script
```bash
python apollo_setup.py
```

## Setup Process

The setup script will:
- ✅ Test your API key validity
- 📊 Check rate limits and usage
- 🔍 Test organization search functionality
- 👥 Test people search functionality
- 📝 Create environment configuration file

## API Endpoints Used

### Organization Search
- **Endpoint**: `POST /api/v1/mixed_companies/search`
- **Purpose**: Find RPO companies based on ICP criteria
- **Reference**: [Organization Search Docs](https://docs.apollo.io/reference/organization-search)

### People Search
- **Endpoint**: `POST /api/v1/mixed_people/search`
- **Purpose**: Find decision makers at target companies
- **Reference**: [People Search Docs](https://docs.apollo.io/reference/people-search)

### Usage Stats
- **Endpoint**: `POST /api/v1/usage_stats`
- **Purpose**: Monitor API usage and rate limits
- **Reference**: [Usage Stats Docs](https://docs.apollo.io/reference/view-api-usage-stats-and-rate-limits)

## Configuration

### Environment Variables
```bash
# Required
APOLLO_API_KEY=your_apollo_api_key_here

# Optional
APOLLO_RATE_LIMIT=100
APOLLO_MAX_PAGES=500
RPO_COMPANY_SIZE_MIN=50
RPO_COMPANY_SIZE_MAX=5000
RPO_REVENUE_MIN=5000000
RPO_REVENUE_MAX=500000000
```

### Search Parameters for RPO
```python
search_params = {
    "company_size": "50-5000",
    "industry": ["Recruitment Process Outsourcing", "Staffing"],
    "keywords": ["RPO", "recruitment", "talent acquisition"],
    "location": ["United States", "Canada", "United Kingdom", "Germany"],
    "revenue": "5000000-500000000"
}
```

## Rate Limits

Apollo API has the following rate limits:
- **Requests per minute**: 100
- **Daily limit**: Varies by plan
- **Monthly limit**: Varies by plan

## Error Handling

Common error responses:
- **401**: Invalid API key
- **429**: Rate limit exceeded
- **400**: Invalid request parameters
- **500**: Server error

## Testing

Run the setup script to test all functionality:
```bash
python apollo_setup.py
```

Expected output:
```
🚀 Starting Apollo API Setup...
✅ API Key is valid and working!
📊 Rate limit information retrieved
🔍 Organization search successful!
👥 People search successful!
✅ Apollo API Setup Complete!
```

## Next Steps

After successful setup:
1. **Apollo Integration Moved**: The working Apollo integration has been moved to `02-Operations/ICP-C-RPO/02-Prospecting/05-Apollo-Integration/` for better organization
2. **Run Working Search**: Use `working_staffing_search.py` in the operations folder
3. **Monitor API Usage**: Track performance and rate limits
4. **Scale Up**: Adjust search parameters based on results

## Troubleshooting

### API Key Issues
- Verify key is correct and active
- Check if key has expired
- Ensure proper permissions

### Rate Limit Issues
- Implement proper delays between requests
- Monitor usage with usage_stats endpoint
- Consider upgrading plan if needed

### Search Issues
- Verify search parameters are valid
- Check for typos in industry/keywords
- Test with simpler parameters first

## Support

- **Apollo API Docs**: https://docs.apollo.io/
- **Apollo Support**: https://help.apollo.io/
- **API Status**: https://status.apollo.io/