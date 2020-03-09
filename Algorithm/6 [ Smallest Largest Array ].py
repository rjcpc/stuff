# Smallest Largest Array

a = [84, 25, 32, 12, 44]
print("Array A is: ", a)
for i in range(len(a)):
    min_ind = i
    print(min_ind)
    for j in range(i + 1, len(a)):
        if a[min_ind] > a[j]:
            min_ind = j
    print("Elemnet swapping here")
    a[i], a[min_ind] = a[min_ind], a[i]
    print(a[i], a[min_ind])
    print("Iteration {} :".format(i+1))
    print(a)
    print("Smallest elemnet is:{} :".format(a[0]))
    print("Greatest element is :{} ".format(a[len(a)-1]))

'''
Output:
>>> 
Array A is: [84, 25, 32, 12, 44]
0
Elemnet swapping here
12 84
Iteration 1:
[12, 25, 32, 84, 44]
Smallest elemnet is:12
Greatest element is :44
1
elemnet swapping here
25 25
Iteration 2:
[12, 25, 32, 84, 44]
Smallest elemnet is:12
Greatest element is :44
2
elemnet swapping here
32 32
Iteration 3:
[12, 25, 32, 84, 44]
Smallest elemnet is:12
Greatest element is :44
3
elemnet swapping here
44 84
Iteration 4:
[12, 25, 32, 44, 84]
Smallest elemnet is:12
Greatest element is :84
4
elemnet swapping here
84 84
Iteration 5:
[12, 25, 32, 44, 84]
Smallest elemnet is:12
Greatest element is :84
'''
