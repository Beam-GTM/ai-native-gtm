<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# LLM Development Standards

## 🤖 **LLM DEVELOPMENT STANDARDS**

### **LLM Feature Structure**
```bash
feature_module/
├── __init__.py
├── feature.py                 # Main implementation
├── feature_handler.py         # Optional handler
├── feature_prompts.py         # ChatPromptTemplate definitions
├── feature_pydantic.py        # Pydantic models
├── tests/                     # Unit tests
└── evals/                     # Evaluation framework
    ├── feature_evals.py       # Evaluation implementation
    └── datasets/              # Test cases
```

### **Prompt Engineering Guidelines**

#### **Structure Requirements**
When generating prompts, ALWAYS include:
- **Role**: Define persona and capabilities
- **Task**: State primary objective (minimum 4 sentences)
- **Task Context**: Explain environment and background
- **Reasoning Guidelines**: Step-by-step thought process
- **In-Prompt Context**: Dynamic variables with Markdown headers
- **Edge Cases** (Optional): Complex situations
- **Mistakes to Avoid** (Optional): Common pitfalls
- **Output Requirements**: Format and constraints

#### **System vs Human Prompt:**
- **System Prompt**: Core role, task, reasoning guidelines, restrictions
- **Human Prompt**: Dynamic variables, input data, `{output_format}` at end

#### **Prompt Template Example:**
```python
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

FEATURE_SYSTEM_PROMPT = """
You are a World Renowned Expert in {domain}.

Your primary objective is to {task_description}.

# Task Context
{detailed_context}

# Reasoning Guidelines
1. First, analyze {step_1}
2. Then, consider {step_2}
3. Finally, determine {step_3}

# Mistakes to Avoid
- Don't assume {common_mistake_1}
- Avoid {common_mistake_2}
"""

FEATURE_HUMAN_PROMPT = """
# Input Data
{input_data}

# Additional Context
{context}

{output_format}
"""

feature_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(FEATURE_SYSTEM_PROMPT),
    HumanMessagePromptTemplate.from_template(FEATURE_HUMAN_PROMPT),
])
```

### **Pydantic Models for LLM**
```python
from pydantic import BaseModel, Field

class FeatureOutput(BaseModel):
    reasoning: str = Field(
        description="Complete reasoning of the Expert. Minimum 10 sentences."
    )
    result: str = Field(
        description="The final result of the feature processing"
    )
    confidence: float = Field(
        ge=0.0, le=1.0,
        description="Confidence score between 0 and 1"
    )
```

### **LLM Testing Requirements**

#### **Test Types:**
1. **Accuracy Tests**: Verify correct outputs
2. **Variance Tests**: Ensure consistency (5-10 runs, temperature 0.0)
3. **Edge Case Tests**: Unusual or boundary inputs

#### **Evaluation with GEval:**
```python
from beam_ai_core.executor.evals.providers.beam_eval import GEval

GEval(
    name="MetricName",
    criteria="Clear description of what constitutes success",
    evaluation_steps=[
        "Step 1 of evaluation process",
        "Step 2 of evaluation process",
    ],
    threshold=0.90,  # Minimum acceptable score
)
```

#### **Test Case Design (MECE Approach):**
- **Maximally Realistic**: Mirror real-world scenarios
- **Mutually Exclusive**: Each test focuses on distinct aspect
- **Collectively Exhausting**: Cover entire spectrum of inputs

### **Common LLM Mistakes to Avoid**
- **Output Format Placement**: `{output_format}` MUST be at end of Human Prompt
- **Duplicate Variables**: Never include same variable in System and Human prompts
- **Overly Complex Models**: Keep Pydantic models focused
- **Insufficient Field Descriptions**: Always provide detailed descriptions
- **Missing Error Handling**: Handle malformed LLM responses
- **Inconsistent Naming**: Maintain consistent conventions

