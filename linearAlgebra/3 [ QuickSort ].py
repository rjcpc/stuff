'''
QuickSort 
'''

import random

def par(sample, start, end):
       print("Sample : ",sample)
       pivot = sample[end]
       print("pivot : ", pivot)
       index = start
       print("Index : ", index)
       current = start
       print("Current : ",current)
       while current < end :
              if sample[current] <= pivot:
                     print(sample[index])
                     print(sample[current])
                     sample[index], sample[current] = sample[current], sample[index]
                     index += 1
              current += 1
       sample[index], sample[end] = sample[end], sample[index]
       print("After Partition : ", sample)
       return index

def quickSort(sample, start, end) :
       if start < end:
              index = par(sample, start, end)
              quickSort(sample, start, index-1)
              quickSort(sample, index + 1, end)

sample = random.sample(range(0, 20), 10)
#print(sample)
quickSort(sample, 0, 9)

'''
Output:
>>>
Sample :  [8, 14, 2, 13, 18, 1, 7, 12, 6, 17]
pivot :  17
Index :  0
Current :  0
8
8
14
14
2
2
13
13
18
1
18
7
18
12
18
6
After Partition :  [8, 14, 2, 13, 1, 7, 12, 6, 17, 18]
Sample :  [8, 14, 2, 13, 1, 7, 12, 6, 17, 18]
pivot :  6
Index :  0
Current :  0
8
2
14
1
After Partition :  [2, 1, 6, 13, 14, 7, 12, 8, 17, 18]
Sample :  [2, 1, 6, 13, 14, 7, 12, 8, 17, 18]
pivot :  1
Index :  0
Current :  0
After Partition :  [1, 2, 6, 13, 14, 7, 12, 8, 17, 18]
Sample :  [1, 2, 6, 13, 14, 7, 12, 8, 17, 18]
pivot :  8
Index :  3
Current :  3
13
7
After Partition :  [1, 2, 6, 7, 8, 13, 12, 14, 17, 18]
Sample :  [1, 2, 6, 7, 8, 13, 12, 14, 17, 18]
pivot :  14
Index :  5
Current :  5
13
13
12
12
After Partition :  [1, 2, 6, 7, 8, 13, 12, 14, 17, 18]
Sample :  [1, 2, 6, 7, 8, 13, 12, 14, 17, 18]
pivot :  12
Index :  5
Current :  5
After Partition :  [1, 2, 6, 7, 8, 12, 13, 14, 17, 18]
'''
