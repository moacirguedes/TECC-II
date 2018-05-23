import matplotlib.pyplot as plt
plt.plot([1,2], [1,4], 'ro', label = "picles")
plt.plot([3,4], [9,16], 'b*', label = "batat")
plt.axis([0, 6, 0, 20])
plt.legend(loc=2)
plt.show()