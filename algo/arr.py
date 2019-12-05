a=[84,25,32,12,44]
print("Array A is:",a)
for i in range(len(a)):
    min_ind=i
    print(min_ind)
    for j in range(i+1,len(a)):
        if a[min_ind]>a[j]:
            min_ind=j
    print("elemnet swapping here")
    a[i],a[min_ind]=a[min_ind],a[i]
    print(a[i],a[min_ind])
    print("Iteration %d:"%(i+1))
    print(a)
    print("Smallest elemnet is:%d" %a[0])
    print("Greatest element is :%d"%a[len(a)-1])
