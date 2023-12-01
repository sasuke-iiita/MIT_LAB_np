import numpy as np

# Define your matrices
matrix_A = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix_B = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Matrix multiplication
result_matrix = np.dot(matrix_A, matrix_B)

# Row space of the result matrix
row_space_result = np.linalg.matrix_rank(result_matrix)
print(f"Row space dimension of result matrix: {row_space_result}")

# Column space of the result matrix
column_space_result = np.linalg.matrix_rank(result_matrix.T)
print(f"Column space dimension of result matrix: {column_space_result}")

# Null space (Kernel) of the result matrix
null_space_basis_result = np.linalg.svd(result_matrix)[2]
null_space_dimension_result = result_matrix.shape[1] - np.count_nonzero(np.isclose(np.linalg.svd(result_matrix)[1], 0))
print(f"Null space dimension of result matrix: {null_space_dimension_result}")
print(f"Null space basis of result matrix (as columns):\n{null_space_basis_result}")
