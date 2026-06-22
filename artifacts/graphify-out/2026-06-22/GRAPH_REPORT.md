# Graph Report - artifacts  (2026-06-22)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 21 nodes · 21 edges · 7 communities (6 shown, 1 thin omitted)
- Extraction: 81% EXTRACTED · 19% INFERRED · 0% AMBIGUOUS · INFERRED: 4 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dd7f5de9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Refactoring with Functions|Refactoring with Functions]]
- [[_COMMUNITY_Maths Quiz Application|Maths Quiz Application]]
- [[_COMMUNITY_User Input Selection|User Input Selection]]

## God Nodes (most connected - your core abstractions)
1. `Maths Quiz Application` - 6 edges
2. `Concept: Refactoring` - 4 edges
3. `mathsquiz.py` - 3 edges
4. `Objective: Reduce Repetition with Functions` - 3 edges
5. `mathsquiz-final.py` - 2 edges
6. `Objective: Fix Bugs in mathsquiz.py` - 2 edges
7. `Objective: Use Random Numbers and Variables` - 2 edges
8. `Objective: Allow User to Choose Times Table via Input` - 2 edges
9. `Concept: Functions` - 2 edges
10. `Concept: Random Numbers` - 2 edges

## Surprising Connections (you probably didn't know these)
- `Concept: Refactoring` --conceptually_related_to--> `Concept: User Input`  [INFERRED]
  README.md → README.md  _Bridges community 0 → community 4_
- `Maths Quiz Application` --references--> `Objective: Reduce Repetition with Functions`  [EXTRACTED]
  README.md → README.md  _Bridges community 3 → community 0_
- `Maths Quiz Application` --references--> `Objective: Allow User to Choose Times Table via Input`  [EXTRACTED]
  README.md → README.md  _Bridges community 3 → community 4_

## Import Cycles
- None detected.

## Communities (7 total, 1 thin omitted)

### Community 0 - "Refactoring with Functions"
Cohesion: 0.50
Nodes (5): Concept: Functions, Concept: Random Numbers, Concept: Refactoring, Objective: Reduce Repetition with Functions, Objective: Use Random Numbers and Variables

### Community 3 - "Maths Quiz Application"
Cohesion: 0.83
Nodes (4): Maths Quiz Application, mathsquiz-final.py, mathsquiz.py, Objective: Fix Bugs in mathsquiz.py

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Maths Quiz Application` connect `Maths Quiz Application` to `Refactoring with Functions`, `User Input Selection`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Why does `Objective: Reduce Repetition with Functions` connect `Refactoring with Functions` to `Maths Quiz Application`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Why does `Concept: Refactoring` connect `Refactoring with Functions` to `User Input Selection`?**
  _High betweenness centrality (0.037) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Concept: Refactoring` (e.g. with `Concept: Functions` and `Concept: Random Numbers`) actually correct?**
  _`Concept: Refactoring` has 4 INFERRED edges - model-reasoned connections that need verification._