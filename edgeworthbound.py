import numpy as np

import matplotlib.pyplot as plt
import itertools

plt.rcParams['figure.dpi'] = 350

def certfind(D,maxval):
    base=range(-maxval,maxval)
    vals=itertools.product(base,repeat=len(D))
    best=0
    size=1000000
    for val in vals:
        if sum(val)==0 and sum([D[i]*val[i] for i in range(len(D))])==1:
            
            newsize=sum([abs(v) for v in val])
            if newsize<size:
                size=newsize
                best=val
    return best,size
x=13

#D=[x,5,3,-9,-x+1]
D=[20, 10.0, 2.0, -13.0, -19.0]

cert,C=certfind(D,5)

print(cert,C)

b=1
m=1/6


mu2=1/6*sum([x**2 for x in D])
sig=np.sqrt(mu2)
mu3=1/6*sum([x**3 for x in D])
mu4=1/6*(sum([x**4 for x in D]))
v3=mu3/sig**3
v4=mu4/sig**4
beta=b/(2*sig)

p0=np.e-1
p1=3*(np.pi-3)/np.pi**3

q1=1/5+v4/24
q2=p0*q1/2+(b**2)*p1/mu2
q3=np.abs(beta)
q4=np.abs(v3)/6
q5=(q3**3)/6+3*(q3**2)*q4/2+15*q3*(q4**2)/2+35*(q4**3)/2

r=16*(b**2)*m/((np.pi*C*sig)**2)



def est(n):
    return -v3/(3*np.sqrt(2*np.pi*n))

def err(n):
    eta=2*np.sqrt(n/q1)
    return 2*q2/n+np.e**(-n*r/2)/(n*r)+2*q5/(np.sqrt(2*(np.pi))*n**(3/2))+\
        (np.e**(-eta))*((1+p0)/eta+4*p0*q1/n+((q3+q4)/eta+2*q4)/(np.pi*(q1*n)**(1/4)))

ns=range(50*1000,100*1000,1000)
ests=[np.abs(est(n)) for n in ns]
errs=[np.abs(err(n)) for n in ns]

plt.scatter(ns,ests,color="green",label="estimate",s=2)
plt.scatter(ns,errs,color="red",label="errors",s=2)