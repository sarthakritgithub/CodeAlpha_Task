# Task-2
# CodeAlpha
# ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock prices.
# ● Simplified Scope:
# ○ User inputs stock names and quantity.
# ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}).
# ○ Display total investment value and optionally save the result in a .txt or .csv file.
# ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional).

import random

# Fixed stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2000,
    "MSFT": 320,
    "AMZN": 140
}

total = 0

print("Welcome to Stock Tracker!")
print("Available stocks: AAPL, TSLA, GOOG, MSFT, AMZN")
print("Type 'done' when you're finished.\n")

while True:
    stock = input("Enter stock name: ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Invalid stock. Try again.\n")
        continue

    qty = input("Enter quantity: ")
    if not qty.isdigit():
        print("Please enter a valid number.\n")
        continue

    qty = int(qty)
    price = stock_prices[stock]
    value = qty * price
    total += value
    print(f"{stock}: {qty} × ${price} = ${value}\n")

print("Total Investment Value: $", total)
