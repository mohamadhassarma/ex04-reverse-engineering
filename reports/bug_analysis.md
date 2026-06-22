# Bug Analysis Report — mathsquiz.py

## Repository
`martinpeck/broken-python` — mathsquiz module
Chosen because it contains multiple intentional bugs in a small,
self-contained Python script. Perfect for demonstrating graph-guided
debugging without environment complexity.

## Bug Summary
8 distinct bugs found, all in `mathsquiz.py`.
The file is completely non-functional as written — no answer can
ever be marked correct and the score is always 0.

## Root Cause
Two compounding bugs make the core logic broken:
1. `input()` returns a string but answers compared to integers
2. `=` (assignment) used instead of `==` (comparison)

Either bug alone would break scoring. Together they make it
impossible for any answer to ever be correct.

## Complete Bug List

### Bug 1 — Python 2 Print Syntax
- **Location:** Lines 2-3
- **Problem:** `print "Hello"` is Python 2 syntax, fails in Python 3
- **Fix:** `print("Hello! I'm going to ask you 10 maths questions.")`

### Bug 2 — Assignment Instead of Comparison
- **Location:** Every if statement (lines 12, 22, 32, 42, 52, 62)
- **Problem:** `if answer = 55` uses `=` not `==`
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
- **Problem:** score = 0 set but never increased
- **Fix:** Add `score += 1` inside every correct answer block

### Bug 6 — Invalid Elif Syntax
- **Location:** Lines 78-79
- **Problem:** `else if` is not valid Python
- **Fix:** `elif score < 8:`

### Bug 7 — Only 6 Questions
- **Location:** Whole file
- **Problem:** README says 10 questions, only 6 implemented
- **Fix:** Add 4 more questions

### Bug 8 — Answer Not Cast to Integer
- **Location:** Every input line
- **Problem:** `input()` returns string, compared to int — always fails
- **Fix:** `answer = int(input("Answer: "))`

## How the Graph Helped
Grphify connected `mathsquiz.py` directly to
`Objective: Fix Bugs in mathsquiz.py` without us reading any code.
This immediately told the agent where to look.

The agent then read `hot.md` which had the bug list pre-documented,
meaning the LLM received focused context instead of raw noisy code.

## Before Fix
- Score always 0
- No answer ever marked correct
- Python 2 syntax causes immediate crash in Python 3

## After Fix
- All 10 questions work correctly
- Score properly incremented
- Proper Python 3 syntax throughout
- Correct mathematical answers
- Proper elif syntax
