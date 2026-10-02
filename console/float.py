"""
FLOATS
======

A float is a number that contains a decimal part.

Examples:

    3.14
    10.5
    -2.75
    0.0
"""

# --------------------------------------------------
# 1. Creating floats
# --------------------------------------------------

price = 19.99
temperature = 25.5
height = 1.75

print(price)
print(temperature)
print(height)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(price))
# <class 'float'>


# --------------------------------------------------
# 3. Arithmetic with floats
# --------------------------------------------------

a = 10.5
b = 2.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# --------------------------------------------------
# 4. Integers and floats can work together
# --------------------------------------------------

integer_number = 10
float_number = 2.5

result = integer_number + float_number

print(result)
print(type(result))


# --------------------------------------------------
# 5. Converting to float
# --------------------------------------------------

number = float("3.14")

print(number)
print(type(number))


# --------------------------------------------------
# 6. Converting an integer to a float
# --------------------------------------------------

number = float(10)

print(number)
# 10.0


# --------------------------------------------------
# 7. Rounding
# --------------------------------------------------

number = 3.14159265

print(round(number))
print(round(number, 2))
print(round(number, 4))


# --------------------------------------------------
# 8. Be careful with decimal precision
# --------------------------------------------------

result = 0.1 + 0.2

print(result)

# You might expect:
# 0.3
#
# But Python may display:
# 0.30000000000000004
#
# This happens because floating-point numbers
# are represented using binary approximations.


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a variable containing the price of a product.

# 2. Calculate the average of three numbers.

# 3. Convert the string "10.5" into a float.

# 4. Round 12.34567 to two decimal places.

# 5. Experiment with:
#
#       0.1 + 0.2
#
#    Why might the result surprise you?
