import numpy as np
import matplotlib.pyplot as plt
import pickle
import matplotlib.patches as mpatches

plt.rcParams['figure.dpi'] = 500
plt.rcParams.update({'font.size': 8})

with open('3sided600', 'rb') as f:
    outcomematrix=pickle.load(f)


halfscale=len(outcomematrix)
scale=2*halfscale
rolls=len(outcomematrix[0])
outs=[[],[],[]] 

for row in outcomematrix:
    mods=[[],[],[]]
    
    for i in range(len(row)):
        mods[(i+1)%3].append(row[i])
    
    for j in range(3):
        outs[j].append(mods[j])
        
fig,axs=plt.subplots(1,3,layout="constrained")

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
    
red_patch = mpatches.Patch(color='black', label='P(X>0)>P(X<0)')


blue_patch = mpatches.Patch(facecolor='white',edgecolor="black",linewidth=0.5, label='P(X>0)<P(X<0)')
redline=mpatches.PathPatch([],facecolor="white",edgecolor="red",linewidth=0.5,label="$1/(2+3n)$")

greenline=mpatches.PathPatch([],facecolor="white", edgecolor="springgreen",linewidth=0.5,label="$2/(1+6n)$")



for j in range(3):
    #plt.title(f'mod={j},scale={scale},rolls={rolls}')
    ax=axs[j-1]
    ax.imshow(outs[j],cmap="Greys")
    
    if j==2:
        manylines=10
        
        for n in range(1,manylines):
            const=scale*(1/(2+3*n))
            redline=ax.plot([0,(rolls-3)/3],[const,const],color="red",linewidth=0.5,label="$1/(2+3n)$")
            print(scale/const)
        
    if j==1:
        manylines=5

        for n in range(1,manylines):
            const=scale*(2/(1+6*n))
            greenline= ax.plot([0,(rolls-3)/3],[const,const],color="springgreen",linewidth=0.5,label="$2/(1+6n)$")
            print(scale/const)
    
    
    
    if j==0:
        
        plt.legend(handles=[red_patch, blue_patch,redline,greenline],fontsize=8)
        j=3
    ax.set_title(f"Rolls {j} mod 3",fontsize=7)
    many=5
    print(rolls/3)
    ax.set_xticks(np.linspace(0,(rolls-1)/3,many),[int(x) for x in np.linspace(j,(rolls-1)/3+j,many)])
    ax.set_xlabel("Number of rolls")
    
        
    if j!=1:
        ax.set_yticks([])
    else:
        ax.set_ylabel("x value")
        many=11
        boxscale=np.linspace(0,halfscale,many)
        realscale=np.round(np.linspace(0,-0.5,many),2)
        
        
        
        
        print(boxscale,realscale)
        ax.set_yticks(boxscale,realscale,fontsize=5)        
fig.suptitle("Outcomes for $\Delta=[1,x,-1-x]$, collated mod 3", y=0.9)
#fig.tight_layout()
