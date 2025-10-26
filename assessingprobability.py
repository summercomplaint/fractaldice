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
    return math.comb(k,2*j)*math.comb(2*j,j)/math.comb(2*k,k)


k=103
probdiff=[]

T={5:1,3:1,-9:1}

iss=range(0,int(k/2))
shortis=range(0,int(k/5))
totaldiff=[]
factors=[]


for i in iss:
    if False:
        
        probdiff.append(0)
        totaldiff.append(0)
        factors.append(0)
    else:
        Pik=anticheckthresh(T,k-2*i,-i)
        Nik=checkthresh(T,k-2*i,-i)
        probdiff.append((Pik-Nik)/(Pik+Nik))
        totaldiff.append(scalefactor(k,i)*(Pik-Nik))
        factors.append(scalefactor(k,i)*3**(k-2*i))


plt.scatter(iss,totaldiff,color="blue",s=2)
#flippeddiff=[-totaldiff[int(2*k/5-i)] for i in iss[:int(k/5)]]

plt.scatter([np.floor(k/5)],[0],alpha=0.5)
plt.scatter([np.floor(k/5)-1],[0])

plt.plot(iss[:int(k/5)],flippeddiff,color="red")
plt.title("paired total face balance")
plt.show()
plt.clf()
#####################################

plt.plot(iss[:int(k/5)],factors[:int(k/5)],color="blue")
flippedfactors=[factors[int(2*k/5-i)] for i in iss[:int(k/5)]]

plt.plot(iss[:int(k/5)],flippedfactors,color="red")
plt.title("paired face scaling")
plt.show()
plt.clf()
############################

plt.scatter(shortis,probdiff[:len(shortis)],s=2,color="blue")

#print([i for i in shortis])
#print([int(2*k/5)-1-i for i in shortis])

flipped=[-probdiff[int(2*k/5)-i] for i in shortis]
plt.scatter(shortis,flipped,alpha=1,s=2,color="red")


#plt.scatter([k/5],[0],color='red',s=2)
rho=-577/3
sigma=np.sqrt(115/3)
probhighs=[]
problows=[]
probs=[]
for i in iss:
    prob=scipy.stats.norm.cdf((k/3-5*i/3)/(sigma*np.sqrt((k-2*i))))
    err=0.5*rho/(sigma**3*np.sqrt(k-2*i))
    probhighs.append(1-2*(prob+err))
    problows.append(1-2*(prob-err))
    probs.append(1-2*prob)

plt.plot(shortis,probhighs[:len(shortis)],color="blue",alpha=0.5)
plt.plot(shortis,problows[:len(shortis)],color="blue",alpha=0.5)


plt.plot(shortis,probs[:len(shortis)],color="blue")

flippedapprox=[-probs[int(2*k/5)-i] for i in shortis]

plt.plot(shortis,flippedapprox,color="red",alpha=0.5)
plt.title("probability balance compared to normal")

plt.show()
plt.clf()


###############################

"""
print(max(shortis),2*k/5-max(shortis))
print(probdiff[-1],flipped[-1])

trueratio=[flipped[i]/probdiff[i] for i in shortis]

approxratio=[flippedapprox[i]/probs[i] for i in shortis]
plt.plot(shortis,trueratio,color="green")
plt.plot(shortis,approxratio,color="red")

plt.title("probability ratio and approx")
plt.show()
plt.clf()
#########
approxtotal=[factors[i]*probs[i] for i in shortis]
approxtotalflipped=[flippedfactors[i]*flipped[i] for i in shortis]
plt.scatter(shortis, approxtotal,color="blue",s=2)
plt.scatter(shortis,approxtotalflipped,color="red",s=2)

plt.title("approximated face balances")
plt.show()

plt.clf()

#######

plt.plot(iss,[probs[i]-probdiff[i]  for i in iss])

plt.title("difference between normal and true")
plt.show()

plt.clf()

#####

approxtotal=[factors[i]*probs[i] for i in shortis]
approxtotalflipped=[flippedfactors[i]*flipped[i] for i in shortis]

approxdiff=[abs(approxtotal[i]-approxtotalflipped[i]) for i in shortis]

convbound=[abs((rho*0.5/sigma**3)*(factors[i]/np.sqrt(k-2*i)+flippedfactors[i]/np.sqrt(k/5+2*i))) for i in shortis]

plt.scatter(shortis,approxdiff,s=2,color="green")
plt.scatter(shortis,convbound,s=2, color="red")

plt.title("actual balance difference vs approximation error")
plt.show()

plt.clf()
"""