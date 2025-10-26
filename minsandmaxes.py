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


def fifther(n,d):
    if n%5==0:
        return int(n/5)+d
    if n%5==1:
        return int(np.floor(n/5))+d
    if n%5==2:
        return int(np.floor(n/5))+d
    if n%5==3:
        if d>0:
            return int(np.floor(n/5))+d
        else:
            return int(np.ceil(n/5))+d
    if n%5==4:
        if d>0:
            return int(np.floor(n/5))+d
        else:
            return int(np.ceil(n/5))+d
        

def sigma(n,d):
    j=fifther(n,d)
    return math.comb(n,2*j)*math.comb(2*j,j)*3**(n-2*j)

def beta(T,n,d):
    
    i=fifther(n,d)
    Pik=anticheckthresh(T,n-2*i,-i)
    Nik=checkthresh(T,n-2*i,-i)
    return (Pik-Nik)/(3**(n-2*i))

probdiff=[]

T={5:1,3:1,-9:1}


ns=[53+5*i for i in range(20)]

minsigmas=[]
maxbetas=[]

mindexes=[]
maxdexes=[]

for n in ns:

    ds=range(0,min(15,int(n/5)))
    
    
    sigma_nds=[]
    sigma_n_ds=[]
    
    beta_nds=[]
    beta_n_ds=[]
    
    nextsigma_nds=[]
    nextsigma_n_ds=[]
    
    nextbeta_nds=[]
    nextbeta_n_ds=[]
    
    sigmaratios=[]
    nextsigmaratios=[]
    
    betaratios=[]
    nextbetaratios=[]
    
    
    
    for d in ds:
        
        
        snd=sigma(n,d)
        sn_d=sigma(n,-d)
        
        sigma_nds.append(snd)
        sigma_n_ds.append(sn_d)

        
        
        bnd=beta(T,n,d)
        bn_d=beta(T,n,-d)
        
        beta_nds.append(bnd)
        beta_n_ds.append(bn_d)
        

        
        sigmaratios.append(snd/sn_d)
        
        betaratios.append(-bn_d/bnd)
        
   
    
    minsigmas.append(min(sigmaratios))
    maxbetas.append(max(betaratios))
    
    mindex=min(range(len(sigmaratios)), key=sigmaratios.__getitem__)
    maxdex=max(range(len(betaratios)), key=betaratios.__getitem__)
    
    mindexes.append(mindex)
    maxdexes.append(maxdex)
    
with open('minsmaxes', 'wb') as f:
    pickle.dump((minsigmas,maxbetas), f)
    
with open('dexes', 'wb') as f:
    pickle.dump((mindexes,maxdexes), f)

plt.scatter(ns,minsigmas,s=2,color="green",label="sigma")
plt.scatter(ns,maxbetas,s=2,color="red",label="beta")

#plt.plot(ns,[1-2.5/(np.sqrt(n)) for n in ns],label="5")





print(minsigmas[1]-minsigmas[0],minsigmas[5]-minsigmas[4])
#ax = plt.gca()
#ax.set_ylim([0,2])
plt.legend()
plt.title(' min sigma ratio vs beta ratio')

plt.show()
plt.clf()


########
"""
plt.scatter(ns,mindexes,color="green",s=2,label="min sigma index",alpha=0.5)
plt.scatter(ns,maxdexes,color="red",s=2,label="max beta index",alpha=0.5)

plt.show()
plt.clf()
"""
#####

#plt.scatter(ns,[minsigmas[n]-maxbetas[n] for n in range(len(ns))])

