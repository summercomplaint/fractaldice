import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle
plt.rcParams['figure.dpi'] = 250
plt.rcParams.update({'font.size': 10})

rolls=350

with open('dicecurve', 'rb') as f:
    xrange,runlengths=pickle.load(f)

plt.title("Inversion Delay for Die=$\{x,5,3,-9,-x+1\}$")
plt.ylabel("Number of Wins before First Loss")

#logx=[np.log(x) for x in xrange]
#loglengths=[np.log(x) for x in runlengths]
#x2=[2*x-5 for x in logx]
#plt.gca().set_aspect('equal')

#matplotlib.rc('font', size=10) 
plt.xticks(fontsize=10)

plt.scatter(xrange,runlengths,s=10,color="red")
a,b,c=np.polyfit(xrange[:25],runlengths[:25], 2)
print(a,b,c)

mval=350
print(a*mval**2+b*mval+c)

plt.plot(range(mval),[a*x**2 for x in range(mval)],color="black",label=f'${np.round(a,3)}x^2{np.round(b,3)}x+{np.round(c,3)}$')
#plt.plot(logx,x2)
plt.legend()
plt.xlabel("x value")


