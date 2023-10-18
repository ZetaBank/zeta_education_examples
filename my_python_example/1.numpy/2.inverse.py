import numpy as np

matrix = np.array([[1, 2], [3, 4]])
print(matrix)
print('------')
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)