import numpy as np
import matplotlib.pyplot as plt
import math
import scipy

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
"""
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
"""

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

n=104
probdiff=[]

T={5:1,3:1,-9:1}


ds=range(1,int(n/5))

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
    
    #nextsnd=sigma(n+5,d)
    #nextsn_d=sigma(n+5,-d)
    
    #nextsigma_nds.append(nextsnd)
    #nextsigma_n_ds.append(nextsn_d)
    
    
    bnd=beta(T,n,d)
    bn_d=beta(T,n,-d)
    
    beta_nds.append(bnd)
    beta_n_ds.append(bn_d)
    
    
    #nextbnd=beta(T,n+5,d)
    #nextbn_d=beta(T,n+5,-d)
    
    #nextbeta_nds.append(nextbnd)
    #nextbeta_n_ds.append(nextbn_d)
    
    sigmaratios.append(snd/sn_d)
    #nextsigmaratios.append(nextsnd/nextsn_d)
    
    betaratios.append(-bn_d/bnd)
    #nextbetaratios.append(-nextbn_d/nextbnd)
"""    
plt.scatter(ds,sigma_nds,s=2,color="green",label="positive d")
plt.scatter(ds,sigma_n_ds,s=2,color="red",label="negative d")
plt.title("sigmas")
plt.show()
plt.clf()
####
plt.scatter(ds,beta_nds,s=2,color="green",label="positive d")
plt.scatter(ds,beta_n_ds,s=2,color="red",label="negative d")
plt.title("betas")
plt.plot([ds[0],ds[-1]],[0,0])
plt.show()
plt.clf()
#####
"""
plt.scatter(ds,sigmaratios, s=2,color="green",label="sigmas")
print(sigmaratios)
#plt.scatter(ds,nextsigmaratios,s=2,color="red",label="next")
plt.title("sigma ratios")
ax=plt.gca()
ax.set_ylim(0,2)

plt.scatter(ds[1:],betaratios[1:], s=2,color="red",label="betas")
#plt.scatter(ds[1:],nextbetaratios[1:],s=2,color="red",label="next")
plt.legend()
plt.title("beta ratios")


bar=1-2.5/np.sqrt(n)
plt.plot([ds[0],ds[-1]],[bar,bar])
plt.show()
plt.clf()

####

indies=range(len(ds))

posprod=[sigma_nds[i]*beta_nds[i] for i in indies]
negprod=[-sigma_n_ds[i]*beta_n_ds[i] for i in indies]

plt.scatter(ds,posprod,s=2,color="green")
plt.scatter(ds,negprod,s=2,color="red")
plt.show()
