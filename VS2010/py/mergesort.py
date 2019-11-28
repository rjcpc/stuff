# this doesn't work
# but was used in class
# so here it stays

def MergeSort(mylist):
	print("dividing",mylist)
	if(len(mylist)>1):
		me=len(mylist)//2
		lefthalve=mylist[:me]
		righthalve=mylist[:me]
		MergeSort(lefthalve)
		MergeSort(righthalve)
		i=0
		j=0
		k=0
	while i<len(lefthalve)and j<(righthalve):
		if lefthalve[i]<righthalve[i]:
			mylist[k]=lefthalve[i]
			i=i+1
		else:
			mylist[k]=righthalve[j]
			j=j+1
			
		k=k+1
	while i<len(righthalve):
		mylist[k]=righthalve[j]
		j=j+1
		k=k+1
	print("merging",mylist)
	
mylist=[2,22,10,5,1]
MergeSort(mylist)
print(mylist)