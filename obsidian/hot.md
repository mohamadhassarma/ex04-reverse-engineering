# Hot — Bug Investigation Focus Page

## Target File
`mathsquiz.py` — identified by Grphify as directly connected to
`Objective: Fix Bugs in mathsquiz.py`

## Why This File
The knowledge graph flagged this file without us reading a single line of code.
It has the lowest cohesion in its community and is connected to the bug objective node.

## Bugs Identified (by graph-guided agent)

### Bug 1 — Python 2 Print Syntax
- **Location:** Lines 2-3
- **Problem:** `print "Hello"` is Python 2 syntax, fails in Python 3
- **Fix:** `print("Hello")`

### Bug 2 — Assignment Instead of Comparison
- **Location:** Every `if answer =` line
- **Problem:** `=` is assignment, not comparison. Should be `==`
- **Fix:** `if answer == 56:`

### Bug 3 — Wrong Answers
- **Location:** Every question's expected answer
- **Problem:** 8x7=55, 4x9=49, 12x6=126, 6x8=668, 7x7=77, 11x6=60
- **Fix:** 56, 36, 72, 48, 49, 66

### Bug 4 — Wrong Question Numbering
- **Location:** Every question header
- **Problem:** Every question prints "Question 1:"
- **Fix:** Increment question number each time

### Bug 5 — Score Never Incremented
- **Location:** Inside every correct answer block
- **Problem:** `score = 0` is set but never increased on correct answer
- **Fix:** Add `score += 1` inside every `if answer == X:` block

### Bug 6 — Wrong Elif Syntax
- **Location:** Final score display block
- **Problem:** `else if` is not valid Python, should be `elif`
- **Fix:** `elif score < 8:`

### Bug 7 — Only 6 Questions
- **Location:** Whole file
- **Problem:** README says 10 questions but only 6 are implemented
- **Fix:** Add 4 more questions

### Bug 8 — Answer Not Cast to Integer
- **Location:** Every `if answer ==` line
- **Problem:** `input()` returns a string, comparing to int always fails
- **Fix:** `answer = int(input("Answer: "))`

## Root Cause Summary
The file was written in Python 2 style and never properly tested.
The core issue is that no answer can ever be marked correct because:
1. `input()` returns a string
2. `=` is used instead of `==`
This means `score` is always 0 regardless of user answers.

## Links
- [[index]] — back to vault index
- [[mathsquiz]] — full file analysis
- [[bug_report]] — fix and before/after proof
