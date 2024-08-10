import numpy as np

# Filtering Numpy arrays with Boolean index lists
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x = [True, True, False, False, True, False, True, True, False, False]

# print(np1)
# print(np1[x])
"""
filtered = []
for thing in np1:
    if thing % 2:
        filtered.append(False)
    else:
        filtered.append(True)
print(filtered)
print(np1[filtered])
"""

# Shortcut !
filtered = np1 % 2 == 0
print(np1[filtered])
