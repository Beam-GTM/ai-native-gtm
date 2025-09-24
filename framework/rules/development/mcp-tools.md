<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# MCP Tool Development

## 🔌 **MCP TOOL DEVELOPMENT**

### **MCP Tool Structure**
```bash
app/
└── mcp/
    ├── agent-os.mcp.json      # MCP server configuration
    ├── mcp.py                 # Main script
    ├── server.py              # FastMCP instance
    └── tools/
        └── your_tool/
            ├── your_tool.py           # Tool implementation
            ├── your_tool_pydantic.py  # Pydantic models
            └── your_tool_prompts.py   # Prompts (if LLM-based)
```

### **Tool Definition Pattern**
```python
from pydantic import BaseModel, Field
from app.mcp.server import mcp

class YourToolInput(BaseModel):
    parameter: str = Field(..., description="Clear parameter description")

class YourToolOutput(BaseModel):
    result: str = Field(..., description="Clear result description")

@mcp.tool(
    description="Clear and concise description of what this tool does."
)
async def your_tool_function(input_data: YourToolInput) -> YourToolOutput:
    """
    REQUIRED: Detailed docstring about tool's behavior.
    """
    # Tool logic: Either pure Python or LLMFeature call
    return YourToolOutput(result=processed_data)
```

### **MCP Tool Guidelines**
1. **Atomicity**: Single, well-defined actions
2. **Clarity**: Clear names and descriptions
3. **Type Safety**: Always use Pydantic models
4. **Modularity**: Logical organization
5. **Async Operations**: Use `async` for I/O operations
6. **Error Handling**: Robust error handling with specific exceptions

