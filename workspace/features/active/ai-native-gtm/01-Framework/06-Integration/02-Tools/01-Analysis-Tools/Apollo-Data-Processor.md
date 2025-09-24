# Apollo Data Processor
**Purpose**: Process and qualify Apollo search results using ICP criteria  
**Status**: Active  
**Integration**: Apollo API Integration Tool

## Overview
This tool processes raw Apollo search results, applies ICP qualification criteria, and generates tiered prospect lists for GTM campaigns.

## ICP Qualification Engine

### Scoring Algorithm Implementation
```python
class ICPQualifier:
    def __init__(self):
        self.icp_criteria = {
            "industry_alignment": {
                "pure_rpo": 30,
                "rpo_staffing_mix": 25,
                "staffing_rpo_potential": 20,
                "other": 0
            },
            "size_fit": {
                "100_2000": 20,
                "200_1000": 18,
                "50_100": 15,
                "1000_5000": 12,
                "other": 0
            },
            "technology_readiness": {
                "ats_crm_integration": 20,
                "ats_only": 15,
                "basic_tech_stack": 10,
                "limited_tech": 5
            },
            "geographic_fit": {
                "north_america": 15,
                "europe": 12,
                "asia_pacific": 10,
                "other": 5
            },
            "revenue_fit": {
                "10m_200m": 15,
                "25m_100m": 13,
                "5m_100m": 12,
                "100m_500m": 10,
                "other": 5
            }
        }
    
    def calculate_icp_score(self, company):
        """
        Calculate ICP score based on company data
        Returns: Score (0-100) and breakdown
        """
        score_breakdown = {}
        total_score = 0
        
        # Industry Alignment (30 points)
        industry_score = self._score_industry_alignment(company)
        score_breakdown["industry_alignment"] = industry_score
        total_score += industry_score
        
        # Size Fit (20 points)
        size_score = self._score_size_fit(company)
        score_breakdown["size_fit"] = size_score
        total_score += size_score
        
        # Technology Readiness (20 points)
        tech_score = self._score_technology_readiness(company)
        score_breakdown["technology_readiness"] = tech_score
        total_score += tech_score
        
        # Geographic Fit (15 points)
        geo_score = self._score_geographic_fit(company)
        score_breakdown["geographic_fit"] = geo_score
        total_score += geo_score
        
        # Revenue Fit (15 points)
        revenue_score = self._score_revenue_fit(company)
        score_breakdown["revenue_fit"] = revenue_score
        total_score += revenue_score
        
        return {
            "total_score": total_score,
            "breakdown": score_breakdown,
            "tier": self._determine_tier(total_score)
        }
    
    def _score_industry_alignment(self, company):
        """Score based on industry alignment with RPO"""
        industry = company.get("industry", "").lower()
        keywords = [k.lower() for k in company.get("keywords", [])]
        
        if "recruitment process outsourcing" in industry or "rpo" in industry:
            return 30
        elif any(keyword in industry for keyword in ["staffing", "talent acquisition"]):
            if any(keyword in keywords for keyword in ["rpo", "recruitment outsourcing"]):
                return 25
            else:
                return 20
        else:
            return 0
    
    def _score_size_fit(self, company):
        """Score based on company size"""
        employees = company.get("employee_count", 0)
        
        if 100 <= employees <= 2000:
            return 20
        elif 200 <= employees <= 1000:
            return 18
        elif 50 <= employees <= 100:
            return 15
        elif 1000 <= employees <= 5000:
            return 12
        else:
            return 0
    
    def _score_technology_readiness(self, company):
        """Score based on technology stack indicators"""
        description = company.get("description", "").lower()
        keywords = [k.lower() for k in company.get("keywords", [])]
        
        tech_indicators = description + " " + " ".join(keywords)
        
        if any(term in tech_indicators for term in ["ats", "crm", "integration"]):
            if all(term in tech_indicators for term in ["ats", "crm"]):
                return 20
            elif "ats" in tech_indicators:
                return 15
            else:
                return 10
        else:
            return 5
    
    def _score_geographic_fit(self, company):
        """Score based on geographic location"""
        country = company.get("country", "").lower()
        
        if country in ["united states", "canada"]:
            return 15
        elif country in ["united kingdom", "germany", "france", "netherlands"]:
            return 12
        elif country in ["australia", "singapore", "japan"]:
            return 10
        else:
            return 5
    
    def _score_revenue_fit(self, company):
        """Score based on annual revenue"""
        revenue = company.get("revenue", 0)
        
        if 10_000_000 <= revenue <= 200_000_000:
            return 15
        elif 25_000_000 <= revenue <= 100_000_000:
            return 13
        elif 5_000_000 <= revenue <= 100_000_000:
            return 12
        elif 100_000_000 <= revenue <= 500_000_000:
            return 10
        else:
            return 5
    
    def _determine_tier(self, score):
        """Determine tier based on total score"""
        if score >= 85:
            return "Tier 1"
        elif score >= 70:
            return "Tier 2"
        elif score >= 50:
            return "Tier 3"
        else:
            return "Unqualified"
```

## Data Processing Pipeline

### Company Data Enrichment
```python
class CompanyDataEnricher:
    def __init__(self):
        self.enrichment_fields = [
            "icp_score",
            "tier_classification",
            "campaign_assignment",
            "priority_level",
            "contact_opportunities"
        ]
    
    def enrich_company_data(self, company, icp_score_data):
        """
        Enrich company data with ICP analysis
        """
        enriched_company = company.copy()
        
        # Add ICP scoring data
        enriched_company.update({
            "icp_score": icp_score_data["total_score"],
            "tier": icp_score_data["tier"],
            "score_breakdown": icp_score_data["breakdown"],
            "priority_level": self._determine_priority(icp_score_data["total_score"]),
            "campaign_assignment": self._assign_campaign(icp_score_data["tier"]),
            "contact_opportunities": self._identify_contact_opportunities(company)
        })
        
        return enriched_company
    
    def _determine_priority(self, score):
        """Determine priority level for outreach"""
        if score >= 90:
            return "High"
        elif score >= 75:
            return "Medium"
        elif score >= 60:
            return "Low"
        else:
            return "Very Low"
    
    def _assign_campaign(self, tier):
        """Assign appropriate campaign based on tier"""
        campaign_assignments = {
            "Tier 1": "Email Campaign - Personalized Outreach",
            "Tier 2": "LinkedIn Campaign - Social Engagement",
            "Tier 3": "Content Campaign - Nurture Sequence",
            "Unqualified": "No Campaign"
        }
        return campaign_assignments.get(tier, "No Campaign")
    
    def _identify_contact_opportunities(self, company):
        """Identify potential contact opportunities"""
        opportunities = []
        
        # Check for LinkedIn presence
        if company.get("linkedin_url"):
            opportunities.append("LinkedIn Outreach")
        
        # Check for website contact info
        if company.get("website"):
            opportunities.append("Website Contact Form")
        
        # Check for industry events
        if "recruitment" in company.get("industry", "").lower():
            opportunities.append("Industry Events")
        
        return opportunities
```

## Tier Classification and Segmentation

### Tier-Based Segmentation
```python
class TierSegmenter:
    def __init__(self):
        self.tier_criteria = {
            "Tier 1": {
                "min_score": 85,
                "max_score": 100,
                "description": "Perfect fit, high probability, immediate opportunity",
                "campaign_type": "Email",
                "outreach_approach": "Personalized"
            },
            "Tier 2": {
                "min_score": 70,
                "max_score": 84,
                "description": "Good fit, medium probability, near-term opportunity",
                "campaign_type": "LinkedIn",
                "outreach_approach": "Social Engagement"
            },
            "Tier 3": {
                "min_score": 50,
                "max_score": 69,
                "description": "Potential fit, lower probability, future opportunity",
                "campaign_type": "Content",
                "outreach_approach": "Nurture Sequence"
            }
        }
    
    def segment_companies(self, enriched_companies):
        """
        Segment companies by tier and campaign assignment
        """
        segments = {
            "Tier 1": [],
            "Tier 2": [],
            "Tier 3": [],
            "Unqualified": []
        }
        
        for company in enriched_companies:
            tier = company.get("tier", "Unqualified")
            if tier in segments:
                segments[tier].append(company)
        
        return segments
    
    def generate_campaign_lists(self, segments):
        """
        Generate campaign-specific lists
        """
        campaign_lists = {
            "email_campaign": {
                "companies": segments["Tier 1"],
                "count": len(segments["Tier 1"]),
                "approach": "Personalized outreach with RPO-specific value props"
            },
            "linkedin_campaign": {
                "companies": segments["Tier 2"],
                "count": len(segments["Tier 2"]),
                "approach": "Social engagement and content sharing"
            },
            "content_campaign": {
                "companies": segments["Tier 3"],
                "count": len(segments["Tier 3"]),
                "approach": "Nurture sequences with educational content"
            }
        }
        
        return campaign_lists
```

## Data Quality and Validation

### Quality Control
```python
class DataQualityController:
    def __init__(self):
        self.required_fields = ["name", "website", "industry", "employee_count"]
        self.quality_thresholds = {
            "min_employee_count": 50,
            "max_employee_count": 5000,
            "min_revenue": 5000000,
            "max_revenue": 500000000
        }
    
    def validate_company_data(self, company):
        """
        Validate company data quality
        """
        validation_results = {
            "is_valid": True,
            "errors": [],
            "warnings": [],
            "quality_score": 0
        }
        
        # Check required fields
        for field in self.required_fields:
            if not company.get(field):
                validation_results["errors"].append(f"Missing required field: {field}")
                validation_results["is_valid"] = False
        
        # Check employee count
        employee_count = company.get("employee_count", 0)
        if not (self.quality_thresholds["min_employee_count"] <= 
                employee_count <= self.quality_thresholds["max_employee_count"]):
            validation_results["warnings"].append(
                f"Employee count {employee_count} outside target range"
            )
        
        # Check revenue
        revenue = company.get("revenue", 0)
        if revenue > 0 and not (self.quality_thresholds["min_revenue"] <= 
                               revenue <= self.quality_thresholds["max_revenue"]):
            validation_results["warnings"].append(
                f"Revenue {revenue} outside target range"
            )
        
        # Calculate quality score
        validation_results["quality_score"] = self._calculate_quality_score(company)
        
        return validation_results
    
    def _calculate_quality_score(self, company):
        """Calculate data quality score (0-100)"""
        score = 0
        
        # Required fields present (40 points)
        required_present = sum(1 for field in self.required_fields if company.get(field))
        score += (required_present / len(self.required_fields)) * 40
        
        # Employee count in range (20 points)
        employee_count = company.get("employee_count", 0)
        if self.quality_thresholds["min_employee_count"] <= employee_count <= self.quality_thresholds["max_employee_count"]:
            score += 20
        
        # Revenue in range (20 points)
        revenue = company.get("revenue", 0)
        if revenue > 0 and self.quality_thresholds["min_revenue"] <= revenue <= self.quality_thresholds["max_revenue"]:
            score += 20
        
        # Additional data present (20 points)
        additional_fields = ["linkedin_url", "description", "keywords"]
        additional_present = sum(1 for field in additional_fields if company.get(field))
        score += (additional_present / len(additional_fields)) * 20
        
        return score
```

## Complete Processing Workflow

### Main Processing Function
```python
def process_apollo_results(apollo_companies):
    """
    Complete processing pipeline for Apollo search results
    """
    # Initialize processors
    qualifier = ICPQualifier()
    enricher = CompanyDataEnricher()
    segmenter = TierSegmenter()
    quality_controller = DataQualityController()
    
    processed_companies = []
    quality_report = {
        "total_companies": len(apollo_companies),
        "valid_companies": 0,
        "invalid_companies": 0,
        "quality_scores": []
    }
    
    # Process each company
    for company in apollo_companies:
        # Validate data quality
        validation = quality_controller.validate_company_data(company)
        
        if validation["is_valid"]:
            quality_report["valid_companies"] += 1
        else:
            quality_report["invalid_companies"] += 1
        
        quality_report["quality_scores"].append(validation["quality_score"])
        
        # Calculate ICP score
        icp_score_data = qualifier.calculate_icp_score(company)
        
        # Enrich company data
        enriched_company = enricher.enrich_company_data(company, icp_score_data)
        
        processed_companies.append(enriched_company)
    
    # Segment companies by tier
    segments = segmenter.segment_companies(processed_companies)
    
    # Generate campaign lists
    campaign_lists = segmenter.generate_campaign_lists(segments)
    
    # Generate processing report
    processing_report = {
        "total_processed": len(processed_companies),
        "tier_distribution": {tier: len(companies) for tier, companies in segments.items()},
        "campaign_assignments": {campaign: data["count"] for campaign, data in campaign_lists.items()},
        "average_quality_score": sum(quality_report["quality_scores"]) / len(quality_report["quality_scores"]),
        "quality_report": quality_report
    }
    
    return {
        "processed_companies": processed_companies,
        "segments": segments,
        "campaign_lists": campaign_lists,
        "processing_report": processing_report
    }
```

## Usage Example

### Complete Workflow Execution
```python
def execute_apollo_processing():
    """
    Execute complete Apollo data processing workflow
    """
    # Step 1: Get Apollo search results (from Apollo API Integration)
    apollo_companies = execute_find_accounts_workflow()
    
    # Step 2: Process and qualify companies
    results = process_apollo_results(apollo_companies)
    
    # Step 3: Generate reports
    print(f"Processing Complete!")
    print(f"Total Companies: {results['processing_report']['total_processed']}")
    print(f"Tier 1: {results['processing_report']['tier_distribution']['Tier 1']}")
    print(f"Tier 2: {results['processing_report']['tier_distribution']['Tier 2']}")
    print(f"Tier 3: {results['processing_report']['tier_distribution']['Tier 3']}")
    print(f"Average Quality Score: {results['processing_report']['average_quality_score']:.1f}")
    
    return results
```

## Implementation Notes
- **Last Updated**: 2025-01-27
- **Created By**: System
- **Status**: Active
- **Dependencies**: Apollo API Integration Tool
- **Next Review**: 2025-02-27
