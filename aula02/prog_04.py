import pylab as plt

x = 200 + 25*plt.randn(1000)
y = 150 + 25*plt.randn(1000)
plt.hist([x, y], label = ["cove","batata"])

plt.legend(loc=2)
plt.show()