'''
--------------Practical 4------------------
Aim: Write a program to do the following :
1. Enter an r by c matrix M(r and c begin positive integers).
2. Display M in Matrix form.
3. Display row and coulmn of matrix M.
4. Find the scalar Multiplication of M for a given Number.
5. Find the transpose of matrix M.
'''
global r, c

def printM(A):
       print("Matrix A : ")
       for i in range(r):
              print(A[i])

def printRM(A):
       print("Row of Matrix A : ")
       for i in range(r):
              print("Row {} = {}".format(i, A[i]))

def printCM(A):
       print("Coloumns of Matrix A : ")
       for j in range(c):
              print('Coloumns {} = '.format(j))
              for i in range(r):
                     print(A[i][j])
              print('\n')
def scalarMulti(A, s):
       n = [[ s*A[i][j] for j in range(c)] for i in range(r)]
       print('The Scaler Multiplication A = s*M ')
       printM(n)

def transpose(A):
       T = [[A[i][j] for i in range(r)] for j in range(c)]
       print("Transpose of M  = ")
       for j in range(c):
              print(T[j])

print("Enter Dimension of Matrix ")
r = int(input("Enter Number of Rows : "))
c = int(input("Enter Number of Columns : "))

M = []

for i in range(r):
       print("Enter Elements of Rows[{}] : ".format(i))
       M.append([])
       for j in range(c):
              n = int(input("Enter No. : "))
              M[i].append(n)



while True:
       print('''
Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit
''')
       ch = int(input("Enter Choice for Operation : "))
       if ch == 1:
              printM(M)
       elif ch == 2:
              printRM(M)
       elif ch == 3:
              printCM(M)
       elif ch == 4:
              sc = int(input("Enter Scalar Value : "))
              scalarMulti(M, sc)
       elif ch == 5:
              transpose(M)
       else :
              break        

'''
Output :
>>> 
Enter Dimension of Matrix 
Enter Number of Rows : 2
Enter Number of Columns : 2
Enter Elements of Rows[0] : 
Enter No. : 1
Enter No. : 3
Enter Elements of Rows[1] : 
Enter No. : 2
Enter No. : 5

Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit

Enter Choice for Operation : 1
The Enter Matrix A : 
[1, 3]
[2, 5]

Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit

Enter Choice for Operation : 2
Row of Matrix A : 
Row 0 = [1, 3]
Row 1 = [2, 5]

Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit

Enter Choice for Operation : 3
Coloumns of Matrix A : 
Coloumns 0 = 
1
2


Coloumns 1 = 
3
5



Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit

Enter Choice for Operation : 4
Enter Scalar Value : 5
The Scaler Multiplication s*M = 
The Enter Matrix A : 
[5, 15]
[10, 25]

Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit

Enter Choice for Operation : 5
Transpose of M  = 
[1, 2]
[3, 5]

Select Operation :
       1. Display Matrix.
       2. Display Rows of Matrix.
       3. Display Columns of Matrix.
       4. Scalar Multiplication of Matrix.
       5. Transpose of matrix.
       Other. Exit

Enter Choice for Operation : 78

'''
