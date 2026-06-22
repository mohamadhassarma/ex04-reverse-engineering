"""
Tests for mathsquiz.quiz module.
Covers all public functions with valid, invalid and edge cases.
"""

from unittest.mock import patch
import pytest
from mathsquiz.quiz import (
    welcome_message,
    ask_question,
    print_final_scores,
    run_quiz,
)


def test_welcome_message_prints(capsys):
    """Test welcome message prints correctly."""
    welcome_message()
    captured = capsys.readouterr()
    assert "10 maths questions" in captured.out
    assert "how many you can get right" in captured.out


def test_ask_question_correct_answer(capsys):
    """Test ask_question returns True on correct answer."""
    with patch("builtins.input", return_value="56"):
        result = ask_question(1, "What is 8 x 7", 56)
    assert result is True
    assert "Correct" in capsys.readouterr().out


def test_ask_question_wrong_answer(capsys):
    """Test ask_question returns False on wrong answer."""
    with patch("builtins.input", return_value="99"):
        result = ask_question(1, "What is 8 x 7", 56)
    assert result is False
    assert "Wrong" in capsys.readouterr().out


def test_ask_question_invalid_input(capsys):
    """Test ask_question handles non-numeric input gracefully."""
    with patch("builtins.input", return_value="abc"):
        result = ask_question(1, "What is 8 x 7", 56)
    assert result is False
    assert "Invalid" in capsys.readouterr().out


def test_print_final_scores_low(capsys):
    """Test final score message for low score."""
    print_final_scores(3, 10)
    assert "practice" in capsys.readouterr().out


def test_print_final_scores_medium(capsys):
    """Test final score message for medium score."""
    print_final_scores(6, 10)
    assert "pretty good" in capsys.readouterr().out


def test_print_final_scores_perfect(capsys):
    """Test final score message for perfect score."""
    print_final_scores(10, 10)
    assert "maths star" in capsys.readouterr().out


def test_print_final_scores_near_perfect(capsys):
    """Test final score message for near perfect score."""
    print_final_scores(9, 10)
    assert "close" in capsys.readouterr().out


def test_run_quiz_all_correct(capsys):
    """Test run_quiz returns perfect score when all answers correct."""
    answers = ["56", "36", "72", "48", "49", "66", "27", "40", "81", "42"]
    with patch("builtins.input", side_effect=answers):
        score = run_quiz()
    assert score == 10


def test_run_quiz_all_wrong(capsys):
    """Test run_quiz returns zero when all answers wrong."""
    answers = ["0"] * 10
    with patch("builtins.input", side_effect=answers):
        score = run_quiz()
    assert score == 0


def test_run_quiz_half_correct(capsys):
    """Test run_quiz returns correct count for mixed answers."""
    answers = ["56", "0", "72", "0", "49", "0", "27", "0", "81", "0"]
    with patch("builtins.input", side_effect=answers):
        score = run_quiz()
    assert score == 5
    