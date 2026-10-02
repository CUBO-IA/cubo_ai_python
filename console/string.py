"""
STRINGS
=======

A string is a sequence of characters.

Strings are used for text.

Examples:

    "Hello"
    "Python"
    "123"
    ""
"""

# --------------------------------------------------
# 1. Creating strings
# --------------------------------------------------

name = "Alice"
message = 'Hello, Python!'

print(name)
print(message)


# --------------------------------------------------
# 2. Strings can contain numbers
# --------------------------------------------------

number = "123"

print(number)
print(type(number))

# This is text, not an integer.


# --------------------------------------------------
# 3. Checking the type
# --------------------------------------------------

print(type(name))
# <class 'str'>


# --------------------------------------------------
# 4. String concatenation
# --------------------------------------------------

first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name

print(full_name)


# --------------------------------------------------
# 5. String repetition
# --------------------------------------------------

print("Python " * 3)


# --------------------------------------------------
# 6. String length
# --------------------------------------------------

message = "Hello"

print(len(message))
# 5


# --------------------------------------------------
# 7. Indexing
# --------------------------------------------------

word = "Python"

print(word[0])
print(word[1])
print(word[5])


# Python indexes start at zero.


# --------------------------------------------------
# 8. Negative indexing
# --------------------------------------------------

print(word[-1])
print(word[-2])


# --------------------------------------------------
# 9. Slicing
# --------------------------------------------------

word = "Python"

print(word[0:2])
print(word[2:6])
print(word[:3])
print(word[3:])


# --------------------------------------------------
# 10. Useful string methods
# --------------------------------------------------

message = "Hello, Python!"

print(message.upper())
print(message.lower())
print(message.capitalize())


# --------------------------------------------------
# 11. Removing whitespace
# --------------------------------------------------

message = "   Hello   "

print(message.strip())


# --------------------------------------------------
# 12. Replacing text
# --------------------------------------------------

message = "I like Java"

print(message.replace("Java", "Python"))


# --------------------------------------------------
# 13. Searching inside strings
# --------------------------------------------------

message = "Python is fun"

print("Python" in message)
print("Java" in message)


# --------------------------------------------------
# 14. Splitting a string
# --------------------------------------------------

colors = "red,green,blue"

result = colors.split(",")

print(result)


# --------------------------------------------------
# 15. f-strings
# --------------------------------------------------

name = "Alice"
age = 25

message = f"My name is {name} and I am {age} years old."

print(message)


# --------------------------------------------------
# 16. Escape characters
# --------------------------------------------------

print("Hello\nWorld")
print("Hello\tWorld")


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a string containing your name.

# 2. Print the length of your name.

# 3. Print the first character of your name.

# 4. Convert your name to uppercase.

# 5. Create first_name and last_name variables
#    and combine them into full_name.

# 6. Create a sentence using an f-string.

# 7. Experiment with string slicing.
