import numpy as np

# np.sort()
np1 = np.array([6, 4, 2, 6, 76, 2, 1, 5, 2, 3, 5, 2, 2])
print(np.sort(np1))


# Alphabetical
np2 = np.array(["dog", "cat", "apple", "banana", "elephant"])
print(np.sort(np2))

# Booleans T/F
np3 = np.array([True, False, False, True, True, False])
print(np.sort(np3))

# It returns a copy not change the original
