print("matrix A is ")

A = [[1, 2, 4], [3, 4, 3], [5, 6, 2]]
for i in A:
    print(i)

print("rows in A ", len(A))
print("columns in A ", len(A[0]))
print("\n\n")
print("matrix B is ")

B = [[2, 7, 8, 1], [1, 9, 6, 0], [2, 3, 1, 4]]
for i in B:
    print(i)

print("rows in A ", len(B))
print("columns in A ", len(B[0]))

result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


for row in A:
    for row_element in row:
        print(row_element)
       # for something in B[0][]:


# explicit for loops
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):

            # resulted matrix
            result[i][j] += A[i][k] * B[k][j]

print(result)
