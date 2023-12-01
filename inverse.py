import numpy as np

# Define your matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate the inverse
inverse_matrix = np.linalg.inv(matrix)

print(f"Inverse of the matrix:\n{inverse_matrix}")
