# --------------------------------------------------
# EXERCISE: AGE CHECK
# --------------------------------------------------

# Ask the user for their name and age.
#
# Rules:
#
#   - If the age is less than 18, print:
#       "<name> is underage"
#
#   - If the age is exactly 18, print:
#       True
#
#   - If the age is greater than 18, print:
#       False
#
# Try to solve this using a boolean expression.

name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 18:
    print(f"{name} is underage")
elif age == 18:
    print(True)
else:
    print(False)
