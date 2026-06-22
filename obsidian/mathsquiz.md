# mathsquiz.py — File Analysis

## Overview
The original buggy Python maths quiz script. Entry point of the application.
Identified by Grphify as the primary bug target node.

## Architecture
This file has NO functions, NO classes — it is purely procedural/linear code.
All logic is written sequentially from top to bottom.

## OOP Analysis
- No classes defined
- No inheritance
- No composition
- No encapsulation
- All variables are global scope
- This is a flat script, not object-oriented

## Block Diagram
START

↓

Print welcome message

↓

Set score = 0

↓

Question 1 → input → check answer → (score never updates)

↓

Question 2 → input → check answer → (score never updates)

↓

... (6 questions total, should be 10)

↓

Print final score

↓

Print message based on score (broken elif)

↓

END
## Key Variables
| Variable | Type | Purpose | Issue |
|----------|------|---------|-------|
| `score` | int | Tracks correct answers | Never incremented |
| `answer` | str | Stores user input | Never cast to int |

## Key Issues Found
1. Python 2 print syntax on lines 2-3
2. `=` instead of `==` in all comparisons
3. All answers are mathematically wrong
4. `input()` returns string, never cast to int
5. Score never incremented on correct answer
6. `else if` instead of `elif`
7. Only 6 questions instead of 10
8. All questions labeled "Question 1:"

## Relationship to Other Files
- `mathsquiz-step1.py` — fixes the syntax errors
- `mathsquiz-step2.py` — refactors into functions
- `mathsquiz-step3.py` — adds user input for times table choice

## Links
- [[index]] — back to vault index
- [[hot]] — bug investigation focus
- [[bug_report]] — fix and proof
