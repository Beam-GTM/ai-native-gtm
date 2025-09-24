# Data Validation and Quality Control Tools
**Purpose**: Ensure data quality and accuracy for Apollo search results  
**Status**: Active  
**Integration**: Apollo Data Processor

## Overview
This tool provides comprehensive data validation, quality control, and error handling for Apollo search results to ensure high-quality prospect data.

## Data Validation Framework

### Core Validation Rules
```python
class DataValidator:
    def __init__(self):
        self.validation_rules = {
            "required_fields": {
                "name": {"type": "string", "min_length": 1, "max_length": 255},
                "website": {"type": "url", "required": True},
                "industry": {"type": "string", "min_length": 1},
                "employee_count": {"type": "integer", "min_value": 1, "max_value": 100000}
            },
            "optional_fields": {
                "revenue": {"type": "integer", "min_value": 0},
                "linkedin_url": {"type": "url"},
                "description": {"type": "string", "max_length": 1000},
                "keywords": {"type": "list", "max_items": 50}
            },
            "business_rules": {
                "employee_count_range": {"min": 50, "max": 5000},
                "revenue_range": {"min": 5000000, "max": 500000000},
                "valid_industries": ["Recruitment Process Outsourcing", "Staffing", "Talent Acquisition"],
                "valid_countries": ["United States", "Canada", "United Kingdom", "Germany", "Australia"]
            }
        }
    
    def validate_company(self, company):
        """
        Comprehensive validation of company data
        Returns: ValidationResult object
        """
        validation_result = ValidationResult()
        
        # Validate required fields
        self._validate_required_fields(company, validation_result)
        
        # Validate optional fields
        self._validate_optional_fields(company, validation_result)
        
        # Validate business rules
        self._validate_business_rules(company, validation_result)
        
        # Calculate overall quality score
        validation_result.calculate_quality_score()
        
        return validation_result
```

### Validation Result Class
```python
class ValidationResult:
    def __init__(self):
        self.is_valid = True
        self.errors = []
        self.warnings = []
        self.quality_score = 0
        self.field_scores = {}
        self.recommendations = []
    
    def add_error(self, field, message):
        """Add critical validation error"""
        self.errors.append({"field": field, "message": message})
        self.is_valid = False
    
    def add_warning(self, field, message):
        """Add validation warning"""
        self.warnings.append({"field": field, "message": message})
    
    def add_recommendation(self, field, message):
        """Add improvement recommendation"""
        self.recommendations.append({"field": field, "message": message})
    
    def calculate_quality_score(self):
        """Calculate overall data quality score (0-100)"""
        if not self.errors:
            # Base score for no errors
            base_score = 80
            
            # Deduct points for warnings
            warning_penalty = len(self.warnings) * 5
            
            # Add points for field completeness
            completeness_bonus = len(self.field_scores) * 2
            
            self.quality_score = max(0, min(100, base_score - warning_penalty + completeness_bonus))
        else:
            self.quality_score = 0
```

## Field-Specific Validation

### String Field Validation
```python
def validate_string_field(self, field_name, value, rules):
    """Validate string fields with length and format checks"""
    if not value and rules.get("required", False):
        return {"valid": False, "error": f"{field_name} is required"}
    
    if value:
        if not isinstance(value, str):
            return {"valid": False, "error": f"{field_name} must be a string"}
        
        if "min_length" in rules and len(value) < rules["min_length"]:
            return {"valid": False, "error": f"{field_name} too short (min: {rules['min_length']})"}
        
        if "max_length" in rules and len(value) > rules["max_length"]:
            return {"valid": False, "error": f"{field_name} too long (max: {rules['max_length']})"}
    
    return {"valid": True}
```

### URL Field Validation
```python
import re

def validate_url_field(self, field_name, value, rules):
    """Validate URL fields with format and accessibility checks"""
    if not value and rules.get("required", False):
        return {"valid": False, "error": f"{field_name} is required"}
    
    if value:
        # Basic URL format validation
        url_pattern = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        
        if not url_pattern.match(value):
            return {"valid": False, "error": f"{field_name} is not a valid URL"}
        
        # Check for common URL issues
        if value.endswith('/'):
            return {"valid": True, "warning": f"{field_name} has trailing slash"}
    
    return {"valid": True}
```

### Numeric Field Validation
```python
def validate_numeric_field(self, field_name, value, rules):
    """Validate numeric fields with range checks"""
    if not value and rules.get("required", False):
        return {"valid": False, "error": f"{field_name} is required"}
    
    if value is not None:
        try:
            numeric_value = int(value)
            
            if "min_value" in rules and numeric_value < rules["min_value"]:
                return {"valid": False, "error": f"{field_name} below minimum ({rules['min_value']})"}
            
            if "max_value" in rules and numeric_value > rules["max_value"]:
                return {"valid": False, "error": f"{field_name} above maximum ({rules['max_value']})"}
            
            return {"valid": True, "value": numeric_value}
            
        except (ValueError, TypeError):
            return {"valid": False, "error": f"{field_name} must be a number"}
    
    return {"valid": True}
```

## Business Logic Validation

### Industry Validation
```python
def validate_industry(self, industry):
    """Validate industry against RPO-relevant industries"""
    valid_industries = [
        "Recruitment Process Outsourcing",
        "Staffing",
        "Talent Acquisition",
        "Human Resources",
        "Professional Services"
    ]
    
    if not industry:
        return {"valid": False, "error": "Industry is required"}
    
    industry_lower = industry.lower()
    
    # Check for exact matches
    for valid_industry in valid_industries:
        if industry_lower == valid_industry.lower():
            return {"valid": True, "industry": valid_industry}
    
    # Check for partial matches
    for valid_industry in valid_industries:
        if valid_industry.lower() in industry_lower:
            return {"valid": True, "industry": valid_industry, "warning": "Industry normalized"}
    
    # Check for RPO-related keywords
    rpo_keywords = ["rpo", "recruitment", "staffing", "talent", "hiring"]
    if any(keyword in industry_lower for keyword in rpo_keywords):
        return {"valid": True, "industry": industry, "warning": "Industry contains RPO keywords"}
    
    return {"valid": False, "error": "Industry not relevant to RPO business"}
```

### Employee Count Validation
```python
def validate_employee_count(self, employee_count):
    """Validate employee count against ICP criteria"""
    if not employee_count:
        return {"valid": False, "error": "Employee count is required"}
    
    try:
        count = int(employee_count)
        
        if count < 50:
            return {"valid": False, "error": "Employee count too low (min: 50)"}
        
        if count > 5000:
            return {"valid": False, "error": "Employee count too high (max: 5000)"}
        
        # Categorize by size
        if 50 <= count <= 100:
            size_category = "Small"
        elif 101 <= count <= 500:
            size_category = "Medium"
        elif 501 <= count <= 2000:
            size_category = "Large"
        else:
            size_category = "Enterprise"
        
        return {
            "valid": True,
            "count": count,
            "category": size_category
        }
        
    except (ValueError, TypeError):
        return {"valid": False, "error": "Employee count must be a number"}
```

### Revenue Validation
```python
def validate_revenue(self, revenue):
    """Validate revenue against ICP criteria"""
    if not revenue:
        return {"valid": True, "warning": "Revenue not provided"}
    
    try:
        revenue_value = int(revenue)
        
        if revenue_value < 0:
            return {"valid": False, "error": "Revenue cannot be negative"}
        
        if revenue_value > 0 and revenue_value < 5000000:
            return {"valid": True, "warning": "Revenue below target range (min: $5M)"}
        
        if revenue_value > 500000000:
            return {"valid": True, "warning": "Revenue above target range (max: $500M)"}
        
        # Categorize by revenue
        if 5000000 <= revenue_value <= 25000000:
            revenue_category = "Small"
        elif 25000001 <= revenue_value <= 100000000:
            revenue_category = "Medium"
        elif 100000001 <= revenue_value <= 500000000:
            revenue_category = "Large"
        else:
            revenue_category = "Enterprise"
        
        return {
            "valid": True,
            "revenue": revenue_value,
            "category": revenue_category
        }
        
    except (ValueError, TypeError):
        return {"valid": False, "error": "Revenue must be a number"}
```

## Data Quality Scoring

### Quality Metrics
```python
class QualityScorer:
    def __init__(self):
        self.metrics = {
            "completeness": {"weight": 0.3, "max_score": 100},
            "accuracy": {"weight": 0.25, "max_score": 100},
            "consistency": {"weight": 0.2, "max_score": 100},
            "relevance": {"weight": 0.25, "max_score": 100}
        }
    
    def calculate_completeness_score(self, company):
        """Calculate data completeness score"""
        required_fields = ["name", "website", "industry", "employee_count"]
        optional_fields = ["revenue", "linkedin_url", "description", "keywords"]
        
        required_present = sum(1 for field in required_fields if company.get(field))
        optional_present = sum(1 for field in optional_fields if company.get(field))
        
        required_score = (required_present / len(required_fields)) * 60
        optional_score = (optional_present / len(optional_fields)) * 40
        
        return required_score + optional_score
    
    def calculate_accuracy_score(self, company, validation_result):
        """Calculate data accuracy score"""
        if not validation_result.errors:
            base_score = 100
        else:
            base_score = 100 - (len(validation_result.errors) * 20)
        
        # Deduct for warnings
        warning_penalty = len(validation_result.warnings) * 5
        
        return max(0, base_score - warning_penalty)
    
    def calculate_consistency_score(self, company):
        """Calculate data consistency score"""
        score = 100
        
        # Check for consistent naming
        name = company.get("name", "")
        if name and name != name.strip():
            score -= 10
        
        # Check for consistent formatting
        website = company.get("website", "")
        if website and not website.startswith(("http://", "https://")):
            score -= 5
        
        # Check for consistent case
        industry = company.get("industry", "")
        if industry and industry != industry.title():
            score -= 5
        
        return max(0, score)
    
    def calculate_relevance_score(self, company):
        """Calculate relevance to RPO business score"""
        score = 0
        
        # Industry relevance
        industry = company.get("industry", "").lower()
        if "recruitment process outsourcing" in industry:
            score += 40
        elif "staffing" in industry or "talent acquisition" in industry:
            score += 30
        elif "human resources" in industry:
            score += 20
        else:
            score += 10
        
        # Size relevance
        employee_count = company.get("employee_count", 0)
        if 100 <= employee_count <= 2000:
            score += 30
        elif 50 <= employee_count <= 100 or 2000 < employee_count <= 5000:
            score += 20
        else:
            score += 10
        
        # Revenue relevance
        revenue = company.get("revenue", 0)
        if 10000000 <= revenue <= 200000000:
            score += 30
        elif 5000000 <= revenue <= 100000000 or 200000000 < revenue <= 500000000:
            score += 20
        else:
            score += 10
        
        return min(100, score)
    
    def calculate_overall_quality_score(self, company, validation_result):
        """Calculate overall data quality score"""
        scores = {
            "completeness": self.calculate_completeness_score(company),
            "accuracy": self.calculate_accuracy_score(company, validation_result),
            "consistency": self.calculate_consistency_score(company),
            "relevance": self.calculate_relevance_score(company)
        }
        
        weighted_score = sum(
            scores[metric] * self.metrics[metric]["weight"]
            for metric in scores
        )
        
        return {
            "overall_score": weighted_score,
            "component_scores": scores,
            "grade": self._assign_quality_grade(weighted_score)
        }
    
    def _assign_quality_grade(self, score):
        """Assign quality grade based on score"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
```

## Batch Processing and Reporting

### Batch Validation
```python
class BatchValidator:
    def __init__(self):
        self.validator = DataValidator()
        self.quality_scorer = QualityScorer()
    
    def validate_batch(self, companies):
        """Validate a batch of companies"""
        results = {
            "total_companies": len(companies),
            "valid_companies": 0,
            "invalid_companies": 0,
            "quality_scores": [],
            "validation_errors": [],
            "quality_grades": {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0},
            "recommendations": []
        }
        
        for company in companies:
            # Validate company
            validation_result = self.validator.validate_company(company)
            
            if validation_result.is_valid:
                results["valid_companies"] += 1
            else:
                results["invalid_companies"] += 1
                results["validation_errors"].extend(validation_result.errors)
            
            # Calculate quality score
            quality_score = self.quality_scorer.calculate_overall_quality_score(
                company, validation_result
            )
            
            results["quality_scores"].append(quality_score["overall_score"])
            results["quality_grades"][quality_score["grade"]] += 1
            
            # Collect recommendations
            results["recommendations"].extend(validation_result.recommendations)
        
        # Calculate summary statistics
        results["average_quality_score"] = sum(results["quality_scores"]) / len(results["quality_scores"])
        results["validation_success_rate"] = results["valid_companies"] / results["total_companies"]
        
        return results
```

### Quality Report Generation
```python
def generate_quality_report(validation_results):
    """Generate comprehensive quality report"""
    report = {
        "summary": {
            "total_companies": validation_results["total_companies"],
            "valid_companies": validation_results["valid_companies"],
            "invalid_companies": validation_results["invalid_companies"],
            "validation_success_rate": f"{validation_results['validation_success_rate']:.1%}",
            "average_quality_score": f"{validation_results['average_quality_score']:.1f}"
        },
        "quality_distribution": validation_results["quality_grades"],
        "common_errors": _get_common_errors(validation_results["validation_errors"]),
        "recommendations": _get_top_recommendations(validation_results["recommendations"]),
        "data_insights": _generate_data_insights(validation_results)
    }
    
    return report

def _get_common_errors(errors):
    """Get most common validation errors"""
    error_counts = {}
    for error in errors:
        error_type = error["message"]
        error_counts[error_type] = error_counts.get(error_type, 0) + 1
    
    return sorted(error_counts.items(), key=lambda x: x[1], reverse=True)[:5]

def _get_top_recommendations(recommendations):
    """Get top improvement recommendations"""
    rec_counts = {}
    for rec in recommendations:
        rec_type = rec["message"]
        rec_counts[rec_type] = rec_counts.get(rec_type, 0) + 1
    
    return sorted(rec_counts.items(), key=lambda x: x[1], reverse=True)[:5]

def _generate_data_insights(validation_results):
    """Generate data quality insights"""
    insights = []
    
    if validation_results["validation_success_rate"] < 0.8:
        insights.append("Low validation success rate - consider improving data sources")
    
    if validation_results["average_quality_score"] < 70:
        insights.append("Below average data quality - implement data enrichment")
    
    if validation_results["quality_grades"]["F"] > validation_results["total_companies"] * 0.1:
        insights.append("High number of poor quality records - review data collection process")
    
    return insights
```

## Implementation Notes
- **Last Updated**: 2025-01-27
- **Created By**: System
- **Status**: Active
- **Dependencies**: Apollo Data Processor
- **Next Review**: 2025-02-27
