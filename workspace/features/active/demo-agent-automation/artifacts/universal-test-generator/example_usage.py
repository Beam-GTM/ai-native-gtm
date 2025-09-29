#!/usr/bin/env python3
"""
Example Usage of Universal Test Case Generator
=============================================

This script demonstrates how to use the Universal Test Case Generator
for different business contexts.
"""

import subprocess
import sys
import os

def run_generator(context, scenarios, agent_id):
    """Run the universal test generator with given parameters"""
    cmd = [
        sys.executable, 
        "universal_test_generator.py",
        "--context", context,
        "--scenarios", str(scenarios),
        "--agent-id", agent_id
    ]
    
    print(f"🚀 Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Success!")
        print(result.stdout)
    else:
        print("❌ Error!")
        print(result.stderr)
    
    return result.returncode == 0

def main():
    """Run example scenarios"""
    
    # Example agent ID (replace with your actual agent ID)
    agent_id = "d8b2e9b5-20da-4e69-81cf-5af2933124c9"
    
    print("Universal Test Case Generator - Example Usage")
    print("=" * 50)
    
    # Example 1: Invoices context
    print("\n📄 Example 1: Generating invoice test cases")
    success1 = run_generator("invoices", 2, agent_id)
    
    # Example 2: Orders context
    print("\n📦 Example 2: Generating order test cases")
    success2 = run_generator("orders", 3, agent_id)
    
    # Example 3: POS context
    print("\n💳 Example 3: Generating POS test cases")
    success3 = run_generator("pos", 2, agent_id)
    
    # Example 4: Custom context
    print("\n🔧 Example 4: Generating custom context test cases")
    success4 = run_generator("custom_business", 1, agent_id)
    
    # Summary
    print("\n📊 Summary:")
    print(f"Invoices: {'✅' if success1 else '❌'}")
    print(f"Orders: {'✅' if success2 else '❌'}")
    print(f"POS: {'✅' if success3 else '❌'}")
    print(f"Custom: {'✅' if success4 else '❌'}")
    
    total_success = sum([success1, success2, success3, success4])
    print(f"\nTotal successful: {total_success}/4")

if __name__ == "__main__":
    main()
