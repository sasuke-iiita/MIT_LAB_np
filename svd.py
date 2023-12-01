import numpy as np

# Define your matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Perform Singular Value Decomposition
U, Sigma, Vt = np.linalg.svd(matrix)

print("U matrix:")
print(U)

print("\nSigma matrix:")
print(np.diag(Sigma))

print("\nVt matrix:")
print(Vt)
