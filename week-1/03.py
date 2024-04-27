# Playing with integers.
# Int mean all negative and positive numbers in Python, excluding decimels.
# Operations supported = + . - . * . / . %
# % = Modulus operator, returns the remainder of the division of the number to the left by the number on its right.

# x = input("Enter the 1st Number: ")
# y = input("Enter the 2nd Number: ")

# z = int(x) + int(y)
# Int is also a function in Python that will convert string to number to perform the operations.

# This program is not efficient. Let's make it efficient with less code.

x = int(input("What is x? "))
y = int(input("What is y? "))

# Function on function. The one inside parenthesis is done first i.e. first input one and then int one. The return value of inner function i.e. input in this case is the argument/parameter of the second function.

print (x + y)

# No need for declaring z variable when it is only going to be used onces. Also, since x & y have been converted to integers, it will be added as integers.

# Making code efficient not only to be considered when making code efficient, but also the code readibility. Don't make it to complicated in name of efficiency, which increases probility of errors.