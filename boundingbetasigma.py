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

def sigma(n,d):
    j=int(n/5)+d
    return math.comb(n,2*j)*math.comb(2*j,j)*3**(n-2*j)

def beta(T,n,d):
    
    i=int(n/5)+d
    Pik=anticheckthresh(T,n-2*i,-i)
    Nik=checkthresh(T,n-2*i,-i)
    return (Pik-Nik)/(3**(n-2*i))

n=200
probdiff=[]

T={5:1,3:1,-9:1}


ds=range(0,int(n/5))

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
    

plt.scatter(ds,sigmaratios,s=2,color="green",label="sigma")
plt.scatter(ds,betaratios,s=2,color="red",label="beta")


plt.plot([np.sqrt(n/4),np.sqrt(n/4)],[0,2])


ax = plt.gca()
ax.set_ylim([0,2])
plt.legend()
plt.title(f'n={n}, sigma ratio vs beta ratio')

print(f'n={n},minsigma={min(sigmaratios)}, maxbeta={max(betaratios)}')


plt.show()

plt.clf()

####
plt.scatter(ds,[1/(sigmaratios[d]/betaratios[d]-1) for d in ds])

ax = plt.gca()
#ax.set_ylim([0,2])
plt.plot([np.sqrt(n/4),np.sqrt(n/4)],[0,2])

