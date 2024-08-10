import numpy as np

# Search
np1 = np.arange(1, 11)
# [ 1  2  3  4  5  6  7  8  9 10]
np1 = np.append(np1, 3)
x = np.where(np1 == 3)
print(x)

# Written even items
y = np.where(np1 % 2 == 0)
print(y)
