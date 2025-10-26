import numpy as np
import matplotlib.pyplot as plt
import pickle

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

    probsset=set()
    
    
    for boundary in boundaries:
        weights=[]
        for tile in tiles:
            state=statefrombinary(boundary,tile)
            vcount=vertexcount(state)
            energy=sum([params[i]*vcount[i] for i in range(4)])
            weights.append(np.exp(-beta*energy))
            
        norm=sum(weights)
        
        probs=[np.round(weight/norm,2) for weight in weights]
        
        
        probsset.add(str(probs))
    cleanset=[el.replace("]","").replace("[","").replace(" ","").split(",") for el in probsset]
    cleanset=[[float(el) for el in arr] for arr in cleanset]
    return cleanset
 
def vardistance(probs1,probs2):
    return 0.5*sum([np.abs(probs1[i]-probs2[i]) for i in range(len(probs1))])

def maxvardistance(probslist):
    varslist=[]
    for probs1 in probslist:
        for probs2 in probslist:
            var=vardistance(probs1,probs2)
            varslist.append(var)
            
    return(max(varslist))

#exampleset=probsfromparams(10,[0,0,0.5,1])

#print(exampleset)

#print(maxvardistance(exampleset))


ens=np.linspace(0,1,10)

maxvars=[]

for en in ens:
    probset=probsfromparams(10,[0,0,en,1-en])
    maxvars.append(maxvardistance(probset))
    
plt.scatter(ens,maxvars)
    
    

        
    
    
    