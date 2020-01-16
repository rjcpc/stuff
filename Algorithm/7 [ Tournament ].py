# Touranament

s = int(input('Enter Size of Array: '))
i = 0
b = []
print('Enter Array Element')
while i < s:
    b.append(int(input()))
    i = i + 1

print(b)

def getSecondHighest(b):
    hi  = mid = lo = 0
    for i in range(0, len(b)):
        x = b[i]
        if (x > hi):
            lo = mid
            mid = hi
            hi = x
        elif (x < hi and x > mid):
            lo = mid
            mid = x
        elif x < lo:
            lo = x
    return mid

print('Seconde Highest Element given in array ',getSecondHighest(b))


'''
Output:
>>> 
Enter Size of Array: 5
Enter Array Element
45
12
32
64
8
[45, 12, 32, 64, 8]
Seconde Highest Element given in array  45
'''

