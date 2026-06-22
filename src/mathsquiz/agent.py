"""
Agent nodes and state for graph-guided bug detection.
Each node performs one focused step in the workflow.
"""

import json
from pathlib import Path
from typing import TypedDict

from anthropic import Anthropic

GRAPH_PATH = Path("artifacts/graphify-out/graph.json")
OBSIDIAN_PATH = Path("obsidian")
CODE_PATH = Path("data/broken-python/mathsquiz/mathsquiz.py")


class AgentState(TypedDict):
    """State tracked throughout the agent workflow."""
    messages: list
    graph_context: str
    index_context: str
    hot_context: str
    code_context: str
    bugs_found: list
    tokens_used: int
    files_read: int
    iterations: int
    final_report: str


def load_graph(state: AgentState) -> AgentState:
    """Step 1: Load Grphify knowledge graph instead of raw code."""
    with open(GRAPH_PATH) as f:
        graph_data = json.load(f)
    nodes = [n.get("id", "") for n in graph_data.get("nodes", [])]
    edges = [
        f"{e.get('source')} --{e.get('relation')}--> {e.get('target')}"
        for e in graph_data.get("edges", [])
    ]
    state["graph_context"] = "Nodes: " + ", ".join(nodes) + "\nEdges:\n" + "\n".join(edges)
    state["files_read"] = 0
    state["tokens_used"] = 0
    state["iterations"] = 1
    state["bugs_found"] = []
    return state


def read_obsidian_index(state: AgentState) -> AgentState:
    """Step 2: Read index.md to understand system architecture."""
    state["index_context"] = (OBSIDIAN_PATH / "index.md").read_text(encoding="utf-8")
    state["files_read"] += 1
    state["iterations"] += 1
    return state


def read_obsidian_hot(state: AgentState) -> AgentState:
    """Step 3: Read hot.md to focus on the bug area."""
    state["hot_context"] = (OBSIDIAN_PATH / "hot.md").read_text(encoding="utf-8")
    state["files_read"] += 1
    state["iterations"] += 1
    return state


def read_target_code(state: AgentState) -> AgentState:
    """Step 4: Read only the file flagged by the graph."""
    state["code_context"] = CODE_PATH.read_text(encoding="utf-8")
    state["files_read"] += 1
    state["iterations"] += 1
    return state


def analyze_bugs(state: AgentState) -> AgentState:
    """Step 5: Use Claude to analyze bugs with pre-filtered context."""
    client = Anthropic()
    prompt = f"""You are a bug analysis agent with graph-guided context.

KNOWLEDGE GRAPH:
{state['graph_context']}

SYSTEM INDEX:
{state['index_context']}

HOT ZONE:
{state['hot_context']}

TARGET CODE:
{state['code_context']}

List all bugs in mathsquiz.py. For each: bug number, location, problem, fix."""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )
    state["final_report"] = response.content[0].text
    state["tokens_used"] += response.usage.input_tokens + response.usage.output_tokens
    state["iterations"] += 1
    return state
