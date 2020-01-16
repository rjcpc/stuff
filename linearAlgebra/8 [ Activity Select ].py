# Activity Select

def printMaxActivity(s, f):
    n = len(f)
    print('The Following Activitices are selected.')
    i = 0
    print(i)
    for j in range(n):
        if (s[j] >= f[i]):
            print(j)
            i = j

s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivity(s, f)

'''
Output:
>>>
The Following Activitices are selected.
0
1
3
4
'''
