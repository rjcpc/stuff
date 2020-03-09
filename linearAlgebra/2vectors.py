num_of_elements = int(input("Enter number of elements in vector required : "))
u = []
v = []
for i in range(num_of_elements):
    a = int(input("Enter the values in first vector : "))
    u.append(a)

for i in range(num_of_elements):
    a = int(input("Enter the values in second vector : "))
    v.append(a)


def add(x, y):
    return [x[i]+y[i] for i in range(len(x))]


def sub(x, y):
    return [x[i]-y[i] for i in range(len(x))]


def mul(x, y):
    num = int(input("Enter scalar number : "))
    return {str(u): [num*x[i] for i in range(len(x))], str(v): [num*y[i] for i in range(len(y))]}


def dot(x, y):
    return sum([x[i]*y[i] for i in range(len(x))])


while True:
    print("\n Choose option : ")
    print("1 : Addition of vectors")
    print("2 : Subtraction of vectors")
    print("3 : Scalar multiplication")
    print("4 : Dot product")
    print("5 : Exit")
    choice = int(input())
    if choice == 1:
        print('Addition of two vectors is : \n', add(u, v))
    elif choice == 2:
        print('Subtraction of two vectors is : \n', sub(u, v))
    elif choice == 3:
        print('Scalar multiple of two vectors is : \n', mul(u, v))
    elif choice == 4:
        print('Dot product of two vectors is : \n', dot(u, v))
    elif choice == 5:
        print("Exit ")
        break
    else:
        print("Invalid Choice")
