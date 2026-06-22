"""
Mathsquiz package — fixed and refactored implementation.
Reverse engineered from martinpeck/broken-python/mathsquiz.
"""

__version__ = "1.0.0"

from mathsquiz.quiz import run_quiz, ask_question, welcome_message, print_final_scores

__all__ = ["run_quiz", "ask_question", "welcome_message", "print_final_scores"]
