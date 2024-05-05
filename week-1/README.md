# Summary - Week 1

So here's the summary of what I have learnt and practiced in week 1.

Python is an interpreted language, so you must have Python (Python intrepreter) installed on your computer that will convert the python code line by line to machine code (zeros and ones - binary)

print is a function that takes argument and print the arguments/parameters on the screen.

When we declare a variable, value is passed to it from right to left.

In coding, never expect user will add correct value. So for example, we have declated a name variable (string) where it will save user name, we can format it using different built-in string functions.

For example,

1. name = name.capitalize()
2. name = name.title()
3. name = name.strip()

By default, a declared variable is string in python, so what if we want to make a calculator? We can only make calculation operations on integers. So, we need to run another function to convert strings to integers.

x = int(input ("What is value of x? "))

int does not support decimals, so for that we need to use float.

We can round the values using round functions. By default, it rounds all decimels.

round (x/y)

If we want to specify to round to 3, we can specify like this

round (x/y, 3)