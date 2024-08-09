import numpy as np

# Docs for universal functions : https://numpy.org/doc/stable/reference/ufuncs.html


# Numpy Universal functions
np1 = np.array([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)

# Square root of each element
# print(np.sqrt(np1))

# Absolute value
print(np.absolute(np1))

# Exponentials - This gives the value of e^x where x is the element in the numpy array
print(np.exp(np1))

# Min/Max
print(np.max(np1))
print(np.min(np1))

# Sign positive or negative
print(np.sign(np1))


# Trigonometry Functions
# sin/log/cos
print(np.sin(np1))
