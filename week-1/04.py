# Float Divisions

x = float(input("What is x? "))
y = float(input("What is y? "))

z = x / y

# Round this to 3 digits. The / can be without spaces, no issue at all.

# z = round(x/y, 3)

# print (z)

# Using fstring to format the results

z = x/y
print(f"{z:.3f}")

# This fstring rounds to 2 float points after decimal.