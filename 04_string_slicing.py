# ==============================================================================
# Topic: String Slicing & Indexing
# Description: Accessing individual characters or sub-strings using the [start:end:step]
#              operator, dynamic slicing with .index(), and an interactive project.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Basic Indexing & Slicing Syntax: [start : end : step]
# Note: start index is INCLUSIVE, end index is EXCLUSIVE
# ------------------------------------------------------------------------------
credit_number = "1234-5678-9012-3456"

print("=== Basic Slicing Examples ===")
print("Character at index 2:   ", credit_number[2])
print("First 4 characters:     ", credit_number[0:4])   # credit_number[:4]
print("Characters from index 5:", credit_number[5:])     # From index 5 to end
print("Last character:         ", credit_number[-1])    # Negative index counts from end
print("Every 3rd character:    ", credit_number[::3])   # Step size of 3

# Practical slicing examples:
last_digits = credit_number[-4:]
print(f"Masked Card: XXXX-XXXX-XXXX-{last_digits}")

reversed_card = credit_number[::-1]
print(f"Reversed String: {reversed_card}")


# ------------------------------------------------------------------------------
# 2. Dynamic Slicing with .index()
# ------------------------------------------------------------------------------
print("\n=== Email Address Splitter ===")
email = input("Enter your email address (e.g. alex@gmail.com): ")

if "@" in email:
    at_index = email.index("@")  # Finds the position of the '@' symbol
    username = email[:at_index]
    domain = email[at_index + 1:]
    print(f"Username: {username}")
    print(f"Domain:   {domain}")
else:
    print("Invalid email: Missing '@' symbol.")


# ------------------------------------------------------------------------------
# 3. Interactive Project: Security Badge Extractor
# ------------------------------------------------------------------------------
print("\n=== Security Badge Extractor ===")
raw_badge = input("Enter security badge code (e.g. 2026-VIP-8492): ")
badge_code = raw_badge.replace(" ", "").upper()

# Validation Rules
if len(badge_code) != 13:
    print("ERROR: Badge code must be exactly 13 characters (e.g., '2026-VIP-8492').")
elif badge_code.find("-") == -1:
    print("ERROR: Badge code must contain hyphens '-'.")
else:
    # Slicing details from sanitized input
    year_issued = badge_code[:4]
    member_id = badge_code[-4:]
    security_pin = member_id[::-1]  # Reversed ID for pin generation
    first_hyphen_pos = badge_code.find("-")

    print("\n=== BADGE ACCESS GRANTED ===")
    print(f"Year Issued:              {year_issued}")
    print(f"Member ID:                {member_id}")
    print(f"Generated Security PIN:   {security_pin}")
    print(f"First Hyphen Index:       {first_hyphen_pos}")