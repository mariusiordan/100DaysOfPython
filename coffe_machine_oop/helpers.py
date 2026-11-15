# =====================================================================
#  helpers.py
#  ---------------------------------------------------------------------
#  Small functions that MORE THAN ONE file needs.
#
#  Why a separate file?
#  coffee_maker.py and money_machine.py both need ask_number().
#  If we put it inside one of them, the other would have to import it
#  from there, and the files would depend on each other in a messy way.
#  A shared "helpers" (or "utils") file is the normal solution.
#
#  These are plain FUNCTIONS, not classes, because they don't need to
#  remember any data. Not everything has to be a class in OOP.
# =====================================================================

import sys
import time


def loading(dots):
    """Print dots slowly, like: Loading....."""
    for _ in range(dots):
        time.sleep(0.4)
        print(".", end="")
        sys.stdout.flush()  # show the dot NOW, don't wait for the end of the line
    print()


def progress_bar(task, seconds=2):
    """Print a simple progress bar, like: Heating water: ██████████"""
    print(task, end="")
    for _ in range(seconds * 5):
        time.sleep(0.2)
        print("█", end="")
        sys.stdout.flush()
    print()


def ask_number(prompt):
    """Keep asking until the user types a whole number (0 or more).

    - Empty input (just Enter) counts as 0.
    - "abc" and "-5" are refused, because .isdigit() is only True
      when EVERY character is a digit 0-9.
    - The while True loop only stops at "return", so the user
      cannot escape with bad input.
    """
    while True:
        text = input(prompt).strip() or "0"
        if text.isdigit():
            return int(text)
        print("❌ Please enter a whole number (0 or more).")