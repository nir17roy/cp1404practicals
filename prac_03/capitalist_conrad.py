"""
CP1404 - Practical
Simulates the changing price of a stock for Capitalist Conrad.
The stock starts at $10.00 and changes each day:
- There's a 50% chance it increases by up to 17.5%
- There's a 50% chance it decreases by up to 5%
The simulation ends if the stock exceeds $100 or drops below $1.
Prices are rounded to the nearest cent.
"""

import random

# Constants for simulation limits
MAX_INCREASE = 0.175  # maximum increase of 17.5%
MAX_DECREASE = 0.05   # maximum decrease of 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

def main():
    generate_simulation_file()
    print(f"Simulation complete. Data saved to '{FILENAME}'.")

def generate_new_price(price):
    """Calculate new price based on a random increase or decrease."""
    if random.randint(1, 2) == 1:
        change = random.uniform(0, MAX_INCREASE)
    else:
        change = random.uniform(-MAX_DECREASE, 0)
    return price * (1 + change)

def generate_simulation_file():
    """Run the price simulation and write each day’s result to a text file."""
    price = INITIAL_PRICE
    day = 0

    out_file = open(FILENAME, 'w')
    print(f"Starting price: ${price:,.2f}", file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        day += 1
        price = generate_new_price(price)
        print(f"On day {day} price is: ${price:,.2f}", file=out_file)

    out_file.close()

main()
