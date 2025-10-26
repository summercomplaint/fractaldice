import numpy as np
import matplotlib.pyplot as plt
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
            
            
def mediansign(a):
    win=0
    lose=0
    for el in a.keys():
        if el>0:
            win+=a[el]
        elif el<0:
            lose+=a[el]
    if win>lose:
        return 1
    elif win<lose:
        return -1
    else:
        return 0

def checkoutcomes(a,r):
    outcomes=[mediansign(a)]
    prev=rollsum(a,a)
    outcomes.append(mediansign(prev))
    for i in range(r-1):
        nextroll=rollsum(prev,a)
        outcomes.append(mediansign(nextroll))
        prev=nextroll
    return outcomes

rolls=50
scale=1680

start=0.25
stop=0.27
xs=range(int(2*0.33*scale),int(2*0.35*scale))

outcomematrix=[]
for x in xs:
    xdict={2*scale:1,-x:1,-2*scale+x:1}
    outcomematrix.append(checkoutcomes(xdict,rolls))
    if x%10==0:
        print(x/scale)
    
outs=[[],[],[]] 

for row in outcomematrix:
    mods=[[],[],[]]
    
    for i in range(len(row)):
        mods[(i+1)%3].append(row[i])
    
    for j in range(3):
        outs[j].append(mods[j])
        
for j in range(3):
    plt.title(f'mod={j},scale={scale},rolls={rolls}')
    plt.imshow(outs[j])
    plt.show()  
    plt.clf()


binars=[]
for row in outcomematrix:
    tot=0
    for i,el in enumerate(row):
        tot+=(1-(1-el)/2)*2**(-i/50)
    binars.append(tot)
plt.scatter(xs,binars,s=2)    

#with open('3sided', 'wb') as f:
    #pickle.dump(outcomematrix, f)
