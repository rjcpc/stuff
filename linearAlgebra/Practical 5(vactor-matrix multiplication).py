'''
--------------Practical 5------------------
Aim: Write a program to do the following :
1. Find The vactor-matrix multiplication of a r by c matrix M with an c-vector u.
2. Find the matrix-matrix product of M with a c by p Matrix N.
'''

global r1, c1, r2, c2

def printMatrix(A):
    for i in range(len(A)):
        print(A[i])

def matrixAdd(A, B):
    C=[[A[i][j] + B[i][j] for j in range(len(B[0]))] for i in range(len(A))]
    print('Addition of Two Matrix = ')
    printMatrix(C)

def matrixMul(A, B):
    C=[[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    print('Multiplication of Two Matrix = ')
    printMatrix(C)

def matrixVecMul(A, v):
    C=[sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
    print('Matrix Vector Multiplication(M1 * v) = ')
    printMatrix(C)

def vecMatrixMul(v, A):
    C=[sum(v[j]*A[j][i] for j in range(len(v))) for i in range(len(A))]
    print('Matrix Vector Multiplication(v * MI) = ')
    printMatrix(C)
# Matrix from User
'''   
print('Enter Dimension of Matrix1 : ')
r1 = int(input('Enter No. of Rows : '))
c1 = int(input('Enter No. of Columns : '))
M = []
for i in range(r1):
    print('Enter Elements of Row ',i)
    M.append([])
    for j in range(c1):
        n = int(input('Enter No. : '))
        M[i].append(n)
''' 
# Matrix defined by me
M = [[1,2],[3,4]]
r1=2
c1=2
print('The Entered Matrix M1 is ')
printMatrix(M)

# Matrix from User
'''
print('Enter Dimension of Matrix2 : ')
r2 = int(input('Enter No. of Rows : '))
c2 = int(input('Enter No. of Columns : '))
N = []
for i in range(r2):
    print('Enter Elements of Row ',i)
    N.append([])
    for j in range(c2):
        n = int(input('Enter No. : '))
        N[i].append(n)
'''  
# Matrix defined by me
N = [[4,3],[2,1]]
r2=2
c2=2
print('The Entered Matrix M2 is ')
printMatrix(N)

print('''Select Opration
1 : Matrix Addition
2 : Matrix Multiplication
3 : Matrix Vector Multiplication
4 : Vector matrix Multiplication
anything : Exit
''')

while True:
    ch = int(input('Enter Choice of opration '))
    if ch == 1:
        if (r1, c1) == (r2, c2):
            matrixAdd(M, N)
        else:
            print('Invalid Matrix: To add Two Matrices Matrix1.Column == Matrix2.Rows')
    elif ch == 2:
        if c1 == r2:
            matrixMul(M, N)
        else:
            print('Invalid Matrix: To Multiply Two Matrices Matrix1.Column == Matrix2.Rows')
    elif ch == 3:
        s = input('Enter Elements of Vector Seprated by Spaces : ')
        v = [int(x) for x in s.split()]
        print(len(v))
        if len(v) != c1:
            print('Invalid Vector and Vector of {} elements(Columns of M1)'.format(c1))
        else:
            matrixVecMul(M, v)
    elif ch == 4:
        s = input('Enter Elements of Vector Seprated by Spaces : ')
        v = [int(x) for x in s.split()]
        print(len(v))
        if len(v) != r1:
            print('Invalid Vector and Vector of {} elements(Columns of M1)'.format(r1))
        else:
            vecMatrixMul(v, M)
    else:
        break
            
'''
Output :
>>> 
The Entered Matrix M1 is 
[1, 2]
[3, 4]
The Entered Matrix M2 is 
[4, 3]
[2, 1]
Select Opration
1 : Matrix Addition
2 : Matrix Multiplication
3 : Matrix Vector Multiplication
4 : Vector matrix Multiplication
anything : Exit

Enter Choice of opration 1
Addition of Two Matrix = 
[5, 5]
[5, 5]
Enter Choice of opration 2
Multiplication of Two Matrix = 
[8, 5]
[20, 13]
Enter Choice of opration 3
Enter Elements of Vector Seprated by Spaces : 4 5
2
Matrix Vector Multiplication(M1 * v) = 
14
32
Enter Choice of opration 4
Enter Elements of Vector Seprated by Spaces : 5 4
2
Matrix Vector Multiplication(v * MI) = 
17
26
Enter Choice of opration 5
'''
