"""
BOOLEANS
========

A boolean represents one of two possible values:

    True
    False

Booleans are commonly used when we need to answer
questions such as:

    Is the user logged in?
    Is the number greater than 10?
    Did something succeed?
"""

# --------------------------------------------------
# 1. Creating booleans
# --------------------------------------------------

is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(is_logged_in))
# <class 'bool'>


# --------------------------------------------------
# 3. Comparisons produce booleans
# --------------------------------------------------

age = 20

print(age > 18)
print(age == 20)
print(age < 10)


# --------------------------------------------------
# 4. Boolean variables can describe a condition
# --------------------------------------------------

temperature = 30

is_hot = temperature > 25

print(is_hot)


# --------------------------------------------------
# 5. The `not` operator
# --------------------------------------------------

is_raining = False

print(not is_raining)


# --------------------------------------------------
# 6. The `and` operator
# --------------------------------------------------

has_username = True
has_password = True

can_login = has_username and has_password

print(can_login)


# --------------------------------------------------
# 7. The `or` operator
# --------------------------------------------------

is_admin = False
is_owner = True

can_delete = is_admin or is_owner

print(can_delete)


# --------------------------------------------------
# 8. Boolean conversion with bool()
# --------------------------------------------------

print(bool(1))
print(bool(0))

print(bool("hello"))
print(bool(""))


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a variable called `is_student`.

# 2. Create a variable called `age`.
#    Create `is_adult` that is True when age
#    is 18 or greater.

# 3. Create:
#
#       has_ticket
#       is_invited
#
#    Create `can_enter` that is True when the
#    person has a ticket OR is invited.

# 4. What does bool("") return?
#    What about bool("Python")?
