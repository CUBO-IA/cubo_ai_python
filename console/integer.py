"""
INTEGERS
========

An integer (int) is a whole number.

Examples:

    10
    0
    -5
    1000

Integers do not contain a decimal part.
"""

# --------------------------------------------------
# 1. Creating integers
# --------------------------------------------------

age = 25
temperature = -5
number_of_students = 30

print(age)
print(temperature)
print(number_of_students)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(age))
# <class 'int'>


# --------------------------------------------------
# 3. Basic arithmetic
# --------------------------------------------------

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Remainder
print(a ** b)  # Exponentiation


# --------------------------------------------------
# 4. Division produces a float
# --------------------------------------------------

result = 10 / 2

print(result)
print(type(result))


# --------------------------------------------------
# 5. Floor division
# --------------------------------------------------

result = 10 // 3

print(result)
# 3

# The decimal part is discarded.


# --------------------------------------------------
# 6. Remainder
# --------------------------------------------------

remainder = 10 % 3

print(remainder)
# 1


# --------------------------------------------------
# 7. Negative integers
# --------------------------------------------------

balance = -100

print(balance)


# --------------------------------------------------
# 8. Comparing integers
# --------------------------------------------------

age = 20

print(age == 20)
print(age != 20)
print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)


# --------------------------------------------------
# 9. Converting to an integer
# --------------------------------------------------

number = int("42")

print(number)
print(type(number))


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a variable containing your age.

# 2. Create two integers and calculate:
#       - their sum
#       - their difference
#       - their product

# 3. Calculate the remainder of 17 divided by 5.

# 4. Calculate 2 to the power of 8.

# 5. What is the difference between `/` and `//`?
