import numpy as np

a = np.zeros((2,3,4))
b = np.ones_like(a)
c = np.empty((2,3))
d = np.full((2,3),0.5)
e = d.reshape((6,))

print(a)
print(b)
print(c)
print(d)
print(e)