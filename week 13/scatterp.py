import matplotlib.pyplot as plt
import random
import numpy as np

n = 100
x = np.random.random(n)
y = np.random.random(n)

#x = [1,2,3,4]
#y=[4,2,1,3]
s = [(50 * random.random()) ** 2 for _ in range(len(x))]
c = [random.random() for _ in range(len(x))]
a = [random.random() for _ in range(len(x))]

plt.scatter(x, y, s=s, c=c, alpha=a, cmap = 'Spectral')
plt.colorbar()
plt.show()