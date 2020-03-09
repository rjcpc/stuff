# We need install numpy in order to import it
import numpy as np

# input two matrices
mat1 = ([1, 6, 5], [3, 4, 8], [2, 12, 3])
mat2 = ([3, 4, 6], [5, 6, 7], [6, 56, 7])

# This will return dot product
res = np.dot(mat1, mat2)

# print resulted matrix
print(res)


# input two matrices of size n x m
matrix1 = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[5, 8, 1],
           [6, 7, 3],
           [4, 5, 9]]

res = [[0 for x in range(3)] for y in range(3)]

# explicit for loops
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):

            # resulted matrix
            res[i][j] += matrix1[i][k] * matrix2[k][j]

print(res)
