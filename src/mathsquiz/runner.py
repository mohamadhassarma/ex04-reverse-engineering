"""
LangGraph workflow builder and runner for graph-guided agent.
Imports nodes from agent.py and compiles the workflow.
"""

import time
from anthropic import Anthropic
from langgraph.graph import StateGraph, END

from mathsquiz.agent import (
    AgentState,
    load_graph,
    read_obsidian_index,
    read_obsidian_hot,
    read_target_code,
    analyze_bugs,
)


def build_graph_agent():
    """Build and compile the graph-guided LangGraph workflow."""
    workflow = StateGraph(AgentState)

    workflow.add_node("load_graph", load_graph)
    workflow.add_node("read_index", read_obsidian_index)
    workflow.add_node("read_hot", read_obsidian_hot)
    workflow.add_node("read_code", read_target_code)
    workflow.add_node("analyze", analyze_bugs)

    workflow.set_entry_point("load_graph")
    workflow.add_edge("load_graph", "read_index")
    workflow.add_edge("read_index", "read_hot")
    workflow.add_edge("read_hot", "read_code")
    workflow.add_edge("read_code", "analyze")
    workflow.add_edge("analyze", END)

    return workflow.compile()


def run_graph_agent() -> dict:
    """
    Run the graph-guided agent and return results with metrics.

    Returns:
        Dictionary with bugs found, tokens used, and performance metrics.
    """
    print("\n=== GRAPH-GUIDED AGENT STARTING ===")
    start = time.time()

    agent = build_graph_agent()
    initial_state: AgentState = {
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

    result = agent.invoke(initial_state)
    elapsed = time.time() - start

    print(f"Files read: {result['files_read']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Tokens used: {result['tokens_used']}")
    print(f"Time: {elapsed:.2f}s")
    print(f"\nBugs found:\n{result['final_report']}")

    return {
        "tokens_used": result["tokens_used"],
        "files_read": result["files_read"],
        "iterations": result["iterations"],
        "elapsed": elapsed,
        "report": result["final_report"],
    }


if __name__ == "__main__":
    run_graph_agent()
    