import numpy as np

# Create 1D numpy array and get shape
np1 = np.arange(1, 13)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
print(np1.shape)

# Create 2D array and get shape (rows/columns)
"""
np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
print(np2)
print(np2.shape)
"""

# Reshape 2D
np3 = np1.reshape(3, 4)
print(np3)
print(np3.shape)


# Reshape 3D
np4 = np1.reshape(2, 3, 2)
print(np4)

# Flatten to 1D
np5 = np4.reshape(-1)
print(np5)
