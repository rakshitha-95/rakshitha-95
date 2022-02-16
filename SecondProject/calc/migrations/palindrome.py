'''consider a positive innum containing atleast two  digits.identify and print a number outnum based on the logic given number
'''
from itertools import permutations,combinations
innum=int(input("enter the number"))
num=str(innum)
l=[]
if innum > 9:
    for i in num:
        l.append(i)
def palindrime(innum):
    res=[]
    for i in innum:
        j=i[::-1]
        if j==i:
            if i not in res:
                res.append(i)
    if len(res)>=1:
        print(max(res))
    else:
        print(-1)

res=permutations(l)
data=[]
for i in res:
    outnum="".join(i)
    data.append(i)
palindrime(data)


