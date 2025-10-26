import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pickle
plt.rcParams['figure.dpi'] = 600

with open('trinarimage', 'rb') as f:
    trinars=pickle.load(f)

plt.rcParams.update({'font.size': 6})
axis=np.arange(-int(1/3),int(1),1,dtype=int)

coinscale=600

halfaxis=np.arange(-int(1),0,1,dtype=int)

fig, ax = plt.subplots()

outs=ax.imshow(trinars, cmap="Greys",aspect="equal", origin="lower")

plt.title("Trinary Representation of Outcomes for $\Delta=\{1,x,y,-1-x-y\}$", fontsize=8)
#plt.plot([0,coinscale/3,4*coinscale/3,0],[2*coinscale/3,coinscale,0,2*coinscale/3],color="red",label="Fundamental Domain",linewidth=0.5)

t=plt.Polygon([[0,2*coinscale/3],[coinscale/3,coinscale],[4*coinscale/3,0],[0,2*coinscale/3]], edgecolor="red",facecolor="none",label="Fundamental Domain")
plt.gca().add_patch(t)

plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.xlim([0,4*coinscale/3])
plt.ylim([0,coinscale])
plt.xticks(ticks=np.arange(0,int(4*coinscale/3),int(np.ceil(coinscale/6))), labels=[np.round(x,2) for x in np.arange(-1/3,1, 1/6)])
plt.yticks(ticks=np.arange(0,coinscale,int(np.ceil(coinscale/6))), labels=[np.round(x,2) for x in np.arange(-1,0, 1/6)])

cbar=fig.colorbar(outs, shrink=0.9, anchor=(-0.3,0.5), ticks=[0,15,30])
cbar.ax.set_yticklabels(["[0,0,...]", "[1,1,...]","[2,2,...]" ],rotation=-90, verticalalignment="center")