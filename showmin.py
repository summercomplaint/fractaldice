import numpy as np
import matplotlib.pyplot as plt
import pickle
import matplotlib.patches as mpatches

plt.rcParams['figure.dpi'] = 250

def vertexcount(state):
    height=len(state)
    width=len(state[0])
    
    vertexcounts=[0,0,0,0]#E,C,H,F
    for i,row in enumerate(state):
        for j,hexval in enumerate(row):
            if i%2==0:
                v1sum=hexval+state[i][(j+1)%width]+state[(i+1)%height][(j+1)%width]
                
                v2sum=hexval+state[(i+1)%height][j]+state[(i+1)%height][(j+1)%width]
                
            if i%2==1:
                v1sum=hexval+state[i][(j+1)%width]+state[(i+1)%height][j]
                v2sum=hexval+state[(i+1)%height][j-1]+state[(i+1)%height][j]
        
            vertexcounts[v1sum]+=1 
            vertexcounts[v2sum]+=1 
        
    return vertexcounts

def splitlist(arr):
    newlist=[el+[0] for el in arr]+[el+[1] for el in arr]
    return(newlist)

def genbinary(n):
    currentlist=[[]]
    for i in range(n):
        currentlist=splitlist(currentlist)
    return(currentlist)

boundaries=genbinary(9)
tiles=genbinary(3)


def statefrombinary(boundary,tile):
    state=[[0]*4 for i in range(4)]
    boundarylist=[(0,0),(0,1),(0,2),(1,0),(1,3),(2,0),(2,2),(3,1),(3,2)]
    tilelist=[(1,1),(1,2),(2,1)]
    
    
    for k, el in enumerate(boundary):
        i,j=boundarylist[k]
        state[i][j]=el
        
    
    for k, el in enumerate(tile):
        i,j=tilelist[k]
        state[i][j]=el
    
    return(state)



def probsfromparams(beta,params):

    probsdict=dict()
    
    
    for boundary in boundaries:
        weights=[]
        for tile in tiles:
            state=statefrombinary(boundary,tile)
            vcount=vertexcount(state)
            energy=sum([params[i]*vcount[i] for i in range(4)])
            weights.append(np.exp(-beta*energy))
            
        norm=sum(weights)
        
        probs=[np.round(weight/norm,2) for weight in weights]
        pstr=str(probs)
        if pstr not in probsdict:
            probsdict[pstr]=boundary
        #else:
            #probsdict[pstr]+=[boundary]
        
    return probsdict

    #cleanset=[el.replace("]","").replace("[","").replace(" ","").split(",") for el in probsset]
    #cleanset=[[float(el) for el in arr] for arr in cleanset]
    #return cleanset
 
statedict=probsfromparams(10,[0,0,1,1])
minsdict=dict()
    
for probs in statedict:
    boundary=statedict[probs]
    fig,ax=plt.subplots()
    
    
    cleanset=probs.replace("]","").replace("[","").replace(" ","").split(",")
    cleanset=[float(el) for el in cleanset]
    
    
    
    state=statefrombinary(boundary,[0,0,0])
    tilelist=[(1,1),(1,2),(2,1)]
    NX=len(state[0])
    NY=len(state)
    sq32=np.sqrt(3)/2
    ax.set_xlim(-1,NX+1)
    ax.set_ylim(-sq32,NY*sq32)
    ax.set_aspect("equal")
    
    
    for i in range(NX):
        for j in range(NY):
            if state[i][j]==1:
                hexagon=mpatches.RegularPolygon((j+((i+1)%2)/2,(NY-1)*sq32-i*sq32),6,radius=0.5,color="black")
                ax.add_patch(hexagon)
            if (i,j) in tilelist:
                hexagon=mpatches.RegularPolygon((j+((i+1)%2)/2,(NY-1)*sq32-i*sq32),6,radius=0.5,color="red")
                ax.add_patch(hexagon)
    ax.set_title([tiles[i] for i in range(8) if cleanset[i]!=0], fontsize=10)
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    
    # Hide X and Y axes tick marks
    ax.set_xticks([])
    ax.set_yticks([])

        
    
    
    