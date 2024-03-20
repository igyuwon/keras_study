import numpy as np

a = np.array([[1,2,3,4,5],[11,12,13,14,15]],dtype = np.float32)
b = np.array([1,2,3,4,5])

b = a.astype(np.int32)
print(a)
print(b)

#print(a.shape) #(2,5)
#print(b.shape) #(5,)

#print(a.ndim)
#print(a.dtype)
#print(a.size)
#print(a)