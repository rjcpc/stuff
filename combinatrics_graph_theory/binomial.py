#

def binomialcoefficient(n,k):
    if n==k or k==0:
        return 1
    #recursive call
    return binomialcoefficient(n-1,k-1)+binomialcoefficient(n-1,k)



n=0
if n==0:
    print ("not allowed")
    exit()
k=2

print ("the binomial coefficient of n={} and k={} is : {}".format(n,k,binomialcoefficient(n,k)))
