import numpy as np
import matplotlib.pyplot as plt
import pickle

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

def rolldist(a,r):
    if r==0:
        return {0:1}
    prev=a
    rolls=1
    for i in range(r-1):
        
        nextroll=rollsum(prev,a)
        prev=nextroll
        rolls+=1
    return prev
            
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

maxval=200
x=75
D={maxval:1,x:1,-maxval-x:1}
rolls=3
later=rolldist(D,rolls)
plt.title(f'rolls={rolls}')
plt.scatter(later.keys(),later.values())
plt.plot([0,0],[0,1])