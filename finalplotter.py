import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle
import matplotlib.patches as mpatches

plt.rcParams['figure.dpi'] = 600

with open('19throll', 'rb') as f:
    trinars=pickle.load(f)

plt.rcParams.update({'font.size': 6})
axis=np.arange(-int(1/3),int(1),1,dtype=int)

coinscale=600

halfaxis=np.arange(-int(1),0,1,dtype=int)

fig, ax = plt.subplots()

outs=ax.imshow(trinars, cmap="Greys",aspect="equal", origin="lower")

plt.title("Dominance relations after the 19th roll for $\Delta=\{1,x,y,-1-x-y\}$", fontsize=8)
#plt.plot([0,coinscale/3,4*coinscale/3,0],[2*coinscale/3,coinscale,0,2*coinscale/3],color="red",label="Fundamental Domain",linewidth=0.5)

t=plt.Polygon([[0,2*coinscale/3],[coinscale/3,coinscale],[4*coinscale/3,0],[0,2*coinscale/3]], edgecolor="red",facecolor="none",label="Fundamental Domain")


plt.gca().add_patch(t)

red_patch = mpatches.Patch(color='black', label='$P(\Delta[19]>0)>P(\Delta[19]<0)$')
green_patch = mpatches.Patch(color='grey', label='$P(\Delta[19]>0)=P(\Delta[19]<0)$')

blue_patch = mpatches.Patch(color="white",linewidth=0.5, label='$P(\Delta[19]>0)<P(\Delta[19]<0)$')

plt.legend(handles=[red_patch, green_patch, blue_patch,t], fontsize=6)

plt.xlabel("x")
plt.ylabel("y")
plt.xlim([0,4*coinscale/3])
plt.ylim([0,coinscale])
plt.xticks(ticks=np.arange(0,int(4*coinscale/3),int(np.ceil(coinscale/6))), labels=[np.round(x,2) for x in np.arange(-1/3,1, 1/6)])
plt.yticks(ticks=np.arange(0,coinscale,int(np.ceil(coinscale/6))), labels=[np.round(x,2) for x in np.arange(-1,0, 1/6)])

