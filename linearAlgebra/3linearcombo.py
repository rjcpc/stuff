def scalermul(x,p):return[p*x[i] for i in range(len(x))]

def lin_comb(vlist,clist):
    s=[(scalermul(vlist[i],clist[i])) for i in range(len(vlist))]
    l=[]
    for j in range(len(s[0])):
        su=0
        for i in range(len(s)):
            su=su+s[i][j]
        l.append(su)
    return l
print(lin_comb([[1,2,3],[0,1,4],[2,-1,1]],[2,1,3]))
print(lin_comb([[1,1],[2,3]],[-6,4]))
