import numpy as np

# Define your matrix
matrix = np.array([[4, -1],
                   [-1, 5]])

# Check if the matrix is positive definite
eigenvalues = np.linalg.eigvals(matrix)

if all(eig > 0 for eig in eigenvalues):
    print("The matrix is positive definite.")
else:
    print("The matrix is not positive definite.")
