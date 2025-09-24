#!/usr/bin/env python3
"""
Working Staffing Company Search using Apollo API
Based on successful company name searches
"""

import os
import requests
import json
import time
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class WorkingStaffingSearch:
    def __init__(self):
        self.api_key = os.getenv('APOLLO_API_KEY')
        self.base_url = "https://api.apollo.io/api/v1"
        self.headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "X-Api-Key": self.api_key
        }
    
    def search_staffing_companies(self):
        """
        Search for staffing companies using multiple approaches
        """
        print("🔍 Working Staffing Company Search")
        print("=" * 50)
        
        # Known staffing companies that we can find
        known_staffing_companies = [
            "Adecco", "ManpowerGroup", "Randstad", "Kelly Services", 
            "Allegis Group", "Aerotek", "Insight Global", "Volt", 
            "Staffmark", "Remedy Intelligent Staffing"
        ]
        
        # Additional search terms that might work
        search_terms = [
            "staffing", "recruitment", "talent acquisition", 
            "employment services", "workforce solutions"
        ]
        
        all_companies = []
        
        # Search for known companies
        print("\n📋 Searching for known staffing companies...")
        for company_name in known_staffing_companies:
            companies = self.search_by_name(company_name)
            if companies:
                all_companies.extend(companies)
                print(f"   ✅ Found {len(companies)} companies for {company_name}")
            else:
                print(f"   ❌ No companies found for {company_name}")
        
        # Search by keywords
        print(f"\n🔍 Searching by keywords...")
        for term in search_terms:
            companies = self.search_by_keyword(term)
            if companies:
                all_companies.extend(companies)
                print(f"   ✅ Found {len(companies)} companies for '{term}'")
            else:
                print(f"   ❌ No companies found for '{term}'")
        
        # Remove duplicates
        unique_companies = []
        seen = set()
        for company in all_companies:
            name = company.get("name", "") or ""
            website = company.get("website_url", "") or ""
            identifier = (name.lower(), website.lower())
            if identifier not in seen and identifier[0] and identifier[1]:
                seen.add(identifier)
                unique_companies.append(company)
        
        print(f"\n📊 Total unique companies found: {len(unique_companies)}")
        return unique_companies
    
    def search_by_name(self, company_name):
        """
        Search for a specific company by name
        """
        search_params = {
            "q_organization_name": company_name,
            "page": 1,
            "per_page": 10
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/mixed_companies/search",
                headers=self.headers,
                json=search_params
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get('accounts', [])
            else:
                return []
                
        except Exception as e:
            print(f"   ❌ Error searching for {company_name}: {e}")
            return []
    
    def search_by_keyword(self, keyword):
        """
        Search by keyword
        """
        search_params = {
            "q_organization_keyword": keyword,
            "page": 1,
            "per_page": 50
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/mixed_companies/search",
                headers=self.headers,
                json=search_params
            )
            
            if response.status_code == 200:
                data = response.json()
                companies = data.get('accounts', [])
                # Filter for staffing-related companies based on name/website
                staffing_companies = []
                for company in companies:
                    name = company.get("name", "").lower()
                    website = company.get("website_url", "").lower()
                    if any(term in name or term in website for term in 
                           ["staffing", "recruitment", "talent", "employment", "workforce", "personnel"]):
                        staffing_companies.append(company)
                return staffing_companies
            else:
                return []
                
        except Exception as e:
            print(f"   ❌ Error searching for '{keyword}': {e}")
            return []
    
    def process_company(self, company):
        """
        Process company data for RPO qualification
        """
        name = company.get("name", "")
        website = company.get("website_url", "")
        location = f"{company.get('city', '')}, {company.get('state', '')}, {company.get('country', '')}"
        
        # Basic qualification based on available data
        score = 0
        qualification_reasons = []
        
        # Company name analysis
        name_lower = name.lower()
        if any(term in name_lower for term in ["staffing", "recruitment", "talent", "employment"]):
            score += 30
            qualification_reasons.append("Staffing-related company name")
        elif any(term in name_lower for term in ["group", "solutions", "services"]):
            score += 20
            qualification_reasons.append("Professional services company")
        else:
            score += 10
            qualification_reasons.append("General company")
        
        # Website analysis
        website_lower = website.lower()
        if any(term in website_lower for term in ["staffing", "recruitment", "talent", "employment", "workforce"]):
            score += 25
            qualification_reasons.append("Staffing-related website")
        elif any(term in website_lower for term in ["hr", "human", "personnel"]):
            score += 15
            qualification_reasons.append("HR-related website")
        else:
            score += 5
            qualification_reasons.append("General website")
        
        # Location analysis
        location_lower = location.lower()
        if any(country in location_lower for country in ["united states", "canada", "mexico"]):
            score += 20
            qualification_reasons.append("North American location")
        elif any(country in location_lower for country in ["brazil", "argentina", "chile", "colombia"]):
            score += 15
            qualification_reasons.append("LATAM location")
        else:
            score += 10
            qualification_reasons.append("Other location")
        
        # Company size estimation (based on name patterns)
        if any(term in name_lower for term in ["group", "global", "international", "worldwide"]):
            score += 15
            qualification_reasons.append("Large company indicator")
        elif any(term in name_lower for term in ["solutions", "services", "partners"]):
            score += 10
            qualification_reasons.append("Mid-size company indicator")
        else:
            score += 5
            qualification_reasons.append("Small company indicator")
        
        # Technology readiness (based on website)
        if any(term in website_lower for term in ["tech", "digital", "online", "platform"]):
            score += 10
            qualification_reasons.append("Technology-focused")
        else:
            score += 5
            qualification_reasons.append("Traditional business")
        
        # Determine tier
        if score >= 80:
            tier = "Tier 1 - High Priority"
        elif score >= 65:
            tier = "Tier 2 - Medium Priority"
        elif score >= 50:
            tier = "Tier 3 - Low Priority"
        else:
            tier = "Unqualified"
        
        return {
            "name": name,
            "website": website,
            "location": location,
            "linkedin_url": company.get("linkedin_url", ""),
            "phone": company.get("phone", ""),
            "apollo_id": company.get("id", ""),
            "qualification_score": score,
            "tier": tier,
            "qualification_reasons": qualification_reasons
        }
    
    def execute_search(self):
        """
        Execute the complete search and qualification process
        """
        print("🚀 Starting Working Staffing Company Search")
        print("=" * 50)
        
        # Search for companies
        companies = self.search_staffing_companies()
        
        if not companies:
            print("❌ No companies found")
            return None
        
        # Process and qualify companies
        print(f"\n🎯 Processing and qualifying {len(companies)} companies...")
        processed_companies = []
        
        for company in companies:
            processed = self.process_company(company)
            processed_companies.append(processed)
        
        # Sort by qualification score
        processed_companies.sort(key=lambda x: x["qualification_score"], reverse=True)
        
        # Generate results
        results = {
            "search_timestamp": datetime.now().isoformat(),
            "total_companies": len(processed_companies),
            "tier_1": [c for c in processed_companies if c["tier"] == "Tier 1 - High Priority"],
            "tier_2": [c for c in processed_companies if c["tier"] == "Tier 2 - Medium Priority"],
            "tier_3": [c for c in processed_companies if c["tier"] == "Tier 3 - Low Priority"],
            "unqualified": [c for c in processed_companies if c["tier"] == "Unqualified"],
            "all_companies": processed_companies
        }
        
        return results
    
    def print_results(self, results):
        """
        Print formatted results
        """
        print("\n" + "=" * 60)
        print("📊 STAFFING COMPANY SEARCH RESULTS")
        print("=" * 60)
        
        print(f"\n📈 SUMMARY:")
        print(f"   Total Companies: {results['total_companies']}")
        print(f"   Tier 1 (High Priority): {len(results['tier_1'])}")
        print(f"   Tier 2 (Medium Priority): {len(results['tier_2'])}")
        print(f"   Tier 3 (Low Priority): {len(results['tier_3'])}")
        print(f"   Unqualified: {len(results['unqualified'])}")
        
        # Show top companies
        print(f"\n🏆 TOP 10 COMPANIES:")
        for i, company in enumerate(results['all_companies'][:10], 1):
            print(f"   {i:2d}. {company['name']:<30} | Score: {company['qualification_score']:2d} | {company['tier']}")
            print(f"       Website: {company['website']}")
            print(f"       Location: {company['location']}")
            print(f"       Reasons: {', '.join(company['qualification_reasons'][:2])}")
            print()
        
        # Show tier breakdown
        for tier_name, tier_companies in [("Tier 1 - High Priority", results['tier_1']), 
                                        ("Tier 2 - Medium Priority", results['tier_2'])]:
            if tier_companies:
                print(f"\n{tier_name}:")
                for company in tier_companies[:5]:  # Show top 5 in each tier
                    print(f"   • {company['name']} (Score: {company['qualification_score']})")
                    print(f"     {company['website']}")
        
        # Save results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"working_staffing_results_{timestamp}.json"
        
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n💾 Results saved to: {filename}")

def main():
    if not os.getenv('APOLLO_API_KEY'):
        print("❌ APOLLO_API_KEY not set")
        return
    
    searcher = WorkingStaffingSearch()
    results = searcher.execute_search()
    
    if results:
        searcher.print_results(results)
    else:
        print("❌ Search failed")

if __name__ == "__main__":
    main()
