'''
--------------Practical 6------------------
Aim: Write a program to do the following :
1. Write a program to check if Matrix is Invertible if then inverse Exist find the inverse.
'''
def printMatrix(A):
    for i in range(len(A)):
        print(A[i])

def transpose(A):
    T = [[A[i][j] for i in range(len(A))] for j in range(len(A))]
    return T

c = int(input('Enter the rows and columns of square Matrix : '))

r=c
M = []
for i in range(r):
    print('Enter element of row', i)
    M.append([])
    for j in range(c):
        n = int(input('Enter No. : '))
        M[i].append(n)

print('The Entered Matrix M1 is :')
printMatrix(M)
determinant = 0
if r == 2:
    determinant = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    print('Determinant : ',determinant)
    if determinant == 0 :
        print('Matrix is Not Invertible. ')
    else:
        print('Matrix is Invertible. ')
        CFM = []
        for i in range(2):
            CFM.append([])
            CFM[0].append(M[1][1])
            CFM[0].append(-(M[0][1]))
            CFM[0].append(-(M[1][0]))
            CFM[0].append(M[0][0])
            print('Co-factor Matrix ')
            printMatrix(CFM)
            M1 = []
            for i in range(1):
                M1.append([])
                for j in range(2):
                    M1[i].append(CFM[i][j]/determinant)

            print('Inverse of A Matrix M is : ')
            printMatrix(M1)
else:
    for i in range(3):
        determinant = determinant + (M[0][i]*M[1][(i+1)%3]*M[2][(i+2)%3] - M[1][(i+2)%3]*M[2][(i+1)%3])
        print('Determinant ',determinant)
        if determinant == 0 :
            print('Matrix is Not Invertible. ')
        else:
            print('Matrix is Invertible. ')
            CFM = []
        for i in range(3):
            CFM.append([])
            for j in range(3):
                v = (M[(i+1)%3][(j+1)%3] * M[(i+2)%3][(j+2)%3]) - (M[(i+1)%3][(j+2)%3] * M[(i+2)%3][(j+1)%3])
                CFM[i].append(v)
    print('Co-factor Matrix ')
    printMatrix(CFM)
    AdjM = transpose(CFM)

    M1 = []
    for i in range(3):
        M1.append([])
        for j in range(3):
            M1[i].append(AdjM[i][j]/determinant)

    print('Inverse of a Matrix M is : ')
    printMatrix(M1)
        
            




        

'''
Output :
>>> 
Enter the rows and columns of square Matrix : 2
Enter element of row 0
Enter No. : 1
Enter No. : 2
Enter element of row 1
Enter No. : 3
Enter No. : 4
The Entered Matrix M1 is :
[1, 2]
[3, 4]
Determinant :  -2
Matrix is Invertible. 
Co-factor Matrix 
[4, -2, -3, 1]
Inverse of A Matrix M is : 
[-2.0, 1.0]
Co-factor Matrix 
[4, -2, -3, 1, 4, -2, -3, 1]
[]
Inverse of A Matrix M is : 
[-2.0, 1.0]
'''
