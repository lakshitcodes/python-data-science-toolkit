# If/Else conditions are used to decide to do something based on something being true or false

x = 3
y = 50

# Comparison operators (== , != , > , < , >= , <=) - Used to compare values

# Simple if
if x > y:
    print(f"{x} is greater than {y}")

# If-Else
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print("They both are equal")
else:
    print(f"{y} is greater than {x}")

# Nested-if
if x > 2:
    if x <= 10:
        print(f"{x} is greater than 2 but less than equal to 10")

# Logical Operators (and , or , not) - Used to combine conditional statements
# and
if x > 2 and x <= 10:
    print(f"{x} is greater than 2 but less than equal to 10")

# or
if x > 2 or x <= 10:
    print(f"{x} is greater than 2 or less than equal to 10")

# not
if not (x == y):
    print("X is not equal to Y")


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object.

numbers = [1, 2, 3, 4, 5]

# in
if x in numbers:
    print("x is there")

# not in
if y not in numbers:
    print("y is not in numbers")

# Identity Operators (is , is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memroy location:

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is not y)
