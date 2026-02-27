"""
Mocking and Patching Examples

Demonstrates mocking LLM calls, API calls, and external tools.

Run tests with:
    uv add --dev pytest
    uv add --dev pytest-mock
    uv run pytest test_mocking.py -v
"""

import pytest
from unittest.mock import Mock, patch, MagicMock, call
from typing import Optional


# ============================================================================
# EXAMPLE: Agent that uses an LLM and Tools
# ============================================================================

class LLMClient:
    """Simulated LLM client"""
    def __init__(self, model: str):
        self.model = model
    
    def generate(self, prompt: str) -> str:
        """Generate response from LLM"""
        # In reality, this would call OpenAI, Ollama, etc.
        raise NotImplementedError("Must be mocked in tests")


class Tool:
    """Base tool class"""
    def execute(self, args: dict) -> any:
        raise NotImplementedError


class SearchTool(Tool):
    """Search tool - simulated"""
    def execute(self, args: dict) -> str:
        # In reality, this would search DuckDuckGo, etc.
        raise NotImplementedError


class Agent:
    """Simple agent that uses LLM and tools"""
    def __init__(self, llm: LLMClient, tools: dict[str, Tool]):
        self.llm = llm
        self.tools = tools
    
    def run(self, prompt: str) -> str:
        """Run agent"""
        response = self.llm.generate(prompt)
        if "search:" in response:
            search_query = response.replace("search:", "").strip()
            search_result = self.tools["search"].execute({"query": search_query})
            return f"Search result: {search_result}"
        return response


# ============================================================================
# 1. BASIC MOCKING
# ============================================================================

def test_agent_uses_llm_basic():
    """Test agent calls LLM"""
    # Create mock LLM
    mock_llm = Mock(spec=LLMClient)
    mock_llm.generate.return_value = "Hello, I'm an agent"
    
    # Create mock tool
    mock_search = Mock(spec=SearchTool)
    
    # Create agent with mocks
    agent = Agent(mock_llm, {"search": mock_search})
    result = agent.run("What is AI?")
    
    # Verify LLM was called
    mock_llm.generate.assert_called_once_with("What is AI?")
    assert result == "Hello, I'm an agent"


# ============================================================================
# 2. VERIFY MOCK WAS CALLED CORRECTLY
# ============================================================================

def test_verify_mock_calls():
    """Verify how mocks were called"""
    mock_llm = Mock()
    
    # Call mock multiple times
    mock_llm.generate("prompt1")
    mock_llm.generate("prompt2")
    mock_llm.generate("prompt2")
    
    # Verify
    assert mock_llm.generate.call_count == 3
    
    # Check specific calls
    mock_llm.generate.assert_any_call("prompt1")
    mock_llm.generate.assert_any_call("prompt2")
    
    # Check call order
    expected_calls = [
        call("prompt1"),
        call("prompt2"),
        call("prompt2"),
    ]
    mock_llm.generate.assert_has_calls(expected_calls)


# ============================================================================
# 3. MOCK WITH SIDE EFFECTS
# ============================================================================

def test_agent_searches_when_needed():
    """Test that agent uses search tool when needed"""
    mock_llm = Mock(spec=LLMClient)
    mock_llm.generate.return_value = "search: python programming"
    
    mock_search = Mock(spec=SearchTool)
    mock_search.execute.return_value = "Python is a programming language"
    
    agent = Agent(mock_llm, {"search": mock_search})
    result = agent.run("How do I learn Python?")
    
    # Verify search was called
    mock_search.execute.assert_called_once_with({"query": "python programming"})
    assert "Python is a programming language" in result


# ============================================================================
# 4. MOCK SIDE EFFECTS (EXCEPTIONS)
# ============================================================================

def test_llm_failure_handling():
    """Test handling of LLM failures"""
    mock_llm = Mock(spec=LLMClient)
    mock_llm.generate.side_effect = RuntimeError("API timeout")
    
    agent = Agent(mock_llm, {})
    
    # Verify exception is raised
    with pytest.raises(RuntimeError, match="API timeout"):
        agent.run("prompt")


# ============================================================================
# 5. USING PATCH DECORATOR
# ============================================================================

@patch("test_mocking.LLMClient.generate")
def test_with_patch_decorator(mock_generate):
    """Test using @patch decorator"""
    mock_generate.return_value = "Mocked response"
    
    # Use the class normally
    llm = LLMClient("gpt-4")
    result = llm.generate("test")
    
    assert result == "Mocked response"
    mock_generate.assert_called_once()


# ============================================================================
# 6. CONTEXT MANAGER PATCHING
# ============================================================================

def test_with_patch_context_manager():
    """Test using context manager for patching"""
    with patch("test_mocking.LLMClient.generate") as mock_generate:
        mock_generate.return_value = "Patched"
        
        llm = LLMClient("gpt-4")
        result = llm.generate("test")
        
        assert result == "Patched"
        mock_generate.assert_called_once()


# ============================================================================
# 7. MOCKER FIXTURE (pytest-mock)
# ============================================================================

def test_with_mocker_fixture(mocker):
    """Test using pytest-mock's mocker fixture"""
    # Mock is automatically cleaned up after test
    mock_generate = mocker.patch(
        "test_mocking.LLMClient.generate",
        return_value="Mocked by pytest-mock"
    )
    
    llm = LLMClient("gpt-4")
    result = llm.generate("test")
    
    assert result == "Mocked by pytest-mock"


# ============================================================================
# 8. PARTIAL MOCKING (MagicMock)
# ============================================================================

def test_partial_mock():
    """Use MagicMock for more complex mocking"""
    # MagicMock returns MagicMock for undefined attributes
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": "success"}
    
    assert mock_response.status_code == 200
    assert mock_response.json() == {"result": "success"}


# ============================================================================
# 9. FIXTURE WITH MOCK
# ============================================================================

@pytest.fixture
def mock_llm():
    """Fixture that provides a mocked LLM"""
    mock = Mock(spec=LLMClient)
    mock.generate.return_value = "Mocked response"
    return mock


@pytest.fixture
def mock_tools():
    """Fixture that provides mocked tools"""
    return {
        "search": Mock(spec=SearchTool)
    }


@pytest.fixture
def agent_with_mocks(mock_llm, mock_tools):
    """Agent fixture with mocked dependencies"""
    return Agent(mock_llm, mock_tools)


def test_agent_with_fixtures(agent_with_mocks, mock_llm):
    """Test using agent with mocked fixtures"""
    result = agent_with_mocks.run("test prompt")
    mock_llm.generate.assert_called_once_with("test prompt")
    assert result == "Mocked response"


# ============================================================================
# 10. REAL-WORLD EXAMPLE: Testing Agent with LLM
# ============================================================================

class RealWorldAgent:
    """More realistic agent implementation"""
    def __init__(self, llm: LLMClient, max_iterations: int = 3):
        self.llm = llm
        self.max_iterations = max_iterations
        self.iteration = 0
    
    def run(self, prompt: str) -> str:
        """Run agent with iteration limit"""
        self.iteration = 0
        
        for _ in range(self.max_iterations):
            self.iteration += 1
            response = self.llm.generate(prompt)
            
            if response.startswith("DONE:"):
                return response.replace("DONE:", "").strip()
        
        return f"Failed after {self.max_iterations} iterations"


def test_real_world_agent(mocker):
    """Test realistic agent behavior"""
    # Mock LLM with sequence of responses
    mock_llm = mocker.Mock(spec=LLMClient)
    mock_llm.generate.side_effect = [
        "Thinking...",
        "Still thinking...",
        "DONE: Final answer"
    ]
    
    agent = RealWorldAgent(mock_llm, max_iterations=5)
    result = agent.run("Complex question")
    
    # Verify
    assert result == "Final answer"
    assert mock_llm.generate.call_count == 3
    assert agent.iteration == 3
