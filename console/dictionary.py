"""
DICTIONARIES
============

A dictionary stores data as key-value pairs.

Example:

    {
        "name": "Alice",
        "age": 25
    }

Here:

    "name" is a key
    "Alice" is its value

    "age" is a key
    25 is its value
"""

# --------------------------------------------------
# 1. Creating a dictionary
# --------------------------------------------------

person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

print(person)


# --------------------------------------------------
# 2. Checking the type
# --------------------------------------------------

print(type(person))
# <class 'dict'>


# --------------------------------------------------
# 3. Accessing values
# --------------------------------------------------

print(person["name"])
print(person["age"])


# --------------------------------------------------
# 4. Adding a new key-value pair
# --------------------------------------------------

person["city"] = "San Salvador"

print(person)


# --------------------------------------------------
# 5. Changing a value
# --------------------------------------------------

person["age"] = 26

print(person)


# --------------------------------------------------
# 6. Checking if a key exists
# --------------------------------------------------

print("name" in person)
print("email" in person)


# --------------------------------------------------
# 7. Using get()
# --------------------------------------------------

print(person.get("name"))

# If the key doesn't exist, get() can return None
# instead of raising an error.

print(person.get("email"))


# --------------------------------------------------
# 8. Removing a key-value pair
# --------------------------------------------------

person.pop("city")

print(person)


# --------------------------------------------------
# 9. Getting all keys
# --------------------------------------------------

print(person.keys())


# --------------------------------------------------
# 10. Getting all values
# --------------------------------------------------

print(person.values())


# --------------------------------------------------
# 11. Getting key-value pairs
# --------------------------------------------------

print(person.items())


# --------------------------------------------------
# 12. Looping through a dictionary
# --------------------------------------------------

person = {
    "name": "Alice",
    "age": 25,
    "city": "San Salvador"
}

for key in person:
    print(key)


# --------------------------------------------------
# 13. Looping through keys and values
# --------------------------------------------------

for key, value in person.items():
    print(key, value)


# --------------------------------------------------
# 14. Nested dictionaries
# --------------------------------------------------

students = {
    "student1": {
        "name": "Alice",
        "age": 20
    },
    "student2": {
        "name": "Bob",
        "age": 22
    }
}

print(students["student1"]["name"])


# --------------------------------------------------
# EXERCISES
# --------------------------------------------------

# 1. Create a dictionary representing yourself.
#
#    Include:
#       name
#       age
#       city
#       favorite_color

# 2. Print each value.

# 3. Add a new key called "email".

# 4. Change your age.

# 5. Remove one key.

# 6. Loop through the dictionary and print
#    every key and value.

# 7. Create a nested dictionary representing
#    two people.
