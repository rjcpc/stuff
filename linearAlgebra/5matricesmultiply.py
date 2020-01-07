global r1,c1,r2,c2
# display M in matrix format
def printmatrix(A):
    for i in range(len(A)):
        print (A[i])

def matrixadd(A,B):
    C=[A[i][j]+B[i][j] for i in range(len(B[0])) for j in range(len(A))]
    print("Addition of two matrices is : ")
    printmatrix(C)

def matrixmul(A,B):
    #doesn't work
    C=[sum(A[i][k]*B[k][j]) for k in range(len(B)) for j in range(len(B[0])) for i in range(len(A))]
    print("Multiplication of two matrices is : ")
    printmatrix(C)

def matrixvectormul(A,v):
    C=[sum(A[i][j]*v[j] for j in range(len(v)))for i in range(len(A))]
    print("Matrix vector multiplication is : ")
    printmatrix(C)

def vectormatrixmul(v,A):
    C=[sum(v[j]*A[j][i]for j in range(len(v)))for i in range(len(A))]
    print("Vector matrix multiplication is : ")
    printmatrix(C)


#Enter rXc matrix M
print('enter demension of Matrix1 : ')
r1=int(input('enter no of rows : '))
c1=int(input('enter no of columns : '))
M=[]

for i in range(r1):
    print("enter elements of row, ",i)
    M.append([])
    for j in range(c1):
        n=int(input("Enter number : "))
        M[i].append(n)

    print("The entered matrix m1 is : ")
    printmatrix(M)


#Enter rXc matrix N
print('enter demension of matrix2 : ')
r2=int(input('enter no of rows : '))
c2=int(input('enter no of columns : '))
N=[]

for i in range(r2):
    print('enter no of rows : ',i)
    N.append([])
    for j in range(c2):
        n=int(input('enter no : '))
        N[i].append(n)
        print('the entered matrix M2 is :')
        printmatrix(N)




print('select operation')
print('1.Matrix addition')
print('2.Matrix multiplication')
print('3.Matrix vector multiplication')
print('4.Vector matrix multiplication')
print('5.EXIT')


while True:
    ch=int(input("enter choice "))
    if ch==1:
        if(r1,c1)==(r2,c2):
            matrixadd(M,N)
        else:
            print("Invalid data")
    elif ch==2:
        if c1==c2:
            matrixmul(M,N)
        else:
            print("Invalid data")
    elif ch==3:
        s=input("enter elements of vector separated by spaces : ")
        v=[int(x) for x in s.split()]
        #print(len(v))
        if len(v)!=c1:
            print("invalid data")
        else:
            matrixvectormul(M,v)
    elif ch==4:
        s=input("enter elements of vector separated by spaces : ")
        v=[int(x) for x in s.split()]
        if len(v)!=r1:
            print("invalid data")
        else:
            vectormatrixmul(v,M)
        
    elif ch==5:
        break
    else:
        break


