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

def checkoutcomes(a,r):
    outcomes=[mediansign(a)]
    prev=rollsum(a,a)
    outcomes.append(mediansign(prev))
    for i in range(r-1):
        nextroll=rollsum(prev,a)
        outcomes.append(mediansign(nextroll))
        prev=nextroll
    return outcomes

numx=50
rolls=100
xs=np.linspace(-0.49,-0.01, numx)

outcomematrix=[]
for x in xs:
    xdict={1:1,x:1,-1-x:1}
    outcomematrix.append(checkoutcomes(xdict,rolls))
plt.imshow(outcomematrix)