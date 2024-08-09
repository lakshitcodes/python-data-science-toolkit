import numpy as np

# numpy - Numeric Python
# ndarray - n-dimensional array

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
# print(arr.shape)  # returns the number of elements in the array

# Range
np1 = np.arange(10)
# print(np1)

# Step
np2 = np.arange(0, 5, 2)
# print(np2)

# Zeroes
np4 = np.zeros(10)
# print(np4)

# Mutli dimensional zeroes
np5 = np.zeros((2, 10))
# print(np5)

# Full
np6 = np.full((10), 6)
# print(np6)

# Multidimensional Full
np7 = np.full((2, 10), 6)
# print(np7)

# Convert python lists to numpy
myList = [1, 2, 3, 4, 5]
np8 = np.array(myList)
print(np8)

# Perform basic operations
# print(arr + 10)
# print(arr * 2)


# Create a 2D array
arr2 = np.array([[1, 2], [6, 7]])

# print(arr2)

# Perform matrix operations
# Transpose of the matrix
# print(arr2.T)
# Matrix Multiplication
# print(np.dot(arr2, arr2))  # matmul can also be used in place of dot


# Generate random numbers
random_array = np.random.rand(3, 3)
# print(random_array)

# Statistical Operations
# print(np.mean(random_array))  # Mean of all elements
# print(np.std(random_array))  # Standard deviation
