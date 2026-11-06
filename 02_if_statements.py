# ==============================================================================
# Topic: If Statements & Conditional Logic
# Description: Controlling program execution flow using comparison operators,
#              logical operators (and, or, not), and if/elif/else structure.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Comparison Operators & Conditional Flow
# Comparison Operators: == (equal), != (not equal), >, <, >=, <=
# ------------------------------------------------------------------------------
age = int(input("Enter your age: "))

if age >= 18:
    print("Status: Adult (Eligible to register)")
elif age > 12:
    print("Status: Teenager")
else:
    print("Status: Child")


# ------------------------------------------------------------------------------
# 2. Logical Operators (and, or, not)
# 'and' -> ALL conditions must be True
# 'or'  -> At least ONE condition must be True
# 'not' -> Reverses a boolean result (True becomes False)
# ------------------------------------------------------------------------------
temp = float(input("\nEnter current temperature in °C: "))
is_raining = input("Is it raining? (yes/no): ").strip().lower() == "yes"

print("\n=== Weather Assessment ===")

# Combining checks using 'and' & 'or'
if temp >= 20 and not is_raining:
    print("Advice: Great day for outdoor activities!")
elif temp < 5 or is_raining:
    print("Advice: Take a jacket and stay warm/dry.")
else:
    print("Advice: Mild weather conditions.")


# ------------------------------------------------------------------------------
# 3. Interactive Mini-Project: Movie Ticket Pricing System
# ------------------------------------------------------------------------------
print("\n=== Movie Ticket Pricing Portal ===")
customer_age = int(input("Enter customer age: "))
has_student_id = input("Do you have a student ID? (yes/no): ").strip().lower() == "yes"

# Nested or combined evaluation rules
if customer_age < 12 or customer_age >= 65:
    price = 6.00
    category = "Discounted (Child / Senior)"
elif has_student_id:
    price = 8.00
    category = "Student Special"
else:
    price = 12.00
    category = "Standard Adult"

print("\n--- BOOKING SUMMARY ---")
print(f"Ticket Type: {category}")
print(f"Price:       €{price:.2f}")