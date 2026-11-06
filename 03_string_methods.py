# ==============================================================================
# Topic: String Methods, Sanitization & Input Validation
# Description: Practical demonstration of built-in string methods, method chaining,
#              and interactive user input validation projects.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic String Inspection & Transformation Methods
# ------------------------------------------------------------------------------
full_name = " alex johnson "
phone_number = "555 123 4567"

print("=== Basic String Methods ===")
print("Original Name:            ", f"'{full_name}'")
print("Total length (inc. space):", len(full_name))
print("First 'a' position:       ", full_name.find("a"))
print("Last 'o' position:        ", full_name.rfind("o"))
print("Title Case:               ", full_name.title())
print("UPPERCASE:                ", full_name.upper())
print("Is digits only?:          ", full_name.isdigit())
print("Is letters only?:         ", full_name.isalpha())
print("Formatted Phone:          ", phone_number.replace(" ", "-"))


# ------------------------------------------------------------------------------
# 2. Mini-Project 1: User Registration Portal
# Rules: Max 12 chars, no spaces, letters only.
# ------------------------------------------------------------------------------
print("\n=== Project 1: User Registration Portal ===")
user_name = input("Enter your desired username: ")

if len(user_name) > 12:
    print("Error: Username must not exceed 12 characters.")
elif user_name.find(" ") != -1:
    print("Error: Username must not contain spaces.")
elif not user_name.isalpha():
    print("Error: Username must contain letters only.")
else:
    print(f"Success: Account created! Welcome, {user_name}.")


# ------------------------------------------------------------------------------
# 3. Mini-Project 2: E-Commerce Promo Code Validator
# Rules: Method chaining sanitization, min length 6, not numbers-only,
#        must contain 'SAVE' or 'DEAL'.
# ------------------------------------------------------------------------------
print("\n=== Project 2: E-Commerce Checkout System ===")
raw_promo = input("Enter your promo code (e.g. ' save - deal10 '): ")

# Method Chaining: strip hyphens/spaces and capitalize
promo_code = raw_promo.replace("-", "").replace(" ", "").upper()
print(f"Sanitized Code: '{promo_code}'")

if len(promo_code) < 6:
    print("Error: Promo code must be at least 6 characters long.")
elif promo_code.isdigit():
    print("Error: Promo code cannot consist of numbers only.")
elif promo_code.find("SAVE") == -1 and promo_code.find("DEAL") == -1:
    print("Error: Promo code must contain a valid keyword ('SAVE' or 'DEAL').")
else:
    print(f"SUCCESS: Discount applied with promo code '{promo_code}'!")


# ------------------------------------------------------------------------------
# 4. Mini-Project 3: Automated Parking Pass Gate Controller
# Rules: Length 5-10, not pure digits or pure letters, must contain 'VIP' or 'PARK'.
# ------------------------------------------------------------------------------
print("\n=== Project 3: Automated Parking Gate ===")
raw_pass = input("Enter your parking Pass Code (e.g. ' park - vip99 '): ")

# Sanitize input
pass_code = raw_pass.replace("-", "").replace(" ", "").upper()
print(f"Sanitized Pass: '{pass_code}'")

if len(pass_code) < 5 or len(pass_code) > 10:
    print("Error: Parking pass must be between 5 and 10 characters.")
elif pass_code.isdigit():
    print("Error: Pass cannot be only numbers.")
elif pass_code.isalpha():
    print("Error: Pass cannot be only letters.")
elif pass_code.find("PARK") == -1 and pass_code.find("VIP") == -1:
    print("Error: Pass must contain 'VIP' or 'PARK'.")
else:
    print(f"GATE OPEN: Parking pass '{pass_code}' accepted! Enjoy your stay.")