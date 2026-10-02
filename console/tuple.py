"""
TUPLES
======

A tuple is a collection of values.

Tuples are:

    - ordered
    - immutable
    - able to contain duplicate values

Tuples use parentheses:

    (1, 2, 3)
"""

# --------------------------------------------------
# 1. Creating a tuple
# --------------------------------------------------

coordinates = (10, 20)

print(coordinates)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(coordinates))
# <class 'tuple'>


# --------------------------------------------------
# 3. Accessing items
# --------------------------------------------------

numbers = (10, 20, 30)

print(numbers[0])
print(numbers[1])


# --------------------------------------------------
# 4. Tuples can contain different types
# --------------------------------------------------

person = ("Alice", 25, True)

print(person)


# --------------------------------------------------
# 5. Tuples are immutable
# --------------------------------------------------

numbers = (10, 20, 30)

# The following would cause an error:
#
# numbers[0] = 100


# --------------------------------------------------
# 6. Tuple unpacking
# --------------------------------------------------

person = ("Alice", 25)

name, age = person

print(name)
print(age)


# --------------------------------------------------
# 7. Tuple length
# --------------------------------------------------

numbers = (10, 20, 30, 40)

print(len(numbers))


# --------------------------------------------------
# 8. Checking for an item
# --------------------------------------------------

numbers = (10, 20, 30)

print(20 in numbers)
print(50 in numbers)


# --------------------------------------------------
# 9. One-item tuples
# --------------------------------------------------

number = (10,)

print(type(number))

# The comma is important.
#
# Without the comma:
#
# number = (10)
#
# that is simply an integer.


# --------------------------------------------------
# 10. Useful tuple methods
# --------------------------------------------------

numbers = (1, 2, 2, 3, 2)

print(numbers.count(2))
print(numbers.index(3))


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a tuple containing three colors.

# 2. Print the first color.

# 3. Try changing the first color.
#    What happens?

# 4. Create a tuple containing your name and age.
#    Unpack it into two variables.

# 5. Create a tuple containing repeated numbers
#    and use count().

# 6. Create a one-item tuple.
