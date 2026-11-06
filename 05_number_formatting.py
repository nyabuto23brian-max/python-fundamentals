# ==============================================================================
# Topic: Format Specifiers
# Description: Formatting numeric values using f-strings with flag options like
#              decimal precision, thousand separators, and alignment.
# ==============================================================================

price1 = 3000.14159
price2 = -9870.653
price3 = 12467.897

print("=== Formatting Numbers ===")

# :.2f  -> Round to 2 decimal places (float)
# :,    -> Add comma as thousand separator
# :,.2f -> Combine thousand separator with 2 decimal places

print(f"Price 1 (Raw):   {price1}")
print(f"Price 1 (Clean): ${price1:,.2f}")
print(f"Price 2 (Clean): ${price2:,.2f}")
print(f"Price 3 (Clean): ${price3:,.2f}")

# Additional format flags:
# :+   -> Display explicit positive/negative sign
# :^10 -> Center-align value within 10 spaces
# :.0% -> Format decimal as a percentage

discount = 0.15
balance = 2500

print("\n=== Additional Format Flags ===")
print(f"Explicit Sign: {price1:+,.2f}")
print(f"Percentage:    {discount:.0%}")
print(f"Right-Aligned: ${balance:>10,.2f}")