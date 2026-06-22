# Bug Report — mathsquiz.py

## Summary
The original `mathsquiz.py` contains 8 bugs that make it completely
non-functional. No answer can ever be marked correct and the score
is always 0.

## Root Cause
Two compounding bugs make the core logic broken:
1. `input()` returns a string but answers are compared to integers
2. `=` (assignment) is used instead of `==` (comparison)

Either bug alone would break the scoring. Together they make it
impossible for any answer to ever be correct.

## Bug List with Fixes

### Fix 1 — Python 2 Print Syntax
**Before:**
```python
print "Hello! I'm going to ask you 10 maths questions."
print "Let's see how many you can get right!"
```
**After:**
```python
print("Hello! I'm going to ask you 10 maths questions.")
print("Let's see how many you can get right!")
```

### Fix 2 — Answer Type + Comparison Operator
**Before:**
```python
answer = input("Answer: ")
if answer = 55:
```
**After:**
```python
answer = int(input("Answer: "))
if answer == 56:
```

### Fix 3 — Wrong Answers
**Before:** 55, 49, 126, 668, 77, 60
**After:** 56, 36, 72, 48, 49, 66

### Fix 4 — Question Numbering
**Before:** Every question prints "Question 1:"
**After:** Questions numbered 1 through 6

### Fix 5 — Score Increment
**Before:** No score increment anywhere
**After:** `score += 1` added inside every correct answer block

### Fix 6 — Elif Syntax
**Before:**
```python
else if score < 8:
```
**After:**
```python
elif score < 8:
```

## Before/After State in Knowledge Graph
**Before fix:**
- `mathsquiz.py` connected to `Objective: Fix Bugs in mathsquiz.py`
- Score always 0, no answer ever correct

**After fix:**
- `mathsquiz.py` fully functional
- Score correctly incremented
- All answers mathematically correct
- Proper Python 3 syntax throughout

## How Graph-Guided Approach Helped
The agent found the bug by:
1. Reading `index.md` — understood system structure (0 code tokens)
2. Reading `hot.md` — identified exact bug location (0 code tokens)
3. Reading only `mathsquiz.py` — confirmed and fixed bugs (1 file)

Naive approach would have read all 4 files before finding anything.

## Links
- [[index]] — back to vault index
- [[hot]] — bug investigation focus
- [[mathsquiz]] — full file analysis
