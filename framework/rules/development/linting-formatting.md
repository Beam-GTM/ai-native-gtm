<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Linting & Formatting

## 🔧 **LINTING & FORMATTING**

### **Ruff Configuration**
Our primary linting and formatting tool is Ruff, configured with:
- Line length: 100 characters
- Python 3.11 target
- Rule sets: E, F, I, UP, N, B, C4, SIM, RUF

### **When to Run Linting**
1. **Before Committing Code**: Always run linter before commits
2. **After Significant Changes**: After new features or refactoring
3. **During CI**: Automated checks on all PRs
4. **When Adding New Files**: Ensure standards from the start
5. **During Code Review**: Verify linting passes

### **Linting Commands**
```bash
# Run linter on all Python files
uv run ruff check .

# Auto-fix issues where possible
uv run ruff check --fix .

# Format all Python files
uv run ruff format .

# Format specific files
uv run ruff format path/to/file.py
```

### **Handling Linting Issues**

#### **Priority: Fix the Issue**
Always prioritize fixing issues when possible.

#### **Inline Ignore (Last Resort)**
If you must ignore a specific rule:
```python
variable = "example"  # noqa: F841
# Always specify exact error code and add comment explaining why
```

### **Common Linting Issues**
- **F401**: Remove unused imports
- **E501**: Break long lines into multiple lines
- **F821**: Ensure all variable names are defined before use
- **F841**: Remove unused variables or prefix with underscore

