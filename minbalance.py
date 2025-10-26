import numpy as np
import matplotlib.pyplot as plt
import pickle
import math

plt.rcParams['figure.dpi'] = 250

def measbalance(n,x,r):
    negtotal=0
    postotal=0
    for i in range(n+1):
        mult=math.comb(n,i)
        negtotal+=mult
        
        j=n-i
        if i>=j:
            postotal+=2*mult
        else:
            if j<n/(x+1):
                postotal+=mult
            else:
                negtotal+=mult
            
            if j<n/(2-x):
                postotal+=mult
            else:
                negtotal+=mult
    m=int((r-n)/3)
    return math.comb(r,n)*math.comb(3*m,m)*math.comb(2*m,m)*(postotal-negtotal)/(2**n)

xs=np.linspace(0,1/2,20,endpoint=False)
r=18

for n in range(3,r,3):
    bals=[measbalance(n,x,r) for x in xs]
    
    plt.scatter(xs,bals,label=f'extrarolls={n}',s=1)
        
plt.legend(fontsize=6)