"""
SETS
====

A set is a collection of unique values.

Sets:

    - do not allow duplicates
    - are mutable
    - do not use indexes like lists

Example:

    {"apple", "banana", "orange"}
"""

# --------------------------------------------------
# 1. Creating a set
# --------------------------------------------------

fruits = {"apple", "banana", "orange"}

print(fruits)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(fruits))
# <class 'set'>


# --------------------------------------------------
# 3. Duplicate values are removed
# --------------------------------------------------

numbers = {1, 2, 2, 3, 3, 3}

print(numbers)

# The set contains only:
#
# {1, 2, 3}


# --------------------------------------------------
# 4. Adding items
# --------------------------------------------------

fruits.add("mango")

print(fruits)


# --------------------------------------------------
# 5. Removing items
# --------------------------------------------------

fruits.remove("mango")

print(fruits)


# --------------------------------------------------
# 6. Safely removing an item
# --------------------------------------------------

fruits.discard("pear")

# discard() does not raise an error if the
# item doesn't exist.


# --------------------------------------------------
# 7. Checking for membership
# --------------------------------------------------

print("apple" in fruits)
print("pear" in fruits)


# --------------------------------------------------
# 8. Set union
# --------------------------------------------------

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


# --------------------------------------------------
# 9. Set intersection
# --------------------------------------------------

print(a & b)


# --------------------------------------------------
# 10. Set difference
# --------------------------------------------------

print(a - b)
print(b - a)


# --------------------------------------------------
# 11. Converting a list to a set
# --------------------------------------------------

numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = set(numbers)

print(unique_numbers)


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a set containing five fruits.

# 2. Add another fruit.

# 3. Remove one fruit.

# 4. Create a set containing duplicate numbers.
#    What happens?

# 5. Create two sets and find their:
#       - union
#       - intersection
#       - difference

# 6. Convert a list containing duplicates into
#    a set to remove the duplicates.
