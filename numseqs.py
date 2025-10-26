import numpy as np
import matplotlib.pyplot as plt

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
    outcomes=[]
    prev=rollsum(a,a)
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
    

coinscale=500
#yaxis=np.linspace(0.01,1,N)
#xaxis=np.linspace(-1,1,2*N)
maxval=1


axis=np.arange(-int(maxval*coinscale),int(maxval*coinscale),1,dtype=int)

halfaxis=np.arange(-int(maxval*coinscale),int(maxval*coinscale),1,dtype=int)



rolls=7



dictlist=[dict() for r in range(rolls)]
currentindex=0
seqs=[]

for x in axis:
    for y in halfaxis:
        if x>=y and y>=-coinscale-x-y and -coinscale-x-y>=-coinscale:
            
            #x+=0.001*(np.random.rand()-1/2)
            #y+=0.001*(np.random.rand()-1/2)
            difflist=[coinscale,x,y,-coinscale-x-y]
            diff={}
            for el in difflist:
                cnt=difflist.count(el)
                diff[el]=cnt

            
            
            dieoutcome=checkoutcomes(diff,rolls)
            reverse=[-el for el in dieoutcome]
            for length in range(rolls):
                trunc=dieoutcome[:length+1]
                rtrunc=reverse[:length+1]
                if str(trunc) not in dictlist[length]:
                    seqs.append(str(trunc))
                    
                    dictlist[length][str(trunc)]=currentindex
                    currentindex+=1
                if str(rtrunc) not in dictlist[length]:
                    seqs.append(str(rtrunc))
                    
                    dictlist[length][str(rtrunc)]=currentindex
                    currentindex+=1
                
            
numseqs=[len(dct) for dct in dictlist]
plt.scatter(range(rolls),numseqs)
print(coinscale)
print(numseqs)