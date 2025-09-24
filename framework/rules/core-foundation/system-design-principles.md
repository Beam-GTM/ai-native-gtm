<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# System Design & Architecture Principles

## 🏗️ **SYSTEM DESIGN & ARCHITECTURE PRINCIPLES**

### **Problem-Solving Methodology**
1. **Understand the problem deeply** - Carefully read the issue and think critically about what is required
2. **Investigate the codebase** - Explore relevant files, search for key functions, and gather context
3. **Develop a clear, step-by-step plan** - Break down the fix into manageable, incremental steps
4. **Implement the fix incrementally** - Make small, testable code changes
5. **Debug as needed** - Use debugging techniques to isolate and resolve issues
6. **Test frequently** - Run tests after each change to verify correctness
7. **Iterate until the root cause is fixed** - Continue until all tests pass
8. **Reflect and validate comprehensively** - Think about original intent, write additional tests

### **Architecture Design Guidelines**
- **Event-Driven Architecture**: Prioritize designs where components communicate asynchronously via events
- **Composability**: Design components that can be easily combined and reused in different ways
- **SOLID Principles**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **Async-First Approach**: Assume asynchronous operations are the default, especially for I/O
- **Framework and Interface Design**: Focus on defining clear contracts between components
- **Developer SDK/API**: Design with the end developer in mind, providing clear, usable APIs
- **Fault Tolerance**: Design systems that can gracefully handle failures in components
- **Durable Execution**: Ensure long-running processes can withstand interruptions

### **Architecture Reasoning Process**
Follow this step-by-step process:

1. **Deconstruct Requirements**: Thoroughly analyze requirements, identify functional and non-functional needs
2. **Analyze Stack Constraints**: Consider available stack, identify hard constraints or preferences
3. **Identify Core Concepts**: Extract fundamental entities, processes, and interactions
4. **Propose High-Level Architectures**: Sketch 2-3 initial architectural styles
5. **Select Key Technologies**: Identify potential technology choices for each architecture
6. **Define Components & Interactions**: Detail main services/components and their interactions
7. **Model Core Data**: Define Domain Models structure, choose database type
8. **Evaluate Trade-offs**: Explicitly list pros and cons for each alternative
9. **Refine and Detail**: Select most promising approach or synthesize hybrid
10. **Consider Cross-Cutting Concerns**: Address security, monitoring, logging, fault tolerance

### **Specific Design Considerations**
```yaml
domain_models:
  - Clearly define primary Domain Models
  - Compare Tabular vs Document databases based on:
    - Data structure
    - Query patterns
    - Scalability needs

framework_design:
  - Evaluate functional vs class-based approaches
  - Justify chosen paradigm
  - Consider maintenance implications

alternatives_presentation:
  minimum: 3 distinct alternatives
  each_must_include:
    - Technical Requirements Addressed
    - Key Design Decisions & Trade-offs
    - Core Domain Events
    - Primary Domain Models
    - High-Level Services/Components
    - Database Choice Justification
    - Framework Choice (Use Existing vs Build Custom)
    - Key Interfaces/Protocols
    - End-user/Developer APIs
```

