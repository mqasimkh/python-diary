# Again Functions (Returning Values)

# In some cases, we might need functions that takes parameters or arguments, perform calculations or action on it, and then return the new value to us so we can use anywhere else in our program.
# This is called return value.

def main():
    x = int(input("What is value of x? "))
    print("The square of x is", square(x))

def square(x):
    return x * x

main()