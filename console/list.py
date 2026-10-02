"""
LISTS
======

A list stores multiple values in a single object.

Lists are:

    - ordered
    - mutable
    - able to contain duplicate values

Examples:

    [1, 2, 3]
    ["apple", "banana", "orange"]
"""

# --------------------------------------------------
# 1. Creating a list
# --------------------------------------------------

fruits = ["apple", "banana", "orange"]

print(fruits)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(fruits))
# <class 'list'>


# --------------------------------------------------
# 3. Lists can contain different types
# --------------------------------------------------

person = ["Alice", 25, True]

print(person)


# --------------------------------------------------
# 4. Accessing items
# --------------------------------------------------

fruits = ["apple", "banana", "orange"]

print(fruits[0])
print(fruits[1])
print(fruits[2])


# --------------------------------------------------
# 5. Negative indexing
# --------------------------------------------------

print(fruits[-1])
print(fruits[-2])


# --------------------------------------------------
# 6. Changing an item
# --------------------------------------------------

fruits[0] = "mango"

print(fruits)


# --------------------------------------------------
# 7. Adding items with append()
# --------------------------------------------------

fruits.append("grape")

print(fruits)


# --------------------------------------------------
# 8. Inserting an item
# --------------------------------------------------

fruits.insert(1, "kiwi")

print(fruits)


# --------------------------------------------------
# 9. Removing an item
# --------------------------------------------------

fruits.remove("kiwi")

print(fruits)


# --------------------------------------------------
# 10. Removing by position
# --------------------------------------------------

removed = fruits.pop()

print(removed)
print(fruits)


# --------------------------------------------------
# 11. List length
# --------------------------------------------------

print(len(fruits))


# --------------------------------------------------
# 12. Checking if an item exists
# --------------------------------------------------

print("apple" in fruits)
print("pear" in fruits)


# --------------------------------------------------
# 13. Slicing lists
# --------------------------------------------------

numbers = [10, 20, 30, 40, 50]

print(numbers[0:3])
print(numbers[:3])
print(numbers[2:])


# --------------------------------------------------
# 14. Sorting
# --------------------------------------------------

numbers = [5, 2, 8, 1, 3]

numbers.sort()

print(numbers)


# --------------------------------------------------
# 15. Reversing
# --------------------------------------------------

numbers.reverse()

print(numbers)


# --------------------------------------------------
# 16. Looping through a list
# --------------------------------------------------

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a list containing five numbers.

# 2. Print the first and last items.

# 3. Add another number.

# 4. Remove one number.

# 5. Change one of the numbers.

# 6. Find the length of the list.

# 7. Loop through the list and print every item.

# 8. Sort the list.
