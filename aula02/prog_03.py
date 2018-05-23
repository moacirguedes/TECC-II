# library
import numpy as np
import matplotlib.pyplot as plt
 
x=range(1,6)
y1=[1,4,6,8,9]
y2=[2,2,7,10,12]
y3=[2,8,5,10,6]
 
# Basic stacked area chart.
plt.stackplot(x, y1, y2, y3, labels=['A','B','C'])

#plt.legend(loc='upper left')
#plt.legend(loc=1)
plt.legend(loc=2)
#plt.legend(loc=3)
#plt.legend(loc=4)

plt.show()