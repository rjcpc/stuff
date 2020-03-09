'''
--------------Practical 2----------------------
Aim : Wright a Program to do the Following:
1. Enter a vactor u as a n-list.
2. Enter amount another vector v as a n-list.
3. Find the vectore au + bv for different values of a and b.
4. Find the dot product u and v.
'''


def addv(x, y):
    return [x[i] + y[i] for i in range(len(x))]


def subv(x, y):
    return [x[i] - y[i] for i in range(len(x))]


def multiv(x, s):
    return [s*x[i] for i in range(len(x))]


def dotprod(x, y):
    return sum([x[i]*y[i] for i in range(len(x))])


v = []
u = []

n = int(input("Enter no of elements you want to add in vector : "))
print("Enter element of vector u : ")
for i in range(n):
    elemu = int(input("Enter Element : "))
    u.append(elemu)
    print("Vector u = {}".format(u))

print("Enter element of vector v : ")
for i in range(n):
    elemv = int(input("Enter Element : "))
    v.append(elemv)
    print("Vector v = {}".format(v))

while True:
    print('''Select Vector Opration
       1 : Addition
       2 : Substraction
       3 : Scalar Multiplication
       4 : Dot Product
       Other : Exit
       ''')
    op = int(input("Enter Your Choice : "))
    if op == 1:
        print("Addition of Vector u & v is (u + v) : ", addv(u, v))
    elif op == 2:
        print("Substraction of Vector u & v is (u - v) : ", subv(u, v))
    elif op == 3:
        a = int(input("Enter Value of a : "))
        print("Scalar Multiplication of Vector u with a is (u.a) : ", multiv(u, a))
    elif op == 4:
        print("Dot Product of Vector u & v is (u . v) : ", dotprod(u, v))
    else:
        break

"""
Output:
>>> 
Enter no of elements you want to add in vector : 2
Enter element of vector u : 
Enter Element : 4
Vector u = [4]
Enter Element : 5
Vector u = [4, 5]
Enter element of vector v : 
Enter Element : 6
Vector v = [6]
Enter Element : 7
Vector v = [6, 7]
Select Vector Opration
       1 : Addition
       2 : Substraction
       3 : Scalar Multiplication
       4 : Dot Product
       Other : Exit
       
Enter Your Choice : 1
Addition of Vector u & v is (u + v) :  [10, 12]
Select Vector Opration
       1 : Addition
       2 : Substraction
       3 : Scalar Multiplication
       4 : Dot Product
       Other : Exit
       
Enter Your Choice : 2
Substraction of Vector u & v is (u - v) :  [-2, -2]
Select Vector Opration
       1 : Addition
       2 : Substraction
       3 : Scalar Multiplication
       4 : Dot Product
       Other : Exit
       
Enter Your Choice : 3
Enter Value of a : 2
Scalar Multiplication of Vector u with a is (u.a) :  [8, 10]
Select Vector Opration
       1 : Addition
       2 : Substraction
       3 : Scalar Multiplication
       4 : Dot Product
       Other : Exit
       
Enter Your Choice : 4
Dot Product of Vector u & v is (u . v) :  59
Select Vector Opration
       1 : Addition
       2 : Substraction
       3 : Scalar Multiplication
       4 : Dot Product
       Other : Exit
       
Enter Your Choice : 
"""
