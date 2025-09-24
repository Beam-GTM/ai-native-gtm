# Apollo API Integration Tool
**Purpose**: Automated company discovery using Apollo Organization Search API  
**Status**: Active  
**Integration**: [Apollo Organization Search API](https://docs.apollo.io/reference/organization-search)

## Overview
This tool provides automated integration with Apollo's Organization Search API to discover and qualify RPO companies based on ICP criteria.

## Setup Requirements

### API Credentials
```bash
# Environment variables required
export APOLLO_API_KEY="your_apollo_api_key_here"
export APOLLO_RATE_LIMIT="100"  # requests per minute
export APOLLO_MAX_PAGES="500"   # maximum pages to fetch
```

### Dependencies
```python
# Required Python packages
pip install requests
pip install python-dotenv
pip install pandas
pip install json
```

## API Configuration

### Base Configuration
```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class ApolloAPI:
    def __init__(self):
        self.api_key = os.getenv('APOLLO_API_KEY')
        self.base_url = "https://api.apollo.io/api/v1/mixed_companies/search"
        self.headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "X-Api-Key": self.api_key
        }
        self.rate_limit = int(os.getenv('APOLLO_RATE_LIMIT', 100))
        self.max_pages = int(os.getenv('APOLLO_MAX_PAGES', 500))
```

### Search Parameters for ICP-C RPO
```python
def get_rpo_search_params():
    return {
        "company_size": "50-5000",
        "industry": ["Recruitment Process Outsourcing", "Staffing"],
        "keywords": ["RPO", "recruitment", "talent acquisition"],
        "location": ["United States", "Canada", "United Kingdom", "Germany"],
        "revenue": "5000000-500000000",
        "page": 1,
        "per_page": 100
    }
```

## Search Execution

### Primary Search Function
```python
def search_companies(search_params, max_pages=500):
    """
    Execute Apollo search with pagination
    Returns: List of company data
    """
    all_companies = []
    page = 1
    
    while page <= max_pages:
        search_params["page"] = page
        
        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                json=search_params
            )
            
            if response.status_code == 200:
                data = response.json()
                companies = data.get('companies', [])
                
                if not companies:
                    break
                    
                all_companies.extend(companies)
                page += 1
                
                # Rate limiting
                time.sleep(60 / self.rate_limit)
                
            else:
                print(f"Error: {response.status_code} - {response.text}")
                break
                
        except Exception as e:
            print(f"API Error: {e}")
            break
    
    return all_companies
```

### Search Variations
```python
def get_search_variations():
    """
    Define multiple search strategies for comprehensive coverage
    """
    return {
        "core_rpo": {
            "company_size": "50-5000",
            "industry": ["Recruitment Process Outsourcing"],
            "keywords": ["RPO", "recruitment outsourcing"],
            "location": ["United States", "Canada", "United Kingdom", "Germany"],
            "revenue": "5000000-500000000"
        },
        "staffing_companies": {
            "company_size": "50-5000",
            "industry": ["Staffing", "Talent Acquisition"],
            "keywords": ["staffing", "recruitment", "hiring"],
            "location": ["United States", "Canada", "United Kingdom", "Germany"],
            "revenue": "5000000-500000000"
        },
        "tech_recruiters": {
            "company_size": "50-5000",
            "keywords": ["ATS", "recruitment technology", "hiring automation"],
            "location": ["United States", "Canada", "United Kingdom", "Germany"],
            "revenue": "5000000-500000000"
        }
    }
```

## Data Processing

### Company Data Extraction
```python
def extract_company_data(company):
    """
    Extract relevant company information from Apollo response
    """
    return {
        "name": company.get("name", ""),
        "website": company.get("website_url", ""),
        "industry": company.get("industry", ""),
        "employee_count": company.get("estimated_num_employees", 0),
        "revenue": company.get("annual_revenue", 0),
        "location": company.get("city", "") + ", " + company.get("state", ""),
        "country": company.get("country", ""),
        "description": company.get("short_description", ""),
        "keywords": company.get("keywords", []),
        "linkedin_url": company.get("linkedin_url", ""),
        "apollo_id": company.get("id", "")
    }
```

### Deduplication
```python
def deduplicate_companies(companies):
    """
    Remove duplicate companies based on name and website
    """
    seen = set()
    unique_companies = []
    
    for company in companies:
        identifier = (company["name"].lower(), company["website"].lower())
        if identifier not in seen:
            seen.add(identifier)
            unique_companies.append(company)
    
    return unique_companies
```

## Error Handling

### API Error Management
```python
def handle_api_errors(response):
    """
    Handle common Apollo API errors
    """
    if response.status_code == 401:
        return "Invalid API key. Please check your credentials."
    elif response.status_code == 429:
        return "Rate limit exceeded. Please wait before retrying."
    elif response.status_code == 400:
        return "Invalid request parameters. Please check your search criteria."
    elif response.status_code == 500:
        return "Apollo API server error. Please try again later."
    else:
        return f"Unknown error: {response.status_code}"
```

### Retry Logic
```python
import time
from functools import wraps

def retry_on_failure(max_retries=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    time.sleep(delay * (2 ** attempt))
            return None
        return wrapper
    return decorator
```

## Performance Optimization

### Batch Processing
```python
def process_companies_in_batches(companies, batch_size=100):
    """
    Process companies in batches to manage memory and API limits
    """
    for i in range(0, len(companies), batch_size):
        batch = companies[i:i + batch_size]
        yield batch
```

### Caching
```python
import json
from datetime import datetime, timedelta

def cache_search_results(search_params, results, cache_duration_hours=24):
    """
    Cache search results to avoid redundant API calls
    """
    cache_key = hash(json.dumps(search_params, sort_keys=True))
    cache_file = f"cache_{cache_key}.json"
    
    cache_data = {
        "timestamp": datetime.now().isoformat(),
        "search_params": search_params,
        "results": results
    }
    
    with open(cache_file, 'w') as f:
        json.dump(cache_data, f)
    
    return cache_file
```

## Usage Example

### Complete Workflow
```python
def execute_find_accounts_workflow():
    """
    Execute the complete Find Accounts workflow
    """
    apollo = ApolloAPI()
    search_variations = get_search_variations()
    all_companies = []
    
    # Execute all search variations
    for search_name, params in search_variations.items():
        print(f"Executing {search_name} search...")
        companies = apollo.search_companies(params)
        all_companies.extend(companies)
        print(f"Found {len(companies)} companies")
    
    # Process and deduplicate
    processed_companies = [extract_company_data(c) for c in all_companies]
    unique_companies = deduplicate_companies(processed_companies)
    
    print(f"Total unique companies found: {len(unique_companies)}")
    return unique_companies
```

## Integration Points

### CRM Integration
- **HubSpot**: Export to HubSpot contacts and companies
- **Salesforce**: Export to Salesforce leads and accounts
- **Custom CRM**: JSON export for custom integrations

### Campaign Tools
- **Email Marketing**: Export to email campaign platforms
- **LinkedIn**: Export to LinkedIn Sales Navigator
- **Content Marketing**: Export to content management systems

## Monitoring and Analytics

### Performance Metrics
- **Search Success Rate**: Percentage of successful API calls
- **Data Quality**: Completeness of company information
- **Processing Time**: Time to complete full search
- **Cost Tracking**: API credit usage and cost per company

### Logging
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('apollo_integration.log'),
        logging.StreamHandler()
    ]
)
```

## Implementation Notes
- **Last Updated**: 2025-01-27
- **Created By**: System
- **Status**: Active
- **API Version**: Apollo v1
- **Next Review**: 2025-02-27
