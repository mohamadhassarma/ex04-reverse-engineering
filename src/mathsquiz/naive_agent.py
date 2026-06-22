"""
Naive agent for token comparison baseline.
Reads ALL files blindly without graph guidance.
This is what we compare against to prove token efficiency.
"""

import time
from pathlib import Path

from anthropic import Anthropic

CODE_DIR = Path("data/broken-python/mathsquiz")

CODE_FILES = [
    "mathsquiz.py",
    "mathsquiz-step1.py",
    "mathsquiz-step2.py",
    "mathsquiz-step3.py",
]


def read_all_files() -> tuple[str, int]:
    """
    Read all code files blindly without any graph guidance.

    Returns:
        Tuple of combined content string and file count.
    """
    combined = ""
    count = 0
    for filename in CODE_FILES:
        path = CODE_DIR / filename
        if path.exists():
            combined += f"\n\n=== {filename} ===\n"
            combined += path.read_text(encoding="utf-8")
            count += 1
    return combined, count


def run_naive_agent() -> dict:
    """
    Run the naive agent and return results with metrics.

    Returns:
        Dictionary with bugs found, tokens used, and performance metrics.
    """
    print("\n=== NAIVE AGENT STARTING ===")
    start = time.time()

    client = Anthropic()
    all_code, files_read = read_all_files()

    prompt = f"""You are a bug analysis agent.
Here is the entire codebase. Find all bugs in mathsquiz.py.

{all_code}

List all bugs found. For each: bug number, location, problem, fix."""

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}],
    )

    elapsed = time.time() - start
    tokens = response.usage.input_tokens + response.usage.output_tokens

    print(f"Files read: {files_read}")
    print(f"Tokens used: {tokens}")
    print(f"Time: {elapsed:.2f}s")
    print(f"\nBugs found:\n{response.content[0].text}")

    return {
        "tokens_used": tokens,
        "files_read": files_read,
        "iterations": 1,
        "elapsed": elapsed,
        "report": response.content[0].text,
    }


if __name__ == "__main__":
    run_naive_agent()
