"""
COMPLEX NUMBERS
===============

A complex number has two parts:

    a + bj

where:

    a = real part
    b = imaginary part

Python uses `j` to represent the imaginary unit.

Examples:

    3 + 2j
    5j
    -2 + 4j
"""

# --------------------------------------------------
# 1. Creating complex numbers
# --------------------------------------------------

number = 3 + 2j

print(number)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(number))
# <class 'complex'>


# --------------------------------------------------
# 3. Real and imaginary parts
# --------------------------------------------------

number = 3 + 2j

print(number.real)
print(number.imag)


# --------------------------------------------------
# 4. Creating a complex number with complex()
# --------------------------------------------------

number = complex(3, 2)

print(number)


# --------------------------------------------------
# 5. Complex arithmetic
# --------------------------------------------------

a = 2 + 3j
b = 1 + 2j

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# --------------------------------------------------
# 6. Complex numbers can contain zero
# --------------------------------------------------

number = 5 + 0j

print(number)


# --------------------------------------------------
# 7. Why do complex numbers exist?
# --------------------------------------------------

# Complex numbers are useful in areas such as:
#
#   - mathematics
#   - engineering
#   - signal processing
#   - physics
#   - electrical engineering
#
# You do not need complex numbers for most
# beginner Python programs.


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create the complex number 4 + 5j.

# 2. Print its real part.

# 3. Print its imaginary part.

# 4. Create two complex numbers and add them.

# 5. Try multiplying two complex numbers.
