l=int(input('Enter lengh of vector :'))
u=[]
v=[]
c=[]
print('Enter elements of first vector u ')
for i in range(l):
    n=int(input('Enter no : '))
    u.append(n)
print('Enter elements of second vector v : ')
for i in range(l):
    n=int(input('Enter no : '))
    v.append(n)
print('Enter elements of coeficient : ')
c1=int(input('Enter first coeficent : '))
c2=int(input('Enter second coeficient : '))
newface=[c1*u[i]+c2*v[i] for i in range(len(u))]
print('New Face of u and v = ',newface)
avgface=[(u[i]+v[i])/2 for i in range(len(u))]
print('Average face of u and v = ', avgface)
