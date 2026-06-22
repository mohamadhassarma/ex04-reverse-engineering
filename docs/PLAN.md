# PLAN — Architecture & Planning

## System Architecture

The project analyzes `martinpeck/broken-python/mathsquiz` using a 
graph-guided approach.

### C4 Model — Context Level
- **User** runs the LangGraph agent
- **Agent** queries the Grphify knowledge graph
- **Graph** was generated from the mathsquiz Python codebase
- **Obsidian vault** stores structured findings and navigation pages

### Component Flow
mathsquiz source code

↓

Grphify

↓

graph.json + GRAPH_REPORT.md

↓

Obsidian vault (index.md, hot.md)

↓

LangGraph Agent

↓

Bug found → Fix applied → Before/After proof
## Architectural Decisions
- **LangGraph over CrewAI**: better control over LLM call count,
  important for token efficiency proof
- **broken-python over BugsInPy**: no complex environment setup,
  focus stays on the graph workflow
- **mathsquiz over polygons**: polygons folder is empty

## Key Components to Build
1. Grphify graph generation pipeline
2. Obsidian vault with linked markdown pages
3. LangGraph agent with graph-first navigation
4. Naive baseline agent for token comparison
5. Token comparison report
6. Fixed and tested mathsquiz code

## ADR — Agent Design
The agent must query graph.json and Obsidian pages FIRST,
then request specific code snippets only when needed.
This is the core token-saving mechanism being demonstrated.
