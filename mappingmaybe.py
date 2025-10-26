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


incs=[]
decs=[]
rats=[]


for dval in dels:
    inc=anticheckthresh(R,dval,dval*x)+anticheckthresh(R,dval,-dval*(x-1))
    dec=checkthresh(R,dval,dval*x)+checkthresh(R,dval,-dval*(x-1))
    rats.append(dec/inc)
    incs.append(inc/(2*3**dval))
    decs.append(dec/(2*3**dval))
    
plt.scatter(dels,incs,color="green",s=2,label="incs")
plt.scatter(dels, decs, color="red",s=2,label="decs")
plt.legend()
plt.show()
plt.clf()

plt.scatter(dels, rats, color="red",s=2,label="rats")
plt.legend()

