# library & dataset
from matplotlib import pyplot as plt
import numpy as np
 
# create data
x = np.random.rand(15)
y = x+np.random.rand(15)
z = x+np.random.rand(15)
z=z*z
 
# Use it with a call in cmap
#plt.scatter(x, y, s=z*2000, c=x, cmap="BuPu", alpha=0.4, edgecolors="grey", linewidth=2)
 
# You can reverse it:
plt.scatter(x, y, s=z*2000, c=x, cmap="BuPu_r", alpha=0.4, edgecolors="grey", linewidth=2, label="treco")
 
# OTHER: viridis / inferno / plasma / magma
#plt.scatter(x, y, s=z*2000, c=x, cmap="plasma", alpha=0.4, edgecolors="grey", linewidth=2)
plt.legend(loc=2)
plt.show()