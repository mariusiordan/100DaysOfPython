# =====================================================================
#  main.py  -  START THE PROGRAM FROM HERE:  python3 main.py
#  ---------------------------------------------------------------------
#  Project structure:
#
#    main.py           -> Receipt, Technician, CoffeeMachine (the "boss")
#    menu.py           -> MenuItem, Menu
#    coffee_maker.py   -> CoffeeMaker   (ingredients)
#    money_machine.py  -> MoneyMachine  (coins and profit)
#    helpers.py        -> small shared functions
#
#  How the classes work together:
#
#    CoffeeMachine  HAS A  Menu
#                   HAS A  CoffeeMaker
#                   HAS A  MoneyMachine
#                   HAS A  Receipt
#                   HAS A  Technician
#
#  This "has a" idea is called COMPOSITION: one big object is built
#  from smaller objects, like a car has an engine, wheels and seats.
# =====================================================================

import getpass
import os

from coffee_maker import CoffeeMaker
from helpers import loading
from menu import Menu
from money_machine import MoneyMachine


class Receipt:
    """Remembers the drinks bought by the CURRENT customer."""

    def __init__(self):
        self.drinks = []  # a list of MenuItem objects

    def add(self, drink):
        self.drinks.append(drink)

    def print_and_reset(self):
        if not self.drinks:  # an empty list counts as False
            print("No drinks bought yet.")
            return

        print("\n=====  Receipt  =====")
        total = 0
        # -------------------------------------------------------------
        #  enumerate() gives a counter AND the item together:
        #     1 Espresso, 2 Espresso, 3 Latte ...
        #  Your old code used receipt.index(i), which always finds the
        #  FIRST match, so two espressos were both numbered "1".
        # -------------------------------------------------------------
        for number, drink in enumerate(self.drinks, start=1):
            print(f"{number}. {drink.name}: £{drink.cost / 100:.2f}")
            total += drink.cost
        print("---------------------")
        print(f"Total: £{total / 100:.2f}")
        print("=====================")

        # .clear() empties THE SAME list. Your old "receipt = []"
        # created a NEW list and broke the link with account.py.
        self.drinks.clear()


class Technician:
    """Checks the technician password."""

    def __init__(self):
        # -------------------------------------------------------------
        #  DevOps habit: secrets are NOT written in the code.
        #  os.environ.get() reads an ENVIRONMENT VARIABLE.
        #  Set it in the Linux terminal before running:
        #      export TECH_PASSWORD=mysecret
        #
        #  "admin" is only a fallback for practice - never in real jobs.
        # -------------------------------------------------------------
        self.password = os.environ.get("TECH_PASSWORD", "admin")

    def login(self):
        typed = getpass.getpass("Technician password: ")  # hidden, like Linux sudo
        if typed == self.password:
            print("Password accepted ✅")
            return True
        print("❌ Access denied.")
        return False


class CoffeeMachine:
    """The 'boss': creates all the other objects and runs the main loop."""

    def __init__(self):
        # Create ONE object from each class and keep it inside self.
        # From now on: self.maker, self.money, etc. are ready to use.
        self.menu = Menu()
        self.maker = CoffeeMaker()
        self.money = MoneyMachine()
        self.receipt = Receipt()
        self.technician = Technician()
        self.is_on = True

    def run(self):
        """The main loop - keeps going until someone types 'exit'."""
        print("Starting the coffee machine ♨️ ", end="")
        loading(5)
        while self.is_on:
            self.menu.show()
            # .strip() removes spaces, .lower() makes "EXIT" -> "exit"
            choice = input("What would you like? ").strip().lower()
            self.handle(choice)

    def handle(self, choice):
        """Decide what to do with the user's choice."""
        match choice:
            case "exit":
                print("Thank you! Turning off", end="")
                loading(3)
                self.is_on = False
            case "receipt":
                self.receipt.print_and_reset()
            case "admin":
                # -----------------------------------------------------
                #  HIDDEN command: it is NOT printed in the menu, so
                #  customers don't know it exists. Only the technician
                #  knows to type "admin".
                #
                #  Password is checked ONCE here. After that, the
                #  technician can do many jobs without logging in again.
                # -----------------------------------------------------
                if self.technician.login():
                    self.admin_menu()
            case _:
                # "_" means "anything else" - so it must be a drink name
                drink = self.menu.find_drink(choice)
                if drink is None:
                    print("❌ Invalid option, please try again.")
                else:
                    self.serve(drink)

    def serve(self, drink):
        # -------------------------------------------------------------
        #  The most important line in the project.
        #
        #  Python reads "and" from LEFT to RIGHT and stops at the
        #  first False ("short-circuit"). So:
        #    1. Check stock first.
        #    2. ONLY if stock is OK -> ask for money.
        #    3. ONLY if both are OK -> make coffee + add to receipt.
        #
        #  The customer can never pay for a drink the machine can't make.
        # -------------------------------------------------------------
        if self.maker.is_resource_sufficient(drink) and self.money.make_payment(drink.cost):
            self.maker.make_coffee(drink)
            self.receipt.add(drink)

    def admin_menu(self):
        """Technician menu - a SECOND loop inside the main loop.

        It keeps running until the technician chooses 0.
        "return" leaves this method and goes back to the customer menu.
        """
        while True:
            print("\n======  ADMIN MENU  ======")
            print("1. Report")
            print("2. Refill")
            print("3. Cash out")
            print("0. Back to customer menu")
            print("==========================")
            option = input("Choose an option: ").strip()

            match option:
                case "1":
                    self.report()
                case "2":
                    self.maker.refill()
                    self.report()
                case "3":
                    self.money.cash_out()
                case "0":
                    print("Logged out. Back to customer menu.")
                    return
                case _:
                    print("❌ Invalid option, choose 0-3.")

    def report(self):
        """Ask each object to print its OWN part of the report."""
        print("\n======  REPORT  ======")
        self.maker.report()
        self.money.report()
        print("======================")


# =====================================================================
#  This block runs ONLY when you start this file directly:
#      python3 main.py        -> runs
#      import main            -> does NOT run (useful for tests later)
# =====================================================================
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.run()