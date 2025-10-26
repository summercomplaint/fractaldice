import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

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


def checkthresh(a,r,thresh):
    below=0
    prev=rolldist(a,r)
    for el in prev.keys():
        if el<thresh:
            below+=prev[el]
    return below

def anticheckthresh(a,r,thresh):
    below=0
    prev=rolldist(a,r)
    for el in prev.keys():
        if el>thresh:
            below+=prev[el]
    return below

def scalefactor(k,j):
    return math.comb(k,2*j)*math.comb(2*j,j)

def uneqscalefactor(k,i,j):
    return math.comb(k,i+j)*math.comb(i+j,i)


def sigma(n,d):
    j=int(n/5)+d
    return math.comb(n,2*j)*math.comb(2*j,j)*3**(n-2*j)

def beta(T,n,d):
    
    i=int(n/5)+d
    Pik=anticheckthresh(T,n-2*i,-i)
    Nik=checkthresh(T,n-2*i,-i)
    return (Pik-Nik)/(3**(n-2*i))

def equalbal(T,n,i):
    
    Pik=anticheckthresh(T,n-2*i,-i)
    Nik=checkthresh(T,n-2*i,-i)
    return (Pik-Nik)


def specialthresher(T,n,r,valset):
    fulldist=rolldist(T,n-r)
    bals=[]
    for val in valset:
        bals.append(0)
    
    for el in fulldist.keys():
        for i in range(len(valset)):
            if el>valset[i]:
                bals[i]+=fulldist[el]
            elif el<valset[i]:
                bals[i]+=-fulldist[el]
    return bals

def unequalbal(T,n,i,j,x):
    
    Pik=anticheckthresh(T,n-i-j,-(i*x+j*(-x+1)))
    Nik=checkthresh(T,n-i-j,-(i*x+j*(-x+1)))
    
    #print(i+j,3**(n-i-j)-(Pik+Nik))
    return (Pik-Nik)

def equalprobbalance(R,n):
    norm=0
    totalbal=0
    for i in range(int(np.floor(n/2))):
        scale=scalefactor(n,i)
        norm+=scale*3**(n-2*i)
        totalbal+=scale*equalbal(R,n,i)
    return totalbal/norm

def unequalprobbalance(R,n,x):
    norm=0
    totalbal=0
    for r in range(n+1):
        threshes=[]
        iss=range(r+1)
        for i in iss:
            j=r-i
            threshes.append(-(i*x+j*(-x+1)))
        bals=specialthresher(R,n,r,threshes)
        for i in iss:
            j=r-i
            if i!=j:
                scale=uneqscalefactor(n, i, j)
            else:
                scale=0
            norm+=scale*3**(n-r)
            totalbal+=scale*bals[i]
               
    return totalbal/norm

R={5:1,3:1,-9:1}

equalprobbalance(R, 200)
unequalprobbalance(R, 200,5)
"""
for x in [21]:#range(1,24):
    R={5:1,3:1,-9:1}
    
    equalbals=[]
    unequalbals=[]
    
    
    
    ns=[20+1*i for i in range(20)]
    
    for n in ns:
    
       
        
        equalbals.append(equalprobbalance(R, n))
        
        unequalbals.append(unequalprobbalance(R, n,x))
    
    fig,(ax1,ax2)=plt.subplots(1,2)
    ax1.scatter(ns, equalbals,s=2,color="green",label="equal")
    ax1.scatter(ns,unequalbals,s=2,color="red",label="unequal")
    ax1.plot([ns[0],ns[-1]],[0,0])
    
    ax1.legend()
    ax1.set_title(f'x={x}')
    
   
    
    ##############
    ratios=[equalbals[i]/abs(unequalbals[i]) for i in range(len(ns))]
    for k in range(5):
        print([ratios[k+5*i] for i in range(int(np.floor(len(ratios)/5)))])
    ax2.scatter(ns,ratios,s=2,color="purple",label="ratio")
    ax2.legend()
    ax2.set_title(f'x={x}')
    plt.show()
    plt.clf()
"""

