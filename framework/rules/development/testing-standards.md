<!-- version: shard-20250825154349 -->
<!-- last-updated: 2025-08-25T15:43:49Z -->
<!-- document-type: engineering-rule-shard -->
<!-- parent-document: consolidated-rules -->

# Testing Standards

## 🧪 **TESTING STANDARDS**

### **Testing Philosophy**
- **Test First**: Write tests before or alongside implementation
- **MECE Principle**: Tests should be Mutually Exclusive, Collectively Exhaustive
- **Isolation**: Each test should be independent
- **Clarity**: Test names should clearly describe what is being tested
- **Speed**: Prioritize fast unit tests over slow integration tests
- **Comprehensive Coverage**: Test all scenarios

### **Test Organization**
```bash
module_name/
├── __init__.py
├── module_code.py
└── tests/
    ├── __init__.py
    ├── __mocks__/             # Mock objects and fixtures
    │   └── mock_*.py
    ├── unit/                  # Unit tests for non-LLM functions
    │   └── test_*.py
    ├── integration/           # Integration tests
    │   └── test_*.py
    ├── accuracy/              # LLM accuracy tests
    │   └── test_*.py
    └── evals/                 # LLM evaluations with GEval
        ├── __data__/          # Test data and datasets
        └── *_evals.py
```

### **Test Scenarios - MANDATORY**

Every function MUST be tested with:

1. **Happy Path**: Expected, valid data
```python
def test_calculate_discount_valid_input():
    """Test discount calculation with valid input."""
    result = calculate_discount(price=100, discount_percent=10)
    assert result == 90
```

2. **Failure Scenarios**: Invalid or unexpected data
```python
def test_calculate_discount_negative_price():
    """Test discount calculation with negative price."""
    with pytest.raises(ValueError, match="Price cannot be negative"):
        calculate_discount(price=-100, discount_percent=10)
```

3. **Blank/Empty Data**: None, empty strings, empty lists
```python
def test_process_items_empty_list():
    """Test processing with empty item list."""
    result = process_items([])
    assert result == {"count": 0, "items": []}

def test_create_user_none_values():
    """Test user creation with None values."""
    with pytest.raises(ValueError, match="Username is required"):
        create_user(username=None, email="test@example.com")
```

4. **Edge Cases**: Boundary conditions and large data
```python
def test_pagination_edge_cases():
    """Test pagination with edge case values."""
    # Test first page
    assert get_page(items=range(100), page=1, size=10) == list(range(10))
    
    # Test last page
    assert get_page(items=range(100), page=10, size=10) == list(range(90, 100))
    
    # Test beyond last page
    assert get_page(items=range(100), page=11, size=10) == []
```

### **Test Structure Patterns**

#### **AAA Pattern (Arrange-Act-Assert):**
```python
def test_calculate_total():
    # Arrange
    items = [{"price": 10}, {"price": 20}]
    
    # Act
    total = calculate_total(items)
    
    # Assert
    assert total == 30
```

#### **Given-When-Then (BDD Style):**
```python
def test_user_authentication():
    # Given a user with valid credentials
    user = User(username="test", password="secure123")
    
    # When the user attempts to authenticate
    result = authenticate(user)
    
    # Then the authentication should succeed
    assert result.is_authenticated is True
```

### **Parametrized Tests**
```python
@pytest.mark.parametrize("input_value,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("", ""),
    (None, None),
])
def test_uppercase_conversion(input_value, expected):
    """Test uppercase conversion with multiple inputs."""
    assert to_uppercase(input_value) == expected
```

### **Async Testing**
```python
@pytest.mark.asyncio
async def test_async_function():
    """Test an async function."""
    result = await async_operation()
    assert result == "expected_value"

@pytest.fixture
async def async_client():
    """Create an async client for testing."""
    client = AsyncClient()
    await client.connect()
    yield client
    await client.disconnect()
```

### **Test Coverage Requirements**
- Overall: 80% minimum
- Core business logic: 90% minimum
- Utility functions: 85% minimum
- API endpoints: 95% minimum

### **Test Execution Commands**
```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest path/to/test_file.py

# Run with coverage
uv run pytest --cov

# Run tests in parallel
uv run pytest -n auto

# Run only failed tests
uv run pytest --lf

# Run with verbose output
uv run pytest -vv
```

