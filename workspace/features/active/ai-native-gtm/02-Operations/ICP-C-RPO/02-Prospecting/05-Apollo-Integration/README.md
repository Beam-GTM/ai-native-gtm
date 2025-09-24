# Apollo Integration for RPO Prospecting

**Purpose**: Apollo API integration for finding and qualifying staffing & recruitment companies  
**Status**: Active  
**Last Updated**: 2025-01-27

## Overview

This folder contains the Apollo API integration tools for prospecting staffing and recruitment companies in North America and LATAM. The integration searches for companies, qualifies them based on RPO criteria, and generates prospect lists for campaign targeting.

## Files

### Core Scripts
- **`working_staffing_search.py`** - Main search and qualification script
- **`apollo_setup.py`** - Apollo API setup and testing script
- **`requirements.txt`** - Python dependencies
- **`.env`** - Environment variables (API key)

### Results
- **`working_staffing_results_20250922_171038.json`** - Latest search results with qualified prospects

## Usage

### Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up Apollo API key in `.env` file
3. Run setup script: `python apollo_setup.py`

### Search Execution
```bash
python working_staffing_search.py
```

## Search Results Summary

### Latest Search (2025-01-27)
- **Total Companies Found**: 15 unique staffing companies
- **Tier 1 (High Priority)**: 1 company - Remedy Intelligent Staffing
- **Tier 2 (Medium Priority)**: 1 company - Allegis Group
- **Tier 3 (Low Priority)**: 5 companies
- **Unqualified**: 8 companies

### Top Prospects
1. **Remedy Intelligent Staffing** (Score: 85)
   - Website: remedystaffing.com
   - Location: Atlanta, Georgia, United States
   - Status: High Priority

2. **Allegis Group** (Score: 65)
   - Website: allegisgroup.com
   - Location: Hanover, Maryland, United States
   - Status: Medium Priority

## Qualification Criteria

The search uses a scoring system based on:
- **Company Name Analysis** (30 points) - Staffing-related keywords
- **Website Analysis** (25 points) - Staffing-related domain indicators
- **Geographic Fit** (20 points) - North America & LATAM preference
- **Company Size Indicators** (15 points) - Based on name patterns
- **Technology Readiness** (10 points) - Tech-focused indicators

## Integration with Campaigns

The qualified prospects are automatically categorized into tiers for campaign targeting:
- **Tier 1**: High-priority prospects for immediate outreach
- **Tier 2**: Medium-priority prospects for targeted campaigns
- **Tier 3**: Low-priority prospects for general campaigns

## Next Steps

1. **Campaign Assignment**: Assign prospects to specific campaigns
2. **Contact Discovery**: Find decision makers at qualified companies
3. **Outreach Execution**: Launch targeted outreach campaigns
4. **Performance Tracking**: Monitor campaign effectiveness and ROI

## Technical Notes

- **API Rate Limits**: 100 requests per minute
- **Search Scope**: North America & LATAM only
- **Company Size**: 50-5000 employees
- **Industry Focus**: Staffing & Recruitment

## Maintenance

- **Monthly**: Run new searches to discover additional prospects
- **Weekly**: Review and update qualification criteria
- **Daily**: Monitor API usage and performance
