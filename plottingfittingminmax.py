import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle
import scipy




with open('minsmaxes', 'rb') as f:
    sigmaratios,betaratios=pickle.load(f)
    
with open('dexes', 'rb') as f:
    mindexes,maxdexes=pickle.load(f)
    
ns=[50+5*i for i in range(20)]

plt.scatter(ns,sigmaratios,s=2,color="green",label="sigma")
plt.scatter(ns,betaratios,s=2,color="red",label="beta")

plt.plot(ns,[1-2.5/(np.sqrt(n)) for n in ns],label="5")

plt.show()
plt.clf()


sigmareverse=[1/(1-x)**2 for x in sigmaratios]
betareverse=[1/(1-x)**2 for x in betaratios]

plt.scatter(ns,sigmareverse,color="green",s=2)
plt.scatter(ns,betareverse,color="red",s=2)

print(sigmareverse[1]-sigmareverse[0],sigmareverse[5]-sigmareverse[4])

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(ns,sigmareverse)

print(slope,intercept, r_value)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(ns,betareverse)

print(slope,intercept,r_value)

plt.show()
plt.clf()

plt.scatter(ns,mindexes,alpha=0.5)
plt.plot(ns,[np.round(np.sqrt(n/4)) for n in ns])
plt.show()


#plt.scatter(np.log(ns),np.log(sigmaratios),color="green",s=2)
#plt.scatter(np.log(ns),np.log(betaratios),color="red",s=2)