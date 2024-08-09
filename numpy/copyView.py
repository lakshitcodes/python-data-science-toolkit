import numpy as np

# Copy vs View
np1 = np.array([0, 1, 2, 3, 4, 5])

# Create a view
np2 = np1.view()  # Creates a shallow copy
# This can be done without using the view option

print(f"Original NP1 ; {np1}")
print(f"Original NP2 ; {np2}")

np1[0] = 41

print(f"Changed NP1 ; {np1}")
print(f"Original NP2 ; {np2}")

# Create a copy
np3 = np1.copy()  # Creates a deep copy

print(f"Original NP1 ; {np1}")
print(f"Original NP3 ; {np3}")

np1[0] = 42

print(f"Changed NP1 ; {np1}")
print(f"Original NP3 ; {np3}")
