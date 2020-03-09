num_of_rows = int(input("Enter number of rows in matrix : "))
num_of_columns = int(input("Enter number of columns in matrix : "))

# DOES NOT WORK => matrix=[[0]*num_of_columns]*num_of_rows

# create empty matrix
# create empty list of given size
matrix = [None] * num_of_rows
for i in range(num_of_rows):
    matrix[i] = [None] * num_of_columns

# prompt values
for i in range(num_of_rows):
    for j in range(num_of_columns):
        print("Row ", i+1, "Column ", j+1)
        a = int(input("Enter the value: "))
        matrix[i][j] = a

print("The matrix is")
for i in matrix:
    print(i)


while True:
    print("\n Choose option : ")
    print("1 : Print rows of Matrix")
    print("2 : Print columns of Matrix")
    print("3 : Print Scalar multiple of Matrix")
    print("4 : Print Transpose of Matrix")
    print("5 : Exit")
    choice = int(input())
    if choice == 1:
        for index, row in enumerate(matrix):
            print('Row', index+1, ": ", row)
    elif choice == 2:
        for i in range(num_of_columns):
            print('Column', i+1, ": ", [row[i] for row in matrix])
    elif choice == 3:
        scalar = int(input("Enter the scalar: "))
        # create empty list of given size
        Scalar_multiple = [None] * num_of_rows
        for i in range(num_of_rows):
            Scalar_multiple[i] = [None] * num_of_columns

        for i in range(num_of_rows):
            for j in range(num_of_columns):
                Scalar_multiple[i][j] = matrix[i][j]*scalar

        print("Scalar multiple is :")
        for i in Scalar_multiple:
            print(i)
    elif choice == 4:
        print("Transpose is :")
        transpose = []
        for i in range(num_of_columns):
            new_row = [row[i] for row in matrix]
            transpose.append(new_row)

        for i in transpose:
            print(i)
    elif choice == 5:
        print("Exit ")
        break
    else:
        print("Invalid Choice")
