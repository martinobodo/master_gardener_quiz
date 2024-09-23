"""
This module contains the logic for running an interactive quiz game.
It includes functions for managing a leaderboard and displaying questions.
"""

import random
import os
import pyfiglet
from termcolor import colored
from questions import QUESTIONS
# Assuming QUESTIONS is imported from questions.py

QUIZ_LENGTHS = [10, 20, 50, 100]


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")

def display_welcome_message():
    """
    Display a welcome message and instructions for the quiz.
    """
    text = pyfiglet.figlet_format("Silly but Serious", font="cybermedium")
    print(text)
    print(colored(
        "\n===== Welcome to the Silly but Serious Quiz! =====", "cyan"
    ))
    print(colored("\nHow to play:", "yellow"))
    print("1. Choose the number of questions you want to answer.")
    print(
        "2. For each question, enter the letter (A, B, C, or D) "
        "corresponding to your answer."
    )
    print(
        "3. After each question, you'll see if you were correct and "
        "your current score."
    )
    print("4. Have fun and test your knowledge across various categories!")
    print(colored("\nLet's begin!", "green"))

    # Ensure only Enter key is pressed
    while True:
        user_input = input("Press Enter to start...")
        if user_input == "":
            break
        else:
            print(colored("Please press Enter only.", "red"))
    clear()

def get_quiz_length():
    """Prompt the user to choose the number of questions for the quiz."""
    while True:
        try:
            print("\nChoose the number of questions:")
            for i, length in enumerate(QUIZ_LENGTHS, 1):
                print(f"{i}. {length} questions")
            choice = int(input("Enter your choice (1-4): "))
            clear()
            if 1 <= choice <= 4:
                return QUIZ_LENGTHS[choice - 1]
            print(
                colored(
                    f"{choice} is an invalid choice. "
                    "Enter a number between 1 and 4.",
                    "red"
                )
            )
        except ValueError:
            print(colored("Invalid input. Please enter a number.", "red"))