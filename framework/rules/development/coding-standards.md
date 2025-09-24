<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# General Coding Standards

## 💻 **CODING STANDARDS**

### **Code Quality Requirements**
- **Clean Code**: Readable, maintainable, efficient implementation
- **Documentation**: Inline comments for non-obvious code only
- **Security**: No exposed secrets, keys, or sensitive data
- **Performance**: Optimize critical sections, prioritize clarity
- **Error Handling**: Always handle potential errors with proper logging

### **Universal Principles**
```yaml
general_standards:
  understand_first: "Ensure full understanding before coding"
  plan_design: "Break complex tasks into manageable steps"
  code_quality: "Write clean, readable, well-documented code"
  testing: "Assume code needs to be testable"
  refactoring: "Continuously improve existing code"
  security: "Be mindful of security best practices"
  performance: "Consider performance implications"
  tool_usage: "Leverage available tools effectively"
```

### **File Headers**
Every source file MUST include:
```typescript
/**
 * @file filename.ext
 * @description Brief description of purpose and contents
 * @module module_name
 * @author Original Author <email> (optional)
 * @copyright Copyright (c) YYYY Organization
 * @license License information
 */
```

### **Function Documentation**
```typescript
/**
 * Brief description of function purpose
 *
 * @param {Type} paramName - Description of parameter
 * @param {Type} [optional=default] - Optional parameter description
 * @returns {ReturnType} Description of return value
 * @throws {ErrorType} When/why error is thrown
 * @example
 * const result = functionName(param1, param2);
 */
```

