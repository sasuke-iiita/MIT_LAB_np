import numpy as np

# Define your matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Calculate the determinant
determinant = np.linalg.det(matrix)

print(f"Determinant of the matrix: {determinant}")
