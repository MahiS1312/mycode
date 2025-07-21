# cash.py

import sys

def process_cash_payment(amount):
    if amount <= 0:
        return "Invalid amount. Please enter a positive value."
    return f"Cash payment of ${amount:.2f} processed."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 cash.py <amount>")
        sys.exit(1)

    try:
        amount = float(sys.argv[1])
        result = process_cash_payment(amount)
        print(result)
    except ValueError:
        print("Please enter a valid number.")
