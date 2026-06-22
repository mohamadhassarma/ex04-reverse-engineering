"""
Tests for agent, naive_agent and runner modules.
Uses mocks to avoid real API calls during testing.
"""

from unittest.mock import patch, MagicMock
import pytest
from mathsquiz.agent import (
    load_graph,
    read_obsidian_index,
    read_obsidian_hot,
    read_target_code,
    analyze_bugs,
    AgentState,
)
from mathsquiz.naive_agent import read_all_files, run_naive_agent


def make_state() -> AgentState:
    """Create a blank agent state for testing."""
    return {
        "messages": [],
        "graph_context": "",
        "index_context": "",
        "hot_context": "",
        "code_context": "",
        "bugs_found": [],
        "tokens_used": 0,
        "files_read": 0,
        "iterations": 0,
        "final_report": "",
    }


def test_load_graph_reads_json(tmp_path):
    """Test load_graph correctly reads and summarizes graph.json."""
    graph = {
        "nodes": [{"id": "mathsquiz.py"}, {"id": "Objective: Fix Bugs"}],
        "edges": [{"source": "mathsquiz.py", "relation": "targets", "target": "Objective: Fix Bugs"}],
    }
    import json
    graph_file = tmp_path / "graph.json"
    graph_file.write_text(json.dumps(graph))

    state = make_state()
    with patch("mathsquiz.agent.GRAPH_PATH", graph_file):
        result = load_graph(state)

    assert "mathsquiz.py" in result["graph_context"]
    assert result["iterations"] == 1
    assert result["files_read"] == 0


def test_read_obsidian_index(tmp_path):
    """Test read_obsidian_index reads index.md correctly."""
    index = tmp_path / "index.md"
    index.write_text("# Index\nSystem overview here.")

    state = make_state()
    with patch("mathsquiz.agent.OBSIDIAN_PATH", tmp_path):
        result = read_obsidian_index(state)

    assert "System overview" in result["index_context"]
    assert result["files_read"] == 1


def test_read_obsidian_hot(tmp_path):
    """Test read_obsidian_hot reads hot.md correctly."""
    hot = tmp_path / "hot.md"
    hot.write_text("# Hot\nBug is here.")

    state = make_state()
    with patch("mathsquiz.agent.OBSIDIAN_PATH", tmp_path):
        result = read_obsidian_hot(state)

    assert "Bug is here" in result["hot_context"]
    assert result["files_read"] == 1


def test_read_target_code(tmp_path):
    """Test read_target_code reads mathsquiz.py correctly."""
    code = tmp_path / "mathsquiz.py"
    code.write_text("print 'Hello'")

    state = make_state()
    with patch("mathsquiz.agent.CODE_PATH", code):
        result = read_target_code(state)

    assert "print 'Hello'" in result["code_context"]
    assert result["files_read"] == 1


def test_analyze_bugs_calls_claude():
    """Test analyze_bugs calls Anthropic and updates state."""
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Bug 1: print syntax")]
    mock_response.usage.input_tokens = 100
    mock_response.usage.output_tokens = 50

    state = make_state()
    state["graph_context"] = "nodes: mathsquiz.py"
    state["index_context"] = "# Index"
    state["hot_context"] = "# Hot"
    state["code_context"] = "print 'Hello'"

    with patch("mathsquiz.agent.Anthropic") as mock_anthropic:
        mock_anthropic.return_value.messages.create.return_value = mock_response
        result = analyze_bugs(state)

    assert "Bug 1" in result["final_report"]
    assert result["tokens_used"] == 150


def test_read_all_files_returns_content(tmp_path):
    """Test naive agent reads all code files."""
    (tmp_path / "mathsquiz.py").write_text("print 'Hello'")
    (tmp_path / "mathsquiz-step1.py").write_text("print('Hello')")
    (tmp_path / "mathsquiz-step2.py").write_text("def run(): pass")
    (tmp_path / "mathsquiz-step3.py").write_text("def run(): pass")

    with patch("mathsquiz.naive_agent.CODE_DIR", tmp_path):
        content, count = read_all_files()

    assert count == 4
    assert "mathsquiz.py" in content


def test_run_naive_agent_calls_claude():
    """Test naive agent calls Anthropic and returns metrics."""
    mock_response = MagicMock()
    mock_response.content = [MagicMock(text="Bug 1: syntax error")]
    mock_response.usage.input_tokens = 200
    mock_response.usage.output_tokens = 100

    with patch("mathsquiz.naive_agent.Anthropic") as mock_anthropic, \
         patch("mathsquiz.naive_agent.read_all_files", return_value=("code", 4)):
        mock_anthropic.return_value.messages.create.return_value = mock_response
        result = run_naive_agent()

    assert result["tokens_used"] == 300
    assert result["files_read"] == 4
    