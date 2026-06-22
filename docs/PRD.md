# PRD — EX04 Reverse Engineering with Grphify and Obsidian

## Project Overview
Reverse engineer the `martinpeck/broken-python` mathsquiz codebase using 
Grphify for graph generation and Obsidian for knowledge documentation. 
Build a LangGraph AI agent that navigates the knowledge graph to find and 
fix bugs in a token-efficient way.

## Why This Repo
`broken-python/mathsquiz` was chosen because it is small, self-contained, 
and contains multiple intentional bugs — making it ideal for demonstrating 
the full reverse engineering and graph-guided debugging workflow without 
environment complexity.

## Research Questions
- What is the actual architecture of the project?
- Which components are most central to the system?
- Where are the God Nodes or areas of mixed responsibility?
- How was the bug identified and what is the root cause?
- How does graph-guided navigation save tokens vs. naive file reading?
- What is the value of Grphify and Obsidian throughout the process?

## Functional Requirements
- Generate knowledge graph from mathsquiz using Grphify
- Build Obsidian vault with index.md, hot.md, and linked pages
- Build LangGraph agent that queries graph before reading raw code
- Fix at least one real bug with before/after proof
- Compare token usage: naive vs. graph-guided

## Non-Functional Requirements
- uv as the only package manager
- 85%+ test coverage
- Zero Ruff linter errors
- No hardcoded secrets
- All files under 150 lines

## Success Criteria
- Agent finds bug using graph context, not raw file reading
- Token comparison shows measurable savings
- Obsidian vault is navigable and properly linked
- README contains all required sections and visuals
