import numpy as np
from scipy.linalg import lu

# Define your matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Perform LU decomposition
P, L, U = lu(matrix)

print("P (permutation matrix):\n", P)
print("L (lower triangular matrix):\n", L)
print("U (upper triangular matrix):\n", U)
