import numpy as np
from scipy.linalg import rref

# Define your matrix
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Perform row echelon form
rref_matrix, pivot_columns = rref(matrix)

print("Row Echelon Form:")
print(rref_matrix)
print("Pivot Columns:", pivot_columns)
