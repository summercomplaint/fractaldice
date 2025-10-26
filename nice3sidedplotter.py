import numpy as np
import matplotlib.pyplot as plt
import pickle
import matplotlib.patches as mpatches

plt.rcParams['figure.dpi'] = 500
plt.rcParams.update({'font.size': 8})

with open('3sided600', 'rb') as f:
    outcomematrix=pickle.load(f)

scale=len(outcomematrix)
rolls=len(outcomematrix[0])
outs=[[],[],[]] 

for row in outcomematrix:
    mods=[[],[],[]]
    
    for i in range(len(row)):
        mods[(i+1)%3].append(row[i])
    
    for j in range(3):
        outs[j].append(mods[j])
        
#fig,axs=plt.subplots(1,3)

newmat=[]

for row in outcomematrix:
    newrow=[]
    for i, el in enumerate(row):
        if el==-1:
            newrow.append(0)
        elif i%3==0:
            newrow.append(1)
        else:
            newrow.append(2)
    newmat.append(newrow)
    
    
plt.imshow(newmat,cmap="Greys")

red_patch = mpatches.Patch(color='black', label='P(X>0)>P(X<0), Number of rolls=2 mod 3')
green_patch = mpatches.Patch(color='grey', label='P(X>0)>P(X<0), Number of rolls=1 mod 3')
blue_patch = mpatches.Patch(facecolor='white',edgecolor="black",linewidth=0.5, label='P(X>0)<P(X<0)')


redline=mpatches.PathPatch([],facecolor="white",edgecolor="red",linewidth=0.5,label="$x=1/(2+3n)$")
greenline=mpatches.PathPatch([],facecolor="white", edgecolor="blue",linewidth=0.5,label="$x=2/(1+6n)$")

plt.legend(handles=[red_patch, green_patch, blue_patch,redline,greenline], loc=(0.52,0.10), fontsize=6)


manylines=6

for n in range(1,manylines):
    const=scale*(2/(2+3*n))
    redline=plt.plot([0,rolls-1],[const,const],color="red",linewidth=0.5,label="$1/(2+3n)$", alpha=0.5)
    
    
manylines=4

for n in range(1,manylines):
    const=scale*(4/(1+6*n))
    greenline= plt.plot([0,rolls-1],[const,const],color="blue",linewidth=0.5,label="$2/(1+6n)$", alpha=0.5)



plt.title("Outcomes for $\Delta=\{1,x,-1-x\}$")

ax=plt.gca()

ax.set_ylabel("x value")

boxscale=np.arange(0,250,50)
realscale=np.arange(0,-5/8,-1/8)

ax.set_yticks(boxscale,realscale) 



"""
for j in range(3):
    #plt.title(f'mod={j},scale={scale},rolls={rolls}')
    ax=axs[j-1]
    ax.imshow(outs[j],cmap="Greys")
    if j==0:
        plt.legend(handles=[red_patch, blue_patch],fontsize=8)
        j=3
    ax.set_title(f"Rolls {j} mod 3",fontsize=7)
    ax.set_xticks(np.arange(0,200,50),np.arange(j,200,50))
    ax.set_xlabel("Number of rolls")
    
        
    if j!=1:
        ax.set_yticks([])
    else:
        ax.set_ylabel("x value")
        boxscale=np.arange(0,250,50)
        realscale=np.arange(0,-5/8,-1/8)
        print(boxscale,realscale)
        ax.set_yticks(boxscale,realscale)        
fig.suptitle("Outcomes for $\Delta=[1,x,-1-x]$, collated mod 3")
fig.tight_layout()
fig.subplots_adjust(top=1.2)
"""