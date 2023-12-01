import numpy as np

# Coefficient matrix
A = np.array([[2, 3, -1],
              [4, 1, 2],
              [3, 6, 2]])

# Right-hand side vector
B = np.array([8, 7, 9])

# Solve the system of linear equations
solution = np.linalg.solve(A, B)

print("Solution:", solution)
