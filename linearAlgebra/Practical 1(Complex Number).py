'''
--------------Practical 1------------------
Aim: Write a program to do the following :
1. Addition of two complex numbers.
2. Displaying the conjugate of a complex number.
3. Plotting a set of complex Number.
4. Creating a new plot by rotating the given number by a
degree 90, 180, 270 degrees and also by scaling b a number a = 1/2, a = 1/3, a = 2, etc.
'''

import matplotlib.pyplot as plt

s = {3 + 3j, 4 + 3j, 2.5 + 1j, 3.25 + 1j}

print('Select Oprations\n1: Addition of two Complex No.\n2: Plot Points from set of Complex No.\n3: Translational\n4: Scaling\n5: Ratation\nAnything: Exit')

while 'Shyamkumar':
    
    ch = int(input('Enter Choice of Operation.'))

    if ch == 1:
        c1 = complex(input('Enter Complex No. c1: '))
        c2 = complex(input('Enter Complex No. c2: '))
        print('Addition of 2 Complex Nos(c1 + c2) : ',c1 + c2)
    elif ch == 2:
        s1 = {x for x in s}
        X = [x.real for x in s1]
        Y = [x.imag for x in s1]
        plt.plot(X, Y, 'ro')
        plt.axis([-6, 6, -6, 6])
        plt.show()
    elif ch == 3:
        c1 = complex(input('Enter Translational in Complex No. Format: '))
        s1 = {x+c1 for x in s}
        print('Translational of No. is: ', s1)
    elif ch == 4:
        scale = float(input('Enter Scale point like (0.5) for 1/2: '))
        s1 = {x * scale for x in s}
        print('Scaling of No. is: ', s1)
    elif ch == 5:
        angle = int(input('Enter Angle f Rotation 30/180/270: '))
        if angle == 90:
            s1 = {x * 1j for x in s}
            print('Rotation of No. is: ', s1)
        elif angle == 180:
            s1 = {x * -1 for x in s}
            print('Rotation of No. is: ', s1)
        elif angle == 270:
            s1 = {x * 1j * -1 for x in s}
            print('Rotation of No. is: ', s1)
        else:
            print('Invalid AngleEnter Only degree 90, 180, 270\b')
    else:
        break
            
            
        




'''
1: goto C:python34/scripts/
2: pip install matplotlib

Output :
>>> 
Select Oprations
1: Addition of two Complex No.
2: Plot Points from set of Complex No.
3: Translational
4: Scaling
5: Ratation
Anything: Exit
Enter Choice of Operation.1
Enter Complex No. c1: 2+3j
Enter Complex No. c2: 3+2j
('Addition of 2 Complex Nos(c1 + c2) : ', (5+5j))
Enter Choice of Operation.2
Path IMG="D:\SYBSCCS\[ Shyam 91 ]\[ Linear Algebra ]\Practical_1.png"
Enter Choice of Operation.3
Enter Translational in Complex No. Format: 4
('Translational of No. is: ', set([(7+3j), (8+3j), (6.5+1j), (7.25+1j)]))
Enter Choice of Operation.4
Enter Scale point like (0.5) for 1/2: 0.5
('Scaling of No. is: ', set([(1.625+0.5j), (1.25+0.5j), (2+1.5j), (1.5+1.5j)]))
Enter Choice of Operation.5
Enter Angle f Rotation 30/180/270: 180
('Rotation of No. is: ', set([(-3.25-1j), (-4-3j), (-3-3j), (-2.5-1j)]))
Enter Choice of Operation.6

'''
