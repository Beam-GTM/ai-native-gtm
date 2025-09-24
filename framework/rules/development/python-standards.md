<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Python-Specific Standards

## 🐍 **PYTHON-SPECIFIC STANDARDS**

### **Code Style Guidelines**

#### **WARNING: Take Exceptional Care for Indentation**

**Function Length & Structure:**
- Handle terminal cases first and exit early
- Keep functions under 30-50 lines
- Create helper functions to reduce duplication

```python
# CORRECT Order:
if not successful:
    return
# ... rest of logic here

# WRONG Order:
if successful:
    # ... rest of logic here
else:
    # Handle Failure
```

#### **Conditionals:**
- Avoid excessive `if`/`else` nesting
- Reverse `if`/`else` ladders - handle `else` first
- Prefer `x = y if condition else z` for concise assignments

#### **Naming Conventions:**
- Use `snake_case` for variables, functions, methods
- Use `PascalCase` for class names
- Use `UPPER_CASE` for constants

#### **Loops & Comprehensions:**
- Avoid nested `for` loop ladders
- Prefer list/dict comprehensions over simple loops
- Use `map()`, `filter()`, `reduce()` when clearer

```python
# Good - Comprehension
squared = [x**2 for x in numbers]

# Good - Functional
doubled = list(map(lambda x: x*2, numbers))
```

#### **Asynchronous Programming:**
- Presume async environment (like WSGI)
- Prefer non-blocking async operations
- Always handle async errors with `try...except`
- Use `httpx` over `requests` for async web calls
- Use `asyncio.Queue` for internal event handling

```python
async def fetch_data(url: str) -> dict:
    """Fetch data asynchronously with error handling."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()
    except httpx.HTTPError as e:
        logger.exception(f"HTTP error fetching {url}: {e}")
        raise
```

#### **Type Hints:**
Always provide type hints - NO EXCEPTIONS:
```python
from typing import List, Optional, Dict, Any

def process_items(
    items: List[Dict[str, Any]], 
    filter_key: Optional[str] = None
) -> Dict[str, List[Any]]:
    """Process items with optional filtering."""
    pass
```

#### **Data Structures:**
- Use Pydantic `BaseModel` for structured data
- Prefer TypedDict for return type hints when needed
- Use dataclasses for simple data containers

```python
from pydantic import BaseModel, Field

class UserData(BaseModel):
    name: str = Field(..., description="User's full name")
    email: str = Field(..., description="Valid email address")
    age: int = Field(..., ge=0, le=150, description="User age")
```

#### **Logging:**
Never use `print()`. Use logging module:
```python
import logging
logger = logging.getLogger(__name__)

logger.debug("Debug information")
logger.info("Process started")
logger.warning("Potential issue detected")
logger.error("Error occurred")
logger.exception("Exception with traceback")
```

#### **Generators & Memory:**
Use generators for memory efficiency:
```python
# Good - Generator for large sequences
def process_large_file(filename: str):
    with open(filename) as f:
        for line in f:  # Process line by line
            yield process_line(line)

# Bad - Loading entire file
def process_large_file(filename: str):
    with open(filename) as f:
        data = f.read()  # Loads entire file
        return process_data(data)
```

### **Code Anti-Patterns to Avoid**

#### **Ladder of Chaos:**
```python
# BAD - Excessive if/else nesting
for key in remaining_keys:
    value = kwargs.pop(key)
    if key in llm_input_fields:
        llm_input_direct_kwargs[key] = value
    elif key in llm_config_fields:
        if provided_llm_config is None:
            llm_config_kwargs[key] = value
        else:
            ignored_keys["llm"].append(key)
    elif key in eval_config_fields:
        if provided_eval_config is None:
            eval_config_kwargs[key] = value
        else:
            ignored_keys["eval"].append(key)
```

#### **No Vertical Whitespace:**
```python
# BAD - No separation between logical blocks
async def arun(self, input_data: PromptType, **kwargs) -> LLMOutputType:
    logger.info(f"CustomLLMGenerator: Applying custom pre-processing.")
    modified_prompt = self._custom_prompt_preprocessing(input_data)
    logger.debug(f"Delegating arun to {self.model.__class__.__name__}")
    result = await self.model.arun(modified_prompt, **kwargs)
    logger.info(f"CustomLLMGenerator: Applying custom post-processing.")
    processed_result = self._custom_result_postprocessing(result)
    return processed_result
```

