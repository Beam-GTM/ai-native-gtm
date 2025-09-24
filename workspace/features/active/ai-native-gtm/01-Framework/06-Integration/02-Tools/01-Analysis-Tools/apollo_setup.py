#!/usr/bin/env python3
"""
Apollo API Setup Script
Based on Apollo API Documentation: https://docs.apollo.io/
"""

import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ApolloAPISetup:
    def __init__(self):
        self.base_url = "https://api.apollo.io/api/v1"
        self.api_key = os.getenv('APOLLO_API_KEY')
        
        if not self.api_key:
            print("❌ APOLLO_API_KEY not found in environment variables")
            print("Please set your Apollo API key:")
            print("export APOLLO_API_KEY='your_api_key_here'")
            return
        
        self.headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "X-Api-Key": self.api_key
        }
        
        print("✅ Apollo API Setup initialized")
        print(f"🔑 API Key: {self.api_key[:8]}...{self.api_key[-4:]}")
    
    def test_api_key(self):
        """
        Test API key validity using Apollo's test endpoint
        Reference: https://docs.apollo.io/reference/test-api-key
        """
        print("\n🧪 Testing Apollo API Key...")
        
        try:
            response = requests.get(
                f"{self.base_url}/auth/health",
                headers=self.headers
            )
            
            if response.status_code == 200:
                print("✅ API Key is valid and working!")
                return True
            elif response.status_code == 401:
                print("❌ API Key is invalid or expired")
                return False
            else:
                print(f"⚠️ Unexpected response: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error testing API key: {e}")
            return False
    
    def get_rate_limits(self):
        """
        Get current rate limits and usage
        Reference: https://docs.apollo.io/reference/view-api-usage-stats-and-rate-limits
        """
        print("\n📊 Checking API Rate Limits...")
        
        try:
            response = requests.post(
                f"{self.base_url}/usage_stats",
                headers=self.headers,
                json={}
            )
            
            if response.status_code == 200:
                data = response.json()
                print("✅ Rate limit information retrieved:")
                print(f"   - Daily limit: {data.get('daily_limit', 'N/A')}")
                print(f"   - Daily used: {data.get('daily_used', 'N/A')}")
                print(f"   - Monthly limit: {data.get('monthly_limit', 'N/A')}")
                print(f"   - Monthly used: {data.get('monthly_used', 'N/A')}")
                return data
            else:
                print(f"❌ Error getting rate limits: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error checking rate limits: {e}")
            return None
    
    def test_organization_search(self):
        """
        Test Organization Search endpoint with RPO criteria
        Reference: https://docs.apollo.io/reference/organization-search
        """
        print("\n🔍 Testing Organization Search...")
        
        # Test search parameters for RPO companies
        search_params = {
            "company_size": "50-5000",
            "industry": ["Recruitment Process Outsourcing", "Staffing"],
            "keywords": ["RPO", "recruitment"],
            "location": ["United States", "Canada"],
            "page": 1,
            "per_page": 10  # Small test to avoid using too many credits
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/mixed_companies/search",
                headers=self.headers,
                json=search_params
            )
            
            if response.status_code == 200:
                data = response.json()
                companies = data.get('companies', [])
                print(f"✅ Organization search successful!")
                print(f"   - Found {len(companies)} companies")
                print(f"   - Total available: {data.get('pagination', {}).get('total_entries', 'Unknown')}")
                
                # Show sample results
                if companies:
                    print("\n📋 Sample companies found:")
                    for i, company in enumerate(companies[:3], 1):
                        print(f"   {i}. {company.get('name', 'N/A')} - {company.get('industry', 'N/A')}")
                
                return True
            else:
                print(f"❌ Organization search failed: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error testing organization search: {e}")
            return False
    
    def test_people_search(self):
        """
        Test People Search endpoint
        Reference: https://docs.apollo.io/reference/people-search
        """
        print("\n👥 Testing People Search...")
        
        # Test search for people at RPO companies
        search_params = {
            "person_titles": ["CEO", "CTO", "VP of Talent", "Head of Recruitment"],
            "organization_domains": ["allegisglobalsolutions.com", "sevenstep.com"],
            "page": 1,
            "per_page": 5
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/mixed_people/search",
                headers=self.headers,
                json=search_params
            )
            
            if response.status_code == 200:
                data = response.json()
                people = data.get('people', [])
                print(f"✅ People search successful!")
                print(f"   - Found {len(people)} people")
                
                # Show sample results
                if people:
                    print("\n👤 Sample people found:")
                    for i, person in enumerate(people[:3], 1):
                        name = f"{person.get('first_name', '')} {person.get('last_name', '')}"
                        title = person.get('title', 'N/A')
                        company = person.get('organization', {}).get('name', 'N/A')
                        print(f"   {i}. {name} - {title} at {company}")
                
                return True
            else:
                print(f"❌ People search failed: {response.status_code}")
                print(f"Response: {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error testing people search: {e}")
            return False
    
    def create_environment_file(self):
        """
        Create .env file template for Apollo API configuration
        """
        print("\n📝 Creating environment configuration...")
        
        env_content = """# Apollo API Configuration
# Get your API key from: https://app.apollo.io/settings/integrations/api
APOLLO_API_KEY=your_apollo_api_key_here

# Rate limiting (requests per minute)
APOLLO_RATE_LIMIT=100

# Maximum pages to fetch per search
APOLLO_MAX_PAGES=500

# Search parameters for RPO companies
RPO_COMPANY_SIZE_MIN=50
RPO_COMPANY_SIZE_MAX=5000
RPO_REVENUE_MIN=5000000
RPO_REVENUE_MAX=500000000

# Target countries
RPO_TARGET_COUNTRIES=United States,Canada,United Kingdom,Germany,Australia

# RPO industry keywords
RPO_INDUSTRY_KEYWORDS=Recruitment Process Outsourcing,Staffing,Talent Acquisition
RPO_BUSINESS_KEYWORDS=RPO,recruitment,talent acquisition,hiring,staffing
"""
        
        try:
            with open('.env', 'w') as f:
                f.write(env_content)
            print("✅ Created .env file template")
            print("   Please update APOLLO_API_KEY with your actual API key")
            return True
        except Exception as e:
            print(f"❌ Error creating .env file: {e}")
            return False
    
    def run_full_setup(self):
        """
        Run complete Apollo API setup and testing
        """
        print("🚀 Starting Apollo API Setup...")
        print("=" * 50)
        
        # Step 1: Test API key
        if not self.test_api_key():
            print("\n❌ Setup failed: Invalid API key")
            return False
        
        # Step 2: Check rate limits
        self.get_rate_limits()
        
        # Step 3: Test organization search
        if not self.test_organization_search():
            print("\n⚠️ Organization search test failed, but continuing...")
        
        # Step 4: Test people search
        if not self.test_people_search():
            print("\n⚠️ People search test failed, but continuing...")
        
        # Step 5: Create environment file
        self.create_environment_file()
        
        print("\n" + "=" * 50)
        print("✅ Apollo API Setup Complete!")
        print("\nNext steps:")
        print("1. Update .env file with your actual API key")
        print("2. Run the Find Accounts Workflow")
        print("3. Monitor API usage and rate limits")
        
        return True

def main():
    """
    Main setup function
    """
    print("Apollo API Setup for Find Accounts Workflow")
    print("Based on: https://docs.apollo.io/")
    print("=" * 50)
    
    # Check if API key is set
    if not os.getenv('APOLLO_API_KEY'):
        print("❌ APOLLO_API_KEY environment variable not set")
        print("\nTo get your API key:")
        print("1. Go to https://app.apollo.io/settings/integrations/api")
        print("2. Create a new API key")
        print("3. Set it as an environment variable:")
        print("   export APOLLO_API_KEY='your_api_key_here'")
        print("4. Run this script again")
        return
    
    # Run setup
    setup = ApolloAPISetup()
    setup.run_full_setup()

if __name__ == "__main__":
    main()
