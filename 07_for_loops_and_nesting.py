# ==============================================================================
# Topic: For Loops, Timers & Nested Loops
# Description: Iterating over ranges, building real-time countdown timers,
#              and using nested loops to print geometric patterns.
# ==============================================================================

import time

# ------------------------------------------------------------------------------
# 1. Countdown Timer (For Loop + time.sleep)
# ------------------------------------------------------------------------------
print("=== Countdown Timer ===")
seconds = int(input("Enter countdown time in seconds: "))

print("Starting countdown...")
for x in range(seconds, 0, -1):
    print(f"Time remaining: {x} second(s)")
    time.sleep(1)  # Pauses execution for 1 second

print("🎉 HAPPY NEW YEAR! 🎉\n")


# ------------------------------------------------------------------------------
# 2. Nested Loops: Grid Pattern Generator
# Structure:
#   outer loop controls ROWS
#       inner loop controls COLUMNS
# ------------------------------------------------------------------------------
print("=== Grid Pattern Generator ===")
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
symbol = input("Enter symbol to use (*, #, @, etc.): ")

print("\nGenerated Grid:")
for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")  # end=" " keeps output on the same line
    print()                     # Print new line after completing a row