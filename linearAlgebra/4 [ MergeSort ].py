

def margeSort(myList) :
       print("Dividing : ", myList)
       if len(myList) > 1 :
              me = len(myList) // 2
              lefthalve = myList[:me]
              righthalve =  myList[me:]
              margeSort(lefthalve)
              margeSort(righthalve)

              i = 0
              j = 0
              k = 0
              while i < len(lefthalve) and j < len(righthalve) :
                     if lefthalve[i] < righthalve[j]:
                            myList[k] = lefthalve[i]
                            i = i + 1
                     else:
                            myList[k] = righthalve[j]
                            j = j + 1
                     k = k + 1

              while i < len(lefthalve) :
                     myList[k] = lefthalve[i]
                     i += 1
                     k += 1

              while j < len(righthalve) :
                     myList[k] = righthalve[j]
                     j += 1
                     k += 1

              print("Marge Sort : ", myList)


mylist = [2, 22, 10, 5, 1]              
margeSort(mylist)
print("Marge Sort List : ", mylist)




'''
Output :
>>> 
Dividing :  [2, 22, 10, 5, 1]
Dividing :  [2, 22]
Dividing :  [2]
Dividing :  [22]
Marge Sort :  [2, 22]
Dividing :  [10, 5, 1]
Dividing :  [10]
Dividing :  [5, 1]
Dividing :  [5]
Dividing :  [1]
Marge Sort :  [1, 5]
Marge Sort :  [1, 5, 10]
Marge Sort :  [1, 2, 5, 10, 22]
Marge Sort List :  [1, 2, 5, 10, 22]

'''
              
                     
                     
                            
