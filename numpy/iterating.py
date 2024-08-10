import numpy as np

# 1-D
np1 = np.arange(1, 11)

for x in np1:
    print(x)

# 2-D array
np2 = np.arange(1, 11).reshape(2, 5)
for x in np2:
    # Print rows
    # print(x)

    # Accessing all the elements
    for y in x:
        print(y)

# 3-D array
np3 = np.arange(1, 13).reshape(2, 2, 3)
"""
for x in np3:
    # print(x)
    for y in x:
        # print(y)
        for z in y:
            print(z)
"""

# Use np.nditer()
# No need to embedding loop insides loops
for x in np.nditer(np3):
    print(x)
