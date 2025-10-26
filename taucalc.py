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

def totaldiff(a):
    win=0
    lose=0
    for el in a.keys():
        if el>0:
            win+=a[el]
        elif el<0:
            lose+=a[el]
    return win-lose

def checkoutcomes(a,r):
    outcomes=[mediansign(a)]
    prev=rollsum(a,a)
    outcomes.append(mediansign(prev))
    for i in range(r-1):
        nextroll=rollsum(prev,a)
        outcomes.append(mediansign(nextroll))
        prev=nextroll
    return outcomes

def tau(dist,maxval):
    total=0
    totx2=0
    totx3=0
    
    for el in dist.keys():
        val=dist[el]
        total+=val
        totx2+=val*(el/maxval)**2 
        totx3+=val*(el/maxval)**3
    totx3=totx3/total
    totx2=totx2/total
    return totx3,totx2,-totx3/totx2**(3/2)

maxval=1000
xs=range(1,int(maxval/2))
#xs=range(25,50)
taus=[]
x3s=[]
x2s=[]
diffs=[]
checkroll=104
for x in xs:
    D={maxval:1,-x:1,-maxval+x:1}
    rolled=rolldist(D,checkroll)
    x3,x2,t=tau(rolled,maxval)
    x3s.append(x3)
    x2s.append(x2)
    taus.append(t)
    diffs.append(totaldiff(rolled)/3**checkroll)

plt.scatter(xs,diffs,s=2)
plt.title(f'probability balance, rolls={checkroll}')
plt.plot([xs[0],xs[-1]],[0,0])

