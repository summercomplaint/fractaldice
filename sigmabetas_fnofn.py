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
    j=int(np.floor(n/5))+d
    return math.comb(n,2*j)*math.comb(2*j,j)*3**(n-2*j)

def beta(T,n,d):
    
    i=int(np.floor(n/5))+d
    Pik=anticheckthresh(T,n-2*i,-i)
    Nik=checkthresh(T,n-2*i,-i)
    return (Pik-Nik)/(3**(n-2*i))

probdiff=[]

T={5:1,3:1,-9:1}



sigma_nds=[]
sigma_n_ds=[]

beta_nds=[]
beta_n_ds=[]



sigmaratios=[]

betaratios=[]

sigmainduction=[]

restinduction=[]


ns=[50+5*i for i in range(20)]
#ns=range(50,200)

for d in range(1,int(ns[0]/5)):
    
    sigma_nds=[]
    sigma_n_ds=[]
    
    beta_nds=[]
    beta_n_ds=[]
    
    
    
    sigmaratios=[]
    
    betaratios=[]

    for n in ns:
        n=int(n)
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
        
        
    """
    print(f'd={d},minsigma={min(sigmaratios)}, maxbeta={max(betaratios)}')
    
    plt.scatter(ns,sigmaratios, s=2,color="green",label="sigma")
    
    
    plt.scatter(ns,betaratios, s=2,color="red",label="beta")
    plt.title(f'start={ns[0]},d={d}')
    plt.legend()
    ax = plt.gca()
    ax.set_ylim([0,2])
    
    plt.show()
    plt.clf()
    
    ######
    
    
    
    plt.scatter(ns,[sigmaratios[i]/betaratios[i] for i in range(len(sigmaratios))], s=2,color="green",label="combo")
    
    plt.plot([ns[0],ns[-1]],[1,1])
    
    plt.title(f'start={ns[0]},d={d}')
    plt.legend()
    ax = plt.gca()
    ax.set_ylim([0,2])
    
    plt.show()
    plt.clf()
    """
    ####
    
    plt.scatter(ns,[1/(sigmaratios[i]/betaratios[i]-1)for i in range(len(sigmaratios))], s=2,color="green",label="combo")
    
    
    plt.title(f'start={ns[0]},d={d}')
    plt.legend()
    
    
    plt.show()
    plt.clf()
    
    #plt.scatter(ns,[1/(1-rat) for rat in sigmaratios], s=2,color="green",label="sigma")
    
    
    #plt.scatter(ns,[1/(1-bet) for bet in betaratios], s=2,color="red",label="beta")

#####

