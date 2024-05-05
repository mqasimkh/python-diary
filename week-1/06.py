# Again Functions

# We don't need to define functions at the start of the program. We can have it anywhere in the program. However, we need to tell the python that we have main functions and a separate functions somewhere below.
# We then call the main function

def main():
    name = input("Whats your name? ").strip().title()
    hello(name)

# hello function
# It is case sensitive, means if you have functions with hello, you must define with small h i.e. hello and not Hello. Both are different.
def hello(to):
    print("Hello, ", to)

main()