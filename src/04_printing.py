"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print('This is x %d, this is y %d, this is z %s' % ( x, y, z))

# Use the 'format' string method to print the same thing
text = "This is the value of x {xname}, this is y {yname}, this is z {zname}".format(xname = x, yname = y, zname = z)
print(text)

# Finally, print the same thing using an f-string
print(f"This is x {x}, this is {y}, this is z {z}")
