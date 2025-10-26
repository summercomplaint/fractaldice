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

def runfilter(dist,maxrolls):
    #looks for diceruns. returns the number of rolls at first non-win
    nextroll=dist
    if mediansign(dist)==1: #checks whether wins on first try
        for i in range(maxrolls-1):
            nextroll=rollsum(nextroll,dist) #rolls the sum
            if mediansign(nextroll)!=1:
                return i+2
        return False #if wins for all rolls checked, assume wins forever
    elif mediansign(dist)==-1: #if loses on first try, flip the sign
        for i in range(maxrolls-1):
            nextroll=rollsum(nextroll,dist)
            if mediansign(nextroll)!=-1:
                return i+2
        return False
    else: #if ties on first try, ignore
        return False

rolls=1100

xrange=np.arange(10,350,step=10)
runlengths=[]

for x in xrange:
    

    print(x)
    diff={x:1,5.0:1,3.0:1,-9.0:1,-x+1:1}
    
    stoppingpt=runfilter(diff,rolls)
    
    
        
    runlengths.append(stoppingpt)

plt.title(f"Die=[x,5,3,-9,-x+1]")
plt.ylabel("Number of Wins before First Loss")
plt.plot(xrange,runlengths,color="black")


with open('dicecurve', 'wb') as f:
    pickle.dump((xrange,runlengths), f)