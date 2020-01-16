# Strassen 

x=[[0,2],[0,1]]
print("matrix x is")
for i in range(len(x)):
    print("\t",x[i])
y=[[0,0],[3,4]]
print("matrix y is")
for j in range(len(y)):
    print("\t",y[j])

def st(a,b):
    s=[b[0][1]-b[1][1],

       a[0][0]+a[0][1],

       a[1][0]+a[1][1],

       b[1][0]+b[0][0],

       a[0][0]+a[1][1],

       b[0][0]+b[1][0],

       a[0][1]-a[1][1],

       b[1][0]+b[1][1],

       a[0][0]-a[1][0],

       b[0][0]+b[0][1]]

    p=[a[0][0]*s[0],
       s[1]*b[1][1],
       s[2]*b[0][0],
       a[1][1]*s[3],
       s[4]*s[5],
       s[6]*s[7],
       s[8]*s[9]]
    c=[
        [p[4]+p[3]-p[1]-p[5]],
        [p[0]+p[1]],
        [p[2]+p[3]],
        [p[4]+p[0]-p[2]-p[6]]
        ]
    print("strassens matrix multiplication of x and y")
    print(s)
    print(p)
    print(c)

st(x,y)

'''
Output:
>>>
matrix x is
	 [0, 2]
	 [0, 1]
matrix y is
	 [0, 0]
	 [3, 4]
strassens matrix multiplication of x and y
[-4, 2, 1, 3, 1, 3, 1, 7, 0, 0]
[0, 8, 0, 3, 3, 7, 0]
[[-9], [8], [3], [3]]
'''




     
     
