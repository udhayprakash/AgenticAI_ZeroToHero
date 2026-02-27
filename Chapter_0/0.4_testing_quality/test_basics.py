"""
Basic pytest Examples

Run tests with:
    uv add --dev pytest
    uv run pytest test_basics.py -v
    uv run pytest test_basics.py -v -s  # Show print statements
"""

import pytest


# ============================================================================
# 1. BASIC TEST FUNCTIONS
# ============================================================================

def add(a, b):
    """Simple function to test"""
    return a + b


def test_add():
    """Test basic addition"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add_edge_cases():
    """Test edge cases"""
    assert add(1.5, 2.5) == 4.0
    assert add(-5, -10) == -15


# ============================================================================
# 2. EXCEPTION TESTING
# ============================================================================

def divide(a, b):
    """Division function that raises ZeroDivisionError"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_divide_success():
    """Test successful division"""
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    """Test that exception is raised"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# ============================================================================
# 3. PARAMETRIZED TESTS
# ============================================================================

@pytest.mark.parametrize("input_val,expected", [
    (1, 1),
    (2, 2),
    (3, 6),
    (5, 120),
])
def test_factorial(input_val, expected):
    """Test factorial with multiple inputs"""
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    assert factorial(input_val) == expected


@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    """Parametrized test for addition"""
    assert add(a, b) == expected


# ============================================================================
# 4. FIXTURES
# ============================================================================

@pytest.fixture
def sample_data():
    """Fixture that provides test data"""
    return {"name": "Agent", "status": "active"}


def test_with_fixture(sample_data):
    """Test that uses a fixture"""
    assert sample_data["name"] == "Agent"
    assert sample_data["status"] == "active"


@pytest.fixture
def api_client():
    """Fixture that sets up and tears down a resource"""
    print("\n[Setup] Creating API client")
    client = {"connected": True}
    
    yield client  # Test runs here
    
    print("\n[Teardown] Closing API client")
    client["connected"] = False


def test_api_client(api_client):
    """Test using API client fixture"""
    assert api_client["connected"] is True


# ============================================================================
# 5. FIXTURE SCOPE
# ============================================================================

@pytest.fixture(scope="module")
def expensive_resource():
    """
    Fixture that's created once per module (not per test).
    Use for expensive operations like database setup.
    """
    print("\n[Module Setup] Creating resource")
    resource = {"data": [1, 2, 3]}
    yield resource
    print("\n[Module Teardown] Cleaning up")


def test_using_expensive_resource_1(expensive_resource):
    """First test using expensive resource"""
    assert len(expensive_resource["data"]) == 3


def test_using_expensive_resource_2(expensive_resource):
    """Second test using same expensive resource"""
    assert 1 in expensive_resource["data"]


# ============================================================================
# 6. MARKERS FOR TEST ORGANIZATION
# ============================================================================

@pytest.mark.slow
def test_slow_operation():
    """Test marked as slow - can skip with: pytest -m 'not slow'"""
    import time
    time.sleep(0.1)
    assert True


@pytest.mark.skip(reason="Not implemented yet")
def test_not_implemented():
    """This test will be skipped"""
    pass


@pytest.mark.xfail(reason="Known issue to be fixed")
def test_known_failure():
    """Test expected to fail - doesn't fail the test suite"""
    assert False


# ============================================================================
# 7. ASYNC TESTS
# ============================================================================

import asyncio


async def async_add(a, b):
    """Async function"""
    await asyncio.sleep(0.01)
    return a + b


@pytest.mark.asyncio
async def test_async_add():
    """Test async function"""
    result = await async_add(5, 3)
    assert result == 8


# ============================================================================
# 8. SETUP AND TEARDOWN
# ============================================================================

def setup_function():
    """Runs before each test function"""
    print("\n[Setup] Before test")


def teardown_function():
    """Runs after each test function"""
    print("\n[Teardown] After test")


def test_with_setup_teardown_1():
    """First test with setup/teardown"""
    assert True


def test_with_setup_teardown_2():
    """Second test with setup/teardown"""
    assert True
