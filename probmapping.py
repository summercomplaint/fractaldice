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

def unequalbal(T,n,i,j,x):
    
    Pik=anticheckthresh(T,n-i-j,-(i*x+j*(-x+1)))
    Nik=checkthresh(T,n-i-j,-(i*x+j*(-x+1)))
    
    #print(i+j,3**(n-i-j)-(Pik+Nik))
    return (Pik-Nik)


R={5:1,3:1,-9:1}
bals=[]
x=5

dels=range(1,20)


agcincs=[]
agcdecs=[]
alcincs=[]
alcdecs=[]

incs=[]
decs=[]
#combos=[]


for dval in dels:
    agcinc=(anticheckthresh(R,dval,dval*x))/(3**dval)
    agcdec=checkthresh(R,dval,dval*x)/(3**dval)
    alcinc=(anticheckthresh(R,dval,-dval*(x-1)))/(3**dval)
    alcdec=checkthresh(R,dval,-dval*(x-1))/3**dval
    
    agcincs.append(agcinc)
    alcincs.append(alcinc)
    agcdecs.append(agcdec)
    alcdecs.append(alcdec)
    
    incs.append((agcinc+alcinc)/2)
    decs.append((agcdec+alcdec)/2)

    
plt.scatter(dels,incs,color="green",s=2,label="incs")
plt.scatter(dels, decs, color="red",s=2,label="decs")
plt.title("P(increasing) vs P(decreasing)")
plt.legend()
plt.show()
plt.clf()

#plt.scatter(dels,combos)



