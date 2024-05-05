# Python is a interpreted language. When we run python3 day_1.py, the python interpreter reads the code line by line and convert it to machine language i.e. zeros and ones.
# Print is a function in python that prints the arguments. In this case, it took "Hi" as argument and printed it.
# Variable is assigned value from right to left = assigns/saves what is on the right to the left.

name = input("What is your name? ")

# print("Hi,", name ) 

# What we pass to the function is technically term for it is parameter = argument.
# Official Documentation -> Builtin Functions in Python -> https://docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=None, flush=False)
# *objects -> function can take any number of objects. sep=' ' -> objects are separated by space. end='\n' -> end of the line is new line.

# print("Hello, ", end="")

# Telling that the end="" instead of default value which is /n which shifts it to new line. This is over-riding the default value.

# print(name)

# overriding default value of separater.
# print("Hello,", name, sep="...")

# Add f to tell python that this is special string, and need special formatting.

# print(f"Hello, {name}")