# Defining Functions

# name = input("What's your name? ").strip().title()
# print("Hello", name)
# print(f"Hello, {name}")

# Defing function hello. Python is indented language, so everything below function indented, otherwise it won't take it as part of function. 
# We defined a function hello, and then declated it takes single parameter called "to". It then prints "Hello, " to.
# In below code, we are passing value of "name" variable that users added as to parameter to the function hello
# Add : after 1st line in defining functions.
# It is case sensitive, means if you have functions with hello, you must define with small h i.e. hello and not Hello. Both are different.

# def hello(to):
    #print("Hello,", to)
    #print(f"Hello, {name}")

# Now we are defining function which takes same one parameter to. However, the default value of to is "World" so if no value is passed to hello() function, it will take to = World and thus print Hello World.
def hello(to="World"):
    print("Hello, ", to)

name = input("What's your name? ").strip().title()
hello(name)

# Output without parameter, so it will use default value of hello() function parameter.

hello()