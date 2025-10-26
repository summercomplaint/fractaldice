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
    for i in range(n+1):
        for j in range(n+1):
            if i+j<=n and i!=j:
               scale=uneqscalefactor(n, i, j)
               norm+=scale*3**(n-i-j)
               totalbal+=scale*unequalbal(R,n,i,j,x)
               
    return totalbal/norm

x=4
R={5:1,3:1,-9:1}

equalbals=[]
unequalbals=[]

ns=[20+5*i for i in range(20)]

for n in ns:
    print(n)
   
    
    equalbals.append(equalprobbalance(R, n))
    
    unequalbals.append(unequalprobbalance(R, n,x))


plt.scatter(ns, equalbals,s=2,color="green",label="equal")
plt.scatter(ns,unequalbals,s=2,color="red",label="unequal")
plt.plot([ns[0],ns[-1]],[0,0])

plt.legend()
plt.title(f'x={x}')
    


