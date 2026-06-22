"""
Fixed and refactored mathsquiz implementation.
Corrects all bugs found in the original mathsquiz.py.
"""

QUESTIONS = [
    ("What is 8 x 7", 56),
    ("What is 4 x 9", 36),
    ("What is 12 x 6", 72),
    ("What is 6 x 8", 48),
    ("What is 7 x 7", 49),
    ("What is 11 x 6", 66),
    ("What is 3 x 9", 27),
    ("What is 5 x 8", 40),
    ("What is 9 x 9", 81),
    ("What is 7 x 6", 42),
]


def welcome_message() -> None:
    """Print welcome message to the player."""
    print("Hello! I'm going to ask you 10 maths questions.")
    print("Let's see how many you can get right!")


def ask_question(number: int, question: str, correct_answer: int) -> bool:
    """
    Ask a single question and return whether the answer was correct.

    Args:
        number: The question number to display.
        question: The question text to display.
        correct_answer: The expected correct answer.

    Returns:
        True if the answer was correct, False otherwise.
    """
    print(f"Question {number}:")
    print(question)
    try:
        answer = int(input("Answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

    if answer == correct_answer:
        print("Correct!")
        return True
    print(f"Wrong! The answer was {correct_answer}.")
    return False


def print_final_scores(score: int, total: int) -> None:
    """
    Print the final score and a message based on performance.

    Args:
        score: Number of correct answers.
        total: Total number of questions.
    """
    print(f"That's all the questions done. So...what was your score...?")
    print(f"You scored {score} points out of a possible {total}.")

    if score < 5:
        print("You need to practice your maths!")
    elif score < 8:
        print("That's pretty good!")
    elif score == total:
        print("Wow! What a maths star you are!! I'm impressed!")
    else:
        print("So close to a perfect score!")


def run_quiz() -> int:
    """
    Run the full maths quiz and return the final score.

    Returns:
        The number of correct answers.
    """
    welcome_message()
    score = 0

    for i, (question, answer) in enumerate(QUESTIONS, start=1):
        if ask_question(i, question, answer):
            score += 1

    print_final_scores(score, len(QUESTIONS))
    return score


if __name__ == "__main__":
    run_quiz()
    