import numpy as np

a = np.arange(0, 30).reshape((2, 3, 5))
print(a)
'''
#print(a.max())
#print(a.max(axis = 0))
#print(a.max(axis = 1))
#print(a.max(axis = 2))
'''
print(a.mean())
m = a.maen(axis=1)
s = a.std(axis=1)

ab = (a[:,0]-m)/s
print(ab)
