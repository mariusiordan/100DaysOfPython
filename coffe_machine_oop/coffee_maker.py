# =====================================================================
#  coffee_maker.py
#  ---------------------------------------------------------------------
#  The CoffeeMaker class looks after the INGREDIENTS only.
#  It does not know about money, passwords or receipts.
#
#  This is called "single responsibility": one class = one job.
#  If the milk numbers are wrong, you know the bug is in THIS file.
# =====================================================================

# Import only the helpers this file needs, from helpers.py
from helpers import ask_number, progress_bar


class CoffeeMaker:
    """Checks, uses and refills the ingredients."""

    def __init__(self):
        # -------------------------------------------------------------
        #  self.resources belongs to THIS object.
        #  In your old version "resources" was a global variable, so
        #  ANY function could change it. Now only CoffeeMaker methods
        #  touch it.
        #
        #  Units: water and milk in ml, coffee and chocolate in g.
        # -------------------------------------------------------------
        self.resources = {"water": 1000, "milk": 500, "coffee": 200, "chocolate": 100}

    def is_resource_sufficient(self, drink):
        """Return True if there is enough of EVERY ingredient.

        "drink" is a MenuItem object, so we can read drink.ingredients.
        One object passed into another object's method - this is how
        objects work together in OOP.
        """
        for item, needed in drink.ingredients.items():
            available = self.resources[item]
            if needed > available:
                print(f"❌ Sorry, not enough {item}. Needed: {needed}, available: {available}")
                return False  # stop at the first missing ingredient
        return True

    def make_coffee(self, drink):
        """Take the ingredients out of the machine and 'brew' the drink.

        This method TRUSTS that is_resource_sufficient() was called
        first. The CoffeeMachine class in main.py makes sure of that.
        """
        for item, needed in drink.ingredients.items():
            self.resources[item] -= needed
        progress_bar("Heating water: ")
        progress_bar("Brewing:       ")
        print(f"\nYour {drink.name} is ready. Enjoy! ☕")

    def refill(self):
        """Ask the technician how much of each ingredient to add."""
        print("Enter amounts in ml / g (press Enter for 0):")
        for item in self.resources:
            # ask_number() already refuses letters and negative numbers,
            # so we don't need try/except here
            self.resources[item] += ask_number(f"{item}: ")
        print("Refill done ✅")

    def report(self):
        """Print how much of each ingredient is left."""
        for item, amount in self.resources.items():
            print(f"{item}: {amount}")