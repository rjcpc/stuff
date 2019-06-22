#/usr/bin/python3
#set in python


#create two sets
set1=set()
set2=set()


#add values in first set
for i in range(1,6):
    set1.add(i)

 
#add values in second set
for i in range(3,8):
    set2.add(i)


print("set1= ",set1)
print ("set2= ",set2)
print("\n")

set3=set1 | set2  # set3=set1.union(set2)
set4=set1 & set2 # set4=set1.intersection(set2)
set5=set1-set2

print("union= ",set3)
print ("intersection= ",set4)
print ("difference= ",set5)

print("\n")

if ( set1 > set2 ):
    print ("set1 is superset of set2")   # set1.issupersetof(set2)

elif( set2 > set1 ):
    print("set1 is subset of set2")  # set1.issubsetof(set2)

elif (set2==set1):
    print("set 1 and set 2 are equal")  

else:
    print("set 1 and set 2 are disjoint sets")





if ( set3 > set4 ):
    print ("set 3 is superset of set 4")   # set1.issupersetof(set2)

elif( set4 > set3 ):
    print("set 3 is subset of set 4")  # set1.issubsetof(set2)

elif (set3==set4):
    print("set 3 and set 4 are equal")  

else:
    print("set 3 and set 4 are disjoint sets")
