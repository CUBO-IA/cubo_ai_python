"""
NONE
====

None is a special Python value that represents
the absence of a value.

Its type is NoneType.

None is NOT:

    0
    ""
    False

Those are different values.
"""

# --------------------------------------------------
# 1. Creating a None value
# --------------------------------------------------

result = None

print(result)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(result))
# <class 'NoneType'>


# --------------------------------------------------
# 3. None means "no value"
# --------------------------------------------------

username = None

print(username)

# Later, the variable might receive a value:

username = "Alice"

print(username)


# --------------------------------------------------
# 4. Checking for None
# --------------------------------------------------

value = None

print(value is None)


# Prefer:

# value is None

# instead of:

# value == None


# --------------------------------------------------
# 5. Functions can return None
# --------------------------------------------------

def say_hello():
    print("Hello!")


result = say_hello()

print(result)

# The function doesn't explicitly return anything,
# so Python returns None.


# --------------------------------------------------
# 6. None is different from False
# --------------------------------------------------

print(None == False)
print(None == 0)
print(None == "")


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a variable called `username` and
#    initially give it the value None.

# 2. Check whether username is None.

# 3. Give username a string value.

# 4. Check username again.

# 5. Create a function that doesn't return
#    anything. Store its result in a variable
#    and print that variable.
