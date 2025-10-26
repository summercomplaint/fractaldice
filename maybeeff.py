import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 250


def rollsum(a,b):
    newdict={}
    for ael in a.keys():
        for bel in b.keys():
            if ael+bel not in newdict:
                newdict[ael+bel]=a[ael]*b[bel]
            else: 
                newdict[ael+bel]=newdict[ael+bel]+a[ael]*b[bel]
    return newdict
            
            
def mediansign(a):
    win=0
    lose=0
    for el in a.keys():
        if el>0:
            win+=a[el]
        elif el<0:
            lose+=a[el]
    if win>lose:
        return 1
    elif win<lose:
        return -1
    else:
        return 0

def offsetoutcomes(a,r,start):
    outcomes=[mediansign(start)]
    prev=start
    for i in range(r-1):
        nextroll=rollsum(prev,a)
        outcomes.append(mediansign(nextroll))
        prev=nextroll
    return outcomes

rolls=100
scale=100

xs=range(1,scale)

outcomematrix=[]
for x in xs:
    xdict={2*scale:1,-x:1,-2*scale+x:1}
    doubled=rollsum(xdict,xdict)
    tripled=rollsum(xdict,doubled)
    outcomematrix.append(offsetoutcomes(tripled,rolls,doubled))
plt.imshow(outcomematrix)