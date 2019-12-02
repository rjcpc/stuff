import random
def partition(sample,start,end):
            print("Sample:",sample)
            pivot=sample[end]
            index=start
            current=start
            while(current<end):
                        if(sample[current]<=pivot):
                                    sample[index],sample[current]=sample[current],sample[index]
                                    index+=1
                        current+=1
            sample[index],sample[end]=sample[end],sample[index]
            print("after partition",sample)
            return index
def quickSort(sample,start,end):
            if(start<end):
                        index=partition(sample,start,end)
                        quickSort(sample,start,index-1)
                        quickSort(sample,index+1,end)
#sample=
['ram','shayam','donald','harry','henry','johnn']
sample=random.sample(range(0,20),10)
quickSort(sample,0,9)
