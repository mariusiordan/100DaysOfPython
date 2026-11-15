# =====================================================================
#  menu.py
#  ---------------------------------------------------------------------
#  Two classes live here:
#    MenuItem -> describes ONE drink
#    Menu     -> holds ALL the drinks
#
#  A CLASS is a blueprint (like a form with empty fields).
#  An OBJECT is one filled-in copy of that form.
#
#      MenuItem   = the blueprint "a drink has a name, cost, ingredients"
#      espresso   = one object made from it
#      latte      = another object made from the same blueprint
# =====================================================================


class MenuItem:
    """One drink. Cost is in PENCE (150 = £1.50).

    Whole numbers avoid float problems: in Python 0.1 + 0.2 = 0.30000000000000004
    """

    # -----------------------------------------------------------------
    #  __init__ runs AUTOMATICALLY when you create an object:
    #      MenuItem("Espresso", 150, water=50, coffee=18)
    #
    #  "self" = the object being created. self.name = name means:
    #  "save this value INSIDE this object, so I can use it later".
    #
    #  water=0, milk=0 ... are DEFAULT values. If you don't give milk,
    #  it becomes 0. That's why espresso doesn't need to say milk=0.
    # -----------------------------------------------------------------
    def __init__(self, name, cost, water=0, milk=0, coffee=0, chocolate=0):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "chocolate": chocolate,
        }


class Menu:
    """Holds all the drinks and knows how to show them."""

    def __init__(self):
        # -------------------------------------------------------------
        #  A dictionary of OBJECTS:
        #    key   = what the customer types ("latte")
        #    value = a MenuItem object with all the details
        #
        #  To add a new drink, add ONE line here. Nothing else changes.
        #  In your old version you also had to edit print_menu()
        #  by hand - now show() builds the menu automatically.
        # -------------------------------------------------------------
        self.items = {
            "espresso": MenuItem("Espresso", 150, water=50, coffee=18),
            "double": MenuItem("Double Espresso", 300, water=100, coffee=36),
            "chocolate": MenuItem("Hot Chocolate", 350, water=50, milk=150, chocolate=30),
            "latte": MenuItem("Coffee Latte", 400, water=200, milk=150, coffee=24),
        }

    def show(self):
        """Print the menu. {key:<10} means: left-align in 10 spaces."""
        print("\n============  MENU  ============")
        for key, item in self.items.items():
            print(f"{key:<10} {item.name:<16} £{item.cost / 100:.2f}")
        print("receipt / exit")
        print("================================\n")

        #print("--- Technician only: report / refill / cash ---")

    def find_drink(self, choice):
        """Return the MenuItem object, or None if the drink doesn't exist.

        dict.get() returns None instead of crashing with a KeyError.
        """
        return self.items.get(choice)