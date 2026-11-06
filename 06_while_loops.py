# ==============================================================================
# Topic: While Loops & Interactive Projects
# Description: Demonstrating code execution while conditions remain true,
#              input validation loops, and a compound interest calculator.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Input Validation Loop
# ------------------------------------------------------------------------------
print("=== Name Validation ===")
name = input("Enter your name: ").strip()

while name == "":
    print("ERROR: Name cannot be blank.")
    name = input("Please enter your name: ").strip().capitalize()

print(f"Welcome, {name}!\n")


# ------------------------------------------------------------------------------
# 2. Sent-Value Loop (Quit Condition)
# ------------------------------------------------------------------------------
print("=== Favorite Foods Tracker ===")
food = input("Enter a food you like ('q' to quit): ")

while food.lower() != "q":
    if food.strip() == "":
        print("ERROR: You didn't type anything!")
    else:
        print(f"Added to list: You like {food}")
    food = input("Enter another food ('q' to quit): ")

print("Thanks for playing!\n")


# ------------------------------------------------------------------------------
# 3. Interactive Project: Compound Interest Calculator
# ------------------------------------------------------------------------------
print("=== Compound Interest Calculator ===")

principal = 0
rate = 0
time_years = 0

# Validate Principal
while True:
    principal = float(input("Enter principal amount (€): "))
    if principal <= 0:
        print("Principal amount must be greater than zero.")
    else:
        break

# Validate Interest Rate
while True:
    rate = float(input("Enter annual interest rate (%): "))
    if rate <= 0:
        print("Interest rate must be greater than zero.")
    else:
        break

# Validate Time Period
while True:
    time_years = int(input("Enter time period (years): "))
    if time_years <= 0:
        print("Time period must be at least 1 year.")
    else:
        break

# Compound Interest Formula: A = P * (1 + r/100)^t
total_balance = principal * pow((1 + rate / 100), time_years)

print("\n--- INVESTMENT SUMMARY ---")
print(f"Initial Principal: €{principal:,.2f}")
print(f"Interest Rate:     {rate}% per year")
print(f"Investment Period: {time_years} year(s)")
print(f"Final Balance:     €{total_balance:,.2f}")