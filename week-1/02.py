# name = input("What is your name? ")

# In coding never think that user will always enter the correct value or in correct format. 
# https://docs.python.org/3/library/stdtypes.html#string-methods
# Built-in functionalities in python to do lot of things with user data.
# strip the white spaces from the name.

# name = name.strip()

# Assigning new value to name = right to left. i.e returns the name value after name.strip function and saves in name.
# capitalize the first letter of the name.

# name = name.capitalize()
# name = name.title()

# Make the code efficient, because things are repeating, so make it efficient.

# name = input("What is your name? ")
# name = name.strip().title()
 
# again 2 lines repeating, so make more efficient.

name = input("What is your name? ").strip().title()
# Get the value of from user, strip the white spaces, capitalize the first letter, and then save in name.

first, last = name.split (" ")
# Split the name into 2 parts, first and last name.

print("Hello,", first)
# Print the first name.

