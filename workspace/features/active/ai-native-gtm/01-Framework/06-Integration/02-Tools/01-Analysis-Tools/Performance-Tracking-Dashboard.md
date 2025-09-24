# Performance Tracking and Analytics Dashboard
**Purpose**: Monitor and analyze Apollo workflow performance and campaign effectiveness  
**Status**: Active  
**Integration**: Apollo Data Processor, Data Validation Tools

## Overview
This tool provides comprehensive performance tracking, analytics, and reporting for the Apollo Find Accounts workflow to optimize prospecting efforts and measure ROI.

## Performance Metrics Framework

### Core KPIs
```python
class PerformanceTracker:
    def __init__(self):
        self.metrics = {
            "search_performance": {
                "companies_discovered": 0,
                "search_success_rate": 0.0,
                "api_response_time": 0.0,
                "credit_usage": 0,
                "error_rate": 0.0
            },
            "qualification_performance": {
                "total_qualified": 0,
                "qualification_rate": 0.0,
                "tier_distribution": {"Tier 1": 0, "Tier 2": 0, "Tier 3": 0},
                "average_icp_score": 0.0,
                "quality_score": 0.0
            },
            "campaign_performance": {
                "companies_assigned": 0,
                "campaign_distribution": {"Email": 0, "LinkedIn": 0, "Content": 0},
                "response_rate": 0.0,
                "conversion_rate": 0.0,
                "roi": 0.0
            }
        }
    
    def track_search_metrics(self, search_results, api_metrics):
        """Track Apollo search performance metrics"""
        self.metrics["search_performance"].update({
            "companies_discovered": len(search_results),
            "search_success_rate": api_metrics.get("success_rate", 0.0),
            "api_response_time": api_metrics.get("avg_response_time", 0.0),
            "credit_usage": api_metrics.get("credits_used", 0),
            "error_rate": api_metrics.get("error_rate", 0.0)
        })
    
    def track_qualification_metrics(self, qualified_companies, quality_scores):
        """Track qualification performance metrics"""
        total_companies = len(qualified_companies)
        qualified_count = sum(1 for company in qualified_companies if company.get("tier") != "Unqualified")
        
        tier_distribution = {"Tier 1": 0, "Tier 2": 0, "Tier 3": 0}
        for company in qualified_companies:
            tier = company.get("tier", "Unqualified")
            if tier in tier_distribution:
                tier_distribution[tier] += 1
        
        icp_scores = [company.get("icp_score", 0) for company in qualified_companies]
        avg_icp_score = sum(icp_scores) / len(icp_scores) if icp_scores else 0
        
        self.metrics["qualification_performance"].update({
            "total_qualified": qualified_count,
            "qualification_rate": qualified_count / total_companies if total_companies > 0 else 0,
            "tier_distribution": tier_distribution,
            "average_icp_score": avg_icp_score,
            "quality_score": sum(quality_scores) / len(quality_scores) if quality_scores else 0
        })
    
    def track_campaign_metrics(self, campaign_results):
        """Track campaign performance metrics"""
        total_assigned = sum(campaign_results.values())
        
        self.metrics["campaign_performance"].update({
            "companies_assigned": total_assigned,
            "campaign_distribution": campaign_results,
            "response_rate": self._calculate_response_rate(campaign_results),
            "conversion_rate": self._calculate_conversion_rate(campaign_results),
            "roi": self._calculate_roi(campaign_results)
        })
```

## Search Performance Analytics

### API Performance Monitoring
```python
class APIPerformanceMonitor:
    def __init__(self):
        self.performance_log = []
        self.rate_limit_tracker = RateLimitTracker()
    
    def log_api_call(self, endpoint, response_time, status_code, credits_used):
        """Log individual API call performance"""
        log_entry = {
            "timestamp": datetime.now(),
            "endpoint": endpoint,
            "response_time": response_time,
            "status_code": status_code,
            "credits_used": credits_used,
            "success": status_code == 200
        }
        self.performance_log.append(log_entry)
    
    def calculate_performance_metrics(self):
        """Calculate API performance metrics"""
        if not self.performance_log:
            return {}
        
        successful_calls = [log for log in self.performance_log if log["success"]]
        failed_calls = [log for log in self.performance_log if not log["success"]]
        
        return {
            "total_calls": len(self.performance_log),
            "successful_calls": len(successful_calls),
            "failed_calls": len(failed_calls),
            "success_rate": len(successful_calls) / len(self.performance_log),
            "average_response_time": sum(log["response_time"] for log in successful_calls) / len(successful_calls) if successful_calls else 0,
            "total_credits_used": sum(log["credits_used"] for log in self.performance_log),
            "error_rate": len(failed_calls) / len(self.performance_log)
        }
    
    def identify_performance_issues(self):
        """Identify potential performance issues"""
        issues = []
        metrics = self.calculate_performance_metrics()
        
        if metrics["success_rate"] < 0.95:
            issues.append("Low API success rate - check API key and rate limits")
        
        if metrics["average_response_time"] > 2.0:
            issues.append("Slow API response times - consider optimizing requests")
        
        if metrics["error_rate"] > 0.05:
            issues.append("High error rate - review API usage patterns")
        
        return issues

class RateLimitTracker:
    def __init__(self):
        self.rate_limit = 100  # requests per minute
        self.current_usage = 0
        self.window_start = datetime.now()
    
    def check_rate_limit(self):
        """Check if rate limit is exceeded"""
        now = datetime.now()
        
        # Reset window if minute has passed
        if (now - self.window_start).seconds >= 60:
            self.current_usage = 0
            self.window_start = now
        
        return self.current_usage < self.rate_limit
    
    def increment_usage(self):
        """Increment current usage counter"""
        self.current_usage += 1
    
    def get_remaining_requests(self):
        """Get remaining requests in current window"""
        return max(0, self.rate_limit - self.current_usage)
```

## Qualification Analytics

### ICP Scoring Analytics
```python
class ICPAnalytics:
    def __init__(self):
        self.scoring_history = []
        self.tier_performance = {}
    
    def analyze_scoring_patterns(self, qualified_companies):
        """Analyze ICP scoring patterns and trends"""
        analysis = {
            "score_distribution": self._calculate_score_distribution(qualified_companies),
            "tier_breakdown": self._calculate_tier_breakdown(qualified_companies),
            "industry_analysis": self._analyze_industry_patterns(qualified_companies),
            "size_analysis": self._analyze_size_patterns(qualified_companies),
            "geographic_analysis": self._analyze_geographic_patterns(qualified_companies)
        }
        
        return analysis
    
    def _calculate_score_distribution(self, companies):
        """Calculate score distribution across companies"""
        scores = [company.get("icp_score", 0) for company in companies]
        
        return {
            "min_score": min(scores) if scores else 0,
            "max_score": max(scores) if scores else 0,
            "average_score": sum(scores) / len(scores) if scores else 0,
            "median_score": sorted(scores)[len(scores)//2] if scores else 0,
            "score_ranges": {
                "90-100": len([s for s in scores if 90 <= s <= 100]),
                "80-89": len([s for s in scores if 80 <= s <= 89]),
                "70-79": len([s for s in scores if 70 <= s <= 79]),
                "60-69": len([s for s in scores if 60 <= s <= 69]),
                "50-59": len([s for s in scores if 50 <= s <= 59]),
                "0-49": len([s for s in scores if 0 <= s <= 49])
            }
        }
    
    def _calculate_tier_breakdown(self, companies):
        """Calculate tier distribution and characteristics"""
        tiers = {"Tier 1": [], "Tier 2": [], "Tier 3": [], "Unqualified": []}
        
        for company in companies:
            tier = company.get("tier", "Unqualified")
            if tier in tiers:
                tiers[tier].append(company)
        
        breakdown = {}
        for tier, tier_companies in tiers.items():
            if tier_companies:
                scores = [c.get("icp_score", 0) for c in tier_companies]
                breakdown[tier] = {
                    "count": len(tier_companies),
                    "percentage": len(tier_companies) / len(companies) * 100,
                    "average_score": sum(scores) / len(scores),
                    "min_score": min(scores),
                    "max_score": max(scores)
                }
            else:
                breakdown[tier] = {
                    "count": 0,
                    "percentage": 0,
                    "average_score": 0,
                    "min_score": 0,
                    "max_score": 0
                }
        
        return breakdown
    
    def _analyze_industry_patterns(self, companies):
        """Analyze industry distribution and scoring patterns"""
        industry_scores = {}
        
        for company in companies:
            industry = company.get("industry", "Unknown")
            score = company.get("icp_score", 0)
            
            if industry not in industry_scores:
                industry_scores[industry] = []
            industry_scores[industry].append(score)
        
        analysis = {}
        for industry, scores in industry_scores.items():
            analysis[industry] = {
                "count": len(scores),
                "average_score": sum(scores) / len(scores),
                "high_scorers": len([s for s in scores if s >= 80])
            }
        
        return analysis
```

## Campaign Performance Analytics

### Campaign Effectiveness Tracking
```python
class CampaignAnalytics:
    def __init__(self):
        self.campaign_metrics = {
            "email_campaign": {"sent": 0, "opened": 0, "responded": 0, "converted": 0},
            "linkedin_campaign": {"sent": 0, "opened": 0, "responded": 0, "converted": 0},
            "content_campaign": {"sent": 0, "opened": 0, "responded": 0, "converted": 0}
        }
    
    def track_campaign_metrics(self, campaign_type, metrics):
        """Track campaign performance metrics"""
        if campaign_type in self.campaign_metrics:
            self.campaign_metrics[campaign_type].update(metrics)
    
    def calculate_campaign_roi(self, campaign_type):
        """Calculate ROI for specific campaign type"""
        if campaign_type not in self.campaign_metrics:
            return 0
        
        metrics = self.campaign_metrics[campaign_type]
        
        # Calculate conversion rate
        if metrics["sent"] > 0:
            conversion_rate = metrics["converted"] / metrics["sent"]
        else:
            conversion_rate = 0
        
        # Calculate response rate
        if metrics["sent"] > 0:
            response_rate = metrics["responded"] / metrics["sent"]
        else:
            response_rate = 0
        
        # Calculate ROI (simplified calculation)
        cost_per_contact = 0.50  # Estimated cost per contact
        revenue_per_conversion = 10000  # Estimated revenue per conversion
        
        total_cost = metrics["sent"] * cost_per_contact
        total_revenue = metrics["converted"] * revenue_per_conversion
        
        if total_cost > 0:
            roi = ((total_revenue - total_cost) / total_cost) * 100
        else:
            roi = 0
        
        return {
            "conversion_rate": conversion_rate,
            "response_rate": response_rate,
            "total_cost": total_cost,
            "total_revenue": total_revenue,
            "roi": roi
        }
    
    def compare_campaign_performance(self):
        """Compare performance across all campaigns"""
        comparison = {}
        
        for campaign_type, metrics in self.campaign_metrics.items():
            roi_data = self.calculate_campaign_roi(campaign_type)
            comparison[campaign_type] = {
                "sent": metrics["sent"],
                "response_rate": roi_data["response_rate"],
                "conversion_rate": roi_data["conversion_rate"],
                "roi": roi_data["roi"]
            }
        
        return comparison
```

## Dashboard Generation

### Performance Dashboard
```python
class PerformanceDashboard:
    def __init__(self):
        self.tracker = PerformanceTracker()
        self.api_monitor = APIPerformanceMonitor()
        self.icp_analytics = ICPAnalytics()
        self.campaign_analytics = CampaignAnalytics()
    
    def generate_dashboard(self, search_results, qualified_companies, campaign_results):
        """Generate comprehensive performance dashboard"""
        dashboard = {
            "executive_summary": self._generate_executive_summary(search_results, qualified_companies),
            "search_performance": self._generate_search_performance_section(),
            "qualification_analytics": self._generate_qualification_section(qualified_companies),
            "campaign_performance": self._generate_campaign_section(campaign_results),
            "recommendations": self._generate_recommendations(),
            "trends": self._generate_trend_analysis()
        }
        
        return dashboard
    
    def _generate_executive_summary(self, search_results, qualified_companies):
        """Generate executive summary of performance"""
        total_discovered = len(search_results)
        total_qualified = len([c for c in qualified_companies if c.get("tier") != "Unqualified"])
        qualification_rate = total_qualified / total_discovered if total_discovered > 0 else 0
        
        tier_1_count = len([c for c in qualified_companies if c.get("tier") == "Tier 1"])
        tier_2_count = len([c for c in qualified_companies if c.get("tier") == "Tier 2"])
        tier_3_count = len([c for c in qualified_companies if c.get("tier") == "Tier 3"])
        
        return {
            "total_companies_discovered": total_discovered,
            "total_companies_qualified": total_qualified,
            "qualification_rate": f"{qualification_rate:.1%}",
            "tier_1_targets": tier_1_count,
            "tier_2_targets": tier_2_count,
            "tier_3_targets": tier_3_count,
            "high_priority_opportunities": tier_1_count,
            "overall_performance": "Excellent" if qualification_rate > 0.15 else "Good" if qualification_rate > 0.10 else "Needs Improvement"
        }
    
    def _generate_search_performance_section(self):
        """Generate search performance section"""
        api_metrics = self.api_monitor.calculate_performance_metrics()
        
        return {
            "api_performance": {
                "success_rate": f"{api_metrics.get('success_rate', 0):.1%}",
                "average_response_time": f"{api_metrics.get('average_response_time', 0):.2f}s",
                "total_credits_used": api_metrics.get('total_credits_used', 0),
                "error_rate": f"{api_metrics.get('error_rate', 0):.1%}"
            },
            "performance_issues": self.api_monitor.identify_performance_issues(),
            "rate_limit_status": {
                "current_usage": self.api_monitor.rate_limit_tracker.current_usage,
                "remaining_requests": self.api_monitor.rate_limit_tracker.get_remaining_requests(),
                "rate_limit": self.api_monitor.rate_limit_tracker.rate_limit
            }
        }
    
    def _generate_qualification_section(self, qualified_companies):
        """Generate qualification analytics section"""
        analysis = self.icp_analytics.analyze_scoring_patterns(qualified_companies)
        
        return {
            "score_distribution": analysis["score_distribution"],
            "tier_breakdown": analysis["tier_breakdown"],
            "industry_analysis": analysis["industry_analysis"],
            "size_analysis": analysis["size_analysis"],
            "geographic_analysis": analysis["geographic_analysis"]
        }
    
    def _generate_campaign_section(self, campaign_results):
        """Generate campaign performance section"""
        comparison = self.campaign_analytics.compare_campaign_performance()
        
        return {
            "campaign_comparison": comparison,
            "best_performing_campaign": max(comparison.items(), key=lambda x: x[1]["roi"])[0] if comparison else "None",
            "recommended_actions": self._generate_campaign_recommendations(comparison)
        }
    
    def _generate_recommendations(self):
        """Generate actionable recommendations"""
        recommendations = []
        
        # API performance recommendations
        api_metrics = self.api_monitor.calculate_performance_metrics()
        if api_metrics.get("success_rate", 0) < 0.95:
            recommendations.append("Improve API reliability - check rate limits and error handling")
        
        if api_metrics.get("average_response_time", 0) > 2.0:
            recommendations.append("Optimize API calls - consider batching or parallel processing")
        
        # Qualification recommendations
        # Add qualification-specific recommendations based on analytics
        
        return recommendations
    
    def _generate_trend_analysis(self):
        """Generate trend analysis over time"""
        # This would typically pull from historical data
        return {
            "qualification_rate_trend": "Increasing",
            "api_performance_trend": "Stable",
            "campaign_roi_trend": "Improving",
            "recommended_focus_areas": ["Tier 1 targeting", "API optimization"]
        }
```

## Reporting and Export

### Report Generation
```python
def generate_performance_report(dashboard_data, format="json"):
    """Generate performance report in specified format"""
    if format == "json":
        return json.dumps(dashboard_data, indent=2)
    elif format == "csv":
        return _convert_to_csv(dashboard_data)
    elif format == "html":
        return _convert_to_html(dashboard_data)
    else:
        return dashboard_data

def export_metrics_to_file(dashboard_data, filename):
    """Export dashboard data to file"""
    with open(filename, 'w') as f:
        json.dump(dashboard_data, f, indent=2)
    
    print(f"Performance report exported to {filename}")
```

## Implementation Notes
- **Last Updated**: 2025-01-27
- **Created By**: System
- **Status**: Active
- **Dependencies**: Apollo Data Processor, Data Validation Tools
- **Next Review**: 2025-02-27
