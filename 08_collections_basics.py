# ==============================================================================
# Topic: Collections Overview (Lists, Tuples, Sets)
# Description: Understanding Python's built-in data collections, element
#              modification, and array sorting methods.
# ==============================================================================

# Collection Types Summary:
# - List  = [] Ordered, mutable (changeable), permits duplicate values.
# - Set   = {} Unordered, immutable elements, NO duplicates allowed.
# - Tuple = () Ordered, immutable (un-changeable), permits duplicates (Faster execution).

# ------------------------------------------------------------------------------
# 1. Working with Lists
# ------------------------------------------------------------------------------
fruits = ["apple", "orange", "banana", "cherry"]

print("=== Initial List ===")
print("Original List:", fruits)
print("Total items:  ", len(fruits))
print("Is 'pineapple' in list?:", "pineapple" in fruits)

# Reassigning an element by index
fruits[0] = "pineapple"

# List methods
fruits.append("kiwi")              # Adds element to the end
fruits.insert(1, "avocado")        # Adds element at specific index
fruits.sort()                      # Sorts elements alphabetically
fruits.remove("banana")            # Removes specific item

print("\n=== Modified & Sorted List ===")
print("Updated List:", fruits)
print("First 3 items (Sliced):", fruits[:3])

# ------------------------------------------------------------------------------
# 2. Iterating Through a List
# ------------------------------------------------------------------------------
print("\n=== Displaying Fruit Inventory ===")
for index, fruit in enumerate(fruits, start=1):
    print(f"Item #{index}: {fruit.title()}")