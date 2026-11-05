# =====================================================================
# Python Basics : Data Types & Variables
# =====================================================================

# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it ws the value it contains
#from tabnanny import process_tokens

# strings                   # Letter

first_name = "Bro"
food = "Pizza"
email = "yoh@gmail.com"

print(f"Hello {first_name}, You like {food}, and your email is: {email}")

#Integers                    # Whole number

age = 28
quantity = 3
num_of_games = 5

print(f"You're {age} years old!, and you are buying {quantity} Consoles, with {num_of_games} games. ")

#float          # have  decimal

price = 532.50

print(f"The console costs €{price}")

#Boolean      #Either True or False

is_Sony = False
for_sale = True

if for_sale:
    print("Yes it's on sale")
else:
    print("Not on sale")


## TYPE CASTING ##

# The process of converting a value of one data type to another
# (string, integer, float, boolean)
# Explicit vs Implicit

name = "ShelVin"
age = 28                        # print(type(smt))
gpa = 2.6
student = False

age = float(age)
print(age)


user_name = input("Enter your user name: ")
game_ID = str(input("Enter your game ID: "))

print(f"Great honour {user_name} of {game_ID} welcome to the GAME!")


adjective = input("Enter the adjective: ")
verb1 = input("Enter the verb1: ")
noun1 = input("Enter the noun1: ")
verb2 = input("Enter the verb2: ")
noun2 = input("Enter the noun2: ")
noun3 = input("Enter the noun3: ")

print(f"My cat' is way {adjective} than yours")
print(f"She {verb1} a lot and she is very {noun1}, I tell you bro! ")
print(f"She is {verb2} funny and her {noun2} is on another level MEHN!")
print(f"She is such a rare {noun3}!!")


length = input("Enter the length of a rectangle: ")
width = input("Enter the width of a rectangle: ")

length = float(length)
width = float(width)

area = length * width

print(f"The area of the rectangle is {area}")


item = input("What item would you like to buy?: ")
price = float(input("What is the price of item would you like to buy: $"))
quantity = int(input("How many items would you like?: "))

total = price * quantity

print(f"You total is €{round(total,2)}")
print(f"You have bought {quantity} * {price}/s")