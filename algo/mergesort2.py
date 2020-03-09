def MergeSort(mylist):
    print("Dividing:", mylist)
    if len(mylist) > 1:
        me = len(mylist)//2
        lefthalve = mylist[:me]
        righthalve = mylist[me:]
        print("lefthalve=====", lefthalve)
        print("righthalve======", righthalve)
        MergeSort(lefthalve)
        MergeSort(righthalve)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalve) and j < len(righthalve):
            if lefthalve[i] < righthalve[j]:
                mylist[k] = lefthalve[i]
                i = i+1
            else:
                mylist[k] = righthalve[j]
                j = j+1
            k = k+1
        while i < len(lefthalve):
            mylist[k] = lefthalve[i]
            i = i+1
            k = k+1
        while j < len(righthalve):
            mylist[k] = righthalve[j]
            j = j+1
            k = k+1
        print("merging:", mylist)


mylist = [2, 22, 10, 5, 1]
MergeSort(mylist)
print(mylist)
