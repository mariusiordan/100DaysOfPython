# =====================================================================
#  money_machine.py
#  ---------------------------------------------------------------------
#  The MoneyMachine class looks after the MONEY only:
#  taking coins, giving change, and keeping the profit.
#
#  All money is in PENCE (whole numbers). We only divide by 100
#  when we PRINT it, so the maths is always exact.
# =====================================================================

from helpers import ask_number, loading


class MoneyMachine:
    """Takes coins, gives change, keeps the profit."""

    # -----------------------------------------------------------------
    #  CLASS ATTRIBUTE (outside __init__, no "self."):
    #  shared by EVERY MoneyMachine object, because the UK coins are
    #  the same for every machine.
    #
    #  Compare with self.profit below - an INSTANCE attribute.
    #  If you had 2 machines, each would have its OWN profit.
    #
    #  To accept £2 coins, add one line: "£2": 200
    # -----------------------------------------------------------------
    COINS = {"£1": 100, "50p": 50, "20p": 20, "10p": 10}

    def __init__(self):
        self.profit = 0  # in pence

    def make_payment(self, cost):
        """Ask for coins. Return True if paid enough, False if not.

        The money is added to profit ONLY when the payment succeeds.
        """
        print(f"\nPlease pay £{cost / 100:.2f}")
        inserted = 0
        for coin_name, value in self.COINS.items():
            inserted += ask_number(f"How many {coin_name} coins? ") * value

        if inserted < cost:
            print(f"❌ Not enough money. £{inserted / 100:.2f} refunded.")
            return False

        change = inserted - cost
        self.profit += cost
        print(f"Inserted: £{inserted / 100:.2f}  |  Change: £{change / 100:.2f}")
        return True

    def report(self):
        print(f"Money: £{self.profit / 100:.2f}")

    def cash_out(self):
        """Technician empties the money box."""
        answer = input(f"Withdraw £{self.profit / 100:.2f}? (y/n): ").strip().lower()
        if answer == "y":
            print("Processing", end="")
            loading(5)
            self.profit = 0
            print("The money has been withdrawn ✅")
        else:
            print("Cancelled.")