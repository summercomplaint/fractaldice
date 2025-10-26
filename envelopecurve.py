import numpy as np
import matplotlib.pyplot as plt
import pickle

plt.rcParams['figure.dpi'] = 250

with open('3sided', 'rb') as f:
    outcomematrix=pickle.load(f)
scale=200
rolls=300
    
outs=[[],[],[]] 

for row in outcomematrix:
    mods=[[],[],[]]
    
    for i in range(len(row)):
        mods[i%3].append(row[i])
    
    for j in range(3):
        outs[j].append(mods[j])
xs=range(1,int(rolls/3))
ys=[10*scale/x for x in xs]
#ys=[scale*0.9*np.arctan(x/3)/np.pi+scale/2 for x in xs]
#ys2=[-scale*0.9*np.arctan(x/3)/np.pi+scale/2 for x in xs]
for j in range(3):
    plt.title(f'mod={j},scale={scale},rolls={rolls}')
    plt.imshow(outs[j])
    plt.scatter(xs,ys,s=2)
    #plt.scatter(xs,ys2,s=2)
    plt.show()  
    plt.clf()



