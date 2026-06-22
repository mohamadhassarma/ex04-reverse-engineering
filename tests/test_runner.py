"""
Tests for runner module — LangGraph workflow builder and runner.
Uses mocks to avoid real API calls during testing.
"""

from unittest.mock import patch, MagicMock
import pytest


def test_build_graph_agent_returns_compiled():
    """Test build_graph_agent returns a compiled workflow."""
    from mathsquiz.runner import build_graph_agent
    agent = build_graph_agent()
    assert agent is not None


def test_run_graph_agent_returns_metrics():
    """Test run_graph_agent returns correct metrics dictionary."""
    from mathsquiz.runner import run_graph_agent

    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Bug 1: syntax error")]
    mock_response.usage.input_tokens = 100
    mock_response.usage.output_tokens = 50

    with patch("mathsquiz.agent.Anthropic") as mock_anthropic:
        mock_anthropic.return_value.messages.create.return_value = mock_response
        result = run_graph_agent()

    assert "tokens_used" in result
    assert "files_read" in result
    assert "report" in result
    