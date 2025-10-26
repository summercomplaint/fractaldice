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

def sigma(n,d):
    j=int(n/5)+d
    return math.comb(n,2*j)*math.comb(2*j,j)*3**(n-2*j)

def beta(T,n,d):
    
    i=int(n/5)+d
    Pik=anticheckthresh(T,n-2*i,-i)
    Nik=checkthresh(T,n-2*i,-i)
    return (Pik-Nik)/(3**(n-2*i))

probdiff=[]

T={5:1,3:1,-9:1}


ns=[50+5*i for i in range(20)]

minsigmas=[]
maxbetas=[]

mindexes=[]
maxdexes=[]

straightsigmas=[]

straightbetas=[]

straightcombos=[]

altsigmas=[]

for n in ns:

    

    
    
    d=int(np.round(np.sqrt(n/4)))
    
        
        
    snd=sigma(n,d)
    sn_d=sigma(n,-d)
    
    sigmaratio=snd/sn_d
    
    bnd=beta(T,n,d)
    bn_d=beta(T,n,-d)
    
    betaratio=-bn_d/bnd
    
    straightcombos.append(1/(sigmaratio/betaratio-1)**2)
    
    straightsigmas.append(1/(1-sigmaratio)**2)
    straightbetas.append(1/(1-betaratio)**2)
    

    

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(ns,straightsigmas)

print(r_value)

print(slope)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(ns,straightbetas)
print(r_value)

print(slope)

#plt.scatter(ns,straightsigmas,color="green",s=2,label="sigma")
plt.scatter(ns, straightbetas,color="red",s=2, label="beta")

#plt.scatter(ns,straightcombos,color="purple",s=2,label="combo")




slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(ns[1:],straightcombos[1:])

print(ns,straightcombos)
print(r_value)

print(slope)

plt.legend()








































































