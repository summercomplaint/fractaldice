import numpy as np
import matplotlib.pyplot as plt
import pickle

plt.rcParams['figure.dpi'] = 350

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
    outcomes=[]
    prev=a
    outcomes.append(mediansign(prev))
    for i in range(r-1):
        nextroll=rollsum(prev,a)
        outcomes.append(mediansign(nextroll))
        prev=nextroll
    return outcomes

def checkfinaloutcome(a,r):
    outcomes=[]
    prev=a
    #outcomes.append(mediansign(prev))
    for i in range(r-1):
        nextroll=rollsum(prev,a)
        #outcomes.append(mediansign(nextroll))
        prev=nextroll
    
    return mediansign(prev)

def colorassign(val):
    if val=="0":
        return "pink"
    if val=="1":
        return "blue"
    if val=="-1":
        return "red"
    else:
        return "pink"
    

coinscale=200
#yaxis=np.linspace(0.01,1,N)
#xaxis=np.linspace(-1,1,2*N)
maxval=1


axis=np.arange(-int(maxval*coinscale/3),int(maxval*coinscale),1,dtype=int)

halfaxis=np.arange(-int(maxval*coinscale),0,1,dtype=int)



rolls=10

trinars=[]
diff={1:1,2:1,3:1}
dieoutcome=checkoutcomes(diff,rolls)
for y in halfaxis:
    xrow=[]
    for x in axis:
        if True: #x>=y and y>=-coinscale-x-y and -coinscale-x-y>=-coinscale:
            
            #x+=0.001*(np.random.rand()-1/2)
            #y+=0.001*(np.random.rand()-1/2)
            difflist=[coinscale,x,y,-coinscale-x-y]
            diff={}
            for el in difflist:
                cnt=difflist.count(el)
                diff[el]=cnt

            
            
            dieoutcome=checkoutcomes(diff,rolls)
            tot=0
            for i,el in enumerate(dieoutcome):
                tot+=(1+el)*3**(-i/50)
            xrow.append(tot)
        else:
            xrow.append(0)

    trinars.append(xrow)
    
plt.imshow(trinars)
plt.axis('off')   
"""  
with open('trinarimage', 'wb') as f:
    pickle.dump(trinars, f)
"""