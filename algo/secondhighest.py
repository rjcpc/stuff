print ("enter size of array")
s=int(input())
i=0
b=[]
print ("enter array elements")
while i<s:
    b.append(int(input()))
    i=i+1
print (b)

def getsecondhighest(b):
    hi=mid=low=0
    for i in range(len(b)):
        x=b[i]
        if x>hi:
            low=mid
            mid=hi
            hi=x
        elif x<low:
            low=x
    return mid
print ("second highest is : ", getsecondhighest(b))
