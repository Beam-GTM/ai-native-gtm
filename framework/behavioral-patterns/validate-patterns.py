#!/usr/bin/env python3
"""
Behavioral Pattern Registry Validator
Purpose: Validate pattern registry structure and content
"""

import yaml
import sys
from datetime import datetime
from typing import Dict, List, Any

class PatternValidator:
    """Validates behavioral pattern registry structure and content"""
    
    REQUIRED_PATTERN_FIELDS = [
        'id', 'name', 'failure_rate', 'severity', 'description',
        'pre_execution_check', 'activation_trigger', 'post_completion_validation'
    ]
    
    REQUIRED_CHECK_FIELDS = ['question', 'validation', 'evidence_required']
    
    VALID_SEVERITIES = ['critical', 'high', 'medium', 'low']
    
    def __init__(self, registry_path: str = 'behavioral-patterns-registry.yaml'):
        self.registry_path = registry_path
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.registry: Dict[str, Any] = {}
        
    def load_registry(self) -> bool:
        """Load and parse the registry YAML file"""
        try:
            with open(self.registry_path, 'r') as f:
                self.registry = yaml.safe_load(f)
            print(f"✅ Registry loaded: {self.registry_path}")
            return True
        except FileNotFoundError:
            self.errors.append(f"Registry file not found: {self.registry_path}")
            return False
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML syntax: {e}")
            return False
            
    def validate_metadata(self) -> None:
        """Validate registry metadata"""
        if 'metadata' not in self.registry:
            self.errors.append("Missing metadata section")
            return
            
        metadata = self.registry['metadata']
        required_meta = ['name', 'description', 'version', 'last_updated']
        
        for field in required_meta:
            if field not in metadata:
                self.errors.append(f"Missing metadata field: {field}")
                
        # Check date format
        if 'last_updated' in metadata:
            try:
                datetime.strptime(metadata['last_updated'], '%Y-%m-%d')
            except ValueError:
                self.warnings.append(f"Invalid date format in last_updated: {metadata['last_updated']}")
                
    def validate_patterns(self) -> None:
        """Validate each pattern in the registry"""
        if 'patterns' not in self.registry:
            self.errors.append("Missing patterns section")
            return
            
        patterns = self.registry['patterns']
        
        for pattern_key, pattern in patterns.items():
            self._validate_pattern(pattern_key, pattern)
            
    def _validate_pattern(self, key: str, pattern: Dict[str, Any]) -> None:
        """Validate individual pattern structure"""
        # Check required fields
        for field in self.REQUIRED_PATTERN_FIELDS:
            if field not in pattern:
                self.errors.append(f"Pattern '{key}' missing required field: {field}")
                
        # Validate ID matches key
        if 'id' in pattern and pattern['id'] != key.replace('_', '-'):
            self.warnings.append(f"Pattern '{key}' ID mismatch: {pattern['id']}")
            
        # Validate severity
        if 'severity' in pattern and pattern['severity'] not in self.VALID_SEVERITIES:
            self.errors.append(f"Pattern '{key}' invalid severity: {pattern['severity']}")
            
        # Validate failure rate format
        if 'failure_rate' in pattern:
            rate = pattern['failure_rate']
            if not (isinstance(rate, str) and rate.endswith('%')):
                self.warnings.append(f"Pattern '{key}' failure_rate should be a percentage string")
                
        # Validate pre_execution_check structure
        if 'pre_execution_check' in pattern:
            self._validate_check_structure(key, pattern['pre_execution_check'], 'pre_execution_check')
            
    def _validate_check_structure(self, pattern_key: str, check: Dict[str, Any], check_name: str) -> None:
        """Validate check structure within a pattern"""
        for field in self.REQUIRED_CHECK_FIELDS:
            if field not in check:
                self.errors.append(f"Pattern '{pattern_key}' {check_name} missing field: {field}")
                
    def validate_loading_references(self) -> None:
        """Validate loading reference definitions"""
        if 'loading_references' not in self.registry:
            self.warnings.append("Missing loading_references section")
            return
            
        references = self.registry['loading_references']
        patterns = self.registry.get('patterns', {})
        
        for ref_name, pattern_list in references.items():
            if not isinstance(pattern_list, list):
                self.errors.append(f"Loading reference '{ref_name}' must be a list")
                continue
                
            for pattern_name in pattern_list:
                if pattern_name not in patterns:
                    self.errors.append(f"Loading reference '{ref_name}' references undefined pattern: {pattern_name}")
                    
    def generate_report(self) -> str:
        """Generate validation report"""
        report = []
        report.append("# Behavioral Pattern Registry Validation Report")
        report.append(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Registry**: {self.registry_path}")
        report.append("")
        
        # Summary
        pattern_count = len(self.registry.get('patterns', {}))
        report.append("## Summary")
        report.append(f"- Patterns: {pattern_count}")
        report.append(f"- Errors: {len(self.errors)}")
        report.append(f"- Warnings: {len(self.warnings)}")
        report.append("")
        
        # Pattern list
        if pattern_count > 0:
            report.append("## Patterns Found")
            for pattern_key in self.registry.get('patterns', {}):
                pattern = self.registry['patterns'][pattern_key]
                rate = pattern.get('failure_rate', 'N/A')
                report.append(f"- **{pattern_key}**: {rate} failure prevention")
            report.append("")
            
        # Errors
        if self.errors:
            report.append("## ❌ Errors")
            for error in self.errors:
                report.append(f"- {error}")
            report.append("")
            
        # Warnings
        if self.warnings:
            report.append("## ⚠️ Warnings")
            for warning in self.warnings:
                report.append(f"- {warning}")
            report.append("")
            
        # Success
        if not self.errors:
            report.append("## ✅ Validation Status: PASSED")
            report.append("Registry is valid and ready for use!")
        else:
            report.append("## ❌ Validation Status: FAILED")
            report.append("Please fix errors before using registry.")
            
        return "\n".join(report)
        
    def validate(self) -> bool:
        """Run all validations"""
        if not self.load_registry():
            return False
            
        self.validate_metadata()
        self.validate_patterns()
        self.validate_loading_references()
        
        return len(self.errors) == 0
        
def main():
    """Main validation entry point"""
    validator = PatternValidator()
    
    print("🔍 Validating Behavioral Pattern Registry...")
    print("")
    
    is_valid = validator.validate()
    
    # Generate and save report
    report = validator.generate_report()
    with open('VALIDATION-REPORT.md', 'w') as f:
        f.write(report)
    
    print(report)
    print("")
    print(f"Report saved to: VALIDATION-REPORT.md")
    
    # Exit code based on validation result
    sys.exit(0 if is_valid else 1)
    
if __name__ == "__main__":
    main()