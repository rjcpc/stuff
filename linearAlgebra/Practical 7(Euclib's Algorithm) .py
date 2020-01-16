'''
--------------Practical 7------------------
Aim: Write a program to do the following :
1. Enter a positive number N and find numbers a and b such that a2 - b2 = N
2. Find the gcd of two number using Euclib's Algorithm
'''

import math

pf = []
n = int(input('Enter a No.: '))
x = n

while n % 2 == 0:
    pf.append(2)
    n = n/2
i = 3

while i <= math.sqrt(n):
    while n%i == 0:
        pf.append(i)
        n = n/i
    i += 2
if n > 2:
    pf.append(n)
    
print('Prime Factors of {} are {}'.format(x, pf))
pf1 = set(pf)
nf = 1

for f in pf1:
    cnt = 0
    for f1 in pf:
        if f == f1:
            cnt += 1
        nf *= cnt + 1
        
print('No. of Factors of {} = {}.'.format(x, nf))
print('No. of Positive integral solutions = {}.'.format(nf/2))

'''
Output :
>>> 
Enter a No.: 25
Prime Factors of 25 are [5, 5]
No. of Factors of 25 = 6.
No. of Positive integral solutions = 3.0.
'''
