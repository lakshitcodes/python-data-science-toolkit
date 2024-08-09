import numpy as np

# Slicing Numpy arrays
np1 = np.arange(15)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

# Return 2,3,4,5
print(np1[2:6])

# Return from something till the end of the array ?
print(np1[3:])  # Nothing means till the terminal

# Return negative slices
print(np1[-3:-1])  # In the reverse order

# Steps
print(np1[1:5:2])

# Steps on the entire array
print(np1[::2])

# Slice a 2D array
np2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# Pull out a single item
print(np2[1][2])

# Slice a 2D array
print(np2[0:1, 1:3])

# Slice from both rows
print(np2[0:, 1:3])
