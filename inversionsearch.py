import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.dpi'] = 250


def rollsum(a,b): #generate convolution of two die
    #die are stored as dicts to be efficient abt multiplicity
    newdict={}
    for ael in a.keys():
        for bel in b.keys():
            if ael+bel not in newdict:
                newdict[ael+bel]=a[ael]*b[bel] #if new value, create value
            else: 
                newdict[ael+bel]=newdict[ael+bel]+a[ael]*b[bel] #if old value, add to
    return newdict
            
def mediansign(a): #checks whether a die is a winner
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

def dicesearch(n,maxrolls,sofar,i,latest,toplist): #recursion to handle varying die size
    if i<n-1:
        lower=np.round(-sum(sofar)/(n-i)) 
        upper=min(sofar[-1],sofar[0]*(n-i-1)-sum(sofar))
        
        for x in np.arange(lower,upper+1): #bounds remove all redundant dice
            
            latest,toplist=dicesearch(n,maxrolls,sofar+[x],i+1,latest,toplist)

    if i==n-1: #at this level, dealing with a single specific die
        last=sofar[0]*(n-i-1)-sum(sofar)
        
        difflist=sofar+[last]
        diff={}
        #convert our die list to dict
        for el in difflist:
            cnt=difflist.count(el)
            diff[el]=cnt
            
        new=runfilter(diff,maxrolls)
        #keeps track of the best run so far, and all the dice that satisfy it
        if new!=False:
            if new>latest:
                return new,[sofar+[last]]
            elif new==latest:
                toplist.append(sofar+[last])
                return new,toplist

    return latest,toplist
    

    
scale=50
sides=4
maxrolls=50

best,champions=dicesearch(sides-1,maxrolls,[scale],0,0,[])

#print(len(champions))
#print(champions)
print(champions[int(np.round(len(champions)/2))])

print(f'sides={sides}, last inversion at {best}, number of latest inverters={len(champions)},(scale={scale},horizon={maxrolls})')


