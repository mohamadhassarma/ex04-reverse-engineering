# Index — Maths Quiz Knowledge Vault

## What This Vault Is
This vault documents the reverse engineering of `martinpeck/broken-python/mathsquiz`
using Grphify and LangGraph. It serves as the navigation hub for the AI agent.

## System Overview
The mathsquiz codebase is a simple Python maths quiz application that asks 
10 multiplication questions and scores the user. It exists in 4 versions 
showing a progression from buggy to refactored code.

## File Map
| File | Purpose | Status |
|------|---------|--------|
| `mathsquiz.py` | Original buggy version | ⚠️ Contains bugs |
| `mathsquiz-step1.py` | First fix attempt | 🔧 Partial fix |
| `mathsquiz-step2.py` | Refactored with functions | ✅ Improved |
| `mathsquiz-step3.py` | Final refactored version | ✅ Best version |

## Graph Communities (from Grphify)
- **Maths Quiz Application** — core quiz logic, God Node with 6 edges
- **Refactoring with Functions** — concepts around code improvement
- **Quiz Step 2 Functions** — `ask_question()`, `print_final_scores()`, `welcome_message()`
- **Quiz Step 3 Functions** — same functions, further refined
- **User Input Selection** — user input and times table selection concepts
- **Core Quiz Script** — the original mathsquiz.py entry point

## God Node
`Maths Quiz Application` is the most connected node (6 edges).
It bridges all communities and is the conceptual center of the system.

## Navigation
- [[hot]] — focus page for bug investigation
- [[mathsquiz]] — detailed analysis of the buggy file
- [[bug_report]] — root cause analysis and fix

## Key Insight (from graph)
Grphify directly connected `mathsquiz.py` to `Objective: Fix Bugs in mathsquiz.py`
confirming it as the primary investigation target without reading any code.
