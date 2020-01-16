s = int(input("enter size of array"))
b = []
print ("enter array elements")
for i in range(s):
    b.append(int(input()))
print (b)

def getsecondhighest(b):
    hi = mid = low = 0
    for x in b:
        if x > hi:
            low,mid,hi = mid,hi,x
        elif x < low:
            low = x
    return mid
print ("second highest is : ", getsecondhighest(b))
