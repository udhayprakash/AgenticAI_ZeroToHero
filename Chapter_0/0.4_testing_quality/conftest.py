"""
Shared pytest fixtures and configuration

This file is automatically discovered and loaded by pytest.
It's useful for common fixtures shared across multiple test files.

Run all tests with:
    uv run pytest -v
"""

import pytest
from unittest.mock import Mock


# ============================================================================
# DATABASE FIXTURES
# ============================================================================

@pytest.fixture
def db_connection():
    """Fixture that provides a mock database connection"""
    mock_db = Mock()
    mock_db.query.return_value = [{"id": 1, "name": "test"}]
    
    yield mock_db
    
    # Cleanup
    mock_db.close()


# ============================================================================
# HTTP CLIENT FIXTURES
# ============================================================================

@pytest.fixture
def http_client():
    """Fixture for HTTP client"""
    from unittest.mock import Mock
    
    mock_client = Mock()
    mock_client.get.return_value.status_code = 200
    mock_client.get.return_value.json.return_value = {"data": "test"}
    
    return mock_client


# ============================================================================
# LLM FIXTURES
# ============================================================================

@pytest.fixture
def mock_llm():
    """Fixture for mocked LLM"""
    mock = Mock()
    mock.generate.return_value = "Generated response"
    return mock


# ============================================================================
# ENVIRONMENT FIXTURES
# ============================================================================

@pytest.fixture
def test_env(monkeypatch):
    """
    Fixture to set environment variables for testing
    
    Usage:
        def test_something(test_env):
            os.environ["TEST_VAR"] = "value"
    """
    import os
    
    def set_env(key: str, value: str):
        monkeypatch.setenv(key, value)
    
    return set_env


# ============================================================================
# PYTEST CONFIGURATION
# ============================================================================

def pytest_configure(config):
    """Configure pytest with custom markers"""
    config.addinivalue_line(
        "markers",
        "integration: mark test as an integration test"
    )
    config.addinivalue_line(
        "markers",
        "slow: mark test as slow"
    )
    config.addinivalue_line(
        "markers",
        "llm: mark test as requiring LLM (mocked)"
    )


# ============================================================================
# PYTEST HOOKS (Advanced)
# ============================================================================

def pytest_collection_modifyitems(config, items):
    """
    Automatically add markers based on test names or paths.
    
    This runs after test collection.
    """
    for item in items:
        # Mark integration tests
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        
        # Mark slow tests
        if "slow" in item.nodeid:
            item.add_marker(pytest.mark.slow)
        
        # Mark LLM tests
        if "llm" in item.nodeid:
            item.add_marker(pytest.mark.llm)
