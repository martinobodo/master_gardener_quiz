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